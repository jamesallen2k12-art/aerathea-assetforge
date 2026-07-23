# Step 09A Contract — Exact Component-Pixel Ownership Interpretation

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Amendment ID: `SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01`
- Parent evidence run: `SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01`
- Recovery run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Status: `authorized by Flamestrike`
- Artifact ceiling: `candidate source-ownership interpretation`
- Geometry / Blender / export / Unreal authority:
  `false / false / false / false`

## Decision

Produce one reviewable, coordinate-bearing ownership interpretation for the
component surfaces and protected gaps that blocked Step 11.

The result must let Flamestrike approve, revise, reject, or keep blocked:

- `C01_CENTER_CORE` in the new front source;
- `C02_STONE_LEFT` in front, top, and bottom;
- `C03_STONE_RIGHT` in front, top, and bottom;
- `C04_STRIKE_FACE_POSITIVE_X` separately for the rune-side and
  metal-center-piece-side right-source halves;
- `C06_UPPER_HAFT_CAP` in the new front source;
- source-connected negative spaces between those owners; and
- the exact ordered boundary-edge sets available to the approved ruled-closure
  process.

## Governing Authority

1. `AGENTS.md`.
2. Flamestrike's exact Step 09A approval record.
3. `SM_DRW_SiegeBreaker_Hammer_A01_STEPS_01_16_PROOF_OF_CONCEPT_PIPELINE_PLAN.md`.
4. `A12_R10_R8_PIXEL_EXACT_STEPS01_16_A01_CONTRACT.md`.
5. The valid Step 01-09 source locks, complete-hammer captures,
   registrations, and measurements.
6. The independently passed Step 10 interpretation and numeric-precedence
   records.
7. The approved component-equation and deterministic-closure rules.

## Exact Inputs

- Six immutable R8 PNGs at the source hashes locked by Step 02.
- Six immutable complete-hammer selected-pixel captures:
  - front:
    `57f11e52d410e5f0fba858276e8dad89fb34e10b93a829e6ccac5af69c803047`;
  - back:
    `453649488a8f9c320ff533461d90c2a4e536060f2e074cadeedcdef0f8620701`;
  - left:
    `9464cce559f975b3855e3e9d894826441924607ffea2884f73c60235e6d26489`;
  - right:
    `cb15d0a2806ca00d716984c929a22a29331893c5117672b571622c0924c2a098`;
  - top:
    `731272c89dae717b646f067e5337c14de0781ec11e01858efe50655aaa222d94`;
  - bottom:
    `da989819826b07e09049e422487a1bb5590dce576796be204c019bec2916ba11`.
- Front component stations:
  `A=600`, `C=670` source edges.
- Right construction axis: `x=557`.
- Right candidate intervals:
  rune side `[557,668)` and metal-center-piece side `[418,557)`.

## Allowed Interpretation Method

1. Decode the existing selected-pixel captures without changing any source
   pixel or membership.
2. Apply the already approved 4-connected exterior rule:
   unselected pixels connected to the source rectangle exterior remain
   protected; fully enclosed omitted pixels may be recorded separately as
   enclosed source-owned pixels.
3. Record visible component contacts as integer source-pixel edges.
4. Where a source-connected gap visibly separates owners, preserve both exact
   gap edges and every unowned pixel run.
5. Where visible components touch with no gap, record one shared source-edge
   cut. A deterministic interpolation between the nearest exact separated
   observations may be proposed only as an interpretation and must remain
   visibly marked for Flamestrike's decision.
6. Preserve every boundary sequence in source-pixel order. Correspondence
   groups may name and order exact boundary sets; they may not create a ruled
   face, resample a curve, or invent a hidden surface.

## Evidence Separation

- Immutable source pixels, prior captures, hashes, scales, axes, and component
  stations are `authoritative evidence`.
- New component assignments, shared contact cuts, and correspondence groups
  are `candidate interpretation`.
- Independent coordinate replay and subset/overlap checks are `proof only`.
- Review images may show source pixels and thin exact marks only. They may not
  show a component fill, inferred volume, smoothed contour, or geometry-like
  solution.

## Required Outputs

- `manifests/STEP_09A_INTERPRETATION_INPUT.json`;
- `evidence/STEP_09A_COMPONENT_SCANLINES.json.gz`;
- `manifests/STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json`;
- four marked source reviews for front, right, top, and bottom;
- one combined visible review board;
- `manifests/STEP_09A_VALIDATION.json`;
- an output record and blocked-or-candidate handoff.

## Independent Validation

The validator must independently read the immutable capture bytes and prove:

- every owner pixel is an exact source coordinate inside its owning capture;
- every owner pixel is either already selected or exactly enclosed by the
  approved 4-connected rule;
- component owner sets do not overlap inside one candidate/view;
- protected negative-space pixels are exterior-connected and unowned;
- all source-edge coordinates lie inside the locked rectangles;
- every boundary sequence is ordered and references existing owner or
  protected-gap edges;
- right-source ownership stays inside the exact candidate intervals and about
  `x=557`;
- review files are reproducible from the candidate record; and
- no blueprint, DCC, geometry, render, export, or Unreal artifact is created.

## Gate

- Complete coordinate record plus independent pass:
  `candidate pending Flamestrike source-ownership decision`.
- Missing, overlapping, out-of-source, or unpaired required record:
  `Blueprint block: source authority missing`.

In either case, stop after opening the review. Step 11 remains locked until
Flamestrike separately approves the finished ownership interpretation.
