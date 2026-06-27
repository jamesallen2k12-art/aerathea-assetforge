from pathlib import Path
import math

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
OUTPUT_DIR = ROOT / "Saved/Automation/StartupReview"
OUTPUT_FILE = "AeratheaStartupReview_InfernalScale_A01.png"
WIDTH = 1280
HEIGHT = 720
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


def actors_by_label():
    return {actor.get_actor_label(): actor for actor in all_level_actors()}


def is_shape_component(component):
    return component.get_class().get_name() in {
        "BoxComponent",
        "CapsuleComponent",
        "SphereComponent",
    }


def set_actor_runtime_visibility(actor, visible):
    try:
        actor.set_actor_hidden_in_game(not visible)
    except Exception:
        pass
    try:
        actor.set_is_temporarily_hidden_in_editor(not visible)
    except Exception:
        pass
    try:
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            if visible and is_shape_component(component):
                component.set_visibility(False, True)
                component.set_hidden_in_game(True, True)
                continue
            component.set_visibility(visible, True)
            component.set_hidden_in_game(not visible, True)
    except Exception:
        pass


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
    review_camera = label_lookup.get("AET_PROD_Camera_Review_A01")
    if review_camera is None:
        raise RuntimeError("Missing review camera actor AET_PROD_Camera_Review_A01")

    set_actor_transform(review_camera, REVIEW_LOCATION, review_rotation)
    review_camera.set_editor_property("tags", [unreal.Name("AET_REVIEW_CAMERA")])
    safe_set(review_camera, "auto_activate_for_player", unreal.AutoReceiveInput.PLAYER0)

    camera_component = review_camera.get_component_by_class(unreal.CameraComponent)
    if camera_component is not None:
        safe_set(camera_component, "field_of_view", REVIEW_FOV)
        safe_set(camera_component, "auto_activate", True)
    return review_camera


def configure_review_director(label_lookup, output_path):
    review_director = label_lookup.get("AET_PROD_ReviewCameraDirector_A01")
    if review_director is None:
        raise RuntimeError("Missing review director actor AET_PROD_ReviewCameraDirector_A01")

    safe_set(review_director, ("capture_review_screenshot", "b_capture_review_screenshot", "bCaptureReviewScreenshot"), True)
    safe_set(review_director, "screenshot_width", WIDTH)
    safe_set(review_director, "screenshot_height", HEIGHT)
    safe_set(review_director, ("screenshot_filename_override", "ScreenshotFilenameOverride"), str(output_path))
    safe_set(review_director, "screenshot_delay_seconds", 0.5)
    safe_set(review_director, "screenshot_warmup_frames", 12)
    return review_director


def configure_lighting(label_lookup):
    key_light = label_lookup.get("AET_BOOT_KeyLight_Directional")
    if key_light is not None:
        set_actor_transform(key_light, unreal.Vector(-500.0, -620.0, 850.0), review_rotator(-36.0, 38.0))
        component = key_light.get_component_by_class(unreal.DirectionalLightComponent)
        if component is not None:
            safe_set(component, "intensity", 0.32)
            safe_set(component, "light_color", unreal.Color(255, 232, 206, 255))
            safe_set(component, ("forward_shading_priority", "ForwardShadingPriority"), 1)

    fill_light = label_lookup.get("AET_PROD_ReviewFillLight_A01")
    if fill_light is not None:
        set_actor_transform(fill_light, unreal.Vector(-760.0, -520.0, 520.0), fill_light.get_actor_rotation())
        component = fill_light.get_component_by_class(unreal.PointLightComponent)
        if component is not None:
            safe_set(component, "intensity", 1000.0)
            safe_set(component, "attenuation_radius", 2200.0)
            safe_set(component, "light_color", unreal.Color(195, 215, 255, 255))

    sky_light = label_lookup.get("AET_BOOT_SkyLight")
    if sky_light is not None:
        component = sky_light.get_component_by_class(unreal.SkyLightComponent)
        if component is not None:
            safe_set(component, "intensity", 0.35)


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / OUTPUT_FILE
    if output_path.exists():
        output_path.unlink()

    review_rotation = look_at_rotation(REVIEW_LOCATION, REVIEW_TARGET)
    label_lookup = actors_by_label()

    for label, actor in label_lookup.items():
        set_actor_runtime_visibility(actor, should_show_actor(label))

    configure_review_camera(label_lookup, review_rotation)
    configure_review_director(label_lookup, output_path)
    configure_lighting(label_lookup)

    unreal.log(
        "Prepared Infernal runtime scale capture at {} / {} -> {}.".format(
            REVIEW_LOCATION,
            review_rotation,
            output_path,
        )
    )

    level_editor_subsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    level_editor_subsystem.editor_request_begin_play()
    unreal.log("Requested Play In Editor for Infernal runtime scale capture.")


main()
