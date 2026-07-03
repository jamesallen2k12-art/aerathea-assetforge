import math
import os
import traceback

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_ReviewIsland"
REVIEW_LOCATION = unreal.Vector(-2500.0, -3600.0, 1850.0)
REVIEW_TARGET = unreal.Vector(0.0, 0.0, 120.0)
REVIEW_FOV = 52.0
APPLY_ON_TICKS = (2, 15, 45)
STOP_ON_TICK = 70
AUTO_BEGIN_PLAY = os.environ.get("AET_REVIEW_AUTO_PLAY", "0").lower() in ("1", "true", "yes")


def review_rotator(pitch, yaw, roll=0.0):
    return unreal.Rotator(roll, pitch, yaw)


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
    return review_rotator(pitch, yaw)


def safe_call(description, callback):
    try:
        callback()
        return True
    except Exception as exc:
        unreal.log_warning("{} failed: {}".format(description, exc))
        return False


def get_active_viewport_key(level_editor_subsystem):
    try:
        return level_editor_subsystem.get_active_viewport_config_key()
    except Exception:
        return unreal.Name("")


def get_viewport_keys(level_editor_subsystem):
    keys = []
    try:
        keys.extend(list(level_editor_subsystem.get_viewport_config_keys()))
    except Exception:
        pass
    keys.append(get_active_viewport_key(level_editor_subsystem))
    keys.append(unreal.Name(""))

    unique = []
    seen = set()
    for key in keys:
        text = str(key)
        if text not in seen:
            seen.add(text)
            unique.append(key)
    return unique


def editor_world_is_review_island():
    try:
        world = unreal.EditorLevelLibrary.get_editor_world()
        if world is None:
            return False
        return "L_Aerathea_ReviewIsland" in world.get_path_name()
    except Exception:
        return False


def apply_viewport():
    if not editor_world_is_review_island():
        if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
            raise RuntimeError("Failed to load review island: {}".format(LEVEL_PATH))

    rotation = look_at_rotation(REVIEW_LOCATION, REVIEW_TARGET)
    world = unreal.EditorLevelLibrary.get_editor_world()
    unreal.SystemLibrary.execute_console_command(world, "DisableAllScreenMessages")
    unreal.SystemLibrary.execute_console_command(world, "VIEWMODE UNLIT")
    unreal.EditorLevelLibrary.clear_actor_selection_set()

    safe_call(
        "UnrealEditorSubsystem viewport camera",
        lambda: unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).set_level_viewport_camera_info(
            REVIEW_LOCATION,
            rotation,
        ),
    )
    safe_call(
        "EditorLevelLibrary viewport camera",
        lambda: unreal.EditorLevelLibrary.set_level_viewport_camera_info(REVIEW_LOCATION, rotation),
    )

    level_editor = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    if level_editor is not None:
        for viewport_key in get_viewport_keys(level_editor):
            safe_call("eject pilot {}".format(viewport_key), lambda key=viewport_key: level_editor.eject_pilot_level_actor(key))
            safe_call(
                "set camera {}".format(viewport_key),
                lambda key=viewport_key: level_editor.set_level_viewport_camera_info(REVIEW_LOCATION, rotation, key),
            )
            safe_call("set FOV {}".format(viewport_key), lambda key=viewport_key: level_editor.set_level_viewport_fov(REVIEW_FOV, key))
            safe_call("disable exact camera {}".format(viewport_key), lambda key=viewport_key: level_editor.set_exact_camera_view(False, key))
            safe_call("disable game view {}".format(viewport_key), lambda key=viewport_key: level_editor.editor_set_game_view(False, key))
        safe_call("invalidate editor viewports", lambda: level_editor.editor_invalidate_viewports())
    else:
        safe_call("invalidate editor viewports", lambda: unreal.EditorLevelLibrary.editor_invalidate_viewports())

    unreal.log(
        "Applied Aerathea review island viewport at {} targeting {} with unlit view mode.".format(
            REVIEW_LOCATION,
            REVIEW_TARGET,
        )
    )


state = {"ticks": 0, "handle": None, "applied_ticks": set()}
state["pie_requested"] = False


def request_begin_play_once():
    if not AUTO_BEGIN_PLAY or state["pie_requested"]:
        return
    level_editor = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    if level_editor is None:
        return
    if safe_call("begin Play In Editor review", level_editor.editor_request_begin_play):
        state["pie_requested"] = True
        if state["handle"] is not None:
            unreal.unregister_slate_post_tick_callback(state["handle"])
            state["handle"] = None
        unreal.log("Requested Aerathea review island Play In Editor camera review.")


def on_tick(delta_time):
    state["ticks"] += 1

    for tick in APPLY_ON_TICKS:
        if state["ticks"] >= tick and tick not in state["applied_ticks"]:
            state["applied_ticks"].add(tick)
            try:
                apply_viewport()
                if tick >= 15:
                    request_begin_play_once()
            except Exception as exc:
                unreal.log_error(
                    "Review island viewport apply failed on tick {}: {}\n{}".format(
                        state["ticks"],
                        exc,
                        traceback.format_exc(),
                    )
                )
            return

    if state["handle"] is not None and state["ticks"] >= STOP_ON_TICK:
        unreal.unregister_slate_post_tick_callback(state["handle"])
        state["handle"] = None
        unreal.log("Aerathea review island viewport setup finished after {} ticks.".format(state["ticks"]))


state["handle"] = unreal.register_slate_post_tick_callback(on_tick)
try:
    apply_viewport()
    request_begin_play_once()
except Exception as exc:
    unreal.log_error("Immediate review island viewport apply failed: {}\n{}".format(exc, traceback.format_exc()))
