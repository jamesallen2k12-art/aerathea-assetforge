from pathlib import Path
import math

import unreal


ROOT = Path(__file__).resolve().parents[2]
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
OUTPUT_DIR = ROOT / "Saved/Automation/StartupReview"
OUTPUT_FILE = "AeratheaStartupReview.png"
WIDTH = 1280
HEIGHT = 720
REVIEW_LOCATION = unreal.Vector(4710.0, -2880.0, 2575.0)
REVIEW_TARGET = unreal.Vector(-70.0, 160.0, 110.0)
REVIEW_FOV = 65.0

RUNTIME_VISIBLE_LABELS = {
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
    "AET_PROD_Palisade_Wall_A01",
    "AET_PROD_Palisade_Post_A01",
    "AET_PROD_Palisade_EndCap_A01",
    "AET_PROD_Palisade_Corner_A01",
    "AET_PROD_Palisade_Gate_A01",
    "AET_PROD_Camera_Review_A01",
    "AET_PROD_ReviewFillLight_A01",
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
}

RUNTIME_HIDDEN_LABELS = {
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_BOOT_Camera_Overview",
    "AET_BOOT_Label_StyleTarget",
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
                try:
                    component.set_visibility(False, True)
                except Exception:
                    pass
                try:
                    component.set_hidden_in_game(True, True)
                except Exception:
                    pass
                continue
            try:
                component.set_visibility(visible, True)
            except Exception:
                pass
            try:
                component.set_hidden_in_game(not visible, True)
            except Exception:
                pass
    except Exception:
        pass


def configure_review_camera(label_lookup, review_rotation):
    review_camera = label_lookup.get("AET_PROD_Camera_Review_A01")
    if review_camera is None:
        raise RuntimeError("Missing review camera actor AET_PROD_Camera_Review_A01")

    review_camera.set_actor_location(REVIEW_LOCATION, False, False)
    review_camera.set_actor_rotation(review_rotation, False)
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


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / OUTPUT_FILE
    if output_path.exists():
        output_path.unlink()

    review_rotation = look_at_rotation(REVIEW_LOCATION, REVIEW_TARGET)
    label_lookup = actors_by_label()

    for label in RUNTIME_HIDDEN_LABELS:
        actor = label_lookup.get(label)
        if actor is not None:
            set_actor_runtime_visibility(actor, False)

    for label in RUNTIME_VISIBLE_LABELS:
        actor = label_lookup.get(label)
        if actor is not None:
            set_actor_runtime_visibility(actor, True)

    configure_review_camera(label_lookup, review_rotation)
    configure_review_director(label_lookup, output_path)

    unreal.log(
        "Prepared Aerathea runtime startup capture at {} / {} -> {}.".format(
            REVIEW_LOCATION,
            review_rotation,
            output_path,
        )
    )

    level_editor_subsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    level_editor_subsystem.editor_request_begin_play()
    unreal.log("Requested Play In Editor for Aerathea runtime startup capture.")


main()
