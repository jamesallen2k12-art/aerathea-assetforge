from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual"
DESTINATION = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns"
ASSET_PATH = "{}/{}".format(DESTINATION, ASSET_NAME)
SOURCE = ROOT / "SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual.fbx"
FBX_IMPORT_UNIFORM_SCALE = 0.01

TEXTURE_SOURCE_DIR = ROOT / "SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual"
TEXTURE_DESTINATION = "/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual"
TEXTURE_SOURCES = {
    "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_BC": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_BC.png",
    "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_N": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_N.png",
    "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_ORM": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_ORM.png",
}

MATERIAL_PATH = "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
PROJECTION_MATERIAL_NAME = "M_GIA_BloodAxeCairn_Test2ManualProjection_A01"
SIDE_MATERIAL_NAME = "M_GIA_BloodAxeCairn_Test2ManualSideStone_A01"
PROJECTION_MI_NAME = "MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_Projection"
SIDE_MI_NAME = "MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_SideStone"
PROJECTION_MI_PATH = "{}/{}".format(MATERIAL_INSTANCE_PATH, PROJECTION_MI_NAME)
SIDE_MI_PATH = "{}/{}".format(MATERIAL_INSTANCE_PATH, SIDE_MI_NAME)

PACKAGE_DOC = "docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/TEST2_MANUAL_ASSET_STATUS.md"


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
        return True
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))
        return False


def material_property(property_name):
    return getattr(unreal.MaterialProperty, property_name, None)


def connect_property(expression, output_name, property_name):
    prop = material_property(property_name)
    if prop is None:
        unreal.log_warning("MaterialProperty.{} is unavailable; skipped connection.".format(property_name))
        return False
    output_name = output_name or ""
    try:
        connected = unreal.MaterialEditingLibrary.connect_material_property(expression, output_name, prop)
    except Exception as exc:
        unreal.log_warning(
            "Could not connect {} output {} to {}: {}".format(
                type(expression).__name__,
                output_name,
                property_name,
                exc,
            )
        )
        return False
    if not connected:
        unreal.log_warning(
            "Material connection failed for {} output {} to {}".format(
                type(expression).__name__,
                output_name,
                property_name,
            )
        )
    return bool(connected)


def connect_expression(output_expression, output_name, input_expression, input_name):
    output_name = output_name or ""
    try:
        connected = unreal.MaterialEditingLibrary.connect_material_expressions(
            output_expression,
            output_name,
            input_expression,
            input_name,
        )
    except Exception as exc:
        unreal.log_warning(
            "Could not connect {} output {} to {} input {}: {}".format(
                type(output_expression).__name__,
                output_name,
                type(input_expression).__name__,
                input_name,
                exc,
            )
        )
        return False
    if not connected:
        unreal.log_warning(
            "Material expression connection failed for {} output {} to {} input {}".format(
                type(output_expression).__name__,
                output_name,
                type(input_expression).__name__,
                input_name,
            )
        )
    return bool(connected)


def connect_first_property(expression, output_names, property_name):
    for output_name in output_names:
        if connect_property(expression, output_name, property_name):
            return True
    raise RuntimeError(
        "Could not connect {} to {} using outputs {}".format(
            type(expression).__name__,
            property_name,
            ", ".join(output_names),
        )
    )


def clear_material_graph(material):
    try:
        for expression in list(material.get_editor_property("expressions")):
            unreal.MaterialEditingLibrary.delete_material_expression(material, expression)
    except Exception as exc:
        unreal.log_warning("Could not clear material graph for {}: {}".format(material.get_name(), exc))


def configure_static_material(material):
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


def create_constant(material, value, x, y):
    expression = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionConstant,
        x,
        y,
    )
    safe_set(expression, "r", float(value))
    return expression


def create_color_constant(material, color, x, y):
    expression = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionConstant3Vector,
        x,
        y,
    )
    safe_set(expression, "constant", color)
    return expression


def create_texture_sample(material, texture, x, y, sampler_type_name=None):
    expression = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionTextureSample,
        x,
        y,
    )
    safe_set(expression, "texture", texture)
    if sampler_type_name:
        sampler_type = getattr(unreal.MaterialSamplerType, sampler_type_name, None)
        if sampler_type is not None:
            safe_set(expression, "sampler_type", sampler_type)
    return expression


def import_texture(asset_name, source_path, srgb, compression_name=None):
    if not source_path.exists():
        raise RuntimeError("Missing source texture {}".format(source_path))
    ensure_directory(TEXTURE_DESTINATION)

    task = unreal.AssetImportTask()
    task.set_editor_property("filename", str(source_path))
    task.set_editor_property("destination_path", TEXTURE_DESTINATION)
    task.set_editor_property("destination_name", asset_name)
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    texture_path = "{}/{}".format(TEXTURE_DESTINATION, asset_name)
    texture = unreal.load_asset(texture_path)
    if texture is None:
        raise RuntimeError("Import did not produce expected texture {}".format(texture_path))

    safe_set(texture, "srgb", bool(srgb))
    if compression_name:
        compression = getattr(unreal.TextureCompressionSettings, compression_name, None)
        if compression is not None:
            safe_set(texture, "compression_settings", compression)
    unreal.EditorAssetLibrary.save_loaded_asset(texture)
    return texture


def import_textures():
    return {
        "bc": import_texture(
            "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_BC",
            TEXTURE_SOURCES["T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_BC"],
            True,
        ),
        "normal": import_texture(
            "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_N",
            TEXTURE_SOURCES["T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_N"],
            False,
            "TC_NORMALMAP",
        ),
        "orm": import_texture(
            "T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_ORM",
            TEXTURE_SOURCES["T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_ORM"],
            False,
            "TC_MASKS",
        ),
    }


def ensure_material(asset_name):
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, asset_name)
    material = unreal.load_asset(asset_path)
    if material is None:
        material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=asset_name,
            package_path=MATERIAL_PATH,
            asset_class=unreal.Material,
            factory=unreal.MaterialFactoryNew(),
        )
        if material is None:
            raise RuntimeError("Failed to create material {}".format(asset_path))
    clear_material_graph(material)
    return material


def ensure_projection_material(textures):
    material = ensure_material(PROJECTION_MATERIAL_NAME)
    blend_mode = getattr(unreal.BlendMode, "BLEND_MASKED", None)
    if blend_mode is not None:
        safe_set(material, "blend_mode", blend_mode)
    safe_set(material, "opacity_mask_clip_value", 0.08)
    safe_set(material, "two_sided", True)

    bc = create_texture_sample(material, textures["bc"], -920, -300, "SAMPLERTYPE_COLOR")
    normal = create_texture_sample(material, textures["normal"], -920, -20, "SAMPLERTYPE_NORMAL")
    orm = create_texture_sample(material, textures["orm"], -920, 260, "SAMPLERTYPE_MASKS")

    connect_first_property(bc, ("RGB", "RGBA", ""), "MP_BASE_COLOR")
    connect_first_property(bc, ("A", "Alpha"), "MP_OPACITY_MASK")
    connect_first_property(normal, ("RGB", "RGBA", ""), "MP_NORMAL")
    connect_first_property(orm, ("R",), "MP_AMBIENT_OCCLUSION")
    connect_first_property(orm, ("G",), "MP_ROUGHNESS")
    connect_first_property(orm, ("B",), "MP_METALLIC")
    configure_static_material(material)
    unreal.EditorAssetLibrary.save_asset("{}/{}".format(MATERIAL_PATH, PROJECTION_MATERIAL_NAME))
    return material


def ensure_side_material():
    material = ensure_material(SIDE_MATERIAL_NAME)
    blend_mode = getattr(unreal.BlendMode, "BLEND_OPAQUE", None)
    if blend_mode is not None:
        safe_set(material, "blend_mode", blend_mode)
    safe_set(material, "two_sided", False)

    base = create_color_constant(material, unreal.LinearColor(0.29, 0.27, 0.23, 1.0), -520, -110)
    rough = create_constant(material, 0.95, -520, 90)
    metal = create_constant(material, 0.0, -520, 240)
    connect_property(base, "", "MP_BASE_COLOR")
    connect_property(rough, "", "MP_ROUGHNESS")
    connect_property(metal, "", "MP_METALLIC")
    configure_static_material(material)
    unreal.EditorAssetLibrary.save_asset("{}/{}".format(MATERIAL_PATH, SIDE_MATERIAL_NAME))
    return material


def ensure_material_instance(name, parent_material):
    ensure_directory(MATERIAL_INSTANCE_PATH)
    asset_path = "{}/{}".format(MATERIAL_INSTANCE_PATH, name)
    instance = unreal.load_asset(asset_path)
    if instance is None:
        instance = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=name,
            package_path=MATERIAL_INSTANCE_PATH,
            asset_class=unreal.MaterialInstanceConstant,
            factory=unreal.MaterialInstanceConstantFactoryNew(),
        )
        if instance is None:
            raise RuntimeError("Failed to create material instance {}".format(asset_path))
    safe_set(instance, "parent", parent_material)
    unreal.EditorAssetLibrary.save_loaded_asset(instance)
    return instance


def import_static_mesh():
    if not SOURCE.exists():
        raise RuntimeError("Missing source FBX: {}".format(SOURCE))
    ensure_directory(DESTINATION)

    fbx_ui = unreal.FbxImportUI()
    safe_set(fbx_ui, "import_mesh", True)
    safe_set(fbx_ui, "import_as_skeletal", False)
    safe_set(fbx_ui, "import_materials", False)
    safe_set(fbx_ui, "import_textures", False)
    safe_set(fbx_ui, "import_uniform_scale", FBX_IMPORT_UNIFORM_SCALE)

    static_data = fbx_ui.static_mesh_import_data
    safe_set(static_data, "combine_meshes", True)
    safe_set(static_data, "auto_generate_collision", False)
    safe_set(static_data, "generate_lightmap_u_vs", True)
    safe_set(static_data, "remove_degenerates", True)
    safe_set(static_data, "one_convex_hull_per_ucx", False)
    safe_set(static_data, "import_uniform_scale", FBX_IMPORT_UNIFORM_SCALE)

    task = unreal.AssetImportTask()
    task.set_editor_property("filename", str(SOURCE))
    task.set_editor_property("destination_path", DESTINATION)
    task.set_editor_property("destination_name", ASSET_NAME)
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)
    task.set_editor_property("options", fbx_ui)

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    mesh = unreal.load_asset(ASSET_PATH)
    if mesh is None:
        raise RuntimeError("Import did not produce expected static mesh: {}".format(ASSET_PATH))
    safe_set(mesh, "light_map_resolution", 128)
    unreal.EditorAssetLibrary.save_asset(ASSET_PATH)
    return mesh


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def assign_project_materials(mesh, projection_instance, side_instance):
    slots = material_slots(mesh)
    if len(slots) < 2:
        unreal.log_warning("{} imported with {} material slots; expected 2.".format(mesh.get_name(), len(slots)))
    for index, slot in enumerate(slots):
        slot_name = str(slot.get_editor_property("material_slot_name"))
        lower_name = slot_name.lower()
        if index == 0 and "side" not in lower_name:
            mesh.set_material(index, projection_instance)
        elif "side" in lower_name or index > 0:
            mesh.set_material(index, side_instance)
        else:
            mesh.set_material(index, projection_instance)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def ensure_review_lods_static(mesh, target_lods=4):
    options = unreal.EditorScriptingMeshReductionOptions()
    safe_set(options, "auto_compute_lod_screen_size", False)
    settings = []
    for percent, screen_size in ((1.0, 1.0), (0.70, 0.55), (0.42, 0.28), (0.22, 0.12)):
        setting = unreal.EditorScriptingMeshReductionSettings()
        safe_set(setting, "percent_triangles", percent)
        safe_set(setting, "screen_size", screen_size)
        settings.append(setting)
    safe_set(options, "reduction_settings", settings)
    unreal.EditorStaticMeshLibrary.set_lods(mesh, options)
    count = unreal.EditorStaticMeshLibrary.get_lod_count(mesh)
    if count < target_lods:
        raise RuntimeError("{} has {} static LODs after reduction, expected {}".format(mesh.get_name(), count, target_lods))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def collision_box_shape():
    enum_candidates = (
        "ScriptCollisionShapeType",
        "ScriptingCollisionShapeType",
        "ScriptingCollisionShapeType_Deprecated",
        "ScriptingCollisionShapeType_DEPRECATED",
    )
    value_candidates = ("BOX", "Box")
    for enum_name in enum_candidates:
        enum_type = getattr(unreal, enum_name, None)
        if enum_type is None:
            continue
        for value_name in value_candidates:
            value = getattr(enum_type, value_name, None)
            if value is not None:
                return value
    return None


def add_broad_simple_collision(mesh):
    remover = getattr(unreal.EditorStaticMeshLibrary, "remove_collisions", None)
    if callable(remover):
        try:
            remover(mesh)
        except Exception as exc:
            unreal.log_warning("Could not clear simple collision on {}: {}".format(mesh.get_name(), exc))

    box_shape = collision_box_shape()
    if box_shape is None:
        raise RuntimeError("Unreal Python collision shape enum is unavailable; cannot add simple box collision")

    collision_index = None
    adder = getattr(unreal.EditorStaticMeshLibrary, "add_simple_collisions", None)
    if callable(adder):
        collision_index = adder(mesh, box_shape)
    else:
        subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
        subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
        subsystem_adder = getattr(subsystem, "add_simple_collisions", None) if subsystem is not None else None
        if callable(subsystem_adder):
            collision_index = subsystem_adder(mesh, box_shape)

    if collision_index is None or int(collision_index) < 0:
        raise RuntimeError("Failed to add simple box collision to {}".format(mesh.get_name()))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def apply_mesh_metadata(mesh):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag is unavailable; skipped test2-manual metadata")
        return
    metadata = {
        "Aerathea.StaticMesh.Package": ASSET_NAME,
        "Aerathea.StaticMesh.Status": "unreal_game_ready_test2_manual_paint01_pending_flamestrike_reapproval",
        "Aerathea.StaticMesh.PackageDoc": PACKAGE_DOC,
        "Aerathea.StaticMesh.DCCStatusDoc": PACKAGE_DOC,
        "Aerathea.StaticMesh.SourceMethod": "front_faithful_deep_a01_image_relief_with_inferred_walkaround_depth",
        "Aerathea.StaticMesh.VisualCanonSource": "VC_GIA_BloodAxe_CairnStones_A01_A1_Crop",
        "Aerathea.StaticMesh.TextureProjection": "paint01_regraded_a01_projection_with_authored_albedo_ao_normal",
        "Aerathea.StaticMesh.CollisionPolicy": "broad_ucx_proxy_static_prop",
        "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
        "Aerathea.StaticMesh.FinalArtAuthored": "true",
        "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_reapproval_after_in_game_color_feedback",
        "Aerathea.StaticMesh.ApprovedPass": "A01-Test2-Paint-01",
    }
    for tag, value in metadata.items():
        setter(mesh, tag, str(value))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def main():
    textures = import_textures()
    projection_parent = ensure_projection_material(textures)
    side_parent = ensure_side_material()
    projection_instance = ensure_material_instance(PROJECTION_MI_NAME, projection_parent)
    side_instance = ensure_material_instance(SIDE_MI_NAME, side_parent)

    mesh = import_static_mesh()
    assign_project_materials(mesh, projection_instance, side_instance)
    ensure_review_lods_static(mesh)
    add_broad_simple_collision(mesh)
    apply_mesh_metadata(mesh)

    unreal.EditorAssetLibrary.save_directory(DESTINATION, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(TEXTURE_DESTINATION, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_INSTANCE_PATH, only_if_is_dirty=False, recursive=True)
    unreal.log("Aerathea Blood Axe test2-manual cairn import complete: {}".format(ASSET_PATH))


if __name__ == "__main__":
    main()
