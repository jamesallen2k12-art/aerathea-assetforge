import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
MAGE_ACTOR_LABEL = "AET_PROD_INF_Mage_A01"
MAGE_MESH_PATH = "/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01"
MAGE_PHYSICS_PATH = "/Game/Aerathea/Characters/Infernals/Mage/PHYS_INF_Mage_A01"
MAGE_SKELETON_PATH = "/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton"
MAGE_ABP_PATH = "/Game/Aerathea/Characters/Infernals/Mage/ABP_INF_Mage_A01"
EXPECTED_VISIBLE_HEIGHT_CM = 203.0
HEIGHT_TOLERANCE_CM = 35.0
ACTOR_SCALE_TOLERANCE = 0.01


REQUIRED_MATERIALS = [
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_Skin_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_HornClaw_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_Wing_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_RitualCloth_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_ObsidianArmor_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_BoneOrnaments_Blockout_A01",
    "/Game/Aerathea/Materials/Infernals/Mage/M_INF_Mage_AbyssalGlow_Blockout_A01",
]


REQUIRED_SOCKETS = [
    "hand_l_claw",
    "hand_r_claw",
    "hand_l_cast",
    "hand_r_cast",
    "vfx_hand_l",
    "vfx_hand_r",
    "vfx_eye_l",
    "vfx_eye_r",
    "vfx_brand_chest",
    "vfx_brand_forearm_l",
    "vfx_brand_forearm_r",
    "vfx_wing_root_l",
    "vfx_wing_root_r",
    "wing_l_tip",
    "wing_r_tip",
    "tail_tip",
    "vfx_tail_tip",
    "vfx_regen_core",
    "vfx_sorcerer_focus",
    "vfx_worthiness_mark",
    "vfx_mouth",
]


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


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    if actor_subsystem is not None:
        return list(actor_subsystem.get_all_level_actors())
    return list(unreal.EditorLevelLibrary.get_all_level_actors())


def actors_by_label():
    return {actor.get_actor_label(): actor for actor in all_level_actors()}


def vector_radius(vector):
    return math.sqrt((vector.x * vector.x) + (vector.y * vector.y) + (vector.z * vector.z))


def approx(value, target, tolerance):
    return abs(value - target) <= tolerance


def validate_assets(failures):
    for asset_path in REQUIRED_MATERIALS:
        if unreal.load_asset(asset_path) is None:
            failures.append("{} failed to load".format(asset_path))

    mesh = unreal.load_asset(MAGE_MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(MAGE_MESH_PATH))
        return None

    material_count = len(mesh.get_editor_property("materials"))
    if material_count < 6:
        failures.append("{} has {} material slots, expected at least 6 for first-pass review".format(MAGE_MESH_PATH, material_count))

    skeleton = skeletal_mesh_skeleton(mesh)
    if skeleton is None:
        failures.append("{} has no assigned skeleton".format(MAGE_MESH_PATH))
    elif asset_path_without_object(skeleton) != MAGE_SKELETON_PATH:
        failures.append("{} has unexpected skeleton {}".format(MAGE_MESH_PATH, skeleton.get_path_name()))

    physics_asset = mesh.get_editor_property("physics_asset")
    if physics_asset is None:
        failures.append("{} has no assigned physics asset".format(MAGE_MESH_PATH))
    elif asset_path_without_object(physics_asset) != MAGE_PHYSICS_PATH:
        failures.append("{} has unexpected physics asset {}".format(MAGE_MESH_PATH, physics_asset.get_path_name()))

    skeletal_subsystem = unreal.get_editor_subsystem(unreal.SkeletalMeshEditorSubsystem)
    if skeletal_subsystem is None:
        failures.append("SkeletalMeshEditorSubsystem unavailable for {}".format(MAGE_MESH_PATH))
    elif skeletal_subsystem.get_lod_count(mesh) < 4:
        failures.append("{} has fewer than 4 LODs".format(MAGE_MESH_PATH))

    missing_sockets = [
        socket_name
        for socket_name in REQUIRED_SOCKETS
        if mesh.find_socket(unreal.Name(socket_name)) is None
    ]
    if missing_sockets:
        failures.append("{} missing sockets {}".format(MAGE_MESH_PATH, ", ".join(missing_sockets)))

    if unreal.load_asset(MAGE_PHYSICS_PATH) is None:
        failures.append("{} failed to load".format(MAGE_PHYSICS_PATH))
    if unreal.load_asset(MAGE_ABP_PATH) is None:
        failures.append("{} failed to load".format(MAGE_ABP_PATH))
    return mesh


def validate_actor(mesh, failures, measurements):
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actor = actors_by_label().get(MAGE_ACTOR_LABEL)
    if actor is None:
        failures.append("{} missing from {}".format(MAGE_ACTOR_LABEL, LEVEL_PATH))
        return

    if actor.get_class().get_name() != "SkeletalMeshActor":
        failures.append("{} has unexpected class {}".format(MAGE_ACTOR_LABEL, actor.get_class().get_name()))

    scale = actor.get_actor_scale3d()
    if not (
        approx(scale.x, 1.0, ACTOR_SCALE_TOLERANCE)
        and approx(scale.y, 1.0, ACTOR_SCALE_TOLERANCE)
        and approx(scale.z, 1.0, ACTOR_SCALE_TOLERANCE)
    ):
        failures.append("{} actor scale is {}, expected 1,1,1".format(MAGE_ACTOR_LABEL, scale))

    component = actor.get_component_by_class(unreal.SkeletalMeshComponent)
    if component is None:
        failures.append("{} has no SkeletalMeshComponent".format(MAGE_ACTOR_LABEL))
        return

    assigned_mesh = component.get_editor_property("skeletal_mesh")
    if assigned_mesh is None:
        failures.append("{} has no assigned skeletal mesh".format(MAGE_ACTOR_LABEL))
    elif asset_path_without_object(assigned_mesh) != MAGE_MESH_PATH:
        failures.append("{} uses {}, expected {}".format(MAGE_ACTOR_LABEL, assigned_mesh.get_path_name(), MAGE_MESH_PATH))
    elif mesh is not None and asset_path_without_object(assigned_mesh) != asset_path_without_object(mesh):
        failures.append("{} component mesh and loaded mesh disagree".format(MAGE_ACTOR_LABEL))

    _origin, extent = actor.get_actor_bounds(False)
    visible_height = extent.z * 2.0
    radius = vector_radius(extent)
    measurements.append((visible_height, radius))
    if visible_height < EXPECTED_VISIBLE_HEIGHT_CM - HEIGHT_TOLERANCE_CM:
        failures.append("{} visible height {:.2f} cm is too small".format(MAGE_ACTOR_LABEL, visible_height))
    if visible_height > 260.0:
        failures.append("{} visible height {:.2f} cm exceeds Standard/Greater first-pass envelope".format(MAGE_ACTOR_LABEL, visible_height))
    if radius > 560.0:
        failures.append("{} bounds radius {:.2f} cm exceeds 560 cm".format(MAGE_ACTOR_LABEL, radius))


def main():
    failures = []
    measurements = []
    mesh = validate_assets(failures)
    validate_actor(mesh, failures, measurements)
    if failures:
        raise RuntimeError("Infernal Mage validation failed: {}".format("; ".join(failures)))

    visible_height, radius = measurements[0]
    print(
        "Infernal Mage validation passed: visible height {:.2f} cm, bounds radius {:.2f} cm, {} sockets.".format(
            visible_height,
            radius,
            len(REQUIRED_SOCKETS),
        )
    )


if __name__ == "__main__":
    main()
