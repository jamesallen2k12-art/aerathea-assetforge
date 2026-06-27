import math
import os
import sys

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
REVIEW_CAMERA_LABEL = "AET_PROD_Camera_Review_A01"
REVIEW_PLAYER_START_LABEL = "AET_PROD_PlayerStart_Review_A01"
REVIEW_CAMERA_TAG = "AET_REVIEW_CAMERA"

PRESETS = {
    "overview": {
        "location": unreal.Vector(4710.0, -2880.0, 2575.0),
        "target": unreal.Vector(-70.0, 160.0, 110.0),
        "fov": 65.0,
        "lighting": {
            "directional_intensity": 5.0,
            "fill_intensity": 6000.0,
            "sky_intensity": 1.5,
        },
    },
    "portal_target": {
        "location": unreal.Vector(1500.0, -1020.0, 620.0),
        "target": unreal.Vector(130.0, 170.0, 130.0),
        "fov": 48.0,
    },
    "palisade": {
        "location": unreal.Vector(1280.0, -1560.0, 620.0),
        "target": unreal.Vector(60.0, -760.0, 135.0),
        "fov": 48.0,
    },
    "gnome_toolpack": {
        "location": unreal.Vector(-1450.0, 520.0, 300.0),
        "target": unreal.Vector(-735.0, 520.0, 82.0),
        "fov": 44.0,
    },
    "mkg_multitool": {
        "location": unreal.Vector(-820.0, -355.0, 220.0),
        "target": unreal.Vector(-310.0, 95.0, 52.0),
        "fov": 32.0,
        "lighting": {
            "directional_intensity": 0.65,
            "fill_location": unreal.Vector(-600.0, -130.0, 220.0),
            "fill_intensity": 900.0,
            "fill_radius": 850.0,
            "sky_intensity": 0.35,
        },
    },
    "gryphon": {
        "location": unreal.Vector(1450.0, 610.0, 285.0),
        "target": unreal.Vector(610.0, 605.0, 112.0),
        "fov": 40.0,
        "lighting": {
            "directional_intensity": 0.9,
            "fill_location": unreal.Vector(1260.0, 610.0, 430.0),
            "fill_intensity": 3000.0,
            "fill_radius": 1800.0,
            "sky_intensity": 0.75,
        },
    },
    "giant_base": {
        "location": unreal.Vector(2300.0, 715.0, 700.0),
        "target": unreal.Vector(700.0, 700.0, 225.0),
        "fov": 50.0,
        "lighting": {
            "directional_intensity": 0.18,
            "fill_location": unreal.Vector(1420.0, 760.0, 520.0),
            "fill_intensity": 420.0,
            "fill_radius": 2200.0,
            "sky_intensity": 0.3,
        },
    },
    "infernal_scale": {
        "location": unreal.Vector(1300.0, -930.0, 700.0),
        "target": unreal.Vector(-10.0, 130.0, 135.0),
        "fov": 54.0,
        "lighting": {
            "directional_intensity": 0.28,
            "fill_location": unreal.Vector(760.0, -520.0, 520.0),
            "fill_intensity": 850.0,
            "fill_radius": 1900.0,
            "sky_intensity": 0.32,
        },
    },
}


def command_line_preset():
    for arg in sys.argv:
        if arg.startswith("-AETReviewCameraPreset="):
            return arg.split("=", 1)[1].strip("\"'")

    try:
        command_line = unreal.SystemLibrary.get_command_line()
    except Exception:
        command_line = ""

    for token in command_line.split():
        if token.startswith("-AETReviewCameraPreset="):
            return token.split("=", 1)[1].strip("\"'")
    return None


def review_rotator(pitch, yaw, roll=0.0):
    return unreal.Rotator(roll, pitch, yaw)


def look_at_rotation(source, target):
    dx = target.x - source.x
    dy = target.y - source.y
    dz = target.z - source.z
    yaw = math.degrees(math.atan2(dy, dx))
    horizontal = math.sqrt((dx * dx) + (dy * dy))
    pitch = math.degrees(math.atan2(dz, horizontal))
    return review_rotator(pitch, yaw)


def safe_set(obj, props, value):
    if isinstance(props, str):
        props = (props,)
    for prop in props:
        try:
            obj.set_editor_property(prop, value)
            return prop
        except Exception:
            pass
    unreal.log_warning("Could not set {}.{}.".format(type(obj).__name__, "/".join(props)))
    return None


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def set_actor_transform(actor, location, rotation):
    try:
        actor.set_actor_location(location, False, True)
    except Exception:
        actor.set_actor_location(location, False, False)
    try:
        actor.set_actor_rotation(rotation, False)
    except Exception:
        pass


def configure_camera(preset_name):
    preset = PRESETS[preset_name]
    location = preset["location"]
    target = preset["target"]
    rotation = look_at_rotation(location, target)

    camera = find_actor_by_label(REVIEW_CAMERA_LABEL)
    if camera is None:
        raise RuntimeError("Missing review camera actor {}".format(REVIEW_CAMERA_LABEL))
    set_actor_transform(camera, location, rotation)
    camera.set_editor_property("tags", [unreal.Name(REVIEW_CAMERA_TAG)])
    safe_set(camera, "auto_activate_for_player", unreal.AutoReceiveInput.PLAYER0)

    component = camera.get_component_by_class(unreal.CameraComponent)
    if component is not None:
        safe_set(component, "field_of_view", preset["fov"])
        safe_set(component, "auto_activate", True)

    player_start = find_actor_by_label(REVIEW_PLAYER_START_LABEL)
    if player_start is not None:
        set_actor_transform(player_start, location, rotation)

    unreal.log(
        "Set Aerathea startup review camera preset {} at {} target {} fov {} rotation {}.".format(
            preset_name,
            location,
            target,
            preset["fov"],
            rotation,
        )
    )


def set_directional_priority(active_light):
    for actor in all_level_actors():
        component = actor.get_component_by_class(unreal.DirectionalLightComponent)
        if component is None:
            continue
        priority = 1 if actor == active_light else 0
        safe_set(component, ("forward_shading_priority", "ForwardShadingPriority"), priority)


def configure_lighting(preset_name):
    lighting = PRESETS[preset_name].get("lighting")
    if lighting is None:
        return

    key_light = find_actor_by_label("AET_BOOT_KeyLight_Directional")
    if key_light is not None:
        component = key_light.get_component_by_class(unreal.DirectionalLightComponent)
        if component is not None:
            safe_set(component, "intensity", lighting["directional_intensity"])
            set_directional_priority(key_light)

    fill_light = find_actor_by_label("AET_PROD_ReviewFillLight_A01")
    if fill_light is not None:
        fill_location = lighting.get("fill_location")
        if fill_location is not None:
            set_actor_transform(fill_light, fill_location, fill_light.get_actor_rotation())
        component = fill_light.get_component_by_class(unreal.PointLightComponent)
        if component is not None:
            safe_set(component, "intensity", lighting["fill_intensity"])
            if "fill_radius" in lighting:
                safe_set(component, "attenuation_radius", lighting["fill_radius"])

    sky_light = find_actor_by_label("AET_BOOT_SkyLight")
    if sky_light is not None:
        component = sky_light.get_component_by_class(unreal.SkyLightComponent)
        if component is not None:
            safe_set(component, "intensity", lighting["sky_intensity"])

    unreal.log("Applied Aerathea startup review lighting for preset {}.".format(preset_name))


def main():
    preset_name = command_line_preset() or os.environ.get("AET_REVIEW_CAMERA_PRESET", "overview")
    if preset_name not in PRESETS:
        raise RuntimeError(
            "Unknown review camera preset '{}'. Expected one of: {}".format(
                preset_name,
                ", ".join(sorted(PRESETS)),
            )
        )

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    configure_camera(preset_name)
    configure_lighting(preset_name)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save camera preset {}".format(preset_name))


main()
