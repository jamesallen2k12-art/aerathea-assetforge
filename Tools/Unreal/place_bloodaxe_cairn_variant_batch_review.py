from pathlib import Path
import math
import sys

import unreal


sys.path.append(str(Path(__file__).resolve().parent))
from bloodaxe_cairn_variant_batch_config import ASSETS, MATERIAL_INSTANCE_PATH  # noqa: E402


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_ReviewIsland"
REVIEW_TAG = "AET_BLOODAXE_CAIRN_VARIANT_BATCH_REVIEW"
STATIC_REVIEW_TAG = "AET_STATIC_REVIEW_TARGET"
CAMERA_TAG = "AET_REVIEW_CAMERA"
LEGACY_REVIEW_LABEL_PREFIXES = (
    "AET_REVIEW_CurrentAsset_",
    "AET_REVIEW_Label_CurrentAsset_",
)


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


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def tag_actor(actor, *tags):
    current = list(actor.get_editor_property("tags"))
    for tag in tags:
        tag_name = unreal.Name(tag)
        if tag_name not in current:
            current.append(tag_name)
    actor.set_editor_property("tags", current)


def clear_previous_batch_review():
    for actor in all_level_actors():
        tags = list(actor.get_editor_property("tags"))
        if unreal.Name(REVIEW_TAG) in tags or actor.get_actor_label().startswith("AET_REVIEW_GIA_BloodAxeCairnVariant_"):
            unreal.EditorLevelLibrary.destroy_actor(actor)


def hide_legacy_single_asset_review_targets():
    for actor in all_level_actors():
        label = actor.get_actor_label()
        if not any(label.startswith(prefix) for prefix in LEGACY_REVIEW_LABEL_PREFIXES):
            continue
        actor.set_actor_hidden_in_game(True)
        actor.set_is_temporarily_hidden_in_editor(True)
        component = actor.get_component_by_class(unreal.SceneComponent)
        if component is not None:
            try:
                component.set_visibility(False, True)
                component.set_hidden_in_game(True, True)
            except Exception:
                pass


def set_metadata(mesh, tag, value):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if callable(setter):
        setter(mesh, tag, str(value))


def actor_location(index):
    columns = 6
    spacing_x = 560.0
    spacing_y = 520.0
    col = index % columns
    row = index // columns
    return unreal.Vector((col - 2.5) * spacing_x, 620.0 + (row * spacing_y), 0.0)


def place_asset(index, asset, material):
    mesh = unreal.load_asset(asset["unreal_path"])
    if mesh is None:
        raise RuntimeError("Missing imported mesh {}".format(asset["unreal_path"]))
    label = "AET_REVIEW_GIA_BloodAxeCairnVariant_{:02d}_{}".format(index + 1, asset["name"])
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor,
        actor_location(index),
        review_rotator(0.0, -18.0),
    )
    if actor is None:
        raise RuntimeError("Failed to spawn {}".format(label))
    actor.set_actor_label(label)
    actor.set_actor_location(actor_location(index), False, True)
    actor.set_actor_rotation(review_rotator(0.0, -18.0), False)
    actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
    actor.set_actor_hidden_in_game(False)
    tag_actor(actor, REVIEW_TAG, STATIC_REVIEW_TAG)

    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        raise RuntimeError("{} has no StaticMeshComponent".format(label))
    component.set_static_mesh(mesh)
    component.set_mobility(unreal.ComponentMobility.STATIC)
    component.set_collision_enabled(unreal.CollisionEnabled.QUERY_AND_PHYSICS)
    collision_profile = getattr(component, "set_collision_profile_name", None)
    if callable(collision_profile):
        component.set_collision_profile_name("BlockAll")
    component.set_visibility(True, True)
    component.set_hidden_in_game(False, True)
    component.set_material(0, material)

    set_metadata(mesh, "Aerathea.StaticMesh.ReviewIslandPlaced", "true")
    set_metadata(mesh, "Aerathea.StaticMesh.ReviewIslandActor", label)
    set_metadata(mesh, "Aerathea.StaticMesh.VisualReview", "review_island_batch_capture_ready_not_final_visual_approval")
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return actor


def configure_review_camera():
    camera_location = unreal.Vector(-2450.0, -4100.0, 2050.0)
    camera_target = unreal.Vector(0.0, 840.0, 115.0)
    camera_rotation = look_at_rotation(camera_location, camera_target)
    camera = find_actor_by_label("AET_REVIEW_Camera_Main_A01")
    if camera is None:
        camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CameraActor, camera_location, camera_rotation)
        if camera is None:
            raise RuntimeError("Failed to create review island camera")
        camera.set_actor_label("AET_REVIEW_Camera_Main_A01")
    camera.set_actor_location(camera_location, False, True)
    camera.set_actor_rotation(camera_rotation, False)
    tag_actor(camera, CAMERA_TAG)
    component = camera.get_component_by_class(unreal.CameraComponent)
    if component is not None:
        try:
            component.set_editor_property("field_of_view", 64.0)
        except Exception:
            pass
        try:
            component.set_editor_property("auto_activate", True)
        except Exception:
            pass
    try:
        camera.set_editor_property("auto_activate_for_player", unreal.AutoReceiveInput.PLAYER0)
    except Exception:
        pass


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load review island level: {}".format(LEVEL_PATH))
    material = unreal.load_asset(MATERIAL_INSTANCE_PATH)
    if material is None:
        raise RuntimeError("Missing shared variant material instance {}".format(MATERIAL_INSTANCE_PATH))

    clear_previous_batch_review()
    hide_legacy_single_asset_review_targets()
    for index, asset in enumerate(ASSETS):
        place_asset(index, asset, material)
    configure_review_camera()

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save review island after Blood Axe cairn variant placement")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Maps", only_if_is_dirty=True, recursive=True)
    for asset in ASSETS:
        unreal.EditorAssetLibrary.save_directory(asset["unreal_path"].rsplit("/", 1)[0], only_if_is_dirty=True, recursive=True)
    unreal.log("Placed {} Blood Axe cairn variants on review island for batch capture.".format(len(ASSETS)))


if __name__ == "__main__":
    main()
