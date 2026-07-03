import math
import os

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_ReviewIsland"
CAMERA_LABEL = "AET_REVIEW_Camera_Main_A01"
PLAYER_START_LABEL = "AET_REVIEW_PlayerStart_A01"
DIRECTOR_LABEL = "AET_REVIEW_ReviewCameraDirector_A01"


def parse_vector(name, fallback):
    raw = os.environ.get(name, "")
    if not raw:
        return unreal.Vector(*fallback)
    parts = [part.strip() for part in raw.split(",")]
    if len(parts) != 3:
        raise RuntimeError("{} must be formatted as x,y,z".format(name))
    return unreal.Vector(float(parts[0]), float(parts[1]), float(parts[2]))


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


def actor_by_label(label):
    world = unreal.EditorLevelLibrary.get_editor_world()
    for actor in unreal.GameplayStatics.get_all_actors_of_class(world, unreal.Actor):
        if actor.get_actor_label() == label:
            return actor
    return None


def set_actor_view(actor, location, rotation):
    if actor is None:
        return
    actor.modify()
    actor.set_actor_location(location, False, False)
    actor.set_actor_rotation(rotation, False)


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load review island: {}".format(LEVEL_PATH))

    location = parse_vector("AET_REVIEW_CAMERA_LOCATION", (0.0, -650.0, 255.0))
    target = parse_vector("AET_REVIEW_CAMERA_TARGET", (0.0, 0.0, 92.0))
    fov = float(os.environ.get("AET_REVIEW_CAMERA_FOV", "45.0"))
    rotation = look_at_rotation(location, target)

    camera = actor_by_label(CAMERA_LABEL)
    if camera is None:
        raise RuntimeError("Missing review camera actor {}".format(CAMERA_LABEL))

    set_actor_view(camera, location, rotation)
    component = camera.get_component_by_class(unreal.CameraComponent)
    if component is not None:
        component.modify()
        component.set_editor_property("field_of_view", fov)

    set_actor_view(actor_by_label(PLAYER_START_LABEL), location, rotation)
    set_actor_view(actor_by_label(DIRECTOR_LABEL), location, rotation)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save review island level")
    unreal.log(
        "Set review island camera to location {} target {} fov {:.1f}".format(
            location,
            target,
            fov,
        )
    )


main()
