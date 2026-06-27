import os
from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MATERIAL_PATH = "/Game/Aerathea/Materials"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
NEXT_SLICE_TAG = "AET_NEXT_SLICE"
# Blender source meshes are authored in centimeters and exported without FBX unit
# conversion, so Unreal must import the raw FBX geometry at 1 cm = 1 Unreal cm.
FBX_IMPORT_UNIFORM_SCALE = 0.01


STATIC_ASSETS = [
    {
        "name": "SM_MKG_MultiTool_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_MultiTool_A01/SM_MKG_MultiTool_A01.fbx",
        "destination": "/Game/Aerathea/Props/Mekgineer/Armory",
    },
    {
        "name": "SM_MKG_GrappleHook_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_GrappleHook_A01/SM_MKG_GrappleHook_A01.fbx",
        "destination": "/Game/Aerathea/Props/Mekgineer/Armory",
    },
    {
        "name": "SM_MKG_SpikeDrill_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_SpikeDrill_A01/SM_MKG_SpikeDrill_A01.fbx",
        "destination": "/Game/Aerathea/Weapons/Mekgineer",
    },
    {
        "name": "SM_MKG_MonkeyWrench_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_MonkeyWrench_A01/SM_MKG_MonkeyWrench_A01.fbx",
        "destination": "/Game/Aerathea/Weapons/Mekgineer",
    },
    {
        "name": "SM_MKG_RatchetCleaver_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_RatchetCleaver_A01/SM_MKG_RatchetCleaver_A01.fbx",
        "destination": "/Game/Aerathea/Weapons/Mekgineer",
    },
    {
        "name": "SM_MKG_GearMace_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_GearMace_A01/SM_MKG_GearMace_A01.fbx",
        "destination": "/Game/Aerathea/Weapons/Mekgineer",
    },
    {
        "name": "SM_MKG_ToolPack_A01",
        "source": ROOT / "SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_ToolPack_A01/SM_MKG_ToolPack_A01.fbx",
        "destination": "/Game/Aerathea/Props/Mekgineer/Armory",
    },
    {
        "name": "SM_AET_Palisade_Wall_A01",
        "source": ROOT / "SourceAssets/Exports/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Wall_A01/SM_AET_Palisade_Wall_A01.fbx",
        "destination": "/Game/Aerathea/Buildings/Common/Palisade",
    },
    {
        "name": "SM_AET_Palisade_Post_A01",
        "source": ROOT / "SourceAssets/Exports/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Post_A01/SM_AET_Palisade_Post_A01.fbx",
        "destination": "/Game/Aerathea/Buildings/Common/Palisade",
    },
    {
        "name": "SM_AET_Palisade_Corner_A01",
        "source": ROOT / "SourceAssets/Exports/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Corner_A01/SM_AET_Palisade_Corner_A01.fbx",
        "destination": "/Game/Aerathea/Buildings/Common/Palisade",
    },
    {
        "name": "SM_AET_Palisade_Gate_A01",
        "source": ROOT / "SourceAssets/Exports/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_Gate_A01/SM_AET_Palisade_Gate_A01.fbx",
        "destination": "/Game/Aerathea/Buildings/Common/Palisade",
    },
    {
        "name": "SM_AET_Palisade_EndCap_A01",
        "source": ROOT / "SourceAssets/Exports/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_EndCap_A01/SM_AET_Palisade_EndCap_A01.fbx",
        "destination": "/Game/Aerathea/Buildings/Common/Palisade",
    },
]

STATIC_MESH_SOCKET_SETS = {
    "SM_MKG_GrappleHook_A01": [
        ("socket_muzzle", unreal.Vector(76.0, 0.0, 3.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("socket_beam", unreal.Vector(86.0, 0.0, 3.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ("socket_cable", unreal.Vector(-54.0, 0.0, 0.0), unreal.Rotator(0.0, 180.0, 0.0)),
    ],
}

SKELETAL_ASSETS = [
    {
        "name": "SK_GNM_Base_A01",
        "source": ROOT / "SourceAssets/Exports/Characters/Gnomes/SK_GNM_Base_A01/SK_GNM_Base_A01.fbx",
        "destination": "/Game/Aerathea/Characters/Gnomes/Base",
        "import_animations": False,
        "physics_asset": "/Game/Aerathea/Characters/Gnomes/Base/PHYS_GNM_Base_A01",
    },
    {
        "name": "SK_CRE_Gryphon_A01",
        "source": ROOT / "SourceAssets/Exports/Creatures/Gryphon/SK_CRE_Gryphon_A01/SK_CRE_Gryphon_A01.fbx",
        "destination": "/Game/Aerathea/Creatures/Gryphon/Base",
        "import_animations": True,
        "physics_asset": "/Game/Aerathea/Creatures/Gryphon/Base/PHYS_CRE_Gryphon_A01",
    },
]

SKELETON_SOCKET_SETS = [
    {
        "skeleton": "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01_Skeleton",
        "mesh": "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01",
        "anim_blueprint": "/Game/Aerathea/Characters/Gnomes/Base/ABP_GNM_Base_A01",
        "sockets": [
            ("hand_r_weapon", "hand_r", unreal.Vector(2.0, -4.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("hand_l_offhand", "hand_l", unreal.Vector(2.0, 4.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("back_pack", "chest", unreal.Vector(-10.0, 0.0, -2.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("head_goggles", "head", unreal.Vector(8.0, 0.0, 2.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("belt_tool_l", "pelvis", unreal.Vector(0.0, 13.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("belt_tool_r", "pelvis", unreal.Vector(0.0, -13.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("muzzle_preview", "hand_r", unreal.Vector(8.0, -4.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("vfx_aether_core", "chest", unreal.Vector(8.0, 0.0, 4.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ],
    },
    {
        "skeleton": "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01_Skeleton",
        "mesh": "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01",
        "anim_blueprint": "/Game/Aerathea/Creatures/Gryphon/Base/ABP_CRE_Gryphon_A01",
        "sockets": [
            ("socket_head_vfx", "head", unreal.Vector(12.0, 0.0, 5.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_beak", "head", unreal.Vector(20.0, 0.0, -2.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_talon_l", "forefoot_l", unreal.Vector(8.0, 0.0, -2.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_talon_r", "forefoot_r", unreal.Vector(8.0, 0.0, -2.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_back_mount", "spine", unreal.Vector(-4.0, 0.0, 16.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_saddle", "spine", unreal.Vector(-4.0, 0.0, 20.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_wing_l_vfx", "wing_l_lower", unreal.Vector(-12.0, 18.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_wing_r_vfx", "wing_r_lower", unreal.Vector(-12.0, -18.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
            ("socket_tail", "tail_02", unreal.Vector(-10.0, 0.0, 0.0), unreal.Rotator(0.0, 0.0, 0.0)),
        ],
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
                unreal.log_warning("Could not set skeletal material usage through MaterialEditingLibrary: {}".format(exc))
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

    mat_lib.recompile_material(material)
    configure_material_usage(material, use_with_skeletal_mesh=use_with_skeletal_mesh)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    return material


def material_instance_name(mesh_name, material_name):
    asset_name = mesh_name
    for prefix in ("SM_", "SK_"):
        if asset_name.startswith(prefix):
            asset_name = asset_name[len(prefix):]
            break
    semantic = material_name
    for prefix in ("M_AET_", "M_GNM_", "M_CRE_"):
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


def ensure_materials(include_skeletal=True):
    materials = {
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
            emissive=unreal.LinearColor(0.0, 1.2, 3.5, 1.0),
        ),
        "M_AET_Leather_Dark_A01": color_material(
            "M_AET_Leather_Dark_A01",
            unreal.LinearColor(0.19, 0.11, 0.07, 1.0),
        ),
    }
    if not include_skeletal:
        return materials

    materials.update(
        {
        "M_GNM_Skin_Blockout_A01": color_material(
            "M_GNM_Skin_Blockout_A01",
            unreal.LinearColor(0.78, 0.55, 0.38, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_GNM_Workwear_Blockout_A01": color_material(
            "M_GNM_Workwear_Blockout_A01",
            unreal.LinearColor(0.18, 0.24, 0.29, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_GNM_BootLeather_Blockout_A01": color_material(
            "M_GNM_BootLeather_Blockout_A01",
            unreal.LinearColor(0.17, 0.10, 0.06, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_GNM_Eye_Blockout_A01": color_material(
            "M_GNM_Eye_Blockout_A01",
            unreal.LinearColor(0.04, 0.16, 0.28, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_CRE_Gryphon_Feather_Blockout_A01": color_material(
            "M_CRE_Gryphon_Feather_Blockout_A01",
            unreal.LinearColor(0.75, 0.58, 0.24, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_CRE_Gryphon_Fur_Blockout_A01": color_material(
            "M_CRE_Gryphon_Fur_Blockout_A01",
            unreal.LinearColor(0.58, 0.38, 0.16, 1.0),
            use_with_skeletal_mesh=True,
        ),
        "M_CRE_Gryphon_Keratin_Blockout_A01": color_material(
            "M_CRE_Gryphon_Keratin_Blockout_A01",
            unreal.LinearColor(0.78, 0.68, 0.46, 1.0),
            use_with_skeletal_mesh=True,
        ),
        }
    )
    return materials


def ensure_review_lods_static(mesh, target_lods=4):
    options = unreal.EditorScriptingMeshReductionOptions()
    safe_set(options, "auto_compute_lod_screen_size", False)
    settings = []
    for percent, screen_size in ((1.0, 1.0), (0.65, 0.55), (0.35, 0.28), (0.18, 0.12)):
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
    unreal.log("Ensured {} skeletal LODs for {}".format(count, mesh.get_name()))


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
    unreal.log("Imported next-slice static mesh: {}".format(asset_path))
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
    safe_set(fbx_ui, "import_animations", bool(entry["import_animations"]))
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
    unreal.log("Imported next-slice skeletal mesh: {}".format(asset_path))
    return mesh


def material_slots(mesh):
    for prop in ("static_materials", "materials"):
        try:
            return list(mesh.get_editor_property(prop))
        except Exception:
            continue
    return []


def assign_project_materials(mesh, project_materials):
    slots = material_slots(mesh)
    edited_skeletal_slots = False
    for index, slot in enumerate(slots):
        slot_name = str(slot.get_editor_property("material_slot_name"))
        current = slot.get_editor_property("material_interface")
        current_name = current.get_name() if current is not None else slot_name
        base_material = project_materials.get(slot_name) or project_materials.get(current_name)
        if base_material is not None:
            material = ensure_material_instance(
                material_instance_name(mesh.get_name(), base_material.get_name()),
                base_material,
            )
            set_material = getattr(mesh, "set_material", None)
            if callable(set_material):
                set_material(index, material)
            else:
                slot.set_editor_property("material_interface", material)
                edited_skeletal_slots = True
    if edited_skeletal_slots:
        mesh.set_editor_property("materials", slots)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log("Synced {} material slots for {}".format(len(slots), mesh.get_name()))


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
            if unreal.EditorAssetLibrary.does_asset_exist(desired_asset_path):
                existing = unreal.load_asset(desired_asset_path)
            else:
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
    unreal.log("Ensured physics asset {} for {}".format(desired_asset_path, mesh.get_name()))
    return existing


def ensure_skeletal_mesh_sockets(mesh_path, socket_specs):
    mesh = unreal.load_asset(mesh_path)
    if mesh is None:
        raise RuntimeError("Missing skeletal mesh for sockets: {}".format(mesh_path))

    def remove_socket_name(name):
        socket_name = unreal.Name(name)
        if mesh.find_socket(socket_name) is not None and not mesh.remove_socket(socket_name):
            raise RuntimeError("Failed to remove existing socket {} from {}".format(name, mesh_path))

    for socket_name, _bone_name, _location, _rotation in socket_specs:
        remove_socket_name(socket_name)

    for socket_name, bone_name, location, rotation in socket_specs:
        remove_socket_name(socket_name)
        remove_socket_name("Socket")

        socket = unreal.new_object(unreal.SkeletalMeshSocket, outer=mesh)
        socket.set_socket_parent(mesh, unreal.Name(bone_name))
        socket.set_editor_property("relative_location", location)
        socket.set_editor_property("relative_rotation", rotation)
        socket.set_editor_property("relative_scale", unreal.Vector(1.0, 1.0, 1.0))
        mesh.add_socket(socket)

        generated_name = socket.get_editor_property("socket_name")
        if not mesh.rename_socket(generated_name, unreal.Name(socket_name)):
            raise RuntimeError(
                "Failed to rename generated socket {} to {} on {}".format(generated_name, socket_name, mesh_path)
            )

        final_socket = mesh.find_socket(unreal.Name(socket_name))
        if final_socket is None:
            raise RuntimeError("Socket {} was not created on {}".format(socket_name, mesh_path))
        final_socket.set_socket_parent(mesh, unreal.Name(bone_name))
        final_socket.set_editor_property("relative_location", location)
        final_socket.set_editor_property("relative_rotation", rotation)
        final_socket.set_editor_property("relative_scale", unreal.Vector(1.0, 1.0, 1.0))

    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log("Ensured {} mesh sockets on {}".format(len(socket_specs), mesh_path))
    return mesh


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
    unreal.log("Ensured animation Blueprint {}".format(asset_path))
    return asset


def ensure_skeletal_infrastructure():
    for entry in SKELETON_SOCKET_SETS:
        ensure_skeletal_mesh_sockets(entry["mesh"], entry["sockets"])
        ensure_anim_blueprint(entry["anim_blueprint"], entry["skeleton"], entry["mesh"])


def ensure_static_mesh_sockets(mesh, socket_specs):
    for name, location, rotation in socket_specs:
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
    next_tag = unreal.Name(NEXT_SLICE_TAG)
    if next_tag not in tags:
        tags.append(next_tag)
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
            collision_profile = getattr(component, "set_collision_profile_name", None)
            if callable(collision_profile):
                component.set_collision_profile_name("BlockAll")
    except Exception:
        pass
    return actor


def spawn_static_mesh(label, mesh, location, rotation=None, scale=None):
    actor = find_actor_by_label(label)
    if actor is None or actor.get_class().get_name() != "StaticMeshActor":
        if actor is not None:
            retire_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.StaticMeshActor,
            location,
            rotation or unreal.Rotator(0, 0, 0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn static mesh actor: {}".format(label))
    actor.set_actor_label(label)
    set_actor_transform(actor, location, rotation, scale)
    tag_actor(actor)
    activate_actor_for_review(actor)
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("Static mesh actor has no StaticMeshComponent: {}".format(label))
    component.set_static_mesh(mesh)
    return actor


def set_skeletal_mesh_component(component, mesh):
    setter_names = ("set_skeletal_mesh_asset", "set_skeletal_mesh")
    for setter_name in setter_names:
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


def spawn_skeletal_mesh(label, mesh, location, rotation=None, scale=None):
    actor = find_actor_by_label(label)
    if actor is None or actor.get_class().get_name() != "SkeletalMeshActor":
        if actor is not None:
            retire_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.SkeletalMeshActor,
            location,
            rotation or unreal.Rotator(0, 0, 0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn skeletal mesh actor: {}".format(label))
    actor.set_actor_label(label)
    set_actor_transform(actor, location, rotation, scale)
    tag_actor(actor)
    activate_actor_for_review(actor)
    component = actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if component is None:
        raise RuntimeError("Skeletal mesh actor has no SkeletalMeshComponent: {}".format(label))
    set_skeletal_mesh_component(component, mesh)
    return actor


def skeletal_socket_location(actor, socket_name):
    component = actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if component is None:
        raise RuntimeError("{} has no SkeletalMeshComponent".format(actor.get_actor_label()))
    if not component.does_socket_exist(unreal.Name(socket_name)):
        raise RuntimeError("{} is missing socket {}".format(actor.get_actor_label(), socket_name))
    return component.get_socket_location(unreal.Name(socket_name))


def spawn_static_mesh_on_skeletal_socket(label, mesh, skeletal_actor, socket_name, rotation=None, scale=None):
    location = skeletal_socket_location(skeletal_actor, socket_name)
    actor = spawn_static_mesh(label, mesh, location, rotation or skeletal_actor.get_actor_rotation(), scale)
    tag_actor(actor)
    tags = list(actor.get_editor_property("tags"))
    fit_tag = unreal.Name("AET_SOCKET_FIT_PREVIEW")
    if fit_tag not in tags:
        tags.append(fit_tag)
        actor.set_editor_property("tags", tags)
    return actor


def load_blueprint_class(asset_path):
    loader = getattr(unreal.EditorAssetLibrary, "load_blueprint_class", None)
    if callable(loader):
        loaded_class = loader(asset_path)
        if loaded_class is not None:
            return loaded_class
    asset_name = asset_path.rsplit("/", 1)[-1]
    return unreal.load_object(None, "{}.{}_C".format(asset_path, asset_name))


def spawn_target_dummy_blueprint():
    label = "AET_PROD_TargetDummy_A01"
    asset_path = "/Game/Aerathea/Blueprints/Props/BP_AET_TargetDummy_A01"
    bp_class = load_blueprint_class(asset_path)
    if bp_class is None:
        fallback = getattr(unreal, "AETTargetDummyActor", None)
        if fallback is None:
            raise RuntimeError("Could not load target dummy Blueprint class or AAETTargetDummyActor")
        bp_class = fallback

    actor = find_actor_by_label(label)
    class_name = actor.get_class().get_name() if actor is not None else ""
    if actor is None or "BP_AET_TargetDummy_A01" not in class_name:
        if actor is not None:
            retire_actor(actor)
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
            bp_class,
            unreal.Vector(-50, 350, 0),
            unreal.Rotator(0, 0, 0),
        )
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(label))
    actor.set_actor_label(label)
    set_actor_transform(actor, unreal.Vector(-50, 350, 0))
    tag_actor(actor)
    activate_actor_for_review(actor)
    unreal.log("Ensured startup target dummy uses {}".format(actor.get_class().get_name()))
    return actor


def update_startup_level(meshes, skeletal_meshes):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    spawn_target_dummy_blueprint()
    spawn_static_mesh(
        "AET_PROD_MKG_MultiTool_A01",
        meshes["SM_MKG_MultiTool_A01"],
        unreal.Vector(-310, 95, 32),
        rotation=review_rotator(0.0, -42.0),
    )
    spawn_static_mesh(
        "AET_PROD_MKG_GrappleHook_A01",
        meshes["SM_MKG_GrappleHook_A01"],
        unreal.Vector(-380, 148, 42),
        rotation=review_rotator(0.0, -54.0),
    )
    spawn_static_mesh(
        "AET_PROD_MKG_SpikeDrill_A01",
        meshes["SM_MKG_SpikeDrill_A01"],
        unreal.Vector(-455, 205, 44),
        rotation=review_rotator(0.0, -24.0),
    )
    spawn_static_mesh(
        "AET_PROD_MKG_MonkeyWrench_A01",
        meshes["SM_MKG_MonkeyWrench_A01"],
        unreal.Vector(-505, 242, 38),
        rotation=review_rotator(0.0, -6.0),
    )
    spawn_static_mesh(
        "AET_PROD_MKG_RatchetCleaver_A01",
        meshes["SM_MKG_RatchetCleaver_A01"],
        unreal.Vector(-540, 282, 45),
        rotation=review_rotator(0.0, 16.0),
    )
    spawn_static_mesh(
        "AET_PROD_MKG_GearMace_A01",
        meshes["SM_MKG_GearMace_A01"],
        unreal.Vector(-620, 365, 45),
        rotation=review_rotator(0.0, -12.0),
    )
    gnome_actor = spawn_skeletal_mesh(
        "AET_PROD_GnomeBase_A01",
        skeletal_meshes["SK_GNM_Base_A01"],
        unreal.Vector(-735, 520, 0),
        rotation=review_rotator(0.0, 0.0),
    )
    spawn_static_mesh_on_skeletal_socket(
        "AET_PROD_MKG_ToolPack_BackFit_A01",
        meshes["SM_MKG_ToolPack_A01"],
        gnome_actor,
        "back_pack",
    )
    spawn_static_mesh(
        "AET_PROD_Palisade_Wall_A01",
        meshes["SM_AET_Palisade_Wall_A01"],
        unreal.Vector(-200, -660, 0),
    )
    spawn_static_mesh(
        "AET_PROD_Palisade_Post_A01",
        meshes["SM_AET_Palisade_Post_A01"],
        unreal.Vector(-430, -660, 0),
    )
    spawn_static_mesh(
        "AET_PROD_Palisade_EndCap_A01",
        meshes["SM_AET_Palisade_EndCap_A01"],
        unreal.Vector(70, -660, 0),
    )
    spawn_static_mesh(
        "AET_PROD_Palisade_Corner_A01",
        meshes["SM_AET_Palisade_Corner_A01"],
        unreal.Vector(360, -660, 0),
    )
    spawn_static_mesh(
        "AET_PROD_Palisade_Gate_A01",
        meshes["SM_AET_Palisade_Gate_A01"],
        unreal.Vector(140, -1020, 0),
    )

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save current level")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea", only_if_is_dirty=True, recursive=True)
    unreal.log("Updated startup level with next-slice production review assets.")


def selected_asset_names():
    raw = os.environ.get("AET_IMPORT_ASSETS", "")
    return {part.strip() for part in raw.split(",") if part.strip()}


def static_asset_path(entry):
    return "{}/{}".format(entry["destination"], entry["name"])


def main():
    selected = selected_asset_names()
    known = {entry["name"] for entry in STATIC_ASSETS} | {entry["name"] for entry in SKELETAL_ASSETS}
    unknown = selected - known
    if unknown:
        raise RuntimeError("Unknown AET_IMPORT_ASSETS entries: {}".format(", ".join(sorted(unknown))))

    process_skeletal_assets = not selected or any(entry["name"] in selected for entry in SKELETAL_ASSETS)
    materials = ensure_materials(include_skeletal=process_skeletal_assets)
    meshes = {}
    skeletal_meshes = {}
    for entry in STATIC_ASSETS:
        if not selected or entry["name"] in selected:
            mesh = import_static_mesh(entry)
            assign_project_materials(mesh, materials)
            ensure_review_lods_static(mesh)
            socket_specs = STATIC_MESH_SOCKET_SETS.get(entry["name"])
            if socket_specs:
                ensure_static_mesh_sockets(mesh, socket_specs)
        else:
            mesh = unreal.load_asset(static_asset_path(entry))
            if mesh is None:
                raise RuntimeError("Missing previously imported static mesh: {}".format(static_asset_path(entry)))
        meshes[entry["name"]] = mesh

    for entry in SKELETAL_ASSETS:
        if not selected or entry["name"] in selected:
            mesh = import_skeletal_mesh(entry)
            assign_project_materials(mesh, materials)
            ensure_physics_asset(mesh, entry["physics_asset"])
            ensure_review_lods_skeletal(mesh)
        else:
            mesh = unreal.load_asset("{}/{}".format(entry["destination"], entry["name"]))
            if mesh is None:
                raise RuntimeError("Missing previously imported skeletal mesh: {}/{}".format(entry["destination"], entry["name"]))
        skeletal_meshes[entry["name"]] = mesh

    if process_skeletal_assets:
        ensure_skeletal_infrastructure()
    update_startup_level(meshes, skeletal_meshes)
    unreal.log("Aerathea next-slice import complete.")


main()
