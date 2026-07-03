from pathlib import Path
import sys

import unreal


sys.path.append(str(Path(__file__).resolve().parent))
from bloodaxe_cairn_variant_batch_config import (  # noqa: E402
    ASSETS,
    FBX_IMPORT_UNIFORM_SCALE,
    IMPORT_PACKET_DOC,
    KIT_ID,
    MATERIAL_INSTANCE_PATH,
    PACKAGE_DOC,
    PARENT_MATERIAL_PATH,
    REVIEW_PROXY_MATERIAL_PATH,
    VISUAL_CANON_SOURCE,
    destination_path,
    import_source_path,
    lod_path,
)


PROXY_SLOT_TERMS = ("collisionproxy", "ucx", "reviewonly", "collision")


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


def connect_property(expression, property_name):
    prop = getattr(unreal.MaterialProperty, property_name, None)
    if prop is None:
        unreal.log_warning("MaterialProperty.{} unavailable; skipped connection.".format(property_name))
        return False
    try:
        unreal.MaterialEditingLibrary.connect_material_property(expression, "", prop)
        return True
    except Exception as exc:
        unreal.log_warning("Could not connect {} to {}: {}".format(type(expression).__name__, property_name, exc))
        return False


def connect_expression(output_expression, input_expression, input_name):
    try:
        unreal.MaterialEditingLibrary.connect_material_expressions(
            output_expression,
            "",
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


def clear_material_graph(material):
    try:
        for expression in list(material.get_editor_property("expressions")):
            unreal.MaterialEditingLibrary.delete_material_expression(material, expression)
    except Exception as exc:
        unreal.log_warning("Could not clear material graph for {}: {}".format(material.get_name(), exc))


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


def ensure_vertex_color_material():
    parent_dir = asset_dir(PARENT_MATERIAL_PATH)
    parent_name = asset_name(PARENT_MATERIAL_PATH)
    ensure_directory(parent_dir)
    material = unreal.load_asset(PARENT_MATERIAL_PATH)
    if material is None:
        material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=parent_name,
            package_path=parent_dir,
            asset_class=unreal.Material,
            factory=unreal.MaterialFactoryNew(),
        )
        if material is None:
            raise RuntimeError("Failed to create material {}".format(PARENT_MATERIAL_PATH))

    clear_material_graph(material)
    mat_lib = unreal.MaterialEditingLibrary
    vertex_color_class = getattr(unreal, "MaterialExpressionVertexColor", None)
    if vertex_color_class is not None:
        vertex_color = mat_lib.create_material_expression(material, vertex_color_class, -620, -120)
    else:
        vertex_color = create_vector_parameter(material, "FallbackColor", unreal.LinearColor(0.34, 0.32, 0.28, 1.0), -620, -120)
        unreal.log_warning("MaterialExpressionVertexColor unavailable; using fallback constant color")

    tint = create_vector_parameter(material, "ValueTint", unreal.LinearColor(0.42, 0.39, 0.34, 1.0), -620, 60)
    multiply_class = getattr(unreal, "MaterialExpressionMultiply", None)
    if multiply_class is not None:
        multiply = mat_lib.create_material_expression(material, multiply_class, -300, -50)
        if connect_expression(vertex_color, multiply, "A") and connect_expression(tint, multiply, "B"):
            connect_property(multiply, "MP_BASE_COLOR")
        else:
            connect_property(vertex_color, "MP_BASE_COLOR")
    else:
        connect_property(vertex_color, "MP_BASE_COLOR")

    roughness = create_scalar_parameter(material, "Roughness", 0.88, -620, 230)
    metallic = create_scalar_parameter(material, "Metallic", 0.0, -620, 380)
    connect_property(roughness, "MP_ROUGHNESS")
    connect_property(metallic, "MP_METALLIC")
    configure_static_material(material)
    unreal.EditorAssetLibrary.save_asset(PARENT_MATERIAL_PATH)
    return material


def ensure_material_instance(parent_material):
    instance_dir = asset_dir(MATERIAL_INSTANCE_PATH)
    instance_name = asset_name(MATERIAL_INSTANCE_PATH)
    ensure_directory(instance_dir)
    instance = unreal.load_asset(MATERIAL_INSTANCE_PATH)
    if instance is None:
        instance = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=instance_name,
            package_path=instance_dir,
            asset_class=unreal.MaterialInstanceConstant,
            factory=unreal.MaterialInstanceConstantFactoryNew(),
        )
        if instance is None:
            raise RuntimeError("Failed to create material instance {}".format(MATERIAL_INSTANCE_PATH))
    safe_set(instance, "parent", parent_material)
    mat_lib = unreal.MaterialEditingLibrary
    mat_lib.set_material_instance_vector_parameter_value(instance, "ValueTint", unreal.LinearColor(0.42, 0.39, 0.34, 1.0))
    mat_lib.set_material_instance_scalar_parameter_value(instance, "Roughness", 0.88)
    mat_lib.set_material_instance_scalar_parameter_value(instance, "Metallic", 0.0)
    unreal.EditorAssetLibrary.save_loaded_asset(instance)
    return instance


def ensure_hidden_proxy_material():
    material = unreal.load_asset(REVIEW_PROXY_MATERIAL_PATH)
    if material is None:
        raise RuntimeError("Missing review proxy material {}".format(REVIEW_PROXY_MATERIAL_PATH))
    return material


def import_static_mesh(asset):
    source = import_source_path(asset)
    if not source.exists():
        raise RuntimeError("Missing source FBX: {}".format(source))
    destination = destination_path(asset)
    ensure_directory(destination)

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
    normal_method = getattr(getattr(unreal, "FBXNormalImportMethod", object), "FBXNIM_IMPORT_NORMALS", None)
    if normal_method is not None:
        safe_set(static_data, "normal_import_method", normal_method)
    vertex_option = getattr(unreal, "VertexColorImportOption", None)
    if vertex_option is not None and hasattr(vertex_option, "REPLACE"):
        safe_set(static_data, "vertex_color_import_option", vertex_option.REPLACE)

    task = unreal.AssetImportTask()
    task.set_editor_property("filename", str(source))
    task.set_editor_property("destination_path", destination)
    task.set_editor_property("destination_name", asset["name"])
    task.set_editor_property("replace_existing", True)
    task.set_editor_property("automated", True)
    task.set_editor_property("save", True)
    task.set_editor_property("options", fbx_ui)

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    mesh = unreal.load_asset(asset["unreal_path"])
    if mesh is None:
        raise RuntimeError("Import did not produce expected static mesh: {}".format(asset["unreal_path"]))
    safe_set(mesh, "light_map_resolution", 64)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return mesh


def import_authored_lods(asset, mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is None:
        raise RuntimeError("StaticMeshEditorSubsystem is unavailable; cannot import authored LODs")

    remover = getattr(subsystem, "remove_lods", None)
    if callable(remover):
        try:
            remover(mesh)
        except Exception as exc:
            unreal.log_warning("Could not clear existing LODs on {}: {}".format(asset["name"], exc))

    importer = getattr(subsystem, "import_lod", None)
    if not callable(importer):
        raise RuntimeError("StaticMeshEditorSubsystem.import_lod is unavailable")
    for lod_index in (1, 2, 3):
        lod_source = lod_path(asset, lod_index)
        if not lod_source.exists():
            raise RuntimeError("Missing authored LOD{} source: {}".format(lod_index, lod_source))
        result = importer(mesh, lod_index, str(lod_source))
        unreal.log("Imported {} LOD{} from {} result={}".format(asset["name"], lod_index, lod_source, result))

    lod_count = int(subsystem.get_lod_count(mesh))
    if lod_count < 4:
        raise RuntimeError("{} has {} LODs after authored LOD import, expected 4".format(asset["name"], lod_count))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def material_slots(mesh):
    try:
        return list(mesh.get_editor_property("static_materials"))
    except Exception:
        return []


def slot_name(slot):
    try:
        return str(slot.get_editor_property("material_slot_name"))
    except Exception:
        return ""


def is_proxy_slot(name):
    lower = name.lower()
    return any(term in lower for term in PROXY_SLOT_TERMS)


def disable_proxy_sections(mesh, proxy_indices):
    if not proxy_indices:
        return
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is None:
        return

    lod_count = int(subsystem.get_lod_count(mesh))
    getter = getattr(subsystem, "get_lod_material_slot", None)
    shadow_setter = getattr(subsystem, "enable_section_cast_shadow", None)
    collision_setter = getattr(subsystem, "enable_section_collision", None)
    if not callable(getter):
        return

    for lod_index in range(lod_count):
        for section_index in range(128):
            try:
                material_slot = int(getter(mesh, lod_index, section_index))
            except Exception:
                break
            if material_slot not in proxy_indices:
                continue
            if callable(shadow_setter):
                try:
                    shadow_setter(mesh, lod_index, section_index, False)
                except Exception:
                    pass
            if callable(collision_setter):
                try:
                    collision_setter(mesh, lod_index, section_index, False)
                except Exception:
                    pass


def assign_materials(mesh, visual_material, hidden_proxy_material):
    proxy_indices = set()
    for index, slot in enumerate(material_slots(mesh)):
        name = slot_name(slot)
        if is_proxy_slot(name):
            mesh.set_material(index, hidden_proxy_material)
            proxy_indices.add(index)
        else:
            mesh.set_material(index, visual_material)
    disable_proxy_sections(mesh, proxy_indices)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return len(proxy_indices)


def collision_counts(mesh):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        try:
            return int(subsystem.get_simple_collision_count(mesh)), int(subsystem.get_convex_collision_count(mesh))
        except Exception as exc:
            unreal.log_warning("Could not read collision counts from StaticMeshEditorSubsystem for {}: {}".format(mesh.get_name(), exc))

    counter = getattr(unreal.EditorStaticMeshLibrary, "get_simple_collision_count", None)
    if callable(counter):
        try:
            return int(counter(mesh)), 0
        except Exception as exc:
            unreal.log_warning("Could not read simple collision count for {}: {}".format(mesh.get_name(), exc))
    return 0, 0


def add_broad_simple_collision_if_needed(mesh, expected_proxy_count):
    simple_count, convex_count = collision_counts(mesh)
    if max(simple_count, convex_count) >= 1:
        return "imported_or_existing", simple_count, convex_count

    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is not None:
        try:
            result = subsystem.set_convex_decomposition_collisions(mesh, max(1, int(expected_proxy_count)), 12, 100000)
            simple_count, convex_count = collision_counts(mesh)
            if max(simple_count, convex_count) >= 1:
                unreal.EditorAssetLibrary.save_loaded_asset(mesh)
                return "generated_convex_fallback", simple_count, convex_count
            unreal.log_warning(
                "Convex fallback returned {} but collision counts are simple={} convex={} for {}".format(
                    result,
                    simple_count,
                    convex_count,
                    mesh.get_name(),
                )
            )
        except Exception as exc:
            unreal.log_warning("Convex fallback failed for {}: {}".format(mesh.get_name(), exc))

    shape = None
    for enum_name in ("ScriptCollisionShapeType", "ScriptingCollisionShapeType", "ScriptingCollisionShapeType_Deprecated"):
        enum_type = getattr(unreal, enum_name, None)
        if enum_type is None:
            continue
        shape = getattr(enum_type, "BOX", None) or getattr(enum_type, "Box", None)
        if shape is not None:
            break
    adder = getattr(unreal.EditorStaticMeshLibrary, "add_simple_collisions", None)
    if shape is None or not callable(adder):
        raise RuntimeError("No collision fallback API available for {}".format(mesh.get_name()))
    collision_index = adder(mesh, shape)
    simple_count, convex_count = collision_counts(mesh)
    if collision_index is None or int(collision_index) < 0 or max(simple_count, convex_count) < 1:
        raise RuntimeError("Failed to add fallback simple box collision to {}".format(mesh.get_name()))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    return "generated_box_fallback", simple_count, convex_count


def set_metadata(mesh, asset, collision_source, simple_count, convex_count, proxy_slot_count):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag is unavailable; skipped batch import metadata")
        return
    metadata = {
        "Aerathea.StaticMesh.Status": "unreal_import_candidate_pending_validation",
        "Aerathea.StaticMesh.SourceStatus": "dcc_game_ready_candidate",
        "Aerathea.StaticMesh.Package": KIT_ID,
        "Aerathea.StaticMesh.PackageDoc": PACKAGE_DOC,
        "Aerathea.StaticMesh.ImportPacket": IMPORT_PACKET_DOC,
        "Aerathea.StaticMesh.VisualCanonSource": VISUAL_CANON_SOURCE,
        "Aerathea.StaticMesh.CollisionPolicy": "broad_simple_static_prop_collision",
        "Aerathea.StaticMesh.GameplayBehavior": "none_static_environmental_storytelling",
        "Aerathea.StaticMesh.FinalArtAuthored": "false",
        "Aerathea.StaticMesh.FinalVisualApproval": "pending_flamestrike_review",
        "Aerathea.StaticMesh.MaterialMode": "shared_vertex_color_review_material_no_final_textures",
        "Aerathea.StaticMesh.FinalTextureSetAuthored": "false",
        "Aerathea.StaticMesh.LODSource": "authored_fbx_lod1_lod2_lod3",
        "Aerathea.StaticMesh.ImportSourceFBX": str(import_source_path(asset).relative_to(Path(__file__).resolve().parents[2])),
        "Aerathea.StaticMesh.UnrealImportTested": "false",
        "Aerathea.StaticMesh.ReviewIslandPlaced": "false",
        "Aerathea.StaticMesh.ExpectedCollisionProxyCount": str(asset["collision_proxies"]),
        "Aerathea.StaticMesh.ImportedSimpleCollisionCount": str(simple_count),
        "Aerathea.StaticMesh.ImportedConvexCollisionCount": str(convex_count),
        "Aerathea.StaticMesh.CollisionImportSource": collision_source,
        "Aerathea.StaticMesh.ProxyRenderSlotCount": str(proxy_slot_count),
    }
    for tag, value in metadata.items():
        setter(mesh, tag, str(value))
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)


def import_asset(asset, visual_material, hidden_proxy_material):
    mesh = import_static_mesh(asset)
    import_authored_lods(asset, mesh)
    proxy_slot_count = assign_materials(mesh, visual_material, hidden_proxy_material)
    collision_source, simple_count, convex_count = add_broad_simple_collision_if_needed(mesh, asset["collision_proxies"])
    set_metadata(mesh, asset, collision_source, simple_count, convex_count, proxy_slot_count)
    unreal.EditorAssetLibrary.save_directory(destination_path(asset), only_if_is_dirty=False, recursive=True)
    unreal.log(
        "Imported {}: {} LODs, collision simple={} convex={} source={}, proxy_render_slots={}".format(
            asset["name"],
            int(unreal.get_editor_subsystem(unreal.StaticMeshEditorSubsystem).get_lod_count(mesh)),
            simple_count,
            convex_count,
            collision_source,
            proxy_slot_count,
        )
    )


def main():
    parent_material = ensure_vertex_color_material()
    material_instance = ensure_material_instance(parent_material)
    hidden_proxy_material = ensure_hidden_proxy_material()
    for asset in ASSETS:
        import_asset(asset, material_instance, hidden_proxy_material)

    unreal.EditorAssetLibrary.save_directory(asset_dir(PARENT_MATERIAL_PATH), only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(asset_dir(MATERIAL_INSTANCE_PATH), only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(asset_dir(REVIEW_PROXY_MATERIAL_PATH), only_if_is_dirty=True, recursive=True)
    unreal.log("Aerathea Blood Axe cairn variant batch import complete: {} assets.".format(len(ASSETS)))


if __name__ == "__main__":
    main()
