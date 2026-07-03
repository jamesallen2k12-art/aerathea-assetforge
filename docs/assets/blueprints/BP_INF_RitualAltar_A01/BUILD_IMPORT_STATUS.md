# BP_INF_RitualAltar_A01 Build And Import Status

Last updated: 2026-06-28

## Current Status

- Build/import status: native-backed ritual altar state wrapper implemented; Blueprint asset created, compiled, placed in startup, and validated, including gameplay timing, trace calls, and first quest/audio/UI binding hooks.
- Unreal Blueprint: `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`
- Startup actor: `AET_PROD_INF_WorthinessAltar_A01`
- Native class: `AAETInfernalRitualAltarActor`
- Backing mesh: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_WorthinessAltar_A01`
- Review scope: first-pass ritual state control, material-state switching, WorthinessJudgment Niagara assignment, interaction volume, VFX locators, culling-floor socket placement, and data-driven binding IDs/tags for future quest, UI, audio, and telemetry work.

## Completed Prerequisites

- Static mesh: `SM_INF_WorthinessAltar_A01`
- BrandGlow materials: `MI_INF_BrandGlowStates_A01_*`
- WorthinessJudgment Niagara systems: `NS_INF_Worthiness_*_A01`
- Native source:
  - `Source/Aerathea/Public/AETInfernalRitualAltarActor.h`
  - `Source/Aerathea/Private/AETInfernalRitualAltarActor.cpp`
- Authoring script: `Tools/Unreal/create_infernal_ritual_altar_blueprint.py`
- Gameplay timing/trace contract: `docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_TIMING_TRACES.md`
- Quest/audio/UI binding packet: `docs/assets/blueprints/BP_INF_RitualAltar_A01/QUEST_AUDIO_UI_BINDING_PACKET.md`
- Gameplay integration packet: `docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_INTEGRATION_PACKET.md`

## Runtime Contract

- Mesh component: `AltarMesh`
- Interaction component: `InteractionVolume`
- Marker components: `InteractFrontLocator`, `AltarCoreLocator`, `SacrificeMarkLocator`, `BrandTransferLocator`, `RingLinkLocator`, `RejectedGapLocator`
- Niagara component: `WorthinessNiagara`
- States: `Inactive`, `Smolder`, `TrialActive`, `Accepted`, `Rejected`, `JudgmentPulse`, `Cooldown`
- Runtime parameters: `TrialProgress`, `JudgmentIntensity`, `RejectedSeverity`, `TrialDurationSeconds`, `JudgmentPulseSeconds`, `CooldownSeconds`, `InteractionRadiusCm`, `InteractionDepthCm`
- Binding defaults: `bBindingHooksEnabled = true`, `RitualBindingId = Ritual_INF_CullingTrial_A01`, `ObjectiveBindingId = OBJ_INF_ProveWorth_A01`, `UIStatePrefix = UI.INF.RitualAltar`, `AudioEventPrefix = Audio.INF.RitualAltar`
- Live binding values: `CurrentUIStateTag`, `CurrentAudioEventName`, `bLastVerdictAccepted`
- Validated timing calls: `ResetRitual`, `StartTrial`, `AdvanceRitual`, `AcceptSacrifice`, `RejectSacrifice`, `TriggerJudgmentPulse`, `SetTrialProgress`
- Validated trace getters: `GetInteractFrontLocation`, `GetAltarCoreLocation`, `GetSacrificeMarkLocation`, `GetBrandTransferLocation`, `GetRingLinkLocation`, `GetRejectedGapLocation`
- Validated binding getters: `GetCurrentUIStateTag`, `GetCurrentAudioEventName`, `GetRitualBindingId`, `GetObjectiveBindingId`
- Blueprint delegates: `OnRitualBindingStateChanged`, `OnRitualVerdictResolved`

## Validation

- C++ build: `AeratheaEditor Linux Development` succeeded.
- Focused Blueprint validator: `Tools/Unreal/validate_infernal_ritual_altar_blueprint.py`
- Gameplay timing/trace validator: `Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py`
- Mesh-level validator: `Tools/Unreal/validate_infernal_worthiness_altar.py`
- Startup validator: `Tools/Unreal/validate_startup_scene.py`
- Focused Blueprint result: passed, `356.00h x 404.00w x 346.00d cm`, bounds radius `320.03 cm`, 9 components, 6 state materials, 6 Niagara systems.
- Gameplay timing/trace result: passed, including trial/cooldown flow, accepted/rejected verdicts, judgment pulse, 6 locator getters, and binding tag/id getters.
- Mesh-level result: passed, `356.00h x 404.00w x 346.00d cm`, bounds radius `320.03 cm`, 9 sockets.
- Startup result: passed, `233 assets`, `55 expected actors`, `25 ground tiles`.

## Remaining To Finalize

1. Replace first-pass altar geometry with final sculpt/retopo, UVs, textures, and tuned collision.
2. Polish bespoke WorthinessJudgment Niagara graphs against the native `User.*` contract.
3. Implement the first quest/audio/UI binding layer against `GAMEPLAY_INTEGRATION_PACKET.md` after the final quest text, reward rules, persistence, and multiplayer authority decisions are approved.
