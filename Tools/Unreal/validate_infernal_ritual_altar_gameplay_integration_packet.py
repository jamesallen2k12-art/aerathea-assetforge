from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKET_PATH = ROOT / "docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_INTEGRATION_PACKET.md"
HEADER_PATH = ROOT / "Source/Aerathea/Public/AETInfernalRitualAltarActor.h"
SOURCE_PATH = ROOT / "Source/Aerathea/Private/AETInfernalRitualAltarActor.cpp"


REQUIRED_SECTIONS = [
    "## Purpose",
    "## Source Contracts",
    "## Locked Implementation Inputs",
    "## First Implementation Target",
    "## Gameplay Event Contract",
    "## Attempt Data Model",
    "## UI Routing Contract",
    "## Audio Routing Contract",
    "## Telemetry Contract",
    "## Interaction And Trace Contract",
    "## Retry And Failure Semantics",
    "## Validation Contract",
    "## Approval-Gated Decisions",
    "## Implementation Order",
]


STATES = [
    "Inactive",
    "Smolder",
    "TrialActive",
    "Accepted",
    "Rejected",
    "JudgmentPulse",
    "Cooldown",
]


CALLABLES = [
    "ResetRitual",
    "StartTrial",
    "AdvanceRitual",
    "AcceptSacrifice",
    "RejectSacrifice",
    "TriggerJudgmentPulse",
    "SetTrialProgress",
]


GETTERS = [
    "GetInteractFrontLocation",
    "GetAltarCoreLocation",
    "GetSacrificeMarkLocation",
    "GetBrandTransferLocation",
    "GetRingLinkLocation",
    "GetRejectedGapLocation",
    "GetCurrentUIStateTag",
    "GetCurrentAudioEventName",
    "GetRitualBindingId",
    "GetObjectiveBindingId",
]


EVENTS = [
    "QEvent.INF.WorthinessAltar.Discovered",
    "QEvent.INF.WorthinessAltar.InteractPromptShown",
    "QEvent.INF.WorthinessAltar.AttemptStarted",
    "QEvent.INF.WorthinessAltar.ProgressUpdated",
    "QEvent.INF.WorthinessAltar.JudgmentPulseStarted",
    "QEvent.INF.WorthinessAltar.VerdictAccepted",
    "QEvent.INF.WorthinessAltar.VerdictRejected",
    "QEvent.INF.WorthinessAltar.CooldownStarted",
    "QEvent.INF.WorthinessAltar.AttemptReset",
]


DATA_KEYS = [
    "RitualAttemptId",
    "RitualBindingId",
    "ObjectiveBindingId",
    "QuestRouteId",
    "AltarActorName",
    "RitualState",
    "CurrentUIStateTag",
    "CurrentAudioEventName",
    "TrialProgress",
    "JudgmentIntensity",
    "RejectedSeverity",
    "CooldownAlpha",
    "ElapsedTrialSeconds",
    "Verdict",
    "FailureReason",
]


APPROVAL_TERMS = [
    "final quest title",
    "success rewards",
    "failure penalties",
    "multiplayer authority model",
    "backend/vendor assumptions",
    "analytics vendor schema",
    "final UI art",
    "final audio middleware",
    "voiceover",
    "WorthinessJudgment bespoke Niagara graph",
]


def require_file(path):
    if not path.exists():
        raise RuntimeError(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def require_terms(text, terms, label):
    missing = [term for term in terms if term not in text]
    if missing:
        raise RuntimeError(f"{label} missing required terms: {', '.join(missing)}")


def main():
    packet = require_file(PACKET_PATH)
    native_text = require_file(HEADER_PATH) + "\n" + require_file(SOURCE_PATH)

    require_terms(packet, REQUIRED_SECTIONS, "Gameplay integration packet")
    require_terms(packet, STATES, "Gameplay integration packet")
    require_terms(packet, CALLABLES, "Gameplay integration packet")
    require_terms(packet, GETTERS, "Gameplay integration packet")
    require_terms(packet, EVENTS, "Gameplay integration packet")
    require_terms(packet, DATA_KEYS, "Gameplay integration packet")
    require_terms(packet, APPROVAL_TERMS, "Gameplay integration packet")

    require_terms(native_text, CALLABLES, "Native ritual altar actor")
    require_terms(native_text, GETTERS, "Native ritual altar actor")
    require_terms(
        native_text,
        [
            "bBindingHooksEnabled",
            "Ritual_INF_CullingTrial_A01",
            "OBJ_INF_ProveWorth_A01",
            "UI.INF.RitualAltar",
            "Audio.INF.RitualAltar",
            "OnRitualBindingStateChanged",
            "OnRitualVerdictResolved",
        ],
        "Native ritual altar actor",
    )

    for state in STATES:
        require_terms(packet, [f"UI.INF.RitualAltar.{state}", f"Audio.INF.RitualAltar.{state}"], f"{state} routing")

    if "JudgmentPulse` is a transition event and must not complete the quest or grant rewards" not in packet:
        raise RuntimeError("Gameplay integration packet must explicitly prevent JudgmentPulse from granting success")

    if "This packet does not implement runtime code" not in packet:
        raise RuntimeError("Gameplay integration packet must state that it is docs-only")

    print(
        "Infernal ritual altar gameplay integration packet validation passed: "
        f"{len(STATES)} states, {len(EVENTS)} gameplay events, {len(DATA_KEYS)} data keys, "
        f"{len(GETTERS)} getters."
    )


if __name__ == "__main__":
    main()
