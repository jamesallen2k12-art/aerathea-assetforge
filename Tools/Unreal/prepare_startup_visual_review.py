import unreal
import math


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
REVIEW_LOCATION = unreal.Vector(-2350.0, 1600.0, 1280.0)
REVIEW_TARGET = unreal.Vector(-70.0, 160.0, 110.0)
REVIEW_FOV = 70.0
APPLY_ON_TICK = 45
STOP_ON_TICK = 70
REQUEST_PIE = True
REVIEW_ACTOR_LABELS = [
    "AET_PROD_TargetDummy_A01",
    "AET_PROD_Portal_A01",
    "AET_PROD_WorkshopCrate_A01",
    "AET_PROD_MKG_AetherKnife_A01",
    "AET_PROD_MKG_AetherCoreUnit_A01",
    "AET_PROD_MKG_SparkPistol_A01",
    "AET_PROD_MKG_AetheriumGrenade_A01",
]
EDITOR_GUIDE_LABELS = [
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_PROD_PlayerStart_Review_A01",
    "AET_PROD_Camera_Review_A01",
    "AET_PROD_ReviewCameraDirector_A01",
    "AET_PROD_ReviewFillLight_A01",
    "AET_BOOT_Camera_Overview",
    "AET_BOOT_Label_StyleTarget",
]


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


def try_set_editor_property(obj, names, value):
    for name in names:
        try:
            obj.set_editor_property(name, value)
            return name
        except Exception:
            pass
    return None


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def hide_editor_guide(actor):
    method = getattr(actor, "set_is_temporarily_hidden_in_editor", None)
    if callable(method):
        try:
            method(True)
            return True
        except Exception as exc:
            unreal.log_warning(
                "Could not hide {} from editor review through set_is_temporarily_hidden_in_editor: {}".format(
                    actor.get_actor_label(),
                    exc,
                )
            )
    return False


if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
    raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

state = {"ticks": 0, "handle": None, "applied": False}


def apply_visual_review_view():
    review_rotation = look_at_rotation(REVIEW_LOCATION, REVIEW_TARGET)
    unreal.EditorLevelLibrary.clear_actor_selection_set()
    actors_by_label = {actor.get_actor_label(): actor for actor in all_level_actors()}
    review_actors = [
        actors_by_label[label]
        for label in REVIEW_ACTOR_LABELS
        if label in actors_by_label
    ]

    hidden_guide_count = 0
    for label in EDITOR_GUIDE_LABELS:
        actor = actors_by_label.get(label)
        if actor is not None and hide_editor_guide(actor):
            hidden_guide_count += 1

    if REQUEST_PIE:
        director = actors_by_label.get("AET_PROD_ReviewCameraDirector_A01")
        if director is not None:
            capture_prop = try_set_editor_property(
                director,
                ("capture_review_screenshot", "b_capture_review_screenshot", "bCaptureReviewScreenshot"),
                True,
            )
            try_set_editor_property(director, ("screenshot_width", "ScreenshotWidth"), 1280)
            try_set_editor_property(director, ("screenshot_height", "ScreenshotHeight"), 720)
            try_set_editor_property(director, ("screenshot_delay_seconds", "ScreenshotDelaySeconds"), 0.5)
            if capture_prop is None:
                unreal.log_warning("Could not enable runtime review screenshot on {}".format(director.get_actor_label()))
            else:
                unreal.log("Enabled runtime review screenshot through {}.{}.".format(director.get_actor_label(), capture_prop))

        review_camera = actors_by_label.get("AET_PROD_Camera_Review_A01")
        if review_camera is not None:
            review_camera.set_actor_location(REVIEW_LOCATION, False, False)
            review_camera.set_actor_rotation(review_rotation, False)
            camera_component = review_camera.get_component_by_class(unreal.CameraComponent)
            if camera_component is not None:
                try_set_editor_property(camera_component, ("field_of_view", "FieldOfView"), REVIEW_FOV)

    world = unreal.EditorLevelLibrary.get_editor_world()
    unreal.SystemLibrary.execute_console_command(world, "VIEWMODE UNLIT")

    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    set_selected = getattr(actor_subsystem, "set_selected_level_actors", None)
    if callable(set_selected):
        set_selected(review_actors)
    else:
        unreal.EditorLevelLibrary.set_selected_level_actors(review_actors)
    unreal.SystemLibrary.execute_console_command(world, "Editor.FocusViewportOnSelection")

    unreal.EditorLevelLibrary.set_level_viewport_camera_info(REVIEW_LOCATION, review_rotation)
    try:
        unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).set_level_viewport_camera_info(
            REVIEW_LOCATION,
            review_rotation,
        )
    except Exception as exc:
        unreal.log_warning("Could not set viewport camera through UnrealEditorSubsystem: {}".format(exc))

    unreal.SystemLibrary.execute_console_command(world, "Editor.FocusViewportOnSelection")
    unreal.EditorLevelLibrary.editor_invalidate_viewports()
    unreal.log(
        "Prepared Aerathea startup visual review viewport after UI init at {} / {} with {} selected actors.".format(
            REVIEW_LOCATION,
            review_rotation,
            len(review_actors),
        )
    )
    unreal.log("Temporarily hid {} editor guide actors for startup visual review.".format(hidden_guide_count))


def on_tick(delta_time):
    state["ticks"] += 1

    if not state["applied"] and state["ticks"] >= APPLY_ON_TICK:
        state["applied"] = True
        apply_visual_review_view()
        return

    if state["ticks"] >= STOP_ON_TICK:
        unreal.unregister_slate_post_tick_callback(state["handle"])
        unreal.log(
            "Aerathea startup visual review post-tick setup complete after {} ticks.".format(
                state["ticks"]
            )
        )


state["handle"] = unreal.register_slate_post_tick_callback(on_tick)
unreal.log(
    "Aerathea startup visual review setup deferred until editor UI tick {}.".format(
        APPLY_ON_TICK
    )
)

try:
    apply_visual_review_view()
    state["applied"] = True
    unreal.log("Aerathea startup visual review applied immediately.")
    if REQUEST_PIE:
        level_editor_subsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
        level_editor_subsystem.editor_request_begin_play()
        unreal.log("Requested Aerathea startup Play In Editor review session.")
except Exception as exc:
    unreal.log_warning("Immediate Aerathea startup visual review setup failed: {}".format(exc))
