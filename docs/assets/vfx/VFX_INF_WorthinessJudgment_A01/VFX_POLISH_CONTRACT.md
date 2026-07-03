# VFX_INF_WorthinessJudgment_A01 Polish Contract

Last updated: 2026-06-28

## Purpose

This contract protects the Infernal worthiness judgment effect from drifting into noisy, overbright, or unreadable VFX while the bespoke Niagara graph pass is still pending.

It validates the current material-instance scalar values, parent blend modes, Niagara system names, and emitter names without claiming the template-derived Niagara graphs are final art.

## Validator

- Tool: `Tools/Unreal/validate_infernal_worthiness_judgment_vfx_polish_contract.py`
- Unreal VFX folder: `/Game/Aerathea/VFX/Infernals/WorthinessJudgment/`
- Material instance folder: `/Game/Aerathea/Materials/Instances/`
- Blueprint consumer: `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`
- Runtime timing source: `docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_TIMING_TRACES.md`
- Niagara art-pass handoff: `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/NIAGARA_ART_PASS_HANDOFF.md`

Latest result: passed, including `5` material instances, `6` Niagara systems, `4` Niagara emitters, and restrained scalar ranges.

## Handoff Gate

The validator also requires the Niagara art-pass handoff to name every required system, emitter, native `User.*` parameter, fixed-bounds requirement, and visual approval gate.

This gate advances production readiness without claiming final graph authoring. The current Unreal assets stay `GraphStatus=template_derived_contract_ready` and `FinalGraphAuthored=false` until the actual Niagara graphs are manually authored, validated, and visually approved.

## Approved Scalar Envelope

| Parameter | Readability rule |
| --- | --- |
| `Opacity` | Must stay `0.0-0.70`; no full-screen fire sheets or dense smoke walls |
| `PulseIntensity` | Must stay within restrained ritual ranges; no constant bloom state |
| `PulseDuration` | Must stay event-readable without lingering as a permanent effect |
| `RingRadiusCm` | Must stay aligned to the culling floor or altar variant scale |
| `AcceptedFocus` | Must remain a controlled ember concentration, not an explosion |
| `RejectedSnap` | Must remain a short violet-red event, not a persistent aura |
| `AshDensity` | Must stay sparse enough to preserve character and altar silhouettes |
| `StateIndex` | Must match the state material language used by the altar Blueprint |

## Current Material State Targets

| Material instance | State use | Blend | Key values |
| --- | --- | --- | --- |
| `MI_INF_WorthinessRing_A01` | trial ring | additive | `Opacity 0.54`, `PulseIntensity 1.00`, `RingRadiusCm 900` |
| `MI_INF_WorthinessSigil_A01` | central sigil | additive | `Opacity 0.62`, `PulseIntensity 1.18`, `RingRadiusCm 220` |
| `MI_INF_WorthinessAsh_A01` | ash motes | translucent | `Opacity 0.30`, `PulseIntensity 0.28`, `AshDensity 0.44` |
| `MI_INF_WorthinessRejected_A01` | rejection snap | additive | `Opacity 0.66`, `PulseDuration 0.65`, `RejectedSnap 1.00` |
| `MI_INF_WorthinessJudgmentPulse_A01` | verdict pulse | translucent | `Opacity 0.50`, `PulseDuration 0.95`, `AcceptedFocus 0.55` |

## Final Niagara Graph Requirements

The next VFX art pass should keep the existing asset names and replace or graph-polish the template-derived systems with bespoke logic:

- `NS_INF_Worthiness_Inactive_A01`: no particles or near-zero ambient glow.
- `NS_INF_Worthiness_Smolder_A01`: low ember and sparse ash only.
- `NS_INF_Worthiness_TrialActive_A01`: readable ring/sigil pulse driven by `TrialProgress` and `JudgmentIntensity`.
- `NS_INF_Worthiness_Accepted_A01`: warm focus from ring to altar core or brand-transfer locator.
- `NS_INF_Worthiness_Rejected_A01`: short violet-red snap toward the rejected-gap locator.
- `NS_INF_Worthiness_JudgmentPulse_A01`: short horned/split-wing verdict pulse, then cooldown.

Fixed bounds must be authored separately for floor-only and altar-attached variants. Particle count should reduce before core ring/sigil readability is removed.

## Quality Gate

- VFX stays readable from MMO camera distance.
- No gore, copied symbols, or screen-filling fire simulation.
- Ember/violet color language matches Infernal material rules.
- Material scalars remain inside the validated restrained ranges.
- `BP_INF_RitualAltar_A01` timing and locator contracts remain the runtime source for altar-attached VFX.
- Bespoke graph polish must pass this validator, the focused VFX validator, the altar timing/trace validator, and startup validation before being marked production-ready.
