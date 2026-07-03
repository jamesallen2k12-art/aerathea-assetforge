from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MATERIAL_PATH = "/Game/Aerathea/Materials/Infernals/WorthinessAltar"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
DESTINATION = "/Game/Aerathea/Props/Infernals/BalgorothCult"
ASSET_NAME = "SM_INF_WorthinessAltar_A01"
SOURCE = ROOT / "SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01/SM_INF_WorthinessAltar_A01.fbx"
FBX_IMPORT_UNIFORM_SCALE = 0.01
NEXT_SLICE_TAG = "AET_NEXT_SLICE"
INF_CULT_TAG = "AET_INFERNAL_CULT_REVIEW"
ALTAR_ACTOR_LABEL = "AET_PROD_INF_WorthinessAltar_A01"
FLOOR_ACTOR_LABEL = "AET_PROD_INF_CullingTrialFloor_A01"


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def configure_static_material_usage(material):
    usage = getattr(unreal.MaterialUsage, "MATUSAGE_STATIC_MESH", None)
    if usage is not None:
        try:
            unreal.MaterialEditingLibrary.set_material_usage(material, usage)
        except Exception as exc:
            unreal.log_warning("Could not set static material usage: {}".format(exc))
    safe_set(material, "used_with_static_mesh", True)
    unreal.MaterialEditingLibrary.recompile_material(material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)


def color_material(name, color, roughness=0.84, metallic=0.0, emissive=None):
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, name)
    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        material = unreal.load_asset(asset_path)
        configure_static_material_usage(material)
        return material

    material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name=name,
        package_path=MATERIAL_PATH,
        asset_class=unreal.Material,
        factory=unreal.MaterialFactoryNew(),
    )
    if material is None:
        raise RuntimeError("Failed to create material {}".format(asset_path))

    mat_lib = unreal.MaterialEditingLibrary
    base = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -420, -80)
    base.set_editor_property("constant", color)
    mat_lib.connect_material_property(base, "", unreal.MaterialProperty.MP_BASE_COLOR)

    rough = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 120)
    rough.set_editor_property("r", roughness)
    mat_lib.connect_material_property(rough, "", unreal.MaterialProperty.MP_ROUGHNESS)

    metal = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 260)
    metal.set_editor_property("r", metallic)
    mat_lib.connect_material_property(metal, "", unreal.MaterialProperty.MP_METALLIC)

    if emissive is not None:
        glow = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -420, 420)
        glow.set_editor_property("constant", emissive)
        mat_lib.connect_material_property(glow, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)

    configure_static_material_usage(material)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    return material


def ensure_materials():
    return {
        "M_INF_WorthinessAltar_CultStone_Blockout_A01": color_material(
            "M_INF_WorthinessAltar_CultStone_Blockout_A01",
            unreal.LinearColor(0.050, 0.052, 0.057, 1.0),
        ),
        "M_INF_WorthinessAltar_ScorchedStone_Blockout_A01": color_material(
            "M_INF_WorthinessAltar_ScorchedStone_Blockout_A01",
            unreal.LinearColor(0.22, 0.055, 0.038, 1.0),
        ),
        "M_INF_WorthinessAltar_ObsidianIron_Blockout_A01": color_material(
            "M_INF_WorthinessAltar_ObsidianIron_Blockout_A01",
            unreal.LinearColor(0.016, 0.015, 0.020, 1.0),
            roughness=0.62,
            metallic=0.42,
        ),
        "M_INF_WorthinessAltar_BoneHorn_Blockout_A01": color_material(
            "M_INF_WorthinessAltar_BoneHorn_Blockout_A01",
            unreal.LinearColor(0.57, 0.48, 0.34, 1.0),
            roughness=0.70,
        ),
        "M_INF_WorthinessAltar_BrandGlow_Blockout_A01": color_material(
            "M_INF_WorthinessAltar_BrandGlow_Blockout_A01",
            unreal.LinearColor(1.0, 0.17, 0.020, 1.0),
            roughness=0.25,
            emissive=unreal.LinearColor(3.0, 0.26, 0.025, 1.0),
        ),
    }


def material_instance_name(mesh_name, material_name):
    asset_name = mesh_name[3:] if mesh_name.startswith("SM_") else mesh_name
    semantic = material_name
    for prefix in ("M_INF_WorthinessAltar_", "M_INF_"):
        if semantic.startswith(prefix):
            semantic = semantic[len(prefix) :]
            break
    for suffix in ("_Blockout_A01", "_Handpainted_A01", "_A01"):
        if semantic.endswith(suffix):
            semantic = semantic[: -len(suffix)]
            break
    return "MI_{}_{}".format(asset_name, semantic)


def ensure_material_instance(name, parent_material):
    ensure_directory(MATERIAL_INSTANCE_PATH)
    asset_path = "{}/{}".format(MATERIAL_INSTANCE_PATH, name)
    instance = unreal.load_asset(asset_path)
    if instance is None:
        instance = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=name,
            package_path=MATERIAL_INSTANCE_PATH,
            asset_class=unreal.MaterialInstanceConstant,
            factory=unreal.MaterialInstanceConstantFactoryNew(),
        )
        if instance is None:
            raise RuntimeError("Failed to create material instance {}".format(asset_path))
    safe_set(instance, "parent", parent_material)
    unreal.EditorAssetLibrary.save_loaded_asset(instance)
    return instance


def material_slots(mesh):
    for prop in ("static_materials", "materials"):
        try:
            return list(mesh.get_editor_property(prop))
        except Exception:
            continue
    return []


def assign_project_materials(mesh, project_materials):
    slots = material_slots(mesh)
    for index, slot in enumerate(slots):
        slot_name = str(slot.get_editor_property("material_slot_name"))
        current = slot.get_editor_property("material_interface")
        current_name = current.get_name() if current is not None else slot_name
        base_material = project_materials.get(slot_name) or project_materials.get(current_name)
        if base_material is None:
            continue
        instance = ensure_material_instance(material_instance_name(mesh.get_name(), base_material.get_name()), base_material)
        mesh.set_material(index, instance)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log("Synced {} Infernal worthiness altar material slots for {}".format(len(slots), mesh.get_name()))


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
    asset_path = "{}/{}".format(DESTINATION, ASSET_NAME)
    mesh = unreal.load_asset(asset_path)
    if mesh is None:
        raise RuntimeError("Import did not produce expected static mesh: {}".format(asset_path))
    safe_set(mesh, "light_map_resolution", 128)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    unreal.log("Imported Infernal worthiness altar static mesh: {}".format(asset_path))
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
    unreal.log("Ensured {} static LODs for {}".format(count, mesh.get_name()))


def remove_static_mesh_socket(mesh, name):
    finder = getattr(mesh, "find_socket", None)
    remover = getattr(mesh, "remove_socket", None)
    if not callable(finder) or not callable(remover):
        return
    existing = None
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
    socket_specs = [
        ("snap_floor", unreal.Vector(0.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("snap_arch_back", unreal.Vector(0.0, -258.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("interact_front", unreal.Vector(0.0, 132.0, 102.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("stage_offering", unreal.Vector(0.0, -6.0, 126.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("vfx_altar_core", unreal.Vector(0.0, -6.0, 132.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("vfx_sacrifice_mark", unreal.Vector(0.0, 74.0, 108.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("vfx_brand_transfer", unreal.Vector(0.0, -146.0, 266.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("vfx_ring_link", unreal.Vector(0.0, 82.0, 106.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("vfx_rejected_gap", unreal.Vector(88.0, 72.0, 111.0), unreal.Rotator(0.0, 0.0, -32.0)),
    ]

    for name, _location, _rotation in socket_specs:
        remove_static_mesh_socket(mesh, name)

    for name, location, rotation in socket_specs:
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
    unreal.log("Ensured {} static mesh sockets for {}".format(len(socket_specs), mesh.get_name()))


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def tag_actor(actor):
    tags = list(actor.get_editor_property("tags"))
    for tag_name in (NEXT_SLICE_TAG, INF_CULT_TAG):
        tag = unreal.Name(tag_name)
        if tag not in tags:
            tags.append(tag)
    actor.set_editor_property("tags", tags)
    return actor


def retire_actor(actor):
    old_label = actor.get_actor_label()
    if old_label.startswith("AET_RETIRED_"):
        return
    actor.set_actor_label("AET_RETIRED_{}".format(old_label))
    try:
        actor.set_actor_hidden_in_game(True)
        actor.set_is_temporarily_hidden_in_editor(True)
        actor.set_actor_location(unreal.Vector(0, 0, -100000), False, True)
        actor.set_actor_scale3d(unreal.Vector(0.01, 0.01, 0.01))
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            component.set_visibility(False, True)
            component.set_hidden_in_game(True, True)
    except Exception:
        pass
    unreal.log("Retired startup actor without deleting it: {}".format(old_label))


def activate_actor_for_review(actor):
    try:
        actor.set_actor_hidden_in_game(False)
        actor.set_is_temporarily_hidden_in_editor(False)
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            component.set_visibility(True, True)
            component.set_hidden_in_game(False, True)
            collision_profile = getattr(component, "set_collision_profile_name", None)
            if callable(collision_profile):
                component.set_collision_profile_name("BlockAll")
    except Exception:
        pass
    return actor


def floor_altar_snap_location():
    floor = find_actor_by_label(FLOOR_ACTOR_LABEL)
    if floor is None:
        return unreal.Vector(0.0, -75.0, 4.0)
    component = floor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        return unreal.Vector(0.0, -75.0, 4.0)
    socket_name = unreal.Name("snap_altar")
    try:
        if component.does_socket_exist(socket_name):
            return component.get_socket_location(socket_name)
    except Exception:
        pass
    return unreal.Vector(0.0, -75.0, 4.0)


def spawn_altar_actor(mesh):
    location = floor_altar_snap_location()
    actor = find_actor_by_label(ALTAR_ACTOR_LABEL)
    if actor is None or actor.get_class().get_name() != "StaticMeshActor":
        if actor is not None:
            retire_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.StaticMeshActor,
            location,
            unreal.Rotator(0.0, 0.0, 0.0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(ALTAR_ACTOR_LABEL))
    actor.set_actor_label(ALTAR_ACTOR_LABEL)
    actor.set_actor_location(location, False, True)
    actor.set_actor_rotation(unreal.Rotator(0.0, 0.0, 0.0), False)
    actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
    tag_actor(actor)
    activate_actor_for_review(actor)
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("Static mesh actor has no StaticMeshComponent: {}".format(ALTAR_ACTOR_LABEL))
    component.set_static_mesh(mesh)
    component.set_mobility(unreal.ComponentMobility.STATIC)
    return actor


def update_startup_level(mesh):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))
    spawn_altar_actor(mesh)
    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea", only_if_is_dirty=False, recursive=True)
    unreal.log("Updated startup level with Infernal worthiness altar.")


def main():
    materials = ensure_materials()
    mesh = import_static_mesh()
    assign_project_materials(mesh, materials)
    ensure_review_lods_static(mesh)
    ensure_static_mesh_sockets(mesh)
    update_startup_level(mesh)
    unreal.log("Aerathea Infernal worthiness altar import complete.")


main()
