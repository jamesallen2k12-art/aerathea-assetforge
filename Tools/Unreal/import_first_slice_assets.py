import math
from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MATERIAL_PATH = "/Game/Aerathea/Materials"
BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/Props"
FIRST_SLICE_TAG = "AET_FIRST_SLICE"
# Blender source meshes are authored in centimeters and exported without FBX unit
# conversion, so Unreal must import the raw FBX geometry at 1 cm = 1 Unreal cm.
FBX_IMPORT_UNIFORM_SCALE = 0.01

ASSETS = [
    {
        "name": "SM_AET_TargetDummy_A01",
        "source": ROOT / "SourceAssets/Exports/Props/Training/SM_AET_TargetDummy_A01/SM_AET_TargetDummy_A01.fbx",
        "destination": "/Game/Aerathea/Props/Training",
    },
    {
        "name": "SM_AET_PortalArch_A01",
        "source": ROOT / "SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01/SM_AET_PortalArch_A01.fbx",
        "destination": "/Game/Aerathea/Props/Portal",
    },
    {
        "name": "SM_AET_ModularGroundTile_A01",
        "source": ROOT / "SourceAssets/Exports/Props/Environment/SM_AET_ModularGroundTile_A01/SM_AET_ModularGroundTile_A01.fbx",
        "destination": "/Game/Aerathea/Props/Environment",
    },
    {
        "name": "SM_MKG_WorkshopPropCrate_A01",
        "source": ROOT / "SourceAssets/Exports/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01/SM_MKG_WorkshopPropCrate_A01.fbx",
        "destination": "/Game/Aerathea/Props/Mekgineer",
    },
    {
        "name": "SM_MKG_AetherKnife_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetherKnife_A01/SM_MKG_AetherKnife_A01.fbx",
        "destination": "/Game/Aerathea/Weapons/Mekgineer",
    },
    {
        "name": "SM_MKG_AetherCoreUnit_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01/SM_MKG_AetherCoreUnit_A01.fbx",
        "destination": "/Game/Aerathea/Props/Mekgineer/Armory",
    },
    {
        "name": "SM_MKG_SparkPistol_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_SparkPistol_A01/SM_MKG_SparkPistol_A01.fbx",
        "destination": "/Game/Aerathea/Weapons/Mekgineer",
    },
    {
        "name": "SM_MKG_AetheriumGrenade_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01/SM_MKG_AetheriumGrenade_A01.fbx",
        "destination": "/Game/Aerathea/Props/Mekgineer/Armory",
    },
]

REPLACED_BLOCKOUT_LABELS = {
    "AET_BOOT_GroundTile_20m_A01",
    "AET_BOOT_PortalArch_LeftColumn_A01",
    "AET_BOOT_PortalArch_RightColumn_A01",
    "AET_BOOT_PortalArch_Capstone_A01",
    "AET_BOOT_PortalCore_Aetherium_A01",
    "AET_BOOT_TargetDummy_Blockout_A01",
    "AET_BOOT_TargetDummy_Crossbar_A01",
    "AET_PROD_PortalArch_A01",
    "AET_PROD_PortalCore_Aetherium_A01",
}
RUNTIME_REVIEW_HIDDEN_LABELS = {
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_BOOT_Camera_Overview",
    "AET_BOOT_Label_StyleTarget",
}


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def set_movable(component):
    if component is None:
        return
    try:
        component.set_mobility(unreal.ComponentMobility.MOVABLE)
        return
    except Exception:
        pass
    safe_set(component, "mobility", unreal.ComponentMobility.MOVABLE)


def color_material(name, color, roughness=0.85, metallic=0.0, emissive=None):
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, name)

    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        return unreal.load_asset(asset_path)

    material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name=name,
        package_path=MATERIAL_PATH,
        asset_class=unreal.Material,
        factory=unreal.MaterialFactoryNew(),
    )
    if material is None:
        raise RuntimeError("Failed to create material {}".format(asset_path))

    mat_lib = unreal.MaterialEditingLibrary
    base = mat_lib.create_material_expression(
        material,
        unreal.MaterialExpressionConstant3Vector,
        -420,
        -80,
    )
    base.set_editor_property("constant", color)
    mat_lib.connect_material_property(base, "", unreal.MaterialProperty.MP_BASE_COLOR)

    rough = mat_lib.create_material_expression(
        material,
        unreal.MaterialExpressionConstant,
        -420,
        120,
    )
    rough.set_editor_property("r", roughness)
    mat_lib.connect_material_property(rough, "", unreal.MaterialProperty.MP_ROUGHNESS)

    metal = mat_lib.create_material_expression(
        material,
        unreal.MaterialExpressionConstant,
        -420,
        260,
    )
    metal.set_editor_property("r", metallic)
    mat_lib.connect_material_property(metal, "", unreal.MaterialProperty.MP_METALLIC)

    if emissive is not None:
        glow = mat_lib.create_material_expression(
            material,
            unreal.MaterialExpressionConstant3Vector,
            -420,
            420,
        )
        glow.set_editor_property("constant", emissive)
        mat_lib.connect_material_property(glow, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)

    mat_lib.recompile_material(material)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    return material


def ensure_materials():
    return {
        "M_AET_Stone_Handpainted_A01": color_material(
            "M_AET_Stone_Handpainted_A01",
            unreal.LinearColor(0.34, 0.36, 0.37, 1.0),
        ),
        "M_AET_Timber_Handpainted_A01": color_material(
            "M_AET_Timber_Handpainted_A01",
            unreal.LinearColor(0.36, 0.22, 0.12, 1.0),
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
            metallic=0.0,
            emissive=unreal.LinearColor(0.0, 1.2, 3.5, 1.0),
        ),
        "M_AET_Straw_A01": color_material(
            "M_AET_Straw_A01",
            unreal.LinearColor(0.72, 0.52, 0.20, 1.0),
        ),
        "M_AET_Leather_Dark_A01": color_material(
            "M_AET_Leather_Dark_A01",
            unreal.LinearColor(0.19, 0.11, 0.07, 1.0),
        ),
        "M_AET_PackedEarth_A01": color_material(
            "M_AET_PackedEarth_A01",
            unreal.LinearColor(0.25, 0.19, 0.13, 1.0),
        ),
        "M_AET_Moss_A01": color_material(
            "M_AET_Moss_A01",
            unreal.LinearColor(0.18, 0.30, 0.16, 1.0),
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

    safe_set(mesh, "light_map_resolution", 64)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    unreal.log("Imported first-slice static mesh: {}".format(asset_path))
    return mesh


def assign_project_materials(mesh, project_materials):
    static_materials = mesh.get_editor_property("static_materials")
    count = len(static_materials)
    for index, static_material in enumerate(static_materials):
        slot_name = str(static_material.get_editor_property("material_slot_name"))
        current = static_material.get_editor_property("material_interface")
        current_name = current.get_name() if current is not None else slot_name
        material = project_materials.get(slot_name) or project_materials.get(current_name)
        if material is not None:
            mesh.set_material(index, material)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log("Synced {} material slots for {}".format(count, mesh.get_name()))


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
            unreal.log_warning(
                "Reparenting {} from {} to AAETPortalActor.".format(
                    asset_path,
                    current_parent_name,
                )
            )
            unreal.BlueprintEditorLibrary.reparent_blueprint(blueprint, parent_class)
            try:
                unreal.BlueprintEditorLibrary.compile_blueprint(blueprint)
            except Exception as exc:
                unreal.log_warning("Could not compile portal Blueprint immediately: {}".format(exc))
            unreal.EditorAssetLibrary.save_asset(asset_path)
            return blueprint
        unreal.log("Portal Blueprint already parented to {}.".format(current_parent_name))
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
    try:
        unreal.BlueprintEditorLibrary.compile_blueprint(blueprint)
    except Exception as exc:
        unreal.log_warning("Could not compile portal Blueprint immediately: {}".format(exc))
    unreal.EditorAssetLibrary.save_asset(asset_path)
    unreal.log("Created portal Blueprint from AAETPortalActor: {}".format(asset_path))
    return blueprint


def tag_actor(actor):
    actor.set_editor_property("tags", [unreal.Name(FIRST_SLICE_TAG)])
    return actor


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def portal_actor_spawn_class():
    parent_type = getattr(unreal, "AETPortalActor", None)
    if parent_type is None:
        raise RuntimeError("Compiled AAETPortalActor class is not available to Unreal Python")
    return parent_type


def set_actor_transform(actor, location, rotation=None, scale=None):
    rotation = rotation or unreal.Rotator(0, 0, 0)
    scale = scale or unreal.Vector(1, 1, 1)
    try:
        actor.set_actor_location(location, False, True)
    except Exception:
        actor.set_actor_location(location, False, False)
    try:
        actor.set_actor_rotation(rotation, False)
    except Exception:
        pass
    actor.set_actor_scale3d(scale)


def review_rotator(pitch, yaw, roll=0.0):
    # Unreal's Python Rotator constructor maps arguments as roll, pitch, yaw.
    return unreal.Rotator(roll, pitch, yaw)


def look_at_rotation(source, target):
    dx = target.x - source.x
    dy = target.y - source.y
    dz = target.z - source.z
    yaw = math.degrees(math.atan2(dy, dx))
    horizontal = math.sqrt((dx * dx) + (dy * dy))
    pitch = math.degrees(math.atan2(dz, horizontal))
    return review_rotator(pitch, yaw)


def is_shape_component(component):
    return component.get_class().get_name() in {
        "BoxComponent",
        "CapsuleComponent",
        "SphereComponent",
    }


def activate_actor_for_review(actor):
    try:
        actor.set_actor_hidden_in_game(False)
    except Exception:
        pass
    try:
        actor.set_is_temporarily_hidden_in_editor(False)
    except Exception:
        pass
    try:
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            if is_shape_component(component):
                try:
                    component.set_visibility(False, True)
                except Exception:
                    pass
                try:
                    component.set_hidden_in_game(True, True)
                except Exception:
                    pass
                continue
            try:
                component.set_visibility(True, True)
            except Exception:
                pass
            try:
                component.set_hidden_in_game(False, True)
            except Exception:
                pass

            collision_profile = getattr(component, "set_collision_profile_name", None)
            if callable(collision_profile):
                try:
                    component.set_collision_profile_name("BlockAll")
                except Exception:
                    pass
    except Exception:
        pass
    return actor


def hide_actor_for_runtime_review(actor):
    try:
        actor.set_actor_hidden_in_game(True)
    except Exception:
        pass
    try:
        actor.set_is_temporarily_hidden_in_editor(True)
    except Exception:
        pass
    try:
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            try:
                component.set_visibility(False, True)
            except Exception:
                pass
            try:
                component.set_hidden_in_game(True, True)
            except Exception:
                pass
    except Exception:
        pass
    return actor


def retire_actor(actor):
    old_label = actor.get_actor_label()
    if old_label.startswith("AET_RETIRED_"):
        return
    actor.set_actor_label("AET_RETIRED_{}".format(old_label))
    actor.set_actor_hidden_in_game(True)
    try:
        actor.set_is_temporarily_hidden_in_editor(True)
    except Exception:
        pass
    try:
        actor.set_actor_location(unreal.Vector(0, 0, -100000), False, True)
    except Exception:
        pass
    try:
        actor.set_actor_scale3d(unreal.Vector(0.01, 0.01, 0.01))
    except Exception:
        pass
    try:
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            component.set_visibility(False, True)
    except Exception:
        pass
    unreal.log("Retired startup actor without deleting it: {}".format(old_label))


def retire_replaced_startup_actors(desired_labels):
    desired = set(desired_labels)
    for actor in all_level_actors():
        label = actor.get_actor_label()
        tags = actor.get_editor_property("tags")
        if label in REPLACED_BLOCKOUT_LABELS:
            retire_actor(actor)
        elif unreal.Name(FIRST_SLICE_TAG) in tags and label not in desired:
            retire_actor(actor)


def spawn_static_mesh(label, mesh, location, rotation=None, scale=None, material=None):
    rotation = rotation or unreal.Rotator(0, 0, 0)
    scale = scale or unreal.Vector(1, 1, 1)
    actor = find_actor_by_label(label)
    if actor is None:
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.StaticMeshActor,
            location,
            rotation,
        )
        actor.set_actor_label(label)
    else:
        set_actor_transform(actor, location, rotation, scale)
    tag_actor(actor)

    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        retire_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.StaticMeshActor,
            location,
            rotation,
        )
        actor.set_actor_label(label)
        tag_actor(actor)
        component = actor.get_component_by_class(unreal.StaticMeshComponent)
        if component is None:
            raise RuntimeError("Static mesh actor has no StaticMeshComponent: {}".format(label))
    set_actor_transform(actor, location, rotation, scale)
    activate_actor_for_review(actor)
    component.set_static_mesh(mesh)
    if material is not None:
        component.set_material(0, material)
    return actor


def spawn_blueprint(label, blueprint, location, rotation=None, scale=None):
    rotation = rotation or unreal.Rotator(0, 0, 0)
    scale = scale or unreal.Vector(1, 1, 1)
    actor = find_actor_by_label(label)
    spawn_class = portal_actor_spawn_class()
    if actor is None:
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(spawn_class, location, rotation)
    elif "BP_AET_Portal_A01" not in actor.get_class().get_name() and "AETPortalActor" not in actor.get_class().get_name():
        retire_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(spawn_class, location, rotation)
    if actor is None:
        raise RuntimeError("Failed to spawn portal actor: {}".format(label))
    actor.set_actor_label(label)
    set_actor_transform(actor, location, rotation, scale)
    activate_actor_for_review(actor)
    tag_actor(actor)
    return actor


def spawn_actor(label, actor_class, location, rotation=None, scale=None):
    rotation = rotation or unreal.Rotator(0, 0, 0)
    scale = scale or unreal.Vector(1, 1, 1)
    actor = find_actor_by_label(label)
    if actor is None or actor.get_class() != actor_class.static_class():
        if actor is not None:
            retire_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, location, rotation)
    if actor is None:
        raise RuntimeError("Failed to spawn actor: {}".format(label))
    actor.set_actor_label(label)
    set_actor_transform(actor, location, rotation, scale)
    activate_actor_for_review(actor)
    tag_actor(actor)
    return actor


def set_directional_forward_priority(actor, priority):
    component = actor.get_component_by_class(unreal.DirectionalLightComponent)
    if component is not None:
        safe_set(component, "forward_shading_priority", priority)
        safe_set(component, "ForwardShadingPriority", priority)
    return component


def ensure_review_lighting():
    directional = find_actor_by_label("AET_BOOT_KeyLight_Directional")
    if directional is None and getattr(unreal, "DirectionalLight", None) is not None:
        directional = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.DirectionalLight,
            unreal.Vector(-260, -420, 780),
            review_rotator(-38.0, 42.0),
        )
        directional.set_actor_label("AET_BOOT_KeyLight_Directional")
    if directional is not None:
        set_actor_transform(
            directional,
            unreal.Vector(-260, -420, 780),
            review_rotator(-38.0, 42.0),
        )
        activate_actor_for_review(directional)
        component = directional.get_component_by_class(unreal.DirectionalLightComponent)
        if component is not None:
            set_movable(component)
            safe_set(component, "intensity", 5.0)
            safe_set(component, "light_color", unreal.Color(255, 236, 205, 255))
            set_directional_forward_priority(directional, 1)
    for actor in all_level_actors():
        if actor == directional or actor.get_component_by_class(unreal.DirectionalLightComponent) is None:
            continue
        set_directional_forward_priority(actor, 0)

    sky_light = find_actor_by_label("AET_BOOT_SkyLight")
    if sky_light is None and getattr(unreal, "SkyLight", None) is not None:
        sky_light = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.SkyLight,
            unreal.Vector(0, 0, 460),
            review_rotator(0.0, 0.0),
        )
        sky_light.set_actor_label("AET_BOOT_SkyLight")
    if sky_light is not None:
        set_actor_transform(sky_light, unreal.Vector(0, 0, 460), review_rotator(0.0, 0.0))
        activate_actor_for_review(sky_light)
        component = sky_light.get_component_by_class(unreal.SkyLightComponent)
        if component is not None:
            set_movable(component)
            safe_set(component, "intensity", 1.5)


def update_startup_level(meshes, materials, portal_blueprint):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    desired_labels = [
        "AET_PROD_TargetDummy_A01",
        "AET_PROD_Portal_A01",
        "AET_PROD_WorkshopCrate_A01",
        "AET_PROD_MKG_AetherKnife_A01",
        "AET_PROD_MKG_SparkPistol_A01",
        "AET_PROD_MKG_AetherCoreUnit_A01",
        "AET_PROD_MKG_AetheriumGrenade_A01",
        "AET_PROD_PlayerStart_Review_A01",
        "AET_PROD_Camera_Review_A01",
        "AET_PROD_ReviewCameraDirector_A01",
        "AET_PROD_ReviewFillLight_A01",
    ]
    for ix in range(5):
        for iy in range(5):
            desired_labels.append("AET_PROD_GroundTile_A01_R{}_C{}".format(iy + 1, ix + 1))
    retire_replaced_startup_actors(desired_labels)
    for label in RUNTIME_REVIEW_HIDDEN_LABELS:
        actor = find_actor_by_label(label)
        if actor is not None:
            hide_actor_for_runtime_review(actor)

    tile = meshes["SM_AET_ModularGroundTile_A01"]
    for ix, x in enumerate(range(-800, 801, 400)):
        for iy, y in enumerate(range(-800, 801, 400)):
            spawn_static_mesh(
                "AET_PROD_GroundTile_A01_R{}_C{}".format(iy + 1, ix + 1),
                tile,
                unreal.Vector(x, y, 0),
            )

    spawn_static_mesh(
        "AET_PROD_TargetDummy_A01",
        meshes["SM_AET_TargetDummy_A01"],
        unreal.Vector(-50, 350, 0),
    )
    spawn_blueprint(
        "AET_PROD_Portal_A01",
        portal_blueprint,
        unreal.Vector(350, 0, 0),
    )
    spawn_static_mesh(
        "AET_PROD_WorkshopCrate_A01",
        meshes["SM_MKG_WorkshopPropCrate_A01"],
        unreal.Vector(-235, 260, 0),
    )

    spawn_static_mesh(
        "AET_PROD_MKG_AetherKnife_A01",
        meshes["SM_MKG_AetherKnife_A01"],
        unreal.Vector(-395, 190, 42),
        rotation=review_rotator(0.0, 18.0),
    )
    spawn_static_mesh(
        "AET_PROD_MKG_SparkPistol_A01",
        meshes["SM_MKG_SparkPistol_A01"],
        unreal.Vector(-465, 190, 50),
        rotation=review_rotator(0.0, -15.0),
    )
    spawn_static_mesh(
        "AET_PROD_MKG_AetherCoreUnit_A01",
        meshes["SM_MKG_AetherCoreUnit_A01"],
        unreal.Vector(-360, 270, 28),
        rotation=review_rotator(0.0, 12.0),
    )
    spawn_static_mesh(
        "AET_PROD_MKG_AetheriumGrenade_A01",
        meshes["SM_MKG_AetheriumGrenade_A01"],
        unreal.Vector(-455, 275, 24),
        rotation=review_rotator(0.0, -10.0),
    )

    review_location = unreal.Vector(4710, -2880, 2575)
    review_target = unreal.Vector(-70, 160, 110)
    review_rotation = look_at_rotation(review_location, review_target)
    player_start_class = getattr(unreal, "PlayerStart", None)
    if player_start_class is None:
        unreal.log_warning("PlayerStart class is not available; skipping review player start.")
    else:
        spawn_actor(
            "AET_PROD_PlayerStart_Review_A01",
            player_start_class,
            review_location,
            review_rotation,
        )

    camera_actor = spawn_actor(
        "AET_PROD_Camera_Review_A01",
        unreal.CameraActor,
        review_location,
        review_rotation,
    )
    camera_component = camera_actor.get_component_by_class(unreal.CameraComponent)
    if camera_component is not None:
        safe_set(camera_component, "field_of_view", 65.0)
        safe_set(camera_component, "auto_activate", True)
    safe_set(camera_actor, "auto_activate_for_player", unreal.AutoReceiveInput.PLAYER0)
    safe_set(camera_actor, "tags", [unreal.Name("AET_REVIEW_CAMERA")])

    review_director_class = getattr(unreal, "AETReviewCameraDirector", None)
    if review_director_class is None:
        unreal.log_warning("AETReviewCameraDirector class is not available; skipping runtime review camera director.")
    else:
        spawn_actor(
            "AET_PROD_ReviewCameraDirector_A01",
            review_director_class,
            unreal.Vector(-900, -80, 220),
            review_rotation,
        )

    fill_light = spawn_actor(
        "AET_PROD_ReviewFillLight_A01",
        unreal.PointLight,
        unreal.Vector(-160, -180, 520),
    )
    light_component = fill_light.get_component_by_class(unreal.PointLightComponent)
    if light_component is not None:
        set_movable(light_component)
        safe_set(light_component, "intensity", 6000.0)
        safe_set(light_component, "attenuation_radius", 2200.0)
        safe_set(light_component, "light_color", unreal.Color(180, 210, 255, 255))

    ensure_review_lighting()

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea", only_if_is_dirty=False, recursive=True)
    unreal.log("Updated startup level with first-slice production assets.")


def main():
    materials = ensure_materials()
    meshes = {}
    for entry in ASSETS:
        mesh = import_static_mesh(entry)
        assign_project_materials(mesh, materials)
        meshes[entry["name"]] = mesh

    portal_blueprint = ensure_portal_blueprint()
    update_startup_level(meshes, materials, portal_blueprint)
    unreal.log("Aerathea first-slice import complete.")


main()
