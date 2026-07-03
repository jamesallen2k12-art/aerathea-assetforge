import unreal


MATERIAL_PATH = "/Game/Aerathea/Materials/Infernals"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
TEXTURE_PATH = "/Game/Aerathea/Textures/Infernals/BalgorothCult"

MASTER_MATERIAL_NAME = "M_INF_CultStone_Master_A01"
PACKAGE_DOC = "docs/assets/materials/MI_INF_CultStone_Set_A01/PRODUCTION_PACKAGE.md"
TASK_ID = "AET-MA-20260628-026"
STATUS = "first_pass_material_ready"
READABILITY_BUDGET = "restrained_state_driven_no_full_screen_fire_no_constant_violet"


MATERIAL_SPECS = {
    "MI_INF_CultStone_Basalt_A01": {
        "role": "blue_black_basalt_ash_edge_wear",
        "base": unreal.LinearColor(0.050, 0.055, 0.062, 1.0),
        "emissive": unreal.LinearColor(0.0, 0.0, 0.0, 1.0),
        "roughness": 0.86,
        "metallic": 0.0,
        "state_index": 0.0,
        "glow_intensity": 0.0,
        "channel_opacity": 0.0,
        "rejected_violet_mix": 0.0,
        "ash_wear_amount": 0.52,
        "edge_wear_amount": 0.42,
        "heat_crack_amount": 0.08,
        "roughness_bias": 0.06,
        "final_textures_authored": 0.0,
    },
    "MI_INF_CultStone_ScorchedRed_A01": {
        "role": "dark_red_brown_scorched_stone_channels",
        "base": unreal.LinearColor(0.210, 0.055, 0.036, 1.0),
        "emissive": unreal.LinearColor(0.72, 0.12, 0.025, 1.0),
        "roughness": 0.82,
        "metallic": 0.0,
        "state_index": 1.0,
        "glow_intensity": 0.18,
        "channel_opacity": 0.34,
        "rejected_violet_mix": 0.0,
        "ash_wear_amount": 0.28,
        "edge_wear_amount": 0.32,
        "heat_crack_amount": 0.56,
        "roughness_bias": 0.03,
        "final_textures_authored": 0.0,
    },
    "MI_INF_CultStone_ObsidianInset_A01": {
        "role": "near_black_obsidian_inset_gloss",
        "base": unreal.LinearColor(0.014, 0.013, 0.018, 1.0),
        "emissive": unreal.LinearColor(0.05, 0.02, 0.015, 1.0),
        "roughness": 0.42,
        "metallic": 0.05,
        "state_index": 0.0,
        "glow_intensity": 0.03,
        "channel_opacity": 0.08,
        "rejected_violet_mix": 0.0,
        "ash_wear_amount": 0.10,
        "edge_wear_amount": 0.18,
        "heat_crack_amount": 0.12,
        "roughness_bias": -0.18,
        "final_textures_authored": 0.0,
    },
    "MI_INF_CultStone_BlackIron_A01": {
        "role": "blackened_iron_dark_bronze_edge_wear",
        "base": unreal.LinearColor(0.026, 0.022, 0.021, 1.0),
        "emissive": unreal.LinearColor(0.0, 0.0, 0.0, 1.0),
        "roughness": 0.66,
        "metallic": 0.48,
        "state_index": 0.0,
        "glow_intensity": 0.0,
        "channel_opacity": 0.0,
        "rejected_violet_mix": 0.0,
        "ash_wear_amount": 0.18,
        "edge_wear_amount": 0.36,
        "heat_crack_amount": 0.10,
        "roughness_bias": -0.04,
        "final_textures_authored": 0.0,
    },
    "MI_INF_CultStone_BoneHorn_A01": {
        "role": "smoke_stained_bone_horn_low_saturation",
        "base": unreal.LinearColor(0.55, 0.46, 0.33, 1.0),
        "emissive": unreal.LinearColor(0.0, 0.0, 0.0, 1.0),
        "roughness": 0.72,
        "metallic": 0.0,
        "state_index": 0.0,
        "glow_intensity": 0.0,
        "channel_opacity": 0.0,
        "rejected_violet_mix": 0.0,
        "ash_wear_amount": 0.22,
        "edge_wear_amount": 0.24,
        "heat_crack_amount": 0.04,
        "roughness_bias": 0.02,
        "final_textures_authored": 0.0,
    },
    "MI_INF_CultStone_AshCloth_A01": {
        "role": "black_ash_cloth_blood_dark_red_trim",
        "base": unreal.LinearColor(0.045, 0.043, 0.039, 1.0),
        "emissive": unreal.LinearColor(0.0, 0.0, 0.0, 1.0),
        "roughness": 0.88,
        "metallic": 0.0,
        "state_index": 0.0,
        "glow_intensity": 0.0,
        "channel_opacity": 0.0,
        "rejected_violet_mix": 0.0,
        "ash_wear_amount": 0.60,
        "edge_wear_amount": 0.20,
        "heat_crack_amount": 0.0,
        "roughness_bias": 0.08,
        "final_textures_authored": 0.0,
    },
    "MI_INF_CultStone_EmissiveChannel_A01": {
        "role": "restrained_ember_deep_red_channel_optional_rejection_pulse",
        "base": unreal.LinearColor(0.32, 0.055, 0.026, 1.0),
        "emissive": unreal.LinearColor(1.0, 0.25, 0.035, 1.0),
        "roughness": 0.55,
        "metallic": 0.0,
        "state_index": 2.0,
        "glow_intensity": 1.15,
        "channel_opacity": 0.78,
        "rejected_violet_mix": 0.15,
        "ash_wear_amount": 0.14,
        "edge_wear_amount": 0.18,
        "heat_crack_amount": 0.65,
        "roughness_bias": -0.08,
        "final_textures_authored": 0.0,
    },
}


SCALAR_PARAMETER_SPEC_KEYS = {
    "StateIndex": "state_index",
    "GlowIntensity": "glow_intensity",
    "ChannelOpacity": "channel_opacity",
    "RejectedVioletMix": "rejected_violet_mix",
    "AshWearAmount": "ash_wear_amount",
    "EdgeWearAmount": "edge_wear_amount",
    "HeatCrackAmount": "heat_crack_amount",
    "Roughness": "roughness",
    "Metallic": "metallic",
    "RoughnessBias": "roughness_bias",
    "FinalTexturesAuthored": "final_textures_authored",
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


def normalized_name(value):
    return str(value).strip().lower()


def expression_parameter_name(expression):
    try:
        return normalized_name(expression.get_editor_property("parameter_name"))
    except Exception:
        return ""


def material_has_scalar_parameter(material, parameter_name):
    expected = normalized_name(parameter_name)
    try:
        expressions = material.get_editor_property("expressions")
    except Exception:
        return False

    scalar_class = getattr(unreal, "MaterialExpressionScalarParameter", None)
    for expression in expressions:
        if scalar_class is not None and not isinstance(expression, scalar_class):
            continue
        if expression_parameter_name(expression) == expected:
            return True
    return False


def ensure_contract_scalar_parameters(material):
    for index, parameter_name in enumerate(SCALAR_PARAMETER_SPEC_KEYS):
        if material_has_scalar_parameter(material, parameter_name):
            continue
        create_scalar_parameter(material, parameter_name, 0.0, -220, -260 + (index * 80))


def ensure_master_material():
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, MASTER_MATERIAL_NAME)
    material = unreal.load_asset(asset_path)
    if material is None:
        material = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=MASTER_MATERIAL_NAME,
            package_path=MATERIAL_PATH,
            asset_class=unreal.Material,
            factory=unreal.MaterialFactoryNew(),
        )
        if material is None:
            raise RuntimeError("Failed to create material {}".format(asset_path))

        base = create_vector_parameter(material, "BaseColor", unreal.LinearColor(0.050, 0.055, 0.062, 1.0), -620, -240)
        connect_property(base, "MP_BASE_COLOR")

        emissive = create_vector_parameter(material, "EmissiveColor", unreal.LinearColor(0.0, 0.0, 0.0, 1.0), -620, -40)
        connect_property(emissive, "MP_EMISSIVE_COLOR")

        roughness = create_scalar_parameter(material, "Roughness", 0.82, -620, 160)
        connect_property(roughness, "MP_ROUGHNESS")

        metallic = create_scalar_parameter(material, "Metallic", 0.0, -620, 320)
        connect_property(metallic, "MP_METALLIC")

    ensure_contract_scalar_parameters(material)
    configure_static_material(material)
    return material


def apply_asset_metadata(asset, spec):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        unreal.log_warning("EditorAssetLibrary.set_metadata_tag is unavailable; skipped metadata for {}".format(asset.get_name()))
        return

    metadata = {
        "Aerathea.Material.Package": "MI_INF_CultStone_Set_A01",
        "Aerathea.Material.Task": TASK_ID,
        "Aerathea.Material.Status": STATUS,
        "Aerathea.Material.Role": spec["role"],
        "Aerathea.Material.PackageDoc": PACKAGE_DOC,
        "Aerathea.Material.ReadabilityBudget": READABILITY_BUDGET,
        "Aerathea.Material.FinalTexturesAuthored": "false",
    }
    for tag, value in metadata.items():
        setter(asset, tag, str(value))


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
    mat_lib.set_material_instance_vector_parameter_value(instance, "BaseColor", spec["base"])
    mat_lib.set_material_instance_vector_parameter_value(instance, "EmissiveColor", spec["emissive"])
    for parameter_name, spec_key in SCALAR_PARAMETER_SPEC_KEYS.items():
        mat_lib.set_material_instance_scalar_parameter_value(instance, parameter_name, spec[spec_key])
    apply_asset_metadata(instance, spec)
    unreal.EditorAssetLibrary.save_loaded_asset(instance)
    return instance


def main():
    ensure_directory(MATERIAL_PATH)
    ensure_directory(MATERIAL_INSTANCE_PATH)
    ensure_directory(TEXTURE_PATH)
    parent = ensure_master_material()
    for name, spec in MATERIAL_SPECS.items():
        ensure_material_instance(name, parent, spec)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_INSTANCE_PATH, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(TEXTURE_PATH, only_if_is_dirty=False, recursive=True)
    unreal.log("Aerathea Infernal CultStone material set complete: {} instances.".format(len(MATERIAL_SPECS)))


main()
