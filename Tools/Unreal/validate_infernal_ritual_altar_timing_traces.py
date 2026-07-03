import math
import re

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
ALTAR_ACTOR_LABEL = "AET_PROD_INF_WorthinessAltar_A01"


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


def require_actor(actors_by_label, label):
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


def assert_state(actor, expected_name):
    value = get_prop(actor, "RitualState")
    if not enum_contains(value, expected_name):
        raise RuntimeError(
            "{} RitualState is {}, expected {}".format(
                actor.get_actor_label(),
                value,
                expected_name,
            )
        )


def assert_bool(actor, prop_name, expected):
    value = bool(get_prop(actor, prop_name))
    if value != expected:
        raise RuntimeError("{} {} is {}, expected {}".format(actor.get_actor_label(), prop_name, value, expected))


def name_string(value):
    if hasattr(value, "name"):
        value = value.name
    return str(value)


def assert_name(actor, prop_name, expected):
    value = name_string(get_prop(actor, prop_name))
    if value != expected:
        raise RuntimeError("{} {} is {}, expected {}".format(actor.get_actor_label(), prop_name, value, expected))


def assert_positive(actor, prop_name):
    value = float(get_prop(actor, prop_name))
    if value <= 0.0:
        raise RuntimeError("{} {} is {:.2f}, expected a positive value".format(actor.get_actor_label(), prop_name, value))
    return value


def assert_range(actor, prop_name, minimum, maximum):
    value = float(get_prop(actor, prop_name))
    if value < minimum or value > maximum:
        raise RuntimeError(
            "{} {} is {:.3f}, expected {:.3f}-{:.3f}".format(
                actor.get_actor_label(),
                prop_name,
                value,
                minimum,
                maximum,
            )
        )
    return value


def assert_approx(actor, prop_name, expected, tolerance):
    value = float(get_prop(actor, prop_name))
    if abs(value - expected) > tolerance:
        raise RuntimeError(
            "{} {} is {:.3f}, expected {:.3f} +/- {:.3f}".format(
                actor.get_actor_label(),
                prop_name,
                value,
                expected,
                tolerance,
            )
        )
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


def assert_binding_tag(actor, expected_suffix):
    ui_tag = name_string(call_actor(actor, "get_current_ui_state_tag", "GetCurrentUIStateTag"))
    audio_event = name_string(call_actor(actor, "get_current_audio_event_name", "GetCurrentAudioEventName"))
    if not ui_tag.endswith(".{}".format(expected_suffix)):
        raise RuntimeError("{} UI tag is {}, expected suffix {}".format(actor.get_actor_label(), ui_tag, expected_suffix))
    if not audio_event.endswith(".{}".format(expected_suffix)):
        raise RuntimeError("{} audio event is {}, expected suffix {}".format(actor.get_actor_label(), audio_event, expected_suffix))


def validate_locator_getters(altar):
    trace_getters = [
        ("interact front", ("get_interact_front_location", "GetInteractFrontLocation"), 450.0),
        ("altar core", ("get_altar_core_location", "GetAltarCoreLocation"), 450.0),
        ("sacrifice mark", ("get_sacrifice_mark_location", "GetSacrificeMarkLocation"), 450.0),
        ("brand transfer", ("get_brand_transfer_location", "GetBrandTransferLocation"), 520.0),
        ("ring link", ("get_ring_link_location", "GetRingLinkLocation"), 450.0),
        ("rejected gap", ("get_rejected_gap_location", "GetRejectedGapLocation"), 450.0),
    ]
    for label, method_names, max_distance in trace_getters:
        assert_trace_location(altar, label, call_actor(altar, *method_names), max_distance)


def validate_timing_flow(altar):
    trial_seconds = assert_positive(altar, "TrialDurationSeconds")
    pulse_seconds = assert_positive(altar, "JudgmentPulseSeconds")
    cooldown_seconds = assert_positive(altar, "CooldownSeconds")
    assert_positive(altar, "InteractionRadiusCm")
    assert_positive(altar, "InteractionDepthCm")
    assert_bool(altar, "bBindingHooksEnabled", True)
    assert_name(altar, "RitualBindingId", "Ritual_INF_CullingTrial_A01")
    assert_name(altar, "ObjectiveBindingId", "OBJ_INF_ProveWorth_A01")
    assert_name(altar, "UIStatePrefix", "UI.INF.RitualAltar")
    assert_name(altar, "AudioEventPrefix", "Audio.INF.RitualAltar")
    ritual_binding_id = name_string(call_actor(altar, "get_ritual_binding_id", "GetRitualBindingId"))
    objective_binding_id = name_string(call_actor(altar, "get_objective_binding_id", "GetObjectiveBindingId"))
    if ritual_binding_id != "Ritual_INF_CullingTrial_A01":
        raise RuntimeError("GetRitualBindingId returned {}, expected Ritual_INF_CullingTrial_A01".format(ritual_binding_id))
    if objective_binding_id != "OBJ_INF_ProveWorth_A01":
        raise RuntimeError("GetObjectiveBindingId returned {}, expected OBJ_INF_ProveWorth_A01".format(objective_binding_id))

    call_actor(altar, "reset_ritual", "ResetRitual")
    assert_state(altar, "Smolder")
    assert_binding_tag(altar, "Smolder")
    assert_approx(altar, "TrialProgress", 0.0, 0.001)
    assert_bool(altar, "bRitualActive", False)

    call_actor(altar, "start_trial", "StartTrial")
    assert_state(altar, "TrialActive")
    assert_binding_tag(altar, "TrialActive")
    assert_bool(altar, "bRitualActive", True)
    assert_approx(altar, "TrialProgress", 0.0, 0.001)

    call_actor(altar, "advance_ritual", "AdvanceRitual", args=(trial_seconds * 0.5,))
    assert_state(altar, "TrialActive")
    assert_range(altar, "TrialProgress", 0.45, 0.55)
    trial_alpha = float(call_actor(altar, "get_trial_alpha", "GetTrialAlpha"))
    if trial_alpha < 0.45 or trial_alpha > 0.55:
        raise RuntimeError("GetTrialAlpha returned {:.3f}, expected around 0.5".format(trial_alpha))

    call_actor(altar, "advance_ritual", "AdvanceRitual", args=(trial_seconds + 0.1,))
    assert_state(altar, "JudgmentPulse")
    assert_binding_tag(altar, "JudgmentPulse")
    assert_bool(altar, "bRitualActive", False)
    assert_approx(altar, "TrialProgress", 1.0, 0.001)

    call_actor(altar, "advance_ritual", "AdvanceRitual", args=(pulse_seconds + 0.1,))
    assert_state(altar, "Cooldown")
    assert_binding_tag(altar, "Cooldown")
    cooldown_alpha = float(call_actor(altar, "get_cooldown_alpha", "GetCooldownAlpha"))
    if cooldown_alpha < 0.0 or cooldown_alpha > 0.05:
        raise RuntimeError("GetCooldownAlpha returned {:.3f}, expected cooldown start".format(cooldown_alpha))

    call_actor(altar, "advance_ritual", "AdvanceRitual", args=(cooldown_seconds + 0.1,))
    assert_state(altar, "Smolder")
    assert_binding_tag(altar, "Smolder")
    assert_approx(altar, "TrialProgress", 0.0, 0.001)
    assert_bool(altar, "bRitualActive", False)


def validate_verdict_flows(altar):
    call_actor(altar, "start_trial", "StartTrial")
    call_actor(altar, "accept_sacrifice", "AcceptSacrifice", args=(0.72,))
    assert_state(altar, "Accepted")
    assert_binding_tag(altar, "Accepted")
    assert_approx(altar, "TrialProgress", 1.0, 0.001)
    assert_approx(altar, "JudgmentIntensity", 0.72, 0.01)
    assert_approx(altar, "RejectedSeverity", 0.0, 0.001)
    assert_bool(altar, "bRitualActive", False)

    call_actor(altar, "reset_ritual", "ResetRitual")
    call_actor(altar, "start_trial", "StartTrial")
    call_actor(altar, "reject_sacrifice", "RejectSacrifice", args=(0.66,))
    assert_state(altar, "Rejected")
    assert_binding_tag(altar, "Rejected")
    assert_approx(altar, "TrialProgress", 1.0, 0.001)
    assert_approx(altar, "JudgmentIntensity", 0.66, 0.01)
    assert_approx(altar, "RejectedSeverity", 0.66, 0.01)
    assert_bool(altar, "bRitualActive", False)

    call_actor(altar, "trigger_judgment_pulse", "TriggerJudgmentPulse", args=(0.88,))
    assert_state(altar, "JudgmentPulse")
    assert_binding_tag(altar, "JudgmentPulse")
    assert_approx(altar, "JudgmentIntensity", 0.88, 0.01)

    call_actor(altar, "reset_ritual", "ResetRitual")
    call_actor(altar, "set_trial_progress", "SetTrialProgress", args=(0.25,))
    assert_state(altar, "TrialActive")
    assert_range(altar, "TrialProgress", 0.24, 0.26)


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actors_by_label = actor_map_by_label()
    altar = require_actor(actors_by_label, ALTAR_ACTOR_LABEL)
    class_name = altar.get_class().get_name()
    if "BP_INF_RitualAltar_A01" not in class_name and "AETInfernalRitualAltarActor" not in class_name:
        raise RuntimeError("{} has unexpected class {}".format(ALTAR_ACTOR_LABEL, class_name))

    validate_locator_getters(altar)
    validate_timing_flow(altar)
    validate_verdict_flows(altar)
    call_actor(altar, "reset_ritual", "ResetRitual")

    print(
        "Infernal ritual altar timing and trace validation passed: trial/cooldown flow, accepted/rejected verdicts, judgment pulse, and 6 locator getters are callable and sane."
    )


if __name__ == "__main__":
    main()
