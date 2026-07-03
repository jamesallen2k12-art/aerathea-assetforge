from pathlib import Path
import sys

import unreal


sys.path.append(str(Path(__file__).resolve().parent))
from bloodaxe_cairn_variant_batch_config import (  # noqa: E402
    ASSETS,
    IMPORT_PACKET_DOC,
    KIT_ID,
    MATERIAL_INSTANCE_PATH,
    PACKAGE_DOC,
    PARENT_MATERIAL_PATH,
    VISUAL_CANON_SOURCE,
    import_source_path,
    lod_path,
)


COMMON_METADATA = {
    "Aerathea.StaticMesh.SourceStatus": "dcc_game_ready_candidate",
    "Aerathea.StaticMesh.Package": KIT_ID,
    "Aerathea.StaticMesh.PackageDoc": PACKAGE_DOC,
    "Aerathea.StaticMesh.ImportPacket": IMPORT_PACKET_DOC,
    "Aerathea.StaticMesh.VisualCanonSource": VISUAL_CANON_SOURCE,
    "Aerathea.StaticMesh.CollisionPolicy": "broad_simple_static_prop_collision",
    "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
    "Aerathea.StaticMesh.FinalArtAuthored": "false",
    "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_review",
    "Aerathea.StaticMesh.MaterialMode": "shared_vertex_color_review_material_no_final_textures",
    "Aerathea.StaticMesh.FinalTextureSetAuthored": "false",
    "Aerathea.StaticMesh.LODSource": "authored_fbx_lod1_lod2_lod3",
}


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def metadata_value(failures, asset, tag):
    getter = getattr(unreal.EditorAssetLibrary, "get_metadata_tag", None)
    if not callable(getter):
        failures.append("EditorAssetLibrary.get_metadata_tag is unavailable")
        return None
    try:
        value = getter(asset, tag)
    except Exception as exc:
        failures.append("{} metadata {} unreadable ({})".format(asset.get_path_name(), tag, exc))
        return None
    return "" if value is None else str(value)


def set_metadata(mesh, tag, value):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if callable(setter):
        setter(mesh, tag, str(value))


def validate_source_files(failures, asset):
    source = import_source_path(asset)
    if not source.exists():
        failures.append("Missing visual-only Unreal import FBX {}".format(source))
        return
    if source.stat().st_size <= 0:
        failures.append("Visual-only Unreal import FBX is empty {}".format(source))
        return
    data = source.read_bytes()
    if b"LayerElementColor" not in data:
        failures.append("{} does not contain FBX LayerElementColor vertex-color data".format(source))
    if b"UCX_" in data:
        failures.append("{} still contains UCX collision proxy objects; expected visual-only import source".format(source))
    for lod_index in (1, 2, 3):
        lod_source = lod_path(asset, lod_index)
        if not lod_source.exists():
            failures.append("Missing authored LOD{} FBX {}".format(lod_index, lod_source))
        elif lod_source.stat().st_size <= 0:
            failures.append("Authored LOD{} FBX is empty {}".format(lod_index, lod_source))


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def validate_materials(failures, asset, mesh):
    parent = unreal.load_asset(PARENT_MATERIAL_PATH)
    if parent is None:
        failures.append("{} failed to load".format(PARENT_MATERIAL_PATH))

    instance = unreal.load_asset(MATERIAL_INSTANCE_PATH)
    if instance is None:
        failures.append("{} failed to load".format(MATERIAL_INSTANCE_PATH))
    else:
        try:
            actual_parent = instance.get_editor_property("parent")
        except Exception:
            actual_parent = None
        if actual_parent is None:
            failures.append("{} has no parent material".format(MATERIAL_INSTANCE_PATH))
        elif asset_path_without_object(actual_parent) != PARENT_MATERIAL_PATH:
            failures.append("{} parent is {}, expected {}".format(MATERIAL_INSTANCE_PATH, actual_parent.get_path_name(), PARENT_MATERIAL_PATH))

    slots = material_slots(mesh)
    if len(slots) != 1:
        failures.append("{} has {} material slots, expected exactly 1".format(asset["unreal_path"], len(slots)))
        return
    material = slots[0].get_editor_property("material_interface")
    if material is None:
        failures.append("{} material slot 0 is unassigned".format(asset["unreal_path"]))
    elif asset_path_without_object(material) != MATERIAL_INSTANCE_PATH:
        failures.append("{} material slot 0 is {}, expected {}".format(asset["unreal_path"], material.get_path_name(), MATERIAL_INSTANCE_PATH))


def lod_count(mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        return int(subsystem.get_lod_count(mesh))
    return int(unreal.EditorStaticMeshLibrary.get_lod_count(mesh))


def collision_counts(mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        return int(subsystem.get_simple_collision_count(mesh)), int(subsystem.get_convex_collision_count(mesh))
    counter = getattr(unreal.EditorStaticMeshLibrary, "get_simple_collision_count", None)
    if callable(counter):
        return int(counter(mesh)), 0
    return 0, 0


def validate_mesh_bounds(failures, asset, mesh, measurements):
    getter = getattr(mesh, "get_bounds", None)
    if not callable(getter):
        failures.append("{} bounds are unreadable".format(asset["unreal_path"]))
        return
    try:
        bounds = getter()
        extent = bounds.get_editor_property("box_extent")
    except Exception as exc:
        failures.append("{} bounds are unreadable ({})".format(asset["unreal_path"], exc))
        return

    width = extent.x * 2.0
    depth = extent.y * 2.0
    height = extent.z * 2.0
    max_horizontal = max(width, depth)
    min_horizontal = min(width, depth)
    measurements.append((asset["name"], height, width, depth))

    if height < 35.0 or height > 260.0:
        failures.append("{} height {:.2f} cm outside cairn variant envelope".format(asset["unreal_path"], height))
    if max_horizontal < 45.0 or max_horizontal > 700.0:
        failures.append("{} max horizontal bounds {:.2f} cm outside cairn variant envelope".format(asset["unreal_path"], max_horizontal))
    if min_horizontal < 20.0 or min_horizontal > 500.0:
        failures.append("{} min horizontal bounds {:.2f} cm outside cairn variant envelope".format(asset["unreal_path"], min_horizontal))


def validate_metadata(failures, asset, mesh):
    status = metadata_value(failures, mesh, "Aerathea.StaticMesh.Status")
    if status not in ("unreal_import_candidate_pending_validation", "unreal_import_candidate"):
        failures.append("{} metadata Aerathea.StaticMesh.Status is {!r}".format(asset["unreal_path"], status))
    for tag, expected in COMMON_METADATA.items():
        value = metadata_value(failures, mesh, tag)
        if value is None:
            continue
        if value != expected:
            failures.append("{} metadata {} is {!r}, expected {!r}".format(asset["unreal_path"], tag, value, expected))
    expected_collision = metadata_value(failures, mesh, "Aerathea.StaticMesh.ExpectedCollisionProxyCount")
    if expected_collision != str(asset["collision_proxies"]):
        failures.append(
            "{} metadata ExpectedCollisionProxyCount is {!r}, expected {!r}".format(
                asset["unreal_path"],
                expected_collision,
                str(asset["collision_proxies"]),
            )
        )


def validate_no_sockets(failures, asset, mesh):
    try:
        sockets = list(mesh.get_editor_property("sockets"))
    except Exception:
        sockets = []
    if sockets:
        failures.append("{} has {} sockets, expected none".format(asset["unreal_path"], len(sockets)))


def validate_asset(failures, measurements, asset):
    validate_source_files(failures, asset)
    mesh = unreal.load_asset(asset["unreal_path"])
    if mesh is None:
        failures.append("{} failed to load".format(asset["unreal_path"]))
        return

    count = lod_count(mesh)
    if count != 4:
        failures.append("{} has {} LODs, expected 4".format(asset["unreal_path"], count))

    simple_count, convex_count = collision_counts(mesh)
    if max(simple_count, convex_count) < 1:
        failures.append("{} has no simple/convex collision".format(asset["unreal_path"]))
    elif max(simple_count, convex_count) < int(asset["collision_proxies"]):
        unreal.log_warning(
            "{} collision count simple={} convex={} is below DCC proxy count {}; accepted as broad simple fallback.".format(
                asset["name"],
                simple_count,
                convex_count,
                asset["collision_proxies"],
            )
        )

    validate_materials(failures, asset, mesh)
    validate_mesh_bounds(failures, asset, mesh, measurements)
    validate_metadata(failures, asset, mesh)
    validate_no_sockets(failures, asset, mesh)


def mark_validated(asset):
    mesh = unreal.load_asset(asset["unreal_path"])
    if mesh is None:
        return
    set_metadata(mesh, "Aerathea.StaticMesh.Status", "unreal_import_candidate")
    set_metadata(mesh, "Aerathea.StaticMesh.UnrealImportTested", "true")
    set_metadata(mesh, "Aerathea.StaticMesh.ImportValidation", "passed_2026-07-03")
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def main():
    failures = []
    measurements = []
    for asset in ASSETS:
        validate_asset(failures, measurements, asset)

    if failures:
        for failure in failures:
            unreal.log_error(failure)
        raise RuntimeError("Blood Axe cairn variant batch validation failed with {} issue(s)".format(len(failures)))

    for asset in ASSETS:
        mark_validated(asset)

    for name, height, width, depth in measurements:
        unreal.log("VALIDATED {} bounds {:.2f}h x {:.2f}w x {:.2f}d cm".format(name, height, width, depth))
    unreal.log("Blood Axe cairn variant batch validation passed: {} Unreal import candidates, 4 authored LODs each, shared vertex-color material, simple collision present, no gameplay behavior.".format(len(ASSETS)))


if __name__ == "__main__":
    main()
