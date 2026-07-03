import unreal


MATERIAL_PATH = "/Game/Aerathea/Materials/Infernals"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
MASTER_MATERIAL_NAME = "M_INF_BrandGlow_Master_A01"
FUNCTION_NAME = "MF_INF_BrandGlowStates_A01"


STATE_SPECS = {
    "Inactive": {
        "base": unreal.LinearColor(0.28, 0.045, 0.035, 1.0),
        "emissive": unreal.LinearColor(0.0, 0.0, 0.0, 1.0),
        "intensity": 0.0,
        "pulse_speed": 0.0,
        "pulse_width": 0.15,
        "violet_mix": 0.0,
        "scar_darken": 0.42,
        "heat_edge_contrast": 0.18,
        "state_index": 0.0,
    },
    "Smolder": {
        "base": unreal.LinearColor(0.42, 0.070, 0.040, 1.0),
        "emissive": unreal.LinearColor(1.00, 0.24, 0.045, 1.0),
        "intensity": 0.55,
        "pulse_speed": 0.22,
        "pulse_width": 0.22,
        "violet_mix": 0.0,
        "scar_darken": 0.34,
        "heat_edge_contrast": 0.32,
        "state_index": 1.0,
    },
    "TrialActive": {
        "base": unreal.LinearColor(0.58, 0.080, 0.035, 1.0),
        "emissive": unreal.LinearColor(1.00, 0.31, 0.035, 1.0),
        "intensity": 1.25,
        "pulse_speed": 0.45,
        "pulse_width": 0.34,
        "violet_mix": 0.08,
        "scar_darken": 0.28,
        "heat_edge_contrast": 0.50,
        "state_index": 2.0,
    },
    "Accepted": {
        "base": unreal.LinearColor(0.50, 0.090, 0.045, 1.0),
        "emissive": unreal.LinearColor(1.00, 0.40, 0.075, 1.0),
        "intensity": 1.05,
        "pulse_speed": 0.12,
        "pulse_width": 0.24,
        "violet_mix": 0.0,
        "scar_darken": 0.24,
        "heat_edge_contrast": 0.40,
        "state_index": 3.0,
    },
    "Rejected": {
        "base": unreal.LinearColor(0.38, 0.040, 0.060, 1.0),
        "emissive": unreal.LinearColor(1.00, 0.06, 0.58, 1.0),
        "intensity": 1.65,
        "pulse_speed": 1.55,
        "pulse_width": 0.16,
        "violet_mix": 0.68,
        "scar_darken": 0.50,
        "heat_edge_contrast": 0.72,
        "state_index": 4.0,
    },
    "SorcererFocus": {
        "base": unreal.LinearColor(0.62, 0.085, 0.040, 1.0),
        "emissive": unreal.LinearColor(1.00, 0.28, 0.82, 1.0),
        "intensity": 1.45,
        "pulse_speed": 0.38,
        "pulse_width": 0.28,
        "violet_mix": 0.35,
        "scar_darken": 0.26,
        "heat_edge_contrast": 0.62,
        "state_index": 5.0,
    },
}


SCALAR_PARAMETERS = [
    "EmissiveIntensity",
    "PulseSpeed",
    "PulseWidth",
    "VioletMix",
    "ScarDarken",
    "HeatEdgeContrast",
    "StateIndex",
]


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


def configure_brand_material(material):
    safe_set(material, "two_sided", False)
    safe_set(material, "used_with_skeletal_mesh", True)
    safe_set(material, "used_with_static_lighting", True)

    usage = getattr(unreal.MaterialUsage, "MATUSAGE_SKELETAL_MESH", None)
    if usage is not None:
        try:
            unreal.MaterialEditingLibrary.set_material_usage(material, usage)
        except Exception as exc:
            unreal.log_warning("Could not set skeletal mesh usage on {}: {}".format(material.get_name(), exc))

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

        base = create_vector_parameter(material, "BrandBaseColor", unreal.LinearColor(0.42, 0.060, 0.035, 1.0), -620, -220)
        connect_property(base, "MP_BASE_COLOR")

        emissive = create_vector_parameter(material, "EmissiveColor", unreal.LinearColor(1.0, 0.24, 0.045, 1.0), -620, -20)
        connect_property(emissive, "MP_EMISSIVE_COLOR")

        roughness = create_scalar_parameter(material, "Roughness", 0.72, -620, 180)
        connect_property(roughness, "MP_ROUGHNESS")

        create_scalar_parameter(material, "EmissiveIntensity", 0.0, -220, -170)
        create_scalar_parameter(material, "PulseSpeed", 0.0, -220, -90)
        create_scalar_parameter(material, "PulseWidth", 0.2, -220, -10)
        create_scalar_parameter(material, "VioletMix", 0.0, -220, 70)
        create_scalar_parameter(material, "ScarDarken", 0.35, -220, 150)
        create_scalar_parameter(material, "HeatEdgeContrast", 0.30, -220, 230)
        create_scalar_parameter(material, "StateIndex", 0.0, -220, 310)

    configure_brand_material(material)
    return material


def ensure_material_function():
    function_path = "{}/{}".format(MATERIAL_PATH, FUNCTION_NAME)
    existing = unreal.load_asset(function_path)
    if existing is not None:
        unreal.EditorAssetLibrary.save_loaded_asset(existing)
        return existing

    function_class = getattr(unreal, "MaterialFunction", None)
    factory_class = getattr(unreal, "MaterialFunctionFactoryNew", None)
    if function_class is None or factory_class is None:
        unreal.log_warning("MaterialFunction factory unavailable; skipped {}".format(function_path))
        return None

    function = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name=FUNCTION_NAME,
        package_path=MATERIAL_PATH,
        asset_class=function_class,
        factory=factory_class(),
    )
    if function is None:
        raise RuntimeError("Failed to create material function {}".format(function_path))
    unreal.EditorAssetLibrary.save_loaded_asset(function)
    return function


def ensure_material_instance(name, parent_material, spec):
    ensure_directory(MATERIAL_INSTANCE_PATH)
    asset_name = "MI_INF_BrandGlowStates_A01_{}".format(name)
    asset_path = "{}/{}".format(MATERIAL_INSTANCE_PATH, asset_name)
    instance = unreal.load_asset(asset_path)
    if instance is None:
        instance = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
            asset_name=asset_name,
            package_path=MATERIAL_INSTANCE_PATH,
            asset_class=unreal.MaterialInstanceConstant,
            factory=unreal.MaterialInstanceConstantFactoryNew(),
        )
        if instance is None:
            raise RuntimeError("Failed to create material instance {}".format(asset_path))

    safe_set(instance, "parent", parent_material)
    mat_lib = unreal.MaterialEditingLibrary
    mat_lib.set_material_instance_vector_parameter_value(instance, "BrandBaseColor", spec["base"])
    mat_lib.set_material_instance_vector_parameter_value(instance, "EmissiveColor", spec["emissive"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "EmissiveIntensity", spec["intensity"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "PulseSpeed", spec["pulse_speed"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "PulseWidth", spec["pulse_width"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "VioletMix", spec["violet_mix"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "ScarDarken", spec["scar_darken"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "HeatEdgeContrast", spec["heat_edge_contrast"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "StateIndex", spec["state_index"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "Roughness", 0.72)
    unreal.EditorAssetLibrary.save_loaded_asset(instance)
    return instance


def main():
    ensure_directory(MATERIAL_PATH)
    ensure_directory(MATERIAL_INSTANCE_PATH)
    parent = ensure_master_material()
    ensure_material_function()
    for state_name, spec in STATE_SPECS.items():
        ensure_material_instance(state_name, parent, spec)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_INSTANCE_PATH, only_if_is_dirty=False, recursive=True)
    unreal.log("Aerathea Infernal brand glow state materials complete: {} states.".format(len(STATE_SPECS)))


main()
