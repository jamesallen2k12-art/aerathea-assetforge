import math
import sys
from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from Tools.review_alignment_markers import REVIEW_ALIGNMENT_MARKERS, REVIEW_MARKER_TAG  # noqa: E402


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
DEBUG_MATERIAL_PATH = "/Game/Aerathea/Materials/Debug"
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


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def ensure_marker_material(marker_id, color):
    ensure_directory(DEBUG_MATERIAL_PATH)
    asset_path = "{}/M_AET_ReviewMarker_{}".format(DEBUG_MATERIAL_PATH, marker_id)
    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        return unreal.load_asset(asset_path)

    material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name="M_AET_ReviewMarker_{}".format(marker_id),
        package_path=DEBUG_MATERIAL_PATH,
        asset_class=unreal.Material,
        factory=unreal.MaterialFactoryNew(),
    )
    if material is None:
        raise RuntimeError("Failed to create review marker material {}".format(asset_path))

    mat_lib = unreal.MaterialEditingLibrary
    base = mat_lib.create_material_expression(
        material,
        unreal.MaterialExpressionConstant3Vector,
        -420,
        -80,
    )
    linear = unreal.LinearColor(color[0], color[1], color[2], color[3])
    base.set_editor_property("constant", linear)
    mat_lib.connect_material_property(base, "", unreal.MaterialProperty.MP_BASE_COLOR)

    emissive = mat_lib.create_material_expression(
        material,
        unreal.MaterialExpressionConstant3Vector,
        -420,
        120,
    )
    emissive.set_editor_property("constant", linear)
    mat_lib.connect_material_property(emissive, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)

    unreal.MaterialEditingLibrary.recompile_material(material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)
    return material


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


def is_shape_component(component):
    return component.get_class().get_name() in {
        "BoxComponent",
        "CapsuleComponent",
        "SphereComponent",
    }


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
            if is_shape_component(component):
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


def tag_review_marker(actor):
    tags = list(actor.get_editor_property("tags"))
    for tag in (unreal.Name(REVIEW_MARKER_TAG), unreal.Name(FIRST_SLICE_TAG)):
        if tag not in tags:
            tags.append(tag)
    actor.set_editor_property("tags", tags)
    return actor


def hide_review_marker(actor):
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
            try:
                component.set_collision_enabled(unreal.CollisionEnabled.NO_COLLISION)
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


def ensure_review_alignment_markers(review_rotation):
    sphere_mesh = unreal.load_asset("/Engine/BasicShapes/Sphere.Sphere")
    if sphere_mesh is None:
        raise RuntimeError("Missing /Engine/BasicShapes/Sphere.Sphere for review markers")

    for marker in REVIEW_ALIGNMENT_MARKERS:
        marker_id = marker["id"]
        x, y, z = marker["location"]
        location = unreal.Vector(x, y, z)
        material = ensure_marker_material(marker_id, marker["color"])

        marker_actor = find_actor_by_label("AET_REVIEW_MARKER_{}".format(marker_id))
        if marker_actor is None:
            marker_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
                unreal.StaticMeshActor,
                location,
                review_rotator(0.0, 0.0),
            )
            if marker_actor is None:
                raise RuntimeError("Failed to spawn review marker {}".format(marker_id))
            marker_actor.set_actor_label("AET_REVIEW_MARKER_{}".format(marker_id))
        set_actor_transform(
            marker_actor,
            location,
            review_rotator(0.0, 0.0),
            unreal.Vector(0.9, 0.9, 0.9) if marker_id == "E" else unreal.Vector(0.7, 0.7, 0.7),
        )
        tag_review_marker(marker_actor)
        component = marker_actor.get_component_by_class(unreal.StaticMeshComponent)
        if component is None:
            raise RuntimeError("Review marker {} has no StaticMeshComponent".format(marker_id))
        component.set_static_mesh(sphere_mesh)
        component.set_material(0, material)
        hide_review_marker(marker_actor)

        text_actor = find_actor_by_label("AET_REVIEW_MARKER_LABEL_{}".format(marker_id))
        if text_actor is None:
            text_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
                unreal.TextRenderActor,
                unreal.Vector(x, y, z + 115.0),
                review_rotation,
            )
            if text_actor is None:
                raise RuntimeError("Failed to spawn review marker label {}".format(marker_id))
            text_actor.set_actor_label("AET_REVIEW_MARKER_LABEL_{}".format(marker_id))
        set_actor_transform(text_actor, unreal.Vector(x, y, z + 115.0), review_rotation)
        tag_review_marker(text_actor)
        text_component = text_actor.get_component_by_class(unreal.TextRenderComponent)
        if text_component is not None:
            text_component.set_text(marker["label"])
            safe_set(text_component, "world_size", 135.0 if marker_id != "E" else 160.0)
            safe_set(
                text_component,
                "text_render_color",
                unreal.Color(
                    int(marker["color"][0] * 255.0),
                    int(marker["color"][1] * 255.0),
                    int(marker["color"][2] * 255.0),
                    255,
                ),
            )
        hide_review_marker(text_actor)


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    review_location = unreal.Vector(4710, -2880, 2575)
    review_target = unreal.Vector(-70, 160, 110)
    review_rotation = look_at_rotation(review_location, review_target)
    ensure_review_alignment_markers(review_rotation)

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
        safe_set(camera_component, "field_of_view", 65.0)
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
        safe_set(director, ("capture_review_screenshot", "b_capture_review_screenshot", "bCaptureReviewScreenshot"), False)
        safe_set(director, "screenshot_width", 1280)
        safe_set(director, "screenshot_height", 720)
        safe_set(director, "screenshot_delay_seconds", 0.5)

    fill_light = ensure_actor("AET_PROD_ReviewFillLight_A01", unreal.PointLight, unreal.Vector(-160, -180, 520))
    fill_component = fill_light.get_component_by_class(unreal.PointLightComponent)
    if fill_component is not None:
        safe_set(fill_component, "intensity", 6000.0)
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
            safe_set(directional_component, ("forward_shading_priority", "ForwardShadingPriority"), 1)
        for actor in all_level_actors():
            component = actor.get_component_by_class(unreal.DirectionalLightComponent)
            if actor != directional and component is not None:
                safe_set(component, ("forward_shading_priority", "ForwardShadingPriority"), 0)

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
