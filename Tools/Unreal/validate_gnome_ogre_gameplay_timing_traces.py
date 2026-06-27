import math
import re

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
LABELS = {
    "encounter": "AET_PROD_GNM_OGR_BattlefieldEncounter_A01",
    "pylon": "AET_PROD_OGR_CrudeTekPylon_A01",
    "manticore": "AET_PROD_CRE_Manticore_Interrupt_A01",
}


def normalized(value):
    if hasattr(value, "name"):
        value = value.name
    return re.sub(r"[^a-z0-9]", "", str(value).lower())


def enum_contains(value, expected_name):
    return normalized(expected_name) in normalized(value)


def all_level_actors():
    try:
        actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        if actor_subsystem is not None:
            return actor_subsystem.get_all_level_actors()
    except Exception:
        pass
    return unreal.EditorLevelLibrary.get_all_level_actors()


def actor_map_by_label():
    return {actor.get_actor_label(): actor for actor in all_level_actors()}


def require_actor(actors_by_label, key):
    label = LABELS[key]
    actor = actors_by_label.get(label)
    if actor is None:
        raise RuntimeError("Missing required actor label: {}".format(label))
    return actor


def call_actor(actor, *method_names, args=()):
    for method_name in method_names:
        method = getattr(actor, method_name, None)
        if callable(method):
            return method(*args)
    raise RuntimeError(
        "{} is missing expected method {}".format(
            actor.get_actor_label(),
            " or ".join(method_names),
        )
    )


def get_prop(actor, prop_name):
    try:
        return actor.get_editor_property(prop_name)
    except Exception as exc:
        raise RuntimeError("{} missing property {} ({})".format(actor.get_actor_label(), prop_name, exc))


def set_prop(actor, prop_name, value):
    try:
        actor.set_editor_property(prop_name, value)
    except Exception as exc:
        raise RuntimeError("{} could not set property {} ({})".format(actor.get_actor_label(), prop_name, exc))


def assert_state(actor, prop_name, expected_name):
    value = get_prop(actor, prop_name)
    if not enum_contains(value, expected_name):
        raise RuntimeError(
            "{} {} is {}, expected {}".format(
                actor.get_actor_label(),
                prop_name,
                value,
                expected_name,
            )
        )


def assert_positive(actor, prop_name):
    value = float(get_prop(actor, prop_name))
    if value <= 0.0:
        raise RuntimeError("{} {} is {:.2f}, expected a positive value".format(actor.get_actor_label(), prop_name, value))
    return value


def vector_distance(a, b):
    return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z - b.z) ** 2))


def assert_trace_location(actor, label, vector, max_distance_cm):
    if vector is None or not hasattr(vector, "x") or not hasattr(vector, "y") or not hasattr(vector, "z"):
        raise RuntimeError("{} returned invalid trace location for {}".format(actor.get_actor_label(), label))
    values = (float(vector.x), float(vector.y), float(vector.z))
    if not all(math.isfinite(value) for value in values):
        raise RuntimeError("{} returned non-finite trace location {}: {}".format(actor.get_actor_label(), label, values))
    distance = vector_distance(vector, actor.get_actor_location())
    if distance > max_distance_cm:
        raise RuntimeError(
            "{} {} trace is {:.1f} cm from the actor, expected within {:.1f} cm".format(
                actor.get_actor_label(),
                label,
                distance,
                max_distance_cm,
            )
        )


def assert_bool_result(actor, expected, *method_names):
    value = bool(call_actor(actor, *method_names))
    if value != expected:
        raise RuntimeError(
            "{} {} returned {}, expected {}".format(
                actor.get_actor_label(),
                " or ".join(method_names),
                value,
                expected,
            )
        )


def prepare_encounter(encounter):
    set_prop(encounter, "bAutoStart", False)
    set_prop(encounter, "bAutoAdvanceReviewPhases", False)
    set_prop(encounter, "bLoopForReview", False)

    validate = getattr(encounter, "validate_dependencies", None)
    if callable(validate) and not validate():
        raise RuntimeError(
            "Encounter dependencies failed: {}".format(
                get_prop(encounter, "LastValidationReport"),
            )
        )

    call_actor(encounter, "reset_encounter", "ResetEncounter")
    assert_state(encounter, "EncounterState", "Setup")


def validate_pylon_timing(encounter, pylon):
    assert_positive(pylon, "DamageWindowSeconds")
    assert_positive(pylon, "RepairWindowSeconds")
    assert_positive(pylon, "DamageTraceRadiusCm")
    assert_positive(pylon, "RepairTraceRadiusCm")
    assert_positive(pylon, "DamagePerTrace")
    assert_positive(pylon, "RepairPerTrace")

    call_actor(encounter, "trigger_pylon_overload", "TriggerPylonOverload", args=(0.82,))
    assert_state(encounter, "EncounterState", "PylonOverload")
    assert_state(pylon, "PylonState", "Overload")
    assert_bool_result(pylon, True, "is_damage_window_active", "IsDamageWindowActive")

    pylon_trace = call_actor(encounter, "get_pylon_trace_location", "GetPylonTraceLocation")
    assert_trace_location(pylon, "encounter pylon", pylon_trace, 800.0)
    assert_trace_location(pylon, "core", call_actor(pylon, "get_core_trace_location", "GetCoreTraceLocation"), 800.0)
    assert_trace_location(pylon, "top arc", call_actor(pylon, "get_top_arc_trace_location", "GetTopArcTraceLocation"), 900.0)
    assert_trace_location(pylon, "ground sparks", call_actor(pylon, "get_ground_sparks_trace_location", "GetGroundSparksTraceLocation"), 800.0)

    damage_before = float(get_prop(pylon, "DamagePercent"))
    call_actor(encounter, "apply_pylon_damage_trace", "ApplyPylonDamageTrace", args=(1.0,))
    damage_after = float(get_prop(pylon, "DamagePercent"))
    if damage_after <= damage_before:
        raise RuntimeError("Pylon damage trace did not increase DamagePercent")

    damage_window_seconds = float(get_prop(pylon, "DamageWindowSeconds"))
    call_actor(encounter, "advance_branch_timing", "AdvanceBranchTiming", args=(damage_window_seconds + 0.1,))
    assert_bool_result(pylon, False, "is_damage_window_active", "IsDamageWindowActive")

    call_actor(encounter, "begin_pylon_repair_window", "BeginPylonRepairWindow")
    assert_bool_result(pylon, True, "is_repair_window_active", "IsRepairWindowActive")
    damage_before_repair = float(get_prop(pylon, "DamagePercent"))
    call_actor(encounter, "apply_pylon_repair_trace", "ApplyPylonRepairTrace", args=(1.0,))
    damage_after_repair = float(get_prop(pylon, "DamagePercent"))
    if damage_after_repair >= damage_before_repair:
        raise RuntimeError("Pylon repair trace did not reduce DamagePercent")

    repair_window_seconds = float(get_prop(pylon, "RepairWindowSeconds"))
    call_actor(encounter, "advance_branch_timing", "AdvanceBranchTiming", args=(repair_window_seconds + 0.1,))
    assert_bool_result(pylon, False, "is_repair_window_active", "IsRepairWindowActive")


def validate_manticore_timing(encounter, manticore):
    stalk_seconds = assert_positive(manticore, "StalkSeconds")
    telegraph_seconds = assert_positive(manticore, "TelegraphSeconds")
    impact_seconds = assert_positive(manticore, "ImpactSeconds")
    threat_hold_seconds = assert_positive(manticore, "ThreatHoldSeconds")
    retreat_seconds = assert_positive(manticore, "RetreatSeconds")
    assert_positive(manticore, "InterruptTraceRadiusCm")
    assert_positive(manticore, "ImpactDamageRadiusCm")

    call_actor(manticore, "reset_interrupt", "ResetInterrupt")
    call_actor(manticore, "begin_interrupt_sequence", "BeginInterruptSequence")
    assert_state(manticore, "InterruptState", "Stalking")
    assert_bool_result(manticore, True, "is_interrupt_sequence_active", "IsInterruptSequenceActive")

    impact_trace = call_actor(encounter, "get_manticore_impact_trace_location", "GetManticoreImpactTraceLocation")
    assert_trace_location(manticore, "encounter impact", impact_trace, 700.0)
    assert_trace_location(manticore, "entry", call_actor(manticore, "get_entry_trace_location", "GetEntryTraceLocation"), 700.0)
    assert_trace_location(manticore, "impact", call_actor(manticore, "get_impact_trace_location", "GetImpactTraceLocation"), 700.0)
    assert_trace_location(manticore, "retreat", call_actor(manticore, "get_retreat_trace_location", "GetRetreatTraceLocation"), 700.0)

    call_actor(encounter, "advance_branch_timing", "AdvanceBranchTiming", args=(stalk_seconds + 0.01,))
    assert_state(manticore, "InterruptState", "Telegraph")
    call_actor(encounter, "advance_branch_timing", "AdvanceBranchTiming", args=(telegraph_seconds + 0.01,))
    assert_state(manticore, "InterruptState", "LeapImpact")
    assert_bool_result(manticore, True, "is_impact_window_active", "IsImpactWindowActive")

    call_actor(
        encounter,
        "advance_branch_timing",
        "AdvanceBranchTiming",
        args=(impact_seconds + threat_hold_seconds + retreat_seconds + 0.25,),
    )
    assert_state(manticore, "InterruptState", "Retreat")
    assert_bool_result(manticore, False, "is_interrupt_sequence_active", "IsInterruptSequenceActive")


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actors_by_label = actor_map_by_label()
    encounter = require_actor(actors_by_label, "encounter")
    pylon = require_actor(actors_by_label, "pylon")
    manticore = require_actor(actors_by_label, "manticore")

    prepare_encounter(encounter)
    validate_pylon_timing(encounter, pylon)
    call_actor(encounter, "reset_encounter", "ResetEncounter")
    validate_manticore_timing(encounter, manticore)

    print("Gnome/Ogre gameplay timing and trace validation passed: pylon damage/repair windows and Manticore interrupt timeline are callable and sane.")


if __name__ == "__main__":
    main()
