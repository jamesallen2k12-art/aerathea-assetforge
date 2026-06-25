import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
FIRST_SLICE_TAG = "AET_FIRST_SLICE"
RUNTIME_VISIBLE_LABELS = [
    "AET_PROD_GroundTile_A01_R3_C3",
    "AET_PROD_TargetDummy_A01",
    "AET_PROD_Portal_A01",
    "AET_PROD_WorkshopCrate_A01",
    "AET_PROD_MKG_AetherKnife_A01",
    "AET_PROD_MKG_AetherCoreUnit_A01",
    "AET_PROD_MKG_SparkPistol_A01",
    "AET_PROD_MKG_AetheriumGrenade_A01",
    "AET_PROD_Camera_Review_A01",
    "AET_PROD_ReviewFillLight_A01",
    "AET_BOOT_KeyLight_Directional",
    "AET_BOOT_SkyLight",
]
RUNTIME_REVIEW_HIDDEN_LABELS = [
    "AET_BOOT_PlayerScale_180cm",
    "AET_BOOT_GnomeScale_110cm",
    "AET_BOOT_MinotaurScale_270cm",
    "AET_BOOT_Camera_Overview",
    "AET_BOOT_Label_StyleTarget",
]


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


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


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def tag_actor(actor):
    tags = list(actor.get_editor_property("tags"))
    first_slice_name = unreal.Name(FIRST_SLICE_TAG)
    if first_slice_name not in tags:
        tags.append(first_slice_name)
    actor.set_editor_property("tags", tags)
    return actor


def set_actor_transform(actor, location, rotation=None, scale=None):
    rotation = rotation or review_rotator(0.0, 0.0)
    scale = scale or unreal.Vector(1, 1, 1)
    try:
        actor.set_actor_location(location, False, True)
    except Exception:
        actor.set_actor_location(location, False, False)
    try:
        actor.set_actor_rotation(rotation, False)
    except Exception:
        pass
    actor.set_actor_scale3d(scale)


def activate_actor_for_review(actor):
    try:
        actor.set_actor_hidden_in_game(False)
    except Exception:
        pass
    try:
        actor.set_is_temporarily_hidden_in_editor(False)
    except Exception:
        pass
    try:
        for component in actor.get_components_by_class(unreal.PrimitiveComponent):
            try:
                component.set_visibility(True, True)
            except Exception:
                pass
            try:
                component.set_hidden_in_game(False, True)
            except Exception:
                pass
    except Exception:
        pass
    return actor


def hide_actor_for_runtime_review(actor):
    try:
        actor.set_actor_hidden_in_game(True)
    except Exception:
        pass
    try:
        actor.set_is_temporarily_hidden_in_editor(True)
    except Exception:
        pass
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
    return actor


def ensure_actor(label, actor_class, location, rotation=None, scale=None):
    actor = find_actor_by_label(label)
    if actor is None:
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, location, rotation or review_rotator(0.0, 0.0))
        if actor is None:
            raise RuntimeError("Failed to spawn {}".format(label))
        actor.set_actor_label(label)
    set_actor_transform(actor, location, rotation, scale)
    activate_actor_for_review(actor)
    tag_actor(actor)
    return actor


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    review_location = unreal.Vector(-2350, 1600, 1280)
    review_target = unreal.Vector(-70, 160, 110)
    review_rotation = look_at_rotation(review_location, review_target)

    for label in RUNTIME_REVIEW_HIDDEN_LABELS:
        actor = find_actor_by_label(label)
        if actor is not None:
            hide_actor_for_runtime_review(actor)

    for label in RUNTIME_VISIBLE_LABELS:
        actor = find_actor_by_label(label)
        if actor is not None:
            activate_actor_for_review(actor)

    player_start_class = getattr(unreal, "PlayerStart", None)
    if player_start_class is not None:
        ensure_actor("AET_PROD_PlayerStart_Review_A01", player_start_class, review_location, review_rotation)

    camera = ensure_actor("AET_PROD_Camera_Review_A01", unreal.CameraActor, review_location, review_rotation)
    camera.set_editor_property("tags", [unreal.Name("AET_REVIEW_CAMERA")])
    camera_component = camera.get_component_by_class(unreal.CameraComponent)
    if camera_component is not None:
        safe_set(camera_component, "field_of_view", 70.0)
        safe_set(camera_component, "auto_activate", True)
    safe_set(camera, "auto_activate_for_player", unreal.AutoReceiveInput.PLAYER0)

    director_class = getattr(unreal, "AETReviewCameraDirector", None)
    if director_class is not None:
        director = ensure_actor(
            "AET_PROD_ReviewCameraDirector_A01",
            director_class,
            unreal.Vector(-900, -80, 220),
            review_rotation,
        )
        safe_set(director, "b_capture_review_screenshot", False)
        safe_set(director, "screenshot_width", 1280)
        safe_set(director, "screenshot_height", 720)
        safe_set(director, "screenshot_delay_seconds", 0.5)

    fill_light = ensure_actor("AET_PROD_ReviewFillLight_A01", unreal.PointLight, unreal.Vector(-160, -180, 520))
    fill_component = fill_light.get_component_by_class(unreal.PointLightComponent)
    if fill_component is not None:
        safe_set(fill_component, "intensity", 350000.0)
        safe_set(fill_component, "attenuation_radius", 2200.0)
        safe_set(fill_component, "light_color", unreal.Color(180, 210, 255, 255))

    directional_class = getattr(unreal, "DirectionalLight", None)
    if directional_class is not None:
        directional = ensure_actor(
            "AET_BOOT_KeyLight_Directional",
            directional_class,
            unreal.Vector(-260, -420, 780),
            review_rotator(-38.0, 42.0),
        )
        directional_component = directional.get_component_by_class(unreal.DirectionalLightComponent)
        if directional_component is not None:
            safe_set(directional_component, "intensity", 5.0)
            safe_set(directional_component, "light_color", unreal.Color(255, 236, 205, 255))

    sky_light_class = getattr(unreal, "SkyLight", None)
    if sky_light_class is not None:
        sky_light = ensure_actor("AET_BOOT_SkyLight", sky_light_class, unreal.Vector(0, 0, 460), review_rotator(0.0, 0.0))
        sky_component = sky_light.get_component_by_class(unreal.SkyLightComponent)
        if sky_component is not None:
            safe_set(sky_component, "intensity", 1.5)

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save runtime review updates to startup level")

    unreal.log("Prepared startup map runtime review camera, visibility, and lighting at {} / {}.".format(review_location, review_rotation))


main()
