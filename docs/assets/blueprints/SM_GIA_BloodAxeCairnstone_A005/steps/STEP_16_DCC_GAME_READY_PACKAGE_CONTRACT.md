# A005 Step 16 DCC Game-Ready Package Contract

Status: approved for complete Step 16 execution by Flamestrike's direct 2026-07-20 authority

Artifact classification: `authoritative execution boundary`

Contract ID: `A005-CR-STEP16-DCC-GAME-READY-PACKAGE-A01`

Date: 2026-07-20

## Flamestrike Authority

Flamestrike stated:

`resume You have complete Approval and Authorization to complete step 16 From Start to finish regardless of what you need to do`

After the required resume audit, Flamestrike answered `approved` to the focused
question approving the exact Step 15 candidate with SHA-256
`7befa56a10003c2d424de3db40e2bc402075b79644b0944413e97c92db6cab89`
for Step 16 DCC game-ready production.

Under Core and the active Blueprint, these statements authorize the complete
bounded Step 16 lifecycle: contract and immutable input lock; copied Blender
game-ready source; `LightmapUV`; LOD0-LOD3; four custom convex collision
proxies; valid A005 FBX exports; imported-FBX technical validation; final DCC
proof renders after technical pass; review board and tracked handoff; recovery
if a gate fails; checkpoints; exact scoped Git closeout; remote verification;
and the mandatory restart.

This authority does not override the Blueprint, authorize Unreal import, or
authorize Step 17 review/approval.

## Controlling Decision

Convert the exact approved Step 15 candidate into one technically validated
`DCC game-ready candidate` without redesigning its source-owned appearance,
LOD0 geometry, UV0, textures, or material language.

The decision output must be one of:

- `pass_step16_dcc_game_ready_candidate_complete`;
- `blocked_step16_technical_gate_failure`; or
- `invalid_step16_scope_or_authority_violation`.

## Locked Production Boundary

- Asset: `SM_GIA_BloodAxeCairnstone_A005` only.
- Immutable Step 15 candidate SHA-256:
  `7befa56a10003c2d424de3db40e2bc402075b79644b0944413e97c92db6cab89`.
- The immutable input is copied to
  `SM_GIA_BloodAxeCairnstone_A005_DCCGameReady_A01.blend`.
- LOD0 must reproduce the candidate's four disconnected watertight shells,
  `400` vertices, `464` faces, `784` evaluated triangles, exact transforms,
  exact `140 x 110 x 220 cm` assembled bounds, `UVMap`, and one shared
  `M_GIA_BloodAxeCairnstone_A005` material.
- Existing Base Color, DirectX Normal, ORM, masks, source-owned mip-0 RGB,
  and material behavior remain byte-identical inputs.
- One additional unique, non-overlapping UV layer named `LightmapUV` is
  required at the approved planned lightmap resolution of `128`, with at
  least four texels of island padding.
- LOD1-LOD3 are optimization interpretations. They may reduce only later-LOD
  topology, must remain watertight, retain all four component reads, preserve
  the exact ground/pivot/height and approved outer bounds, and remain below
  the Step 11 target triangle budgets.
- Collision is non-rendering interpretation and must use exactly the four
  approved `UCX_SM_GIA_BloodAxeCairnstone_A005_00` through `_03` convex hulls.

## Required Candidate Outputs

1. One Blender source containing LOD0-LOD3, `LightmapUV`, the shared material,
   and four named UCX collision hulls.
2. Primary LOD0/collision FBX at the Step 11 documented path
   `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005.fbx`.
3. Separate deterministic LOD1, LOD2, and LOD3 FBX files in the same package
   for later controlled Unreal assignment.
4. The unchanged 2K Base Color, DirectX Normal, and ORM texture package.
5. A Step 16 export manifest with hashes, object names, triangle counts,
   bounds, UV data, material data, collision data, and evidence/interpretation
   classifications.
6. An independent technical audit including a clean re-import of every FBX.
7. Final DCC LOD proofs, imported-FBX triangle/geometry proof, and a Step 16
   DCC game-ready review board after the technical audit passes.

## LOD And Collision Rules

- LOD0 is an exact joined export representation of the four approved source
  shells; joining may change object packaging but not mesh values or material
  data.
- Optimization order follows Step 11: secondary apron/course facets first,
  then minor planar subdivisions, while C001, the N3 envelope, the four-layer
  read, the `220/140/110 cm` envelope, and the stepped base silhouette remain.
- Step 11 triangle targets are upper targets, not permission to subdivide the
  approved `784`-triangle LOD0. LOD counts must decrease monotonically from
  the actual approved LOD0 and stay below `4000`, `1800`, and `700` for
  LOD1-LOD3 respectively.
- Every LOD remains one render mesh containing four disconnected watertight
  shells, one material slot, `UVMap`, and `LightmapUV`.
- Collision hulls must be convex, closed, positive-volume, non-rendering,
  A005-only, and mapped one-to-one to C001-C004. Complex-as-simple is false.

## Required Audit Sequence

1. Schema-only builder and auditor preflight with no `bpy` import or writes.
2. Verify every locked input and the focused Step 15 approval identity.
3. Build once from the immutable Step 15 candidate copy.
4. Audit LOD0 exact geometry/UV0/material/texture identity before accepting
   any downstream output.
5. Audit UV1 uniqueness, bounds, overlap, and four-texel padding.
6. Audit monotonic LOD triangles, topology, component count, bounds, pivot,
   material slots, UV layers, and silhouette-preservation invariants.
7. Audit all four collision hull names, convexity, topology, volume, and
   component containment.
8. Import every exported FBX into a clean in-memory Blender scene and verify
   names, triangle counts, bounds, materials, UV layers, collision, and scale.
9. Stop before proof rendering if any gate fails.
10. After technical pass, render fixed-camera LOD and imported-FBX proofs,
    package the review board, and open it visibly with the review record.
11. Record `DCC game-ready candidate`; do not perform the separate Step 17
    approval or any Unreal work.

## Fail-Closed Conditions

Step 16 stops if any locked hash changes; LOD0 geometry, UV0, maps, material,
scale, pivot, or visual identity differs; `LightmapUV` overlaps or violates
padding; a LOD is not lower than its predecessor or breaks the four-layer
read; a collision hull is missing, non-convex, open, or non-positive; FBX
re-import changes scale/bounds/counts beyond exporter round-trip precision;
proof framing is clipped or misoriented; or A001-A004/quarantined A005 data
enters the input chain.

## Explicitly Forbidden

- source-visual, silhouette, material, texture, or faction redesign;
- mutation of the immutable Step 15 candidate or its three texture maps;
- hidden repair of approved LOD0 geometry;
- emissive, displacement, extra material slots, rigging, animation, or VFX;
- Unreal assets, import, configuration, maps, placement, or validation;
- Step 17 approval, `Fully game-ready`, approved-library, or visual-canon
  promotion;
- staging, committing, or pushing unrelated user work.

## Acceptance And Closeout

Pass requires all independent Step 16 technical gates, clean re-import of the
four FBX files, complete proof outputs, exact hashes, zero forbidden outputs,
and a visible review package. The pass classification is `candidate` with
pipeline status `DCC game-ready candidate`; final DCC approval remains the
separate Step 17 gate.

After pass: update the authoritative A005 status records, checkpoint, stage
only the dependency-complete Step 16 scope, audit staged paths/syntax/secrets
and unstaged in-scope differences, commit, push `main` to `assetforge`, verify
the live remote hash, record closeout metadata, checkpoint again, and stop for
the mandatory post-Step-16 restart.
