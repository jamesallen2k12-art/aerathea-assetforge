from pathlib import Path
import math

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
OUTPUT_DIR = ROOT / "Saved/Automation/StartupReview"
OUTPUT_FILE = "AeratheaStartupReview.png"
WIDTH = 1280
HEIGHT = 720
REVIEW_LOCATION = unreal.Vector(-2350.0, 1600.0, 1280.0)
REVIEW_TARGET = unreal.Vector(-70.0, 160.0, 110.0)
REVIEW_FOV = 70.0

EDITOR_GUIDE_LABELS = {
    "AET_PROD_PlayerStart_Review_A01",
    "AET_PROD_Camera_Review_A01",
    "AET_PROD_ReviewCameraDirector_A01",
    "AET_BOOT_Camera_Overview",
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


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def try_set_editor_property(obj, name, value):
    try:
        obj.set_editor_property(name, value)
        return True
    except Exception as exc:
        unreal.log_warning(
            "Could not set {}.{}: {}".format(type(obj).__name__, name, exc)
        )
    return False


def hide_editor_guides():
    hidden_count = 0
    for actor in all_level_actors():
        if actor.get_actor_label() not in EDITOR_GUIDE_LABELS:
            continue
        try:
            actor.set_actor_hidden_in_game(True)
            hidden_count += 1
        except Exception as exc:
            unreal.log_warning("Could not hide {} for capture: {}".format(actor.get_actor_label(), exc))
    unreal.log("Hid {} editor guide actors for render-target capture.".format(hidden_count))


def create_render_target():
    render_target = unreal.TextureRenderTarget2D()
    try_set_editor_property(render_target, "size_x", WIDTH)
    try_set_editor_property(render_target, "size_y", HEIGHT)
    render_target_format = getattr(unreal, "TextureRenderTargetFormat", None)
    if render_target_format is not None:
        try_set_editor_property(render_target, "render_target_format", render_target_format.RTF_RGBA8_SRGB)
    try_set_editor_property(render_target, "clear_color", unreal.LinearColor(0.02, 0.02, 0.025, 1.0))
    update_resource = getattr(render_target, "update_resource_immediate", None)
    if callable(update_resource):
        update_resource(True)
    return render_target


def export_render_target(world, render_target):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rendering_library = getattr(unreal, "RenderingLibrary", None)
    if rendering_library is None:
        rendering_library = getattr(unreal, "KismetRenderingLibrary", None)
    if rendering_library is None:
        raise RuntimeError("Unreal RenderingLibrary/KismetRenderingLibrary is not available")

    export_method = getattr(rendering_library, "export_render_target", None)
    if not callable(export_method):
        raise RuntimeError("Rendering library has no export_render_target method")

    export_method(world, render_target, str(OUTPUT_DIR), OUTPUT_FILE)
    output_path = OUTPUT_DIR / OUTPUT_FILE
    unreal.log("Exported Aerathea startup render-target review to {}".format(output_path))
    return output_path


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    world = unreal.EditorLevelLibrary.get_editor_world()
    if world is None:
        raise RuntimeError("Editor world is not available")

    review_rotation = look_at_rotation(REVIEW_LOCATION, REVIEW_TARGET)
    hide_editor_guides()
    render_target = create_render_target()
    capture_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.SceneCapture2D,
        REVIEW_LOCATION,
        review_rotation,
    )
    if capture_actor is None:
        raise RuntimeError("Failed to spawn SceneCapture2D")

    capture_component = capture_actor.get_component_by_class(unreal.SceneCaptureComponent2D)
    if capture_component is None:
        raise RuntimeError("SceneCapture2D has no SceneCaptureComponent2D")

    try_set_editor_property(capture_component, "texture_target", render_target)
    try_set_editor_property(capture_component, "fov_angle", REVIEW_FOV)
    capture_source = getattr(unreal.SceneCaptureSource, "SCS_BASE_COLOR", None)
    if capture_source is None:
        capture_source = unreal.SceneCaptureSource.SCS_FINAL_COLOR_LDR
    try_set_editor_property(capture_component, "capture_source", capture_source)
    try_set_editor_property(capture_component, "capture_every_frame", False)
    try_set_editor_property(capture_component, "capture_on_movement", False)

    unreal.log(
        "Capturing Aerathea startup map from {} / {} into {}x{} render target.".format(
            REVIEW_LOCATION,
            review_rotation,
            WIDTH,
            HEIGHT,
        )
    )
    capture_component.capture_scene()
    capture_component.capture_scene()
    output_path = export_render_target(world, render_target)

    try:
        unreal.EditorLevelLibrary.destroy_actor(capture_actor)
    except Exception as exc:
        unreal.log_warning("Could not destroy temporary capture actor: {}".format(exc))

    if not output_path.exists():
        raise RuntimeError("Render-target export did not create {}".format(output_path))


main()
