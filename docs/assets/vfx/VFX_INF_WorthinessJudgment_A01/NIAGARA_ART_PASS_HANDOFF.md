# VFX_INF_WorthinessJudgment_A01 Niagara Art Pass Handoff

## Purpose

Author the final Niagara graph polish for `VFX_INF_WorthinessJudgment_A01` using the existing ritual altar state, socket, material, and readability contracts. This handoff defines the final art behavior, emitters, native `User.*` parameters, fixed bounds, LOD rules, and visual approval checks.

This does not claim the Unreal Niagara graphs are authored. Current assets remain `GraphStatus=template_derived_contract_ready` and `FinalGraphAuthored=false` until a manual Unreal/Niagara pass updates the systems and passes visual approval.

## Current Contract

Native actor: `AAETInfernalRitualAltarActor`

Blueprint/native consumer:

- `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`
- `Source/Aerathea/Private/AETInfernalRitualAltarActor.cpp`

Current native Niagara component:

- Component: `WorthinessNiagara`
- Auto activation: false
- Hidden while inactive
- Relative placement: altar-centered, offset upward for readable altar-core pulse

Current native Niagara systems by state:

- `InactiveNiagaraSystem` -> `NS_INF_Worthiness_Inactive_A01`
- `SmolderNiagaraSystem` -> `NS_INF_Worthiness_Smolder_A01`
- `TrialActiveNiagaraSystem` -> `NS_INF_Worthiness_TrialActive_A01`
- `AcceptedNiagaraSystem` -> `NS_INF_Worthiness_Accepted_A01`
- `RejectedNiagaraSystem` -> `NS_INF_Worthiness_Rejected_A01`
- `JudgmentPulseNiagaraSystem` -> `NS_INF_Worthiness_JudgmentPulse_A01`

Current native `User.*` parameters pushed by `AAETInfernalRitualAltarActor`:

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

## Final Niagara Targets

- Unreal folder: `/Game/Aerathea/VFX/Infernals/WorthinessJudgment/`
- Material parent folder: `/Game/Aerathea/Materials/Infernals/VFX/`
- Material instance folder: `/Game/Aerathea/Materials/Instances/`
- Runtime timing source: `docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_TIMING_TRACES.md`
- Polish contract: `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/VFX_POLISH_CONTRACT.md`

Niagara systems:

- `NS_INF_Worthiness_Inactive_A01`
- `NS_INF_Worthiness_Smolder_A01`
- `NS_INF_Worthiness_TrialActive_A01`
- `NS_INF_Worthiness_Accepted_A01`
- `NS_INF_Worthiness_Rejected_A01`
- `NS_INF_Worthiness_JudgmentPulse_A01`

Niagara emitters:

- `NE_INF_WorthinessRingPulse_A01`
- `NE_INF_WorthinessSigilPulse_A01`
- `NE_INF_WorthinessAshMote_A01`
- `NE_INF_WorthinessRejectedSnap_A01`

## Visual Direction

- Primary read is the ember ring and central horned/split-wing sigil.
- Smolder and cooldown stay low, sparse, and readable.
- Trial active uses rhythmic ring/sigil pulses driven by trial progress and judgment intensity.
- Accepted concentrates warm ember energy from the ring toward altar core or brand-transfer locator.
- Rejected is a short violet-red snap toward the rejected-gap locator, not a persistent aura.
- Judgment pulse is a short verdict event, then fades into cooldown.

Avoid gore, copied religious symbols, full-screen fire, dense smoke walls, white-hot bloom, or tiny noisy sparks that hide character silhouettes.

## System Behavior

| System | State | Final behavior |
| --- | --- | --- |
| `NS_INF_Worthiness_Inactive_A01` | inactive | Niagara hidden or near-zero ambient ember only |
| `NS_INF_Worthiness_Smolder_A01` | smolder | sparse ash motes and low floor-channel ember |
| `NS_INF_Worthiness_TrialActive_A01` | trial active | ring pulse plus central sigil pulse driven by `User.TrialProgress` and `User.JudgmentIntensity` |
| `NS_INF_Worthiness_Accepted_A01` | accepted | warm ring-to-core or ring-to-brand transfer using `User.BrandTransferWorldLocation` |
| `NS_INF_Worthiness_Rejected_A01` | rejected | short violet-red snap using `User.RejectedSeverity` and `User.RejectedGapWorldLocation` |
| `NS_INF_Worthiness_JudgmentPulse_A01` | judgment pulse | horned/split-wing verdict pulse using `User.RitualStateColor`, then cooldown fade |

## Emitter Plan

| Emitter | Purpose | Notes |
| --- | --- | --- |
| `NE_INF_WorthinessRingPulse_A01` | primary floor ring read | Last emitter to disable by distance; no dense smoke attachment |
| `NE_INF_WorthinessSigilPulse_A01` | central horned/split-wing sigil pulse | Low frequency, readable from MMO camera distance |
| `NE_INF_WorthinessAshMote_A01` | sparse ember ash | First emitter to reduce by distance and low scalability |
| `NE_INF_WorthinessRejectedSnap_A01` | violet-red rejection event | Short event only; not a looping aura |

## Parameter Mapping

- `User.RitualState`: gates state selection and emitter enablement.
- `User.TrialProgress`: controls ring pulse phase, sigil pulse phase, and trial-active intensity ramp.
- `User.JudgmentIntensity`: controls emissive response, pulse width, and event brightness inside the approved scalar envelope.
- `User.RejectedSeverity`: controls rejected snap length, crack count, and violet-red intensity.
- `User.CooldownAlpha`: fades motes and channel glow during cooldown.
- `User.bTrialActive`: enables trial-active ring/sigil emitters.
- `User.bAccepted`: enables accepted transfer behavior.
- `User.bRejected`: enables rejected snap behavior.
- `User.RitualStateColor`: drives state color blend without changing material palette identity.
- `User.AltarCoreWorldLocation`: target for altar-core pulse.
- `User.SacrificeMarkWorldLocation`: optional origin or hold point for sacrifice-mark feedback.
- `User.BrandTransferWorldLocation`: accepted-state transfer target.
- `User.RingLinkWorldLocation`: ring-to-altar link point.
- `User.RejectedGapWorldLocation`: rejected snap target and broken-circle emphasis.

Do not rename existing parameters without a matching native/Blueprint implementation task.

## Material Requirements

Use the existing validated material instances:

- `MI_INF_WorthinessRing_A01`
- `MI_INF_WorthinessSigil_A01`
- `MI_INF_WorthinessAsh_A01`
- `MI_INF_WorthinessRejected_A01`
- `MI_INF_WorthinessJudgmentPulse_A01`

Required scalar rules:

- `Opacity` remains `0.0-0.70`.
- `AshDensity` remains `0.0-0.50`.
- Rejected and judgment pulse materials remain event-pulse-only.
- Material slots do not increase for this pass.
- No dynamic lights by default.

## Fixed Bounds

Author separate fixed bounds behavior for:

- Floor-only states: radius up to `1000 cm`, height `80-220 cm`.
- Altar-attached states: radius up to `900 cm`, height up to `420 cm`.

The bounds must cover altar-core, brand-transfer, ring-link, and rejected-gap locators without overextending into adjacent review actors.

## LOD And Scalability

- LOD0: ring pulse, sigil pulse, ash motes, accepted transfer, rejected snap, judgment pulse.
- LOD1: reduce ash density and event sparkle count.
- LOD2: keep ring/sigil read and one accepted/rejected event sprite.
- LOD3: disable particles and rely on material glow only.
- Low scalability: disable ash first, then rejected fragments, then accepted transfer; preserve ring/sigil readability longest.

## Manual Graph Authoring Checklist

1. Open each `NS_INF_Worthiness_*_A01` system in Unreal Niagara.
2. Replace template behavior with the state-specific emitter stack from this handoff.
3. Bind the native `User.*` parameters exactly as documented.
4. Assign fixed bounds for floor-only and altar-attached review variants.
5. Keep material instances inside the validated polish scalar envelope.
6. Save the existing asset names in `/Game/Aerathea/VFX/Infernals/WorthinessJudgment/`.
7. Run focused VFX, polish contract, ritual altar timing/trace, and startup validators.
8. Capture a visual review against the altar/floor source view before final approval.

## Validation Requirements

Before final visual approval:

1. `Tools/Unreal/validate_infernal_worthiness_judgment_vfx.py` passes.
2. `Tools/Unreal/validate_infernal_worthiness_judgment_vfx_polish_contract.py` passes.
3. `Tools/Unreal/validate_infernal_ritual_altar_timing_traces.py` passes.
4. `Tools/Unreal/validate_startup_scene.py` passes if the startup map or assigned assets changed.
5. Review capture confirms no screen-filling fire, dense smoke, excessive bloom, or silhouette loss.

## Acceptance Checklist

- The effect reads as Infernal/Balgoroth ritual judgment.
- Ember/violet color language stays restrained and consistent.
- Six runtime states are distinct at gameplay camera distance.
- Rejected and judgment pulse are short events, not persistent auras.
- Native `User.*` parameters are consumed by the graph.
- Fixed bounds are tuned for floor and altar variants.
- Existing asset names and Blueprint assignments remain stable.
- `GraphStatus` and `FinalGraphAuthored` metadata are only updated after actual graph authoring and visual approval.
