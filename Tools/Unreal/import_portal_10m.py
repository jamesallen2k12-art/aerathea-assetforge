from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MATERIAL_PATH = "/Game/Aerathea/Materials"
BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/Props"
PORTAL_TAG = "AET_PORTAL_10M_REVIEW"
FBX_IMPORT_UNIFORM_SCALE = 0.01

PORTAL_ENTRY = {
    "name": "SM_AET_PortalArch_A01",
    "source": ROOT / "SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01/SM_AET_PortalArch_A01.fbx",
    "destination": "/Game/Aerathea/Props/Portal",
}

SOCKET_SPECS = [
    ("Socket_PortalCore", unreal.Vector(0.0, -32.0, 500.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("Socket_VFX_Center", unreal.Vector(0.0, -64.0, 520.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("Socket_Audio_Hum", unreal.Vector(0.0, -72.0, 450.0), unreal.Rotator(0.0, 0.0, 0.0)),
]


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def color_material(name, color, roughness=0.85, metallic=0.0, emissive=None):
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, name)
    material = unreal.load_asset(asset_path)
    if material is not None:
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

    mat_lib.recompile_material(material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)
    return material


def ensure_materials():
    return {
        "M_AET_Stone_Handpainted_A01": color_material(
            "M_AET_Stone_Handpainted_A01",
            unreal.LinearColor(0.34, 0.36, 0.37, 1.0),
        ),
        "M_AET_DarkIron_A01": color_material(
            "M_AET_DarkIron_A01",
            unreal.LinearColor(0.08, 0.09, 0.10, 1.0),
            roughness=0.7,
            metallic=0.65,
        ),
        "M_AET_Brass_A01": color_material(
            "M_AET_Brass_A01",
            unreal.LinearColor(0.78, 0.55, 0.25, 1.0),
            roughness=0.55,
            metallic=0.8,
        ),
        "M_AET_AetheriumGlow_Blue_A01": color_material(
            "M_AET_AetheriumGlow_Blue_A01",
            unreal.LinearColor(0.05, 0.35, 0.95, 1.0),
            roughness=0.25,
            emissive=unreal.LinearColor(0.0, 1.2, 3.5, 1.0),
        ),
    }


def import_static_mesh(entry):
    if not entry["source"].exists():
        raise RuntimeError("Missing source FBX: {}".format(entry["source"]))
    ensure_directory(entry["destination"])

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
    task.set_editor_property("filename", str(entry["source"]))
    task.set_editor_property("destination_path", entry["destination"])
    task.set_editor_property("destination_name", entry["name"])
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)
    task.set_editor_property("options", fbx_ui)

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    asset_path = "{}/{}".format(entry["destination"], entry["name"])
    mesh = unreal.load_asset(asset_path)
    if mesh is None:
        raise RuntimeError("Import did not produce expected static mesh: {}".format(asset_path))
    safe_set(mesh, "light_map_resolution", 256)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return mesh


def assign_project_materials(mesh, project_materials):
    static_materials = mesh.get_editor_property("static_materials")
    for index, static_material in enumerate(static_materials):
        slot_name = str(static_material.get_editor_property("material_slot_name"))
        current = static_material.get_editor_property("material_interface")
        current_name = current.get_name() if current is not None else slot_name
        material = project_materials.get(slot_name) or project_materials.get(current_name)
        if material is not None:
            mesh.set_material(index, material)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log("Synced {} material slots for {}".format(len(static_materials), mesh.get_name()))


def ensure_review_lods_static(mesh, target_lods=4):
    options = unreal.EditorScriptingMeshReductionOptions()
    safe_set(options, "auto_compute_lod_screen_size", False)
    settings = []
    for percent, screen_size in ((1.0, 1.0), (0.58, 0.55), (0.32, 0.28), (0.15, 0.12)):
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


def remove_static_socket(mesh, name):
    existing = None
    finder = getattr(mesh, "find_socket", None)
    if callable(finder):
        try:
            existing = finder(unreal.Name(name))
        except Exception:
            existing = None
    remover = getattr(mesh, "remove_socket", None)
    if existing is not None and callable(remover):
        try:
            remover(existing)
        except TypeError:
            remover(unreal.Name(name))


def ensure_static_mesh_sockets(mesh):
    for name, _location, _rotation in SOCKET_SPECS:
        remove_static_socket(mesh, name)
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
    unreal.log("Ensured {} portal static mesh sockets for {}".format(len(SOCKET_SPECS), mesh.get_name()))


def ensure_portal_blueprint():
    ensure_directory(BLUEPRINT_PATH)
    asset_path = "{}/BP_AET_Portal_A01".format(BLUEPRINT_PATH)
    parent_type = getattr(unreal, "AETPortalActor", None)
    if parent_type is None:
        raise RuntimeError("Compiled AAETPortalActor class is not available to Unreal Python")
    parent_class = parent_type.static_class() if hasattr(parent_type, "static_class") else parent_type

    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        blueprint = unreal.load_asset(asset_path)
        current_parent = unreal.BlueprintEditorLibrary.get_blueprint_parent_class(blueprint)
        current_parent_name = current_parent.get_name() if current_parent is not None else "None"
        parent_class_name = parent_class.get_name()
        if current_parent != parent_class and current_parent_name != parent_class_name:
            unreal.BlueprintEditorLibrary.reparent_blueprint(blueprint, parent_class)
        try:
            unreal.BlueprintEditorLibrary.compile_blueprint(blueprint)
        except Exception as exc:
            unreal.log_warning("Could not compile portal Blueprint immediately: {}".format(exc))
        unreal.EditorAssetLibrary.save_asset(asset_path)
        return blueprint

    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", parent_class)
    blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name="BP_AET_Portal_A01",
        package_path=BLUEPRINT_PATH,
        asset_class=unreal.Blueprint,
        factory=factory,
    )
    if blueprint is None:
        raise RuntimeError("Failed to create {}".format(asset_path))
    unreal.BlueprintEditorLibrary.compile_blueprint(blueprint)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    return blueprint


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def set_actor_transform(actor, location, rotation=None, scale=None):
    rotation = rotation or unreal.Rotator(0.0, 0.0, 0.0)
    scale = scale or unreal.Vector(1.0, 1.0, 1.0)
    try:
        actor.set_actor_location(location, False, True)
    except Exception:
        actor.set_actor_location(location, False, False)
    try:
        actor.set_actor_rotation(rotation, False)
    except Exception:
        pass
    actor.set_actor_scale3d(scale)


def set_component_relative_location(component, location):
    try:
        component.set_relative_location(location, False, None, False)
        return
    except TypeError:
        pass
    try:
        component.set_relative_location(location, False, False)
        return
    except TypeError:
        pass
    try:
        component.set_relative_location(location, False)
        return
    except TypeError:
        pass
    safe_set(component, "relative_location", location)


def configure_portal_actor(actor, mesh):
    actor.set_editor_property("tags", [unreal.Name(PORTAL_TAG)])
    set_actor_transform(actor, unreal.Vector(350.0, 0.0, 0.0))
    safe_set(actor, "interaction_box_extent", unreal.Vector(560.0, 260.0, 560.0))

    arch_component = actor.get_editor_property("portal_arch_mesh")
    if arch_component is None:
        arch_component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if arch_component is None:
        raise RuntimeError("Portal actor has no arch StaticMeshComponent")
    arch_component.set_static_mesh(mesh)
    try:
        arch_component.set_collision_profile_name("BlockAll")
    except Exception:
        pass

    core_component = actor.get_editor_property("portal_core_mesh")
    if core_component is not None:
        set_component_relative_location(core_component, unreal.Vector(0.0, -32.0, 500.0))
        core_component.set_relative_scale3d(unreal.Vector(7.4, 0.18, 10.0))
        core_component.set_collision_enabled(unreal.CollisionEnabled.NO_COLLISION)

    interaction = actor.get_editor_property("interaction_volume")
    if interaction is not None:
        set_component_relative_location(interaction, unreal.Vector(0.0, -120.0, 520.0))
        interaction.set_box_extent(unreal.Vector(560.0, 260.0, 560.0), True)
        interaction.set_collision_enabled(unreal.CollisionEnabled.QUERY_ONLY)
        try:
            interaction.set_collision_profile_name("Trigger")
        except Exception:
            pass
        safe_set(interaction, "generate_overlap_events", True)
        interaction.set_visibility(False, True)
        interaction.set_hidden_in_game(True, True)


def update_startup_level(mesh, blueprint):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    parent_type = getattr(unreal, "AETPortalActor", None)
    actor = find_actor_by_label("AET_PROD_Portal_A01")
    if actor is None:
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(parent_type, unreal.Vector(350.0, 0.0, 0.0))
    if actor is None:
        raise RuntimeError("Failed to spawn portal actor")
    actor.set_actor_label("AET_PROD_Portal_A01")
    configure_portal_actor(actor, mesh)

    if blueprint is not None:
        try:
            unreal.BlueprintEditorLibrary.compile_blueprint(blueprint)
        except Exception as exc:
            unreal.log_warning("Could not compile portal Blueprint after placement: {}".format(exc))

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Props/Portal", only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(BLUEPRINT_PATH, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Maps", only_if_is_dirty=False, recursive=True)
    unreal.log("Updated startup level with 10 m universal portal review actor.")


def main():
    materials = ensure_materials()
    mesh = import_static_mesh(PORTAL_ENTRY)
    assign_project_materials(mesh, materials)
    ensure_review_lods_static(mesh)
    ensure_static_mesh_sockets(mesh)
    blueprint = ensure_portal_blueprint()
    update_startup_level(mesh, blueprint)
    unreal.log("Aerathea 10 m portal import complete.")


main()
