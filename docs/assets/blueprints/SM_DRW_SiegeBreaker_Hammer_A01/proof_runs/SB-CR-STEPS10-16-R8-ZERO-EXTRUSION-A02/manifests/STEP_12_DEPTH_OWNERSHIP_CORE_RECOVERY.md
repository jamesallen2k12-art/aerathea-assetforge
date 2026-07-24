# Step 12 Depth-Ownership Core Recovery

- Date: `2026-07-24`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01` / Siege Breaker
  - `SM_DRW_FoeHammer_Hammer_A01` / Foe Hammer
- Run under recovery: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Recovery status: `authoritative`
- Production status: `stopped`
- Step 13 authority: `false`
- Blender rebuild authority: `false`
- Unreal authority: `false`

## Approved Decision

Flamestrike clarified and approved the following controlling truths:

1. Siege Breaker and Foe Hammer are twin assets with identical overall
   dimensions and the same body and hammer-face envelope.
2. Siege Breaker uses the rune-side treatment on both strike faces.
3. Foe Hammer uses the metal-center-piece treatment on both strike faces.
4. The unequal rune and metal source spans describe local `C04` face
   treatments. They do not define two different global hammer-body depths.
5. The common body depth is the larger, already approved axial depth:
   `6644212/149985 cm`, displayed as `44.299176584 cm`.

This decision is authoritative within the twin-identity, dimension-ownership,
and recovery-classification scope. It does not authorize geometry execution.

## Evidence Versus Approved Interpretation

### Proven Evidence

- The A11 axial measurement explicitly assigns head-depth scale to the
  top/bottom axial views.
- Its approved exact full depth is:
  `6644212/149985 cm = 44.299176584 cm`.
- Its exact half depth is:
  `3322106/149985 cm = 22.149588292163 cm`.
- A11 manifest SHA-256:
  `46877ab4b0142d8141deb4feab234f461a31e61e118d3ce7b41e0b3679786096`.
- The independent A11 audit passed `26/26`.
- Independent A11 audit SHA-256:
  `4d4e46b2d1ad71bbdcc8952d85063601b672f4835a2bb95c03f2a7e49eeaff07`.
- Step 09A names the relevant evidence
  `RIGHT_C04_CANDIDATE_HALF_BOUNDARIES` and records two candidate-specific
  `C04` source intervals about the right-view rotation axis `x=557`:
  - metal-center-piece side: `[418,557)`, `139 px`;
  - rune side: `[557,668)`, `111 px`.
- Step 09A boundary index SHA-256:
  `e190ed266753c797d4f9ec812154ff3b29f5d5d780e53e235e780c43492d0bd8`.
- At the unchanged right-view scale, the local completed `C04` spans are:
  - rune: `9435/274 cm = 34.434306569343 cm`;
  - metal centerpiece: `11815/274 cm = 43.120437956204 cm`.
- Both local spans fit inside the common axial body envelope.

### Approved Meaning

The `C04` values above are local face-treatment extents:

- the rune treatment reaches
  `9435/548 cm = 17.217153284672 cm` from the center plane and is inset
  `405405613/82191780 cm = 4.932435007491 cm` per side from the common
  outer envelope;
- the metal-center-piece treatment reaches
  `11815/548 cm = 21.560218978102 cm` from the center plane and remains
  `48441313/82191780 cm = 0.589369314060 cm` per side inside the common
  outer envelope.

The metal treatment extends farther from the center plane than the rune
treatment, but neither local value replaces the global body depth.

## Core Recovery Finding

### Last Known Core-Valid State

The last known Core-valid authority before the depth drift is:

1. the A11 axial outer-footprint measurement and its approved depth ownership;
2. the Step 09A local `C04` ownership boundaries and source pixels;
3. the approved one-scale source registration and one `Rz(180 degrees)`
   completion rule, within their unchanged scopes; and
4. Flamestrike's twin-identity selection: Siege Breaker is double rune sided
   and Foe Hammer is double metal-center-piece sided.

### First Drift Action

Drift began in Step 10 when the local `C04` completed spans were promoted to
candidate-specific **final global depth**:

- rune `34.434306569343 cm`;
- metal centerpiece `43.120437956204 cm`.

The affected Step 10 output record has SHA-256:
`583c1c66810ea1d02f5cd6727fe9785aff26f5c2eee3ec234a9b7543cc95ec8f`.

### Assumption That Caused Drift

The process assumed that the distance from the right-view rotation axis to
each candidate-specific `C04` owner edge represented the entire hammer-body
half depth. The source record identifies those intervals as local `C04`
face-treatment boundaries; it does not transfer global body-depth ownership
away from A11.

### Propagation

Step 11 encoded each local span as `source_half_depth_cm`,
`front_envelope_y_cm`, and `completed_dimensions_cm.depth`. It then used
`EQ_CANDIDATE_AXIAL_INTERSECTION` to clip the axial body evidence to that
candidate-specific value.

- Step 11 blueprint SHA-256:
  `2b598497ba5e61a4352c217f3fb20b3545189c710934f3a21d9b7398ddb472c7`.

The Step 12 builder read `source_half_depth_cm` into one global `half_depth`
value and used it for the front-owned body surfaces, axial surfaces,
closures, and expected bounds.

- Step 12 builder SHA-256:
  `85356eb4f79e5c83fbb84c6add3d94f36325553bb715068774d351fc5f0f4032`.
- Step 12 independent auditor SHA-256:
  `4e7a3a4c3d6e3b85ffab66f56f404393cd0379a6bb8953286843844e676aa443`.

The saved geometry therefore passed its declared implementation checks while
implementing an invalid global-depth premise. The arithmetic was correct; the
semantic ownership was not.

## Exact Twin-Dimension Rule

Every future valid Siege Breaker and Foe Hammer candidate must:

- use one identical overall XYZ envelope;
- use the common full body depth
  `6644212/149985 cm = 44.299176584 cm`;
- retain the same shared body, hammer-face, scale, pivot, and longitudinal
  construction;
- vary only the local doubled `C04` face treatment;
- preserve the local source-pixel intervals without stretching;
- avoid using either local `C04` span as a global clipping plane; and
- pass an exact cross-asset bounding-dimension equality audit.

The shared height remains `170 cm`. This recovery does not change the existing
shared front-view width authority or its approved cross-view tolerance; it
removes only the candidate-specific global-depth substitution.

## Affected Outputs And Classification

### Authoritative And Unaffected

- A11 axial outer-footprint and depth ownership:
  `authoritative`.
- Step 09A source pixels and local `C04` boundaries:
  `authoritative within measured ownership scope`.
- Siege Breaker/Foe Hammer twin identity and doubled-treatment selection:
  `authoritative`.

### Partially Invalid Step 10 Family

The Step 10 decision/output, numeric substitution, validation, review, and
Step 10-to-Step 11 handoff records are:

- `invalid` wherever they assign final global depth to the rune or metal
  `C04` span;
- `proof only` for the exact interval arithmetic they replay; and
- not construction authority for a recovery build.

They remain preserved in place as historical evidence.

### Invalid Step 11 Construction Family

The Step 11 production blueprint, its authority lock, validations, approval
and output records, review, handoffs, and later amendments are
`invalid / quarantined in place` as construction authority because they
inherit the candidate-specific global-depth premise.

Their unchanged source hashes, exact local `C04` equations, and narrow
mechanical audit results remain `proof only` within the checks they actually
performed.

### Invalid Step 12 Construction Family

The following are `invalid / quarantined in place` as production geometry:

- `Tools/DCC/build_siegebreaker_r8_step12_source_geometry_a01.py`;
- `Tools/DCC/audit_siegebreaker_r8_step12_source_geometry_a01.py`;
- the Step 12 contract, approval, manifest, validation, independent audit,
  event trace, output record, state, and Step 12-to-Step 13 handoff wherever
  they depend on candidate-specific global depth;
- both complete `run_a/rune_side/` and
  `run_a/metal_center_piece_side/` output families, including `.blend`,
  canonical geometry, inventories, manifests, audits, validations, and
  renders; and
- `STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_REVIEW_BOARD.png`.

The `105/105 PASS` results and the dual-candidate validation remain
`proof only` for implementation consistency. They do not prove correct
dimension ownership and cannot support either asset's advancement.

No file was moved, deleted, renamed, or overwritten. In-place quarantine
preserves the hash-locked evidence and avoids breaking its lineage.

## Current Asset Status

### Siege Breaker

- Identity selection: `authoritative`.
- Required treatment: `double rune sided`.
- Current valid geometry: `does not exist`.
- Former Step 12 rune geometry: `invalid / quarantined in place`.
- DCC source candidate: `false`.

### Foe Hammer

- Identity selection: `authoritative`.
- Required treatment: `double metal-center-piece sided`.
- Current valid geometry: `does not exist`.
- Former Step 12 metal geometry: `invalid / quarantined in place`.
- Standalone Foe Hammer source: `does not exist`.
- DCC source candidate: `false`.

## Smallest Sufficient Recovery

Do not repair either Step 12 mesh forward.

A separately approved recovery contract must first replace the invalid
Step 10/11 global-depth rule with:

1. one common axial body envelope;
2. local `C04` offsets inside that envelope;
3. exact shared-dimension equality gates for both assets; and
4. a fresh build from the last Core-valid evidence, with no geometry reuse
   from either quarantined Step 12 candidate.

Until that contract is stated and approved, Blender, geometry, Step 13,
retopology, UVs, baking, export, and Unreal remain locked.
