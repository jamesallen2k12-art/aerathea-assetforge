from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
DESTINATION = "/Game/Aerathea/Props/Infernals/BalgorothCult/Sigils"
ASSET_NAME = "SM_INF_BalgorothSigil_A01"
ASSET_PATH = "{}/{}".format(DESTINATION, ASSET_NAME)
SOURCE = ROOT / "SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/SM_INF_BalgorothSigil_A01.fbx"
FBX_IMPORT_UNIFORM_SCALE = 0.01

TASK_ID = "AET-MA-20260628-029"
PACKAGE_DOC = "docs/assets/props/SM_INF_BalgorothSigil_A01/PRODUCTION_PACKAGE.md"
HANDOFF_DOC = "docs/assets/props/SM_INF_BalgorothSigil_A01/MODELING_HANDOFF.md"


MATERIAL_INSTANCE_PATHS = {
    "MI_INF_CultStone_Basalt_A01": "/Game/Aerathea/Materials/Instances/MI_INF_CultStone_Basalt_A01",
    "MI_INF_CultStone_ScorchedRed_A01": "/Game/Aerathea/Materials/Instances/MI_INF_CultStone_ScorchedRed_A01",
    "MI_INF_CultStone_ObsidianInset_A01": "/Game/Aerathea/Materials/Instances/MI_INF_CultStone_ObsidianInset_A01",
    "MI_INF_CultStone_EmissiveChannel_A01": "/Game/Aerathea/Materials/Instances/MI_INF_CultStone_EmissiveChannel_A01",
}


SOCKET_SPECS = [
    ("vfx_sigil_core", unreal.Vector(0.0, -32.0, 150.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_eye_core", unreal.Vector(0.0, -36.0, 150.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_rejected_break", unreal.Vector(96.0, -36.0, 150.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("snap_floor_center", unreal.Vector(0.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
]


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def load_material_instances():
    materials = {}
    for material_name, asset_path in MATERIAL_INSTANCE_PATHS.items():
        material = unreal.load_asset(asset_path)
        if material is None:
            raise RuntimeError("Required material instance failed to load: {}".format(asset_path))
        materials[material_name] = material
    return materials


def material_slots(mesh):
    for prop in ("static_materials", "materials"):
        try:
            return list(mesh.get_editor_property(prop))
        except Exception:
            continue
    return []


def assign_project_materials(mesh, project_materials):
    slots = material_slots(mesh)
    assigned = 0
    for index, slot in enumerate(slots):
        slot_name = str(slot.get_editor_property("material_slot_name"))
        current = slot.get_editor_property("material_interface")
        current_name = current.get_name() if current is not None else slot_name
        material = project_materials.get(slot_name) or project_materials.get(current_name)
        if material is None:
            continue
        mesh.set_material(index, material)
        assigned += 1
    if assigned < len(project_materials):
        unreal.log_warning(
            "Assigned {} Balgoroth sigil materials; expected {}. Slot names: {}".format(
                assigned,
                len(project_materials),
                ", ".join(str(slot.get_editor_property("material_slot_name")) for slot in slots),
            )
        )
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def import_static_mesh():
    if not SOURCE.exists():
        raise RuntimeError("Missing source FBX: {}".format(SOURCE))
    ensure_directory(DESTINATION)

    fbx_ui = unreal.FbxImportUI()
    safe_set(fbx_ui, "import_mesh", True)
    safe_set(fbx_ui, "import_as_skeletal", False)
    safe_set(fbx_ui, "import_materials", False)
    safe_set(fbx_ui, "import_textures", False)
    safe_set(fbx_ui, "import_uniform_scale", FBX_IMPORT_UNIFORM_SCALE)
    static_data = fbx_ui.static_mesh_import_data
    safe_set(static_data, "combine_meshes", True)
    safe_set(static_data, "auto_generate_collision", False)
    safe_set(static_data, "generate_lightmap_u_vs", True)
    safe_set(static_data, "remove_degenerates", True)
    safe_set(static_data, "one_convex_hull_per_ucx", False)
    safe_set(static_data, "import_uniform_scale", FBX_IMPORT_UNIFORM_SCALE)

    task = unreal.AssetImportTask()
    task.set_editor_property("filename", str(SOURCE))
    task.set_editor_property("destination_path", DESTINATION)
    task.set_editor_property("destination_name", ASSET_NAME)
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)
    task.set_editor_property("options", fbx_ui)

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    mesh = unreal.load_asset(ASSET_PATH)
    if mesh is None:
        raise RuntimeError("Import did not produce expected static mesh: {}".format(ASSET_PATH))
    safe_set(mesh, "light_map_resolution", 128)
    unreal.EditorAssetLibrary.save_asset(ASSET_PATH)
    return mesh


def ensure_review_lods_static(mesh, target_lods=4):
    options = unreal.EditorScriptingMeshReductionOptions()
    safe_set(options, "auto_compute_lod_screen_size", False)
    settings = []
    for percent, screen_size in ((1.0, 1.0), (0.58, 0.55), (0.32, 0.28), (0.14, 0.12)):
        setting = unreal.EditorScriptingMeshReductionSettings()
        safe_set(setting, "percent_triangles", percent)
        safe_set(setting, "screen_size", screen_size)
        settings.append(setting)
    safe_set(options, "reduction_settings", settings)
    unreal.EditorStaticMeshLibrary.set_lods(mesh, options)
    count = unreal.EditorStaticMeshLibrary.get_lod_count(mesh)
    if count < target_lods:
        raise RuntimeError("{} has {} static LODs after reduction, expected {}".format(mesh.get_name(), count, target_lods))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def remove_static_mesh_socket(mesh, name):
    finder = getattr(mesh, "find_socket", None)
    remover = getattr(mesh, "remove_socket", None)
    if not callable(finder) or not callable(remover):
        return
    try:
        existing = finder(unreal.Name(name))
    except Exception:
        existing = None
    if existing is None:
        return
    try:
        remover(existing)
    except TypeError:
        remover(unreal.Name(name))


def ensure_static_mesh_sockets(mesh):
    for name, _location, _rotation in SOCKET_SPECS:
        remove_static_mesh_socket(mesh, name)

    for name, location, rotation in SOCKET_SPECS:
        socket = unreal.new_object(unreal.StaticMeshSocket, outer=mesh)
        socket.set_editor_property("socket_name", unreal.Name(name))
        socket.set_editor_property("relative_location", location)
        socket.set_editor_property("relative_rotation", rotation)
        socket.set_editor_property("relative_scale", unreal.Vector(1.0, 1.0, 1.0))
        add_socket = getattr(mesh, "add_socket", None)
        if not callable(add_socket):
            raise RuntimeError("StaticMesh.add_socket is not available for {}".format(mesh.get_name()))
        add_socket(socket)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def apply_mesh_metadata(mesh):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag is unavailable; skipped sigil metadata")
        return
    metadata = {
        "Aerathea.StaticMesh.Package": "SM_INF_BalgorothSigil_A01",
        "Aerathea.StaticMesh.Task": TASK_ID,
        "Aerathea.StaticMesh.Status": "first_pass_import_validated_target",
        "Aerathea.StaticMesh.PackageDoc": PACKAGE_DOC,
        "Aerathea.StaticMesh.HandoffDoc": HANDOFF_DOC,
        "Aerathea.StaticMesh.StartupPlaced": "false",
        "Aerathea.StaticMesh.FinalArtAuthored": "false",
    }
    for tag, value in metadata.items():
        setter(mesh, tag, str(value))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def main():
    materials = load_material_instances()
    mesh = import_static_mesh()
    assign_project_materials(mesh, materials)
    ensure_review_lods_static(mesh)
    ensure_static_mesh_sockets(mesh)
    apply_mesh_metadata(mesh)
    unreal.EditorAssetLibrary.save_directory(DESTINATION, only_if_is_dirty=False, recursive=True)
    unreal.log("Aerathea Infernal Balgoroth sigil import complete.")


main()
