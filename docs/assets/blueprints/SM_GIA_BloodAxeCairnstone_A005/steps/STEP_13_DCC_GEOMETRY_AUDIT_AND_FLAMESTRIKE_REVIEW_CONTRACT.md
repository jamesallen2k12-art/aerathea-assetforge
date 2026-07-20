# A005 Step 13 DCC Geometry Audit And Flamestrike Review Contract

Status: approved for complete Step 13 execution

Artifact classification: `authoritative execution boundary`

Contract ID: `A005-CR-STEP13-DCC-GEOMETRY-REVIEW-A01`

Date: 2026-07-20

## Flamestrike Authority

Flamestrike stated: `resume    You have full Approval and Authority to complete
step 13 from beginning to end, no matter what is required`.

Under Core, this authorizes preparation, immutable input locking,
non-mutating DCC inspection, exact fixed-camera/source comparison, proof-only
diagnostics, evidence-bound approval/rejection/block classification, visible
desktop review, status closeout, checkpointing, exact scoped Git closeout,
push, remote verification, and the mandatory post-Step-13 restart for this
contract only. It does not override the Blueprint or authorize geometry
repair, UVs, textures, materials, LODs, collision, FBX, Unreal, visual-canon
reclassification, or Step 14 execution.

## Controlling Decision

Audit the unchanged Step 12 `SM_GIA_BloodAxeCairnstone_A005` DCC source
candidate against the source panels, exact measurement contracts, approved
Step 10/11 interpretations, 360-degree coherence, and Aerathea geometry
requirements. Close Step 13 with exactly one result:

- `approved` for later Step 14 contract preparation;
- `rejected` with an evidence-linked mismatch list; or
- `blocked` with the missing or conflicting authority identified.

The Step 12 numeric pass is necessary evidence but is not visual-fidelity
approval. Step 13 must separately distinguish geometry obligations from the
later C-005/C-006/C-007 and surface-detail consumers reserved to Step 14.

## Required Pre-Action Check

1. Core principle: Evidence-Bound Decision, First Principles, Kaizen,
   Stop-the-Line, and closed-world authorization.
2. Blueprint authority: Step 13 of
   `BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`, the
   authoritative Step 12 closeout, and the Step 12-to-Step 13 handoff.
3. Flamestrike approval: complete Step 13 start-to-finish authority quoted
   above.
4. Smallest sufficient change: one immutable input lock, one independent
   read-only auditor/review packager, proof-only comparisons, one decision
   record, one handoff, and bounded status updates; candidate geometry remains
   byte-identical.
5. Decision output: one evidence-bound `approved`, `rejected`, or `blocked`
   classification that Flamestrike can inspect visibly.
6. Drift control: SHA-256 input locks, candidate and source before/after hash
   equality, no Blender save operation, exact changed-path allowlist, no
   production-path writes outside the Step 13 proof root, and fail-closed
   classification.

Pre-action checkpoint:
`Saved/ProjectRecovery/20260720-160223/`.

## Immutable Review Boundary

`manifests/STEP_13_INPUT_LOCK.json` controls every direct file consumed by the
auditor. The authoritative Step 11 and Step 12 input locks preserve the
transitive source, measurement, interpretation, and construction chain.

The following candidate artifacts must remain byte-identical throughout Step
13:

- `SM_GIA_BloodAxeCairnstone_A005_DCCSource_A01.blend`;
- `SM_GIA_BloodAxeCairnstone_A005_GEOMETRY_MANIFEST.json`;
- `build_bloodaxe_cairnstone_a005_step12_dcc_source.py`;
- every Step 03 source panel;
- every Step 12 clean proof render.

## Geometry Review Authority

The review must apply these boundaries:

- C-001 through C-004 are the only Step 13 geometry subjects.
- C-001 must preserve the approved view-owned faceted construction. Analytic
  smoothing or a generic rounded primitive is forbidden, so a deliberately
  faceted body is not by itself a defect.
- C-002 and C-003 are independent watertight masonry-course envelopes.
  Individual stone divisions are later Normal/Base Color consumers except
  for any source-critical silhouette break already carried by the approved
  source-owned profiles.
- C-004 is the irregular peripheral apron envelope. Small-rubble microdetail
  is a later Normal/Base Color consumer; its approved macro boundary remains
  N3/K80 with the exact front/left inward-refinement limit.
- C-005, C-006, and C-007 have zero Step 13 geometry authority. Their absence
  from the untextured candidate is not a geometry defect and must be recorded
  as deferred Step 14 work, not silently approved as finished appearance.
- Stone cracks, grain, small chips, small runes, paint/inlay response, and
  micro-rubble are texture/Normal/material subjects unless an approved
  geometry authority explicitly says otherwise.
- Macro silhouette, component nesting, source-owned critical breaks, exact
  dimensions, contact coherence, watertightness, visible hidden closures,
  object transforms, pivot, face/normal integrity, and complete 360-degree
  plausibility are Step 13 geometry subjects.

## Allowed Outputs

- `Tools/DCC/audit_bloodaxe_cairnstone_a005_step13_geometry_review.py`;
- `manifests/STEP_13_INPUT_LOCK.json`;
- `manifests/STEP_13_DCC_GEOMETRY_REVIEW_AUDIT.json`;
- proof-only diagnostic JSON, six exact fixed-camera comparison PNGs, and one
  review board under
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/Step13/`;
- `review/STEP_13_DCC_GEOMETRY_REVIEW.md`;
- `steps/STEP_13_OUTPUT_RECORD.md`;
- `handoffs/STEP_13_TO_STEP_14_HANDOFF.md` only on approval, or an exact
  rejected/blocked handoff otherwise;
- bounded Step 13 entries in the A005 approval log, artifact index, and
  reset/resume state;
- recovery-journal entries created by the required checkpoint tool.

## Required Audit Gates

The auditor must fail closed unless all applicable gates pass:

1. all immutable direct inputs exist as regular non-symlink files and match
   the Step 13 lock;
2. the contract ID and Flamestrike statement match exactly;
3. the `.blend`, geometry manifest, source panels, and Step 12 proof views are
   unchanged before and after the audit;
4. Blender opens the candidate without saving, exactly four required mesh
   objects exist, and C-005/C-006/C-007 geometry remains zero;
5. evaluated transforms, bounds, pivot, units, component names, shell
   topology, face normals, manifoldness, volume, and triangle count remain
   coherent;
6. the approved Step 12 numeric/authority audit still reports all required
   passes and its candidate hash matches the audited `.blend`;
7. front and left construction-owner comparisons preserve the approved exact
   source observations and Step 11 piecewise-linear interpretations;
8. back and right remain non-metric validation holdouts and introduce no
   construction-coordinate claims;
9. top comparison preserves approved N3/K80 containment and 360-degree
   component nesting without claiming one unified source-pixel transform;
10. perspective comparison is explicitly non-metric and corroborates a
    coherent assembled object without underside, clipping, or detached
    carrier/projection geometry;
11. hidden contact closures and the three one-centimeter overlaps are not
    exposed in any clean review view;
12. C-005/C-006/C-007 and micro-surface differences are classified as
    deferred Step 14 consumers, not geometry mismatches;
13. every actual macro-geometry mismatch is evidence-linked by view,
    component, authority source, and disposition;
14. exact fixed-camera comparisons and a legible review board exist and are
    classified `proof only`;
15. the review record states exactly one decision and the resulting candidate
    classification/hash;
16. the review board and Markdown decision record are opened automatically in
    persistent visible desktop windows;
17. no candidate, source, UV, texture, material, LOD, collision, FBX,
    Content, Unreal, or visual-canon artifact changes;
18. changed and staged paths remain inside the Step 13 allowlist; unrelated
    user work remains untouched and unstaged;
19. a final checkpoint, exact scoped commit, push to `assetforge/main`, and
    local/remote hash verification succeed before completion; and
20. the closeout requires a mandatory restart and grants only later Step 14
    contract preparation on an approved result.

## Decision Rule

Approve only if every applicable technical gate passes, all macro-geometry
findings are pass or explicitly non-geometry/deferred under existing
authority, the candidate is coherent from all six review views, and no source
or authority mutation occurs.

Reject if the unchanged candidate has one or more evidence-linked
macro-geometry defects that can be evaluated under existing authority.

Block if the decision depends on missing, incomplete, or conflicting source,
measurement, interpretation, or visual authority. Do not invent a repair or
resolve a block through visual preference.

## Blocked Methods

- geometry repair, replacement, smoothing, fitting, sculpting, decimation,
  retopology, remeshing, vertex movement, modifier application, or `.blend`
  save;
- source raster mutation, rectification, crop replacement, resampling as
  evidence, or candidate-filled interpretation overlay;
- treating C-005/C-006/C-007, stone cracks, microchips, individual rubble, or
  material response as required Step 13 geometry without explicit authority;
- UV, texture, material, Normal, ORM, emissive, LOD, collision, FBX, Unreal,
  visual-canon, or Step 14 production work;
- legacy A001-A004 asset-specific input;
- staging, committing, or pushing unrelated work.

## Completion And Restart

After one evidence-bound decision, open the review board and decision record
visibly, update the bounded A005 status records, create the required final
checkpoint, commit only the exact Step 13 dependency scope, push `main` to
`assetforge`, verify exact local/remote equality, record closeout metadata,
and stop for the mandatory post-Step-13 restart. Do not begin Step 14 in this
session.
