from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]
DESTINATION = "/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp"
ASSET_NAME = "SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
ASSET_PATH = "{}/{}".format(DESTINATION, ASSET_NAME)
SOURCE = ROOT / "SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.fbx"
FBX_IMPORT_UNIFORM_SCALE = 0.01

MATERIAL_PATH = "/Game/Aerathea/Materials/Giants/BloodAxe"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
PARENT_MATERIAL_NAME = "M_GIA_BloodAxeMovedCampVertexColor_Blockout_A01"
MATERIAL_INSTANCE_NAME = "MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01"
MATERIAL_INSTANCE_ASSET_PATH = "{}/{}".format(MATERIAL_INSTANCE_PATH, MATERIAL_INSTANCE_NAME)

TASK_ID = "AET-MA-20260629-574"
PACKAGE_DOC = "docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PRODUCTION_PACKAGE.md"
DCC_STATUS_DOC = "docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/DCC_BUILD_STATUS.md"
IMPORT_PACKET_DOC = "docs/agents/AET-MA-20260629-574_UNREAL_IMPORT_TASK_PACKET.md"


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def connect_property(expression, property_name):
    prop = getattr(unreal.MaterialProperty, property_name, None)
    if prop is None:
        unreal.log_warning("MaterialProperty.{} unavailable; skipped connection.".format(property_name))
        return
    unreal.MaterialEditingLibrary.connect_material_property(expression, "", prop)


def connect_expression(output_expression, output_name, input_expression, input_name):
    try:
        unreal.MaterialEditingLibrary.connect_material_expressions(
            output_expression,
            output_name,
            input_expression,
            input_name,
        )
        return True
    except Exception as exc:
        unreal.log_warning(
            "Could not connect {} to {}.{}: {}".format(
                type(output_expression).__name__,
                type(input_expression).__name__,
                input_name,
                exc,
            )
        )
        return False


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


def ensure_vertex_color_material():
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, PARENT_MATERIAL_NAME)
    material = unreal.load_asset(asset_path)
    if material is None:
        material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=PARENT_MATERIAL_NAME,
            package_path=MATERIAL_PATH,
            asset_class=unreal.Material,
            factory=unreal.MaterialFactoryNew(),
        )
        if material is None:
            raise RuntimeError("Failed to create material {}".format(asset_path))

    mat_lib = unreal.MaterialEditingLibrary
    try:
        for expression in list(material.get_editor_property("expressions")):
            mat_lib.delete_material_expression(material, expression)
    except Exception:
        pass

    vertex_color_class = getattr(unreal, "MaterialExpressionVertexColor", None)
    if vertex_color_class is not None:
        base = mat_lib.create_material_expression(material, vertex_color_class, -420, -120)
    else:
        base = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -420, -120)
        safe_set(base, "constant", unreal.LinearColor(0.34, 0.32, 0.28, 1.0))
        unreal.log_warning("MaterialExpressionVertexColor unavailable; using constant Blood Axe blockout color")

    multiply_class = getattr(unreal, "MaterialExpressionMultiply", None)
    if multiply_class is not None:
        value_tint = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -420, 70)
        safe_set(value_tint, "constant", unreal.LinearColor(0.30, 0.32, 0.34, 1.0))
        value_control = mat_lib.create_material_expression(material, multiply_class, -130, -70)
        if connect_expression(base, "", value_control, "A") and connect_expression(value_tint, "", value_control, "B"):
            connect_property(value_control, "MP_BASE_COLOR")
        else:
            connect_property(base, "MP_BASE_COLOR")
    else:
        unreal.log_warning("MaterialExpressionMultiply unavailable; Blood Axe blockout material has no value multiplier")
        connect_property(base, "MP_BASE_COLOR")

    rough = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 90)
    safe_set(rough, "r", 0.88)
    connect_property(rough, "MP_ROUGHNESS")

    metal = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 220)
    safe_set(metal, "r", 0.0)
    connect_property(metal, "MP_METALLIC")

    configure_static_material(material)
    unreal.EditorAssetLibrary.save_asset(asset_path)
    return material


def ensure_material_instance(parent_material):
    ensure_directory(MATERIAL_INSTANCE_PATH)
    instance = unreal.load_asset(MATERIAL_INSTANCE_ASSET_PATH)
    if instance is None:
        instance = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=MATERIAL_INSTANCE_NAME,
            package_path=MATERIAL_INSTANCE_PATH,
            asset_class=unreal.MaterialInstanceConstant,
            factory=unreal.MaterialInstanceConstantFactoryNew(),
        )
        if instance is None:
            raise RuntimeError("Failed to create material instance {}".format(MATERIAL_INSTANCE_ASSET_PATH))
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
    vertex_option = getattr(unreal, "VertexColorImportOption", None)
    if vertex_option is not None and hasattr(vertex_option, "REPLACE"):
        safe_set(static_data, "vertex_color_import_option", vertex_option.REPLACE)

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


def assign_material(mesh, material_instance):
    slots = material_slots(mesh)
    if not slots:
        unreal.log_warning("{} has no static material slots after import".format(mesh.get_name()))
    for index, _slot in enumerate(slots):
        mesh.set_material(index, material_instance)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def ensure_review_lods_static(mesh, target_lods=4):
    options = unreal.EditorScriptingMeshReductionOptions()
    safe_set(options, "auto_compute_lod_screen_size", False)
    settings = []
    for percent, screen_size in ((1.0, 1.0), (0.58, 0.55), (0.32, 0.28), (0.14, 0.12)):
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


def remove_simple_collision(mesh):
    remover = getattr(unreal.EditorStaticMeshLibrary, "remove_collisions", None)
    if callable(remover):
        try:
            remover(mesh)
        except Exception as exc:
            unreal.log_warning("Could not remove collisions from {}: {}".format(mesh.get_name(), exc))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def apply_mesh_metadata(mesh):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag is unavailable; skipped Blood Axe metadata")
        return
    metadata = {
        "Aerathea.StaticMesh.Package": ASSET_NAME,
        "Aerathea.StaticMesh.Task": TASK_ID,
        "Aerathea.StaticMesh.Status": "material_value_pass_review_target",
        "Aerathea.StaticMesh.PackageDoc": PACKAGE_DOC,
        "Aerathea.StaticMesh.DCCStatusDoc": DCC_STATUS_DOC,
        "Aerathea.StaticMesh.ImportPacket": IMPORT_PACKET_DOC,
        "Aerathea.StaticMesh.StartupPlaced": "startup_review_actor",
        "Aerathea.StaticMesh.StartupActor": "AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01",
        "Aerathea.StaticMesh.VisualReview": "requested_changes_material_value_pass_pending_approval_not_final_art",
        "Aerathea.StaticMesh.FinalArtAuthored": "false",
        "Aerathea.StaticMesh.CollisionPolicy": "disabled_no_correctness_claim",
        "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
        "Aerathea.StaticMesh.VertexColorMaterial": "true",
        "Aerathea.StaticMesh.MaterialValueRevision": "AET-MA-20260629-583_requested_changes",
        "Aerathea.StaticMesh.MaterialValueControl": "standard_color_channel_vertex_material_multiplier_v03",
    }
    for tag, value in metadata.items():
        setter(mesh, tag, str(value))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def main():
    parent_material = ensure_vertex_color_material()
    material_instance = ensure_material_instance(parent_material)
    mesh = import_static_mesh()
    assign_material(mesh, material_instance)
    ensure_review_lods_static(mesh)
    remove_simple_collision(mesh)
    apply_mesh_metadata(mesh)
    unreal.EditorAssetLibrary.save_directory(DESTINATION, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_INSTANCE_PATH, only_if_is_dirty=False, recursive=True)
    unreal.log("Aerathea Blood Axe moved-camp low cairn remnant import complete.")


main()
