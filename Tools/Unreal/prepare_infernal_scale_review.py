from pathlib import Path
import json
import math
import os
import sys

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
STATE_PATH = ROOT / "Saved/Automation/StartupReview/InfernalScaleCaptureState.json"

REVIEW_CAMERA_LABEL = "AET_PROD_Camera_Review_A01"
REVIEW_PLAYER_START_LABEL = "AET_PROD_PlayerStart_Review_A01"
REVIEW_CAMERA_TAG = "AET_REVIEW_CAMERA"

REVIEW_LOCATION = unreal.Vector(1300.0, -930.0, 700.0)
REVIEW_TARGET = unreal.Vector(-10.0, 130.0, 135.0)
REVIEW_FOV = 54.0

VISIBLE_EXACT_LABELS = {
    "AET_PROD_Camera_Review_A01",
    "AET_PROD_PlayerStart_Review_A01",
    "AET_PROD_ReviewCameraDirector_A01",
    "AET_PROD_ReviewFillLight_A01",
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
}


def command_line_mode():
    for arg in sys.argv:
        if arg.startswith("-AETInfernalReviewMode="):
            return arg.split("=", 1)[1].strip("\"'")

    try:
        command_line = unreal.SystemLibrary.get_command_line()
    except Exception:
        command_line = ""

    for token in command_line.split():
        if token.startswith("-AETInfernalReviewMode="):
            return token.split("=", 1)[1].strip("\"'")
    return os.environ.get("AET_INFERNAL_REVIEW_MODE", "prepare")


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


def safe_call(obj, method_name, *args):
    method = getattr(obj, method_name, None)
    if not callable(method):
        return None
    try:
        return method(*args)
    except Exception:
        return None


def safe_get(obj, prop_name, default=None):
    try:
        return obj.get_editor_property(prop_name)
    except Exception:
        return default


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


def actors_by_label():
    return {actor.get_actor_label(): actor for actor in all_level_actors()}


def vector_to_list(value):
    return [float(value.x), float(value.y), float(value.z)]


def rotator_to_list(value):
    return [float(value.roll), float(value.pitch), float(value.yaw)]


def vector_from_list(value):
    return unreal.Vector(float(value[0]), float(value[1]), float(value[2]))


def rotator_from_list(value):
    return unreal.Rotator(float(value[0]), float(value[1]), float(value[2]))


def is_shape_component(component):
    return component.get_class().get_name() in {
        "BoxComponent",
        "CapsuleComponent",
        "SphereComponent",
    }


def actor_hidden_in_game(actor):
    hidden = safe_call(actor, "get_actor_hidden_in_game")
    if hidden is not None:
        return bool(hidden)
    return bool(safe_get(actor, "hidden", False))


def actor_temp_hidden(actor):
    hidden = safe_call(actor, "is_temporarily_hidden_in_editor")
    if hidden is not None:
        return bool(hidden)
    hidden = safe_call(actor, "get_is_temporarily_hidden_in_editor")
    if hidden is not None:
        return bool(hidden)
    return False


def component_hidden_in_game(component):
    hidden = safe_call(component, "is_hidden_in_game")
    if hidden is not None:
        return bool(hidden)
    return False


def component_visible(component):
    visible = safe_call(component, "is_visible")
    if visible is not None:
        return bool(visible)
    return True


def component_collision(component):
    value = safe_call(component, "get_collision_enabled")
    if value is None:
        return None
    return str(value)


def parse_collision(value):
    if value is None:
        return None
    for candidate in (
        unreal.CollisionEnabled.NO_COLLISION,
        unreal.CollisionEnabled.QUERY_ONLY,
        unreal.CollisionEnabled.PHYSICS_ONLY,
        unreal.CollisionEnabled.QUERY_AND_PHYSICS,
    ):
        if str(candidate) == value:
            return candidate
    return None


def capture_component_state(component):
    return {
        "name": component.get_name(),
        "class": component.get_class().get_name(),
        "visible": component_visible(component),
        "hidden_in_game": component_hidden_in_game(component),
        "collision_enabled": component_collision(component),
    }


def capture_actor_state(actor):
    components = [
        capture_component_state(component)
        for component in actor.get_components_by_class(unreal.PrimitiveComponent)
    ]
    camera_component = actor.get_component_by_class(unreal.CameraComponent)
    light_component = (
        actor.get_component_by_class(unreal.DirectionalLightComponent)
        or actor.get_component_by_class(unreal.PointLightComponent)
        or actor.get_component_by_class(unreal.SkyLightComponent)
    )
    state = {
        "class": actor.get_class().get_name(),
        "location": vector_to_list(actor.get_actor_location()),
        "rotation": rotator_to_list(actor.get_actor_rotation()),
        "scale": vector_to_list(actor.get_actor_scale3d()),
        "hidden_in_game": actor_hidden_in_game(actor),
        "temporarily_hidden_in_editor": actor_temp_hidden(actor),
        "components": components,
    }
    if camera_component is not None:
        state["camera"] = {
            "field_of_view": float(safe_get(camera_component, "field_of_view", 90.0)),
            "auto_activate": bool(safe_get(camera_component, "auto_activate", False)),
        }
    if light_component is not None:
        state["light"] = {
            "intensity": safe_get(light_component, "intensity", None),
            "attenuation_radius": safe_get(light_component, "attenuation_radius", None),
            "forward_shading_priority": safe_get(light_component, "forward_shading_priority", None),
        }
    return state


def write_state(label_lookup):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    state = {
        "level": LEVEL_PATH,
        "actors": {
            label: capture_actor_state(actor)
            for label, actor in sorted(label_lookup.items())
        },
    }
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    unreal.log("Saved Infernal scale review state to {}.".format(STATE_PATH))


def restore_actor(actor, state):
    safe_call(actor, "set_actor_hidden_in_game", bool(state["hidden_in_game"]))
    safe_call(actor, "set_is_temporarily_hidden_in_editor", bool(state["temporarily_hidden_in_editor"]))
    try:
        actor.set_actor_location(vector_from_list(state["location"]), False, True)
    except Exception:
        actor.set_actor_location(vector_from_list(state["location"]), False, False)
    try:
        actor.set_actor_rotation(rotator_from_list(state["rotation"]), False)
    except Exception:
        pass
    actor.set_actor_scale3d(vector_from_list(state["scale"]))

    components_by_name = {
        component.get_name(): component
        for component in actor.get_components_by_class(unreal.PrimitiveComponent)
    }
    for component_state in state.get("components", []):
        component = components_by_name.get(component_state["name"])
        if component is None:
            continue
        safe_call(component, "set_visibility", bool(component_state["visible"]), True)
        safe_call(component, "set_hidden_in_game", bool(component_state["hidden_in_game"]), True)
        collision = parse_collision(component_state.get("collision_enabled"))
        if collision is not None:
            safe_call(component, "set_collision_enabled", collision)

    camera_state = state.get("camera")
    camera_component = actor.get_component_by_class(unreal.CameraComponent)
    if camera_state is not None and camera_component is not None:
        safe_set(camera_component, "field_of_view", camera_state["field_of_view"])
        safe_set(camera_component, "auto_activate", camera_state["auto_activate"])

    light_state = state.get("light")
    light_component = (
        actor.get_component_by_class(unreal.DirectionalLightComponent)
        or actor.get_component_by_class(unreal.PointLightComponent)
        or actor.get_component_by_class(unreal.SkyLightComponent)
    )
    if light_state is not None and light_component is not None:
        if light_state.get("intensity") is not None:
            safe_set(light_component, "intensity", light_state["intensity"])
        if light_state.get("attenuation_radius") is not None:
            safe_set(light_component, "attenuation_radius", light_state["attenuation_radius"])
        if light_state.get("forward_shading_priority") is not None:
            safe_set(
                light_component,
                ("forward_shading_priority", "ForwardShadingPriority"),
                light_state["forward_shading_priority"],
            )


def restore_state(label_lookup):
    if not STATE_PATH.exists():
        raise RuntimeError("Missing Infernal scale review state: {}".format(STATE_PATH))
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    for label, actor_state in state.get("actors", {}).items():
        actor = label_lookup.get(label)
        if actor is None:
            unreal.log_warning("Cannot restore missing actor {}.".format(label))
            continue
        restore_actor(actor, actor_state)
    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save restored Infernal scale review state.")
    unreal.log("Restored Infernal scale review state from {}.".format(STATE_PATH))


def set_actor_runtime_visibility(actor, visible):
    safe_call(actor, "set_actor_hidden_in_game", not visible)
    safe_call(actor, "set_is_temporarily_hidden_in_editor", not visible)
    for component in actor.get_components_by_class(unreal.PrimitiveComponent):
        if visible and is_shape_component(component):
            safe_call(component, "set_visibility", False, True)
            safe_call(component, "set_hidden_in_game", True, True)
            continue
        safe_call(component, "set_visibility", visible, True)
        safe_call(component, "set_hidden_in_game", not visible, True)


def should_show_actor(label):
    if label in VISIBLE_EXACT_LABELS:
        return True
    if label.startswith("AET_PROD_GroundTile_"):
        return True
    if label.startswith("AET_PROD_Infernal"):
        return True
    return False


def set_actor_transform(actor, location, rotation):
    try:
        actor.set_actor_location(location, False, True)
    except Exception:
        actor.set_actor_location(location, False, False)
    try:
        actor.set_actor_rotation(rotation, False)
    except Exception:
        pass


def configure_review_camera(label_lookup, review_rotation):
    review_camera = label_lookup.get(REVIEW_CAMERA_LABEL)
    if review_camera is None:
        raise RuntimeError("Missing review camera actor {}".format(REVIEW_CAMERA_LABEL))

    set_actor_transform(review_camera, REVIEW_LOCATION, review_rotation)
    review_camera.set_editor_property("tags", [unreal.Name(REVIEW_CAMERA_TAG)])
    safe_set(review_camera, "auto_activate_for_player", unreal.AutoReceiveInput.PLAYER0)

    camera_component = review_camera.get_component_by_class(unreal.CameraComponent)
    if camera_component is not None:
        safe_set(camera_component, "field_of_view", REVIEW_FOV)
        safe_set(camera_component, "auto_activate", True)

    player_start = label_lookup.get(REVIEW_PLAYER_START_LABEL)
    if player_start is not None:
        set_actor_transform(player_start, REVIEW_LOCATION, review_rotation)


def configure_lighting(label_lookup):
    key_light = label_lookup.get("AET_BOOT_KeyLight_Directional")
    if key_light is not None:
        set_actor_transform(key_light, unreal.Vector(-500.0, -620.0, 850.0), review_rotator(-36.0, 38.0))
        component = key_light.get_component_by_class(unreal.DirectionalLightComponent)
        if component is not None:
            safe_set(component, "intensity", 0.32)
            safe_set(component, ("forward_shading_priority", "ForwardShadingPriority"), 1)

    fill_light = label_lookup.get("AET_PROD_ReviewFillLight_A01")
    if fill_light is not None:
        set_actor_transform(fill_light, unreal.Vector(-760.0, -520.0, 520.0), fill_light.get_actor_rotation())
        component = fill_light.get_component_by_class(unreal.PointLightComponent)
        if component is not None:
            safe_set(component, "intensity", 1000.0)
            safe_set(component, "attenuation_radius", 2200.0)

    sky_light = label_lookup.get("AET_BOOT_SkyLight")
    if sky_light is not None:
        component = sky_light.get_component_by_class(unreal.SkyLightComponent)
        if component is not None:
            safe_set(component, "intensity", 0.35)


def prepare_state(label_lookup):
    write_state(label_lookup)
    review_rotation = look_at_rotation(REVIEW_LOCATION, REVIEW_TARGET)
    for label, actor in label_lookup.items():
        set_actor_runtime_visibility(actor, should_show_actor(label))
    configure_review_camera(label_lookup, review_rotation)
    configure_lighting(label_lookup)
    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save prepared Infernal scale review state.")
    unreal.log(
        "Prepared Infernal scale review state at {} / {}.".format(
            REVIEW_LOCATION,
            review_rotation,
        )
    )


def main():
    mode = command_line_mode()
    if mode not in {"prepare", "restore"}:
        raise RuntimeError("Unknown Infernal review mode '{}'; expected prepare or restore.".format(mode))
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))
    label_lookup = actors_by_label()
    if mode == "prepare":
        prepare_state(label_lookup)
    else:
        restore_state(label_lookup)


main()
