# Proposed Step 12 A01 Contract — Fresh DCC Source Geometry Candidates

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract ID: `SB-CR-R8-STEP12-FRESH-DCC-SOURCE-GEOMETRY-A01`
- Recovery run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Current artifact status: `candidate`
- Current contract status: `draft only; waiting for exact Flamestrike approval`
- Drafting authority: Flamestrike's exact response,
  `Yes I authorize you to draft Step 12`
- Step 12 execution authority now: `false`
- Blender / builder / geometry / render / export / Unreal authority now:
  `false / false / false / false / false / false`
- Maximum classification after a later approved, passing execution:
  `DCC source candidate`

## Contract Effect

This document does not authorize or execute itself.

If Flamestrike later approves this exact document by its recorded SHA-256, that
approval authorizes only the Step 12 actions, files, gates, and stop condition
declared below. It does not authorize Step 13, production UVs or materials,
LODs, collision, FBX/GLB export, Unreal work, visual-canon promotion, a
`DCC game-ready candidate`, or `Fully game-ready` status.

## Core Decision

Build fresh, deterministic, watertight, source-aligned LOD0 geometry for both
candidate variants named by the authoritative Step 11 blueprint:

1. `rune_side`;
2. `metal_center_piece_side`.

The variants remain independent. They may not be averaged, normalized,
stretched to one common depth, merged into a third variant, or selected by
Codex. Step 12 decides only whether each exact variant passes the technical
`DCC source candidate` gate.

## Controlling Authority

Authority is applied in this order:

1. `AGENTS.md` Core Principles and closed-world authorization rules.
2. Flamestrike's later exact approval of this contract, if granted.
3. Step 11 decision approval record:
   `STEP_11_PRODUCTION_BLUEPRINT_A02_DECISION_APPROVAL_RECORD.md`,
   SHA-256
   `e2c9957e9f1bb3ccdaa56406b3f81f47c8aff647cb02d0c3520b3117eb3c6d2a`.
4. Step 11 authority lock:
   `../manifests/STEP_11_PRODUCTION_BLUEPRINT_A02_AUTHORITY_LOCK.json`,
   SHA-256
   `3235fcc9480ad246f968b275792aa3a309aa34710b5bfec3fc005980ae3d5069`.
5. Authoritative Step 11 construction blueprint:
   `../manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json`,
   SHA-256
   `2b598497ba5e61a4352c217f3fb20b3545189c710934f3a21d9b7398ddb472c7`.
6. Every hash-locked item in that blueprint's `authority_files` catalog.
7. The authoritative Steps 01–16 process plan where it does not conflict with
   later approved R8 recovery authority.

The blueprint's embedded `artifact_status` value records its pre-decision
history. The later Step 11 decision record and authority lock control its
current `authoritative` classification.

## Proposed Resolution Of Two Step 11 Placeholders

These rules are proposed by this contract and remain non-authoritative until
Flamestrike approves the exact contract.

### Recovery-Route Input Rule

The general process plan's Step 12 phrase `approved A06 records only` may not
be used to read A05, legacy A06, or invalid parent-run construction artifacts.
For this R8 recovery run, the complete permitted construction-input set is
only the Step 11 blueprint plus the exact hash-locked `authority_files` catalog
inside it.

This proposed rule explicitly resolves the old route label in favor of the
later Flamestrike-approved R8 recovery authority.

### Fresh Output Root And Variant Rule

The Step 11 placeholder `<fresh-isolated-root>` is proposed as:

`SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_Step12_SourceGeometry_A01`

The root must not exist when execution begins. If it exists, execution stops
with:

`Blueprint block: rule missing — approved clean output root is not fresh`

Step 12 will execute one isolated Run A for each of the two blueprint variants:

- `run_a/rune_side`;
- `run_a/metal_center_piece_side`.

The blueprint's `run_b` roots, interruption replay, and negative-test matrix
remain reserved for the later Step 16 reproducibility gate.

## Required Preflight Before Any Blender Process

The later approved execution must:

1. create a manual Aerathea checkpoint;
2. verify the exact contract hash recorded by Flamestrike's approval;
3. verify all four controlling Step 11 hashes above;
4. independently verify every path and SHA-256 in the blueprint's
   `authority_files` catalog;
5. verify the active state is exactly
   `step11_approved_authoritative_step12_locked`;
6. verify neither candidate output root exists;
7. verify no permitted builder or validator output path would overwrite an
   existing file;
8. write and independently validate
   `../manifests/STEP_12_ENVIRONMENT_LOCK_A01.json`;
9. verify network access is disabled for production;
10. verify every required environment field before Blender starts; and
11. fail closed on every missing, changed, unreadable, or conflicting input.

The environment lock must record:

- Blender binary path and SHA-256;
- Blender version;
- Python version;
- OS and architecture;
- locale and unit system;
- color-management settings;
- render backend and device class;
- dependency versions and hashes;
- fixed seeds; and
- network-disabled state.

No environment default may be inferred.

## Exact Allowed Implementation Files

After approval, Step 12 may create only these implementation tools:

- `Tools/DCC/build_siegebreaker_r8_step12_source_geometry_a01.py`;
- `Tools/DCC/audit_siegebreaker_r8_step12_source_geometry_a01.py`.

The independent validator may not import the builder, trust builder booleans,
trust Blender custom properties as proof, or read expected values from build
outputs. It must derive expected authority directly from the hash-locked Step
11 blueprint and its cited source records.

No existing authority, source, builder, validator, manifest, Blender file, or
review artifact may be modified.

## Manifest-Driven Entry Point

The only permitted production entry point is the exact Step 11 command shape:

```text
python3 Tools/DCC/build_siegebreaker_r8_step12_source_geometry_a01.py \
  --blueprint docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json \
  --candidate {rune_side|metal_center_piece_side} \
  --output-root SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_Step12_SourceGeometry_A01/run_a/{candidate}
```

The wrapper must invoke only the Blender binary recorded in the environment
lock. Manual Blender editing and an interactive production decision are
forbidden.

## Required State Path

Each candidate must traverse the Step 11 state path exactly once:

1. `STEP_11_BLUEPRINT_APPROVED`;
2. `STEP_12_AUTHORITY_VERIFIED`;
3. `STEP_12_SOURCE_HALF_BUILT`;
4. `STEP_12_SOURCE_HALF_AUDITED`;
5. `STEP_12_RZ180_COMPLETED`;
6. `STEP_12_SAVED_CANDIDATE_AUDITED`;
7. `STEP_12_REVIEW_READY`.

Every transition must be written to an append-only event trace with:

- monotonic event index;
- UTC timestamp;
- state before and after;
- candidate variant;
- command and parameters;
- input hashes;
- output hashes;
- tool versions;
- observed check result; and
- failure or retry reason.

An illegal transition stops the run and preserves the last independently
verified state. Resume is allowed only from an output whose canonical hash and
state-transition record independently verify.

## Exact Geometry Scope

For each candidate, the builder must:

1. replay every one of the blueprint's `17` surface instructions;
2. replay every one of its `16` closure, contact, cap, guard, and completion
   instructions;
3. use only each instruction's cited ownership, equation, and measurement
   references;
4. build one coherent source set;
5. build the selected C04 owner half and apply exactly one local `Y=0` mirror;
6. preserve every reserved central axial pixel as non-geometric evidence;
7. build only declared shared contacts, ruled faces, shoulders, and caps;
8. leave every protected negative space empty;
9. apply exactly one whole-asset
   `(X,Y,Z)->(-X,-Y,Z)` completion;
10. weld only coordinate-equal seam vertices; and
11. save only after the direct independent pre-render audit passes.

The exact completed bounds are:

- `rune_side`:
  `97.873941674506 x 34.434306569343 x 170.000000000000 cm`;
- `metal_center_piece_side`:
  `97.873941674506 x 43.120437956204 x 170.000000000000 cm`.

The pivot is bottom-center terminal/pommel at world `(0,0,0)`.

LOD0 target is `8,000` triangles. The hard cap is `10,000` triangles.
Source-owned boundaries, protected gaps, contacts, and primary silhouette may
not be removed or moved to meet the target. If faithful LOD0 geometry exceeds
the hard cap, stop before candidate classification with:

`Blueprint block: rule missing — performance amendment required`

## Mandatory Technical Gates

Both the builder preflight and independent validator must prove:

1. all authority hashes match;
2. every constructed surface resolves to one blueprint surface instruction;
3. every hidden face resolves to one closure instruction;
4. no protected source pixel is occupied;
5. no owner pixel is claimed by two visible surfaces in one view;
6. no independent backing wall or copied depth face exists;
7. no extrusion, slab, primitive replacement, or generalized cross-section
   exists;
8. every rotational radius replays from the exact front row;
9. each C04 variant retains its own exact completed depth;
10. one C04 local mirror and one whole Rz180 occur, no more;
11. only coordinate-equal seam vertices weld;
12. pivot is world `(0,0,0)` and height is exactly `170 cm`;
13. LOD0 does not exceed the hard cap;
14. all required volumes are genuine and watertight;
15. topology, normals, transforms, component identities, bounds, and contacts
    are observed directly from the saved Blender candidate; and
16. the canonical geometry record contains exact rational pre-serialization
    positions, face order, normals, transforms, pivot, and bounds.

Missing, skipped, unreadable, or unevaluated checks are failures.

## Proof-Render Gate

No render may begin until authority, numeric, method, topology, normal,
transform, contact, protected-space, pivot, and triangle-cap gates all pass
against the saved candidate.

After that pre-render pass, Step 12 must produce for each variant:

- fixed front, back, left, right, top, and bottom binary silhouette renders;
- source comparison masks and XOR images with observed pixel counts;
- clean front, back, left, right, top, and bottom neutral-clay proofs;
- one neutral-clay three-quarter proof;
- one rotating-parallax/360-degree coherence proof; and
- one wireframe/contact/negative-space diagnostic set.

Only a temporary neutral-clay proof material is allowed. No production UV,
Base Color, Normal, ORM, Emissive, texture, or material work is authorized.

The final Step 12 comparison board must be:

`../review/STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_REVIEW_BOARD.png`

It must compare both variants at identical production scale and camera rules,
label every artifact as `candidate` or `proof only`, and open automatically in
a visible desktop window. A clickable path alone does not satisfy the review
gate.

## Required Output Records

Approved execution may write only:

- the two implementation files named above;
- `../manifests/STEP_12_ENVIRONMENT_LOCK_A01.json`;
- `../manifests/STEP_12_SOURCE_GEOMETRY_A01_MANIFEST.json`;
- `../manifests/STEP_12_SOURCE_GEOMETRY_A01_VALIDATION.json`;
- `../manifests/STEP_12_SOURCE_GEOMETRY_A01_INDEPENDENT_AUDIT.json`;
- `../manifests/STEP_12_SOURCE_GEOMETRY_A01_EVENT_TRACE.jsonl`;
- `STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_APPROVAL_RECORD.md`;
- `STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_OUTPUT_RECORD.md`;
- `../handoffs/STEP_12_TO_STEP_13_HANDOFF_A01.md`;
- files inventoried before creation beneath the exact fresh output root;
- proof files beneath
  `../review/STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01/`;
- the final comparison board named above; and
- mandatory checkpoint, recovery-journal, drift-ledger, or local status
  records required by Core.

Every created file must appear in the Step 12 manifest with its artifact
status and SHA-256. No unrelated dirty worktree file may be read as production
authority, staged, modified, deleted, or committed.

## Explicitly Forbidden

- any method named by the blueprint's `forbidden_methods` list;
- Blender Extrude, Solidify, or any `bmesh` extrusion;
- cube, primitive, slab, card, facade, projection-carrier, detached-shell, or
  backing-block replacement;
- copied depth faces or per-component backing walls;
- source resampling, smoothing, averaging, nearby-row search, or visual fit;
- per-component scale;
- filling a protected gap;
- old mesh, coordinate, mask, UV, material, texture, dimension, or render
  input;
- A05 construction input;
- any invalid or quarantined parent Steps 10–16 output;
- network access, package download, cloud generation, image generation,
  image-to-3D, TRELLIS, TripoSR, or another generative reconstruction method;
- manual mesh edits, sculpting, UV edits, material edits, or validation
  overrides;
- retrying with changed rules, silent fallbacks, or repair-forward;
- LOD1–LOD3, production collision, production UVs/materials/textures, FBX/GLB,
  Unreal, Step 13, or later work; and
- changing any approved Step 11 blueprint byte.

## Pass, Block, And Drift Disposition

### Pass

A variant may be classified `DCC source candidate` only when its saved Blender
file and every mandatory technical and proof gate independently pass.

If both variants pass, both remain separate `DCC source candidate` artifacts
pending Step 13 immutable-geometry and artistic review. Step 12 may not select
one or promote either further.

### Block

If a required authority, rule, environment field, correspondence, boundary,
contact, or performance amendment is missing or conflicting:

1. stop;
2. preserve the last verified state;
3. classify incomplete production output `invalid` or `proof only` according
   to what it actually proves;
4. do not retry; and
5. report the exact `Blueprint block`.

One variant passing does not conceal or repair the other variant's failure.
The Step 12 package remains `blocked` until Flamestrike decides the disposition.

### Drift

If execution departs from the approved contract or blueprint:

1. stop production immediately;
2. identify the last Core-valid state and first drift action;
3. quarantine all affected outputs;
4. record the event in `docs/projects/assetforge/DRIFT_LEDGER.md` and the local
   asset status record; and
5. do not repair forward.

## Checkpoint, Commit, And Stop

An approved long Blender execution requires:

1. a manual checkpoint before the first Blender process;
2. a manual checkpoint after pass, block, failure, or drift;
3. staging only the exact dependency-complete Step 12 scope;
4. committing and pushing only valid scoped tracked work to
   `assetforge/main`; and
5. preserving invalid or quarantined production outputs in their declared
   local quarantine location rather than promoting them.

After the final review board opens, stop and present:

- both candidate classifications;
- all proof and audit results;
- files created;
- assumptions or interpretations made;
- blockers or uncertainty;
- artifact statuses; and
- the exact Step 13 approval need.

No Step 13 action follows automatically.

## Exact Approval Gate

Approval must answer this exact question:

> Do you approve this exact hash-locked Step 12 A01 contract and authorize its
> execution for both `rune_side` and `metal_center_piece_side`, including the
> fresh deterministic builders, isolated Run A Blender builds, independent
> audits, proof renders, visible comparison board, scoped checkpoints, commit,
> and push—then stop before Step 13?

Until Flamestrike answers that question with `approved`, `yes`, or `proceed`,
Step 12 remains locked and no production action is authorized.

