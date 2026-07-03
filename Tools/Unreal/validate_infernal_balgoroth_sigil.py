from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/SM_INF_BalgorothSigil_A01.fbx"
MESH_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/Sigils/SM_INF_BalgorothSigil_A01"

REQUIRED_MATERIALS = [
    "/Game/Aerathea/Materials/Instances/MI_INF_CultStone_Basalt_A01",
    "/Game/Aerathea/Materials/Instances/MI_INF_CultStone_ScorchedRed_A01",
    "/Game/Aerathea/Materials/Instances/MI_INF_CultStone_ObsidianInset_A01",
    "/Game/Aerathea/Materials/Instances/MI_INF_CultStone_EmissiveChannel_A01",
]

REQUIRED_SOCKETS = [
    "vfx_sigil_core",
    "vfx_eye_core",
    "vfx_rejected_break",
    "snap_floor_center",
]

COMMON_METADATA = {
    "Aerathea.StaticMesh.Package": "SM_INF_BalgorothSigil_A01",
    "Aerathea.StaticMesh.Task": "AET-MA-20260628-029",
    "Aerathea.StaticMesh.Status": "first_pass_import_validated_target",
    "Aerathea.StaticMesh.StartupPlaced": "false",
    "Aerathea.StaticMesh.FinalArtAuthored": "false",
}


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def metadata_value(failures, asset, tag):
    getter = getattr(unreal.EditorAssetLibrary, "get_metadata_tag", None)
    if not callable(getter):
        failures.append("EditorAssetLibrary.get_metadata_tag is unavailable; cannot validate sigil metadata")
        return None
    try:
        value = getter(asset, tag)
    except Exception as exc:
        failures.append("{} metadata {} unreadable ({})".format(asset.get_path_name(), tag, exc))
        return None
    if value is None:
        return ""
    return str(value)


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
    loaded_materials = []
    for material_path in REQUIRED_MATERIALS:
        material = unreal.load_asset(material_path)
        if material is None:
            failures.append("{} failed to load".format(material_path))
            continue
        loaded_materials.append(material_path)

    assigned = set()
    for slot in material_slots(mesh):
        material = slot.get_editor_property("material_interface")
        if material is not None:
            assigned.add(asset_path_without_object(material))

    missing_assignments = [material_path for material_path in loaded_materials if material_path not in assigned]
    if missing_assignments:
        failures.append("{} missing material assignments {}".format(MESH_PATH, ", ".join(missing_assignments)))
    if len(material_slots(mesh)) < 4:
        failures.append("{} has {} material slots, expected at least 4".format(MESH_PATH, len(material_slots(mesh))))


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
    if height < 260.0 or height > 380.0:
        failures.append("{} height {:.2f} cm is outside sigil envelope".format(MESH_PATH, height))
    if width < 280.0 or width > 430.0:
        failures.append("{} width {:.2f} cm is outside sigil envelope".format(MESH_PATH, width))
    if depth < 18.0 or depth > 60.0:
        failures.append("{} depth {:.2f} cm is outside sigil envelope".format(MESH_PATH, depth))


def validate_assets(failures):
    if not SOURCE.exists():
        failures.append("Missing source FBX {}".format(SOURCE))
    elif SOURCE.stat().st_size <= 0:
        failures.append("Source FBX is empty {}".format(SOURCE))

    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(MESH_PATH))
        return None

    if unreal.EditorStaticMeshLibrary.get_lod_count(mesh) < 4:
        failures.append("{} has fewer than 4 LODs".format(MESH_PATH))

    missing_sockets = [
        socket_name
        for socket_name in REQUIRED_SOCKETS
        if mesh.find_socket(unreal.Name(socket_name)) is None
    ]
    if missing_sockets:
        failures.append("{} missing sockets {}".format(MESH_PATH, ", ".join(missing_sockets)))

    validate_materials(failures, mesh)
    validate_metadata(failures, mesh)
    return mesh


def main():
    failures = []
    measurements = []
    mesh = validate_assets(failures)
    if mesh is not None:
        validate_mesh_bounds(failures, mesh, measurements)
    if failures:
        raise RuntimeError("Infernal BalgorothSigil validation failed: {}".format("; ".join(failures)))

    if measurements and measurements[0][0] != "unavailable":
        height, width, depth = measurements[0]
        print(
            "Infernal BalgorothSigil validation passed: {:.2f}h x {:.2f}w x {:.2f}d cm, 4 material lanes, {} sockets.".format(
                height,
                width,
                depth,
                len(REQUIRED_SOCKETS),
            )
        )
    else:
        print(
            "Infernal BalgorothSigil validation passed: 4 material lanes, {} sockets, static bounds API unavailable.".format(
                len(REQUIRED_SOCKETS),
            )
        )


if __name__ == "__main__":
    main()
