import unreal


MATERIAL_PATH = "/Game/Aerathea/Materials/Infernals/VFX"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
VFX_PATH = "/Game/Aerathea/VFX/Infernals/AbyssalSpellcasting"


VFX_MATERIAL_SPECS = {
    "AbyssalArc": {
        "parent": "M_INF_AbyssalArc_A01",
        "instance": "MI_INF_AbyssalArc_A01",
        "base": unreal.LinearColor(1.0, 0.18, 0.025, 1.0),
        "emissive": unreal.LinearColor(4.2, 0.72, 0.045, 1.0),
        "opacity": 0.62,
        "blend": "BLEND_ADDITIVE",
    },
    "AbyssalFlame": {
        "parent": "M_INF_AbyssalFlame_A01",
        "instance": "MI_INF_AbyssalFlame_A01",
        "base": unreal.LinearColor(0.90, 0.12, 0.035, 1.0),
        "emissive": unreal.LinearColor(3.8, 0.38, 0.035, 1.0),
        "opacity": 0.72,
        "blend": "BLEND_ADDITIVE",
    },
    "BrandPulse": {
        "parent": "M_INF_BrandPulse_A01",
        "instance": "MI_INF_BrandPulse_A01",
        "base": unreal.LinearColor(1.0, 0.24, 0.040, 1.0),
        "emissive": unreal.LinearColor(5.0, 0.55, 0.055, 1.0),
        "opacity": 0.55,
        "blend": "BLEND_TRANSLUCENT",
    },
    "EyeReveal": {
        "parent": "M_INF_EyeReveal_A01",
        "instance": "MI_INF_EyeReveal_A01",
        "base": unreal.LinearColor(0.95, 0.13, 0.10, 1.0),
        "emissive": unreal.LinearColor(3.2, 0.34, 1.2, 1.0),
        "opacity": 0.48,
        "blend": "BLEND_ADDITIVE",
    },
    "AshMote": {
        "parent": "M_INF_AshMote_A01",
        "instance": "MI_INF_AshMote_A01",
        "base": unreal.LinearColor(0.20, 0.16, 0.13, 1.0),
        "emissive": unreal.LinearColor(0.65, 0.12, 0.035, 1.0),
        "opacity": 0.34,
        "blend": "BLEND_TRANSLUCENT",
    },
}


NIAGARA_SYSTEM_TARGETS = {
    "NS_INF_AbyssalHandCharge_A01": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
    "NS_INF_AbyssalBolt_A01": "/Niagara/DefaultAssets/Templates/Systems/DirectionalBurst",
    "NS_INF_ClawSlashCast_A01": "/Niagara/DefaultAssets/Templates/Systems/DirectionalBurst",
    "NS_INF_BrandChannel_A01": "/Niagara/DefaultAssets/Templates/Systems/AttributeReaderTrails",
    "NS_INF_RegenerationFlare_A01": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
    "NS_INF_InvisibleSightReveal_A01": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
    "NS_INF_WingMantleCast_A01": "/Niagara/DefaultAssets/Templates/Systems/DirectionalBurst",
    "NS_INF_RageSurge_A01": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
}


NIAGARA_EMITTER_TARGETS = {
    "NE_INF_AbyssalArc_A01": "/Niagara/DefaultAssets/Templates/Emitters/StaticBeam",
    "NE_INF_AbyssalFlame_A01": "/Niagara/DefaultAssets/Templates/Emitters/SimpleSpriteBurst",
    "NE_INF_BrandPulse_A01": "/Niagara/DefaultAssets/Templates/Emitters/SingleLoopingParticle",
    "NE_INF_EyeReveal_A01": "/Niagara/DefaultAssets/Templates/Emitters/SimpleSpriteBurst",
    "NE_INF_AshMote_A01": "/Niagara/DefaultAssets/Templates/Emitters/ConfettiBurst",
}


def ensure_directory(path):
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)


def safe_set(obj, prop, value):
    try:
        obj.set_editor_property(prop, value)
    except Exception as exc:
        unreal.log_warning("Could not set {}.{}: {}".format(type(obj).__name__, prop, exc))


def material_property(property_name):
    return getattr(unreal.MaterialProperty, property_name, None)


def connect_property(expression, property_name):
    prop = material_property(property_name)
    if prop is None:
        unreal.log_warning("MaterialProperty.{} is unavailable; skipped connection.".format(property_name))
        return
    unreal.MaterialEditingLibrary.connect_material_property(expression, "", prop)


def configure_vfx_material(material, blend_name):
    blend_mode = getattr(unreal.BlendMode, blend_name, None)
    if blend_mode is not None:
        safe_set(material, "blend_mode", blend_mode)

    shading_model = getattr(unreal.MaterialShadingModel, "MSM_UNLIT", None)
    if shading_model is not None:
        safe_set(material, "shading_model", shading_model)

    safe_set(material, "two_sided", True)
    safe_set(material, "used_with_niagara_sprites", True)
    safe_set(material, "used_with_particle_sprites", True)
    safe_set(material, "used_with_beam_trails", True)
    safe_set(material, "used_with_mesh_particles", True)

    for usage_name in (
        "MATUSAGE_NIAGARA_SPRITES",
        "MATUSAGE_PARTICLE_SPRITES",
        "MATUSAGE_BEAM_TRAILS",
        "MATUSAGE_MESH_PARTICLES",
    ):
        usage = getattr(unreal.MaterialUsage, usage_name, None)
        if usage is None:
            continue
        try:
            unreal.MaterialEditingLibrary.set_material_usage(material, usage)
        except Exception as exc:
            unreal.log_warning("Could not set material usage {} on {}: {}".format(usage_name, material.get_name(), exc))

    unreal.MaterialEditingLibrary.recompile_material(material)
    unreal.EditorAssetLibrary.save_loaded_asset(material)


def create_vfx_material(spec):
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, spec["parent"])
    existing = unreal.load_asset(asset_path)
    if existing is not None:
        configure_vfx_material(existing, spec["blend"])
        return existing

    material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name=spec["parent"],
        package_path=MATERIAL_PATH,
        asset_class=unreal.Material,
        factory=unreal.MaterialFactoryNew(),
    )
    if material is None:
        raise RuntimeError("Failed to create material {}".format(asset_path))

    mat_lib = unreal.MaterialEditingLibrary

    base = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -520, -140)
    base.set_editor_property("constant", spec["base"])
    connect_property(base, "MP_BASE_COLOR")

    emissive = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -520, 40)
    emissive.set_editor_property("constant", spec["emissive"])
    connect_property(emissive, "MP_EMISSIVE_COLOR")

    opacity = mat_lib.create_material_expression(material, unreal.MaterialExpressionConstant, -520, 220)
    opacity.set_editor_property("r", spec["opacity"])
    connect_property(opacity, "MP_OPACITY")

    configure_vfx_material(material, spec["blend"])
    unreal.EditorAssetLibrary.save_asset(asset_path)
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


def ensure_vfx_materials():
    for spec in VFX_MATERIAL_SPECS.values():
        parent = create_vfx_material(spec)
        ensure_material_instance(spec["instance"], parent)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_INSTANCE_PATH, only_if_is_dirty=False, recursive=True)


def duplicate_template_asset(target_asset_path, template_asset_path):
    package_path, asset_name = target_asset_path.rsplit("/", 1)
    ensure_directory(package_path)

    existing = unreal.load_asset(target_asset_path)
    if existing is not None:
        unreal.EditorAssetLibrary.save_loaded_asset(existing)
        return existing

    template_asset = unreal.load_asset(template_asset_path)
    if template_asset is None:
        raise RuntimeError("Niagara template {} is not available for {}".format(template_asset_path, target_asset_path))

    duplicated = unreal.EditorAssetLibrary.duplicate_asset(template_asset_path, target_asset_path)
    if duplicated is None:
        duplicated = unreal.AssetToolsHelpers.get_asset_tools().duplicate_asset(
            asset_name=asset_name,
            package_path=package_path,
            original_object=template_asset,
        )
    if duplicated is None:
        raise RuntimeError("Could not duplicate Niagara template {} to {}".format(template_asset_path, target_asset_path))

    unreal.EditorAssetLibrary.save_loaded_asset(duplicated)
    unreal.log("Created template-derived Niagara asset {} from {}.".format(target_asset_path, template_asset_path))
    return duplicated


def ensure_niagara_assets():
    for asset_name, template_path in NIAGARA_SYSTEM_TARGETS.items():
        duplicate_template_asset("{}/{}".format(VFX_PATH, asset_name), template_path)
    for asset_name, template_path in NIAGARA_EMITTER_TARGETS.items():
        duplicate_template_asset("{}/{}".format(VFX_PATH, asset_name), template_path)
    unreal.EditorAssetLibrary.save_directory(VFX_PATH, only_if_is_dirty=False, recursive=True)


def main():
    ensure_directory(MATERIAL_PATH)
    ensure_directory(MATERIAL_INSTANCE_PATH)
    ensure_directory(VFX_PATH)
    ensure_vfx_materials()
    ensure_niagara_assets()
    unreal.log("Aerathea Infernal abyssal spellcasting VFX first-pass assets complete.")


main()
