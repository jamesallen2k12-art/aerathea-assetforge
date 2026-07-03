from pathlib import Path

import unreal


ROOT = Path(__file__).resolve().parents[2]

ASSET_NAME = "SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial"
DESTINATION = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns"
ASSET_PATH = "{}/{}".format(DESTINATION, ASSET_NAME)
SOURCE = ROOT / "SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial.fbx"
FBX_IMPORT_UNIFORM_SCALE = 0.01

TEXTURE_SOURCE_DIR = ROOT / "SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial"
TEXTURE_DESTINATION = "/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial"
MATERIAL_PATH = "/Game/Aerathea/Materials/Giants/BloodAxe/Cairns"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
PACKAGE_DOC = "docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/FINAL_TRIAL_ASSET_STATUS.md"

MATERIAL_SPECS = {
    "projection": {
        "parent": "M_GIA_BloodAxeCairn_FinalTrial_A1Projection_A01",
        "instance": "MI_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_A1Projection",
        "slot_terms": ("projection", "a1projection", "a1"),
        "bc": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_A1Projection_BC.png",
        "n": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_A1Projection_N.png",
        "orm": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_A1Projection_ORM.png",
        "roughness": 0.88,
        "color": unreal.LinearColor(0.96, 0.94, 0.86, 1.0),
        "metallic": 0.0,
    },
    "stone": {
        "parent": "M_GIA_BloodAxeCairn_FinalTrial_Stone_A01",
        "instance": "MI_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_Stone",
        "slot_terms": ("stone", "slab", "highlight", "crack"),
        "bc": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_Stone_BC.png",
        "n": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_Stone_N.png",
        "orm": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_Stone_ORM.png",
        "roughness": 0.9,
        "color": unreal.LinearColor(0.92, 0.88, 0.74, 1.0),
        "metallic": 0.0,
    },
    "dark_stone": {
        "parent": "M_GIA_BloodAxeCairn_FinalTrial_DarkStone_A01",
        "instance": "MI_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_DarkStone",
        "slot_terms": ("darkstone", "dark_stone"),
        "bc": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_DarkStone_BC.png",
        "n": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_DarkStone_N.png",
        "orm": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_DarkStone_ORM.png",
        "roughness": 0.93,
        "color": unreal.LinearColor(0.78, 0.74, 0.62, 1.0),
        "metallic": 0.0,
    },
    "earth": {
        "parent": "M_GIA_BloodAxeCairn_FinalTrial_EarthAsh_A01",
        "instance": "MI_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_EarthAsh",
        "slot_terms": ("earth", "ash", "mud", "ground"),
        "bc": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_EarthAsh_BC.png",
        "n": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_EarthAsh_N.png",
        "orm": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_EarthAsh_ORM.png",
        "roughness": 0.94,
        "color": unreal.LinearColor(0.82, 0.64, 0.48, 1.0),
        "metallic": 0.0,
    },
    "rawhide": {
        "parent": "M_GIA_BloodAxeCairn_FinalTrial_Rawhide_A01",
        "instance": "MI_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_Rawhide",
        "slot_terms": ("rawhide", "binding", "lashing"),
        "bc": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_Rawhide_BC.png",
        "n": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_Rawhide_N.png",
        "orm": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_Rawhide_ORM.png",
        "roughness": 0.84,
        "color": unreal.LinearColor(0.92, 0.78, 0.54, 1.0),
        "metallic": 0.0,
    },
    "red": {
        "parent": "M_GIA_BloodAxeCairn_FinalTrial_BloodAxeRedPaint_A01",
        "instance": "MI_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_BloodAxeRedPaint",
        "slot_terms": ("red", "paint", "bloodaxe"),
        "bc": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_BloodAxeRedPaint_BC.png",
        "n": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_BloodAxeRedPaint_N.png",
        "orm": TEXTURE_SOURCE_DIR / "T_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_BloodAxeRedPaint_ORM.png",
        "roughness": 0.82,
        "color": unreal.LinearColor(1.00, 0.30, 0.24, 1.0),
        "metallic": 0.0,
    },
}


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
    try:
        connected = unreal.MaterialEditingLibrary.connect_material_property(expression, output_name or "", prop)
    except Exception as exc:
        unreal.log_warning("Could not connect {} to {}: {}".format(type(expression).__name__, property_name, exc))
        return False
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
    raise RuntimeError("Could not connect {} to {}".format(type(expression).__name__, property_name))


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


def create_constant(material, value, x, y):
    expression = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionConstant,
        x,
        y,
    )
    safe_set(expression, "r", float(value))
    return expression


def create_vector_parameter(material, name, value, x, y):
    expression = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionVectorParameter,
        x,
        y,
    )
    safe_set(expression, "parameter_name", unreal.Name(name))
    safe_set(expression, "default_value", value)
    return expression


def create_scalar_parameter(material, name, value, x, y):
    expression = unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionScalarParameter,
        x,
        y,
    )
    safe_set(expression, "parameter_name", unreal.Name(name))
    safe_set(expression, "default_value", float(value))
    return expression


def create_multiply(material, x, y):
    return unreal.MaterialEditingLibrary.create_material_expression(
        material,
        unreal.MaterialExpressionMultiply,
        x,
        y,
    )


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
        suffix = asset_name.split("_FinalTrial_", 1)[-1]
        try:
            candidate_paths = unreal.EditorAssetLibrary.list_assets(TEXTURE_DESTINATION, recursive=False, include_folder=False)
        except Exception:
            candidate_paths = []
        for candidate_path in candidate_paths:
            candidate_name = candidate_path.rsplit("/", 1)[-1].split(".", 1)[0]
            if "FinalTrial" in candidate_name and candidate_name.endswith(suffix):
                if candidate_path != texture_path:
                    unreal.EditorAssetLibrary.rename_asset(candidate_path, texture_path)
                texture = unreal.load_asset(texture_path)
                break
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
    imported = {}
    for key, spec in MATERIAL_SPECS.items():
        imported[key] = {
            "bc": import_texture(spec["bc"].stem, spec["bc"], True),
            "normal": import_texture(spec["n"].stem, spec["n"], False, "TC_NORMALMAP"),
            "orm": import_texture(spec["orm"].stem, spec["orm"], False, "TC_MASKS"),
        }
    return imported


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


def ensure_parent_material(key, textures):
    spec = MATERIAL_SPECS[key]
    material = ensure_material(spec["parent"])
    blend_mode = getattr(unreal.BlendMode, "BLEND_OPAQUE", None)
    if blend_mode is not None:
        safe_set(material, "blend_mode", blend_mode)
    safe_set(material, "two_sided", False)

    bc = create_texture_sample(material, textures["bc"], -980, -300, "SAMPLERTYPE_COLOR")
    normal = create_texture_sample(material, textures["normal"], -980, -20, "SAMPLERTYPE_NORMAL")
    orm = create_texture_sample(material, textures["orm"], -980, 260, "SAMPLERTYPE_MASKS")
    base = create_vector_parameter(material, "BaseColor", spec["color"], -620, -220)
    multiply = create_multiply(material, -330, -260)
    emissive = create_vector_parameter(material, "EmissiveColor", unreal.LinearColor(0.0, 0.0, 0.0, 1.0), -620, -40)
    roughness = create_scalar_parameter(material, "Roughness", spec["roughness"], -620, 140)
    metallic = create_scalar_parameter(material, "Metallic", spec["metallic"], -620, 300)

    connect_expression(bc, "RGB", multiply, "A")
    connect_expression(base, "", multiply, "B")
    connect_first_property(multiply, ("",), "MP_BASE_COLOR")
    connect_first_property(emissive, ("",), "MP_EMISSIVE_COLOR")
    connect_first_property(normal, ("RGB", "RGBA", ""), "MP_NORMAL")
    connect_first_property(orm, ("R",), "MP_AMBIENT_OCCLUSION")
    connect_first_property(orm, ("G",), "MP_ROUGHNESS")
    connect_first_property(orm, ("B",), "MP_METALLIC")
    configure_static_material(material)
    unreal.EditorAssetLibrary.save_asset("{}/{}".format(MATERIAL_PATH, spec["parent"]))
    return material


def ensure_material_instance(name, parent_material, spec):
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
    mat_lib = unreal.MaterialEditingLibrary
    mat_lib.set_material_instance_vector_parameter_value(instance, "BaseColor", spec["color"])
    mat_lib.set_material_instance_vector_parameter_value(instance, "EmissiveColor", unreal.LinearColor(0.0, 0.0, 0.0, 1.0))
    mat_lib.set_material_instance_scalar_parameter_value(instance, "Roughness", spec["roughness"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "Metallic", spec["metallic"])
    unreal.EditorAssetLibrary.save_loaded_asset(instance)
    return instance


def build_materials(imported_textures):
    instances = {}
    for key, textures in imported_textures.items():
        parent = ensure_parent_material(key, textures)
        instances[key] = ensure_material_instance(MATERIAL_SPECS[key]["instance"], parent, MATERIAL_SPECS[key])
    return instances


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
    safe_set(static_data, "auto_generate_collision", True)
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


def material_key_for_slot(slot_name, index):
    lower_name = str(slot_name).lower()
    if "a1projection" in lower_name or "projection" in lower_name:
        return "projection"
    if "darkstone" in lower_name or "dark_stone" in lower_name:
        return "dark_stone"
    if "earth" in lower_name or "ash" in lower_name or "mud" in lower_name or "ground" in lower_name:
        return "earth"
    if "rawhide" in lower_name or "binding" in lower_name or "lashing" in lower_name:
        return "rawhide"
    if "bloodaxeredpaint" in lower_name or "redpaint" in lower_name or "red_paint" in lower_name or "paint" in lower_name:
        return "red"
    if "stone" in lower_name or "slab" in lower_name or "highlight" in lower_name or "crack" in lower_name:
        return "stone"
    for key, spec in MATERIAL_SPECS.items():
        if any(term in lower_name for term in spec["slot_terms"]):
            return key
    if index == 1:
        return "stone"
    return "stone"


def assign_materials(mesh, instances):
    slots = material_slots(mesh)
    if len(slots) < 6:
        unreal.log_warning("{} imported with {} material slots; expected at least 6.".format(mesh.get_name(), len(slots)))
    for index, slot in enumerate(slots):
        slot_name = slot.get_editor_property("material_slot_name")
        key = material_key_for_slot(slot_name, index)
        mesh.set_material(index, instances[key])
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def ensure_review_lods_static(mesh, target_lods=4):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is None:
        raise RuntimeError("StaticMeshEditorSubsystem is unavailable; cannot create static mesh LODs")

    reduction_settings = unreal.Array(unreal.StaticMeshReductionSettings)
    for percent in (1.0, 0.70, 0.42, 0.22):
        setting = unreal.StaticMeshReductionSettings()
        safe_set(setting, "percent_triangles", percent)
        reduction_settings.append(setting)

    options = unreal.StaticMeshReductionOptions()
    safe_set(options, "auto_compute_lod_screen_size", True)
    safe_set(options, "reduction_settings", reduction_settings)
    result = subsystem.set_lods(mesh, options)
    count = subsystem.get_lod_count(mesh)
    if count < target_lods:
        raise RuntimeError("{} has {} static LODs after reduction, expected {}".format(mesh.get_name(), count, target_lods))
    if not result:
        unreal.log_warning("{} generated {} LODs, but StaticMeshEditorSubsystem.set_lods returned false.".format(mesh.get_name(), count))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def collision_box_shape():
    enum_candidates = (
        "ScriptCollisionShapeType",
        "ScriptingCollisionShapeType",
        "ScriptingCollisionShapeType_Deprecated",
        "ScriptingCollisionShapeType_DEPRECATED",
    )
    for enum_name in enum_candidates:
        enum_type = getattr(unreal, enum_name, None)
        if enum_type is None:
            continue
        for value_name in ("BOX", "Box"):
            value = getattr(enum_type, value_name, None)
            if value is not None:
                return value
    return None


def add_broad_simple_collision(mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        try:
            subsystem.remove_collisions(mesh)
        except Exception as exc:
            unreal.log_warning("Could not clear simple collision on {}: {}".format(mesh.get_name(), exc))

        try:
            result = subsystem.set_convex_decomposition_collisions(mesh, 4, 16, 100000)
            convex_count = subsystem.get_convex_collision_count(mesh)
            simple_count = subsystem.get_simple_collision_count(mesh)
        except Exception as exc:
            raise RuntimeError("Failed to generate convex collision for {}: {}".format(mesh.get_name(), exc))
        if not result or max(int(convex_count), int(simple_count)) < 1:
            raise RuntimeError(
                "Convex collision generation returned {} with convex_count={} simple_count={} for {}".format(
                    result,
                    convex_count,
                    simple_count,
                    mesh.get_name(),
                )
            )
        unreal.EditorAssetLibrary.save_loaded_asset(mesh)
        return

    box_shape = collision_box_shape()
    if box_shape is None:
        raise RuntimeError("Unreal Python collision shape enum is unavailable; cannot add simple box collision")

    adder = getattr(unreal.EditorStaticMeshLibrary, "add_simple_collisions", None)
    collision_index = adder(mesh, box_shape) if callable(adder) else None
    if collision_index is None or int(collision_index) < 0:
        raise RuntimeError("Could not add fallback simple box collision to {}".format(mesh.get_name()))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def apply_mesh_metadata(mesh):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag is unavailable; skipped final-trial cairn metadata")
        return
    metadata = {
        "Aerathea.StaticMesh.Package": ASSET_NAME,
        "Aerathea.StaticMesh.Status": "unreal_game_ready_final_trial_candidate_pending_flamestrike_review",
        "Aerathea.StaticMesh.PackageDoc": PACKAGE_DOC,
        "Aerathea.StaticMesh.DCCStatusDoc": PACKAGE_DOC,
        "Aerathea.StaticMesh.SourceMethod": "hand_authored_360_dcc_with_a01_front_projection_material_and_inferred_side_back_forms",
        "Aerathea.StaticMesh.VisualCanonSource": "VC_GIA_BloodAxe_CairnStones_A01_A1_Crop",
        "Aerathea.StaticMesh.TextureProjection": "a01_guided_front_projection_on_true_3d_mesh_faces_no_front_card_projection",
        "Aerathea.StaticMesh.CollisionPolicy": "broad_simple_static_prop_collision",
        "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
        "Aerathea.StaticMesh.FinalArtAuthored": "true",
        "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_review",
    }
    for tag, value in metadata.items():
        setter(mesh, tag, str(value))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def main():
    imported_textures = import_textures()
    material_instances = build_materials(imported_textures)
    mesh = import_static_mesh()
    assign_materials(mesh, material_instances)
    ensure_review_lods_static(mesh)
    add_broad_simple_collision(mesh)
    apply_mesh_metadata(mesh)

    unreal.EditorAssetLibrary.save_directory(DESTINATION, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(TEXTURE_DESTINATION, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_INSTANCE_PATH, only_if_is_dirty=False, recursive=True)
    unreal.log("Aerathea Blood Axe final-trial cairn import complete: {}".format(ASSET_PATH))


if __name__ == "__main__":
    main()
