# BP_INF_RitualAltar_A01 Quest Audio UI Binding Packet

Last updated: 2026-06-28

## Purpose

Define the documentation-only binding contract for quest/objective logic, UI prompts, audio cues, telemetry, retry behavior, and validation around `BP_INF_RitualAltar_A01`.

This packet does not implement Source, Tools, Content, global index, balance, reward, persistence, backend, or multiplayer authority changes. It binds future work to the already validated altar runtime contract.

## Source Contracts

- Gameplay timing and trace source: `docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_TIMING_TRACES.md`
- Blueprint production package: `docs/assets/blueprints/BP_INF_RitualAltar_A01/PRODUCTION_PACKAGE.md`
- Current implementation handoff: `docs/assets/blueprints/BP_INF_RitualAltar_A01/IMPLEMENTATION_HANDOFF.md`
- Current build/import status: `docs/assets/blueprints/BP_INF_RitualAltar_A01/BUILD_IMPORT_STATUS.md`
- Gameplay integration packet: `docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_INTEGRATION_PACKET.md`
- Worthiness VFX polish contract: `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/VFX_POLISH_CONTRACT.md`
- BrandGlow material package: `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`

## Locked Runtime Inputs

The binding layer must consume these existing names without renaming them:

| Contract | Locked value |
| --- | --- |
| Blueprint | `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01` |
| Startup actor | `AET_PROD_INF_WorthinessAltar_A01` |
| Native class | `AAETInfernalRitualAltarActor` |
| State enum | `EAETInfernalRitualAltarState` |
| States | `Inactive`, `Smolder`, `TrialActive`, `Accepted`, `Rejected`, `JudgmentPulse`, `Cooldown` |
| Timing defaults | `TrialDurationSeconds = 8.0`, `JudgmentPulseSeconds = 1.25`, `CooldownSeconds = 2.5` |
| Progress fields | `TrialProgress`, `JudgmentIntensity`, `RejectedSeverity`, `CooldownAlpha`, `bRitualActive` |
| Callable controls | `ResetRitual`, `StartTrial`, `AdvanceRitual`, `AcceptSacrifice`, `RejectSacrifice`, `TriggerJudgmentPulse`, `SetTrialProgress` |
| Locator getters | `GetInteractFrontLocation`, `GetAltarCoreLocation`, `GetSacrificeMarkLocation`, `GetBrandTransferLocation`, `GetRingLinkLocation`, `GetRejectedGapLocation` |

## Quest And Objective Hooks

Working quest name: `Q_INF_WorthinessTrial_A01`. The name is a binding placeholder only; final quest title, lore text, reward rules, and progression ownership need approval.

| Hook | Runtime trigger | Objective use | Required data |
| --- | --- | --- | --- |
| `OnAltarDiscovered` | player enters altar discovery/interaction range | reveal or advance approach objective | altar actor id, `GetInteractFrontLocation()` |
| `OnAltarInteractPromptShown` | player is eligible to interact while state is `Smolder` or `Inactive` | show interaction objective prompt | state, interaction range result |
| `OnWorthinessTrialStarted` | `StartTrial()` succeeds | start active trial objective | `TrialDurationSeconds`, attempt id |
| `OnWorthinessTrialProgress` | `TrialProgress` changes during `TrialActive` | update objective bar and optional ritual callouts | `TrialProgress`, `GetTrialAlpha()` if exposed to binding |
| `OnWorthinessJudgmentPulse` | `TriggerJudgmentPulse()` or trial duration completion | pause input/reward resolution until verdict window finishes | `JudgmentIntensity`, `JudgmentPulseSeconds` |
| `OnWorthinessAccepted` | `AcceptSacrifice(Intensity)` | complete success branch | intensity, altar location, character id/token |
| `OnWorthinessRejected` | `RejectSacrifice(Intensity)` | complete failure branch or retry branch | intensity, `RejectedSeverity`, cooldown |
| `OnWorthinessCooldownStarted` | state enters `Cooldown` | suppress repeated interaction and show retry delay if allowed | `CooldownSeconds`, `CooldownAlpha` |
| `OnWorthinessReset` | `ResetRitual()` or cooldown returns to `Smolder` | clear transient UI and unlock retry when rules allow | state, attempt id |

Objective binding should treat `Accepted` and `Rejected` as terminal verdict states for the current attempt. `JudgmentPulse` is a transition state and should not grant rewards by itself.

## UI State Contract

UI must read from runtime state and fields instead of maintaining a separate ritual state machine.

| UI state | Altar state/data | Presentation rule |
| --- | --- | --- |
| Hidden | no valid altar focus or blocked by quest phase | no prompt, no progress bar |
| Interact available | `Smolder` or approved `Inactive`, player near `InteractionVolume` | show one interact prompt anchored near `GetInteractFrontLocation()` |
| Trial active | `TrialActive`, `TrialProgress 0.0-1.0` | show a compact progress meter and restrained objective text |
| Judgment resolving | `JudgmentPulse` | hide interaction prompt, hold final result until verdict call/state |
| Accepted | `Accepted` | show success feedback, then hand off to quest reward/next objective |
| Rejected | `Rejected` | show failure feedback and retry/cooldown status if allowed |
| Cooldown | `Cooldown`, `CooldownAlpha` | disable interaction, show retry countdown only if current quest rules allow retry |

Final wording, iconography, accessibility pass, controller prompts, localization keys, and success/failure copy are approval-gated. The UI implementation must avoid blocking the altar silhouette or WorthinessJudgment readability.

## Audio Event Contract

Audio events should be one-shot or short loop cues bound to state changes and locator getters. No final mix, middleware, or asset format is locked here.

| Event key | Trigger | Locator | Readability rule |
| --- | --- | --- | --- |
| `SFX_INF_RitualAltar_Interact_A01` | successful interaction/start request | `GetInteractFrontLocation()` | short stone/ember response |
| `SFX_INF_RitualAltar_SmolderLoop_A01` | `Smolder` | `GetAltarCoreLocation()` | low-volume loop, optional, must not mask ambience |
| `SFX_INF_RitualAltar_TrialStart_A01` | `StartTrial()` | `GetRingLinkLocation()` | clear start sting, no long roar |
| `SFX_INF_RitualAltar_TrialPulse_A01` | periodic `TrialProgress` pulse | `GetAltarCoreLocation()` and `GetRingLinkLocation()` | sparse pulses synced to readable VFX |
| `SFX_INF_RitualAltar_JudgmentPulse_A01` | `JudgmentPulse` begins | `GetAltarCoreLocation()` | brief verdict swell within `JudgmentPulseSeconds` |
| `SFX_INF_RitualAltar_Accepted_A01` | `Accepted` | `GetBrandTransferLocation()` | warm focused ember response |
| `SFX_INF_RitualAltar_Rejected_A01` | `Rejected` | `GetRejectedGapLocation()` | short violet-red snap, no persistent failure loop |
| `SFX_INF_RitualAltar_Cooldown_A01` | `Cooldown` begins | `GetAltarCoreLocation()` | quick decay cue |

Audio implementation should expose per-state volume and cooldown throttles. Repeated rejected/accepted events must be rate-limited by attempt id to prevent stacked one-shots.

## Telemetry And Progress Fields

The first implementation pass should log deterministic gameplay fields only. Player/account identity format, analytics vendor, retention policy, and backend schema require approval before production telemetry is locked.

| Field | Source | Use |
| --- | --- | --- |
| `RitualAttemptId` | quest/binding layer | de-duplicate verdict, audio, UI, and telemetry events |
| `QuestId` | quest layer | route objective progress |
| `AltarActorName` | actor | identify placed altar instance |
| `RitualState` | altar state | state transition logging |
| `TrialProgress` | altar field | progress bar and progression analytics |
| `JudgmentIntensity` | altar field | verdict strength/tuning review |
| `RejectedSeverity` | altar field | failure severity/tuning review |
| `CooldownAlpha` | altar field | retry countdown and cooldown validation |
| `ElapsedTrialSeconds` | binding layer from trial start | timing validation and abandon detection |
| `Verdict` | accepted/rejected/reset/abandoned | objective completion branch |
| `FailureReason` | binding layer | rejected, cancelled, out-of-range, interrupted, authority denied, or timeout |

Telemetry must not mark the quest complete until `Accepted` is confirmed. `Rejected`, cancel, timeout, and reset events are attempt outcomes, not success completions.

## Failure And Retry Semantics

- `Rejected` ends the current attempt and may unlock retry only after `Cooldown` returns to `Smolder`.
- `Cooldown` blocks additional interaction prompts unless a designer explicitly enables a queued retry prompt.
- Player cancellation before verdict should call or request `ResetRitual()` and record `FailureReason = cancelled`.
- Leaving interaction range during `TrialActive` should be treated as approval-gated gameplay. Recommended default for the first pass is non-lethal cancellation to `ResetRitual()` with no reward.
- Combat interruption, sacrifice requirements, item costs, health costs, group participation, respawn penalties, and reward grants are not locked in this packet.
- Network authority must be server-owned for MMO production, but the exact authority model is approval-gated and should not be hard-coded from this document alone.

## Validation Expectations

No new validator is required for this documentation-only packet. The next implementation packet should add or extend deterministic validation for:

- quest binding references the locked Blueprint path and startup actor name;
- UI state table maps all seven altar states exactly once;
- audio event keys exist and are rate-limited by attempt id;
- telemetry records terminal attempt outcomes without granting success on `JudgmentPulse`;
- retry remains blocked during `Cooldown`;
- all locator getters return finite world-space vectors before UI/audio/VFX anchors use them;
- existing validators still pass:
  - `Tools/Unreal/validate_infernal_ritual_altar_blueprint.py`
  - `Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py`
  - `Tools/Unreal/validate_infernal_worthiness_judgment_vfx_polish_contract.py`
  - `Tools/Unreal/validate_startup_scene.py`

## Approval-Gated Items

Do not lock or implement these without user approval:

- final quest title, story text, objective copy, and localization keys;
- success/failure rewards, item costs, sacrifice costs, death/health penalties, and economy hooks;
- class-specific altar interactions or class skill identity;
- combat interruption rules and encounter pacing;
- multiplayer authority model, replication rules, party credit, and MMO backend/vendor assumptions;
- analytics vendor schema, account/player identifiers, retention policy, and privacy rules;
- final audio middleware, mix targets, voiceover, subtitles, and accessibility copy;
- final UI art, icons, animations, and controller/keybind presentation;
- final WorthinessJudgment bespoke Niagara graph behavior beyond the existing VFX polish contract.

## Implementation Handoff

The next gameplay implementation task should use `GAMEPLAY_INTEGRATION_PACKET.md` as the concrete event/data contract. It should create a binding layer that listens to the locked altar state/timing calls, exposes quest-safe events, and routes UI/audio/telemetry without duplicating altar state. It should update validators in the same pass and keep visual intensity within the BrandGlow and WorthinessJudgment contracts.
