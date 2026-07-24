# Step 13 Immutable Geometry And Artistic Review A01 Contract

- Date: `2026-07-24`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01` / Siege Breaker
  - `SM_DRW_FoeHammer_Hammer_A01` / Foe Hammer
- Artifact status: `candidate`
- Current asset status: `DCC source candidate` for both assets
- Step 13 execution authority: `false pending Flamestrike approval`
- Geometry modification authority: `false`
- Retopology / UV / bake / texture / LOD / collision authority: `false`
- Export / Unreal authority: `false`

## Documentation-Gate Authority

Flamestrike approved only this documentation gate:

1. reconcile the stale visual-decision fields in `STEP_STATE.json`;
2. draft and independently audit this Step 13 contract; and
3. stop for an approve, reject, or blocked decision.

That approval does not authorize Step 13 execution. This contract remains a
`candidate` until Flamestrike explicitly approves this exact scope.

## Controlling Decision

If separately approved, Step 13 will audit the two byte-identical saved source
inputs without changing or resaving either `.blend`. It will decide whether
each current high-poly source:

1. still satisfies every applicable exact geometry, identity, provenance,
   shared-base, local-variant, transform, pivot, contact, negative-space, and
   forbidden-method obligation;
2. preserves the geometry-readable artistic-soul keeper features defined by
   the authoritative Aerathea source and plan; and
3. may complete Step 13 while remaining a `DCC source candidate`.

Step 13 does not decide final materials, final artistic approval, optimization
strategy, direct Nanite import, or game readiness.

## Governing Authority

The execution must fail closed if any required authority is missing or its
locked hash differs.

1. `AGENTS.md` Core Principles and closed-world authorization rules.
2. Governing Step 01-16 plan:
   `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/SM_DRW_SiegeBreaker_Hammer_A01_STEPS_01_16_PROOF_OF_CONCEPT_PIPELINE_PLAN.md`
   - SHA-256:
     `53046eb839b94d9548dfc2e49471b3605a2fc882228ca5e4291db7390e584a2a`.
   - Step 13 authority used:
     byte-identical geometry audit, keeper-feature review, fixed six-view and
     three-quarter comparisons, silhouette, thumbnail, turntable, wireframe,
     contact, and negative-space proof.
3. Approved visual canon:
   `VC-DRW-SiegeBreaker-Hammer-A01` in
   `docs/assets/VISUAL_CANON_REGISTRY.md`.
   - Siege Breaker source concept and the registered front, back, left, right,
     top, and bottom orthographic views own the approved visual target.
   - `siege_breaker_silhouette_reference.png` remains `reference only` and
     cannot pass, fail, or override a gate.
4. Governing shared-depth recovery blueprint:
   `../manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json`
   - SHA-256:
     `efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58`.
5. Shared-depth authority lock:
   `../manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK.json`
   - SHA-256:
     `6889b826481e5e11dd10775f2b81467b1014687b7fda9ebbff62d519bfff09bc`.
6. High-poly source-stage performance amendment:
   `STEP_11B_HIGH_POLY_NANITE_PERFORMANCE_AMENDMENT_A01.md`
   - SHA-256:
     `2e4276ea0adc32d8c6a21fb5bfbd46eacf627a9708c6187e56be1556eee76ba6`.
   - Step 13 inherits only the classification of the current sources as
     high-poly source candidates whose polygon counts are observed metrics.
     It does not authorize Nanite import or resolve the deferred high-to-low
     strategy.
7. Fresh-builder approval:
   `FRESH_TWIN_DCC_SOURCE_BUILDER_A01_APPROVAL_RECORD.md`
   - SHA-256:
     `8b59685cf27656805ecf73385ab980c1d96dec2686ac1928f6f547f4dad787ef`.
8. Fresh-builder output record:
   `FRESH_TWIN_DCC_SOURCE_BUILDER_A01_OUTPUT_RECORD.md`
   - SHA-256:
     `6cc72297048abbef35ad2893396effbff8101bc196a304e14544ceb1d7cb7533`.
9. Fresh-builder manifest:
   `../manifests/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_MANIFEST.json`
   - SHA-256:
     `6e77b264cfceb9233f2f8b4ae8a9844a53069d8bcf724bd6b0699b8416181350`.
10. Independent saved-file and cross-asset audit:
    `../manifests/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_INDEPENDENT_AUDIT.json`
    - SHA-256:
      `f2c5434a61b15dcbb616a3c10c23bef0f91f62f4966d46b6d758dbc8dc9cc285`.
    - Artifact status: `proof only; PASS`.
11. Flamestrike visual-decision record:
    `FRESH_TWIN_DCC_SOURCE_BUILDER_A01_VISUAL_DECISION_APPROVAL_RECORD.md`
    - SHA-256:
      `3ae3e8a823262870e3ea01cc4b33a470d68d3b5b7d8fe49049315d68e6c66eb7`.
    - Scope inherited:
      both displayed candidates were visually approved for advancement.
    - Scope not inherited:
      visual canon promotion, final artistic approval, Step 13 execution, or
      any later production work.
12. Foe Hammer identity:
    `docs/assets/blueprints/SM_DRW_FoeHammer_Hammer_A01/SM_DRW_FoeHammer_Hammer_A01_IDENTITY_AND_RESUME_STATE.md`
    - SHA-256:
      `63c17d6fbd5f27d6487b40ba163d6721bbfeb69a2bc46cee26453433f16e1944`.

The earlier Step 11 construction blueprint, former Step 12 candidates,
historical Step 13 contract, and superseded Step 12-to-13 handoff are
`invalid`, `quarantined`, or `reference only` for this execution. They may be
read only to prove non-use; they may not provide geometry, rules, thresholds,
or expected results.

## Immutable Source Inputs

### Siege Breaker

- Path:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_SharedDepth_DCCSource_A01/SM_DRW_SiegeBreaker_Hammer_A01_DCCSource_SharedDepth_A01.blend`
- SHA-256:
  `c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537`
- Approved local distinction: `double rune sided`
- Status entering Step 13: `DCC source candidate`

### Foe Hammer

- Path:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_FoeHammer_Hammer_A01/A12_R10_R8_SharedDepth_DCCSource_A01/SM_DRW_FoeHammer_Hammer_A01_DCCSource_SharedDepth_A01.blend`
- SHA-256:
  `67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4`
- Approved local distinction: `double metal-center-piece sided`
- Status entering Step 13: `DCC source candidate`

### Shared Locks

- Exact shared XYZ:
  `50719500/517681 × 6644212/149985 × 170/1 cm`.
- Decimal shared XYZ:
  `97.974428267601 × 44.299176584 × 170 cm`.
- Required observed cross-asset XYZ difference:
  `0.0 × 0.0 × 0.0 cm`.
- Exact builder shared-base canonical SHA-256:
  `ac0d08252ee71166842779bfb85904c4378ff1a9a4b8328d82dfac9c914e8049`.
- Independently derived saved shared-base canonical SHA-256:
  `f03b975b03141204b4a3c061306d8f48f8668e2a2bdcd214d1f72f555efe86c4`.
- Allowed cross-asset geometry difference:
  tagged local `C04` treatment only.
- Quarantined geometry read count:
  `0`.

Expected rational dimensions and observed Blender float32 dimensions must
remain separate fields. Expected values may not substitute for direct
saved-file observations.

## Authorized Execution Scope

Execution begins only after this exact contract is approved and the approval
is recorded and hash-locked.

### 1. Recovery And Environment Preflight

1. Run `Tools/System/aerathea_checkpoint.sh` before Blender or validation.
2. Verify every governing file and immutable source hash.
3. Verify both sources are readable and neither source is modified in the
   worktree.
4. Record Blender executable identity and the no-network execution boundary.
5. Create all Step 13 scripts and outputs under new Step 13-specific filenames.
6. If any preflight check fails, create a blocked record and stop before
   rendering.

### 2. Independent Saved-Geometry Audit

The auditor must read each saved `.blend` directly. It may not trust builder
claims without observation.

It must independently record and pass:

1. source SHA-256 before inspection;
2. asset ID, object identities, variant identity, and build lineage;
3. exact expected dimensions and direct observed saved-mesh bounds;
4. zero observed XYZ difference between twins;
5. origin/pivot at `(0,0,0)`, applied scale, and approved transforms;
6. one canonical shared-base equality result excluding only tagged local
   `C04` objects;
7. no cross-asset difference outside the tagged local `C04` treatment;
8. correct doubled local treatment for each asset;
9. approved local source intervals, local mirrors, common depth envelope, and
   one whole-asset `Rz180` completion;
10. complete source-owner and equation provenance for every mesh surface;
11. zero forbidden candidate-specific global-depth equation use;
12. zero bounding-box, footprint, interval-rectangle, backing-plate, facade,
    card, carrier, detached-shell, or projection-fill geometry;
13. closed/manifold volume, boundary-edge, non-manifold-edge, degenerate-face,
    duplicate-face, zero-area-face, and normal-orientation results for every
    mesh object;
14. exact declared contacts and protected negative spaces;
15. zero linked libraries, external image dependencies, or quarantined
    geometry reads;
16. direct observed vertex, polygon, triangle, and mesh-object counts; and
17. source SHA-256 after inspection, exactly equal to the pre-inspection hash.

No unapproved tolerance may convert a failed exact check into a pass. Where an
approved tolerance exists, the audit must cite its exact authority and report
both the exact residual and the pass/fail comparison.

The current high-poly triangle counts are observed evidence, not an
optimization pass/fail gate. Step 13 may not retopologize, decimate, select a
Nanite route, or reinterpret the assets as final LOD0 meshes.

### 3. Read-Only Review Rendering

Only after the saved-geometry audit passes may a new renderer load each
immutable source. The renderer may create cameras, lights, and diagnostic
materials in memory, but it must never save the source `.blend`.

Use matched production scale, orientation, framing, and cameras for both
assets. Produce:

1. fixed front, back, left, right, top, and bottom neutral-clay renders;
2. matched neutral-clay three-quarter renders;
3. binary silhouette comparisons and exact XOR evidence against the
   applicable approved orthographic owners;
4. full-size and thumbnail-read silhouettes;
5. wireframe views that make genuine volume and topology readable;
6. contact and negative-space diagnostic views;
7. a matched turntable or parallax sequence proving 360-degree authorship;
8. a direct twin comparison emphasizing the local `C04` difference while
   keeping the shared body visibly identical; and
9. source hashes after rendering, exactly equal to the locked input hashes.

Source pixels, candidate renders, silhouettes, XOR diagnostics, and review
labels must remain visually separated. A diagnostic mask, source footprint,
bounding box, or colored overlay may not be presented as approved geometry.

The final Step 13 review board must be opened automatically in a visible
desktop window.

### 4. Geometry-Readable Keeper-Feature Audit

The review must separately classify each feature as `PASS`, `FAIL`, or
`BLOCKED`, with cited evidence:

1. monumental, top-heavy Aerathean Dwarven great-hammer silhouette;
2. two irregular faceted strike masses that remain balanced without reading
   as bland mirrored boxes;
3. dense and believable structural bracing shapes;
4. dominant layered central diamond shield/crystal focal hierarchy;
5. narrow shaft contrast against the massive head;
6. readable grip and weighted faceted pommel massing;
7. authored front, back, sides, top, bottom, contacts, and negative spaces;
8. no blank backs, copied facades, cards, projection carriers, or hollow
   presentation tricks;
9. large-form geometry suitable for later material interpretation; and
10. correct twin identity:
    - Siege Breaker remains double-rune-sided;
    - Foe Hammer remains double-metal-center-piece-sided;
    - no other identity or shared-base difference exists.

Material-dependent keeper features such as final aged-bronze color, dark-steel
response, leather color, emissive intensity, wear, scratches, cracks, grain,
and final surface storytelling are explicitly deferred. Step 13 must mark
them `not evaluated at this geometry-only gate`; it may not silently pass or
invent them.

Foe Hammer has no separate approved color concept. Its Step 13 visual target is
the authoritative shared Siege Breaker base and keeper-feature language plus
the separately approved local metal-center-piece `C04` treatment. Step 13 may
not invent additional Foe Hammer distinctions.

## Required Outputs

If executed, Step 13 may create only:

- `Tools/DCC/audit_siegebreaker_foehammer_step13_immutable_geometry_a01.py`;
- `Tools/DCC/render_siegebreaker_foehammer_step13_review_a01.py`;
- `../manifests/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_TECHNICAL_AUDIT.json`;
- `../manifests/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_KEEPER_FEATURE_AUDIT.json`;
- `../review/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01/`;
- `../review/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_REVIEW.png`;
- `STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_OUTPUT_RECORD.md`; and
- `../handoffs/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_STOP_HANDOFF.md`.

All output manifests must record source hashes, authority hashes, observed
values, pass/fail details, artifact classifications, created-file inventory,
assumptions, blockers, and the post-execution source hashes.

## Disposition Rules

### Pass

Step 13 passes only if:

- every required technical check passes;
- every geometry-readable keeper feature passes;
- no authority, assumption, or visual condition is unresolved;
- both source hashes remain byte-identical; and
- the visible review board contains every required view without misleading
  evidence/interpretation presentation.

On pass:

- Step 13 status becomes `complete`;
- both assets remain `DCC source candidate`;
- the Step 13 audits are `proof only; PASS`;
- the review board is `proof only`;
- final artistic approval remains reserved to Step 16; and
- Step 14 remains locked behind a separate visible contract and approval.

### Fail Or Block

Any failed exact requirement, lost keeper feature, missing authority, hidden
assumption, changed source hash, absent review view, or misleading review
presentation stops the run.

- Missing source authority:
  `Blueprint block: source authority missing`.
- Missing rule or threshold:
  `Blueprint block: rule missing`.
- Technical or keeper-feature failure:
  preserve evidence, classify both sources no higher than their entering
  `DCC source candidate` status, and stop.
- No repair-forward, geometry edit, threshold invention, or automatic Step 14
  escalation is permitted.

## Explicitly Forbidden

This contract does not authorize:

- modifying, resaving, replacing, copying, or renaming either source `.blend`;
- changing geometry, transforms, pivot, object identities, or component tags;
- repairing a failure;
- using former quarantined geometry or historical rules as current authority;
- retopology, decimation, UVs, baking, textures, production materials, LODs,
  collision, sockets, rigging, or animation;
- deciding direct Nanite import versus an optimized derivative;
- FBX, GLB, or other interchange export;
- Unreal import, placement, capture, validation, or promotion;
- visual-canon promotion;
- `DCC game-ready candidate`, `Fully game-ready`, approved-library, or final
  artistic classification; or
- beginning Step 14.

## Recovery, Commit, And Stop Boundary

After a pass or block:

1. run a post-job manual checkpoint;
2. preserve every Step 13 evidence artifact and classification;
3. commit and push only the scoped tracked Step 13 records required by the
   Aerathea recovery rule, without staging unrelated worktree changes;
4. open the final review board visibly; and
5. stop.

The execution report must state:

- files created;
- source hashes before and after;
- technical and keeper-feature dispositions;
- assumptions or interpretations;
- blockers or uncertainty;
- artifact statuses; and
- the exact next approval need.

## Current Approval Question

Approve, reject, or mark blocked this exact Step 13 contract.

Approval authorizes only the bounded read-only audits, in-memory review
rendering, evidence packaging, recovery actions, and scoped commit/push listed
above. It does not authorize any geometry or downstream production change.
