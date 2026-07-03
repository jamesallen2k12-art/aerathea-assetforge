from pathlib import Path
import sys

import unreal


sys.path.append(str(Path(__file__).resolve().parent))
import place_bloodaxe_cairn_variant_batch_review as batch_review  # noqa: E402
from bloodaxe_cairn_variant_batch_config import ASSETS, MATERIAL_INSTANCE_PATH  # noqa: E402


def configure_texture_review_camera():
    camera_location = unreal.Vector(-1640.0, -2380.0, 1180.0)
    camera_target = unreal.Vector(0.0, 850.0, 96.0)
    camera_rotation = batch_review.look_at_rotation(camera_location, camera_target)
    camera = batch_review.find_actor_by_label("AET_REVIEW_Camera_Main_A01")
    if camera is None:
        camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CameraActor, camera_location, camera_rotation)
        if camera is None:
            raise RuntimeError("Failed to create review island camera")
        camera.set_actor_label("AET_REVIEW_Camera_Main_A01")
    camera.set_actor_location(camera_location, False, True)
    camera.set_actor_rotation(camera_rotation, False)
    batch_review.tag_actor(camera, batch_review.CAMERA_TAG)
    component = camera.get_component_by_class(unreal.CameraComponent)
    if component is not None:
        try:
            component.set_editor_property("field_of_view", 55.0)
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


def set_metadata(mesh, tag, value):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if callable(setter):
        setter(mesh, tag, str(value))


def main():
    if not unreal.EditorLevelLibrary.load_level(batch_review.LEVEL_PATH):
        raise RuntimeError("Failed to load review island level: {}".format(batch_review.LEVEL_PATH))
    material = unreal.load_asset(MATERIAL_INSTANCE_PATH)
    if material is None:
        raise RuntimeError("Missing shared variant material instance {}".format(MATERIAL_INSTANCE_PATH))

    batch_review.clear_previous_batch_review()
    batch_review.hide_legacy_single_asset_review_targets()
    for index, asset in enumerate(ASSETS):
        batch_review.place_asset(index, asset, material)
        mesh = unreal.load_asset(asset["unreal_path"])
        if mesh is not None:
            set_metadata(mesh, "Aerathea.StaticMesh.TextureMaterialReview", "close_review_island_capture_ready_not_final_visual_approval")
            unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    configure_texture_review_camera()

    if not unreal.EditorLevelLibrary.save_current_level():
        raise RuntimeError("Failed to save review island after Blood Axe cairn variant texture placement")
    unreal.EditorAssetLibrary.save_directory("/Game/Aerathea/Maps", only_if_is_dirty=True, recursive=True)
    for asset in ASSETS:
        unreal.EditorAssetLibrary.save_directory(asset["unreal_path"].rsplit("/", 1)[0], only_if_is_dirty=True, recursive=True)
    unreal.log("Placed {} Blood Axe cairn variants for close texture/material review capture.".format(len(ASSETS)))


if __name__ == "__main__":
    main()
