from pathlib import Path
import sys

import unreal


sys.path.append(str(Path(__file__).resolve().parent))
from bloodaxe_cairn_variant_batch_config import ASSETS, MATERIAL_INSTANCE_PATH, PARENT_MATERIAL_PATH  # noqa: E402
from import_bloodaxe_cairn_variant_textures import (  # noqa: E402
    TEXTURE_ASSET_PATHS,
    TEXTURE_BASENAME,
    TEXTURE_DESTINATION,
    TEXTURE_SOURCES,
)


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def metadata_value(asset, tag):
    getter = getattr(unreal.EditorAssetLibrary, "get_metadata_tag", None)
    if not callable(getter):
        return None
    value = getter(asset, tag)
    return "" if value is None else str(value)


def validate_texture_sources(failures):
    for key, source in TEXTURE_SOURCES.items():
        if not source.exists():
            failures.append("Missing source {} texture {}".format(key, source))
        elif source.stat().st_size <= 0:
            failures.append("Source {} texture is empty {}".format(key, source))


def validate_texture_assets(failures):
    for key, asset_path in TEXTURE_ASSET_PATHS.items():
        texture = unreal.load_asset(asset_path)
        if texture is None:
            failures.append("Missing Unreal {} texture {}".format(key, asset_path))
            continue
        srgb = bool(texture.get_editor_property("srgb"))
        if key == "bc" and not srgb:
            failures.append("{} should have sRGB enabled".format(asset_path))
        if key != "bc" and srgb:
            failures.append("{} should have sRGB disabled".format(asset_path))
        if key == "normal":
            compression = str(texture.get_editor_property("compression_settings"))
            if "TC_NORMALMAP" not in compression:
                failures.append("{} compression is {}, expected TC_NORMALMAP".format(asset_path, compression))
        if key == "orm":
            compression = str(texture.get_editor_property("compression_settings"))
            if "TC_MASKS" not in compression:
                failures.append("{} compression is {}, expected TC_MASKS".format(asset_path, compression))


def validate_materials(failures):
    parent = unreal.load_asset(PARENT_MATERIAL_PATH)
    if parent is None:
        failures.append("Missing parent material {}".format(PARENT_MATERIAL_PATH))
    instance = unreal.load_asset(MATERIAL_INSTANCE_PATH)
    if instance is None:
        failures.append("Missing material instance {}".format(MATERIAL_INSTANCE_PATH))
        return
    try:
        actual_parent = instance.get_editor_property("parent")
    except Exception:
        actual_parent = None
    if actual_parent is None or asset_path_without_object(actual_parent) != PARENT_MATERIAL_PATH:
        failures.append("{} parent is {}, expected {}".format(MATERIAL_INSTANCE_PATH, actual_parent, PARENT_MATERIAL_PATH))


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def validate_mesh_materials_and_metadata(failures):
    for asset in ASSETS:
        mesh = unreal.load_asset(asset["unreal_path"])
        if mesh is None:
            failures.append("Missing mesh {}".format(asset["unreal_path"]))
            continue
        slots = material_slots(mesh)
        if len(slots) != 1:
            failures.append("{} has {} material slots, expected 1".format(asset["unreal_path"], len(slots)))
            continue
        material = slots[0].get_editor_property("material_interface")
        if material is None or asset_path_without_object(material) != MATERIAL_INSTANCE_PATH:
            failures.append("{} material slot 0 is {}, expected {}".format(asset["unreal_path"], material, MATERIAL_INSTANCE_PATH))
        expected = {
            "Aerathea.StaticMesh.MaterialMode": "shared_BC_N_ORM_texture_candidate_vertex_color_detail_multiplier",
            "Aerathea.StaticMesh.TextureSet": "{}_BC_N_ORM".format(TEXTURE_BASENAME),
            "Aerathea.StaticMesh.TextureMaterialStatus": "texture_material_candidate_pending_flamestrike_review",
            "Aerathea.StaticMesh.FinalTextureSetAuthored": "false_pending_flamestrike_review",
            "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_review",
            "Aerathea.StaticMesh.Status": "unreal_import_candidate",
        }
        for tag, value in expected.items():
            actual = metadata_value(mesh, tag)
            if actual != value:
                failures.append("{} metadata {} is {!r}, expected {!r}".format(asset["unreal_path"], tag, actual, value))


def main():
    failures = []
    validate_texture_sources(failures)
    validate_texture_assets(failures)
    validate_materials(failures)
    validate_mesh_materials_and_metadata(failures)

    if failures:
        for failure in failures:
            unreal.log_error(failure)
        raise RuntimeError("Blood Axe cairn variant texture/material validation failed with {} issue(s)".format(len(failures)))

    unreal.log(
        "Blood Axe cairn variant texture/material validation passed: {} textures in {}, shared one-slot material assigned to {} meshes.".format(
            len(TEXTURE_ASSET_PATHS),
            TEXTURE_DESTINATION,
            len(ASSETS),
        )
    )


if __name__ == "__main__":
    main()
