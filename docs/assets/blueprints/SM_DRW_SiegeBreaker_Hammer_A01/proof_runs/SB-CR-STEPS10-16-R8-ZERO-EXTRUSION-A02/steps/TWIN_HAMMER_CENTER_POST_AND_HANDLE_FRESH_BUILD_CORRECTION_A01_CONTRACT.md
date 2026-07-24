# Twin Hammer Center-Post And Handle Fresh-Build Correction A01 Contract

- Date: `2026-07-24`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Contract ID:
  `TWIN-HAMMER-CENTER-POST-HANDLE-FRESH-BUILD-CORRECTION-A01`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01`
  - `SM_DRW_FoeHammer_Hammer_A01`
- Artifact status: `candidate`
- Contract status:
  `draft only; waiting for exact Flamestrike execution approval`
- Drafting authority:
  Flamestrike approved the exact documentation-only drafting step on
  `2026-07-24`
- Production authority from the drafting approval: `false`
- Code / Blender / geometry / render / export / Unreal authority now:
  `false / false / false / false / false / false`
- Valid DCC source candidates before execution: `0`
- Maximum result after a later approved and fully passing execution:
  `two DCC source candidates pending Flamestrike visual decision`

## Contract Effect

This document does not authorize or execute itself.

The approval that authorized this document covered only:

1. drafting this one candidate contract;
2. validating its cited authority paths and hashes;
3. presenting it for review; and
4. stopping.

If Flamestrike later approves this exact contract by the SHA-256 reported with
its review, that later approval authorizes only the code, fresh DCC builds,
audits, proof renders, visible review boards, state records, checkpoints, and
scoped repository actions declared below.

That later approval would not authorize Step 13 completion, Step 14,
retopology, production UVs, baking, textures, production materials, LODs,
collision, FBX/GLB export, Unreal work, visual-canon promotion,
`DCC game-ready candidate`, or `Fully game-ready` status.

Any byte change to this contract after approval invalidates the approval until
Flamestrike reviews and approves the new hash.

## Core Decision

The decision requested by this contract is:

> Approve, reject, revise, or keep blocked one fresh deterministic rebuild of
> the Siege Breaker and Foe Hammer twins from the last Core-valid source and
> component authority, correcting only the center-post separation and
> rotational handle-shape failures while retaining every later approved twin,
> face-placement, and mirror constraint.

The execution result must answer:

1. Does the head preserve the source-owned separation around the top center
   post instead of becoming a front-profile slab?
2. Are C06-C11 genuine source-radius rotational surfaces instead of
   rectangular sections?
3. Are both hammers canonically identical outside the approved local C04
   treatment?
4. Do both saved sources pass direct topology, ownership, protected-space,
   rotational-section, symmetry, bounds, and source-integrity audits?
5. Do the two visible boards give Flamestrike enough evidence to approve,
   reject, revise, or mark the DCC sources blocked?

## Controlling Truths

1. Both latest A13 R1 Blender sources are
   `invalid / quarantined in place`.
2. Their manifold, welded-seam, bounds, and twin-equality results are
   `proof only`; those checks did not prove component shape.
3. The first drift action was using the front Step 06 mask as a paired
   front/back construction domain and closing its perimeter.
4. A correct front silhouette, common depth, closed manifold, welded symmetry,
   and equal dimensions do not prove correct three-dimensional component
   surfaces.
5. The source images, exact measurement and ownership evidence through Step
   09A, approved zero-extrusion component rules, shared twin identity and
   bounds, exact face elevation, and `X=0` mirror-and-weld correction remain
   authoritative within their stated scopes.
6. The common XYZ envelope is a validation bound. It creates no surface,
   volume, backing wall, or fill by itself.
7. Missing surface ownership, missing edge correspondence, or missing closure
   authority is a block. It is not permission to extrude, interpolate a new
   silhouette, smooth, average, or repair forward.

## Authority Order And Verified Hashes

All paths are repository-relative. A future execution must verify every hash
before creating or modifying code.

### Core And Current Recovery Authority

1. `AGENTS.md`
   - SHA-256:
     `5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55`
   - Status: `authoritative`
2. `../manifests/TWIN_HAMMER_CENTER_POST_AND_HANDLE_SHAPE_DRIFT_RECOVERY_A01.md`
   - SHA-256:
     `3c24c18d940a428918bad714ca3fb04c3a2092a4656f77c6b5736658b116546a`
   - Status: `authoritative recovery record`
3. `../handoffs/TWIN_HAMMER_CENTER_POST_AND_HANDLE_RESET_HANDOFF_A01.md`
   - SHA-256:
     `041d6ea4151849970426bbfa9b3d8dd6dc3804631d946ee815af66a112628037`
   - Status: `authoritative recovery and resume instruction`
4. `../manifests/STEP_STATE.json`
   - SHA-256 at draft:
     `d6ef38eb769b1b76f7093b8d2ce4f1868adc60dc7becab67cc177cd153d1a981`
   - Required execution state:
     `core_recovery_stopped_no_valid_dcc_source_candidate_new_contract_required`

### Immutable Source Images

1. `SourceAssets/Concepts/SiegeBreaker/siege_breaker_front_view.png`
   - SHA-256:
     `d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95`
2. `SourceAssets/Concepts/SiegeBreaker/siege_breaker_back_view.png`
   - SHA-256:
     `15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799`
3. `SourceAssets/Concepts/SiegeBreaker/siege_breaker_left_view.png`
   - SHA-256:
     `1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b`
4. `SourceAssets/Concepts/SiegeBreaker/siege_breaker_right_view.png`
   - SHA-256:
     `04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330`
5. `SourceAssets/Concepts/SiegeBreaker/siege_breaker_top_view.png`
   - SHA-256:
     `06d9cc7f78a4fe459a1f620e4787b53bf63399f7215bb9106a4e264749147d1c`
6. `SourceAssets/Concepts/SiegeBreaker/siege_breaker_bottom_view.png`
   - SHA-256:
     `634dcf706a95a7f967b0c73d3c28fff318e3f91b2866e790369a57fa3b6e8d91`

The images remain evidence within their approved owner scopes. Printed labels,
background, arrows, paper, shadows, and non-owner regions do not become
geometry authority.

### Measurement, Ownership, And Component Authority

1. `../../SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01/manifests/STEP_09A_AUTHORITY_LOCK.json`
   - SHA-256:
     `a7e07ad68e9b2737c7c70e71e9df714766a285695693e741197900e17c3a06a5`
   - Effective status:
     component scanlines, protected negative spaces, contact/boundary edge
     sets, and ordered correspondence groups are `authoritative`
2. `../../SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01/manifests/STEP_09A_BOUNDARY_AND_CORRESPONDENCE_INDEX.json`
   - SHA-256:
     `e190ed266753c797d4f9ec812154ff3b29f5d5d780e53e235e780c43492d0bd8`
3. `../../SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01/evidence/STEP_09A_COMPONENT_SCANLINES.json.gz`
   - SHA-256:
     `396adfbaaefc8a8ea35104e5e96dfde322510fb4ce88530fbb32f7f3073b3562`
4. `../../SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json`
   - SHA-256:
     `5a0a3eea8f877d55216f9efabe15b0ee1cf938e4c15a825a0e218f72ba76839a`
5. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/manifests/A12_R10_STEP01_SOURCE_MEASUREMENT_CENTERLINE_A01.json`
   - SHA-256:
     `4d47a3e6bb375cc9f6371341f7b359dbfa107a1a2856fb239ccaa0ca01dda327`
   - Status:
     `reference evidence where later approved component equations explicitly
     resolve its recorded blocks`
6. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/manifests/A11_TRUE_AXIAL_TOP_BOTTOM_PIXEL_MEASUREMENT.json`
   - SHA-256:
     `46877ab4b0142d8141deb4feab234f461a31e61e118d3ce7b41e0b3679786096`
   - Status:
     `authoritative outer-footprint and common-depth measurement`

### Approved Process And Equation Authority

1. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/SM_DRW_SiegeBreaker_Hammer_A01_STEPS_01_16_PROOF_OF_CONCEPT_PIPELINE_PLAN.md`
   - SHA-256:
     `53046eb839b94d9548dfc2e49471b3605a2fc882228ca5e4291db7390e584a2a`
2. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/SM_DRW_SiegeBreaker_Hammer_A01_A12_R7_COMPONENT_GEOMETRY_RECOVERY_PLAN.md`
   - SHA-256:
     `b0b077c8d39a07e5d1ab12309e77560afa1c407fe3bb3e6272a0c4e6d568b22e`
3. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_DRAFT.md`
   - Approved SHA-256:
     `a40d0b67d802687ac3c9ec9ad8e00a915cc1dc730ce31f3fab00b18a1837a21c`
4. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_A01_APPROVAL_RECORD.md`
   - SHA-256:
     `8296f530d48f43b99c6de26271e3be4da0a9fd512e389c90f55b9d5208185b29`
5. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/A12_R10_R8_PIXEL_EXACT_STEPS01_16_A01_CONTRACT.md`
   - SHA-256:
     `77b0339126388be01f59532cd6b79228450b61e739ebc10c2f849833fd337bd4`
6. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/A12_R10_R8_ZERO_EXTRUSION_AUTHORITY_RECOVERY_A01_APPROVAL_RECORD.md`
   - SHA-256:
     `76c9b6a1d798780def0662c3a072f76144531f82b3228d7e2ce4adb4ee0d5ee0`
7. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/handoffs/A12_R10_R8_ZERO_EXTRUSION_RESET_HANDOFF.md`
   - SHA-256:
     `405d93b079c0fe52bdc443cadd085010fb64acf4cf9d078bf6e78d7e915e3ba0`

The zero-extrusion component, source-owner, combined-boundary, hidden-closure,
cylinder-wrap, and fail-closed rules remain in force.

### Approved Twin, Bounds, Face, And Completion Authority

1. `../manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json`
   - SHA-256:
     `efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58`
   - Effective status through its authority lock:
     `authoritative shared-depth recovery blueprint`
2. `../manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK.json`
   - SHA-256:
     `6889b826481e5e11dd10775f2b81467b1014687b7fda9ebbff62d519bfff09bc`
3. `../manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01.json`
   - SHA-256:
     `4e960362ebcf27ffd3c6ed811584679d5f8ca75befcaad8286370224fe9eb3e4`
   - Status:
     `authoritative correction amendment within Flamestrike-approved fix`
4. `../manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01_VALIDATION.json`
   - SHA-256:
     `8f6cfa57c8044c93e671a0d4270ef801df311f8cfa7428eaa17f19003837bb07`
   - Status: `proof only; PASS 51/51`
5. `TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_APPROVAL_RECORD.md`
   - SHA-256:
     `bb1b090befd1db4a76a37434855e9577e2e41e2cc9cda64982dd6df1e998ba85`
   - Status: `authoritative approval record`
6. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/A09_FULL_PIXEL_HALF_MIRROR_VISUAL_MATCH_CONTRACT.md`
   - SHA-256:
     `294bb6c10178b9314bb011a59877f30df187728ef1e21e763a7f391aa5bc9395`
7. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/review/A09_FULL_PIXEL_HALF_MIRROR_A01_FINAL_REVIEW.md`
   - SHA-256:
     `9edfae8a31b17ed07e31e8ac0582681f06d0347463b1dcf87712fec490d3628a`
   - Approved role:
     `visual appearance, source-pixel proportions, and X=0 mirror method`

## Explicit Supersession Rule

The later approved centered-face correction and current Core Recovery state
control whole-asset completion for this contract:

`(X,Y,Z)->(-X,Y,Z)` across `X=0`, exactly once.

Therefore:

- the R8 whole-asset `Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)` clause is
  superseded for this correction;
- whole-asset Rz180 count must be `0`;
- X-mirror count must be `1`;
- the center seam must be joined and welded only at coordinate-equal points;
- the approved zero-extrusion component and cylinder equations remain in
  force; and
- no other clause is silently superseded.

## Reference-Only Process History

The following artifacts were read because the zero-extrusion reset handoff
requires them, but they are not executable construction inputs:

1. `Tools/DCC/build_siegebreaker_a12_r10_a09_process_complete_rz180.py`
   - SHA-256:
     `088ec22595437611e4f0e136db13b49d32ce3caaf8224c60f145f1c15153f235`
2. `Tools/DCC/audit_siegebreaker_a12_r10_a09_process_complete_rz180.py`
   - SHA-256:
     `6db37706e87021cf1ea978091c1e7b9f30c21163a5d5bd64bb6b32919ee352e0`
3. `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/A12_R10_A09_PROCESS_COMPLETE_RZ180_A02_OUTPUT_RECORD.md`
   - SHA-256:
     `639db9d0c565aae7b974dab6fce9fb888f1b8412c77bbb2f6046413a7dbdff52`

They may establish process history and known audit omissions only. The future
builder and auditor may not import, execute, copy, or use coordinates,
geometry, source objects, fill sets, faces, UVs, materials, or output files
from them.

## Evidence And Interpretation Firewall

### Evidence

Evidence permitted by this contract includes:

- immutable source pixels and exact source hashes;
- Step 09 and Step 09A scanline memberships;
- exact component IDs, owner runs, ordered boundary edge sets, contacts, and
  protected negative spaces;
- approved exact component equations and physical locks;
- the shared XYZ bounds and twin identity rules;
- the exact C04 local intervals and face-placement translation;
- approved transform and mirror equations; and
- direct independently observed saved-file audit results.

### Interpretation

This contract does not authorize:

- a smoothed, averaged, visually fitted, or hand-edited contour;
- a bounding box, footprint, interval rectangle, mask, or protected-space
  envelope used as fill geometry;
- a new hidden exterior surface;
- arbitrary point pairing between order-only correspondence groups;
- a primitive substitute;
- a fixed segment count that skips or repeats a source-owned column; or
- any surface whose owner, equation, measurement, and closure/contact rule
  cannot all be cited.

Step 09A correspondence groups preserve order only. They do not, by
themselves, authorize point pairing or surface creation.

If a required ruled face lacks an existing explicit corresponding-edge rule,
future execution must stop before code or Blender with:

`Blueprint block: rule missing`

If a required visible or hidden surface lacks a source owner, future execution
must stop before code or Blender with:

`Blueprint block: source authority missing`

## Required Preflight Before Any Future Code Change

A later approved execution must perform a read-only preflight and stop unless
all of the following pass:

1. the approved contract SHA-256 matches the reviewed hash;
2. every authority path above exists and matches;
3. the current state still reports zero valid DCC source candidates and no
   active competing geometry contract;
4. both proposed source output roots and the proposed review root remain
   absent;
5. the six source images decode losslessly;
6. Step 09A authority still covers C01, C02, C03, C04, and C06 ownership,
   contacts, protected spaces, boundary sets, and correspondence ordering;
7. the approved component equations still cover every constructed surface,
   rotational station, contact, cap, and hidden closure;
8. the exact C04 local intervals, shared dimensions, face translation, and
   X-mirror rule are unchanged;
9. all required C01/C02/C03 front/top/bottom boundary records are readable;
10. all required C06-C11 radius-by-Z and source-column records are readable;
11. C12 retains an unchanged approved owner/equation path or execution blocks
    before geometry;
12. no required surface depends on a quarantined mesh, prior builder output,
    inferred fill, or unapproved point correspondence; and
13. no permitted output path would overwrite an existing file.

The preflight must write its observed results only after this contract receives
execution approval. It may not convert a missing rule into a builder default.

## Exact Allowed Future Implementation Files

After separate execution approval, exactly these new tools may be created:

- `Tools/DCC/build_twin_hammer_center_post_handle_fresh_build_correction_a01.py`
- `Tools/DCC/audit_twin_hammer_center_post_handle_fresh_build_correction_a01.py`
- `Tools/DCC/render_twin_hammer_center_post_handle_fresh_build_correction_a01.py`

The independent auditor:

- may not import the builder;
- may not trust builder-authored pass booleans;
- may not trust Blender custom properties as proof;
- must recompute expected values from the hash-locked authority files; and
- must inspect both saved Blender files directly.

The renderer may run only after both independent saved-file audits pass. It
may use temporary neutral-clay, topology, and section-proof materials in
memory, but it may not resave or alter either source.

No existing tool may be modified.

## Exact Fresh Output Roots

The future build roots are:

- Siege Breaker:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A13_R2_CenterPostHandleFreshBuild_DCCSource_A01/`
- Foe Hammer:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_FoeHammer_Hammer_A01/A13_R2_CenterPostHandleFreshBuild_DCCSource_A01/`
- Review:
  `../review/TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01/`

All three roots were absent when this contract was drafted. If any root exists
when future execution begins, stop with:

`Blueprint block: drift risk — approved fresh output root is not fresh`

## Fresh-Only Input Rule

The future builder may read only the hash-locked non-geometry authority listed
in this contract.

It must not read geometry, vertices, faces, edges, normals, UVs, materials,
coordinates, transforms, canonical geometry, masks created by a failed
builder, or Blender objects from:

- either A13 R1 centered-face source;
- either earlier shared-depth source;
- either former Step 12 candidate;
- any A09/R10 component proof `.blend`;
- any other rejected, invalid, or quarantined hammer mesh; or
- any prior builder output root.

Old Blender files may be hash-checked as quarantine evidence without opening
their geometry.

## Exact Construction Sequence

Future execution must use this sequence once:

1. Verify authority and write the authority-preflight record.
2. Decode the authoritative source and measurement records without resampling.
3. Construct one canonical shared positive-`X` half from source-owned
   component surfaces only.
4. Construct and integrate the selected local C04 treatment on the positive-X
   strike end.
5. Run the complete pre-save authority, method, protected-space, rotational,
   topology, contact, and bounds audit.
6. Mirror the sealed positive-X half once across `X=0`.
7. Weld only coordinate-equal center-seam vertices.
8. Repeat every gate against the complete unsaved geometry.
9. Save the Siege Breaker source only if every gate passes.
10. Instantiate the same canonical shared base for Foe Hammer and replace only
    the tagged local C04 treatment.
11. Repeat every pre-save gate and save the Foe Hammer source only if every
    gate passes.
12. Close Blender.
13. Independently reopen and audit both saved files.
14. Render only after both independent audits pass.
15. Build and open one review board per hammer.
16. Record results, checkpoint, perform only the approved scoped repository
    actions, and stop for Flamestrike's visual decision.

No failed step may be repaired or retried with changed rules inside the same
execution.

## C01/C02/C03 Head-Surface Rule

The center core and two stones must be reconstructed as separate physical
components from their approved front, top, and bottom owner boundaries.

Required rules:

1. Front owner surfaces use the exact front scanline memberships and component
   owner runs.
2. Top and bottom owner surfaces use their exact C02 and C03 inner owner edge
   sets.
3. A side or hidden closure may be created only where the approved
   zero-extrusion closure equation cites both boundary owners and an explicit
   correspondence rule.
4. The components share one declared contact boundary where authority says
   they contact; coincident independent walls are forbidden.
5. No 2D owner mask may be copied to a second depth plane.
6. No perimeter of a front mask may be closed as a slab.
7. The common depth envelope may clip or validate a source-owned surface but
   may not create a surface.
8. The central-post separation and every other protected source-connected
   negative space remain unoccupied.

### Center-Post Protected-Space Gate

`TOP_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER` contains the exact protected
top-view half-open runs. Those pixels are an exclusion set, not a candidate
fill or a smoothed gap.

`BOTTOM_STONE_SEPARATION_WITHOUT_CENTRAL_OWNER` currently contains no
bottom-specific protected-run samples. That absence does not authorize a
bottom fill, new bottom contour, or inferred bottom owner.

The independently audited complete geometry must satisfy both:

1. every exact top protected-run pixel-center ray has zero triangle
   intersections inside the registered C01/C02/C03 head interval of the
   source-owned center-post separation; and
2. the same three-dimensional separation has zero triangle intersections
   inside that same registered head interval when tested from the matched
   bottom projection.

If satisfying the bottom projection requires a new bottom-specific surface or
owner not already authorized, execution stops with:

`Blueprint block: source authority missing`

The gap may not be produced by cutting, deleting, or booleaning the finished
slab. It must exist because no unauthorized fill geometry was created.

## C06-C11 Rotational-Surface Rule

C06, C07, C08, C09, C10, and C11 must be built as exact source-driven radial
surfaces about world `X=0,Y=0`.

At every approved station:

`P(z,theta)=(r(z)cos(theta),r(z)sin(theta),z)`.

Required rules:

1. `r(z)` comes only from the approved front positive-half source edge and
   later approved physical locks.
2. C07 remains a true `5 cm` diameter, `2.5 cm` radius cylinder.
3. The cylinder mapping remains:
   `theta(U)=-pi/2+pi*U`.
4. The flat-diameter-to-half-circumference factor remains exactly:
   `pi/2`.
5. Every retained source-owned column owns its exact proportional U interval.
6. No fixed segment count may skip, repeat, average, or normalize source
   columns.
7. No row may use `Y=+r` and `Y=-r` planes joined to `X=+r` and `X=-r`
   planes.
8. No rectangle, square, rounded square, ellipse, cube, prism, extrusion,
   bevel repair, or primitive substitute is permitted.
9. Component transitions use only the approved half-open Z stations and
   declared common contacts.
10. C12 retains its separately approved rotational owner/equation rule and may
    not be reshaped to repair the head.

### Rotational Audit

The builder pre-save audit and independent saved-file audit must:

- recompute every expected `P(z,theta)` directly from authority;
- test every generated rotational vertex, not a sample;
- require maximum coordinate delta no greater than `1e-6 cm` after Blender
  float serialization;
- require exact equality in the canonical pre-serialization equation record;
- verify every declared station has the expected ordered source-column
  ownership;
- verify all radii at a station match its authoritative `r(z)`;
- verify all C07 radii equal `2.5 cm` within `1e-6 cm`;
- verify no four-corner or planar-section substitute exists; and
- produce audited sections for the haft, grip, collar, and pommel.

## Local C04 Treatment Rule

The positive-X strike-end surface must be an integrated part of the shared
head, not a detached, floating, hanging, backed, or intersecting panel.

The exact local variants remain:

- Siege Breaker:
  `rune_side`, source interval `[557,668)`, completed as double rune sided;
- Foe Hammer:
  `metal_center_piece_side`, source interval `[418,557)`, completed as double
  metal-center-piece sided.

Required rules:

1. Preserve the exact right-view scale `85/548 cm` per pixel.
2. Preserve each local source interval and local extent without stretching,
   normalization, averaging, resampling, or promotion to global depth.
3. Apply exactly one face-local `Y=0` mirror where required by the approved
   C04 rule.
4. Apply the exact positive-Z translation:
   `+1608625/145631 cm`.
5. Do not scale the local treatment.
6. Let the source-owned integrated strike-face perimeter control containment.
7. Do not let the local treatment enlarge, clip, or define the shared body.
8. Do not create a separate backing wall or copied depth face.
9. Require one welded physical boundary between treatment and adjoining head.
10. Preserve only the tagged local C04 geometry difference between twins.

## Whole-Asset Mirror And Twin Rule

The builder must:

1. construct one correct, sealed, source-owned positive-X half;
2. apply exactly one:
   `(X,Y,Z)->(-X,Y,Z)`;
3. use no whole-asset Rz180;
4. remove center-plane closure faces before joining;
5. merge only coordinate-equal `X=0` vertices;
6. weld the center seam;
7. recalculate and independently verify outward winding;
8. construct one canonical shared base;
9. instantiate that exact shared base for both assets; and
10. change only the tagged local C04 treatment.

The exact shared output XYZ is:

`50719500/517681 × 6644212/149985 × 170/1 cm`.

Decimal reference:

`97.974428267601 × 44.299176584 × 170 cm`.

Required cross-asset XYZ difference:

`0 × 0 × 0 cm`.

The canonical shared-base hash must match exactly after excluding only:

- `C04_RUNE_LOCAL_TREATMENT`; or
- `C04_METAL_CENTER_PIECE_LOCAL_TREATMENT`.

## Mandatory Pre-Save And Independent Saved-File Gates

Each asset must independently prove:

- authority hashes: `PASS`;
- source-owner/equation citation for every surface: `PASS`;
- prohibited method scan: `PASS`;
- top center-post protected-space projection: `PASS`;
- bottom center-post protected-space projection: `PASS`;
- all other protected negative spaces: `PASS`;
- rotational section equations for C06-C11: `PASS`;
- C07 diameter and `pi/2` wrap: `PASS`;
- C04 local interval, scale, translation, containment, and mirror: `PASS`;
- shared contacts: `PASS`;
- open boundary edges: `0`;
- edges used by more than two faces: `0`;
- face-winding mismatches: `0`;
- loose edges: `0`;
- zero-area faces: `0`;
- duplicate coordinate faces: `0`;
- unwelded center-seam vertices: `0`;
- whole-asset Rz180 count: `0`;
- X-mirror count: `1`;
- unapplied object transforms: `0`;
- modifiers: `0`;
- pivot: exact world `(0,0,0)`;
- observed bounds: exact approved XYZ within `1e-6 cm` serialization
  tolerance;
- cross-asset bounds difference: exact `0 × 0 × 0 cm`;
- canonical shared-base equality: `PASS`;
- geometry difference outside tagged local C04: `0`;
- source hashes after save: unchanged; and
- geometry read from a forbidden source: `0`.

Expected values and observed values must be stored separately. A builder-authored
target value cannot satisfy an observed gate.

Any missing, skipped, unreadable, or unevaluated gate is a failure.

## Review Gate

Rendering is forbidden until both saved files pass the independent auditor.

The renderer must create exactly one clearly framed review board per hammer.
Each board must show:

1. a matched normal three-quarter view;
2. a direct top view centered on the head and center-post separation;
3. a direct handle view that reveals its round profile;
4. an audited handle-section panel showing haft, grip, collar, and pommel
   sections with expected/observed radius results; and
5. a compact technical footer identifying the source hash, audit result,
   bounds, mirror rule, and artifact status.

The two boards must use matched camera yaw, pitch, framing, scale, lighting,
section planes, labels, and panel layout.

The boards must not:

- hide the pommel, head top, or center gap;
- use perspective or framing differences to disguise shape;
- use texture, material, shadow, or glow to conceal geometry;
- present expected values as observed evidence; or
- imply Step 13, game-ready, or visual-canon approval.

Both boards must be opened automatically in visible desktop windows. The build
must then stop for Flamestrike's:

`approve / revise / reject / blocked`

No production stage follows automatically.

## Exact Future Output Records

A later approved execution may create only:

- the three new implementation files named in this contract;
- `../manifests/TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01_AUTHORITY_PREFLIGHT.json`;
- `../manifests/TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01_MANIFEST.json`;
- `../manifests/TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01_INDEPENDENT_AUDIT.json`;
- `../manifests/TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01_REVIEW_RENDER_MANIFEST.json`;
- `../manifests/TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01_EVENT_TRACE.jsonl`;
- `TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01_APPROVAL_RECORD.md`;
- `TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01_OUTPUT_RECORD.md`;
- `../handoffs/TWIN_HAMMER_CENTER_POST_HANDLE_FRESH_BUILD_CORRECTION_A01_REVIEW_HANDOFF.md`;
- files inventoried before creation beneath the two exact fresh source roots;
- files inventoried before creation beneath the exact fresh review root;
- required updates to the two asset resume/status records, `STEP_STATE.json`,
  approval log, artifact index, recovery journal, or drift ledger;
- mandatory local checkpoints; and
- the exact dependency-complete staged commit and push authorized by the later
  execution approval.

No unrelated dirty worktree file may be modified, deleted, staged, committed,
or pushed.

## Explicitly Forbidden

- repair-forward of either A13 R1 mesh;
- cutting gaps into a completed slab;
- beveling or rounding a square handle into compliance;
- transferring a component from an older candidate;
- reading geometry from any `.blend` or canonical geometry file;
- importing or copying any old builder or auditor;
- front-mask paired planes or perimeter closure;
- extrusion, Solidify, `bmesh.ops.extrude_*`, slab, cube, prism, card, facade,
  backing block, projection carrier, or generalized cross-section;
- a common envelope, bounding box, footprint, mask, or interval used as fill;
- point pairing created from an order-only correspondence group;
- smoothing, averaging, resampling, nearby-row search, visual fitting, or
  unapproved tolerance;
- per-component or per-variant scale;
- filling any protected gap;
- changing source pixels or approved measurements;
- whole-asset Rz180;
- geometry difference outside tagged local C04;
- manual Blender mesh edits;
- production UV, bake, texture, material, LOD, collision, FBX/GLB, export, or
  Unreal work;
- Step 13 or Step 14 advancement;
- image generation, generated views, image-to-3D, TRELLIS, TripoSR, diffusion,
  cloud generation, network-dependent production, or package installation;
- retrying with changed rules after a failure; and
- self-approval or automatic visual promotion.

## Pass, Block, Failure, And Drift Disposition

### Pass

An asset may be classified `DCC source candidate pending Flamestrike visual
decision` only if its pre-save and independent saved-file gates all pass.

Both assets must pass before the paired review gate opens. One passing asset
does not conceal, repair, or promote the other.

### Block

If source ownership, boundary correspondence, hidden closure, component
station, environment, output-root, or approval authority is missing or
conflicting:

1. stop before the dependent action;
2. preserve the last verified state;
3. report the exact `Blueprint block`;
4. create no substitute rule; and
5. wait for Flamestrike.

### Technical Failure

If a constructed output fails a mandatory gate:

1. stop;
2. preserve and classify only the evidence actually produced;
3. mark the output `invalid` or `quarantined`;
4. do not render it as a corrected candidate;
5. do not retry with changed rules; and
6. record the exact failure before stopping.

### Drift

If execution departs from the approved contract:

1. stop production immediately;
2. identify the last Core-valid state and first drift action;
3. classify and quarantine every affected output;
4. record the event in `docs/projects/assetforge/DRIFT_LEDGER.md` and both
   affected asset status records; and
5. do not repair forward.

## Checkpoint, Repository, And Stop Rule

A later approved execution must:

1. run a manual checkpoint before code or Blender work;
2. run a manual checkpoint after pass, block, failure, or drift;
3. stage only the exact dependency-complete approved scope;
4. commit and push only valid scoped tracked work to `assetforge/main`;
5. preserve local-only and quarantined artifacts under their declared paths;
   and
6. stop after both boards are visibly open and the review handoff is complete.

This draft does not authorize any checkpoint, commit, or push.

## Exact Execution Approval Gate

Approval must answer this exact question:

> Do you approve the exact SHA-256 of
> `TWIN_HAMMER_CENTER_POST_AND_HANDLE_FRESH_BUILD_CORRECTION_A01_CONTRACT.md`
> reported with its review, and authorize only its fresh twin-hammer builder,
> independent auditor, Blender source builds, proof renderer, visible review
> boards, required state/recovery records, checkpoints, scoped commit, and
> push—then stop before Step 13, UVs, textures, LODs, collision, export, or
> Unreal?

Until Flamestrike answers that question with `approved`, `yes`, or `proceed`,
production remains stopped and this contract remains `candidate`.
