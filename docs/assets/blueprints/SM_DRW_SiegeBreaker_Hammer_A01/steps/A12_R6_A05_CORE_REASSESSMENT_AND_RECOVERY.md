# A12 R6 A05 Core Reassessment And Recovery

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: `2026-07-22`
- Status: `authoritative recovery boundary`
- DCC production authority: `false`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Decision

The A05-local cylindrical haft/collar UV rule was followed, but the complete
R6/A05 construction did not follow the governing component-geometry rule.
A05 A01-A03 are `invalid / quarantined` and cannot be approved, audited as a
candidate, exported, or repaired forward.

## Last Core-Valid State

- immutable six-view source pixels and hashes;
- `170 cm` vertical frame and source-pixel proportion evidence;
- centered shaft axis;
- approved centered core and two separate strike-stone component direction;
- left/right source ownership of the outward strike faces;
- one physical component half duplicated at its declared center plane;
- Flamestrike's new explicit corrections:
  - the strike-face division line runs down the vertical middle of one face;
  - only one half of that face is duplicated;
  - the face piece pitches inward toward the head at its bottom, preserving its
    visible narrow-top/wide-bottom form;
  - no stone occupies the space between the two upper haft-cap halves;
  - the pommel and top cap are tapered cylinders/cones.

## First Drift Action

In `build_row_occupancy_factory`, every non-haft layer became:

`all front-row X cells × all right-row Y cells`

That Cartesian product created one monolithic occupancy volume. It did not
build each physical component as its own closed boundary volume as required by
R6. The subsequent exact Y-depth mirror duplicated a wrong half correctly; it
could not correct the wrong component decomposition.

The strike-face UV mapping compounded the error by folding the source around
the global shaft axis. The mapped half already contained the complete face
motif, so the mirror created two motifs and widened the visible head. The face
piece's side-source pitch was never converted into controlling geometry.

## Affected Outputs And Status

- A05 A01: `invalid / quarantined`; bright source-outline seam plus invalid
  inherited geometry.
- A05 A02: `invalid / quarantined`; selected endpoints retained the same seam
  plus invalid inherited geometry.
- A05 A03: `invalid / quarantined`; outline seam reduced, but stretched head,
  complete-face duplication, wrong face pitch, inter-cap stone fill, and
  extruded pommel/top cap remain.
- Topology, Y-depth mirror/weld, outward-normal, and haft/collar static-UV
  evidence: `proof only` for those narrow mechanics.
- No A05 independent candidate audit was run.

## Smallest Sufficient Recovery

Do not edit an A05 blend. A new contract must return to immutable pixels and
declare, measure, and audit at least:

1. separate centered core, left stone, right stone, strike-face half, upper
   cap, haft, grip, lower collar, pommel body, and terminal-cap components;
2. the strike face's own vertical centerline, not the shaft axis, as its half
   duplication plane;
3. exact side-source top/bottom face widths and inward pitch/rotation;
4. zero stone occupancy in the upper haft-cap negative space;
5. tapered surface-of-revolution rules for the pommel and top cap;
6. front/side/top pixel bounds reconciled per component before any mirroring;
7. review views that expose the face centerline, face pitch, cap negative
   space, pommel taper, top-cap taper, and complete head envelope.

No new DCC build is authorized until Flamestrike approves that contract.

## Reset-Safe Forward Plan

The draft forward plan is
`../SM_DRW_SiegeBreaker_Hammer_A01_A12_R7_COMPONENT_GEOMETRY_RECOVERY_PLAN.md`.
It is not execution authority. After reset, present it for Flamestrike approval
or revision before Step 01 measurement work.
