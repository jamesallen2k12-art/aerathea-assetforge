from pathlib import Path
import math

import unreal

"""Experimental importer for the non-canon Power Nexus proof package.

Do not use this as the formal production import path. The approved process must
start from visual-canon intake and a Blender/DCC source package, then proceed to
FBX export, Unreal import validation, review-map capture, and Flamestrike
approval.
"""


ROOT = Path(__file__).resolve().parents[2]
ASSET_NAME = "SM_Gnome_AetherTek_PowerNexus_FuelCell_01"
SOURCE = ROOT / "SourceAssets/Generated/Props/Mekgineer" / ASSET_NAME / "Meshes" / f"{ASSET_NAME}_LOD0.obj"
DESTINATION = "/Game/Aerathea/Props/Mekgineer/Power"
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_ReviewIsland"
MATERIAL_PATH = "/Game/Aerathea/Materials/Gnome/PowerNexus"
ACTOR_LABEL = "AET_REVIEW_CurrentAsset_GnomePowerNexusFuelCell_A01"
CAMERA_LABEL = "AET_REVIEW_Camera_Main_A01"
PLAYER_START_LABEL = "AET_REVIEW_PlayerStart_A01"
DIRECTOR_LABEL = "AET_REVIEW_ReviewCameraDirector_A01"
REVIEW_TAG = "AET_REVIEW_ISLAND"


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def color_material(name, color, roughness=0.75, metallic=0.0, emissive=None, two_sided=False):
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

    if two_sided:
        safe_set(material, "two_sided", True)

    mat_lib = unreal.MaterialEditingLibrary
    base = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -420, -80)
    base.set_editor_property("constant", color)
    mat_lib.connect_material_property(base, "", unreal.MaterialProperty.MP_BASE_COLOR)

    rough = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 100)
    rough.set_editor_property("r", roughness)
    mat_lib.connect_material_property(rough, "", unreal.MaterialProperty.MP_ROUGHNESS)

    metal = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 240)
    metal.set_editor_property("r", metallic)
    mat_lib.connect_material_property(metal, "", unreal.MaterialProperty.MP_METALLIC)

    if emissive is not None:
        glow = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -420, 390)
        glow.set_editor_property("constant", emissive)
        mat_lib.connect_material_property(glow, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)

    mat_lib.recompile_material(material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)
    return material


def ensure_materials():
    return {
        "dark": color_material(
            "M_GNM_PowerNexus_DarkIron_A01",
            unreal.LinearColor(0.055, 0.060, 0.065, 1.0),
            roughness=0.58,
            metallic=0.75,
        ),
        "brass": color_material(
            "M_GNM_PowerNexus_Brass_A01",
            unreal.LinearColor(0.74, 0.49, 0.19, 1.0),
            roughness=0.42,
            metallic=0.75,
        ),
        "copper": color_material(
            "M_GNM_PowerNexus_Copper_A01",
            unreal.LinearColor(0.68, 0.29, 0.13, 1.0),
            roughness=0.46,
            metallic=0.8,
        ),
        "leather": color_material(
            "M_GNM_PowerNexus_DarkLeather_A01",
            unreal.LinearColor(0.16, 0.085, 0.045, 1.0),
            roughness=0.82,
            metallic=0.0,
        ),
        "glass": color_material(
            "M_GNM_PowerNexus_RefractorGlass_A01",
            unreal.LinearColor(0.18, 0.66, 0.95, 1.0),
            roughness=0.18,
            metallic=0.0,
            emissive=unreal.LinearColor(0.03, 0.16, 0.32, 1.0),
            two_sided=True,
        ),
        "aether": color_material(
            "M_GNM_PowerNexus_AetheriumCore_A01",
            unreal.LinearColor(0.04, 0.40, 1.0, 1.0),
            roughness=0.25,
            metallic=0.0,
            emissive=unreal.LinearColor(0.0, 0.52, 1.45, 1.0),
        ),
        "paint": color_material(
            "M_GNM_PowerNexus_RunePaint_A01",
            unreal.LinearColor(0.02, 0.22, 0.58, 1.0),
            roughness=0.65,
            metallic=0.0,
            emissive=unreal.LinearColor(0.0, 0.18, 0.55, 1.0),
        ),
    }


def import_static_mesh():
    if not SOURCE.exists():
        raise RuntimeError("Missing source OBJ: {}".format(SOURCE))
    ensure_directory(DESTINATION)

    task = unreal.AssetImportTask()
    task.set_editor_property("filename", str(SOURCE))
    task.set_editor_property("destination_path", DESTINATION)
    task.set_editor_property("destination_name", ASSET_NAME)
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    asset_path = "{}/{}".format(DESTINATION, ASSET_NAME)
    mesh = unreal.load_asset(asset_path)
    if mesh is None:
        raise RuntimeError("Import did not produce expected static mesh: {}".format(asset_path))
    safe_set(mesh, "light_map_resolution", 64)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return mesh


def assign_materials(mesh, materials):
    static_materials = mesh.get_editor_property("static_materials")
    for index, slot in enumerate(static_materials):
        slot_name = str(slot.get_editor_property("material_slot_name")).lower()
        if "aetheriumcore" in slot_name:
            material = materials["aether"]
        elif "refractor" in slot_name or "glass" in slot_name:
            material = materials["glass"]
        elif "brass" in slot_name:
            material = materials["brass"]
        elif "copper" in slot_name:
            material = materials["copper"]
        elif "leather" in slot_name:
            material = materials["leather"]
        elif "runepaint" in slot_name or "trace" in slot_name:
            material = materials["paint"]
        else:
            material = materials["dark"]
        mesh.set_material(index, material)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def ensure_lods(mesh):
    options = unreal.EditorScriptingMeshReductionOptions()
    safe_set(options, "auto_compute_lod_screen_size", False)
    settings = []
    for percent, screen_size in ((1.0, 1.0), (0.58, 0.55), (0.34, 0.28), (0.18, 0.12)):
        setting = unreal.EditorScriptingMeshReductionSettings()
        safe_set(setting, "percent_triangles", percent)
        safe_set(setting, "screen_size", screen_size)
        settings.append(setting)
    safe_set(options, "reduction_settings", settings)
    unreal.EditorStaticMeshLibrary.set_lods(mesh, options)
    count = unreal.EditorStaticMeshLibrary.get_lod_count(mesh)
    if count < 4:
        raise RuntimeError("{} has {} static LODs after reduction, expected 4".format(mesh.get_name(), count))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def collision_box_shape():
    for enum_name in (
        "ScriptCollisionShapeType",
        "ScriptingCollisionShapeType",
        "ScriptingCollisionShapeType_Deprecated",
        "ScriptingCollisionShapeType_DEPRECATED",
    ):
        enum_type = getattr(unreal, enum_name, None)
        if enum_type is None:
            continue
        for value_name in ("BOX", "Box"):
            value = getattr(enum_type, value_name, None)
            if value is not None:
                return value
    return None


def add_simple_collision(mesh):
    remover = getattr(unreal.EditorStaticMeshLibrary, "remove_collisions", None)
    if callable(remover):
        try:
            remover(mesh)
        except Exception as exc:
            unreal.log_warning("Could not remove existing collision: {}".format(exc))

    shape = collision_box_shape()
    if shape is None:
        unreal.log_warning("Collision enum unavailable; simple collision was not added")
        return
    adder = getattr(unreal.EditorStaticMeshLibrary, "add_simple_collisions", None)
    if callable(adder):
        adder(mesh, shape)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def remove_socket(mesh, name):
    finder = getattr(mesh, "find_socket", None)
    remover = getattr(mesh, "remove_socket", None)
    if not callable(finder) or not callable(remover):
        return
    try:
        existing = finder(unreal.Name(name))
    except Exception:
        existing = None
    if existing is not None:
        try:
            remover(existing)
        except TypeError:
            remover(unreal.Name(name))


def ensure_sockets(mesh):
    socket_specs = [
        ("Socket_PowerRoute_A", unreal.Vector(-15.0, -24.4, 65.0)),
        ("Socket_PowerRoute_B", unreal.Vector(15.0, -24.4, 65.0)),
        ("Socket_PowerRoute_C", unreal.Vector(0.0, -24.4, 14.0)),
    ]
    for name, _location in socket_specs:
        remove_socket(mesh, name)
    add_socket = getattr(mesh, "add_socket", None)
    if not callable(add_socket):
        unreal.log_warning("StaticMesh.add_socket unavailable; sockets were not added")
        return
    for name, location in socket_specs:
        socket = unreal.new_object(unreal.StaticMeshSocket, outer=mesh)
        socket.set_editor_property("socket_name", unreal.Name(name))
        socket.set_editor_property("relative_location", location)
        socket.set_editor_property("relative_rotation", unreal.Rotator(0.0, 0.0, 0.0))
        socket.set_editor_property("relative_scale", unreal.Vector(1.0, 1.0, 1.0))
        add_socket(socket)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def apply_metadata(mesh):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        return
    metadata = {
        "Aerathea.StaticMesh.Package": ASSET_NAME,
        "Aerathea.StaticMesh.Status": "unreal_import_candidate_pending_flamestrike_approval",
        "Aerathea.StaticMesh.SourceMethod": "lore_to_dcc_candidate_obj_import",
        "Aerathea.StaticMesh.VisualCanonSource": "pending_flamestrike_visual_approval",
        "Aerathea.StaticMesh.CollisionPolicy": "simple_box_review_collision",
        "Aerathea.StaticMesh.GameplayBehavior": "none_static_power_cell_prop",
        "Aerathea.StaticMesh.FinalVisualApproval": "pending",
    }
    for tag, value in metadata.items():
        setter(mesh, tag, str(value))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def look_at_rotation(source, target):
    math_library = getattr(unreal, "MathLibrary", None)
    if math_library is not None:
        try:
            return math_library.find_look_at_rotation(source, target)
        except Exception:
            pass
    dx = target.x - source.x
    dy = target.y - source.y
    dz = target.z - source.z
    yaw = math.degrees(math.atan2(dy, dx))
    horizontal = math.sqrt((dx * dx) + (dy * dy))
    pitch = math.degrees(math.atan2(dz, horizontal))
    return unreal.Rotator(0.0, pitch, yaw)


def tag_actor(actor):
    tags = list(actor.get_editor_property("tags"))
    tag = unreal.Name(REVIEW_TAG)
    if tag not in tags:
        tags.append(tag)
    actor.set_editor_property("tags", tags)


def place_review_actor(mesh):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load review island level: {}".format(LEVEL_PATH))
    actor = actor_by_label(ACTOR_LABEL)
    if actor is None or actor.get_class().get_name() != "StaticMeshActor":
        if actor is not None:
            unreal.EditorLevelLibrary.destroy_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.StaticMeshActor,
            unreal.Vector(0.0, 0.0, 0.0),
            unreal.Rotator(0.0, 0.0, 0.0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn review actor")
    actor.set_actor_label(ACTOR_LABEL)
    actor.set_actor_location(unreal.Vector(0.0, 0.0, 0.0), False, True)
    actor.set_actor_rotation(unreal.Rotator(0.0, 0.0, 0.0), False)
    actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
    tag_actor(actor)
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("Review actor has no StaticMeshComponent")
    component.set_static_mesh(mesh)
    component.set_mobility(unreal.ComponentMobility.STATIC)
    component.set_collision_enabled(unreal.CollisionEnabled.QUERY_AND_PHYSICS)
    return actor


def set_review_camera():
    camera_location = unreal.Vector(125.0, -255.0, 135.0)
    camera_target = unreal.Vector(0.0, 0.0, 38.0)
    rotation = look_at_rotation(camera_location, camera_target)
    for label in (CAMERA_LABEL, PLAYER_START_LABEL, DIRECTOR_LABEL):
        actor = actor_by_label(label)
        if actor is None:
            continue
        actor.modify()
        actor.set_actor_location(camera_location, False, False)
        actor.set_actor_rotation(rotation, False)
        camera_component = actor.get_component_by_class(unreal.CameraComponent)
        if camera_component is not None:
            camera_component.modify()
            camera_component.set_editor_property("field_of_view", 38.0)


def main():
    materials = ensure_materials()
    mesh = import_static_mesh()
    assign_materials(mesh, materials)
    ensure_lods(mesh)
    add_simple_collision(mesh)
    ensure_sockets(mesh)
    apply_metadata(mesh)
    place_review_actor(mesh)
    set_review_camera()
    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save review island level")
    unreal.EditorAssetLibrary.save_directory(DESTINATION, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=False, recursive=True)
    unreal.log("Aerathea gnome Power Nexus fuel cell import complete: {}/{}".format(DESTINATION, ASSET_NAME))


main()
