import json
from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]

ASSET_NAME = "SM_GIA_BloodAxeCairnstone_A002"
DCC_PACKAGE = "SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01"
DESTINATION = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns"
ASSET_PATH = "{}/{}".format(DESTINATION, ASSET_NAME)

SOURCE_DIR = ROOT / "SourceAssets/Exports/Props/Giants/BloodAxe/Cairns" / DCC_PACKAGE
SOURCE = SOURCE_DIR / "{}.fbx".format(DCC_PACKAGE)
LOD_SOURCES = {
    1: SOURCE_DIR / "{}_LOD1.fbx".format(DCC_PACKAGE),
    2: SOURCE_DIR / "{}_LOD2.fbx".format(DCC_PACKAGE),
    3: SOURCE_DIR / "{}_LOD3.fbx".format(DCC_PACKAGE),
}
UCX_SOURCE = SOURCE_DIR / "{}_UCX.fbx".format(DCC_PACKAGE)
DCC_MANIFEST = ROOT / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Manifest.json"
DCC_AUDIT = ROOT / "Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Audit.json"

SOURCE_TEXTURE = ROOT / "docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png"
TEXTURE_DESTINATION = "/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002"
TEXTURE_NAME = "T_GIA_BloodAxeCairnstone_A002_SourceTemplate_BC"
TEXTURE_PATH = "{}/{}".format(TEXTURE_DESTINATION, TEXTURE_NAME)

MATERIAL_PATH = "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
SOURCE_PARENT_NAME = "M_GIA_BloodAxeCairnstone_A002_SourceTemplate"
INFERRED_PARENT_NAME = "M_GIA_BloodAxeCairnstone_A002_InferredHidden"
SOURCE_INSTANCE_NAME = "MI_GIA_BloodAxeCairnstone_A002_SourceTemplate"
INFERRED_INSTANCE_NAME = "MI_GIA_BloodAxeCairnstone_A002_InferredHidden"

PHASE6_RECORD = "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_6C_DCC_GAME_READY_CANDIDATE_OUTPUT_RECORD.md"
PHASE7_PLAN = "docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_7A_UNREAL_IMPORT_CANDIDATE_PLAN.md"


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


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def relative_project_path(path):
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_dcc_sources():
    required_sources = [SOURCE, UCX_SOURCE, DCC_MANIFEST, DCC_AUDIT] + list(LOD_SOURCES.values())
    for source in required_sources:
        if not source.exists():
            raise RuntimeError("Missing Phase 7 source file: {}".format(source))
        if source.stat().st_size <= 0:
            raise RuntimeError("Phase 7 source file is empty: {}".format(source))

    audit = read_json(DCC_AUDIT)
    if audit.get("status") != "pass":
        raise RuntimeError("Phase 6C DCC audit is {}, expected pass".format(audit.get("status")))

    manifest = read_json(DCC_MANIFEST)
    proxies = manifest.get("collision_proxies") or []
    if not proxies:
        raise RuntimeError("DCC manifest has no collision proxy list")
    return len(proxies)


def connect_property(expression, output_name, property_name):
    prop = getattr(unreal.MaterialProperty, property_name, None)
    if prop is None:
        unreal.log_warning("MaterialProperty.{} unavailable; skipped connection.".format(property_name))
        return False
    try:
        return bool(unreal.MaterialEditingLibrary.connect_material_property(expression, output_name or "", prop))
    except Exception as exc:
        unreal.log_warning("Could not connect {} to {}: {}".format(type(expression).__name__, property_name, exc))
        return False


def clear_material_graph(material):
    expressions = []
    try:
        expressions = list(material.get_editor_property("expressions"))
    except Exception:
        pass
    for expression in expressions:
        try:
            unreal.MaterialEditingLibrary.delete_material_expression(material, expression)
        except Exception:
            pass


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


def import_source_texture():
    if not SOURCE_TEXTURE.exists():
        raise RuntimeError("Missing approved source texture {}".format(SOURCE_TEXTURE))
    ensure_directory(TEXTURE_DESTINATION)
    task = unreal.AssetImportTask()
    task.set_editor_property("filename", str(SOURCE_TEXTURE))
    task.set_editor_property("destination_path", TEXTURE_DESTINATION)
    task.set_editor_property("destination_name", TEXTURE_NAME)
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    texture = unreal.load_asset(TEXTURE_PATH)
    if texture is None:
        raise RuntimeError("Import did not produce expected source texture {}".format(TEXTURE_PATH))
    safe_set(texture, "srgb", True)
    unreal.EditorAssetLibrary.save_loaded_asset(texture)
    return texture


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


def build_source_material(texture):
    material = ensure_material(SOURCE_PARENT_NAME)
    sample = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionTextureSample, -420, -120)
    safe_set(sample, "texture", texture)
    connect_property(sample, "", "MP_BASE_COLOR")
    rough = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 80)
    safe_set(rough, "r", 0.92)
    connect_property(rough, "", "MP_ROUGHNESS")
    metal = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 210)
    safe_set(metal, "r", 0.0)
    connect_property(metal, "", "MP_METALLIC")
    configure_static_material(material)
    return material


def build_inferred_material():
    material = ensure_material(INFERRED_PARENT_NAME)
    color = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -420, -120)
    safe_set(color, "constant", unreal.LinearColor(0.24, 0.23, 0.22, 1.0))
    connect_property(color, "", "MP_BASE_COLOR")
    rough = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 80)
    safe_set(rough, "r", 0.96)
    connect_property(rough, "", "MP_ROUGHNESS")
    metal = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant, -420, 210)
    safe_set(metal, "r", 0.0)
    connect_property(metal, "", "MP_METALLIC")
    configure_static_material(material)
    return material


def ensure_material_instance(name, parent):
    ensure_directory(MATERIAL_INSTANCE_PATH)
    path = "{}/{}".format(MATERIAL_INSTANCE_PATH, name)
    instance = unreal.load_asset(path)
    if instance is None:
        instance = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=name,
            package_path=MATERIAL_INSTANCE_PATH,
            asset_class=unreal.MaterialInstanceConstant,
            factory=unreal.MaterialInstanceConstantFactoryNew(),
        )
    if instance is None:
        raise RuntimeError("Failed to create material instance {}".format(path))
    safe_set(instance, "parent", parent)
    unreal.EditorAssetLibrary.save_loaded_asset(instance)
    return instance


def import_static_mesh():
    ensure_directory(DESTINATION)

    fbx_ui = unreal.FbxImportUI()
    safe_set(fbx_ui, "import_mesh", True)
    safe_set(fbx_ui, "import_as_skeletal", False)
    safe_set(fbx_ui, "import_materials", False)
    safe_set(fbx_ui, "import_textures", False)
    safe_set(fbx_ui, "import_uniform_scale", 1.0)

    static_data = fbx_ui.static_mesh_import_data
    safe_set(static_data, "combine_meshes", True)
    safe_set(static_data, "auto_generate_collision", False)
    safe_set(static_data, "generate_lightmap_u_vs", True)
    safe_set(static_data, "remove_degenerates", True)
    safe_set(static_data, "one_convex_hull_per_ucx", False)
    safe_set(static_data, "import_uniform_scale", 1.0)

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
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return mesh


def import_authored_lods(mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    importer = getattr(subsystem, "import_lod", None) if subsystem is not None else None
    if not callable(importer):
        unreal.log_warning("StaticMeshEditorSubsystem.import_lod unavailable; generating editor LODs from LOD0")
        options = unreal.EditorScriptingMeshReductionOptions()
        safe_set(options, "auto_compute_lod_screen_size", False)
        settings = []
        for percent, screen_size in ((1.0, 1.0), (0.6, 0.55), (0.35, 0.28), (0.15, 0.12)):
            setting = unreal.EditorScriptingMeshReductionSettings()
            safe_set(setting, "percent_triangles", percent)
            safe_set(setting, "screen_size", screen_size)
            settings.append(setting)
        safe_set(options, "reduction_settings", settings)
        unreal.EditorStaticMeshLibrary.set_lods(mesh, options)
    else:
        for lod_index, lod_source in LOD_SOURCES.items():
            if not lod_source.exists():
                raise RuntimeError("Missing authored LOD{} source: {}".format(lod_index, lod_source))
            importer(mesh, lod_index, str(lod_source))
    if unreal.EditorStaticMeshLibrary.get_lod_count(mesh) < 4:
        raise RuntimeError("{} has fewer than 4 LODs after setup".format(ASSET_NAME))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def collision_box_shape():
    for enum_name in ("ScriptCollisionShapeType", "ScriptingCollisionShapeType", "ScriptingCollisionShapeType_DEPRECATED"):
        enum_type = getattr(unreal, enum_name, None)
        if enum_type is None:
            continue
        for value_name in ("BOX", "Box"):
            value = getattr(enum_type, value_name, None)
            if value is not None:
                return value
    return None


def collision_counts(mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        try:
            return int(subsystem.get_simple_collision_count(mesh)), int(subsystem.get_convex_collision_count(mesh))
        except Exception:
            pass
    counter = getattr(unreal.EditorStaticMeshLibrary, "get_simple_collision_count", None)
    if callable(counter):
        try:
            return int(counter(mesh)), 0
        except Exception:
            pass
    return 0, 0


def add_simple_collision(mesh, expected_proxy_count):
    remover = getattr(unreal.EditorStaticMeshLibrary, "remove_collisions", None)
    if callable(remover):
        try:
            remover(mesh)
        except Exception as exc:
            unreal.log_warning("Could not clear simple collision on {}: {}".format(ASSET_NAME, exc))
    shape = collision_box_shape()
    adder = getattr(unreal.EditorStaticMeshLibrary, "add_simple_collisions", None)
    if shape is None or not callable(adder):
        raise RuntimeError("Unreal Python simple collision API unavailable")
    result = adder(mesh, shape)
    if result is None or int(result) < 0:
        raise RuntimeError("Failed to add simple collision to {}".format(ASSET_NAME))
    simple_count, convex_count = collision_counts(mesh)
    if max(simple_count, convex_count) < 1:
        raise RuntimeError("Simple collision count is still zero after fallback on {}".format(ASSET_NAME))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    unreal.log(
        "{} collision fallback recorded from DCC UCX source: expected_proxy_count={} simple_count={} convex_count={}".format(
            ASSET_NAME,
            expected_proxy_count,
            simple_count,
            convex_count,
        )
    )
    return "generated_box_fallback_dcc_ucx_source_verified", simple_count, convex_count


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def assign_materials(mesh, source_instance, inferred_instance):
    slots = material_slots(mesh)
    for index, slot in enumerate(slots):
        slot_name = str(slot.get_editor_property("material_slot_name")).lower()
        if "inferred" in slot_name or "hidden" in slot_name:
            mesh.set_material(index, inferred_instance)
        else:
            mesh.set_material(index, source_instance)
    if not slots:
        unreal.log_warning("{} imported with no material slots".format(ASSET_NAME))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def apply_metadata(mesh, collision_source, simple_count, convex_count, expected_proxy_count):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag unavailable; skipped A002 metadata")
        return
    metadata = {
        "Aerathea.StaticMesh.Package": ASSET_NAME,
        "Aerathea.StaticMesh.Status": "unreal_import_candidate_pending_validation",
        "Aerathea.StaticMesh.SourceMethod": "A002 measured DCC game-ready candidate",
        "Aerathea.StaticMesh.DCCPackage": DCC_PACKAGE,
        "Aerathea.StaticMesh.DCCManifest": relative_project_path(DCC_MANIFEST),
        "Aerathea.StaticMesh.DCCAudit": relative_project_path(DCC_AUDIT),
        "Aerathea.StaticMesh.DCCAuditStatus": "pass",
        "Aerathea.StaticMesh.Phase6Record": PHASE6_RECORD,
        "Aerathea.StaticMesh.Phase7Plan": PHASE7_PLAN,
        "Aerathea.StaticMesh.CollisionPolicy": "broad_simple_static_prop_collision",
        "Aerathea.StaticMesh.CollisionImportSource": collision_source,
        "Aerathea.StaticMesh.CollisionSourceFBX": relative_project_path(UCX_SOURCE),
        "Aerathea.StaticMesh.CollisionFallbackRecorded": "true",
        "Aerathea.StaticMesh.ExpectedCollisionProxyCount": str(expected_proxy_count),
        "Aerathea.StaticMesh.ImportedSimpleCollisionCount": str(simple_count),
        "Aerathea.StaticMesh.ImportedConvexCollisionCount": str(convex_count),
        "Aerathea.StaticMesh.ComplexAsSimple": "false",
        "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
        "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_review",
        "Aerathea.StaticMesh.FullyGameReady": "false",
        "Aerathea.StaticMesh.A001A02SourceAuthority": "false",
    }
    for tag, value in metadata.items():
        setter(mesh, tag, value)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def main():
    expected_proxy_count = validate_dcc_sources()
    texture = import_source_texture()
    source_material = build_source_material(texture)
    inferred_material = build_inferred_material()
    source_instance = ensure_material_instance(SOURCE_INSTANCE_NAME, source_material)
    inferred_instance = ensure_material_instance(INFERRED_INSTANCE_NAME, inferred_material)
    mesh = import_static_mesh()
    import_authored_lods(mesh)
    collision_source, simple_count, convex_count = add_simple_collision(mesh, expected_proxy_count)
    assign_materials(mesh, source_instance, inferred_instance)
    apply_metadata(mesh, collision_source, simple_count, convex_count, expected_proxy_count)
    unreal.EditorAssetLibrary.save_directory(DESTINATION, only_if_is_dirty=True, recursive=True)
    unreal.EditorAssetLibrary.save_directory(TEXTURE_DESTINATION, only_if_is_dirty=True, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=True, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_INSTANCE_PATH, only_if_is_dirty=True, recursive=True)
    unreal.log("Imported {} as Unreal import candidate.".format(ASSET_NAME))


if __name__ == "__main__":
    main()
