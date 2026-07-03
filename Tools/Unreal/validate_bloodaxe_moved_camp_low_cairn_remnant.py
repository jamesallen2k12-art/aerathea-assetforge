from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.fbx"
MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
PARENT_MATERIAL_PATH = "/Game/Aerathea/Materials/Giants/BloodAxe/M_GIA_BloodAxeMovedCampVertexColor_Blockout_A01"

COMMON_METADATA = {
    "Aerathea.StaticMesh.Package": "SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01",
    "Aerathea.StaticMesh.Task": "AET-MA-20260629-574",
    "Aerathea.StaticMesh.Status": "material_value_pass_review_target",
    "Aerathea.StaticMesh.StartupPlaced": "startup_review_actor",
    "Aerathea.StaticMesh.StartupActor": "AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01",
    "Aerathea.StaticMesh.VisualReview": "requested_changes_material_value_pass_pending_approval_not_final_art",
    "Aerathea.StaticMesh.FinalArtAuthored": "false",
    "Aerathea.StaticMesh.CollisionPolicy": "disabled_no_correctness_claim",
    "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
    "Aerathea.StaticMesh.VertexColorMaterial": "true",
    "Aerathea.StaticMesh.MaterialValueRevision": "AET-MA-20260629-583_requested_changes",
    "Aerathea.StaticMesh.MaterialValueControl": "standard_color_channel_vertex_material_multiplier_v03",
}


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def metadata_value(failures, asset, tag):
    getter = getattr(unreal.EditorAssetLibrary, "get_metadata_tag", None)
    if not callable(getter):
        failures.append("EditorAssetLibrary.get_metadata_tag is unavailable; cannot validate Blood Axe metadata")
        return None
    try:
        value = getter(asset, tag)
    except Exception as exc:
        failures.append("{} metadata {} unreadable ({})".format(asset.get_path_name(), tag, exc))
        return None
    if value is None:
        return ""
    return str(value)


def validate_source_fbx(failures):
    if not SOURCE.exists():
        failures.append("Missing source FBX {}".format(SOURCE))
        return
    if SOURCE.stat().st_size <= 0:
        failures.append("Source FBX is empty {}".format(SOURCE))
        return
    data = SOURCE.read_bytes()
    if b"LayerElementColor" not in data:
        failures.append("{} does not contain FBX LayerElementColor vertex-color data".format(SOURCE))


def validate_metadata(failures, mesh):
    for tag, expected in COMMON_METADATA.items():
        value = metadata_value(failures, mesh, tag)
        if value is None:
            continue
        if value != expected:
            failures.append("{} metadata {} is {!r}, expected {!r}".format(mesh.get_path_name(), tag, value, expected))


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def validate_materials(failures, mesh):
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
        failures.append("{} has {} material slots, expected exactly 1".format(MESH_PATH, len(slots)))
        return

    material = slots[0].get_editor_property("material_interface")
    if material is None:
        failures.append("{} material slot 0 is unassigned".format(MESH_PATH))
    elif asset_path_without_object(material) != MATERIAL_INSTANCE_PATH:
        failures.append("{} material slot 0 is {}, expected {}".format(MESH_PATH, material.get_path_name(), MATERIAL_INSTANCE_PATH))


def validate_no_sockets(failures, mesh):
    try:
        sockets = list(mesh.get_editor_property("sockets"))
    except Exception:
        sockets = []
    if sockets:
        failures.append("{} has {} sockets, expected none".format(MESH_PATH, len(sockets)))


def validate_mesh_bounds(failures, mesh, measurements):
    getter = getattr(mesh, "get_bounds", None)
    if not callable(getter):
        measurements.append(("unavailable", "unavailable", "unavailable"))
        return
    try:
        bounds = getter()
        extent = bounds.get_editor_property("box_extent")
    except Exception:
        measurements.append(("unavailable", "unavailable", "unavailable"))
        return

    width = extent.x * 2.0
    depth = extent.y * 2.0
    height = extent.z * 2.0
    measurements.append((height, width, depth))

    if height < 118.0 or height > 145.0:
        failures.append("{} height {:.2f} cm is outside low-cairn remnant envelope".format(MESH_PATH, height))
    if max(width, depth) < 300.0 or max(width, depth) > 360.0:
        failures.append("{} max horizontal bounds {:.2f} cm is outside expected 330 cm envelope".format(MESH_PATH, max(width, depth)))
    if min(width, depth) < 210.0 or min(width, depth) > 270.0:
        failures.append("{} min horizontal bounds {:.2f} cm is outside expected 236 cm envelope".format(MESH_PATH, min(width, depth)))


def validate_assets(failures):
    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(MESH_PATH))
        return None

    if unreal.EditorStaticMeshLibrary.get_lod_count(mesh) < 4:
        failures.append("{} has fewer than 4 review LODs".format(MESH_PATH))

    validate_materials(failures, mesh)
    validate_metadata(failures, mesh)
    validate_no_sockets(failures, mesh)
    return mesh


def main():
    failures = []
    measurements = []
    validate_source_fbx(failures)
    mesh = validate_assets(failures)
    if mesh is not None:
        validate_mesh_bounds(failures, mesh, measurements)
    if failures:
        raise RuntimeError("Blood Axe low cairn remnant validation failed: {}".format("; ".join(failures)))

    if measurements and measurements[0][0] != "unavailable":
        height, width, depth = measurements[0]
        print(
            "Blood Axe low cairn remnant validation passed: {:.2f}h x {:.2f}w x {:.2f}d cm, 4 review LODs, 1 vertex-color material, no sockets, startup review metadata present, final art not authored.".format(
                height,
                width,
                depth,
            )
        )
    else:
        print("Blood Axe low cairn remnant validation passed: 4 review LODs, 1 vertex-color material, no sockets, startup review metadata present, final art not authored.")


if __name__ == "__main__":
    main()
