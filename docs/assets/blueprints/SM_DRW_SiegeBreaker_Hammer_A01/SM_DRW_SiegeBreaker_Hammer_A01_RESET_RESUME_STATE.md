# SM_DRW_SiegeBreaker_Hammer_A01 Reset / Resume State

- Active approved route: `SB-SC3M-A07`
- Plan: `SM_DRW_SiegeBreaker_Hammer_A01_SOURCE_CONSTRAINED_AUTHORITATIVE_3D_MASTER_A07_PLAN.md`
- Reset handoff: `handoffs/SOURCE_CONSTRAINED_AUTHORITATIVE_3D_MASTER_A07_RESET_HANDOFF.md`
- First contract: `steps/A07_GATE_00_COMMERCIAL_SAFE_EXECUTION_PATH_CONTRACT.md`
- Current state: `A07 process saved; context-reset ready; production not started`
- Next approved activity: Core resume handshake followed by A07 Gate 00 only
- Source processing authorized now: `false`
- Model inference authorized now: `false`
- DCC production authorized now: `false`
- Unreal authority: `false`
- Fully game-ready: `false`

## Last Core-Valid State

- Original Siege Breaker concept: `authoritative visual target`.
- Source path proposed for Gate 01:
  `SourceAssets/Concepts/SiegeBreaker/siege_breaker_concept_view.png`.
- Source SHA-256:
  `9f1ac142a5047968bb20c74216c2dccf61470ed9f4e21689ff01934bd849c586`.
- Existing numeric envelope: `52 x 32 x 170 cm`; A07 uses `170 cm` as
  the uniform scale anchor and treats width/depth as fail-closed constraints.
- Shared frame: bottom-center pommel origin; `X=0,Y=0`; protected stations
  remain recorded in `manifests/MEASUREMENT_AND_OWNERSHIP_CONTRACTS.json`.
- A06 state: preserved at `step_10_waiting_flamestrike_decision`; no longer the
  active production route.
- `SB-CM-VISUAL-A01`: `quarantined; invalid as Hero Candidate or authority`.
- A07 visual, geometry, or measurement candidate: does not exist.

## Active Method

A07 creates one complete 3D object before it creates authoritative
orthographic images:

`concept -> licensed AI 3D hypotheses -> source-converged Blender model ->`
`approved hidden surfaces -> uniform scale lock -> approved authoritative 3D`
`Concept Master -> exact derived orthographic measurements -> game-ready derivative`

The original concept controls visible design. AI outputs remain candidates.
Flamestrike controls interpretation and promotion. The locked 3D master controls
geometry and measurement.

## License Stop

The existing local TRELLIS/TRELLIS.2 GLB route invokes restricted NVIDIA
components and is not cleared for A07 production. Existing TRELLIS outputs are
not A07 inputs. Gate 00 must prove a commercially safe inference and raw-geometry
export route before Gate 01 or any generation.

## Resume Instruction

Read the recovery journal/latest checkpoint, this state, the A07 plan, A07
handoff, Gate 00 contract, and prior canonical-master rejection record. Report
the current state summary. Then execute Gate 00 only. Do not crop the source,
run inference, create geometry, or advance to Gate 01 unless Gate 00 records
`go`.
