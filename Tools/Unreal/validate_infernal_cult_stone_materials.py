import re

import unreal


MATERIAL_PATH = "/Game/Aerathea/Materials/Infernals"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
MASTER_MATERIAL_PATH = "{}/M_INF_CultStone_Master_A01".format(MATERIAL_PATH)

PACKAGE_DOC = "docs/assets/materials/MI_INF_CultStone_Set_A01/PRODUCTION_PACKAGE.md"
TASK_ID = "AET-MA-20260628-026"
STATUS = "first_pass_material_ready"
READABILITY_BUDGET = "restrained_state_driven_no_full_screen_fire_no_constant_violet"
SCALAR_TOLERANCE = 0.003


EXPECTED_INSTANCES = {
    "MI_INF_CultStone_Basalt_A01": {
        "GlowIntensity": (0.0, 0.0, 0.10),
        "ChannelOpacity": (0.0, 0.0, 0.10),
        "RejectedVioletMix": (0.0, 0.0, 0.20),
        "AshWearAmount": (0.52, 0.0, 0.75),
        "EdgeWearAmount": (0.42, 0.0, 0.70),
        "HeatCrackAmount": (0.08, 0.0, 0.25),
        "Roughness": (0.86, 0.35, 0.95),
        "Metallic": (0.0, 0.0, 0.10),
        "FinalTexturesAuthored": (0.0, 0.0, 0.0),
    },
    "MI_INF_CultStone_ScorchedRed_A01": {
        "GlowIntensity": (0.18, 0.0, 0.45),
        "ChannelOpacity": (0.34, 0.0, 0.60),
        "RejectedVioletMix": (0.0, 0.0, 0.20),
        "AshWearAmount": (0.28, 0.0, 0.75),
        "EdgeWearAmount": (0.32, 0.0, 0.70),
        "HeatCrackAmount": (0.56, 0.0, 0.75),
        "Roughness": (0.82, 0.35, 0.95),
        "Metallic": (0.0, 0.0, 0.10),
        "FinalTexturesAuthored": (0.0, 0.0, 0.0),
    },
    "MI_INF_CultStone_ObsidianInset_A01": {
        "GlowIntensity": (0.03, 0.0, 0.15),
        "ChannelOpacity": (0.08, 0.0, 0.20),
        "RejectedVioletMix": (0.0, 0.0, 0.20),
        "AshWearAmount": (0.10, 0.0, 0.75),
        "EdgeWearAmount": (0.18, 0.0, 0.70),
        "HeatCrackAmount": (0.12, 0.0, 0.30),
        "Roughness": (0.42, 0.35, 0.95),
        "Metallic": (0.05, 0.0, 0.10),
        "FinalTexturesAuthored": (0.0, 0.0, 0.0),
    },
    "MI_INF_CultStone_BlackIron_A01": {
        "GlowIntensity": (0.0, 0.0, 0.10),
        "ChannelOpacity": (0.0, 0.0, 0.10),
        "RejectedVioletMix": (0.0, 0.0, 0.20),
        "AshWearAmount": (0.18, 0.0, 0.75),
        "EdgeWearAmount": (0.36, 0.0, 0.70),
        "HeatCrackAmount": (0.10, 0.0, 0.30),
        "Roughness": (0.66, 0.35, 0.95),
        "Metallic": (0.48, 0.35, 0.70),
        "FinalTexturesAuthored": (0.0, 0.0, 0.0),
    },
    "MI_INF_CultStone_BoneHorn_A01": {
        "GlowIntensity": (0.0, 0.0, 0.10),
        "ChannelOpacity": (0.0, 0.0, 0.10),
        "RejectedVioletMix": (0.0, 0.0, 0.20),
        "AshWearAmount": (0.22, 0.0, 0.75),
        "EdgeWearAmount": (0.24, 0.0, 0.70),
        "HeatCrackAmount": (0.04, 0.0, 0.25),
        "Roughness": (0.72, 0.35, 0.95),
        "Metallic": (0.0, 0.0, 0.10),
        "FinalTexturesAuthored": (0.0, 0.0, 0.0),
    },
    "MI_INF_CultStone_AshCloth_A01": {
        "GlowIntensity": (0.0, 0.0, 0.10),
        "ChannelOpacity": (0.0, 0.0, 0.10),
        "RejectedVioletMix": (0.0, 0.0, 0.20),
        "AshWearAmount": (0.60, 0.0, 0.75),
        "EdgeWearAmount": (0.20, 0.0, 0.70),
        "HeatCrackAmount": (0.0, 0.0, 0.10),
        "Roughness": (0.88, 0.35, 0.95),
        "Metallic": (0.0, 0.0, 0.10),
        "FinalTexturesAuthored": (0.0, 0.0, 0.0),
    },
    "MI_INF_CultStone_EmissiveChannel_A01": {
        "GlowIntensity": (1.15, 0.65, 1.35),
        "ChannelOpacity": (0.78, 0.30, 0.90),
        "RejectedVioletMix": (0.15, 0.0, 0.25),
        "AshWearAmount": (0.14, 0.0, 0.75),
        "EdgeWearAmount": (0.18, 0.0, 0.70),
        "HeatCrackAmount": (0.65, 0.0, 0.80),
        "Roughness": (0.55, 0.35, 0.95),
        "Metallic": (0.0, 0.0, 0.10),
        "FinalTexturesAuthored": (0.0, 0.0, 0.0),
    },
}


COMMON_METADATA = {
    "Aerathea.Material.Package": "MI_INF_CultStone_Set_A01",
    "Aerathea.Material.Task": TASK_ID,
    "Aerathea.Material.Status": STATUS,
    "Aerathea.Material.PackageDoc": PACKAGE_DOC,
    "Aerathea.Material.ReadabilityBudget": READABILITY_BUDGET,
    "Aerathea.Material.FinalTexturesAuthored": "false",
}


def normalized(value):
    if hasattr(value, "name"):
        value = value.name
    return re.sub(r"[^a-z0-9]", "", str(value).lower())


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def numeric_value(raw_value):
    if isinstance(raw_value, bool):
        return None
    if isinstance(raw_value, (int, float)):
        return float(raw_value)
    if isinstance(raw_value, (tuple, list)):
        for item in raw_value:
            value = numeric_value(item)
            if value is not None:
                return value
    return None


def scalar_from_parameter_values(instance, parameter_name):
    try:
        parameter_values = instance.get_editor_property("scalar_parameter_values")
    except Exception:
        return None

    for parameter_value in parameter_values:
        try:
            parameter_info = parameter_value.get_editor_property("parameter_info")
            name = parameter_info.get_editor_property("name")
            value = parameter_value.get_editor_property("parameter_value")
        except Exception:
            continue
        if normalized(name) == normalized(parameter_name):
            return numeric_value(value)
    return None


def get_scalar_parameter(instance, parameter_name):
    getter = getattr(unreal.MaterialEditingLibrary, "get_material_instance_scalar_parameter_value", None)
    if callable(getter):
        for key in (parameter_name, unreal.Name(parameter_name)):
            try:
                value = numeric_value(getter(instance, key))
                if value is not None:
                    return value
            except Exception:
                pass
    return scalar_from_parameter_values(instance, parameter_name)


def metadata_value(failures, asset, tag):
    getter = getattr(unreal.EditorAssetLibrary, "get_metadata_tag", None)
    if not callable(getter):
        failures.append("EditorAssetLibrary.get_metadata_tag is unavailable; cannot validate material metadata")
        return None
    try:
        value = getter(asset, tag)
    except Exception as exc:
        failures.append("{} metadata {} unreadable ({})".format(asset.get_path_name(), tag, exc))
        return None
    if value is None:
        return ""
    return str(value)


def validate_metadata(failures, asset):
    for tag, expected in COMMON_METADATA.items():
        value = metadata_value(failures, asset, tag)
        if value is None:
            continue
        if value != expected:
            failures.append("{} metadata {} is {!r}, expected {!r}".format(asset.get_path_name(), tag, value, expected))
    role = metadata_value(failures, asset, "Aerathea.Material.Role")
    if role is not None and not role:
        failures.append("{} has empty Aerathea.Material.Role metadata".format(asset.get_path_name()))


def validate_instance(failures, name, spec):
    asset_path = "{}/{}".format(MATERIAL_INSTANCE_PATH, name)
    instance = unreal.load_asset(asset_path)
    if instance is None:
        failures.append("{} failed to load".format(asset_path))
        return

    try:
        parent = instance.get_editor_property("parent")
    except Exception:
        parent = None
    if parent is None:
        failures.append("{} has no parent material".format(asset_path))
    elif asset_path_without_object(parent) != MASTER_MATERIAL_PATH:
        failures.append("{} has unexpected parent {}".format(asset_path, parent.get_path_name()))

    for parameter_name, (expected, minimum, maximum) in spec.items():
        value = get_scalar_parameter(instance, parameter_name)
        if value is None:
            failures.append("{} missing scalar parameter {}".format(asset_path, parameter_name))
            continue
        if value < (minimum - SCALAR_TOLERANCE) or value > (maximum + SCALAR_TOLERANCE):
            failures.append(
                "{} scalar {} is {:.3f}, expected range {:.3f}-{:.3f}".format(
                    asset_path,
                    parameter_name,
                    value,
                    minimum,
                    maximum,
                )
            )
        if minimum == maximum and abs(value - expected) > SCALAR_TOLERANCE:
            failures.append(
                "{} scalar {} is {:.3f}, expected {:.3f}".format(
                    asset_path,
                    parameter_name,
                    value,
                    expected,
                )
            )

    validate_metadata(failures, instance)


def main():
    failures = []
    parent = unreal.load_asset(MASTER_MATERIAL_PATH)
    if parent is None:
        failures.append("{} failed to load".format(MASTER_MATERIAL_PATH))

    for instance_name, spec in EXPECTED_INSTANCES.items():
        validate_instance(failures, instance_name, spec)

    if failures:
        raise RuntimeError("Infernal CultStone material validation failed: {}".format("; ".join(failures)))

    print(
        "Infernal CultStone material validation passed: 1 master material, {} first-pass material instances, final textures not authored.".format(
            len(EXPECTED_INSTANCES),
        )
    )


if __name__ == "__main__":
    main()
