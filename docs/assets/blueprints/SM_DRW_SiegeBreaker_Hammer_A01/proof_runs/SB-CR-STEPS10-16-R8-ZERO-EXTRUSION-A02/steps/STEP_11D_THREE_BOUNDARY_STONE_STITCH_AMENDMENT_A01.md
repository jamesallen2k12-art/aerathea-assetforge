# Step 11D Three-Boundary Stone Stitch Amendment A01

- Date: `2026-07-24`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Amendment ID:
  `SB-CR-R8-STEP11D-THREE-BOUNDARY-STONE-STITCH-A01`
- Recovery run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Artifact status: `authoritative`
- Decision authority: `Flamestrike`
- Affected instructions:
  `CLOSURE_C02_INNER`, `CLOSURE_C03_INNER`
- New source pixels: `none`
- New measured coordinates: `none`
- New contour or silhouette: `none`
- Added thickness or backing surface: `none`
- Protected-gap fill: `forbidden`
- Step 13 authority: `false`
- Unreal authority: `false`

## Exact Clarification And Approval

Codex reported that each affected closure names three ordered measured boundary
sets while the existing binary ruled-face formula accepts only two. Codex then
asked:

> The safest choice is to treat them as one closed perimeter and join them
> with straight triangles using only measured points. No new shape, thickness,
> or filled gaps. I recommend this approach. Do you approve that stitching
> rule for both stones?

Flamestrike responded:

> approved

This approval authorizes the exact additive construction rule below for both
stone closures and continuation of the already-approved Step 12 high-poly
build after independent validation and the required checkpoint.

## Controlling Rule

For each finished stone, the approved front, top, and corrected-bottom inner
owner edges form one closed perimeter after the one approved whole-asset
`Rz180` completion.

Fill that perimeter with deterministic straight triangles whose vertices are
only:

1. vertices of the exact measured owner-edge polylines;
2. exact intersections of those existing source edges with the approved
   candidate depth planes or `Y=0`; and
3. the same vertices produced by the one approved
   `(X,Y,Z)->(-X,-Y,Z)` completion.

No free interior point, center point, Steiner point, averaged point, projected
point, smoothed point, resampled point, tolerance weld, backing plate, or
added thickness is permitted.

## Corrected Logical Boundary Authority

The Step 11C label-only correction remains controlling:

- logical `BOTTOM_C02_INNER_OWNER_EDGE` consumes the exact stored
  `BOTTOM_C03_INNER_OWNER_EDGE` payload;
- logical `BOTTOM_C03_INNER_OWNER_EDGE` consumes the exact stored
  `BOTTOM_C02_INNER_OWNER_EDGE` payload;
- the stored bottom evidence remains unchanged; and
- the approved bottom equation remains
  `X=(1529/2-x)*52020/517681`.

The front and top logical boundary records retain their approved identities.

## Candidate-Specific Boundary Preparation

Apply this preparation independently to `rune_side` and
`metal_center_piece_side`:

1. map the front owner edge with `EQ_FRONT_XZ` and place it at
   `Y=-D_candidate/2`;
2. map the top owner edge with `EQ_TOP_XY`, place it at
   `MEAS_C02.world_z_top_cm` or `MEAS_C03.world_z_top_cm`, and retain only
   `-D_candidate/2<=Y<=0`;
3. map the corrected logical bottom owner edge with `EQ_BOTTOM_XY`, place it
   at `MEAS_C02.world_z_bottom_cm` or
   `MEAS_C03.world_z_bottom_cm`, and retain only
   `-D_candidate/2<=Y<=0`;
4. when either axial polyline crosses a candidate plane or `Y=0`, use the
   exact line intersection on its existing straight source edge;
5. preserve every remaining measured vertex and its source provenance; and
6. collapse only adjacent vertices whose canonical rational XYZ coordinates
   are exactly equal.

This preparation may clip an existing edge at an already-approved candidate
plane. It may not move an original edge or create an arbitrary sample.

## Exact Completed-Perimeter Order

The two finished stone perimeters are paired by the existing `Rz180`
completion:

- finished negative-X stone:
  logical C02 front/top/bottom boundaries plus the `Rz180` images of the
  logical C03 front/top/bottom boundaries;
- finished positive-X stone:
  logical C03 front/top/bottom boundaries plus the `Rz180` images of the
  logical C02 front/top/bottom boundaries.

For either finished stone, walk the perimeter in this exact cycle:

1. front inner owner edge from its top endpoint to its bottom endpoint;
2. one straight endpoint edge to the front endpoint of the bottom owner edge;
3. bottom owner edge from the front plane to `Y=0`;
4. one straight `Y=0` endpoint edge to the rotated counterpart bottom edge;
5. rotated counterpart bottom owner edge from `Y=0` to the back plane;
6. one straight endpoint edge to the rotated counterpart front-bottom
   endpoint;
7. rotated counterpart front inner owner edge from bottom to top;
8. one straight endpoint edge to the rotated counterpart top-back endpoint;
9. rotated counterpart top owner edge from the back plane to `Y=0`;
10. one straight `Y=0` endpoint edge to the source top owner edge;
11. source top owner edge from `Y=0` to the front plane; and
12. one straight endpoint edge back to the source front-top endpoint.

Every straight endpoint edge joins two existing authorized endpoints. It adds
no vertex and may not extend beyond either endpoint.

The raw center endpoints are intentionally not tolerance-welded. Their proven
small offsets remain source evidence and are closed only by the two straight
`Y=0` endpoint edges named above.

## Deterministic Triangle Rule

The builder must create triangle connectivity without changing the 3D
perimeter:

1. assign every perimeter vertex an immutable index in the cycle above;
2. create a convex canonical 2D parameter polygon with one ordered side for
   each of the twelve cycle members;
3. place each measured polyline vertex on its corresponding parameter side in
   exact source order using its exact cumulative source-edge length;
4. place each straight endpoint edge only between the two adjacent side
   endpoints;
5. run deterministic constrained ear clipping in counter-clockwise parameter
   order;
6. an ear is eligible only when its exact parameter-space area is positive
   and it contains no other active perimeter vertex;
7. among eligible ears, choose the one with the shortest new 3D diagonal by
   exact squared length; break an exact tie by immutable perimeter index;
8. emit the corresponding straight 3D triangle and remove that ear;
9. continue until one triangle remains; and
10. reject instead of repairing if no eligible ear exists.

This parameter polygon chooses connectivity only. Its 2D coordinates are not
geometry, UVs, texture data, or permission to move a 3D vertex.

No triangle fan center, Blender automatic ngon fill, Delaunay resampling,
beautify pass, remesh, voxelization, shrinkwrap, solidify, or freehand repair
is permitted.

## Protected-Space And Contact Guard

The owner edge is the only stone-side edge consumed from each boundary
record.

- Never use `central_owner_edge_x` or `partition_cut_edge_x` as a stone
  closure vertex.
- Never create a vertex inside a `protected_runs_half_open` interval.
- A `protected_gap` record remains an open separation between the stone owner
  and the central owner; no triangle may connect across that interval.
- A `shared_contact_cut` may contribute its exact stone owner endpoint, but
  may not create a second coincident wall.
- Every emitted triangle must pass the existing
  `GUARD_PROTECTED_NEGATIVE_SPACES` projection audit in front, top, bottom,
  and right evidence.
- Any triangle entering an approved protected source pixel invalidates that
  candidate before its `.blend` file is accepted.

## Narrow Construction-Order Amendment

The complete perimeter does not exist until the approved counterpart
boundaries exist. Therefore, for `CLOSURE_C02_INNER` and
`CLOSURE_C03_INNER` only:

1. build and validate all source-half visible owner surfaces and other
   pre-completion geometry;
2. apply the existing whole-asset `Rz180` exactly once;
3. read the six required boundary curves from the resulting exact source and
   rotated occurrences;
4. build the two stone closure surfaces with the rule above; and
5. run the independent saved-file audit before rendering.

This narrow order change does not authorize a second rotation, a local
rotation, an extra mirrored occurrence, or any other post-completion geometry.
All other Step 11 construction instructions retain their approved order and
meaning.

## Independent Fail-Closed Gates

The builder and independent validator must reject before review if:

- this amendment or any controlling authority fails its locked hash;
- a logical bottom boundary does not use the Step 11C corrected payload;
- a required boundary is absent, empty, reordered, smoothed, or resampled;
- the completed cycle is not closed topologically;
- any triangle contains a vertex outside the authorized vertex classes;
- any protected pixel is occupied;
- any source-visible owner boundary is moved or deleted;
- a tolerance weld, duplicate wall, backing surface, or thickness is found;
- the two closures do not use the same deterministic rule;
- the one whole-asset `Rz180` count is not exactly one;
- a triangle is degenerate, duplicated, self-intersecting, or non-manifold;
  or
- a candidate cannot be completed without an additional interpretation.

Failure leaves Step 12 blocked and creates no approval-ready review board.

## Authority Preserved Without Change

This amendment does not change:

- any approved source pixel, measurement, scale, equation, component station,
  or candidate dimension;
- the Step 11B high-poly/Nanite amendment;
- the Step 11C bottom C02/C03 label correction;
- the exact `64` positive-X angular divisions;
- the zero-extrusion rule;
- the one C04 local `Y=0` mirror;
- the one whole-asset `Rz180`;
- pivot `(0,0,0)` or exact `170 cm` height;
- UV, material, texture, LOD, collision, export, or Unreal scope; or
- the stop before Step 13.

## Amended Production Entry Point

The only permitted Step 12 production entry point now verifies all three
additive amendments:

```text
python3 Tools/DCC/build_siegebreaker_r8_step12_source_geometry_a01.py \
  --blueprint docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json \
  --amendment docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/STEP_11B_HIGH_POLY_NANITE_PERFORMANCE_AMENDMENT_A01.md \
  --parity-amendment docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/STEP_11C_BOTTOM_C02_C03_LABEL_CORRECTION_A01.md \
  --stitch-amendment docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/STEP_11D_THREE_BOUNDARY_STONE_STITCH_AMENDMENT_A01.md \
  --candidate {rune_side|metal_center_piece_side} \
  --output-root SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_Step12_SourceGeometry_A01/run_a/{candidate}
```

## Additional Allowed Records

Flamestrike's approval authorizes these additive records:

- this amendment;
- `../manifests/STEP_11D_THREE_BOUNDARY_STONE_STITCH_AMENDMENT_A01_VALIDATION.json`;
- additive clearance events in
  `../manifests/STEP_12_SOURCE_GEOMETRY_A01_EVENT_TRACE.jsonl`; and
- additive references in the Step 12 manifest, output record, and handoff.

After this amendment passes independently, the prior block

`Blueprint block: rule missing — three-boundary stone closure construction`

is resolved. Step 12 may resume only inside the already-approved dual-variant
high-poly DCC source, audit, proof-render, comparison-board, checkpoint,
commit, push, and stop-before-Step-13 contract.
