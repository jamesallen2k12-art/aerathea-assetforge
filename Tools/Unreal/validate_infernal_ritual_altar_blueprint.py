import math

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
BLUEPRINT_PATH = "/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01"
ALTAR_ACTOR_LABEL = "AET_PROD_INF_WorthinessAltar_A01"
FLOOR_ACTOR_LABEL = "AET_PROD_INF_CullingTrialFloor_A01"
ALTAR_MESH_PATH = "/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01"
SNAP_DISTANCE_TOLERANCE_CM = 2.0
ACTOR_SCALE_TOLERANCE = 0.01


EXPECTED_MATERIALS = {
    "BrandGlowInactiveMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Inactive",
    "BrandGlowSmolderMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Smolder",
    "BrandGlowTrialActiveMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_TrialActive",
    "BrandGlowAcceptedMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Accepted",
    "BrandGlowRejectedMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Rejected",
    "BrandGlowJudgmentPulseMaterial": "/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_SorcererFocus",
}


EXPECTED_NIAGARA = {
    "InactiveNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Inactive_A01",
    "SmolderNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Smolder_A01",
    "TrialActiveNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_TrialActive_A01",
    "AcceptedNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Accepted_A01",
    "RejectedNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_Rejected_A01",
    "JudgmentPulseNiagaraSystem": "/Game/Aerathea/VFX/Infernals/WorthinessJudgment/NS_INF_Worthiness_JudgmentPulse_A01",
}


EXPECTED_COMPONENTS = [
    "AltarMesh",
    "InteractionVolume",
    "InteractFrontLocator",
    "AltarCoreLocator",
    "SacrificeMarkLocator",
    "BrandTransferLocator",
    "RingLinkLocator",
    "RejectedGapLocator",
    "WorthinessNiagara",
]

EXPECTED_BINDINGS = {
    "RitualBindingId": "Ritual_INF_CullingTrial_A01",
    "ObjectiveBindingId": "OBJ_INF_ProveWorth_A01",
    "UIStatePrefix": "UI.INF.RitualAltar",
    "AudioEventPrefix": "Audio.INF.RitualAltar",
}


def asset_path_without_object(asset):
    return asset.get_path_name().split(".", 1)[0]


def material_matches_expected(material, expected_path):
    if material is None:
        return False
    if asset_path_without_object(material) == expected_path:
        return True
    expected_name = expected_path.rsplit("/", 1)[-1]
    return expected_name in material.get_name()


def name_matches_expected(value, expected):
    if hasattr(value, "name"):
        value = value.name
    return str(value) == expected


def all_level_actors():
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    if actor_subsystem is not None:
        return list(actor_subsystem.get_all_level_actors())
    return list(unreal.EditorLevelLibrary.get_all_level_actors())


def actors_by_label():
    return {actor.get_actor_label(): actor for actor in all_level_actors()}


def try_call(obj, method_name):
    method = getattr(obj, method_name, None)
    if not callable(method):
        return None
    try:
        return method()
    except Exception:
        return None


def vector_distance(a, b):
    return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z - b.z) ** 2))


def vector_radius(vector):
    return math.sqrt((vector.x * vector.x) + (vector.y * vector.y) + (vector.z * vector.z))


def approx(value, target, tolerance):
    return abs(value - target) <= tolerance


def component_by_name(actor, component_class, expected_name):
    for component in actor.get_components_by_class(component_class):
        name = component.get_name()
        if name == expected_name or name.startswith("{}_".format(expected_name)):
            return component
    return None


def any_component_by_name(actor, expected_name):
    for component in actor.get_components_by_class(unreal.ActorComponent):
        name = component.get_name()
        if name == expected_name or name.startswith("{}_".format(expected_name)):
            return component
    return None


def static_mesh_component_mesh(component):
    mesh = try_call(component, "get_static_mesh")
    if mesh is not None:
        return mesh
    try:
        return component.get_editor_property("static_mesh")
    except Exception:
        return None


def floor_snap_location(label_to_actor):
    floor = label_to_actor.get(FLOOR_ACTOR_LABEL)
    if floor is None:
        return None
    component = floor.get_component_by_class(unreal.StaticMeshComponent)
    if component is None:
        return None
    socket_name = unreal.Name("snap_altar")
    try:
        if component.does_socket_exist(socket_name):
            return component.get_socket_location(socket_name)
    except Exception:
        return None
    return None


def validate_asset_references(actor, failures):
    for prop_name, expected_path in EXPECTED_MATERIALS.items():
        try:
            material = actor.get_editor_property(prop_name)
        except Exception as exc:
            failures.append("missing material property {} ({})".format(prop_name, exc))
            continue
        if material is None:
            failures.append("{} is not assigned".format(prop_name))
        elif asset_path_without_object(material) != expected_path:
            failures.append("{} is {}, expected {}".format(prop_name, material.get_path_name(), expected_path))

    for prop_name, expected_path in EXPECTED_NIAGARA.items():
        try:
            system = actor.get_editor_property(prop_name)
        except Exception as exc:
            failures.append("missing Niagara property {} ({})".format(prop_name, exc))
            continue
        if system is None:
            failures.append("{} is not assigned".format(prop_name))
        elif asset_path_without_object(system) != expected_path:
            failures.append("{} is {}, expected {}".format(prop_name, system.get_path_name(), expected_path))


def validate_ranged_properties(actor, failures):
    ranged_properties = {
        "TrialProgress": (0.0, 1.0),
        "JudgmentIntensity": (0.0, 1.0),
        "RejectedSeverity": (0.0, 1.0),
        "TrialDurationSeconds": (0.05, 60.0),
        "JudgmentPulseSeconds": (0.05, 10.0),
        "CooldownSeconds": (0.05, 30.0),
        "InteractionRadiusCm": (0.0, 1000.0),
        "InteractionDepthCm": (0.0, 1000.0),
    }
    for prop_name, (min_value, max_value) in ranged_properties.items():
        try:
            value = float(actor.get_editor_property(prop_name))
        except Exception as exc:
            failures.append("missing property {} ({})".format(prop_name, exc))
            continue
        if value < min_value or value > max_value:
            failures.append("{} value {:.2f} is outside {:.2f}-{:.2f}".format(prop_name, value, min_value, max_value))

    try:
        slot_index = int(actor.get_editor_property("BrandGlowMaterialSlotIndex"))
        if slot_index != 4:
            failures.append("BrandGlowMaterialSlotIndex is {}, expected 4".format(slot_index))
    except Exception as exc:
        failures.append("missing BrandGlowMaterialSlotIndex ({})".format(exc))


def validate_binding_properties(actor, failures):
    try:
        binding_enabled = bool(actor.get_editor_property("bBindingHooksEnabled"))
        if not binding_enabled:
            failures.append("bBindingHooksEnabled is false, expected true for first binding contract")
    except Exception as exc:
        failures.append("missing bBindingHooksEnabled ({})".format(exc))

    for prop_name, expected_value in EXPECTED_BINDINGS.items():
        try:
            value = actor.get_editor_property(prop_name)
        except Exception as exc:
            failures.append("missing binding property {} ({})".format(prop_name, exc))
            continue
        if not name_matches_expected(value, expected_value):
            failures.append("{} is {}, expected {}".format(prop_name, value, expected_value))

    for prop_name in ("CurrentUIStateTag", "CurrentAudioEventName"):
        try:
            value = actor.get_editor_property(prop_name)
        except Exception as exc:
            failures.append("missing live binding property {} ({})".format(prop_name, exc))
            continue
        if "RitualAltar" not in str(value):
            failures.append("{} is {}, expected RitualAltar tag".format(prop_name, value))


def validate_actor(failures, measurements):
    if not unreal.EditorAssetLibrary.does_asset_exist(BLUEPRINT_PATH):
        failures.append("{} is missing".format(BLUEPRINT_PATH))

    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    label_to_actor = actors_by_label()
    actor = label_to_actor.get(ALTAR_ACTOR_LABEL)
    if actor is None:
        failures.append("{} missing from {}".format(ALTAR_ACTOR_LABEL, LEVEL_PATH))
        return

    class_name = actor.get_class().get_name()
    if "BP_INF_RitualAltar_A01" not in class_name and "AETInfernalRitualAltarActor" not in class_name:
        failures.append("{} has unexpected class {}".format(ALTAR_ACTOR_LABEL, class_name))

    scale = actor.get_actor_scale3d()
    if not (
        approx(scale.x, 1.0, ACTOR_SCALE_TOLERANCE)
        and approx(scale.y, 1.0, ACTOR_SCALE_TOLERANCE)
        and approx(scale.z, 1.0, ACTOR_SCALE_TOLERANCE)
    ):
        failures.append("{} actor scale is {}, expected 1,1,1".format(ALTAR_ACTOR_LABEL, scale))

    snap_location = floor_snap_location(label_to_actor)
    if snap_location is not None:
        actor_location = actor.get_actor_location()
        snap_distance = vector_distance(actor_location, snap_location)
        if snap_distance > SNAP_DISTANCE_TOLERANCE_CM:
            failures.append("{} is {:.2f} cm from floor snap_altar".format(ALTAR_ACTOR_LABEL, snap_distance))

    for component_name in EXPECTED_COMPONENTS:
        if any_component_by_name(actor, component_name) is None:
            failures.append("missing component {}".format(component_name))

    mesh_component = component_by_name(actor, unreal.StaticMeshComponent, "AltarMesh")
    if mesh_component is None:
        failures.append("missing AltarMesh StaticMeshComponent")
    else:
        mesh = static_mesh_component_mesh(mesh_component)
        if mesh is None:
            failures.append("AltarMesh has no static mesh")
        elif asset_path_without_object(mesh) != ALTAR_MESH_PATH:
            failures.append("AltarMesh uses {}, expected {}".format(mesh.get_path_name(), ALTAR_MESH_PATH))

        state_material = mesh_component.get_material(4)
        if state_material is None:
            failures.append("AltarMesh material slot 4 is empty")
        elif not any(material_matches_expected(state_material, expected_path) for expected_path in EXPECTED_MATERIALS.values()):
            failures.append("AltarMesh slot 4 uses {}, expected one of the BrandGlow state materials".format(state_material.get_path_name()))

    niagara_component = component_by_name(actor, unreal.NiagaraComponent, "WorthinessNiagara")
    if niagara_component is None:
        failures.append("missing WorthinessNiagara component")
    else:
        asset = try_call(niagara_component, "get_asset")
        allowed_systems = set(EXPECTED_NIAGARA.values())
        if asset is not None and asset_path_without_object(asset) not in allowed_systems:
            failures.append("WorthinessNiagara uses {}, expected WorthinessJudgment system".format(asset.get_path_name()))

    validate_ranged_properties(actor, failures)
    validate_asset_references(actor, failures)
    validate_binding_properties(actor, failures)

    _origin, extent = actor.get_actor_bounds(False)
    visible_height = extent.z * 2.0
    visible_width = extent.x * 2.0
    visible_depth = extent.y * 2.0
    radius = vector_radius(extent)
    measurements.append((visible_height, visible_width, visible_depth, radius))
    if visible_height < 250.0 or visible_height > 390.0:
        failures.append("{} visible height {:.2f} cm is outside RitualAltar envelope".format(ALTAR_ACTOR_LABEL, visible_height))
    if visible_width < 300.0 or visible_width > 430.0:
        failures.append("{} visible width {:.2f} cm is outside RitualAltar envelope".format(ALTAR_ACTOR_LABEL, visible_width))
    if visible_depth < 170.0 or visible_depth > 390.0:
        failures.append("{} visible depth {:.2f} cm is outside RitualAltar envelope".format(ALTAR_ACTOR_LABEL, visible_depth))
    if radius > 550.0:
        failures.append("{} bounds radius {:.2f} cm exceeds 550 cm".format(ALTAR_ACTOR_LABEL, radius))


def main():
    failures = []
    measurements = []
    validate_actor(failures, measurements)
    if failures:
        raise RuntimeError("Infernal RitualAltar Blueprint validation failed: {}".format("; ".join(failures)))

    visible_height, visible_width, visible_depth, radius = measurements[0]
    print(
        "Infernal RitualAltar Blueprint validation passed: {:.2f}h x {:.2f}w x {:.2f}d cm, bounds radius {:.2f} cm, {} components, {} state materials, {} Niagara systems.".format(
            visible_height,
            visible_width,
            visible_depth,
            radius,
            len(EXPECTED_COMPONENTS),
            len(EXPECTED_MATERIALS),
            len(EXPECTED_NIAGARA),
        )
    )


if __name__ == "__main__":
    main()
