from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MATERIAL_PATH = "/Game/Aerathea/Materials"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
OGRE_TAG = "AET_OGRE_BASE_REVIEW"
FBX_IMPORT_UNIFORM_SCALE = 0.01


OGRE_ASSETS = [
    {
        "name": "SK_OGR_Base_Male_A01",
        "source": ROOT / "SourceAssets/Exports/Characters/Ogres/SK_OGR_Base_A01/SK_OGR_Base_Male_A01.fbx",
        "destination": "/Game/Aerathea/Characters/Ogres/Base",
        "physics_asset": "/Game/Aerathea/Characters/Ogres/Base/PHYS_OGR_Base_Male_A01",
        "anim_blueprint": "/Game/Aerathea/Characters/Ogres/Base/ABP_OGR_Base_Male_A01",
        "skeleton": "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
        "actor_label": "AET_PROD_OgreMaleBase_A01",
        "actor_location": unreal.Vector(80.0, 450.0, 0.0),
        "actor_yaw": -42.0,
    },
    {
        "name": "SK_OGR_Base_Female_A01",
        "source": ROOT / "SourceAssets/Exports/Characters/Ogres/SK_OGR_Base_A01/SK_OGR_Base_Female_A01.fbx",
        "destination": "/Game/Aerathea/Characters/Ogres/Base",
        "physics_asset": "/Game/Aerathea/Characters/Ogres/Base/PHYS_OGR_Base_Female_A01",
        "anim_blueprint": "/Game/Aerathea/Characters/Ogres/Base/ABP_OGR_Base_Female_A01",
        "skeleton": "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Female_A01_Skeleton",
        "actor_label": "AET_PROD_OgreFemaleBase_A01",
        "actor_location": unreal.Vector(-65.0, 375.0, 0.0),
        "actor_yaw": -42.0,
    },
]


OGRE_SOCKET_SPECS = [
    ("hand_r_weapon", "hand_r", unreal.Vector(40.0, -20.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("hand_l_offhand", "hand_l", unreal.Vector(40.0, 20.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("hand_r_twohand_grip", "hand_r", unreal.Vector(52.0, -12.0, 12.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("hand_l_twohand_grip", "hand_l", unreal.Vector(52.0, 12.0, 12.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("back_large_weapon", "chest", unreal.Vector(-48.0, -24.0, 22.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("back_shield", "chest", unreal.Vector(-52.0, 24.0, 16.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("spine_teknomancy_pack", "chest", unreal.Vector(-46.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("shoulder_l_large", "chest", unreal.Vector(0.0, 64.0, 36.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("shoulder_r_large", "chest", unreal.Vector(0.0, -64.0, 36.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("belt_front", "pelvis", unreal.Vector(46.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("belt_back", "pelvis", unreal.Vector(-34.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_mouth", "head", unreal.Vector(48.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_eye_l", "head", unreal.Vector(34.0, 8.0, 8.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_eye_r", "head", unreal.Vector(34.0, -8.0, 8.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_chest_core", "chest", unreal.Vector(52.0, 0.0, -18.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_stomp_ground", "root", unreal.Vector(64.0, 0.0, 4.0), unreal.Rotator(0.0, 0.0, 0.0)),
]


SCALE_MARKERS = [
    {
        "label": "AET_PROD_OgreScale_MinotaurMale_A01",
        "height": 274.0,
        "location": unreal.Vector(-330.0, 250.0, 137.0),
        "color": unreal.LinearColor(0.45, 0.30, 0.18, 1.0),
        "material": "M_OGR_ReviewScale_Minotaur_A01",
    },
    {
        "label": "AET_PROD_OgreScale_AnubisathMale_A01",
        "height": 254.0,
        "location": unreal.Vector(-210.0, 310.0, 127.0),
        "color": unreal.LinearColor(0.03, 0.03, 0.04, 1.0),
        "material": "M_OGR_ReviewScale_Anubisath_A01",
    },
    {
        "label": "AET_PROD_OgreScale_GiantMale_A01",
        "height": 470.0,
        "location": unreal.Vector(270.0, 580.0, 235.0),
        "color": unreal.LinearColor(0.35, 0.45, 0.52, 1.0),
        "material": "M_OGR_ReviewScale_Giant_A01",
    },
]


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def configure_material_usage(material, use_with_skeletal_mesh=False):
    if use_with_skeletal_mesh:
        usage = getattr(unreal.MaterialUsage, "MATUSAGE_SKELETAL_MESH", None)
        if usage is not None:
            try:
                unreal.MaterialEditingLibrary.set_material_usage(material, usage)
            except Exception as exc:
                unreal.log_warning("Could not set skeletal material usage: {}".format(exc))
        safe_set(material, "used_with_skeletal_mesh", True)
    unreal.MaterialEditingLibrary.recompile_material(material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)


def color_material(name, color, roughness=0.85, metallic=0.0, emissive=None, use_with_skeletal_mesh=False):
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, name)
    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        material = unreal.load_asset(asset_path)
        configure_material_usage(material, use_with_skeletal_mesh=use_with_skeletal_mesh)
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

    configure_material_usage(material, use_with_skeletal_mesh=use_with_skeletal_mesh)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    return material


def ensure_materials():
    return {
        "M_OGR_Skin_Blockout_A01": color_material(
            "M_OGR_Skin_Blockout_A01",
            unreal.LinearColor(0.48, 0.40, 0.31, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_OGR_Warpaint_Blockout_A01": color_material(
            "M_OGR_Warpaint_Blockout_A01",
            unreal.LinearColor(0.24, 0.10, 0.06, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_OGR_Leather_Blockout_A01": color_material(
            "M_OGR_Leather_Blockout_A01",
            unreal.LinearColor(0.20, 0.11, 0.07, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_OGR_Iron_Blockout_A01": color_material(
            "M_OGR_Iron_Blockout_A01",
            unreal.LinearColor(0.12, 0.12, 0.11, 1.0),
            roughness=0.7,
            metallic=0.55,
            use_with_skeletal_mesh=True,
        ),
        "M_OGR_Brass_Blockout_A01": color_material(
            "M_OGR_Brass_Blockout_A01",
            unreal.LinearColor(0.64, 0.36, 0.16, 1.0),
            roughness=0.55,
            metallic=0.7,
            use_with_skeletal_mesh=True,
        ),
        "M_OGR_Bone_Blockout_A01": color_material(
            "M_OGR_Bone_Blockout_A01",
            unreal.LinearColor(0.66, 0.58, 0.43, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_OGR_AetheriumGlow_Blockout_A01": color_material(
            "M_OGR_AetheriumGlow_Blockout_A01",
            unreal.LinearColor(0.0, 0.55, 1.0, 1.0),
            roughness=0.25,
            emissive=unreal.LinearColor(0.0, 1.1, 2.5, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_OGR_NecroGlow_Blockout_A01": color_material(
            "M_OGR_NecroGlow_Blockout_A01",
            unreal.LinearColor(0.16, 0.95, 0.28, 1.0),
            roughness=0.3,
            emissive=unreal.LinearColor(0.08, 1.6, 0.25, 1.0),
            use_with_skeletal_mesh=True,
        ),
    }


def material_instance_name(mesh_name, material_name):
    asset_name = mesh_name[3:] if mesh_name.startswith("SK_") else mesh_name
    semantic = material_name
    for prefix in ("M_OGR_", "M_AET_"):
        if semantic.startswith(prefix):
            semantic = semantic[len(prefix):]
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
    for prop in ("materials", "static_materials"):
        try:
            return list(mesh.get_editor_property(prop))
        except Exception:
            continue
    return []


def assign_project_materials(mesh, project_materials):
    slots = material_slots(mesh)
    edited_slots = False
    for index, slot in enumerate(slots):
        slot_name = str(slot.get_editor_property("material_slot_name"))
        current = slot.get_editor_property("material_interface")
        current_name = current.get_name() if current is not None else slot_name
        base_material = project_materials.get(slot_name) or project_materials.get(current_name)
        if base_material is None:
            continue
        material = ensure_material_instance(material_instance_name(mesh.get_name(), base_material.get_name()), base_material)
        set_material = getattr(mesh, "set_material", None)
        if callable(set_material):
            set_material(index, material)
        else:
            slot.set_editor_property("material_interface", material)
            edited_slots = True
    if edited_slots:
        mesh.set_editor_property("materials", slots)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log("Synced {} Ogre material slots for {}".format(len(slots), mesh.get_name()))


def import_skeletal_mesh(entry):
    if not entry["source"].exists():
        raise RuntimeError("Missing source FBX: {}".format(entry["source"]))
    ensure_directory(entry["destination"])

    fbx_ui = unreal.FbxImportUI()
    safe_set(fbx_ui, "import_mesh", True)
    safe_set(fbx_ui, "import_as_skeletal", True)
    safe_set(fbx_ui, "import_materials", False)
    safe_set(fbx_ui, "import_textures", False)
    safe_set(fbx_ui, "import_animations", False)
    safe_set(fbx_ui, "create_physics_asset", True)
    safe_set(fbx_ui, "import_uniform_scale", FBX_IMPORT_UNIFORM_SCALE)
    skeletal_data = fbx_ui.skeletal_mesh_import_data
    safe_set(skeletal_data, "import_morph_targets", False)
    safe_set(skeletal_data, "update_skeleton_reference_pose", True)
    safe_set(skeletal_data, "use_t0_as_ref_pose", True)
    safe_set(skeletal_data, "import_uniform_scale", FBX_IMPORT_UNIFORM_SCALE)

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
        raise RuntimeError("Import did not produce expected skeletal mesh: {}".format(asset_path))
    unreal.EditorAssetLibrary.save_asset(asset_path)
    unreal.log("Imported Ogre skeletal mesh: {}".format(asset_path))
    return mesh


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def ensure_physics_asset(mesh, desired_asset_path):
    existing = unreal.load_asset(desired_asset_path)
    smes = unreal.get_editor_subsystem(unreal.SkeletalMeshEditorSubsystem)
    if smes is None:
        raise RuntimeError("SkeletalMeshEditorSubsystem is not available")

    if existing is None:
        created = smes.create_physics_asset(mesh, set_to_mesh=True)
        if created is None:
            raise RuntimeError("Failed to create physics asset for {}".format(mesh.get_name()))
        created_path = asset_path_without_object(created)
        if created_path != desired_asset_path:
            if not unreal.EditorAssetLibrary.rename_asset(created_path, desired_asset_path):
                raise RuntimeError("Failed to rename {} to {}".format(created_path, desired_asset_path))
            existing = unreal.load_asset(desired_asset_path)
        else:
            existing = created

    if existing is None:
        raise RuntimeError("Failed to load physics asset: {}".format(desired_asset_path))
    if not smes.assign_physics_asset(mesh, existing):
        raise RuntimeError("Failed to assign {} to {}".format(desired_asset_path, mesh.get_name()))
    unreal.EditorAssetLibrary.save_loaded_asset(existing)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return existing


def ensure_review_lods_skeletal(mesh, target_lods=4):
    smes = unreal.get_editor_subsystem(unreal.SkeletalMeshEditorSubsystem)
    if smes is None:
        raise RuntimeError("SkeletalMeshEditorSubsystem is not available")
    count = smes.get_lod_count(mesh)
    if count < target_lods:
        try:
            smes.regenerate_lod(
                skeletal_mesh=mesh,
                new_lod_count=target_lods,
                regenerate_even_if_imported=True,
                generate_base_lod=False,
            )
        except TypeError:
            smes.regenerate_lod(mesh, target_lods, True, False)
    count = smes.get_lod_count(mesh)
    if count < target_lods:
        raise RuntimeError("{} has {} skeletal LODs after reduction, expected {}".format(mesh.get_name(), count, target_lods))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def remove_socket_name(mesh, name):
    socket_name = unreal.Name(name)
    if mesh.find_socket(socket_name) is not None and not mesh.remove_socket(socket_name):
        raise RuntimeError("Failed to remove existing socket {} from {}".format(name, mesh.get_name()))


def ensure_skeletal_mesh_sockets(mesh):
    for socket_name, _bone_name, _location, _rotation in OGRE_SOCKET_SPECS:
        remove_socket_name(mesh, socket_name)
        remove_socket_name(mesh, "SOCKET_{}".format(socket_name))

    for socket_name, bone_name, location, rotation in OGRE_SOCKET_SPECS:
        socket = unreal.new_object(unreal.SkeletalMeshSocket, outer=mesh)
        socket.set_socket_parent(mesh, unreal.Name(bone_name))
        socket.set_editor_property("relative_location", location)
        socket.set_editor_property("relative_rotation", rotation)
        socket.set_editor_property("relative_scale", unreal.Vector(1.0, 1.0, 1.0))
        mesh.add_socket(socket)
        generated_name = socket.get_editor_property("socket_name")
        if not mesh.rename_socket(generated_name, unreal.Name(socket_name)):
            raise RuntimeError("Failed to rename generated socket {} to {}".format(generated_name, socket_name))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def ensure_anim_blueprint(asset_path, skeleton_path, preview_mesh_path):
    existing = unreal.load_asset(asset_path)
    if existing is not None:
        unreal.EditorAssetLibrary.save_loaded_asset(existing)
        return existing

    package_path, asset_name = asset_path.rsplit("/", 1)
    ensure_directory(package_path)
    skeleton = unreal.load_asset(skeleton_path)
    preview_mesh = unreal.load_asset(preview_mesh_path)
    if skeleton is None:
        raise RuntimeError("Missing skeleton for animation Blueprint: {}".format(skeleton_path))

    factory = unreal.AnimBlueprintFactory()
    safe_set(factory, "target_skeleton", skeleton)
    if preview_mesh is not None:
        safe_set(factory, "preview_skeletal_mesh", preview_mesh)
    asset = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name=asset_name,
        package_path=package_path,
        asset_class=unreal.AnimBlueprint,
        factory=factory,
    )
    if asset is None:
        raise RuntimeError("Failed to create animation Blueprint {}".format(asset_path))
    unreal.EditorAssetLibrary.save_loaded_asset(asset)
    return asset


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
    for tag in (unreal.Name(OGRE_TAG), unreal.Name("AET_NEXT_SLICE")):
        if tag not in tags:
            tags.append(tag)
    actor.set_editor_property("tags", tags)
    return actor


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
    return unreal.Rotator(roll, pitch, yaw)


def is_shape_component(component):
    return component.get_class().get_name() in {
        "BoxComponent",
        "CapsuleComponent",
        "SphereComponent",
    }


def activate_actor_for_review(actor):
    try:
        actor.set_actor_hidden_in_game(False)
        actor.set_is_temporarily_hidden_in_editor(False)
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            if is_shape_component(component):
                component.set_visibility(False, True)
                component.set_hidden_in_game(True, True)
                continue
            component.set_visibility(True, True)
            component.set_hidden_in_game(False, True)
    except Exception:
        pass
    return actor


def set_skeletal_mesh_component(component, mesh):
    for setter_name in ("set_skeletal_mesh_asset", "set_skeletal_mesh"):
        setter = getattr(component, setter_name, None)
        if callable(setter):
            setter(mesh)
            return
    for prop_name in ("skeletal_mesh_asset", "skeletal_mesh"):
        try:
            component.set_editor_property(prop_name, mesh)
            return
        except Exception:
            continue
    raise RuntimeError("Could not assign skeletal mesh {}".format(mesh.get_name()))


def spawn_skeletal_mesh(label, mesh, location, yaw):
    actor = find_actor_by_label(label)
    if actor is None or actor.get_class().get_name() != "SkeletalMeshActor":
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.SkeletalMeshActor,
            location,
            review_rotator(0.0, yaw),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn skeletal mesh actor: {}".format(label))
    actor.set_actor_label(label)
    set_actor_transform(actor, location, review_rotator(0.0, yaw))
    tag_actor(actor)
    activate_actor_for_review(actor)
    component = actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if component is None:
        raise RuntimeError("Skeletal mesh actor has no SkeletalMeshComponent: {}".format(label))
    set_skeletal_mesh_component(component, mesh)
    return actor


def ensure_scale_marker_material(name, color):
    return color_material(name, color, use_with_skeletal_mesh=False)


def spawn_scale_marker(entry):
    mesh = unreal.load_asset("/Engine/BasicShapes/Cube.Cube")
    if mesh is None:
        raise RuntimeError("Missing Engine cube mesh for Ogre scale marker")
    material = ensure_scale_marker_material(entry["material"], entry["color"])
    actor = find_actor_by_label(entry["label"])
    if actor is None or actor.get_class().get_name() != "StaticMeshActor":
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.StaticMeshActor,
            entry["location"],
            review_rotator(0.0, -42.0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn scale marker {}".format(entry["label"]))
    actor.set_actor_label(entry["label"])
    set_actor_transform(
        actor,
        entry["location"],
        review_rotator(0.0, -42.0),
        unreal.Vector(0.18, 0.18, entry["height"] / 100.0),
    )
    tag_actor(actor)
    activate_actor_for_review(actor)
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("Scale marker has no StaticMeshComponent: {}".format(entry["label"]))
    component.set_static_mesh(mesh)
    component.set_material(0, material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)
    return actor


def update_startup_level(meshes):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    for marker in SCALE_MARKERS:
        spawn_scale_marker(marker)

    for entry in OGRE_ASSETS:
        spawn_skeletal_mesh(
            entry["actor_label"],
            meshes[entry["name"]],
            entry["actor_location"],
            entry["actor_yaw"],
        )

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea", only_if_is_dirty=False, recursive=True)
    unreal.log("Updated startup level with Ogre base review actors.")


def main():
    materials = ensure_materials()
    meshes = {}
    for entry in OGRE_ASSETS:
        mesh = import_skeletal_mesh(entry)
        assign_project_materials(mesh, materials)
        ensure_physics_asset(mesh, entry["physics_asset"])
        ensure_review_lods_skeletal(mesh)
        ensure_skeletal_mesh_sockets(mesh)
        ensure_anim_blueprint(
            entry["anim_blueprint"],
            entry["skeleton"],
            "{}/{}".format(entry["destination"], entry["name"]),
        )
        meshes[entry["name"]] = mesh

    update_startup_level(meshes)
    unreal.log("Aerathea Ogre base import complete.")


main()
