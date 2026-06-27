from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MATERIAL_PATH = "/Game/Aerathea/Materials"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
TEKNOMANCER_TAG = "AET_OGRE_TEKNOMANCER_REVIEW"
FBX_IMPORT_UNIFORM_SCALE = 0.01


TEKNOMANCER_ASSET = {
    "name": "SK_OGR_Teknomancer_A01",
    "source": ROOT / "SourceAssets/Exports/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01/SK_OGR_Teknomancer_A01.fbx",
    "destination": "/Game/Aerathea/Characters/Ogres/Teknomancer",
    "physics_asset": "/Game/Aerathea/Characters/Ogres/Teknomancer/PHYS_OGR_Teknomancer_A01",
    "anim_blueprint": "/Game/Aerathea/Characters/Ogres/Teknomancer/ABP_OGR_Teknomancer_A01",
    "skeleton": "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
    "actor_label": "AET_PROD_OgreTeknomancer_A01",
    "actor_location": unreal.Vector(130.0, -150.0, 0.0),
    "actor_yaw": 126.0,
}


TEKNOMANCER_SOCKET_SPECS = [
    ("hand_r_weapon", "hand_r", unreal.Vector(40.0, -20.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("hand_l_offhand", "hand_l", unreal.Vector(40.0, 20.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("hand_r_twohand_grip", "hand_r", unreal.Vector(52.0, -12.0, 12.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("hand_l_twohand_grip", "hand_l", unreal.Vector(52.0, 12.0, 12.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("spine_teknomancy_pack", "chest", unreal.Vector(-46.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_chest_core", "chest", unreal.Vector(52.0, 0.0, -18.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_mouth", "head", unreal.Vector(48.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_stomp_ground", "root", unreal.Vector(64.0, 0.0, 4.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_hammer_core", "hand_r", unreal.Vector(122.0, -21.0, -42.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_bracer_l", "lowerarm_l", unreal.Vector(42.0, 18.0, 8.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_bracer_r", "lowerarm_r", unreal.Vector(42.0, -18.0, 8.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_tek_core", "pelvis", unreal.Vector(72.0, 0.0, 18.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("weapon_socket_r", "hand_r", unreal.Vector(82.0, -18.0, -10.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("head_fx", "head", unreal.Vector(48.0, 0.0, 10.0), unreal.Rotator(0.0, 0.0, 0.0)),
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


def color_material(name, color, roughness=0.85, metallic=0.0, emissive=None, use_with_skeletal_mesh=True):
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

    configure_material_usage(material, use_with_skeletal_mesh=use_with_skeletal_mesh)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    return material


def ensure_materials():
    return {
        "M_OGR_Skin_Blockout_A01": color_material("M_OGR_Skin_Blockout_A01", unreal.LinearColor(0.48, 0.40, 0.31, 1.0)),
        "M_OGR_Warpaint_Blockout_A01": color_material("M_OGR_Warpaint_Blockout_A01", unreal.LinearColor(0.24, 0.10, 0.06, 1.0)),
        "M_OGR_Leather_Blockout_A01": color_material("M_OGR_Leather_Blockout_A01", unreal.LinearColor(0.20, 0.11, 0.07, 1.0)),
        "M_OGR_Iron_Blockout_A01": color_material(
            "M_OGR_Iron_Blockout_A01",
            unreal.LinearColor(0.12, 0.12, 0.11, 1.0),
            roughness=0.7,
            metallic=0.55,
        ),
        "M_OGR_Brass_Blockout_A01": color_material(
            "M_OGR_Brass_Blockout_A01",
            unreal.LinearColor(0.64, 0.36, 0.16, 1.0),
            roughness=0.55,
            metallic=0.7,
        ),
        "M_OGR_Bone_Blockout_A01": color_material("M_OGR_Bone_Blockout_A01", unreal.LinearColor(0.66, 0.58, 0.43, 1.0)),
        "M_OGR_AetheriumGlow_Blockout_A01": color_material(
            "M_OGR_AetheriumGlow_Blockout_A01",
            unreal.LinearColor(0.0, 0.55, 1.0, 1.0),
            roughness=0.25,
            emissive=unreal.LinearColor(0.0, 1.1, 2.5, 1.0),
        ),
        "M_OGR_NecroGlow_Blockout_A01": color_material(
            "M_OGR_NecroGlow_Blockout_A01",
            unreal.LinearColor(0.16, 0.95, 0.28, 1.0),
            roughness=0.3,
            emissive=unreal.LinearColor(0.08, 1.6, 0.25, 1.0),
        ),
        "M_OGR_TekGlow_Blockout_A01": color_material(
            "M_OGR_TekGlow_Blockout_A01",
            unreal.LinearColor(1.0, 0.36, 0.03, 1.0),
            roughness=0.25,
            emissive=unreal.LinearColor(2.0, 0.55, 0.03, 1.0),
        ),
        "M_OGR_SootedCopper_Blockout_A01": color_material(
            "M_OGR_SootedCopper_Blockout_A01",
            unreal.LinearColor(0.40, 0.18, 0.075, 1.0),
            roughness=0.65,
            metallic=0.55,
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
    try:
        return list(mesh.get_editor_property("materials"))
    except Exception:
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
        setter = getattr(mesh, "set_material", None)
        if callable(setter):
            setter(index, material)
        else:
            slot.set_editor_property("material_interface", material)
            edited_slots = True
    if edited_slots:
        mesh.set_editor_property("materials", slots)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log("Synced {} Teknomancer material slots for {}".format(len(slots), mesh.get_name()))


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
    skeleton = unreal.load_asset(entry["skeleton"])
    if skeleton is not None:
        safe_set(fbx_ui, "skeleton", skeleton)
    skeletal_data = fbx_ui.skeletal_mesh_import_data
    safe_set(skeletal_data, "import_morph_targets", False)
    safe_set(skeletal_data, "update_skeleton_reference_pose", False)
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
    return mesh


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def skeletal_mesh_skeleton(mesh):
    getter = getattr(mesh, "get_skeleton", None)
    if callable(getter):
        try:
            return getter()
        except Exception:
            pass
    try:
        return mesh.get_editor_property("skeleton")
    except Exception:
        return None


def log_skeleton_binding(mesh, expected_skeleton_path):
    skeleton = skeletal_mesh_skeleton(mesh)
    if skeleton is None:
        unreal.log_warning("{} has no skeleton after import.".format(mesh.get_name()))
        return
    skeleton_path = asset_path_without_object(skeleton)
    if skeleton_path != expected_skeleton_path:
        unreal.log_warning(
            "{} is bound to {}, expected {}. Final rig pass must resolve this before production animation.".format(
                mesh.get_name(),
                skeleton_path,
                expected_skeleton_path,
            )
        )
        return
    unreal.log("{} bound to expected skeleton {}.".format(mesh.get_name(), expected_skeleton_path))


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
    if smes.get_lod_count(mesh) < target_lods:
        try:
            smes.regenerate_lod(
                skeletal_mesh=mesh,
                new_lod_count=target_lods,
                regenerate_even_if_imported=True,
                generate_base_lod=False,
            )
        except TypeError:
            smes.regenerate_lod(mesh, target_lods, True, False)
    if smes.get_lod_count(mesh) < target_lods:
        raise RuntimeError("{} has fewer than {} LODs".format(mesh.get_name(), target_lods))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def remove_socket_name(mesh, name):
    socket_name = unreal.Name(name)
    if mesh.find_socket(socket_name) is not None and not mesh.remove_socket(socket_name):
        raise RuntimeError("Failed to remove existing socket {} from {}".format(name, mesh.get_name()))


def ensure_skeletal_mesh_sockets(mesh):
    for socket_name, _bone_name, _location, _rotation in TEKNOMANCER_SOCKET_SPECS:
        remove_socket_name(mesh, socket_name)
        remove_socket_name(mesh, "SOCKET_{}".format(socket_name))

    for socket_name, bone_name, location, rotation in TEKNOMANCER_SOCKET_SPECS:
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


def review_rotator(pitch, yaw, roll=0.0):
    return unreal.Rotator(roll, pitch, yaw)


def tag_actor(actor):
    tags = list(actor.get_editor_property("tags"))
    for tag in (unreal.Name(TEKNOMANCER_TAG), unreal.Name("AET_NEXT_SLICE")):
        if tag not in tags:
            tags.append(tag)
    actor.set_editor_property("tags", tags)
    return actor


def activate_actor_for_review(actor):
    try:
        actor.set_actor_hidden_in_game(False)
        actor.set_is_temporarily_hidden_in_editor(False)
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            if component.get_class().get_name() in {"BoxComponent", "CapsuleComponent", "SphereComponent"}:
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


def spawn_skeletal_mesh(entry, mesh):
    actor = find_actor_by_label(entry["actor_label"])
    if actor is None or actor.get_class().get_name() != "SkeletalMeshActor":
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.SkeletalMeshActor,
            entry["actor_location"],
            review_rotator(0.0, entry["actor_yaw"]),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn skeletal mesh actor: {}".format(entry["actor_label"]))
    actor.set_actor_label(entry["actor_label"])
    actor.set_actor_location(entry["actor_location"], False, False)
    actor.set_actor_rotation(review_rotator(0.0, entry["actor_yaw"]), False)
    actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
    tag_actor(actor)
    activate_actor_for_review(actor)
    component = actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if component is None:
        raise RuntimeError("Skeletal mesh actor has no SkeletalMeshComponent: {}".format(entry["actor_label"]))
    set_skeletal_mesh_component(component, mesh)
    return actor


def update_startup_level(mesh):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))
    spawn_skeletal_mesh(TEKNOMANCER_ASSET, mesh)
    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")
    for directory in (
        TEKNOMANCER_ASSET["destination"],
        MATERIAL_PATH,
        MATERIAL_INSTANCE_PATH,
    ):
        unreal.EditorAssetLibrary.save_directory(directory, only_if_is_dirty=True, recursive=True)


def main():
    materials = ensure_materials()
    mesh = import_skeletal_mesh(TEKNOMANCER_ASSET)
    log_skeleton_binding(mesh, TEKNOMANCER_ASSET["skeleton"])
    assign_project_materials(mesh, materials)
    ensure_physics_asset(mesh, TEKNOMANCER_ASSET["physics_asset"])
    ensure_review_lods_skeletal(mesh)
    ensure_skeletal_mesh_sockets(mesh)
    ensure_anim_blueprint(
        TEKNOMANCER_ASSET["anim_blueprint"],
        TEKNOMANCER_ASSET["skeleton"],
        "{}/{}".format(TEKNOMANCER_ASSET["destination"], TEKNOMANCER_ASSET["name"]),
    )
    update_startup_level(mesh)
    unreal.log("Aerathea Ogre Teknomancer import complete.")


main()
