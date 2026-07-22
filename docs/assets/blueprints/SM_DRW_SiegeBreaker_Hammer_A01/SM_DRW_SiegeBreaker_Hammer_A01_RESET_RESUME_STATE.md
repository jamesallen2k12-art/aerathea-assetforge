# SM_DRW_SiegeBreaker_Hammer_A01 Reset / Resume State

- Active approved route: `SB-ORTHO-A10-DERIVED-A01`
- Plan: `SM_DRW_SiegeBreaker_Hammer_A01_PIXEL_HALF_MIRROR_A09_PLAN.md`
- Active contract: `steps/A10_DERIVED_ORTHOGRAPHIC_RENDER_CONTRACT.md`
- Current state: `A10 six-view orthographic candidate complete; independent audit pass 25/25; pending Flamestrike visual decision`
- Next approved activity: open the exact A10 review board and receive one `approved`, `revise`, `rejected`, or `blocked` decision
- Source processing authorized now: `false`
- Model inference authorized now: `false`
- DCC production authorized now: `false; visible A10 decision gate active`
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
- A07 visual, geometry, or measurement candidate: does not exist; route stopped.
- No TRELLIS, TRELLIS.2, TripoSR, generative-image, or image-to-3D software is
  authorized for Siege Breaker.
- Blender is the sole approved visual and geometry construction exception.
- A08 Step 01 A06 pommel: `reference only; revision requested by Flamestrike`.
- A08 A07 estimated-match script: `invalid; unexecuted; preserved in place`.
- A09 visual-match rule: uniform front-pixel scale anchored to `170 cm`;
  measured envelope approximately `75.130513051 x 32.957619477 x 170 cm`.
- A08 A01-A05 pommel attempts: `quarantined`.
- A08 independent audit: `proof only`, `18/18 pass`.
- A09 complete mirrored visual-match DCC source: `approved by Flamestrike` for
  its exact hash-locked visual appearance, pixel proportions, and mirrored
  geometry. LODs, collision, exports, and Unreal remain unauthorized.
- A10 derived orthographics: six true views at one common `190 cm` scale from
  the unchanged approved A09 source; independent audit `25/25`; `candidate`
  pending Flamestrike review of all revealed surfaces.

## Active Method

A09 applies Flamestrike's Visual Match direction:

`immutable front/left/back pixels + uniform pixel proportions -> fresh X>=0`
`Blender half -> exact X=0 mirror -> separate source-color and gray geometry`
`proofs -> Flamestrike visual decision`

No prior Siege Breaker candidate geometry is an A09 construction input.
Flamestrike controls visual approval.

## Prohibited Software Boundary

TRELLIS, TRELLIS.2, TripoSR, diffusion, generative-image, image-to-3D, and
generated-view software are forbidden. Existing outputs from those methods are
not A09 inputs. A07 Gate 00 is stopped and superseded by Flamestrike's later
Blender-only direction.

## Resume Instruction

Read the recovery journal/latest checkpoint, this state, the A09 plan, the A09
contract, the A09 output record, the A09 final review decision, and the A08/A07
recovery record, then read the A10 contract and output record. A10 is complete;
stop at visible review and wait for Flamestrike's decision. Never use TRELLIS
or any other prohibited generation software.
