import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
REVIEW_CAMERA_LOCATION = unreal.Vector(4710.0, -2880.0, 2575.0)
REVIEW_CAMERA_TARGET = unreal.Vector(-70, 160, 110)
EXPECTED_ASSETS = [
    "/Game/Aerathea/Materials/M_AET_Stone_Handpainted_A01",
    "/Game/Aerathea/Materials/M_AET_Timber_Handpainted_A01",
    "/Game/Aerathea/Materials/M_AET_DarkIron_A01",
    "/Game/Aerathea/Materials/M_AET_Brass_A01",
    "/Game/Aerathea/Materials/M_AET_AetheriumGlow_Blue_A01",
    "/Game/Aerathea/Materials/M_AET_Straw_A01",
    "/Game/Aerathea/Materials/M_AET_Leather_Dark_A01",
    "/Game/Aerathea/Materials/M_AET_PackedEarth_A01",
    "/Game/Aerathea/Materials/M_AET_Moss_A01",
    "/Game/Aerathea/Materials/M_GNM_Skin_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Workwear_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_BootLeather_Blockout_A01",
    "/Game/Aerathea/Materials/M_GNM_Eye_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Gryphon_Feather_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Gryphon_Fur_Blockout_A01",
    "/Game/Aerathea/Materials/M_CRE_Gryphon_Keratin_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Skin_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Tattoo_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Leather_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Fur_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Hair_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Iron_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_Stone_Blockout_A01",
    "/Game/Aerathea/Materials/M_GIA_RuneGlow_Blockout_A01",
    "/Game/Aerathea/Materials/M_INF_CultStone_Blockout_A01",
    "/Game/Aerathea/Materials/M_INF_ScorchedStone_Blockout_A01",
    "/Game/Aerathea/Materials/M_INF_ObsidianIron_Blockout_A01",
    "/Game/Aerathea/Materials/M_INF_RitualGlow_Blockout_A01",
    "/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01",
    "/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01",
    "/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01",
    "/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_AetherKnife_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SparkPistol_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_MultiTool_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SpikeDrill_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_MonkeyWrench_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_RatchetCleaver_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_GearMace_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_ToolPack_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Wall_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Post_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Corner_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Gate_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_EndCap_A01",
    "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01",
    "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01_Skeleton",
    "/Game/Aerathea/Characters/Gnomes/Base/PHYS_GNM_Base_A01",
    "/Game/Aerathea/Characters/Gnomes/Base/ABP_GNM_Base_A01",
    "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01",
    "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01_Skeleton",
    "/Game/Aerathea/Creatures/Gryphon/Base/PHYS_CRE_Gryphon_A01",
    "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01_Anim",
    "/Game/Aerathea/Creatures/Gryphon/Base/ABP_CRE_Gryphon_A01",
    "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01",
    "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01_Skeleton",
    "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Male_A01",
    "/Game/Aerathea/Characters/Giants/Base/ABP_GIA_Base_Male_A01",
    "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01",
    "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01_Skeleton",
    "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Female_A01",
    "/Game/Aerathea/Characters/Giants/Base/ABP_GIA_Base_Female_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01",
    "/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01",
    "/Game/Aerathea/Blueprints/Props/BP_AET_TargetDummy_A01",
    LEVEL_PATH,
]
EXPECTED_ACTOR_LABELS = [
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_PROD_GroundTile_A01_R3_C3",
    "AET_PROD_TargetDummy_A01",
    "AET_PROD_Portal_A01",
    "AET_PROD_WorkshopCrate_A01",
    "AET_PROD_MKG_AetherKnife_A01",
    "AET_PROD_MKG_AetherCoreUnit_A01",
    "AET_PROD_MKG_SparkPistol_A01",
    "AET_PROD_MKG_AetheriumGrenade_A01",
    "AET_PROD_MKG_MultiTool_A01",
    "AET_PROD_MKG_SpikeDrill_A01",
    "AET_PROD_MKG_MonkeyWrench_A01",
    "AET_PROD_MKG_RatchetCleaver_A01",
    "AET_PROD_MKG_GearMace_A01",
    "AET_PROD_GnomeBase_A01",
    "AET_PROD_MKG_ToolPack_BackFit_A01",
    "AET_PROD_CRE_Gryphon_A01",
    "AET_PROD_GiantMaleBase_A01",
    "AET_PROD_GiantFemaleBase_A01",
    "AET_PROD_Palisade_Wall_A01",
    "AET_PROD_Palisade_Post_A01",
    "AET_PROD_Palisade_EndCap_A01",
    "AET_PROD_Palisade_Corner_A01",
    "AET_PROD_Palisade_Gate_A01",
    "AET_PROD_INF_CullingTrialFloor_A01",
    "AET_PROD_PlayerStart_Review_A01",
    "AET_PROD_Camera_Review_A01",
    "AET_PROD_ReviewCameraDirector_A01",
    "AET_PROD_ReviewFillLight_A01",
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
    "AET_BOOT_Camera_Overview",
    "AET_BOOT_Label_StyleTarget",
]
RETIRED_BLOCKOUT_LABELS = [
    "AET_BOOT_GroundTile_20m_A01",
    "AET_BOOT_PortalArch_LeftColumn_A01",
    "AET_BOOT_PortalArch_RightColumn_A01",
    "AET_BOOT_PortalArch_Capstone_A01",
    "AET_BOOT_PortalCore_Aetherium_A01",
    "AET_BOOT_TargetDummy_Blockout_A01",
    "AET_BOOT_TargetDummy_Crossbar_A01",
    "AET_PROD_PortalArch_A01",
    "AET_PROD_PortalCore_Aetherium_A01",
]
EXPECTED_STATIC_MESHES = [
    "/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01",
    "/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01",
    "/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01",
    "/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_AetherKnife_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SparkPistol_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_MultiTool_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SpikeDrill_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_MonkeyWrench_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_RatchetCleaver_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_GearMace_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_ToolPack_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Wall_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Post_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Corner_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Gate_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_EndCap_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01",
]
EXPECTED_SKELETAL_MESHES = [
    (
        "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01",
        "/Game/Aerathea/Characters/Gnomes/Base/PHYS_GNM_Base_A01",
    ),
    (
        "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01",
        "/Game/Aerathea/Creatures/Gryphon/Base/PHYS_CRE_Gryphon_A01",
    ),
    (
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01",
        "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Male_A01",
    ),
    (
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01",
        "/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Female_A01",
    ),
]
EXPECTED_LOD_STATIC_MESHES = [
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_MultiTool_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_SpikeDrill_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_MonkeyWrench_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_RatchetCleaver_A01",
    "/Game/Aerathea/Weapons/Mekgineer/SM_MKG_GearMace_A01",
    "/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_ToolPack_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Wall_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Post_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Corner_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_Gate_A01",
    "/Game/Aerathea/Buildings/Common/Palisade/SM_AET_Palisade_EndCap_A01",
    "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01",
]
EXPECTED_STATIC_MESH_SOCKETS = [
    (
        "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01",
        [
            "vfx_center",
            "vfx_ring_active",
            "vfx_rejected_gap",
            "snap_altar",
            "snap_arch_front",
            "stage_spawn",
            "stage_blooded",
            "stage_elder",
        ],
    ),
]
EXPECTED_SKELETAL_MESH_SOCKETS = [
    (
        "/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "back_pack",
            "head_goggles",
            "belt_tool_l",
            "belt_tool_r",
            "muzzle_preview",
            "vfx_aether_core",
        ],
    ),
    (
        "/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01",
        [
            "socket_head_vfx",
            "socket_beak",
            "socket_talon_l",
            "socket_talon_r",
            "socket_back_mount",
            "socket_saddle",
            "socket_wing_l_vfx",
            "socket_wing_r_vfx",
            "socket_tail",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "belt_tool_l",
            "belt_tool_r",
            "head_hair_ornament",
            "chest_talisman",
            "vfx_rune_hand_l",
            "vfx_rune_hand_r",
            "vfx_stomp_ground",
        ],
    ),
    (
        "/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01",
        [
            "hand_r_weapon",
            "hand_l_offhand",
            "hand_r_twohand_grip",
            "hand_l_twohand_grip",
            "back_large_weapon",
            "back_shield",
            "belt_tool_l",
            "belt_tool_r",
            "head_hair_ornament",
            "chest_talisman",
            "vfx_rune_hand_l",
            "vfx_rune_hand_r",
            "vfx_stomp_ground",
        ],
    ),
]
EXPECTED_RUNTIME_VISIBLE_LABELS = [
    "AET_PROD_GroundTile_A01_R3_C3",
    "AET_PROD_TargetDummy_A01",
    "AET_PROD_Portal_A01",
    "AET_PROD_WorkshopCrate_A01",
    "AET_PROD_MKG_AetherKnife_A01",
    "AET_PROD_MKG_AetherCoreUnit_A01",
    "AET_PROD_MKG_SparkPistol_A01",
    "AET_PROD_MKG_AetheriumGrenade_A01",
    "AET_PROD_MKG_MultiTool_A01",
    "AET_PROD_MKG_SpikeDrill_A01",
    "AET_PROD_MKG_MonkeyWrench_A01",
    "AET_PROD_MKG_RatchetCleaver_A01",
    "AET_PROD_MKG_GearMace_A01",
    "AET_PROD_GnomeBase_A01",
    "AET_PROD_MKG_ToolPack_BackFit_A01",
    "AET_PROD_CRE_Gryphon_A01",
    "AET_PROD_GiantMaleBase_A01",
    "AET_PROD_GiantFemaleBase_A01",
    "AET_PROD_Palisade_Wall_A01",
    "AET_PROD_Palisade_Post_A01",
    "AET_PROD_Palisade_EndCap_A01",
    "AET_PROD_Palisade_Corner_A01",
    "AET_PROD_Palisade_Gate_A01",
    "AET_PROD_INF_CullingTrialFloor_A01",
    "AET_PROD_Camera_Review_A01",
    "AET_PROD_ReviewFillLight_A01",
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
]
EXPECTED_RUNTIME_HIDDEN_LABELS = [
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_BOOT_Camera_Overview",
    "AET_BOOT_Label_StyleTarget",
]
EXPECTED_BOUNDS_LIMITS = {
    "AET_PROD_GroundTile_A01_R3_C3": {
        "extent_min": unreal.Vector(150.0, 150.0, 1.0),
        "extent_max": unreal.Vector(250.0, 250.0, 20.0),
        "radius_max": 360.0,
    },
    "AET_PROD_Portal_A01": {"radius_max": 600.0},
    "AET_PROD_TargetDummy_A01": {"radius_max": 350.0},
    "AET_PROD_WorkshopCrate_A01": {"radius_max": 250.0},
    "AET_PROD_GnomeBase_A01": {"radius_max": 250.0},
    "AET_PROD_CRE_Gryphon_A01": {"radius_max": 600.0},
    "AET_PROD_GiantMaleBase_A01": {
        "extent_min": unreal.Vector(45.0, 45.0, 180.0),
        "radius_max": 700.0,
    },
    "AET_PROD_GiantFemaleBase_A01": {
        "extent_min": unreal.Vector(40.0, 40.0, 155.0),
        "radius_max": 650.0,
    },
    "AET_PROD_Palisade_Gate_A01": {"radius_max": 800.0},
    "AET_PROD_INF_CullingTrialFloor_A01": {
        "extent_min": unreal.Vector(390.0, 390.0, 8.0),
        "radius_max": 720.0,
    },
}
REVIEW_CAMERA_ROTATION_TOLERANCE_DEGREES = 2.0
KEY_DIRECTIONAL_LIGHT_LABEL = "AET_BOOT_KeyLight_Directional"


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def try_call(obj, method_name):
    method = getattr(obj, method_name, None)
    if not callable(method):
        return None
    try:
        return method()
    except Exception:
        return None


def is_actor_hidden_in_game(actor):
    hidden = try_call(actor, "get_actor_hidden_in_game")
    if hidden is not None:
        return bool(hidden)
    try:
        return bool(actor.get_editor_property("hidden"))
    except Exception:
        return False


def component_hidden_or_invisible(component):
    component_name = component.get_name()
    component_class_name = component.get_class().get_name()
    editor_visual_classes = (
        "BillboardComponent",
        "DrawFrustumComponent",
        "CameraProxyMeshComponent",
        "ArrowComponent",
    )
    if component_class_name in editor_visual_classes or any(name in component_name for name in editor_visual_classes):
        return False
    hidden_runtime_helpers = {
        "HitVolume",
        "InteractionVolume",
    }
    hidden_runtime_helper_classes = {
        "BoxComponent",
        "CapsuleComponent",
        "SphereComponent",
    }
    if component_name in hidden_runtime_helpers and component_class_name in hidden_runtime_helper_classes:
        return False
    hidden = try_call(component, "is_hidden_in_game")
    visible = try_call(component, "is_visible")
    return bool(hidden) or visible is False


def vector_distance(a, b):
    return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z - b.z) ** 2))


def vector_radius(vector):
    return math.sqrt((vector.x * vector.x) + (vector.y * vector.y) + (vector.z * vector.z))


def angle_delta_degrees(a, b):
    return abs((a - b + 180.0) % 360.0 - 180.0)


def log_camera_aim(camera_actor):
    location = camera_actor.get_actor_location()
    rotation = camera_actor.get_actor_rotation()
    target = REVIEW_CAMERA_TARGET
    location_error = vector_distance(location, REVIEW_CAMERA_LOCATION)
    if location_error > 1.0:
        raise RuntimeError("Review camera location mismatch: {:.2f} cm".format(location_error))
    dx = target.x - location.x
    dy = target.y - location.y
    dz = target.z - location.z
    expected_yaw = math.degrees(math.atan2(dy, dx))
    expected_pitch = math.degrees(math.atan2(dz, math.sqrt((dx * dx) + (dy * dy))))
    unreal.log(
        "Aerathea review camera diagnostic: location={} rotation={} expected_pitch={:.2f} expected_yaw={:.2f}.".format(
            location,
            rotation,
            expected_pitch,
            expected_yaw,
        )
    )
    pitch_error = angle_delta_degrees(rotation.pitch, expected_pitch)
    yaw_error = angle_delta_degrees(rotation.yaw, expected_yaw)
    if pitch_error > REVIEW_CAMERA_ROTATION_TOLERANCE_DEGREES or yaw_error > REVIEW_CAMERA_ROTATION_TOLERANCE_DEGREES:
        raise RuntimeError(
            "Review camera aim mismatch: pitch error {:.2f} deg, yaw error {:.2f} deg".format(
                pitch_error,
                yaw_error,
            )
        )


def validate_actor_bounds(actors_by_label):
    failures = []
    for label, limits in EXPECTED_BOUNDS_LIMITS.items():
        actor = actors_by_label.get(label)
        if actor is None:
            continue
        _origin, extent = actor.get_actor_bounds(False)
        radius = vector_radius(extent)
        extent_min = limits.get("extent_min")
        if extent_min is not None and (
            extent.x < extent_min.x or extent.y < extent_min.y or extent.z < extent_min.z
        ):
            failures.append("{} bounds extent {} is below expected {}".format(label, extent, extent_min))
        extent_max = limits.get("extent_max")
        if extent_max is not None and (
            extent.x > extent_max.x or extent.y > extent_max.y or extent.z > extent_max.z
        ):
            failures.append("{} bounds extent {} exceeds expected {}".format(label, extent, extent_max))
        radius_max = limits.get("radius_max")
        if radius_max is not None and radius > radius_max:
            failures.append("{} bounds radius {:.2f} cm exceeds {:.2f} cm".format(label, radius, radius_max))
    if failures:
        raise RuntimeError("Startup actor bounds validation failed: {}".format("; ".join(failures)))


def get_forward_shading_priority(component):
    for prop in ("forward_shading_priority", "ForwardShadingPriority"):
        try:
            return int(component.get_editor_property(prop))
        except Exception:
            pass
    return None


def validate_directional_light_priority(actors):
    failures = []
    winning_labels = []
    for actor in actors:
        component = actor.get_component_by_class(unreal.DirectionalLightComponent)
        if component is None:
            continue
        priority = get_forward_shading_priority(component)
        if actor.get_actor_label() == KEY_DIRECTIONAL_LIGHT_LABEL:
            if priority != 1:
                failures.append("{} ForwardShadingPriority is {}, expected 1".format(KEY_DIRECTIONAL_LIGHT_LABEL, priority))
            winning_labels.append(actor.get_actor_label())
        elif priority not in (None, 0):
            failures.append("{} ForwardShadingPriority is {}, expected 0".format(actor.get_actor_label(), priority))
    if KEY_DIRECTIONAL_LIGHT_LABEL not in winning_labels:
        failures.append("Missing key directional light {}".format(KEY_DIRECTIONAL_LIGHT_LABEL))
    if failures:
        raise RuntimeError("Directional light priority validation failed: {}".format("; ".join(failures)))


def main():
    missing_assets = [
        asset_path
        for asset_path in EXPECTED_ASSETS
        if not unreal.EditorAssetLibrary.does_asset_exist(asset_path)
    ]
    if missing_assets:
        raise RuntimeError("Missing expected assets: {}".format(", ".join(missing_assets)))

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actors = all_level_actors()
    actors_by_label = {actor.get_actor_label(): actor for actor in actors}
    actor_labels = set(actors_by_label.keys())
    missing_labels = [
        label
        for label in EXPECTED_ACTOR_LABELS
        if label not in actor_labels
    ]
    if missing_labels:
        raise RuntimeError("Missing startup actors: {}".format(", ".join(missing_labels)))

    retired_labels = [
        label
        for label in RETIRED_BLOCKOUT_LABELS
        if label in actor_labels
    ]
    if retired_labels:
        raise RuntimeError("Retired blockout actors still present: {}".format(", ".join(retired_labels)))

    ground_tiles = [
        label
        for label in actor_labels
        if label.startswith("AET_PROD_GroundTile_A01_")
    ]
    if len(ground_tiles) != 25:
        raise RuntimeError("Expected 25 production ground tiles, found {}".format(len(ground_tiles)))
    validate_actor_bounds(actors_by_label)
    validate_directional_light_priority(actors)

    portal_actor = next(
        actor
        for actor in actors
        if actor.get_actor_label() == "AET_PROD_Portal_A01"
    )
    portal_class_name = portal_actor.get_class().get_name()
    if "BP_AET_Portal_A01" not in portal_class_name and "AETPortalActor" not in portal_class_name:
        raise RuntimeError("Portal actor has unexpected class: {}".format(portal_class_name))

    target_dummy_actor = actors_by_label["AET_PROD_TargetDummy_A01"]
    target_dummy_class_name = target_dummy_actor.get_class().get_name()
    if "BP_AET_TargetDummy_A01" not in target_dummy_class_name and "AETTargetDummyActor" not in target_dummy_class_name:
        raise RuntimeError("Target dummy actor has unexpected class: {}".format(target_dummy_class_name))

    mesh_slot_failures = []
    for mesh_path in EXPECTED_STATIC_MESHES:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            mesh_slot_failures.append("{} failed to load".format(mesh_path))
            continue
        if len(mesh.get_editor_property("static_materials")) == 0:
            mesh_slot_failures.append("{} has no material slots".format(mesh_path))
    if mesh_slot_failures:
        raise RuntimeError("Static mesh validation failed: {}".format("; ".join(mesh_slot_failures)))

    skeletal_slot_failures = []
    for mesh_path, physics_asset_path in EXPECTED_SKELETAL_MESHES:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            skeletal_slot_failures.append("{} failed to load".format(mesh_path))
            continue
        if len(mesh.get_editor_property("materials")) == 0:
            skeletal_slot_failures.append("{} has no material slots".format(mesh_path))
        physics_asset = mesh.get_editor_property("physics_asset")
        if physics_asset is None:
            skeletal_slot_failures.append("{} has no assigned physics asset".format(mesh_path))
        elif physics_asset.get_path_name().split(".", 1)[0] != physics_asset_path:
            skeletal_slot_failures.append(
                "{} has unexpected physics asset {}".format(mesh_path, physics_asset.get_path_name())
            )
    if skeletal_slot_failures:
        raise RuntimeError("Skeletal mesh validation failed: {}".format("; ".join(skeletal_slot_failures)))

    lod_failures = []
    for mesh_path in EXPECTED_LOD_STATIC_MESHES:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            lod_failures.append("{} failed to load".format(mesh_path))
            continue
        lod_count = unreal.EditorStaticMeshLibrary.get_lod_count(mesh)
        if lod_count < 4:
            lod_failures.append("{} has {} LODs, expected at least 4".format(mesh_path, lod_count))

    skeletal_subsystem = unreal.get_editor_subsystem(unreal.SkeletalMeshEditorSubsystem)
    for mesh_path, _physics_asset_path in EXPECTED_SKELETAL_MESHES:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            continue
        if skeletal_subsystem is None:
            lod_failures.append("SkeletalMeshEditorSubsystem unavailable for {}".format(mesh_path))
            continue
        lod_count = skeletal_subsystem.get_lod_count(mesh)
        if lod_count < 4:
            lod_failures.append("{} has {} LODs, expected at least 4".format(mesh_path, lod_count))
    if lod_failures:
        raise RuntimeError("LOD validation failed: {}".format("; ".join(lod_failures)))

    socket_failures = []
    for mesh_path, expected_socket_names in EXPECTED_STATIC_MESH_SOCKETS:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            socket_failures.append("{} failed to load".format(mesh_path))
            continue
        missing_sockets = [
            socket_name
            for socket_name in expected_socket_names
            if mesh.find_socket(unreal.Name(socket_name)) is None
        ]
        if missing_sockets:
            socket_failures.append("{} missing sockets {}".format(mesh_path, ", ".join(missing_sockets)))

    for mesh_path, expected_socket_names in EXPECTED_SKELETAL_MESH_SOCKETS:
        mesh = unreal.load_asset(mesh_path)
        if mesh is None:
            socket_failures.append("{} failed to load".format(mesh_path))
            continue
        socket_names = {
            str(mesh.get_socket_by_index(index).get_editor_property("socket_name"))
            for index in range(mesh.num_sockets())
        }
        missing_sockets = [
            socket_name
            for socket_name in expected_socket_names
            if socket_name not in socket_names
        ]
        if missing_sockets:
            socket_failures.append("{} missing sockets {}".format(mesh_path, ", ".join(missing_sockets)))
    if socket_failures:
        raise RuntimeError("Socket validation failed: {}".format("; ".join(socket_failures)))

    gnome_actor = actors_by_label["AET_PROD_GnomeBase_A01"]
    toolpack_actor = actors_by_label["AET_PROD_MKG_ToolPack_BackFit_A01"]
    gnome_component = gnome_actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if gnome_component is None:
        raise RuntimeError("AET_PROD_GnomeBase_A01 has no SkeletalMeshComponent")
    if not gnome_component.does_socket_exist(unreal.Name("back_pack")):
        raise RuntimeError("AET_PROD_GnomeBase_A01 component missing back_pack socket")
    if unreal.Name("AET_SOCKET_FIT_PREVIEW") not in toolpack_actor.get_editor_property("tags"):
        raise RuntimeError("ToolPack fit actor is missing AET_SOCKET_FIT_PREVIEW tag")
    socket_location = gnome_component.get_socket_location(unreal.Name("back_pack"))
    toolpack_location = toolpack_actor.get_actor_location()
    fit_distance = vector_distance(socket_location, toolpack_location)
    if fit_distance > 2.0:
        raise RuntimeError(
            "ToolPack fit actor is {:.2f} cm from gnome back_pack socket".format(fit_distance)
        )

    runtime_visibility_failures = []
    for label in EXPECTED_RUNTIME_VISIBLE_LABELS:
        actor = actors_by_label.get(label)
        if actor is None:
            continue
        if is_actor_hidden_in_game(actor):
            runtime_visibility_failures.append("{} is hidden in game".format(label))
        primitive_components = actor.get_components_by_class(unreal.PrimitiveComponent)
        for component in primitive_components:
            if component_hidden_or_invisible(component):
                runtime_visibility_failures.append(
                    "{} component {} is hidden or invisible".format(
                        label,
                        component.get_name(),
                    )
                )
    if runtime_visibility_failures:
        raise RuntimeError("Runtime visibility validation failed: {}".format("; ".join(runtime_visibility_failures)))

    hidden_guide_failures = []
    for label in EXPECTED_RUNTIME_HIDDEN_LABELS:
        actor = actors_by_label.get(label)
        if actor is None:
            continue
        if not is_actor_hidden_in_game(actor):
            hidden_guide_failures.append("{} is visible in game".format(label))
    if hidden_guide_failures:
        raise RuntimeError("Runtime hidden-guide validation failed: {}".format("; ".join(hidden_guide_failures)))

    review_camera = actors_by_label["AET_PROD_Camera_Review_A01"]
    if unreal.Name("AET_REVIEW_CAMERA") not in review_camera.get_editor_property("tags"):
        raise RuntimeError("Review camera is missing AET_REVIEW_CAMERA tag")
    log_camera_aim(review_camera)

    unreal.log(
        "Aerathea startup validation complete: {} assets, {} expected actors, {} ground tiles.".format(
            len(EXPECTED_ASSETS),
            len(EXPECTED_ACTOR_LABELS),
            len(ground_tiles),
        )
    )


main()
