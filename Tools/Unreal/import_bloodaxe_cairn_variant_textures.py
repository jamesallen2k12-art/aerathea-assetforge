from pathlib import Path
import sys

import unreal


sys.path.append(str(Path(__file__).resolve().parent))
from bloodaxe_cairn_variant_batch_config import (  # noqa: E402
    ASSETS,
    KIT_ID,
    MATERIAL_INSTANCE_PATH,
    PARENT_MATERIAL_PATH,
)


ROOT = Path(__file__).resolve().parents[2]
TEXTURE_SOURCE_DIR = (
    ROOT
    / "SourceAssets"
    / "Textures"
    / "Props"
    / "Giants"
    / "BloodAxe"
    / "Cairns"
    / "KIT_GIA_BloodAxeCairnVariantBatch_A01"
)
TEXTURE_DESTINATION = "/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/KIT_GIA_BloodAxeCairnVariantBatch_A01"
TEXTURE_BASENAME = "T_GIA_BloodAxeCairnVariants_A01"
TEXTURE_SOURCES = {
    "bc": TEXTURE_SOURCE_DIR / "{}_BC.png".format(TEXTURE_BASENAME),
    "normal": TEXTURE_SOURCE_DIR / "{}_N.png".format(TEXTURE_BASENAME),
    "orm": TEXTURE_SOURCE_DIR / "{}_ORM.png".format(TEXTURE_BASENAME),
}
TEXTURE_ASSET_PATHS = {
    key: "{}/{}".format(TEXTURE_DESTINATION, source.stem)
    for key, source in TEXTURE_SOURCES.items()
}


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def asset_dir(asset_path):
    return asset_path.rsplit("/", 1)[0]


def asset_name(asset_path):
    return asset_path.rsplit("/", 1)[1]


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
        return True
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))
        return False


def clear_material_graph(material):
    expressions = []
    getter = getattr(unreal.MaterialEditingLibrary, "get_material_expressions", None)
    try:
        if callable(getter):
            expressions = list(getter(material))
        else:
            expressions = list(material.get_editor_property("expressions"))
    except Exception as exc:
        unreal.log_warning("Could not read material graph for {}: {}".format(material.get_name(), exc))
    for expression in expressions:
        try:
            unreal.MaterialEditingLibrary.delete_material_expression(material, expression)
        except Exception as exc:
            unreal.log_warning("Could not delete {} from {}: {}".format(type(expression).__name__, material.get_name(), exc))


def configure_static_material(material):
    safe_set(material, "two_sided", False)
    safe_set(material, "used_with_static_mesh", True)
    safe_set(material, "used_with_static_lighting", True)
    usage = getattr(unreal.MaterialUsage, "MATUSAGE_STATIC_MESH", None)
    if usage is not None:
        try:
            unreal.MaterialEditingLibrary.set_material_usage(material, usage)
        except Exception as exc:
            unreal.log_warning("Could not set static mesh usage on {}: {}".format(material.get_name(), exc))
    unreal.MaterialEditingLibrary.recompile_material(material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)


def create_texture_sample(material, texture, x, y, sampler_type_name):
    expression = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionTextureSample,
        x,
        y,
    )
    safe_set(expression, "texture", texture)
    sampler_type = getattr(unreal.MaterialSamplerType, sampler_type_name, None)
    if sampler_type is not None:
        safe_set(expression, "sampler_type", sampler_type)
    return expression


def create_scalar_parameter(material, name, default_value, x, y):
    expression = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionScalarParameter,
        x,
        y,
    )
    safe_set(expression, "parameter_name", unreal.Name(name))
    safe_set(expression, "default_value", float(default_value))
    return expression


def create_vector_parameter(material, name, color, x, y):
    expression = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionVectorParameter,
        x,
        y,
    )
    safe_set(expression, "parameter_name", unreal.Name(name))
    safe_set(expression, "default_value", color)
    return expression


def create_multiply(material, x, y):
    multiply_class = getattr(unreal, "MaterialExpressionMultiply", None)
    if multiply_class is None:
        raise RuntimeError("MaterialExpressionMultiply is unavailable")
    return unreal.MaterialEditingLibrary.create_material_expression(material, multiply_class, x, y)


def connect_expression(output_expression, output_names, input_expression, input_name):
    for output_name in output_names:
        try:
            unreal.MaterialEditingLibrary.connect_material_expressions(
                output_expression,
                output_name,
                input_expression,
                input_name,
            )
            return True
        except Exception:
            continue
    unreal.log_warning(
        "Could not connect {} outputs {} to {}.{}".format(
            type(output_expression).__name__,
            output_names,
            type(input_expression).__name__,
            input_name,
        )
    )
    return False


def connect_property(expression, output_names, property_name):
    prop = getattr(unreal.MaterialProperty, property_name, None)
    if prop is None:
        unreal.log_warning("MaterialProperty.{} unavailable; skipped connection.".format(property_name))
        return False
    for output_name in output_names:
        try:
            unreal.MaterialEditingLibrary.connect_material_property(expression, output_name, prop)
            return True
        except Exception:
            continue
    unreal.log_warning("Could not connect {} outputs {} to {}".format(type(expression).__name__, output_names, property_name))
    return False


def import_texture(name, source_path, srgb, compression_name=None):
    if not source_path.exists():
        raise RuntimeError("Missing texture source {}".format(source_path))
    ensure_directory(TEXTURE_DESTINATION)
    task = unreal.AssetImportTask()
    task.set_editor_property("filename", str(source_path))
    task.set_editor_property("destination_path", TEXTURE_DESTINATION)
    task.set_editor_property("destination_name", name)
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    texture = unreal.load_asset("{}/{}".format(TEXTURE_DESTINATION, name))
    if texture is None:
        raise RuntimeError("Import did not produce expected texture {}".format(name))
    safe_set(texture, "srgb", bool(srgb))
    if compression_name:
        compression = getattr(unreal.TextureCompressionSettings, compression_name, None)
        if compression is not None:
            safe_set(texture, "compression_settings", compression)
    unreal.EditorAssetLibrary.save_loaded_asset(texture)
    return texture


def import_textures():
    return {
        "bc": import_texture(TEXTURE_SOURCES["bc"].stem, TEXTURE_SOURCES["bc"], True),
        "normal": import_texture(TEXTURE_SOURCES["normal"].stem, TEXTURE_SOURCES["normal"], False, "TC_NORMALMAP"),
        "orm": import_texture(TEXTURE_SOURCES["orm"].stem, TEXTURE_SOURCES["orm"], False, "TC_MASKS"),
    }


def ensure_textured_parent_material(textures):
    ensure_directory(asset_dir(PARENT_MATERIAL_PATH))
    material = unreal.load_asset(PARENT_MATERIAL_PATH)
    if material is None:
        material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=asset_name(PARENT_MATERIAL_PATH),
            package_path=asset_dir(PARENT_MATERIAL_PATH),
            asset_class=unreal.Material,
            factory=unreal.MaterialFactoryNew(),
        )
        if material is None:
            raise RuntimeError("Failed to create material {}".format(PARENT_MATERIAL_PATH))

    clear_material_graph(material)
    blend_mode = getattr(unreal.BlendMode, "BLEND_OPAQUE", None)
    if blend_mode is not None:
        safe_set(material, "blend_mode", blend_mode)

    mat_lib = unreal.MaterialEditingLibrary
    vertex_color_class = getattr(unreal, "MaterialExpressionVertexColor", None)
    if vertex_color_class is not None:
        vertex_color = mat_lib.create_material_expression(material, vertex_color_class, -900, -170)
    else:
        vertex_color = create_vector_parameter(material, "FallbackColor", unreal.LinearColor(0.22, 0.20, 0.17, 1.0), -900, -170)
        unreal.log_warning("MaterialExpressionVertexColor unavailable; using fallback constant color")

    tint = create_vector_parameter(material, "ValueTint", unreal.LinearColor(0.86, 0.80, 0.68, 1.0), -900, 20)
    bc = create_texture_sample(material, textures["bc"], -900, -420, "SAMPLERTYPE_COLOR")
    vertex_tinted = create_multiply(material, -590, -210)
    textured_base = create_multiply(material, -330, -300)
    connect_expression(vertex_color, ("", "RGB"), vertex_tinted, "A")
    connect_expression(tint, ("", "RGB"), vertex_tinted, "B")
    connect_expression(vertex_tinted, ("", "RGB"), textured_base, "A")
    connect_expression(bc, ("RGB", ""), textured_base, "B")
    connect_property(textured_base, ("", "RGB"), "MP_BASE_COLOR")

    normal = create_texture_sample(material, textures["normal"], -900, -10, "SAMPLERTYPE_NORMAL")
    connect_property(normal, ("RGB", ""), "MP_NORMAL")

    orm = create_texture_sample(material, textures["orm"], -900, 270, "SAMPLERTYPE_MASKS")
    connect_property(orm, ("R",), "MP_AMBIENT_OCCLUSION")
    connect_property(orm, ("G",), "MP_ROUGHNESS")
    connect_property(orm, ("B",), "MP_METALLIC")

    configure_static_material(material)
    unreal.EditorAssetLibrary.save_asset(PARENT_MATERIAL_PATH)
    return material


def ensure_material_instance(parent_material):
    ensure_directory(asset_dir(MATERIAL_INSTANCE_PATH))
    instance = unreal.load_asset(MATERIAL_INSTANCE_PATH)
    if instance is None:
        instance = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=asset_name(MATERIAL_INSTANCE_PATH),
            package_path=asset_dir(MATERIAL_INSTANCE_PATH),
            asset_class=unreal.MaterialInstanceConstant,
            factory=unreal.MaterialInstanceConstantFactoryNew(),
        )
        if instance is None:
            raise RuntimeError("Failed to create material instance {}".format(MATERIAL_INSTANCE_PATH))
    safe_set(instance, "parent", parent_material)
    mat_lib = unreal.MaterialEditingLibrary
    mat_lib.set_material_instance_vector_parameter_value(instance, "ValueTint", unreal.LinearColor(0.86, 0.80, 0.68, 1.0))
    unreal.EditorAssetLibrary.save_loaded_asset(instance)
    return instance


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def set_metadata(mesh, tag, value):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if callable(setter):
        setter(mesh, tag, str(value))


def assign_material_and_metadata(material_instance):
    for asset in ASSETS:
        mesh = unreal.load_asset(asset["unreal_path"])
        if mesh is None:
            raise RuntimeError("Missing imported mesh {}".format(asset["unreal_path"]))
        mesh.set_material(0, material_instance)
        set_metadata(mesh, "Aerathea.StaticMesh.MaterialMode", "shared_BC_N_ORM_texture_candidate_vertex_color_detail_multiplier")
        set_metadata(mesh, "Aerathea.StaticMesh.TextureSet", "{}_BC_N_ORM".format(TEXTURE_BASENAME))
        set_metadata(mesh, "Aerathea.StaticMesh.TextureMaterialStatus", "texture_material_candidate_pending_flamestrike_review")
        set_metadata(mesh, "Aerathea.StaticMesh.FinalTextureSetAuthored", "false_pending_flamestrike_review")
        set_metadata(mesh, "Aerathea.StaticMesh.FinalVisualApproval", "pending_flamestrike_review")
        set_metadata(mesh, "Aerathea.StaticMesh.Status", "unreal_import_candidate")
        unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def main():
    textures = import_textures()
    parent = ensure_textured_parent_material(textures)
    instance = ensure_material_instance(parent)
    assign_material_and_metadata(instance)

    unreal.EditorAssetLibrary.save_directory(TEXTURE_DESTINATION, only_if_is_dirty=False, recursive=True)
    for asset in ASSETS:
        unreal.EditorAssetLibrary.save_directory(asset["unreal_path"].rsplit("/", 1)[0], only_if_is_dirty=True, recursive=True)
    unreal.log("Imported shared Blood Axe cairn variant texture/material candidate for {} meshes in {}.".format(len(ASSETS), KIT_ID))


if __name__ == "__main__":
    main()
