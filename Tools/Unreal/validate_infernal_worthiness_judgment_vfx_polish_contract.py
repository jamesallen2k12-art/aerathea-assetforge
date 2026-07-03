import math
import os
import re

import unreal


MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
MATERIAL_PARENT_PATH = "/Game/Aerathea/Materials/Infernals/VFX"
VFX_PATH = "/Game/Aerathea/VFX/Infernals/WorthinessJudgment"

POLISH_TASK_ID = "AET-MA-20260628-002"
GRAPH_STATUS = "template_derived_contract_ready"
FINAL_GRAPH_AUTHORED = "false"
RUNTIME_CONTRACT_DOC = "docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_TIMING_TRACES.md"
READABILITY_BUDGET = "restrained_no_screen_fire_no_dense_smoke"
FIXED_BOUNDS_CONTRACT = "floor_radius_1000cm_altar_height_420cm"
SCALAR_RANGE_TOLERANCE = 0.002
HANDOFF_PATH = "docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/NIAGARA_ART_PASS_HANDOFF.md"

COMMON_CONTRACT_PARAMS = {
    "RuntimeBindingReady": (1.0, 1.0, 1.0),
    "GraphContractReady": (1.0, 1.0, 1.0),
    "FinalGraphAuthored": (0.0, 0.0, 0.0),
    "MaxOpacityBudget": (0.70, 0.70, 0.70),
    "MaxAshDensity": (0.50, 0.50, 0.50),
    "FloorBoundsRadiusCm": (1000.0, 1000.0, 1000.0),
    "AltarBoundsHeightCm": (420.0, 420.0, 420.0),
}


EXPECTED_MATERIALS = {
    "MI_INF_WorthinessRing_A01": {
        "parent": "M_INF_WorthinessRing_A01",
        "blend": "BLEND_ADDITIVE",
        "params": {
            "Opacity": (0.54, 0.0, 0.70),
            "StateIndex": (2.0, 2.0, 2.0),
            "PulseIntensity": (1.00, 0.10, 1.65),
            "PulseDuration": (2.40, 0.50, 4.50),
            "RingRadiusCm": (900.0, 600.0, 1000.0),
            "AcceptedFocus": (0.15, 0.0, 0.80),
            "RejectedSnap": (0.0, 0.0, 1.0),
            "AshDensity": (0.10, 0.0, 0.50),
        },
    },
    "MI_INF_WorthinessSigil_A01": {
        "parent": "M_INF_WorthinessSigil_A01",
        "blend": "BLEND_ADDITIVE",
        "params": {
            "Opacity": (0.62, 0.0, 0.70),
            "StateIndex": (2.0, 2.0, 2.0),
            "PulseIntensity": (1.18, 0.10, 1.65),
            "PulseDuration": (1.65, 0.50, 4.50),
            "RingRadiusCm": (220.0, 120.0, 420.0),
            "AcceptedFocus": (0.35, 0.0, 0.80),
            "RejectedSnap": (0.0, 0.0, 1.0),
            "AshDensity": (0.08, 0.0, 0.50),
        },
    },
    "MI_INF_WorthinessAsh_A01": {
        "parent": "M_INF_WorthinessAsh_A01",
        "blend": "BLEND_TRANSLUCENT",
        "params": {
            "Opacity": (0.30, 0.0, 0.70),
            "StateIndex": (5.0, 5.0, 5.0),
            "PulseIntensity": (0.28, 0.05, 1.65),
            "PulseDuration": (3.80, 0.50, 4.50),
            "RingRadiusCm": (780.0, 500.0, 1000.0),
            "AcceptedFocus": (0.0, 0.0, 0.80),
            "RejectedSnap": (0.0, 0.0, 1.0),
            "AshDensity": (0.44, 0.0, 0.50),
        },
    },
    "MI_INF_WorthinessRejected_A01": {
        "parent": "M_INF_WorthinessRejected_A01",
        "blend": "BLEND_ADDITIVE",
        "params": {
            "Opacity": (0.66, 0.0, 0.70),
            "StateIndex": (4.0, 4.0, 4.0),
            "PulseIntensity": (1.55, 0.10, 1.65),
            "PulseDuration": (0.65, 0.50, 4.50),
            "RingRadiusCm": (900.0, 600.0, 1000.0),
            "AcceptedFocus": (0.0, 0.0, 0.80),
            "RejectedSnap": (1.0, 0.0, 1.0),
            "AshDensity": (0.20, 0.0, 0.50),
        },
    },
    "MI_INF_WorthinessJudgmentPulse_A01": {
        "parent": "M_INF_WorthinessJudgmentPulse_A01",
        "blend": "BLEND_TRANSLUCENT",
        "params": {
            "Opacity": (0.50, 0.0, 0.70),
            "StateIndex": (6.0, 6.0, 6.0),
            "PulseIntensity": (1.35, 0.10, 1.65),
            "PulseDuration": (0.95, 0.50, 4.50),
            "RingRadiusCm": (900.0, 600.0, 1000.0),
            "AcceptedFocus": (0.55, 0.0, 0.80),
            "RejectedSnap": (0.25, 0.0, 1.0),
            "AshDensity": (0.18, 0.0, 0.50),
        },
    },
}

EVENT_PULSE_ONLY_BY_MATERIAL = {
    "MI_INF_WorthinessRing_A01": 0.0,
    "MI_INF_WorthinessSigil_A01": 0.0,
    "MI_INF_WorthinessAsh_A01": 0.0,
    "MI_INF_WorthinessRejected_A01": 1.0,
    "MI_INF_WorthinessJudgmentPulse_A01": 1.0,
}

for material_name, spec in EXPECTED_MATERIALS.items():
    spec["params"].update(COMMON_CONTRACT_PARAMS)
    event_pulse_only = EVENT_PULSE_ONLY_BY_MATERIAL[material_name]
    spec["params"]["EventPulseOnly"] = (event_pulse_only, event_pulse_only, event_pulse_only)


REQUIRED_NIAGARA_SYSTEMS = [
    "NS_INF_Worthiness_Inactive_A01",
    "NS_INF_Worthiness_Smolder_A01",
    "NS_INF_Worthiness_TrialActive_A01",
    "NS_INF_Worthiness_Accepted_A01",
    "NS_INF_Worthiness_Rejected_A01",
    "NS_INF_Worthiness_JudgmentPulse_A01",
]

EXPECTED_NIAGARA_SYSTEM_METADATA = {
    "NS_INF_Worthiness_Inactive_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
        "Aerathea.VFX.AssetRole": "system",
        "Aerathea.VFX.State": "Inactive",
        "Aerathea.VFX.BehaviorContract": "no_particles_or_near_zero_ambient_glow",
        "Aerathea.VFX.LocatorContract": "vfx_center",
        "Aerathea.VFX.UserParameters": ("User.State", "User.JudgmentIntensity", "User.PulseIntensity"),
    },
    "NS_INF_Worthiness_Smolder_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
        "Aerathea.VFX.AssetRole": "system",
        "Aerathea.VFX.State": "Smolder",
        "Aerathea.VFX.BehaviorContract": "low_ember_sparse_ash_only",
        "Aerathea.VFX.LocatorContract": "vfx_ring_active",
        "Aerathea.VFX.UserParameters": ("User.State", "User.JudgmentIntensity", "User.AshDensity", "User.PulseIntensity"),
    },
    "NS_INF_Worthiness_TrialActive_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Systems/AttributeReaderTrails",
        "Aerathea.VFX.AssetRole": "system",
        "Aerathea.VFX.State": "TrialActive",
        "Aerathea.VFX.BehaviorContract": "ring_sigil_pulse_driven_by_trial_progress_and_judgment_intensity",
        "Aerathea.VFX.LocatorContract": "vfx_ring_active",
        "Aerathea.VFX.UserParameters": (
            "User.State",
            "User.JudgmentIntensity",
            "User.TrialProgress",
            "User.RingRadiusCm",
            "User.PulseIntensity",
        ),
    },
    "NS_INF_Worthiness_Accepted_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
        "Aerathea.VFX.AssetRole": "system",
        "Aerathea.VFX.State": "Accepted",
        "Aerathea.VFX.BehaviorContract": "warm_focus_from_ring_to_altar_core_or_brand_transfer",
        "Aerathea.VFX.LocatorContract": "vfx_brand_transfer",
        "Aerathea.VFX.UserParameters": (
            "User.State",
            "User.JudgmentIntensity",
            "User.AcceptedFocus",
            "User.BrandTransferLocation",
        ),
    },
    "NS_INF_Worthiness_Rejected_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Systems/DirectionalBurst",
        "Aerathea.VFX.AssetRole": "system",
        "Aerathea.VFX.State": "Rejected",
        "Aerathea.VFX.BehaviorContract": "short_violet_red_snap_to_rejected_gap",
        "Aerathea.VFX.LocatorContract": "vfx_rejected_gap",
        "Aerathea.VFX.UserParameters": (
            "User.State",
            "User.JudgmentIntensity",
            "User.RejectedSeverity",
            "User.RejectedGapLocation",
            "User.RejectedSnap",
        ),
    },
    "NS_INF_Worthiness_JudgmentPulse_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
        "Aerathea.VFX.AssetRole": "system",
        "Aerathea.VFX.State": "JudgmentPulse",
        "Aerathea.VFX.BehaviorContract": "short_horned_split_wing_verdict_pulse_then_cooldown",
        "Aerathea.VFX.LocatorContract": "vfx_altar_core",
        "Aerathea.VFX.UserParameters": (
            "User.State",
            "User.JudgmentIntensity",
            "User.PulseDuration",
            "User.AltarCoreLocation",
        ),
    },
}


REQUIRED_NIAGARA_EMITTERS = [
    "NE_INF_WorthinessRingPulse_A01",
    "NE_INF_WorthinessSigilPulse_A01",
    "NE_INF_WorthinessAshMote_A01",
    "NE_INF_WorthinessRejectedSnap_A01",
]

EXPECTED_NIAGARA_EMITTER_METADATA = {
    "NE_INF_WorthinessRingPulse_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Emitters/SingleLoopingParticle",
        "Aerathea.VFX.AssetRole": "emitter",
        "Aerathea.VFX.EmitterRole": "floor_ring_pulse",
        "Aerathea.VFX.BehaviorContract": "restrained_loop_or_event_ring_read",
        "Aerathea.VFX.UserParameters": ("User.State", "User.RingRadiusCm", "User.PulseIntensity"),
    },
    "NE_INF_WorthinessSigilPulse_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Emitters/SimpleSpriteBurst",
        "Aerathea.VFX.AssetRole": "emitter",
        "Aerathea.VFX.EmitterRole": "central_sigil_pulse",
        "Aerathea.VFX.BehaviorContract": "low_frequency_horned_split_wing_read",
        "Aerathea.VFX.UserParameters": ("User.State", "User.TrialProgress", "User.JudgmentIntensity"),
    },
    "NE_INF_WorthinessAshMote_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Emitters/ConfettiBurst",
        "Aerathea.VFX.AssetRole": "emitter",
        "Aerathea.VFX.EmitterRole": "sparse_ash_motes",
        "Aerathea.VFX.BehaviorContract": "density_reduces_before_primary_read",
        "Aerathea.VFX.UserParameters": ("User.State", "User.AshDensity"),
    },
    "NE_INF_WorthinessRejectedSnap_A01": {
        "Aerathea.VFX.TemplateSource": "/Niagara/DefaultAssets/Templates/Emitters/StaticBeam",
        "Aerathea.VFX.AssetRole": "emitter",
        "Aerathea.VFX.EmitterRole": "rejected_gap_snap",
        "Aerathea.VFX.BehaviorContract": "short_violet_red_event_not_persistent_aura",
        "Aerathea.VFX.UserParameters": (
            "User.State",
            "User.RejectedSeverity",
            "User.RejectedGapLocation",
            "User.RejectedSnap",
        ),
    },
}

REQUIRED_NATIVE_USER_PARAMETERS = [
    "User.RitualState",
    "User.TrialProgress",
    "User.JudgmentIntensity",
    "User.RejectedSeverity",
    "User.CooldownAlpha",
    "User.bTrialActive",
    "User.bAccepted",
    "User.bRejected",
    "User.RitualStateColor",
    "User.AltarCoreWorldLocation",
    "User.SacrificeMarkWorldLocation",
    "User.BrandTransferWorldLocation",
    "User.RingLinkWorldLocation",
    "User.RejectedGapWorldLocation",
]

REQUIRED_HANDOFF_TERMS = [
    "GraphStatus=template_derived_contract_ready",
    "FinalGraphAuthored=false",
    "fixed bounds",
    "visual approval",
]

COMMON_METADATA = {
    "Aerathea.VFX.PolishTask": POLISH_TASK_ID,
    "Aerathea.VFX.GraphStatus": GRAPH_STATUS,
    "Aerathea.VFX.FinalGraphAuthored": FINAL_GRAPH_AUTHORED,
    "Aerathea.VFX.RuntimeContract": RUNTIME_CONTRACT_DOC,
    "Aerathea.VFX.FixedBoundsContract": FIXED_BOUNDS_CONTRACT,
    "Aerathea.VFX.ReadabilityBudget": READABILITY_BUDGET,
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


def validate_asset_exists(failures, path):
    asset = unreal.load_asset(path)
    if asset is None:
        failures.append("{} failed to load".format(path))
    return asset


def metadata_value(failures, asset, tag):
    getter = getattr(unreal.EditorAssetLibrary, "get_metadata_tag", None)
    if not callable(getter):
        failures.append("EditorAssetLibrary.get_metadata_tag is unavailable; cannot validate VFX polish metadata")
        return None

    try:
        value = getter(asset, tag)
    except Exception as exc:
        failures.append("{} metadata {} unreadable ({})".format(asset.get_path_name(), tag, exc))
        return None
    if value is None:
        return ""
    return str(value)


def validate_metadata_value(failures, asset, tag, expected):
    value = metadata_value(failures, asset, tag)
    if value is None:
        return
    if value != str(expected):
        failures.append("{} metadata {} is {!r}, expected {!r}".format(asset.get_path_name(), tag, value, expected))


def validate_metadata_parameters(failures, asset, expected_parameters):
    raw_value = metadata_value(failures, asset, "Aerathea.VFX.UserParameters")
    if raw_value is None:
        return
    actual = {item.strip() for item in raw_value.split(",") if item.strip()}
    missing = [parameter for parameter in expected_parameters if parameter not in actual]
    if missing:
        failures.append("{} metadata UserParameters missing {}".format(asset.get_path_name(), ", ".join(missing)))


def validate_polish_metadata(failures, asset, expected_metadata):
    for tag, expected in COMMON_METADATA.items():
        validate_metadata_value(failures, asset, tag, expected)
    for tag, expected in expected_metadata.items():
        if tag == "Aerathea.VFX.UserParameters":
            validate_metadata_parameters(failures, asset, expected)
        else:
            validate_metadata_value(failures, asset, tag, expected)


def validate_material_instance(failures, name, spec):
    instance_path = "{}/{}".format(MATERIAL_INSTANCE_PATH, name)
    parent_path = "{}/{}".format(MATERIAL_PARENT_PATH, spec["parent"])
    instance = validate_asset_exists(failures, instance_path)
    if instance is None:
        return

    try:
        parent = instance.get_editor_property("parent")
    except Exception as exc:
        failures.append("{} has no readable parent ({})".format(instance_path, exc))
        parent = None

    if parent is None:
        failures.append("{} has no parent material".format(instance_path))
    elif asset_path_without_object(parent) != parent_path:
        failures.append("{} parent is {}, expected {}".format(instance_path, parent.get_path_name(), parent_path))
    else:
        try:
            blend_mode = parent.get_editor_property("blend_mode")
            if normalized(spec["blend"]) not in normalized(blend_mode):
                failures.append("{} parent blend mode is {}, expected {}".format(instance_path, blend_mode, spec["blend"]))
        except Exception as exc:
            failures.append("{} parent blend mode unreadable ({})".format(instance_path, exc))

    for parameter_name, expected_range in spec["params"].items():
        expected, minimum, maximum = expected_range
        value = get_scalar_parameter(instance, parameter_name)
        if value is None:
            failures.append("{} missing scalar parameter {}".format(instance_path, parameter_name))
            continue
        if not math.isfinite(value):
            failures.append("{} {} is non-finite".format(instance_path, parameter_name))
            continue
        if value < minimum - SCALAR_RANGE_TOLERANCE or value > maximum + SCALAR_RANGE_TOLERANCE:
            failures.append(
                "{} {} is {:.3f}, expected restrained range {:.3f}-{:.3f}".format(
                    instance_path,
                    parameter_name,
                    value,
                    minimum,
                    maximum,
                )
            )
        if abs(value - expected) > 0.02:
            failures.append(
                "{} {} is {:.3f}, expected current approved value {:.3f}".format(
                    instance_path,
                    parameter_name,
                    value,
                    expected,
                )
            )


def validate_vfx_assets(failures):
    for asset_name in REQUIRED_NIAGARA_SYSTEMS:
        asset = validate_asset_exists(failures, "{}/{}".format(VFX_PATH, asset_name))
        if asset is not None:
            validate_polish_metadata(failures, asset, EXPECTED_NIAGARA_SYSTEM_METADATA[asset_name])
    for asset_name in REQUIRED_NIAGARA_EMITTERS:
        asset = validate_asset_exists(failures, "{}/{}".format(VFX_PATH, asset_name))
        if asset is not None:
            validate_polish_metadata(failures, asset, EXPECTED_NIAGARA_EMITTER_METADATA[asset_name])


def project_file_path(relative_path):
    candidate = os.path.join(os.getcwd(), relative_path)
    if os.path.exists(candidate):
        return candidate

    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(script_dir, "..", "..", relative_path))


def validate_handoff_document(failures):
    handoff_path = project_file_path(HANDOFF_PATH)
    if not os.path.exists(handoff_path):
        failures.append("{} is missing".format(HANDOFF_PATH))
        return

    with open(handoff_path, "r", encoding="utf-8") as handle:
        contents = handle.read()

    required_terms = (
        list(REQUIRED_NIAGARA_SYSTEMS)
        + list(REQUIRED_NIAGARA_EMITTERS)
        + REQUIRED_NATIVE_USER_PARAMETERS
        + REQUIRED_HANDOFF_TERMS
    )
    missing = [term for term in required_terms if term not in contents]
    if missing:
        failures.append("{} missing required handoff terms: {}".format(HANDOFF_PATH, ", ".join(missing)))


def main():
    failures = []
    for name, spec in EXPECTED_MATERIALS.items():
        validate_material_instance(failures, name, spec)
    validate_vfx_assets(failures)
    validate_handoff_document(failures)

    if failures:
        raise RuntimeError("Infernal worthiness judgment VFX polish contract failed: {}".format("; ".join(failures)))

    print(
        "Infernal worthiness judgment VFX polish contract passed: {} material instances, {} Niagara systems, {} Niagara emitters, restrained scalar ranges, graph-status metadata locked as {} with FinalGraphAuthored={}, and Niagara art-pass handoff validated.".format(
            len(EXPECTED_MATERIALS),
            len(REQUIRED_NIAGARA_SYSTEMS),
            len(REQUIRED_NIAGARA_EMITTERS),
            GRAPH_STATUS,
            FINAL_GRAPH_AUTHORED,
        )
    )


if __name__ == "__main__":
    main()
