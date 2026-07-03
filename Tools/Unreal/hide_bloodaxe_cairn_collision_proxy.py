import unreal


MESH_PATH = "/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady"
LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_ReviewIsland"
ACTOR_LABEL = "AET_REVIEW_CurrentAsset_BloodAxeCairn_A01"
REVIEW_MATERIAL_PATH = "/Game/Aerathea/Materials/Review"
HIDDEN_PROXY_MATERIAL_NAME = "M_AET_CollisionProxy_Hidden_A01"
HIDDEN_PROXY_MATERIAL_PATH = "{}/{}".format(REVIEW_MATERIAL_PATH, HIDDEN_PROXY_MATERIAL_NAME)
PROXY_TERMS = ("collisionproxy", "reviewonly", "collision")


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
        return bool(unreal.MaterialEditingLibrary.connect_material_property(expression, output_name or "", prop))
    except Exception as exc:
        unreal.log_warning("Could not connect {} to {}: {}".format(type(expression).__name__, property_name, exc))
        return False


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


def configure_static_material(material):
    safe_set(material, "used_with_static_mesh", True)
    usage = getattr(unreal.MaterialUsage, "MATUSAGE_STATIC_MESH", None)
    if usage is not None:
        try:
            unreal.MaterialEditingLibrary.set_material_usage(material, usage)
        except Exception as exc:
            unreal.log_warning("Could not set static mesh usage on {}: {}".format(material.get_name(), exc))
    unreal.MaterialEditingLibrary.recompile_material(material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)


def ensure_hidden_proxy_material():
    ensure_directory(REVIEW_MATERIAL_PATH)
    material = unreal.load_asset(HIDDEN_PROXY_MATERIAL_PATH)
    if material is None:
        material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=HIDDEN_PROXY_MATERIAL_NAME,
            package_path=REVIEW_MATERIAL_PATH,
            asset_class=unreal.Material,
            factory=unreal.MaterialFactoryNew(),
        )
        if material is None:
            raise RuntimeError("Failed to create material {}".format(HIDDEN_PROXY_MATERIAL_PATH))

    clear_material_graph(material)
    blend_mode = getattr(unreal.BlendMode, "BLEND_MASKED", None)
    if blend_mode is not None:
        safe_set(material, "blend_mode", blend_mode)
    safe_set(material, "two_sided", False)
    safe_set(material, "opacity_mask_clip_value", 0.5)

    base = create_vector_parameter(material, "BaseColor", unreal.LinearColor(0.0, 0.0, 0.0, 1.0), -520, -120)
    roughness = create_constant(material, 1.0, -520, 80)
    mask = create_constant(material, 0.0, -520, 240)
    connect_first_property(base, ("",), "MP_BASE_COLOR")
    connect_first_property(roughness, ("",), "MP_ROUGHNESS")
    connect_first_property(mask, ("",), "MP_OPACITY_MASK")
    configure_static_material(material)
    return material


def slot_name(slot):
    try:
        return str(slot.get_editor_property("material_slot_name"))
    except Exception:
        return ""


def is_proxy_slot(name):
    lower_name = name.lower()
    return any(term in lower_name for term in PROXY_TERMS)


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    return list(actor_subsystem.get_all_level_actors())


def find_actor_by_label(label):
    for actor in all_level_actors():
        if actor.get_actor_label() == label:
            return actor
    return None


def disable_proxy_sections(mesh, proxy_indices):
    subsystem_class = getattr(unreal, "StaticMeshEditorSubsystem", None)
    subsystem = unreal.get_editor_subsystem(subsystem_class) if subsystem_class is not None else None
    if subsystem is None or not proxy_indices:
        return

    try:
        lod_count = subsystem.get_lod_count(mesh)
    except Exception:
        return

    getter = getattr(subsystem, "get_lod_material_slot", None)
    shadow_setter = getattr(subsystem, "enable_section_cast_shadow", None)
    collision_setter = getattr(subsystem, "enable_section_collision", None)
    if not callable(getter):
        return

    for lod_index in range(int(lod_count)):
        for section_index in range(64):
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


def update_review_actor(hidden_material, proxy_indices):
    if not unreal.EditorAssetLibrary.does_asset_exist(LEVEL_PATH):
        return
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        unreal.log_warning("Could not load review island {}".format(LEVEL_PATH))
        return

    actor = find_actor_by_label(ACTOR_LABEL)
    if actor is None:
        unreal.log_warning("Review actor {} not found; mesh material was still updated.".format(ACTOR_LABEL))
        return
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        unreal.log_warning("{} has no StaticMeshComponent.".format(ACTOR_LABEL))
        return

    component.modify()
    for index in sorted(proxy_indices):
        component.set_material(index, hidden_material)
    unreal.EditorLevelLibrary.save_current_level()


def main():
    mesh = unreal.load_asset(MESH_PATH)
    if mesh is None:
        raise RuntimeError("Missing mesh {}".format(MESH_PATH))

    hidden_material = ensure_hidden_proxy_material()
    slots = list(mesh.get_editor_property("static_materials"))
    proxy_indices = set()
    for index, slot in enumerate(slots):
        name = slot_name(slot)
        if not is_proxy_slot(name):
            continue
        mesh.set_material(index, hidden_material)
        proxy_indices.add(index)
        unreal.log("Assigned hidden proxy material to {} slot {} ({})".format(MESH_PATH, index, name))

    if not proxy_indices:
        raise RuntimeError("{} has no proxy material slots to hide".format(MESH_PATH))

    disable_proxy_sections(mesh, proxy_indices)
    unreal.EditorAssetLibrary.save_loaded_asset(mesh)
    update_review_actor(hidden_material, proxy_indices)
    unreal.EditorAssetLibrary.save_directory(REVIEW_MATERIAL_PATH, only_if_is_dirty=False, recursive=True)
    unreal.log("Hidden {} proxy slot(s) on {}".format(len(proxy_indices), MESH_PATH))


if __name__ == "__main__":
    main()
