import unreal


FLOOR_MESH_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01"
MATERIAL_PATH = "/Game/Aerathea/Materials/Infernals/VFX"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
VFX_PATH = "/Game/Aerathea/VFX/Infernals/WorthinessJudgment"

POLISH_TASK_ID = "AET-MA-20260628-002"
GRAPH_STATUS = "template_derived_contract_ready"
FINAL_GRAPH_AUTHORED = "false"
RUNTIME_CONTRACT_DOC = "docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_TIMING_TRACES.md"
READABILITY_BUDGET = "restrained_no_screen_fire_no_dense_smoke"
FIXED_BOUNDS_CONTRACT = "floor_radius_1000cm_altar_height_420cm"


REQUIRED_PARENT_MATERIALS = [
    "M_INF_WorthinessRing_A01",
    "M_INF_WorthinessSigil_A01",
    "M_INF_WorthinessAsh_A01",
    "M_INF_WorthinessRejected_A01",
    "M_INF_WorthinessJudgmentPulse_A01",
]


REQUIRED_MATERIAL_INSTANCES = [
    "MI_INF_WorthinessRing_A01",
    "MI_INF_WorthinessSigil_A01",
    "MI_INF_WorthinessAsh_A01",
    "MI_INF_WorthinessRejected_A01",
    "MI_INF_WorthinessJudgmentPulse_A01",
]


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

COMMON_METADATA = {
    "Aerathea.VFX.PolishTask": POLISH_TASK_ID,
    "Aerathea.VFX.GraphStatus": GRAPH_STATUS,
    "Aerathea.VFX.FinalGraphAuthored": FINAL_GRAPH_AUTHORED,
    "Aerathea.VFX.RuntimeContract": RUNTIME_CONTRACT_DOC,
    "Aerathea.VFX.FixedBoundsContract": FIXED_BOUNDS_CONTRACT,
    "Aerathea.VFX.ReadabilityBudget": READABILITY_BUDGET,
}


REQUIRED_FLOOR_SOCKETS = [
    "vfx_center",
    "vfx_ring_active",
    "vfx_rejected_gap",
    "snap_altar",
]


REQUIRED_BRAND_STATE_INSTANCES = [
    "MI_INF_BrandGlowStates_A01_Inactive",
    "MI_INF_BrandGlowStates_A01_Smolder",
    "MI_INF_BrandGlowStates_A01_TrialActive",
    "MI_INF_BrandGlowStates_A01_Accepted",
    "MI_INF_BrandGlowStates_A01_Rejected",
    "MI_INF_BrandGlowStates_A01_SorcererFocus",
]


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


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


def validate_asset_group(failures, base_path, asset_names):
    loaded = []
    for asset_name in asset_names:
        asset_path = "{}/{}".format(base_path, asset_name)
        asset = unreal.load_asset(asset_path)
        if asset is None:
            failures.append("{} failed to load".format(asset_path))
        else:
            loaded.append(asset)
    return loaded


def validate_material_instances(failures):
    parents_by_name = {
        asset.get_name(): asset
        for asset in validate_asset_group(failures, MATERIAL_PATH, REQUIRED_PARENT_MATERIALS)
    }
    instances = validate_asset_group(failures, MATERIAL_INSTANCE_PATH, REQUIRED_MATERIAL_INSTANCES)
    expected_parent_paths = {
        "{}/{}".format(MATERIAL_PATH, parent_name)
        for parent_name in parents_by_name
    }
    for instance in instances:
        parent = None
        try:
            parent = instance.get_editor_property("parent")
        except Exception:
            parent = None
        if parent is None:
            failures.append("{} has no parent material".format(instance.get_path_name()))
            continue
        if asset_path_without_object(parent) not in expected_parent_paths:
            failures.append("{} has unexpected parent {}".format(instance.get_path_name(), parent.get_path_name()))


def validate_floor_socket_contract(failures):
    mesh = unreal.load_asset(FLOOR_MESH_PATH)
    if mesh is None:
        failures.append("{} failed to load".format(FLOOR_MESH_PATH))
        return

    missing_sockets = [
        socket_name
        for socket_name in REQUIRED_FLOOR_SOCKETS
        if mesh.find_socket(unreal.Name(socket_name)) is None
    ]
    if missing_sockets:
        failures.append("{} missing VFX sockets {}".format(FLOOR_MESH_PATH, ", ".join(missing_sockets)))


def main():
    failures = []
    validate_material_instances(failures)
    niagara_systems = validate_asset_group(failures, VFX_PATH, REQUIRED_NIAGARA_SYSTEMS)
    niagara_emitters = validate_asset_group(failures, VFX_PATH, REQUIRED_NIAGARA_EMITTERS)
    for system in niagara_systems:
        validate_polish_metadata(failures, system, EXPECTED_NIAGARA_SYSTEM_METADATA[system.get_name()])
    for emitter in niagara_emitters:
        validate_polish_metadata(failures, emitter, EXPECTED_NIAGARA_EMITTER_METADATA[emitter.get_name()])
    validate_asset_group(failures, MATERIAL_INSTANCE_PATH, REQUIRED_BRAND_STATE_INSTANCES)
    validate_floor_socket_contract(failures)

    if failures:
        raise RuntimeError("Infernal worthiness judgment VFX validation failed: {}".format("; ".join(failures)))

    print(
        "Infernal worthiness judgment VFX validation passed: {} systems, {} emitters, {} material instances, {} floor sockets, {} brand state dependencies, graph-status metadata locked as {} with FinalGraphAuthored={}.".format(
            len(REQUIRED_NIAGARA_SYSTEMS),
            len(REQUIRED_NIAGARA_EMITTERS),
            len(REQUIRED_MATERIAL_INSTANCES),
            len(REQUIRED_FLOOR_SOCKETS),
            len(REQUIRED_BRAND_STATE_INSTANCES),
            GRAPH_STATUS,
            FINAL_GRAPH_AUTHORED,
        )
    )


if __name__ == "__main__":
    main()
