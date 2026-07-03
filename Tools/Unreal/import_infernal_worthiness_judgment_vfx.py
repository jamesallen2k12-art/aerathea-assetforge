import unreal


MATERIAL_PATH = "/Game/Aerathea/Materials/Infernals/VFX"
MATERIAL_INSTANCE_PATH = "/Game/Aerathea/Materials/Instances"
VFX_PATH = "/Game/Aerathea/VFX/Infernals/WorthinessJudgment"

POLISH_TASK_ID = "AET-MA-20260628-002"
GRAPH_STATUS = "template_derived_contract_ready"
FINAL_GRAPH_AUTHORED = "false"
RUNTIME_CONTRACT_DOC = "docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_TIMING_TRACES.md"
READABILITY_BUDGET = "restrained_no_screen_fire_no_dense_smoke"
FIXED_BOUNDS_CONTRACT = "floor_radius_1000cm_altar_height_420cm"

COMMON_USER_PARAMETERS = (
    "User.State",
    "User.JudgmentIntensity",
)


VFX_MATERIAL_SPECS = {
    "Ring": {
        "parent": "M_INF_WorthinessRing_A01",
        "instance": "MI_INF_WorthinessRing_A01",
        "base": unreal.LinearColor(0.95, 0.18, 0.030, 1.0),
        "emissive": unreal.LinearColor(3.8, 0.55, 0.045, 1.0),
        "opacity": 0.54,
        "state_index": 2.0,
        "pulse_intensity": 1.00,
        "pulse_duration": 2.40,
        "ring_radius_cm": 900.0,
        "accepted_focus": 0.15,
        "rejected_snap": 0.0,
        "ash_density": 0.10,
        "blend": "BLEND_ADDITIVE",
        "runtime_binding_ready": 1.0,
        "graph_contract_ready": 1.0,
        "final_graph_authored": 0.0,
        "max_opacity_budget": 0.70,
        "max_ash_density": 0.50,
        "floor_bounds_radius_cm": 1000.0,
        "altar_bounds_height_cm": 420.0,
        "event_pulse_only": 0.0,
    },
    "Sigil": {
        "parent": "M_INF_WorthinessSigil_A01",
        "instance": "MI_INF_WorthinessSigil_A01",
        "base": unreal.LinearColor(1.00, 0.24, 0.040, 1.0),
        "emissive": unreal.LinearColor(4.6, 0.68, 0.060, 1.0),
        "opacity": 0.62,
        "state_index": 2.0,
        "pulse_intensity": 1.18,
        "pulse_duration": 1.65,
        "ring_radius_cm": 220.0,
        "accepted_focus": 0.35,
        "rejected_snap": 0.0,
        "ash_density": 0.08,
        "blend": "BLEND_ADDITIVE",
        "runtime_binding_ready": 1.0,
        "graph_contract_ready": 1.0,
        "final_graph_authored": 0.0,
        "max_opacity_budget": 0.70,
        "max_ash_density": 0.50,
        "floor_bounds_radius_cm": 1000.0,
        "altar_bounds_height_cm": 420.0,
        "event_pulse_only": 0.0,
    },
    "Ash": {
        "parent": "M_INF_WorthinessAsh_A01",
        "instance": "MI_INF_WorthinessAsh_A01",
        "base": unreal.LinearColor(0.20, 0.17, 0.14, 1.0),
        "emissive": unreal.LinearColor(0.50, 0.10, 0.025, 1.0),
        "opacity": 0.30,
        "state_index": 5.0,
        "pulse_intensity": 0.28,
        "pulse_duration": 3.80,
        "ring_radius_cm": 780.0,
        "accepted_focus": 0.0,
        "rejected_snap": 0.0,
        "ash_density": 0.44,
        "blend": "BLEND_TRANSLUCENT",
        "runtime_binding_ready": 1.0,
        "graph_contract_ready": 1.0,
        "final_graph_authored": 0.0,
        "max_opacity_budget": 0.70,
        "max_ash_density": 0.50,
        "floor_bounds_radius_cm": 1000.0,
        "altar_bounds_height_cm": 420.0,
        "event_pulse_only": 0.0,
    },
    "Rejected": {
        "parent": "M_INF_WorthinessRejected_A01",
        "instance": "MI_INF_WorthinessRejected_A01",
        "base": unreal.LinearColor(0.75, 0.035, 0.25, 1.0),
        "emissive": unreal.LinearColor(3.2, 0.08, 2.4, 1.0),
        "opacity": 0.66,
        "state_index": 4.0,
        "pulse_intensity": 1.55,
        "pulse_duration": 0.65,
        "ring_radius_cm": 900.0,
        "accepted_focus": 0.0,
        "rejected_snap": 1.0,
        "ash_density": 0.20,
        "blend": "BLEND_ADDITIVE",
        "runtime_binding_ready": 1.0,
        "graph_contract_ready": 1.0,
        "final_graph_authored": 0.0,
        "max_opacity_budget": 0.70,
        "max_ash_density": 0.50,
        "floor_bounds_radius_cm": 1000.0,
        "altar_bounds_height_cm": 420.0,
        "event_pulse_only": 1.0,
    },
    "JudgmentPulse": {
        "parent": "M_INF_WorthinessJudgmentPulse_A01",
        "instance": "MI_INF_WorthinessJudgmentPulse_A01",
        "base": unreal.LinearColor(1.00, 0.30, 0.055, 1.0),
        "emissive": unreal.LinearColor(5.0, 0.72, 0.12, 1.0),
        "opacity": 0.50,
        "state_index": 6.0,
        "pulse_intensity": 1.35,
        "pulse_duration": 0.95,
        "ring_radius_cm": 900.0,
        "accepted_focus": 0.55,
        "rejected_snap": 0.25,
        "ash_density": 0.18,
        "blend": "BLEND_TRANSLUCENT",
        "runtime_binding_ready": 1.0,
        "graph_contract_ready": 1.0,
        "final_graph_authored": 0.0,
        "max_opacity_budget": 0.70,
        "max_ash_density": 0.50,
        "floor_bounds_radius_cm": 1000.0,
        "altar_bounds_height_cm": 420.0,
        "event_pulse_only": 1.0,
    },
}


NIAGARA_SYSTEM_TARGETS = {
    "NS_INF_Worthiness_Inactive_A01": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
    "NS_INF_Worthiness_Smolder_A01": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
    "NS_INF_Worthiness_TrialActive_A01": "/Niagara/DefaultAssets/Templates/Systems/AttributeReaderTrails",
    "NS_INF_Worthiness_Accepted_A01": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
    "NS_INF_Worthiness_Rejected_A01": "/Niagara/DefaultAssets/Templates/Systems/DirectionalBurst",
    "NS_INF_Worthiness_JudgmentPulse_A01": "/Niagara/DefaultAssets/Templates/Systems/RadialBurst",
}

NIAGARA_SYSTEM_POLISH_SPECS = {
    "NS_INF_Worthiness_Inactive_A01": {
        "state": "Inactive",
        "behavior": "no_particles_or_near_zero_ambient_glow",
        "locator": "vfx_center",
        "user_parameters": COMMON_USER_PARAMETERS + ("User.PulseIntensity",),
    },
    "NS_INF_Worthiness_Smolder_A01": {
        "state": "Smolder",
        "behavior": "low_ember_sparse_ash_only",
        "locator": "vfx_ring_active",
        "user_parameters": COMMON_USER_PARAMETERS + ("User.AshDensity", "User.PulseIntensity"),
    },
    "NS_INF_Worthiness_TrialActive_A01": {
        "state": "TrialActive",
        "behavior": "ring_sigil_pulse_driven_by_trial_progress_and_judgment_intensity",
        "locator": "vfx_ring_active",
        "user_parameters": COMMON_USER_PARAMETERS + ("User.TrialProgress", "User.RingRadiusCm", "User.PulseIntensity"),
    },
    "NS_INF_Worthiness_Accepted_A01": {
        "state": "Accepted",
        "behavior": "warm_focus_from_ring_to_altar_core_or_brand_transfer",
        "locator": "vfx_brand_transfer",
        "user_parameters": COMMON_USER_PARAMETERS + ("User.AcceptedFocus", "User.BrandTransferLocation"),
    },
    "NS_INF_Worthiness_Rejected_A01": {
        "state": "Rejected",
        "behavior": "short_violet_red_snap_to_rejected_gap",
        "locator": "vfx_rejected_gap",
        "user_parameters": COMMON_USER_PARAMETERS + ("User.RejectedSeverity", "User.RejectedGapLocation", "User.RejectedSnap"),
    },
    "NS_INF_Worthiness_JudgmentPulse_A01": {
        "state": "JudgmentPulse",
        "behavior": "short_horned_split_wing_verdict_pulse_then_cooldown",
        "locator": "vfx_altar_core",
        "user_parameters": COMMON_USER_PARAMETERS + ("User.PulseDuration", "User.AltarCoreLocation"),
    },
}


NIAGARA_EMITTER_TARGETS = {
    "NE_INF_WorthinessRingPulse_A01": "/Niagara/DefaultAssets/Templates/Emitters/SingleLoopingParticle",
    "NE_INF_WorthinessSigilPulse_A01": "/Niagara/DefaultAssets/Templates/Emitters/SimpleSpriteBurst",
    "NE_INF_WorthinessAshMote_A01": "/Niagara/DefaultAssets/Templates/Emitters/ConfettiBurst",
    "NE_INF_WorthinessRejectedSnap_A01": "/Niagara/DefaultAssets/Templates/Emitters/StaticBeam",
}

NIAGARA_EMITTER_POLISH_SPECS = {
    "NE_INF_WorthinessRingPulse_A01": {
        "role": "floor_ring_pulse",
        "behavior": "restrained_loop_or_event_ring_read",
        "user_parameters": ("User.State", "User.RingRadiusCm", "User.PulseIntensity"),
    },
    "NE_INF_WorthinessSigilPulse_A01": {
        "role": "central_sigil_pulse",
        "behavior": "low_frequency_horned_split_wing_read",
        "user_parameters": ("User.State", "User.TrialProgress", "User.JudgmentIntensity"),
    },
    "NE_INF_WorthinessAshMote_A01": {
        "role": "sparse_ash_motes",
        "behavior": "density_reduces_before_primary_read",
        "user_parameters": ("User.State", "User.AshDensity"),
    },
    "NE_INF_WorthinessRejectedSnap_A01": {
        "role": "rejected_gap_snap",
        "behavior": "short_violet_red_event_not_persistent_aura",
        "user_parameters": ("User.State", "User.RejectedSeverity", "User.RejectedGapLocation", "User.RejectedSnap"),
    },
}


SCALAR_PARAMETERS = [
    "Opacity",
    "StateIndex",
    "PulseIntensity",
    "PulseDuration",
    "RingRadiusCm",
    "AcceptedFocus",
    "RejectedSnap",
    "AshDensity",
]

CONTRACT_SCALAR_PARAMETERS = [
    "RuntimeBindingReady",
    "GraphContractReady",
    "FinalGraphAuthored",
    "MaxOpacityBudget",
    "MaxAshDensity",
    "FloorBoundsRadiusCm",
    "AltarBoundsHeightCm",
    "EventPulseOnly",
]


SCALAR_PARAMETER_SPEC_KEYS = {
    "StateIndex": "state_index",
    "PulseIntensity": "pulse_intensity",
    "PulseDuration": "pulse_duration",
    "RingRadiusCm": "ring_radius_cm",
    "AcceptedFocus": "accepted_focus",
    "RejectedSnap": "rejected_snap",
    "AshDensity": "ash_density",
}

CONTRACT_SCALAR_PARAMETER_SPEC_KEYS = {
    "RuntimeBindingReady": "runtime_binding_ready",
    "GraphContractReady": "graph_contract_ready",
    "FinalGraphAuthored": "final_graph_authored",
    "MaxOpacityBudget": "max_opacity_budget",
    "MaxAshDensity": "max_ash_density",
    "FloorBoundsRadiusCm": "floor_bounds_radius_cm",
    "AltarBoundsHeightCm": "altar_bounds_height_cm",
    "EventPulseOnly": "event_pulse_only",
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


def ensure_contract_scalar_parameters(material, spec):
    for index, parameter_name in enumerate(CONTRACT_SCALAR_PARAMETERS):
        if material_has_scalar_parameter(material, parameter_name):
            continue
        create_scalar_parameter(
            material,
            parameter_name,
            spec[CONTRACT_SCALAR_PARAMETER_SPEC_KEYS[parameter_name]],
            160,
            -260 + (index * 80),
        )


def create_vfx_material(spec):
    ensure_directory(MATERIAL_PATH)
    asset_path = "{}/{}".format(MATERIAL_PATH, spec["parent"])
    existing = unreal.load_asset(asset_path)
    if existing is not None:
        ensure_contract_scalar_parameters(existing, spec)
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

    base = create_vector_parameter(material, "BaseColor", spec["base"], -620, -240)
    connect_property(base, "MP_BASE_COLOR")

    emissive = create_vector_parameter(material, "EmissiveColor", spec["emissive"], -620, -40)
    connect_property(emissive, "MP_EMISSIVE_COLOR")

    opacity = create_scalar_parameter(material, "Opacity", spec["opacity"], -620, 160)
    connect_property(opacity, "MP_OPACITY")

    for index, parameter_name in enumerate(SCALAR_PARAMETERS[1:], start=1):
        create_scalar_parameter(
            material,
            parameter_name,
            spec[SCALAR_PARAMETER_SPEC_KEYS[parameter_name]],
            -220,
            -260 + (index * 80),
        )

    ensure_contract_scalar_parameters(material, spec)
    configure_vfx_material(material, spec["blend"])
    unreal.EditorAssetLibrary.save_asset(asset_path)
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
    mat_lib.set_material_instance_vector_parameter_value(instance, "BaseColor", spec["base"])
    mat_lib.set_material_instance_vector_parameter_value(instance, "EmissiveColor", spec["emissive"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "Opacity", spec["opacity"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "StateIndex", spec["state_index"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "PulseIntensity", spec["pulse_intensity"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "PulseDuration", spec["pulse_duration"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "RingRadiusCm", spec["ring_radius_cm"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "AcceptedFocus", spec["accepted_focus"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "RejectedSnap", spec["rejected_snap"])
    mat_lib.set_material_instance_scalar_parameter_value(instance, "AshDensity", spec["ash_density"])
    for parameter_name, spec_key in CONTRACT_SCALAR_PARAMETER_SPEC_KEYS.items():
        mat_lib.set_material_instance_scalar_parameter_value(instance, parameter_name, spec[spec_key])
    unreal.EditorAssetLibrary.save_loaded_asset(instance)
    return instance


def ensure_vfx_materials():
    for spec in VFX_MATERIAL_SPECS.values():
        parent = create_vfx_material(spec)
        ensure_material_instance(spec["instance"], parent, spec)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_PATH, only_if_is_dirty=False, recursive=True)
    unreal.EditorAssetLibrary.save_directory(MATERIAL_INSTANCE_PATH, only_if_is_dirty=False, recursive=True)


def metadata_user_parameters(parameters):
    return ",".join(parameters)


def common_asset_metadata(template_asset_path):
    return {
        "Aerathea.VFX.PolishTask": POLISH_TASK_ID,
        "Aerathea.VFX.GraphStatus": GRAPH_STATUS,
        "Aerathea.VFX.FinalGraphAuthored": FINAL_GRAPH_AUTHORED,
        "Aerathea.VFX.TemplateSource": template_asset_path,
        "Aerathea.VFX.RuntimeContract": RUNTIME_CONTRACT_DOC,
        "Aerathea.VFX.FixedBoundsContract": FIXED_BOUNDS_CONTRACT,
        "Aerathea.VFX.ReadabilityBudget": READABILITY_BUDGET,
    }


def niagara_system_metadata(asset_name, template_asset_path):
    spec = NIAGARA_SYSTEM_POLISH_SPECS[asset_name]
    metadata = common_asset_metadata(template_asset_path)
    metadata.update(
        {
            "Aerathea.VFX.AssetRole": "system",
            "Aerathea.VFX.State": spec["state"],
            "Aerathea.VFX.BehaviorContract": spec["behavior"],
            "Aerathea.VFX.LocatorContract": spec["locator"],
            "Aerathea.VFX.UserParameters": metadata_user_parameters(spec["user_parameters"]),
        }
    )
    return metadata


def niagara_emitter_metadata(asset_name, template_asset_path):
    spec = NIAGARA_EMITTER_POLISH_SPECS[asset_name]
    metadata = common_asset_metadata(template_asset_path)
    metadata.update(
        {
            "Aerathea.VFX.AssetRole": "emitter",
            "Aerathea.VFX.EmitterRole": spec["role"],
            "Aerathea.VFX.BehaviorContract": spec["behavior"],
            "Aerathea.VFX.UserParameters": metadata_user_parameters(spec["user_parameters"]),
        }
    )
    return metadata


def apply_asset_metadata(asset, metadata):
    setter = getattr(unreal.EditorAssetLibrary, "set_metadata_tag", None)
    if not callable(setter):
        raise RuntimeError("EditorAssetLibrary.set_metadata_tag is unavailable; cannot stamp VFX polish contract metadata")

    for tag, value in metadata.items():
        setter(asset, tag, str(value))


def duplicate_template_asset(target_asset_path, template_asset_path, metadata):
    package_path, asset_name = target_asset_path.rsplit("/", 1)
    ensure_directory(package_path)

    existing = unreal.load_asset(target_asset_path)
    if existing is not None:
        apply_asset_metadata(existing, metadata)
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

    apply_asset_metadata(duplicated, metadata)
    unreal.EditorAssetLibrary.save_loaded_asset(duplicated)
    unreal.log("Created template-derived Niagara asset {} from {}.".format(target_asset_path, template_asset_path))
    return duplicated


def ensure_niagara_assets():
    for asset_name, template_path in NIAGARA_SYSTEM_TARGETS.items():
        duplicate_template_asset(
            "{}/{}".format(VFX_PATH, asset_name),
            template_path,
            niagara_system_metadata(asset_name, template_path),
        )
    for asset_name, template_path in NIAGARA_EMITTER_TARGETS.items():
        duplicate_template_asset(
            "{}/{}".format(VFX_PATH, asset_name),
            template_path,
            niagara_emitter_metadata(asset_name, template_path),
        )
    unreal.EditorAssetLibrary.save_directory(VFX_PATH, only_if_is_dirty=False, recursive=True)


def main():
    ensure_directory(MATERIAL_PATH)
    ensure_directory(MATERIAL_INSTANCE_PATH)
    ensure_directory(VFX_PATH)
    ensure_vfx_materials()
    ensure_niagara_assets()
    unreal.log("Aerathea Infernal worthiness judgment VFX first-pass assets complete.")


main()
