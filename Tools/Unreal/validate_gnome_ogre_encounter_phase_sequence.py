import re

import unreal


LEVEL_PATH = "/Game/Aerathea/Maps/L_Aerathea_Startup"
LABELS = {
    "encounter": "AET_PROD_GNM_OGR_BattlefieldEncounter_A01",
    "shieldwall": "AET_PROD_GNM_HeavyMekShieldwall_A01",
    "pylon": "AET_PROD_OGR_CrudeTekPylon_A01",
    "shaman": "AET_PROD_OgreShaman_A01",
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
    actors = all_level_actors()
    return {actor.get_actor_label(): actor for actor in actors}


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


def assert_float_at_least(actor, prop_name, minimum):
    value = float(get_prop(actor, prop_name))
    if value < minimum:
        raise RuntimeError(
            "{} {} is {:.2f}, expected at least {:.2f}".format(
                actor.get_actor_label(),
                prop_name,
                value,
                minimum,
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


def assert_sequence_phase(encounter, expected_state, expected_index):
    assert_state(encounter, "EncounterState", expected_state)
    review_index = int(get_prop(encounter, "ReviewPhaseIndex"))
    if review_index != expected_index:
        raise RuntimeError(
            "ReviewPhaseIndex is {}, expected {} for {}".format(
                review_index,
                expected_index,
                expected_state,
            )
        )


def main():
    if not unreal.EditorLevelLibrary.load_level(LEVEL_PATH):
        raise RuntimeError("Failed to load level: {}".format(LEVEL_PATH))

    actors_by_label = actor_map_by_label()
    encounter = require_actor(actors_by_label, "encounter")
    shieldwall = require_actor(actors_by_label, "shieldwall")
    pylon = require_actor(actors_by_label, "pylon")
    shaman = require_actor(actors_by_label, "shaman")
    manticore = require_actor(actors_by_label, "manticore")

    prepare_encounter(encounter)

    call_actor(encounter, "start_review_phase_sequence", "StartReviewPhaseSequence")
    assert_sequence_phase(encounter, "GnomeHoldLine", 0)

    sequence_expectations = [
        ("OgreAdvance", 1),
        ("ShieldImpact", 2),
        ("PylonOverload", 3),
        ("CasterReinforcement", 4),
        ("ManticoreInterrupt", 5),
        ("Resolution", 6),
    ]
    for expected_state, expected_index in sequence_expectations:
        call_actor(encounter, "advance_review_phase", "AdvanceReviewPhase")
        assert_sequence_phase(encounter, expected_state, expected_index)
        if expected_state == "ShieldImpact":
            assert_state(shieldwall, "ShieldState", "Impact")
            assert_float_at_least(shieldwall, "ImpactIntensity", 0.6)
        elif expected_state == "PylonOverload":
            assert_state(pylon, "PylonState", "Overload")
            assert_float_at_least(pylon, "OverloadPercent", 0.75)
        elif expected_state == "CasterReinforcement":
            if shaman.is_hidden_ed():
                raise RuntimeError("Ogre Shaman should remain editor-visible for caster reinforcement review")
        elif expected_state == "ManticoreInterrupt":
            assert_state(manticore, "InterruptState", "LeapImpact")
            assert_float_at_least(manticore, "SequenceProgress", 0.7)

    print(
        "Gnome/Ogre encounter phase validation passed: {} phases, shield impact, pylon overload, caster reinforcement, and Manticore interrupt.".format(
            len(sequence_expectations) + 1,
        )
    )


if __name__ == "__main__":
    main()
