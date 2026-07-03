# BP_INF_RitualAltar_A01 Production Package

## 1. Art Direction Summary

- Asset name: `BP_INF_RitualAltar_A01`
- Asset type: Blueprint Actor with native C++ parent
- Native class: `AAETInfernalRitualAltarActor`
- Parent kit: `KIT_INF_BalgorothCult_A01`
- Backing mesh: `SM_INF_WorthinessAltar_A01`
- Status: first-pass native-backed Blueprint implementation complete, placed in startup, and validated, including gameplay timing, trace calls, and quest/audio/UI binding hooks

`BP_INF_RitualAltar_A01` is the gameplay wrapper for the Balgoroth worthiness altar. It keeps the approved altar silhouette and cleaned visual direction intact while exposing a reusable state machine for smolder, trial, accepted, rejected, judgment-pulse, and cooldown ritual states plus stable binding hooks for future quest, UI, audio, and telemetry systems.

## 2. Gameplay Purpose

- Presents the altar as a single placed gameplay actor instead of a static prop only.
- Drives BrandGlow material states on the altar glow slot.
- Assigns WorthinessJudgment Niagara systems by state.
- Exposes interaction, altar-core, sacrifice-mark, brand-transfer, ring-link, and rejected-gap locator positions for quest, VFX, audio, and encounter scripting.
- Provides a validated trial/cooldown timing flow plus accepted, rejected, and judgment-pulse verdict calls.
- Provides stable binding IDs, derived UI/audio state tags, and Blueprint delegates so future systems can listen without duplicating altar state.
- Provides the future binding point for Lesser Infernal culling trials, cult room set dressing, and judgment interactions.

## 3. Silhouette Notes

The Blueprint must preserve the static mesh read: low heavy altar body, horned crown backplate, split-wing side slabs, central basin, and a readable front interaction side. Blueprint helper volumes and VFX must not obscure the altar mass or add noisy particle clutter.

## 4. Scale Notes

- Startup actor: `AET_PROD_INF_WorthinessAltar_A01`
- Startup envelope after Blueprint wrapper: `356.00h x 404.00w x 346.00d cm`
- Bounds radius: `320.03 cm`
- Actor scale: `1.0, 1.0, 1.0`
- Placement: snapped to `SM_INF_CullingTrialFloor_A01` `snap_altar`

## 5. Materials And Color Palette

State material properties:

- `BrandGlowInactiveMaterial`: `MI_INF_BrandGlowStates_A01_Inactive`
- `BrandGlowSmolderMaterial`: `MI_INF_BrandGlowStates_A01_Smolder`
- `BrandGlowTrialActiveMaterial`: `MI_INF_BrandGlowStates_A01_TrialActive`
- `BrandGlowAcceptedMaterial`: `MI_INF_BrandGlowStates_A01_Accepted`
- `BrandGlowRejectedMaterial`: `MI_INF_BrandGlowStates_A01_Rejected`
- `BrandGlowJudgmentPulseMaterial`: `MI_INF_BrandGlowStates_A01_SorcererFocus`

Runtime material parameters: `RitualState`, `TrialProgress`, `JudgmentIntensity`, `RejectedSeverity`, `CooldownAlpha`, and `RitualStateColor`.

Binding defaults:

- `bBindingHooksEnabled`: `true`
- `RitualBindingId`: `Ritual_INF_CullingTrial_A01`
- `ObjectiveBindingId`: `OBJ_INF_ProveWorth_A01`
- `UIStatePrefix`: `UI.INF.RitualAltar`
- `AudioEventPrefix`: `Audio.INF.RitualAltar`
- Live derived values: `CurrentUIStateTag`, `CurrentAudioEventName`, `bLastVerdictAccepted`

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG Blueprint concept sheet of `BP_INF_RitualAltar_A01` for the Infernals of Aerathea. The design should emphasize a Balgoroth worthiness altar state machine, a heavy black-basalt altar with horned crown backplate, split-wing side slabs, restrained ember and violet BrandGlow states, clear interaction and VFX locators, and MMO-friendly production behavior. Present it as a clean Blueprint behavior sheet with inactive, smolder, trial active, accepted, rejected, judgment pulse, and cooldown states, component callouts, material-state swatches, Niagara system assignments, collision volume, and scale beside a 180 cm humanoid and 274 cm Infernal. Avoid copied franchise designs, gore, excessive particles, unreadable text, watermarks, and micro-detail noise.

## 7. Modeling Notes

No additional modeled geometry is required for the Blueprint wrapper. Keep all visible form changes on `SM_INF_WorthinessAltar_A01`, material instances, or Niagara. The Blueprint owns placement, locators, hidden interaction volume, state material selection, and VFX routing only.

## 8. Texture And Material Notes

The Blueprint uses the altar material slot index `4` for BrandGlow state swapping. Final art should preserve that glow slot or update both `BrandGlowMaterialSlotIndex` and validators together.

## 9. Triangle Budget

The Blueprint adds no visible mesh triangles beyond `SM_INF_WorthinessAltar_A01`. VFX helper geometry should remain lightweight and state-driven.

## 10. LOD Plan

The Blueprint inherits the altar static mesh LOD0-LOD3 plan. VFX should reduce sprite/ribbon density before removing the core altar read.

## 11. Collision Notes

- `AltarMesh`: blocking collision for the altar body.
- `InteractionVolume`: hidden `BoxComponent`, overlap profile, centered on the front interaction side.
- Interaction volume defaults: `InteractionRadiusCm = 170`, `InteractionDepthCm = 90`.
- Do not use the interaction volume as visible geometry.

## 12. Animation Notes

State enum: `EAETInfernalRitualAltarState`.

- `Inactive`: dark channels, no active Niagara.
- `Smolder`: low ember state.
- `TrialActive`: ring/core pulse.
- `Accepted`: warm focused ember pulse.
- `Rejected`: violet-red rejection snap.
- `JudgmentPulse`: short high-intensity judgment state.
- `Cooldown`: dim return to smolder.

Callable functions: `SetRitualState`, `SetTrialProgress`, `SetJudgmentIntensity`, `StartTrial`, `AcceptSacrifice`, `RejectSacrifice`, `TriggerJudgmentPulse`, `AdvanceRitual`, `ResetRitual`, and locator getters.

Validated timing flow: `ResetRitual` -> `StartTrial` -> `AdvanceRitual` through trial duration -> `JudgmentPulse` -> `Cooldown` -> `Smolder`, with separate accepted/rejected verdict calls.

Validated binding flow: state application updates `CurrentUIStateTag` and `CurrentAudioEventName`, then broadcasts `OnRitualBindingStateChanged` when hooks are enabled. Accepted and rejected verdict calls broadcast `OnRitualVerdictResolved` with the objective ID and verdict intensity.

## 13. Unreal Import Notes

- Blueprint path: `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`
- Native source:
  - `Source/Aerathea/Public/AETInfernalRitualAltarActor.h`
  - `Source/Aerathea/Private/AETInfernalRitualAltarActor.cpp`
- Authoring script: `Tools/Unreal/create_infernal_ritual_altar_blueprint.py`
- Focused validator: `Tools/Unreal/validate_infernal_ritual_altar_blueprint.py`
- Timing/trace validator: `Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py`
- Gameplay integration packet validator: `Tools/Unreal/validate_infernal_ritual_altar_gameplay_integration_packet.py`
- Mesh validator: `Tools/Unreal/validate_infernal_worthiness_altar.py`
- Startup validator: `Tools/Unreal/validate_startup_scene.py`

## 14. Folder And Naming Recommendation

- Package folder: `docs/assets/blueprints/BP_INF_RitualAltar_A01/`
- Unreal Blueprint: `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`
- Startup actor: `AET_PROD_INF_WorthinessAltar_A01`
- Native class: `AAETInfernalRitualAltarActor`

## 15. Quality Gate Checklist

- Native C++ build succeeds.
- Blueprint asset exists, compiles, and is parented to `AAETInfernalRitualAltarActor`.
- Startup actor uses `AltarMesh` with `SM_INF_WorthinessAltar_A01`.
- Six BrandGlow state materials are assigned.
- Six WorthinessJudgment Niagara systems are assigned.
- Nine required components are present.
- Actor stays snapped to the culling floor altar socket.
- Binding defaults and live UI/audio state tags are present.
- Focused Blueprint, gameplay timing/trace, mesh-level altar, and startup validators pass.
