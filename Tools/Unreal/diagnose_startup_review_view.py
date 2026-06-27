import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
REVIEW_CAMERA_LABEL = "AET_PROD_Camera_Review_A01"
REVIEW_TARGET = unreal.Vector(-70.0, 160.0, 110.0)

REPORT_LABELS = [
    "AET_PROD_Camera_Review_A01",
    "AET_BOOT_Camera_Overview",
    "AET_PROD_GroundTile_A01_R3_C3",
    "AET_PROD_Portal_A01",
    "AET_PROD_TargetDummy_A01",
    "AET_PROD_WorkshopCrate_A01",
    "AET_PROD_MKG_MultiTool_A01",
    "AET_PROD_MKG_SpikeDrill_A01",
    "AET_PROD_MKG_MonkeyWrench_A01",
    "AET_PROD_MKG_RatchetCleaver_A01",
    "AET_PROD_MKG_GearMace_A01",
    "AET_PROD_GnomeBase_A01",
    "AET_PROD_MKG_ToolPack_BackFit_A01",
    "AET_PROD_GNM_HeavyMekShieldwall_A01",
    "AET_PROD_OgreTeknomancer_A01",
    "AET_PROD_OgreWarrior_Rival_A01",
    "AET_PROD_OGR_CairnBattleGate_A01",
    "AET_PROD_GNM_HeavyMek_Rivalry_A01",
    "AET_PROD_CRE_Gryphon_A01",
    "AET_PROD_Palisade_Wall_A01",
    "AET_PROD_Palisade_Gate_A01",
]


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def vsub(a, b):
    return unreal.Vector(a.x - b.x, a.y - b.y, a.z - b.z)


def vdot(a, b):
    return (a.x * b.x) + (a.y * b.y) + (a.z * b.z)


def vlen(a):
    return math.sqrt(vdot(a, a))


def vscale(a, scale):
    return unreal.Vector(a.x * scale, a.y * scale, a.z * scale)


def vnorm(a):
    length = vlen(a)
    if length <= 0.0001:
        return unreal.Vector(1.0, 0.0, 0.0)
    return vscale(a, 1.0 / length)


def extent_radius(extent):
    return math.sqrt((extent.x * extent.x) + (extent.y * extent.y) + (extent.z * extent.z))


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actors_by_label = {actor.get_actor_label(): actor for actor in all_level_actors()}
    camera = actors_by_label.get(REVIEW_CAMERA_LABEL)
    if camera is None:
        raise RuntimeError("Missing {}".format(REVIEW_CAMERA_LABEL))

    camera_location = camera.get_actor_location()
    camera_rotation = camera.get_actor_rotation()
    forward = vnorm(vsub(REVIEW_TARGET, camera_location))
    unreal.log(
        "Aerathea view diagnostic camera: location={} rotation={} target={} forward={}.".format(
            camera_location,
            camera_rotation,
            REVIEW_TARGET,
            forward,
        )
    )

    for label in REPORT_LABELS:
        actor = actors_by_label.get(label)
        if actor is None:
            unreal.log_warning("Aerathea view diagnostic missing actor: {}".format(label))
            continue
        origin, extent = actor.get_actor_bounds(False)
        to_origin = vsub(origin, camera_location)
        forward_distance = vdot(to_origin, forward)
        closest = vsub(to_origin, vscale(forward, forward_distance))
        perpendicular_distance = vlen(closest)
        radius = extent_radius(extent)
        unreal.log(
            "Aerathea view diagnostic actor={} class={} location={} bounds_origin={} bounds_extent={} radius={:.1f} camera_forward_distance={:.1f} camera_perp_distance={:.1f} rough_line_overlap={}.".format(
                label,
                actor.get_class().get_name(),
                actor.get_actor_location(),
                origin,
                extent,
                radius,
                forward_distance,
                perpendicular_distance,
                forward_distance > 0.0 and perpendicular_distance < radius,
            )
        )


main()
