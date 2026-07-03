# BP_INF_RitualAltar_A01 Gameplay Integration Packet

Last updated: 2026-06-28

## Purpose

Define the first implementation-facing gameplay integration packet for `BP_INF_RitualAltar_A01`.

This packet converts the existing quest/audio/UI binding contract into concrete event names, data keys, UI/audio routing rules, telemetry fields, retry semantics, and validator requirements that can be implemented later without reinterpreting altar state.

This packet does not implement runtime code, final quest text, final rewards, item costs, economy rules, backend authority, voice/cast decisions, final UI art, or final audio assets.

## Source Contracts

- Binding packet: `docs/assets/blueprints/BP_INF_RitualAltar_A01/QUEST_AUDIO_UI_BINDING_PACKET.md`
- Gameplay timing and trace contract: `docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_TIMING_TRACES.md`
- Blueprint implementation handoff: `docs/assets/blueprints/BP_INF_RitualAltar_A01/IMPLEMENTATION_HANDOFF.md`
- Build/import status: `docs/assets/blueprints/BP_INF_RitualAltar_A01/BUILD_IMPORT_STATUS.md`
- Worthiness VFX contract: `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/VFX_POLISH_CONTRACT.md`
- BrandGlow material package: `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`
- Native class: `AAETInfernalRitualAltarActor`
- Native header: `Source/Aerathea/Public/AETInfernalRitualAltarActor.h`
- Native implementation: `Source/Aerathea/Private/AETInfernalRitualAltarActor.cpp`

## Locked Implementation Inputs

The gameplay integration layer must consume these existing names without renaming or duplicating altar state:

| Contract | Locked value |
| --- | --- |
| Blueprint path | `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01` |
| Startup actor | `AET_PROD_INF_WorthinessAltar_A01` |
| Native class | `AAETInfernalRitualAltarActor` |
| Binding enabled flag | `bBindingHooksEnabled = true` |
| Ritual binding id | `Ritual_INF_CullingTrial_A01` |
| Objective binding id | `OBJ_INF_ProveWorth_A01` |
| UI route prefix | `UI.INF.RitualAltar` |
| Audio route prefix | `Audio.INF.RitualAltar` |
| State delegate | `OnRitualBindingStateChanged` |
| Verdict delegate | `OnRitualVerdictResolved` |
| State getter | `GetCurrentUIStateTag()` |
| Audio getter | `GetCurrentAudioEventName()` |
| Ritual id getter | `GetRitualBindingId()` |
| Objective id getter | `GetObjectiveBindingId()` |

Valid altar states:

- `Inactive`
- `Smolder`
- `TrialActive`
- `Accepted`
- `Rejected`
- `JudgmentPulse`
- `Cooldown`

Callable altar controls:

- `ResetRitual`
- `StartTrial`
- `AdvanceRitual`
- `AcceptSacrifice`
- `RejectSacrifice`
- `TriggerJudgmentPulse`
- `SetTrialProgress`

Approved locator getters:

- `GetInteractFrontLocation`
- `GetAltarCoreLocation`
- `GetSacrificeMarkLocation`
- `GetBrandTransferLocation`
- `GetRingLinkLocation`
- `GetRejectedGapLocation`

## First Implementation Target

Recommended future implementation surface:

| Item | Recommendation |
| --- | --- |
| Binding component | `BPC_INF_RitualAltarBinding_A01` |
| Owner | Quest/gameplay layer, not the altar actor |
| Altar reference | `BP_INF_RitualAltar_A01` or `AAETInfernalRitualAltarActor` reference |
| Quest route | `Q_INF_WorthinessTrial_A01` as a placeholder route only |
| Objective route | `OBJ_INF_ProveWorth_A01` |
| Attempt id source | binding layer generated per `StartTrial()` success |
| State authority | consume altar state; do not maintain a second ritual state machine |
| UI/audio routing | derived from `GetCurrentUIStateTag()` and `GetCurrentAudioEventName()` |
| Telemetry adapter | local deterministic adapter first; production analytics/backend schema requires approval |

The binding component should listen to altar delegates and translate them into quest, UI, audio, and telemetry events. It should request altar calls through the native callable controls, then read the resulting state/tags back from the altar.

## Gameplay Event Contract

Use these event names for the first binding implementation:

| Event name | Native source | Required payload | Integration behavior |
| --- | --- | --- | --- |
| `QEvent.INF.WorthinessAltar.Discovered` | player enters discovery/focus range | `RitualBindingId`, `AltarActorName`, `InteractFrontLocation` | reveal the altar objective route if quest rules allow |
| `QEvent.INF.WorthinessAltar.InteractPromptShown` | valid focus while `Inactive` or `Smolder` | `RitualState`, `CurrentUIStateTag`, `InteractFrontLocation` | show one prompt only; do not stack prompts |
| `QEvent.INF.WorthinessAltar.AttemptStarted` | `StartTrial()` succeeds | `RitualAttemptId`, `ObjectiveBindingId`, `TrialDurationSeconds` | start progress tracking and lock duplicate interaction |
| `QEvent.INF.WorthinessAltar.ProgressUpdated` | `OnRitualBindingStateChanged` while `TrialActive` | `RitualAttemptId`, `TrialProgress`, `ElapsedTrialSeconds` | update objective and compact progress UI |
| `QEvent.INF.WorthinessAltar.JudgmentPulseStarted` | state becomes `JudgmentPulse` | `RitualAttemptId`, `JudgmentIntensity`, `JudgmentPulseSeconds` | hold result presentation; this event must not grant success |
| `QEvent.INF.WorthinessAltar.VerdictAccepted` | `OnRitualVerdictResolved(bAccepted=true, ...)` | `RitualAttemptId`, `ObjectiveBindingId`, `JudgmentIntensity` | mark current attempt as successful, then hand off to approval-gated reward logic |
| `QEvent.INF.WorthinessAltar.VerdictRejected` | `OnRitualVerdictResolved(bAccepted=false, ...)` | `RitualAttemptId`, `ObjectiveBindingId`, `JudgmentIntensity`, `RejectedSeverity` | mark current attempt as failed, then enter retry/cooldown handling |
| `QEvent.INF.WorthinessAltar.CooldownStarted` | state becomes `Cooldown` | `RitualAttemptId`, `CooldownSeconds`, `CooldownAlpha` | block interaction and optionally show retry delay |
| `QEvent.INF.WorthinessAltar.AttemptReset` | `ResetRitual()` or cooldown returns to `Smolder` | `RitualAttemptId`, `FailureReason`, `RitualState` | clear transient UI/audio state and unlock retry only when quest rules allow |

`Accepted` and `Rejected` are terminal verdict events for the current attempt. `JudgmentPulse` is a transition event and must not complete the quest or grant rewards by itself.

## Attempt Data Model

The first implementation should use these deterministic data keys:

| Key | Type | Source | Notes |
| --- | --- | --- | --- |
| `RitualAttemptId` | string/name | binding layer | generated once per successful `StartTrial()` |
| `RitualBindingId` | name | `GetRitualBindingId()` | expected `Ritual_INF_CullingTrial_A01` |
| `ObjectiveBindingId` | name | `GetObjectiveBindingId()` | expected `OBJ_INF_ProveWorth_A01` |
| `QuestRouteId` | name | quest layer | placeholder route until final quest naming is approved |
| `AltarActorName` | string | actor label | expected startup actor `AET_PROD_INF_WorthinessAltar_A01` |
| `RitualState` | enum/name | altar actor | one of the seven locked states |
| `CurrentUIStateTag` | name | `GetCurrentUIStateTag()` | derived from `UI.INF.RitualAltar` |
| `CurrentAudioEventName` | name | `GetCurrentAudioEventName()` | derived from `Audio.INF.RitualAltar` |
| `TrialProgress` | float 0-1 | altar actor | validated by timing trace |
| `JudgmentIntensity` | float 0-1 | altar actor | verdict and judgment pulse intensity |
| `RejectedSeverity` | float 0-1 | altar actor | rejection branch only |
| `CooldownAlpha` | float 0-1 | altar actor | retry/cooldown display |
| `ElapsedTrialSeconds` | float | binding layer | used for validation and abandon detection |
| `Verdict` | enum/name | binding layer | `accepted`, `rejected`, `cancelled`, `timeout`, `reset`, or `abandoned` |
| `FailureReason` | enum/name | binding layer | `none`, `cancelled`, `out_of_range`, `interrupted`, `authority_denied`, `timeout`, or `reset` |

Player/account identifiers, analytics vendor IDs, persistence keys, and backend schema are intentionally excluded until approved.

## UI Routing Contract

UI must use `GetCurrentUIStateTag()` and altar fields. It must not run its own ritual state machine.

| Altar state | Required UI route | UI behavior |
| --- | --- | --- |
| `Inactive` | `UI.INF.RitualAltar.Inactive` | hidden or locked prompt, depending on quest phase |
| `Smolder` | `UI.INF.RitualAltar.Smolder` | one interact prompt at `GetInteractFrontLocation()` |
| `TrialActive` | `UI.INF.RitualAltar.TrialActive` | compact progress meter from `TrialProgress` |
| `JudgmentPulse` | `UI.INF.RitualAltar.JudgmentPulse` | suppress interaction; wait for accepted/rejected verdict |
| `Accepted` | `UI.INF.RitualAltar.Accepted` | short success feedback, then quest handoff |
| `Rejected` | `UI.INF.RitualAltar.Rejected` | short failure feedback, then retry/cooldown handoff |
| `Cooldown` | `UI.INF.RitualAltar.Cooldown` | disabled interaction and optional retry countdown |

Final text, localization keys, icons, controller prompts, accessibility copy, and UI animation are approval-gated.

## Audio Routing Contract

Audio should route from `GetCurrentAudioEventName()` to content-specific event keys. The first pass should be one-shot or short-loop only and must be rate-limited by `RitualAttemptId`.

| Altar state | Native audio route | Content event key | Location |
| --- | --- | --- | --- |
| `Inactive` | `Audio.INF.RitualAltar.Inactive` | none by default | none |
| `Smolder` | `Audio.INF.RitualAltar.Smolder` | `SFX_INF_RitualAltar_SmolderLoop_A01` | `GetAltarCoreLocation()` |
| `TrialActive` | `Audio.INF.RitualAltar.TrialActive` | `SFX_INF_RitualAltar_TrialPulse_A01` | `GetAltarCoreLocation()` and `GetRingLinkLocation()` |
| `JudgmentPulse` | `Audio.INF.RitualAltar.JudgmentPulse` | `SFX_INF_RitualAltar_JudgmentPulse_A01` | `GetAltarCoreLocation()` |
| `Accepted` | `Audio.INF.RitualAltar.Accepted` | `SFX_INF_RitualAltar_Accepted_A01` | `GetBrandTransferLocation()` |
| `Rejected` | `Audio.INF.RitualAltar.Rejected` | `SFX_INF_RitualAltar_Rejected_A01` | `GetRejectedGapLocation()` |
| `Cooldown` | `Audio.INF.RitualAltar.Cooldown` | `SFX_INF_RitualAltar_Cooldown_A01` | `GetAltarCoreLocation()` |

Audio middleware, final mix, voiceover, subtitles, and accessibility audio rules remain approval-gated.

## Telemetry Contract

The first pass should log deterministic development telemetry only. It must be local or tool-facing until analytics vendor, backend schema, player identity, retention policy, and privacy rules are approved.

Required telemetry events:

- `Telemetry.INF.WorthinessAltar.AttemptStarted`
- `Telemetry.INF.WorthinessAltar.ProgressSample`
- `Telemetry.INF.WorthinessAltar.JudgmentPulse`
- `Telemetry.INF.WorthinessAltar.VerdictAccepted`
- `Telemetry.INF.WorthinessAltar.VerdictRejected`
- `Telemetry.INF.WorthinessAltar.AttemptReset`
- `Telemetry.INF.WorthinessAltar.CooldownStarted`

Rules:

- `JudgmentPulse` must not complete the quest or grant rewards.
- `Accepted` is the only success branch in this packet.
- `Rejected`, `cancelled`, `timeout`, `reset`, and `abandoned` are attempt outcomes, not success completions.
- Repeated verdict, audio, UI, and telemetry events must be de-duplicated by `RitualAttemptId`.
- No account ID, player ID, or backend persistence key should be added until approval.

## Interaction And Trace Contract

Use altar locators for all player-facing anchors:

| Need | Locator |
| --- | --- |
| Prompt anchor and interact focus | `GetInteractFrontLocation()` |
| Core VFX/audio pulse | `GetAltarCoreLocation()` |
| Sacrifice/target mark | `GetSacrificeMarkLocation()` |
| Accepted brand transfer | `GetBrandTransferLocation()` |
| Trial ring link | `GetRingLinkLocation()` |
| Rejected snap and failure feedback | `GetRejectedGapLocation()` |

The first gameplay implementation should validate that all locator getters return finite world-space vectors before UI, audio, VFX, or quest traces use them.

## Retry And Failure Semantics

- `StartTrial()` creates one active attempt if the altar enters `TrialActive`.
- `TrialActive` blocks duplicate interaction requests.
- `JudgmentPulse` blocks interaction and waits for verdict resolution.
- `Accepted` completes the current attempt only; reward grant remains approval-gated.
- `Rejected` fails the current attempt and may unlock retry only after `Cooldown`.
- `Cooldown` suppresses interaction prompts until the altar returns to `Smolder`.
- `ResetRitual()` clears transient attempt data and records `FailureReason = reset` unless called as normal cooldown cleanup.
- Leaving range, cancellation, combat interruption, group credit, health sacrifice, item sacrifice, death penalty, and respawn rules are not locked by this packet.

Recommended first pass for out-of-range during `TrialActive`: cancel to `ResetRitual()` with `FailureReason = out_of_range`, no reward, and no penalty. This remains approval-gated before production.

## Validation Contract

Current validation expected for this docs-only packet:

- `Tools/Unreal/validate_infernal_ritual_altar_gameplay_integration_packet.py`
- `Tools/Unreal/validate_infernal_ritual_altar_blueprint.py`
- `Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py`
- `git diff --check`
- `python Tools/Agents/validate_agent_workflow.py` after task-board edits

Future implementation validation should additionally confirm:

- binding component or gameplay layer listens to `OnRitualBindingStateChanged`;
- accepted/rejected branches listen to `OnRitualVerdictResolved`;
- all nine `QEvent.INF.WorthinessAltar.*` names are present;
- UI maps all seven altar states exactly once;
- audio route tags map to the content event keys without stacking duplicate one-shots;
- telemetry never grants success on `JudgmentPulse`;
- retry stays blocked during `Cooldown`;
- locator getters are finite before any binding consumer uses them.

## Approval-Gated Decisions

Stop before implementing or locking:

- final quest title, story text, objective copy, and localization keys;
- success rewards, failure penalties, item costs, sacrifice costs, health costs, and economy hooks;
- class-specific altar interactions or class skill identity;
- combat interruption rules, encounter pacing, group participation, and party credit;
- multiplayer authority model, replication rules, persistence rules, and backend/vendor assumptions;
- analytics vendor schema, account/player identifiers, retention policy, and privacy policy;
- final UI art, icons, animation, controller prompts, and accessibility copy;
- final audio middleware, mix targets, voiceover, subtitles, and cast decisions;
- final WorthinessJudgment bespoke Niagara graph behavior beyond the validated contract.

## Implementation Order

1. Add the gameplay binding component or quest-layer adapter.
2. Resolve the placed altar by `RitualBindingId` or actor reference.
3. Subscribe to `OnRitualBindingStateChanged` and `OnRitualVerdictResolved`.
4. Generate `RitualAttemptId` only after `StartTrial()` succeeds.
5. Route UI from `GetCurrentUIStateTag()` and audio from `GetCurrentAudioEventName()`.
6. Log local deterministic telemetry with no player/account identifiers.
7. Add an implementation validator for event names, state mapping, retry blocking, and verdict handling.
8. Stop for approval before rewards, backend authority, final quest copy, final UI art, final audio, or production telemetry.
