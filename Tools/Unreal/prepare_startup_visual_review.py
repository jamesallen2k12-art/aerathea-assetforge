import math
import traceback

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
REVIEW_LOCATION = unreal.Vector(4710.0, -2880.0, 2575.0)
REVIEW_TARGET = unreal.Vector(-70.0, 160.0, 110.0)
REVIEW_FOV = 65.0
# The editor can restore its last viewport after script startup. Reapply the
# camera after Slate has settled so the live view matches the DCC proof render.
APPLY_ON_TICKS = (10, 45, 90)
STOP_ON_TICK = 120
REQUEST_PIE = False
REVIEW_ACTOR_LABELS = [
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
CAMERA_GUIDE_LABELS = [
    "AET_PROD_Camera_Review_A01",
    "AET_BOOT_Camera_Overview",
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
    try:
        actor.set_actor_hidden_in_game(True)
    except Exception:
        pass
    method = getattr(actor, "set_is_temporarily_hidden_in_editor", None)
    if callable(method):
        try:
            method(True)
        except Exception as exc:
            unreal.log_warning(
                "Could not hide {} from editor review through set_is_temporarily_hidden_in_editor: {}".format(
                    actor.get_actor_label(),
                    exc,
                )
            )

    try:
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            try:
                component.set_visibility(False, True)
            except Exception:
                pass
            try:
                component.set_hidden_in_game(True, True)
            except Exception:
                pass
    except Exception:
        pass

    return True


def move_camera_guide_out_of_review(actor):
    if actor.get_component_by_class(unreal.CameraComponent) is None:
        return False
    try:
        actor.set_actor_location(
            unreal.Vector(REVIEW_LOCATION.x, REVIEW_LOCATION.y, REVIEW_LOCATION.z - 100000.0),
            False,
            False,
        )
        return True
    except Exception as exc:
        unreal.log_warning("Could not move camera guide {} out of review view: {}".format(actor.get_actor_label(), exc))
        return False


def get_active_viewport_key(level_editor_subsystem):
    try:
        return level_editor_subsystem.get_active_viewport_config_key()
    except Exception:
        return unreal.Name("")


def get_review_viewport_keys(level_editor_subsystem):
    keys = []
    try:
        keys.extend(list(level_editor_subsystem.get_viewport_config_keys()))
    except Exception:
        pass
    keys.append(get_active_viewport_key(level_editor_subsystem))
    keys.append(unreal.Name(""))

    unique_keys = []
    seen = set()
    for key in keys:
        key_text = str(key)
        if key_text not in seen:
            seen.add(key_text)
            unique_keys.append(key)
    return unique_keys


def set_review_viewport(level_editor_subsystem, review_rotation):
    applied_keys = []

    try:
        editor_subsystem = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
        if editor_subsystem is not None:
            editor_subsystem.set_level_viewport_camera_info(REVIEW_LOCATION, review_rotation)
            applied_keys.append("primary:UnrealEditorSubsystem")
            try:
                active_info = editor_subsystem.get_level_viewport_camera_info()
                unreal.log("Primary viewport camera after set: {}".format(active_info))
            except Exception as exc:
                unreal.log_warning("Could not read primary viewport camera after set: {}".format(exc))
    except Exception as exc:
        unreal.log_warning("Could not set primary viewport camera through UnrealEditorSubsystem: {}".format(exc))

    try:
        unreal.EditorLevelLibrary.set_level_viewport_camera_info(REVIEW_LOCATION, review_rotation)
        applied_keys.append("primary:EditorLevelLibrary")
    except Exception as exc:
        unreal.log_warning("Could not set primary viewport camera through EditorLevelLibrary: {}".format(exc))

    for viewport_key in get_review_viewport_keys(level_editor_subsystem):
        try:
            level_editor_subsystem.eject_pilot_level_actor(viewport_key)
        except Exception as exc:
            unreal.log_warning("Could not eject pilot for {}: {}".format(viewport_key, exc))

        try:
            level_editor_subsystem.set_level_viewport_camera_info(
                REVIEW_LOCATION,
                review_rotation,
                viewport_key,
            )
        except Exception as exc:
            unreal.log_warning("Could not set level viewport camera for {}: {}".format(viewport_key, exc))

        try:
            level_editor_subsystem.set_level_viewport_fov(REVIEW_FOV, viewport_key)
        except Exception as exc:
            unreal.log_warning("Could not set level viewport FOV for {}: {}".format(viewport_key, exc))

        try:
            level_editor_subsystem.set_exact_camera_view(False, viewport_key)
        except Exception as exc:
            unreal.log_warning("Could not disable exact camera view for {}: {}".format(viewport_key, exc))

        try:
            level_editor_subsystem.editor_set_game_view(True, viewport_key)
        except Exception as exc:
            unreal.log_warning("Could not enable game view for {}: {}".format(viewport_key, exc))

        applied_keys.append(str(viewport_key))

    if applied_keys:
        unreal.log(
            "Set viewport(s) {} to proof-camera transform for free-perspective visual review.".format(
                ", ".join(applied_keys),
            )
        )


if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
    raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

state = {"ticks": 0, "handle": None, "applied_ticks": set()}


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

    moved_camera_guide_count = 0
    if not REQUEST_PIE:
        for label in CAMERA_GUIDE_LABELS:
            actor = actors_by_label.get(label)
            if actor is not None and move_camera_guide_out_of_review(actor):
                moved_camera_guide_count += 1

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
    if REQUEST_PIE and review_camera is not None:
        review_camera.set_actor_location(REVIEW_LOCATION, False, False)
        review_camera.set_actor_rotation(review_rotation, False)
        camera_component = review_camera.get_component_by_class(unreal.CameraComponent)
        if camera_component is not None:
            try_set_editor_property(camera_component, ("field_of_view", "FieldOfView"), REVIEW_FOV)

    world = unreal.EditorLevelLibrary.get_editor_world()
    unreal.SystemLibrary.execute_console_command(world, "DisableAllScreenMessages")
    unreal.SystemLibrary.execute_console_command(world, "VIEWMODE UNLIT")

    level_editor_subsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    set_review_viewport(level_editor_subsystem, review_rotation)
    unreal.EditorLevelLibrary.clear_actor_selection_set()

    try:
        level_editor_subsystem.editor_invalidate_viewports()
    except Exception:
        unreal.EditorLevelLibrary.editor_invalidate_viewports()
    unreal.log(
        "Prepared Aerathea startup visual review viewport after UI init at {} / {} with {} visible review actors.".format(
            REVIEW_LOCATION,
            review_rotation,
            len(review_actors),
        )
    )
    unreal.log("Temporarily hid {} editor guide actors for startup visual review.".format(hidden_guide_count))
    unreal.log("Temporarily moved {} camera guide actors out of the editor review frustum.".format(moved_camera_guide_count))


def on_tick(delta_time):
    state["ticks"] += 1

    for apply_tick in APPLY_ON_TICKS:
        if state["ticks"] >= apply_tick and apply_tick not in state["applied_ticks"]:
            state["applied_ticks"].add(apply_tick)
            try:
                apply_visual_review_view()
            except Exception as exc:
                unreal.log_error(
                    "Aerathea startup visual review setup failed on deferred tick {}: {}\n{}".format(
                        state["ticks"],
                        exc,
                        traceback.format_exc(),
                    )
                )
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
    "Aerathea startup visual review setup deferred until editor UI ticks {}.".format(
        ", ".join(str(tick) for tick in APPLY_ON_TICKS)
    )
)

try:
    apply_visual_review_view()
    unreal.log("Aerathea startup visual review applied immediately; deferred proof-camera reapplies remain scheduled.")
    if REQUEST_PIE:
        level_editor_subsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
        level_editor_subsystem.editor_request_begin_play()
        unreal.log("Requested Aerathea startup Play In Editor review session.")
except Exception as exc:
    unreal.log_error(
        "Immediate Aerathea startup visual review setup failed: {}\n{}".format(
            exc,
            traceback.format_exc(),
        )
    )
