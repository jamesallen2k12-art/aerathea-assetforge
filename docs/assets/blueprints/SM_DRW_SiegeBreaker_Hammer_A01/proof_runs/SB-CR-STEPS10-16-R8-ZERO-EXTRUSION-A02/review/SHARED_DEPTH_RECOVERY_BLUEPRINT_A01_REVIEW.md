# Shared-Depth Recovery Blueprint A01 Review

- Date: `2026-07-24`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01` / Siege Breaker
  - `SM_DRW_FoeHammer_Hammer_A01` / Foe Hammer
- Review artifact status: `candidate pending Flamestrike approval`
- Exact shared XYZ decision: `authoritative`
- Equation validation: `proof only; 66/66 PASS`
- Builder authority: `false`
- Blender authority: `false`
- Geometry authority: `false`
- Step 13 authority: `false`
- Unreal authority: `false`

## Decision Summary

Both weapons use this exact overall bounding box:

`97.974428267601 × 44.299176584 × 170 cm`

Exact width × depth × height:

`50719500/517681 × 6644212/149985 × 170/1 cm`

Flamestrike explicitly approved this shared XYZ rule while the documentation
step was in progress.

## What Is Shared

The two assets must use:

- one identical overall XYZ envelope;
- one canonical shared body;
- the same scale, pivot, orientation, transforms, nonvariant components,
  contacts, and closures;
- zero cross-asset bounds difference; and
- an identical shared-base canonical hash after excluding only the tagged
  local `C04` treatment.

The common body depth is:

`6644212/149985 cm = 44.299176584 cm`

The prior `EQ_CANDIDATE_AXIAL_INTERSECTION` rule is invalid and forbidden.
Neither local treatment may clip or resize the shared body.

## What Differs

### Siege Breaker

- Local treatment: double rune sided.
- Source half: `[557,668)`, exactly `111 px`.
- Local half extent:
  `9435/548 cm = 17.217153284672 cm`.
- Local completed span:
  `9435/274 cm = 34.434306569343 cm`.
- Inset from the common envelope:
  `405405613/82191780 cm = 4.932435007491 cm` per side.

### Foe Hammer

- Local treatment: double metal-center-piece sided.
- Source half: `[418,557)`, exactly `139 px`.
- Local half extent:
  `11815/548 cm = 21.560218978102 cm`.
- Local completed span:
  `11815/274 cm = 43.120437956204 cm`.
- Inset from the common envelope:
  `48441313/82191780 cm = 0.589369314060 cm` per side.

Both local mappings retain the exact `85/548 cm/px` right-view scale. Neither
is stretched, normalized, averaged, or resampled.

## Width Decision

The front-controlled width remains:

`104040/1063 cm = 97.873941674506 cm`

The exact source-owned output bound is the larger:

`50719500/517681 cm = 97.974428267601 cm`

The difference is one secondary-view pixel across the completed width, or
one-half pixel per side. It passes the already approved pixel, relative, and
absolute limits. The larger measured bound is preserved for both twins; no
cell is clipped or rescaled.

## Evidence And Interpretation Boundary

Authoritative evidence:

- A11 owns the common body depth.
- Step 09A owns the two local `C04` source intervals.
- The approved width rule preserves the larger measured output bound.
- Flamestrike owns the twin identity and exact shared XYZ decision.

Candidate blueprint rules pending review:

- construct the nonvariant shared body once;
- require canonical equality of that shared base across both assets;
- permit geometry/topology differences only in the tagged local `C04`
  treatment; and
- require every future surface to cite approved source ownership and an exact
  equation.

The common envelope is a validation bound, not fill geometry. If a future
surface lacks exact source ownership or a connection equation, the builder
must stop with the applicable Blueprint block.

## Independent Validation

- Result: `66/66 PASS`.
- Blueprint:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json`
- Blueprint SHA-256:
  `efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58`.
- Validation:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_VALIDATION.json`
- Validation SHA-256:
  `48e53e3ddfff94319927aebaec47fcbe9c40ea7369c20a4b73cdc0c38fa47ff5`.

The validation independently replayed all authority hashes, rational
dimensions, width limits, local spans, local insets, shared-bound equality,
invalid-rule guards, and the documentation-only software boundary.

## Current Stop

No builder, Blender, geometry, Foe Hammer source fork, Step 13, retopology,
UV, bake, export, or Unreal action is authorized.

Flamestrike must approve, reject, or mark this blueprint blocked. Approval of
this blueprint would still require a separate visible fresh-builder contract
before any production action.
