# BP_INF_RitualAltar_A01 Implementation Handoff

## Purpose

Wrap `SM_INF_WorthinessAltar_A01` in a reusable native-backed Blueprint Actor that owns ritual state, altar interaction, BrandGlow state materials, WorthinessJudgment VFX routing, quest/audio/UI binding hooks, and validated startup placement.

## Source References

- Kit breakdown: `docs/assets/kits/KIT_INF_BalgorothCult_A01/VISUAL_KIT_BREAKDOWN.md`
- Static mesh package: `docs/assets/props/SM_INF_WorthinessAltar_A01/PRODUCTION_PACKAGE.md`
- VFX package: `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/PRODUCTION_PACKAGE.md`
- Material package: `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`
- Binding packet: `docs/assets/blueprints/BP_INF_RitualAltar_A01/QUEST_AUDIO_UI_BINDING_PACKET.md`
- Gameplay integration packet: `docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_INTEGRATION_PACKET.md`

## Native Files

- Header: `Source/Aerathea/Public/AETInfernalRitualAltarActor.h`
- Implementation: `Source/Aerathea/Private/AETInfernalRitualAltarActor.cpp`
- Blueprint authoring: `Tools/Unreal/create_infernal_ritual_altar_blueprint.py`
- Gameplay timing/trace validation: `Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py`

## Blueprint Components

| Component | Type | Notes |
| --- | --- | --- |
| `SceneRoot` | Scene Component | actor root at altar snap point |
| `AltarMesh` | Static Mesh Component | uses `SM_INF_WorthinessAltar_A01` |
| `InteractionVolume` | Box Component | hidden overlap helper, front-facing |
| `InteractFrontLocator` | Scene Component | interaction prompt and player-facing point |
| `AltarCoreLocator` | Scene Component | central basin and core pulse |
| `SacrificeMarkLocator` | Scene Component | top/front mark target |
| `BrandTransferLocator` | Scene Component | backplate-to-character brand transfer |
| `RingLinkLocator` | Scene Component | floor ring link |
| `RejectedGapLocator` | Scene Component | rejected-state crack/snap target |
| `WorthinessNiagara` | Niagara Component | active system selected by ritual state |

## State Contract

| State | Material/VFX read | Gameplay use |
| --- | --- | --- |
| `Inactive` | dark channels, no active Niagara by default | dormant altar |
| `Smolder` | low ember state | idle review state |
| `TrialActive` | ring/core pulse | active judgment window |
| `Accepted` | warm focused ember | success response |
| `Rejected` | violet-red snap | failure response |
| `JudgmentPulse` | short bright pulse | verdict transition |
| `Cooldown` | dim return to smolder | reset window |

## Data Parameters

- `RitualState`
- `TrialProgress`: `0.0-1.0`
- `JudgmentIntensity`: `0.0-1.0`
- `RejectedSeverity`: `0.0-1.0`
- `TrialDurationSeconds`: default `8.0`
- `JudgmentPulseSeconds`: default `1.25`
- `CooldownSeconds`: default `2.5`
- `InteractionRadiusCm`: default `170.0`
- `InteractionDepthCm`: default `90.0`
- `BrandGlowMaterialSlotIndex`: default `4`
- `bUseNiagara`
- `bShowInteractionVolume`
- `bBindingHooksEnabled`: default `true`
- `RitualBindingId`: default `Ritual_INF_CullingTrial_A01`
- `ObjectiveBindingId`: default `OBJ_INF_ProveWorth_A01`
- `UIStatePrefix`: default `UI.INF.RitualAltar`
- `AudioEventPrefix`: default `Audio.INF.RitualAltar`
- `CurrentUIStateTag`: live state tag, derived from `UIStatePrefix` and `RitualState`
- `CurrentAudioEventName`: live audio event key, derived from `AudioEventPrefix` and `RitualState`
- `bLastVerdictAccepted`: last verdict branch for binding consumers

## Gameplay Timing Contract

- `ResetRitual()` returns the altar to `Smolder`, clears trial progress, and marks the trial inactive.
- `StartTrial()` enters `TrialActive`, clears progress, and marks the trial active.
- `AdvanceRitual(DeltaSeconds)` advances `TrialProgress` through `TrialDurationSeconds`, then enters `JudgmentPulse`, `Cooldown`, and finally `Smolder`.
- `AcceptSacrifice(Intensity)` enters `Accepted`, sets progress to complete, sets `JudgmentIntensity`, clears `RejectedSeverity`, and marks the trial inactive.
- `RejectSacrifice(Intensity)` enters `Rejected`, sets progress to complete, sets `JudgmentIntensity` and `RejectedSeverity`, and marks the trial inactive.
- `TriggerJudgmentPulse(Intensity)` enters `JudgmentPulse` and sets `JudgmentIntensity`.
- `SetTrialProgress(Value)` clamps progress and enters `TrialActive` while progress is between `0.0` and `1.0`.

## Quest Audio UI Binding Contract

The altar now exposes the first validated binding surface for future quest, UI, audio, and telemetry layers. Binding consumers should read the altar state and derived tags instead of duplicating the ritual state machine.

| Binding surface | Purpose |
| --- | --- |
| `RitualBindingId` | Stable altar/ritual route key for future quest binding. |
| `ObjectiveBindingId` | Stable first objective route key for the worthiness trial attempt. |
| `CurrentUIStateTag` | Derived UI tag such as `UI.INF.RitualAltar.TrialActive`. |
| `CurrentAudioEventName` | Derived audio event key such as `Audio.INF.RitualAltar.Rejected`. |
| `GetCurrentUIStateTag()` | Blueprint-callable getter for UI routing. |
| `GetCurrentAudioEventName()` | Blueprint-callable getter for audio routing. |
| `GetRitualBindingId()` | Blueprint-callable getter for quest/telemetry routing. |
| `GetObjectiveBindingId()` | Blueprint-callable getter for objective routing. |
| `OnRitualBindingStateChanged` | Broadcasts state, UI tag, audio tag, trial progress, and judgment intensity after state application. |
| `OnRitualVerdictResolved` | Broadcasts accepted/rejected branch, objective ID, verdict intensity, and rejection severity. |

Final quest title, reward rules, persistence, multiplayer authority, analytics schema, UI copy, and audio middleware remain approval-gated by `QUEST_AUDIO_UI_BINDING_PACKET.md`.

The first gameplay implementation should follow `GAMEPLAY_INTEGRATION_PACKET.md` for exact `QEvent.INF.WorthinessAltar.*` event names, attempt data keys, UI/audio routing tags, telemetry guardrails, retry semantics, and validator requirements.

## Blueprint Callable Functions

- `SetRitualState`
- `SetTrialProgress`
- `SetJudgmentIntensity`
- `StartTrial`
- `AcceptSacrifice`
- `RejectSacrifice`
- `TriggerJudgmentPulse`
- `AdvanceRitual`
- `ResetRitual`
- `GetInteractFrontLocation`
- `GetAltarCoreLocation`
- `GetSacrificeMarkLocation`
- `GetBrandTransferLocation`
- `GetRingLinkLocation`
- `GetRejectedGapLocation`
- `GetCurrentUIStateTag`
- `GetCurrentAudioEventName`
- `GetRitualBindingId`
- `GetObjectiveBindingId`

## Material And Niagara Contract

Material parameters pushed to all altar materials:

- `RitualState`
- `TrialProgress`
- `JudgmentIntensity`
- `RejectedSeverity`
- `CooldownAlpha`
- `RitualStateColor`

Niagara `User.*` parameters:

- `User.RitualState`
- `User.TrialProgress`
- `User.JudgmentIntensity`
- `User.RejectedSeverity`
- `User.CooldownAlpha`
- `User.bTrialActive`
- `User.bAccepted`
- `User.bRejected`
- `User.RitualStateColor`
- `User.AltarCoreWorldLocation`
- `User.SacrificeMarkWorldLocation`
- `User.BrandTransferWorldLocation`
- `User.RingLinkWorldLocation`
- `User.RejectedGapWorldLocation`

## Validation Checklist

- `AeratheaEditor Linux Development` builds after native class additions.
- `Tools/Unreal/create_infernal_ritual_altar_blueprint.py` creates or reparents the Blueprint and places `AET_PROD_INF_WorthinessAltar_A01`.
- `Tools/Unreal/validate_infernal_ritual_altar_blueprint.py` validates the Blueprint contract.
- `Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py` validates the timed state flow, verdict calls, 6 locator getters, and binding ID/tag getters.
- `Tools/Unreal/validate_infernal_worthiness_altar.py` validates the backing mesh, sockets, LODs, snap, and envelope.
- `Tools/Unreal/validate_startup_scene.py` validates the live startup actor and global startup contract.
