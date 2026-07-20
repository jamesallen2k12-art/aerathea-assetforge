# A005 Step 12 DCC Source Geometry Candidate Contract

Status: approved for complete Step 12 execution

Artifact classification: `authoritative execution boundary`

Contract ID: `A005-CR-STEP12-DCC-SOURCE-GEOMETRY-A01`

Date: 2026-07-20

## Flamestrike Authority

Flamestrike stated: `resume    you have full authority and full approval to
complete step 12 from start to finish no matter what is required`.

Under Core, this authorizes preparation, visible presentation, execution,
validation, proof rendering, Step 12 classification, checkpointing, exact
scoped Git closeout, push, remote verification, and the mandatory post-Step-12
restart for this contract only. It does not override the Blueprint or authorize
Step 13 repair/review decisions, UVs, textures, materials, LODs, collision,
FBX, Unreal, or any other downstream production.

## Controlling Decision

Build exactly one fresh Blender DCC source geometry candidate for
`SM_GIA_BloodAxeCairnstone_A005` that consumes the approved Step 11
construction blueprint exactly and satisfies Blueprint Step 12.

The pass status is `DCC source candidate`. The candidate is not DCC game-ready,
fully game-ready, approved geometry, or visual canon.

## Pre-Action Check

1. Core principle: Evidence-Bound Decision, First Principles, Kaizen,
   Stop-the-Line, and closed-world authorization.
2. Blueprint authority: Step 12 of
   `BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`, the
   authoritative Step 11 blueprint package, and the Step 11-to-Step 12 handoff.
3. Flamestrike approval: complete Step 12 start-to-finish authority quoted
   above.
4. Smallest sufficient change: one fresh A005-only generator, one independent
   auditor, four separate primary shells, one `.blend`, one complete geometry
   lineage sidecar, audit/proof outputs, and Step 12 closeout records.
5. Decision output: `candidate`, `blocked`, or `invalid`; only a complete audit
   pass permits source-aligned proof rendering and `candidate` classification.
6. Drift control: immutable input hashes, schema-only preflight incapable of
   output, fresh A005-only output roots, exact path allowlist, independent
   audit, legacy-path firewall, and fail-closed holdouts.

## Immutable Inputs

`manifests/STEP_12_INPUT_LOCK.json` is controlling. Every file actually read
by the generator or auditor must appear in that lock and match SHA-256 before
execution. The locked Step 11 input lock provides the transitive planning
dependency record; direct Step 12 construction inputs are additionally locked
individually.

The pre-action checkpoint is
`Saved/ProjectRecovery/20260720-152708/`.

## Required Construction

- Blender target frame: centimeters; `+X` source-registered right in front,
  `+Y` back, `+Z` up; origin and pivot `(0,0,0)`.
- Build order: C-004, C-003, C-002, C-001.
- DCC objects: `C004_APRON`, `C003_LOWER_TIER`, `C002_UPPER_TIER`, and
  `C001_BODY`.
- Each object must be a separate independently watertight shell.
- Final runtime intent remains one Static Mesh containing four disconnected,
  positively overlapping shells; Step 12 creates no export or runtime asset.
- Front XZ and left YZ are construction owners. Back and right are immutable
  validation holdouts. Perspective is non-metric corroboration only.
- C-001 uses piecewise-linear owner-view profiles and direct planar corner
  facets. No analytic smoothing, averaging, fitted primitive, inferred corner
  vertex, or physical cross-view pairing is allowed.
- C-002 and C-003 remain independent component-specific courses. Neither may
  copy or scale the other; K80 is allowed only for C-003 at CL-003.
- C-004 uses the approved 32-by-3 R3/R5/R7/R9 N3/K80 transition lattice.
  Front/left exact outer anchors may refine inward only; N3 outward exceedance
  is zero. The last-to-first closure is technical topology only and creates no
  symbolic periodic wrap.
- C-004 bottom is the flat undecorated Z=0 N3-bounded cap.
- Contacts CL-001/002/003 use independent caps and exactly 1 cm hidden positive
  intersection thickness, with zero visible overlap pixels.
- C-005/C-006/C-007 create zero vertices, faces, objects, or geometry.
- All generated vertices must map to exactly one primary Step 11 VAG group;
  every record must retain component, visibility, owner/rule, source or
  interpretation authority, and Step 11 technical-rule lineage.
- Object transforms must be applied before audit. Geometry remains in
  centimeters and the scene unit scale remains explicit.

## Exact Bounds And Budget

- assembled height: exactly `220 cm`;
- C-001 maximum width: exactly `120 cm`;
- C-001 maximum depth: exactly `90 cm`;
- C-004 maximum width: exactly `140 cm`;
- C-004 maximum depth: exactly `110 cm`;
- visible base span: exactly `35 cm`;
- contact stations: CL-003 `Z=10`, CL-002 `Z=23`, CL-001 `Z=35` cm;
- hidden component Z ranges: C-004 `[0,10.5]`, C-003 `[9.5,23.5]`,
  C-002 `[22.5,35.5]`, C-001 `[34.5,220]` cm;
- LOD0 candidate hard cap: `10,000` triangles; target `8,000` triangles.

## Fresh Generator And Schema-Only Boundary

Create only
`Tools/DCC/build_bloodaxe_cairnstone_a005_step12_dcc_source.py` as the Step 12
generator. It must be new, A005-only, and must not import, call, parse, or copy
any prior A001-A004 or A005 geometry builder.

The generator must implement `--schema-only`. That path must terminate before
`bpy` import, output-directory creation, file writes, scene mutation, or
Blender launch and must validate argument schema, A005-only path/constants,
required input names, and declared output names.

All geometry-driving constants must be read from locked approved A005
manifests. The generator may derive deterministic interpolation values only by
the approved formulas and must record those derivations in the geometry
manifest.

## Exact Outputs

Before execution, only these Step 12 production outputs are declared:

- `Tools/DCC/build_bloodaxe_cairnstone_a005_step12_dcc_source.py`;
- `Tools/DCC/audit_bloodaxe_cairnstone_a005_step12_dcc_source.py`;
- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_DCCSource_A01.blend`;
- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_GEOMETRY_MANIFEST.json`;
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/Step12/STEP_12_NUMERIC_AUDIT.json`;
- six clean source-aligned proof PNGs under that Step 12 production root;
- one clean Step 12 review-board PNG under that Step 12 production root;
- `manifests/STEP_12_INPUT_LOCK.json`;
- `manifests/STEP_12_DCC_SOURCE_GEOMETRY_AUDIT.json`;
- `review/STEP_12_DCC_SOURCE_GEOMETRY_CANDIDATE_REVIEW.md`;
- `steps/STEP_12_OUTPUT_RECORD.md`;
- `handoffs/STEP_12_TO_STEP_13_HANDOFF.md`;
- bounded Step 12 status entries in the A005 approval log, artifact index, and
  reset/resume record.

No export, texture, Content, Unreal, collision, LOD, UV, or material path is an
output of this contract.

## Required Audit Gates

The independent auditor must fail closed unless every gate passes:

1. every immutable input exists, is a regular non-symlink file, and matches
   SHA-256;
2. contract ID and Flamestrike statement match exactly;
3. schema-only preflight performs no filesystem write and never imports `bpy`;
4. generator/auditor source is A005-only and contains no legacy builder import,
   legacy asset-specific path, A001-A004 constant, network call, subprocess,
   shell execution, package installation, or dynamic code execution;
5. exactly four required mesh objects exist and C-005/C-006/C-007 geometry is
   zero;
6. scene units, transforms, origin, pivot, axes, bounds, base span, stations,
   and hidden Z ranges match the approved targets;
7. every mesh vertex has exactly one primary VAG assignment and all fourteen
   groups are accounted for with complete lineage;
8. front and left owner-view constraints use only approved piecewise-linear
   normalization; N3 outward exceedance and K80 out-of-scope use are zero;
9. back/right holdouts pass without modifying construction geometry;
10. each primary shell is watertight with zero open/non-manifold edges,
    degenerate faces, duplicate faces, loose vertices, or unsupported
    self-intersections;
11. CL-001/002/003 positive intersection is exactly 1 cm and visible overlap
    is zero in owner/holdout projections;
12. assembled and component bounds match the exact targets within the
    auditor's recorded floating-point tolerance;
13. total evaluated LOD0 triangles are at most `10,000`;
14. the geometry manifest covers every vertex and face range, records hashes,
    derivations, topology, contacts, bounds, holdouts, and blocked methods;
15. Blender source saves successfully and reopens in background validation
    without data loss;
16. no proof render exists before the numeric/topology/holdout audit pass;
17. six clean source-aligned proof views and one review board exist only after
    that pass, and source panels remain byte-identical;
18. all changed paths remain inside the Step 12 allowlist and unrelated user
    work remains unstaged;
19. the review and output records classify the asset only as `DCC source
    candidate` and route to Step 13 without repair;
20. final checkpoint, exact scoped commit, push to `assetforge/main`, and
    local/remote hash verification succeed before completion.

## Proof And Review Boundary

Proof rendering is prohibited until numeric, authority, topology, contact,
budget, and holdout gates pass. After the pass, render clean front, back, left,
right, top, and perspective views. Orthographic views must use the Step 11
axes and ten-percent margin. Perspective orientation must be marker-verified
if uncertain, followed by a clean rerun.

The final board must clearly label the result `DCC source candidate` and
separate source panels from candidate renders. It is proof for Step 13 review,
not Step 12 self-approval of visual fidelity. The review Markdown and board
must be opened automatically in visible desktop windows.

## Blocked Methods

- old builder reuse or reading any A001-A004 asset-specific data;
- consuming `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/CoreRecovery/`;
- projection shells, detached carriers, source-sheet planes, diagnostic masks,
  or geometry from footprint/envelope diagnostics;
- averaging, smoothing, primitive fitting, local warp, visual-fit tuning, or
  source-pixel modification;
- copied/scaled C-002/C-003 contours or K80 outside CL-003;
- cross-view physical pairing, shared source loops, snap anchors, source
  centers, or invented repair rules;
- visible contact overlap, hidden closure exposure, or moving visible contact
  edges to force a pass;
- UV, texture, final material, LOD, collision, FBX, Unreal, or Step 13 repair;
- staging, committing, or pushing unrelated work.

## Fail-Closed Conditions

Stop and classify `blocked` without proof rendering or forward repair on any
input hash mismatch, authority gap, unsupported vertex, missing VAG mapping,
legacy access, source/interpretation relabeling, holdout mismatch, N3
exceedance, out-of-scope K80 use, containment failure, visible overlap,
non-watertight shell, unsupported intersection, triangle-cap failure,
schema-only write, source mutation, Blender reopen failure, or Git-scope
contamination.

## Completion And Restart Rule

On a complete pass, classify the `.blend`, generator, and geometry manifest as
`candidate`; classify audits and renders as `proof only`; update the mutable
A005 status records; visibly open the review; create the required checkpoint;
commit only the exact Step 12 dependency scope; push `main` to `assetforge`;
verify local and remote hashes; record the closeout metadata; and stop for the
mandatory post-Step-12 restart. Do not begin Step 13 in this session.
