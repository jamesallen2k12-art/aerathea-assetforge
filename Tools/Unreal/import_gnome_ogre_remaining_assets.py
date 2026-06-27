from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MATERIAL_PATH = "/Game/Aerathea/Materials"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
FBX_IMPORT_UNIFORM_SCALE = 0.01
NEXT_SLICE_TAG = "AET_NEXT_SLICE"
REVIEW_TAG = "AET_GNOME_OGRE_REMAINING_REVIEW"


STATIC_ASSETS = [
    {
        "name": "SM_OGR_CrudeTekPylon_A01",
        "source": ROOT / "SourceAssets/Exports/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/SM_OGR_CrudeTekPylon_A01.fbx",
        "destination": "/Game/Aerathea/Props/Ogres/Teknomancy",
        "actor_label": "AET_PROD_OGR_CrudeTekPylon_A01",
        "actor_location": unreal.Vector(-1260.0, -450.0, 0.0),
        "actor_yaw": -10.0,
        "lightmap": 256,
        "sockets": [
            ("socket_core", unreal.Vector(56.0, 0.0, 206.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_top_arc", unreal.Vector(72.0, 0.0, 436.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_conductor_l", unreal.Vector(52.0, 128.0, 354.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_conductor_r", unreal.Vector(52.0, -128.0, 354.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_vent_l", unreal.Vector(-52.0, 96.0, 170.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_vent_r", unreal.Vector(-52.0, -96.0, 170.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_cable_in", unreal.Vector(-56.0, 96.0, 165.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_cable_out", unreal.Vector(60.0, 52.0, 210.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_hit_core", unreal.Vector(88.0, 0.0, 206.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_repair_panel", unreal.Vector(126.0, 0.0, 124.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_ground_sparks", unreal.Vector(18.0, 0.0, 38.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_overload_burst", unreal.Vector(72.0, 0.0, 436.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ],
    },
]

MANTICORE_SOCKET_SPECS = [
    ("socket_head_fx", "head", unreal.Vector(334.0, 0.0, 294.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_mouth_fx", "head", unreal.Vector(374.0, 0.0, 270.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_bite_trace", "jaw", unreal.Vector(386.0, 0.0, 264.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_claw_l", "paw_fl", unreal.Vector(252.0, 86.0, 6.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_claw_r", "paw_fr", unreal.Vector(252.0, -86.0, 6.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_foot_l", "paw_fl", unreal.Vector(196.0, 86.0, 6.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_foot_r", "paw_fr", unreal.Vector(196.0, -86.0, 6.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_wing_l_root", "wing_l_root", unreal.Vector(78.0, 58.0, 208.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_wing_r_root", "wing_r_root", unreal.Vector(78.0, -58.0, 208.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_wing_l_tip", "wing_l_tip", unreal.Vector(-174.0, 520.0, 118.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_wing_r_tip", "wing_r_tip", unreal.Vector(-174.0, -520.0, 118.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_tail_base", "tail_01", unreal.Vector(-150.0, 0.0, 140.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_tail_mid", "tail_04", unreal.Vector(-190.0, 0.0, 454.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_tail_stinger", "tail_stinger_tip", unreal.Vector(150.0, 0.0, 394.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_vfx_venom_drip", "tail_stinger_tip", unreal.Vector(142.0, 0.0, 404.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_vfx_landing_dust", "root", unreal.Vector(42.0, 0.0, 6.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("socket_back_variant", "spine_02", unreal.Vector(30.0, 0.0, 224.0), unreal.Rotator(0.0, 0.0, 0.0)),
]

OGRE_COMMON_SOCKET_SPECS = [
    ("hand_r_weapon", "hand_r", unreal.Vector(40.0, -20.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("hand_l_offhand", "hand_l", unreal.Vector(40.0, 20.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("hand_r_twohand_grip", "hand_r", unreal.Vector(52.0, -12.0, 12.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("hand_l_twohand_grip", "hand_l", unreal.Vector(52.0, 12.0, 12.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("back_large_weapon", "chest", unreal.Vector(-48.0, -24.0, -4.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("back_shield", "chest", unreal.Vector(-52.0, 24.0, -10.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_mouth", "head", unreal.Vector(48.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_stomp_ground", "root", unreal.Vector(64.0, 0.0, 4.0), unreal.Rotator(0.0, 0.0, 0.0)),
]

SHAMAN_SOCKET_SPECS = OGRE_COMMON_SOCKET_SPECS + [
    ("vfx_staff_head", "hand_r", unreal.Vector(142.0, -100.0, 220.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_rune_wheel", "chest", unreal.Vector(-96.0, 0.0, 28.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_totem_chest", "chest", unreal.Vector(80.0, 0.0, -8.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("weapon_staff_r", "hand_r", unreal.Vector(84.0, -100.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("head_fx", "head", unreal.Vector(48.0, 0.0, 10.0), unreal.Rotator(0.0, 0.0, 0.0)),
]

NECROMANCER_SOCKET_SPECS = OGRE_COMMON_SOCKET_SPECS + [
    ("vfx_lantern_core", "hand_r", unreal.Vector(132.0, -100.0, 172.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_chest_necro", "chest", unreal.Vector(88.0, 0.0, -8.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_bracer_l", "lowerarm_l", unreal.Vector(42.0, 18.0, 8.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("vfx_bracer_r", "lowerarm_r", unreal.Vector(42.0, -18.0, 8.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("weapon_staff_r", "hand_r", unreal.Vector(84.0, -100.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
    ("head_fx", "head", unreal.Vector(48.0, 0.0, 10.0), unreal.Rotator(0.0, 0.0, 0.0)),
]

SKELETAL_ASSETS = [
    {
        "name": "SK_CRE_Manticore_A01",
        "source": ROOT / "SourceAssets/Exports/Creatures/Manticores/SK_CRE_Manticore_A01/SK_CRE_Manticore_A01.fbx",
        "destination": "/Game/Aerathea/Creatures/Manticores/Base",
        "physics_asset": "/Game/Aerathea/Creatures/Manticores/Base/PHYS_CRE_Manticore_A01",
        "anim_blueprint": "/Game/Aerathea/Creatures/Manticores/Base/ABP_CRE_Manticore_A01",
        "skeleton": None,
        "expected_skeleton": "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01_Skeleton",
        "actor_label": "AET_PROD_CRE_Manticore_A01",
        "actor_location": unreal.Vector(-1230.0, 280.0, 0.0),
        "actor_yaw": 18.0,
        "socket_specs": MANTICORE_SOCKET_SPECS,
    },
    {
        "name": "SK_CRE_Manticore_Interrupt_A01",
        "source": ROOT / "SourceAssets/Exports/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01/SK_CRE_Manticore_Interrupt_A01.fbx",
        "destination": "/Game/Aerathea/Creatures/Manticores",
        "physics_asset": "/Game/Aerathea/Creatures/Manticores/PHYS_CRE_Manticore_Interrupt_A01",
        "anim_blueprint": "/Game/Aerathea/Creatures/Manticores/Base/ABP_CRE_Manticore_A01",
        "skeleton": "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01_Skeleton",
        "expected_skeleton": "/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01_Skeleton",
        "actor_label": "AET_PROD_CRE_Manticore_Interrupt_A01",
        "actor_location": unreal.Vector(-1230.0, 890.0, 0.0),
        "actor_yaw": -18.0,
        "socket_specs": MANTICORE_SOCKET_SPECS,
    },
    {
        "name": "SK_OGR_Shaman_A01",
        "source": ROOT / "SourceAssets/Exports/Characters/Ogres/Shaman/SK_OGR_Shaman_A01/SK_OGR_Shaman_A01.fbx",
        "destination": "/Game/Aerathea/Characters/Ogres/Shaman",
        "physics_asset": "/Game/Aerathea/Characters/Ogres/Shaman/PHYS_OGR_Shaman_A01",
        "anim_blueprint": "/Game/Aerathea/Characters/Ogres/Shaman/ABP_OGR_Shaman_A01",
        "skeleton": "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
        "expected_skeleton": "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
        "actor_label": "AET_PROD_OgreShaman_A01",
        "actor_location": unreal.Vector(-260.0, -1240.0, 0.0),
        "actor_yaw": 116.0,
        "socket_specs": SHAMAN_SOCKET_SPECS,
    },
    {
        "name": "SK_OGR_Necromancer_A01",
        "source": ROOT / "SourceAssets/Exports/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01/SK_OGR_Necromancer_A01.fbx",
        "destination": "/Game/Aerathea/Characters/Ogres/Necromancer",
        "physics_asset": "/Game/Aerathea/Characters/Ogres/Necromancer/PHYS_OGR_Necromancer_A01",
        "anim_blueprint": "/Game/Aerathea/Characters/Ogres/Necromancer/ABP_OGR_Necromancer_A01",
        "skeleton": "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
        "expected_skeleton": "/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton",
        "actor_label": "AET_PROD_OgreNecromancer_A01",
        "actor_location": unreal.Vector(-40.0, -1300.0, 0.0),
        "actor_yaw": 116.0,
        "socket_specs": NECROMANCER_SOCKET_SPECS,
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


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def try_call(obj, method_name):
    method = getattr(obj, method_name, None)
    if not callable(method):
        return None
    try:
        return method()
    except Exception:
        return None


def skeletal_mesh_skeleton(mesh):
    skeleton = try_call(mesh, "get_skeleton")
    if skeleton is not None:
        return skeleton
    try:
        return mesh.get_editor_property("skeleton")
    except Exception:
        return None


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
    materials = {
        "M_OGR_CairnStone_Blockout_A01": color_material("M_OGR_CairnStone_Blockout_A01", unreal.LinearColor(0.24, 0.25, 0.24, 1.0)),
        "M_OGR_Iron_Blockout_A01": color_material("M_OGR_Iron_Blockout_A01", unreal.LinearColor(0.10, 0.10, 0.09, 1.0), roughness=0.68, metallic=0.55),
        "M_OGR_Brass_Blockout_A01": color_material("M_OGR_Brass_Blockout_A01", unreal.LinearColor(0.60, 0.34, 0.13, 1.0), roughness=0.58, metallic=0.65),
        "M_OGR_SootedCopper_Blockout_A01": color_material("M_OGR_SootedCopper_Blockout_A01", unreal.LinearColor(0.40, 0.18, 0.075, 1.0), roughness=0.65, metallic=0.55),
        "M_OGR_Leather_Blockout_A01": color_material("M_OGR_Leather_Blockout_A01", unreal.LinearColor(0.20, 0.11, 0.07, 1.0)),
        "M_OGR_Warpaint_Blockout_A01": color_material("M_OGR_Warpaint_Blockout_A01", unreal.LinearColor(0.28, 0.075, 0.035, 1.0)),
        "M_OGR_TekGlow_Blockout_A01": color_material("M_OGR_TekGlow_Blockout_A01", unreal.LinearColor(1.0, 0.36, 0.025, 1.0), roughness=0.25, emissive=unreal.LinearColor(2.5, 0.55, 0.03, 1.0)),
        "M_OGR_Skin_Blockout_A01": color_material("M_OGR_Skin_Blockout_A01", unreal.LinearColor(0.48, 0.40, 0.31, 1.0)),
        "M_OGR_Bone_Blockout_A01": color_material("M_OGR_Bone_Blockout_A01", unreal.LinearColor(0.66, 0.58, 0.43, 1.0)),
        "M_OGR_AetheriumGlow_Blockout_A01": color_material("M_OGR_AetheriumGlow_Blockout_A01", unreal.LinearColor(0.0, 0.55, 1.0, 1.0), roughness=0.25, emissive=unreal.LinearColor(0.0, 1.1, 2.5, 1.0)),
        "M_OGR_NecroGlow_Blockout_A01": color_material("M_OGR_NecroGlow_Blockout_A01", unreal.LinearColor(0.16, 0.95, 0.28, 1.0), roughness=0.25, emissive=unreal.LinearColor(0.08, 1.6, 0.25, 1.0)),
        "M_OGR_RuneGlow_Blockout_A01": color_material("M_OGR_RuneGlow_Blockout_A01", unreal.LinearColor(0.15, 0.62, 1.0, 1.0), roughness=0.25, emissive=unreal.LinearColor(0.15, 1.15, 2.0, 1.0)),
        "M_OGR_StormRuneGlow_Blockout_A01": color_material("M_OGR_StormRuneGlow_Blockout_A01", unreal.LinearColor(0.26, 0.82, 1.0, 1.0), roughness=0.25, emissive=unreal.LinearColor(0.26, 1.45, 2.2, 1.0)),
        "M_OGR_ShamanStone_Blockout_A01": color_material("M_OGR_ShamanStone_Blockout_A01", unreal.LinearColor(0.31, 0.32, 0.29, 1.0)),
        "M_OGR_FurMantle_Blockout_A01": color_material("M_OGR_FurMantle_Blockout_A01", unreal.LinearColor(0.28, 0.20, 0.13, 1.0)),
        "M_OGR_GraveCloth_Blockout_A01": color_material("M_OGR_GraveCloth_Blockout_A01", unreal.LinearColor(0.055, 0.055, 0.052, 1.0)),
        "M_OGR_TombMetal_Blockout_A01": color_material("M_OGR_TombMetal_Blockout_A01", unreal.LinearColor(0.095, 0.11, 0.10, 1.0), roughness=0.72, metallic=0.48),
        "M_CRE_Manticore_Body_Blockout_A01": color_material("M_CRE_Manticore_Body_Blockout_A01", unreal.LinearColor(0.50, 0.32, 0.15, 1.0)),
        "M_CRE_Manticore_Mane_Blockout_A01": color_material("M_CRE_Manticore_Mane_Blockout_A01", unreal.LinearColor(0.10, 0.07, 0.045, 1.0)),
        "M_CRE_Manticore_Wing_Blockout_A01": color_material("M_CRE_Manticore_Wing_Blockout_A01", unreal.LinearColor(0.20, 0.075, 0.055, 1.0)),
        "M_CRE_Manticore_TailClaw_Blockout_A01": color_material("M_CRE_Manticore_TailClaw_Blockout_A01", unreal.LinearColor(0.17, 0.13, 0.095, 1.0)),
        "M_CRE_Manticore_Venom_Blockout_A01": color_material("M_CRE_Manticore_Venom_Blockout_A01", unreal.LinearColor(0.18, 0.95, 0.30, 1.0), roughness=0.25, emissive=unreal.LinearColor(0.12, 1.45, 0.28, 1.0)),
    }
    return materials


def material_instance_name(mesh_name, material_name):
    asset_name = mesh_name[3:] if mesh_name.startswith(("SM_", "SK_")) else mesh_name
    semantic = material_name
    for prefix in ("M_OGR_", "M_CRE_", "M_AET_"):
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
    for prop in ("static_materials", "materials"):
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
            unreal.log_warning("No project material match for {} slot {}".format(mesh.get_name(), slot_name))
            continue
        instance = ensure_material_instance(material_instance_name(mesh.get_name(), base_material.get_name()), base_material)
        setter = getattr(mesh, "set_material", None)
        if callable(setter):
            setter(index, instance)
        else:
            slot.set_editor_property("material_interface", instance)
            edited_slots = True
    if edited_slots:
        try:
            mesh.set_editor_property("materials", slots)
        except Exception:
            mesh.set_editor_property("static_materials", slots)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log("Synced {} material slots for {}".format(len(slots), mesh.get_name()))


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
    safe_set(mesh, "light_map_resolution", entry.get("lightmap", 128))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return mesh


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
    skeleton_path = entry.get("skeleton")
    if skeleton_path:
        skeleton = unreal.load_asset(skeleton_path)
        if skeleton is None:
            raise RuntimeError("Missing skeleton for import: {}".format(skeleton_path))
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
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return mesh


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


def remove_static_socket(mesh, name):
    finder = getattr(mesh, "find_socket", None)
    remover = getattr(mesh, "remove_socket", None)
    if not callable(finder) or not callable(remover):
        return
    existing = finder(unreal.Name(name))
    if existing is None:
        return
    try:
        remover(existing)
    except TypeError:
        remover(unreal.Name(name))


def ensure_static_mesh_sockets(mesh, socket_specs):
    for name, _location, _rotation in socket_specs:
        remove_static_socket(mesh, name)
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


def remove_skeletal_socket(mesh, name):
    socket_name = unreal.Name(name)
    if mesh.find_socket(socket_name) is not None and not mesh.remove_socket(socket_name):
        raise RuntimeError("Failed to remove existing socket {} from {}".format(name, mesh.get_name()))


def ensure_skeletal_mesh_sockets(mesh, socket_specs):
    for socket_name, _bone_name, _location, _rotation in socket_specs:
        remove_skeletal_socket(mesh, socket_name)
        remove_skeletal_socket(mesh, "SOCKET_{}".format(socket_name))
    for socket_name, bone_name, location, rotation in socket_specs:
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


def log_skeleton_binding(mesh, expected_skeleton_path):
    skeleton = skeletal_mesh_skeleton(mesh)
    if skeleton is None:
        raise RuntimeError("{} has no skeleton after import.".format(mesh.get_name()))
    skeleton_path = asset_path_without_object(skeleton)
    if skeleton_path != expected_skeleton_path:
        raise RuntimeError("{} is bound to {}, expected {}".format(mesh.get_name(), skeleton_path, expected_skeleton_path))
    unreal.log("{} bound to expected skeleton {}.".format(mesh.get_name(), expected_skeleton_path))


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
    for tag_name in (NEXT_SLICE_TAG, REVIEW_TAG):
        tag = unreal.Name(tag_name)
        if tag not in tags:
            tags.append(tag)
    actor.set_editor_property("tags", tags)
    return actor


def activate_actor_for_review(actor):
    try:
        actor.set_actor_hidden_in_game(False)
        actor.set_is_temporarily_hidden_in_editor(False)
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            component.set_visibility(True, True)
            component.set_hidden_in_game(False, True)
            if component.get_class().get_name() in {"BoxComponent", "CapsuleComponent", "SphereComponent"}:
                component.set_visibility(False, True)
                component.set_hidden_in_game(True, True)
    except Exception:
        pass
    return actor


def spawn_static_mesh_actor(entry, mesh):
    actor = find_actor_by_label(entry["actor_label"])
    if actor is None or actor.get_class().get_name() != "StaticMeshActor":
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.StaticMeshActor,
            entry["actor_location"],
            unreal.Rotator(0.0, entry["actor_yaw"], 0.0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(entry["actor_label"]))
    actor.set_actor_label(entry["actor_label"])
    actor.set_actor_location(entry["actor_location"], False, True)
    actor.set_actor_rotation(unreal.Rotator(0.0, entry["actor_yaw"], 0.0), False)
    actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
    tag_actor(actor)
    activate_actor_for_review(actor)
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("Static mesh actor has no StaticMeshComponent: {}".format(entry["actor_label"]))
    component.set_static_mesh(mesh)
    component.set_mobility(unreal.ComponentMobility.STATIC)
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


def spawn_skeletal_mesh_actor(entry, mesh):
    actor = find_actor_by_label(entry["actor_label"])
    if actor is None or actor.get_class().get_name() != "SkeletalMeshActor":
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.SkeletalMeshActor,
            entry["actor_location"],
            unreal.Rotator(0.0, entry["actor_yaw"], 0.0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn skeletal mesh actor: {}".format(entry["actor_label"]))
    actor.set_actor_label(entry["actor_label"])
    actor.set_actor_location(entry["actor_location"], False, False)
    actor.set_actor_rotation(unreal.Rotator(0.0, entry["actor_yaw"], 0.0), False)
    actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
    tag_actor(actor)
    activate_actor_for_review(actor)
    component = actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if component is None:
        raise RuntimeError("Skeletal mesh actor has no SkeletalMeshComponent: {}".format(entry["actor_label"]))
    set_skeletal_mesh_component(component, mesh)
    return actor


def update_startup_level(imported_static, imported_skeletal):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))
    for entry, mesh in imported_static:
        spawn_static_mesh_actor(entry, mesh)
    for entry, mesh in imported_skeletal:
        spawn_skeletal_mesh_actor(entry, mesh)
    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")
    for directory in {entry["destination"] for entry in STATIC_ASSETS + SKELETAL_ASSETS} | {MATERIAL_PATH, MATERIAL_INSTANCE_PATH}:
        unreal.EditorAssetLibrary.save_directory(directory, only_if_is_dirty=True, recursive=True)


def main():
    materials = ensure_materials()
    imported_static = []
    imported_skeletal = []

    for entry in STATIC_ASSETS:
        mesh = import_static_mesh(entry)
        assign_project_materials(mesh, materials)
        ensure_review_lods_static(mesh)
        ensure_static_mesh_sockets(mesh, entry["sockets"])
        imported_static.append((entry, mesh))

    for entry in SKELETAL_ASSETS:
        mesh = import_skeletal_mesh(entry)
        assign_project_materials(mesh, materials)
        log_skeleton_binding(mesh, entry["expected_skeleton"])
        ensure_physics_asset(mesh, entry["physics_asset"])
        ensure_review_lods_skeletal(mesh)
        ensure_skeletal_mesh_sockets(mesh, entry["socket_specs"])
        ensure_anim_blueprint(
            entry["anim_blueprint"],
            entry["expected_skeleton"],
            "{}/{}".format(entry["destination"], entry["name"]),
        )
        imported_skeletal.append((entry, mesh))

    update_startup_level(imported_static, imported_skeletal)
    unreal.log("Aerathea Gnome/Ogre remaining asset import complete.")


main()
