# A12 R10 Step 02 Component-Equation Contract — Draft

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract ID: `SB-A12-R10-S02-COMPONENT-EQUATIONS-A01`
- Date: `2026-07-23`
- Status: `draft; awaiting Flamestrike approval`
- Governing process: `A12 R7 Component-Geometry Recovery Plan, Step 02`
- Input measurement record:
  `manifests/A12_R10_STEP01_SOURCE_MEASUREMENT_CENTERLINE_A01.json`
- Output ceiling after later construction: `DCC source candidate pending
  Flamestrike visual approval`
- Blender execution authority from this draft: `false`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Decision This Contract Produces

Approve or revise the exact equations that convert the already approved R10
measurements into the R7 component construction sequence.

This contract does not authorize a new representation. It continues the
documented source-pixel half-construction process and replaces only the center,
axis, rotation, and duplication registrations that R8 was created to correct.

## Governing Inputs

1. Original front, back, left, right, true axial top, and true axial bottom
   source pixels and their locked hashes.
2. A09 source-pixel visual-match scale and approved visible appearance.
3. A11 outer head footprint:
   `75.130513051 x 44.299176584 cm`.
4. R6 narrow proof mechanics:
   - front physical half to back by `(X,Y,Z)->(X,-Y,Z)`;
   - front-derived cylindrical UV with exact `pi/2` wrapping.
5. R7 component sequence and fail-closed gates.
6. R10 A01 exact scanline captures, component ledger, station measurements,
   original-source landmarks, and independent `183/183` replay.
7. R8 only for these transform relationships:
   - structural origin `(X,Y)=(0,0)`;
   - no unintended internal translation or rotation;
   - each outward face motif is centered on its own face-local vertical
     centerline;
   - outward face motifs are face-on only in left/right views and edge-on or
     occluded in true axial views.

No R8 silhouette, size, color, material, component contour, radius, or surface
detail is a construction input.

## Resolved Step 01 Blocks

### R10-S01-B01 — Strike-Face Centerline

The R8 transform relationship resolves the original landmark choice:

- positive-X/right source centerline:
  exact emissive motif center edge `x = 1095/2 = 547.5 px`;
- negative-X/left source centerline:
  exact emissive motif center edge `x = 473 px`.

Each value maps to face-local `u=0`. The shaft axis is forbidden as a
substitute. Rail-midpoint residuals remain recorded source asymmetry and do not
move the motif off the R8-authorized face centerline.

Only one source half, `u>=0`, is constructed. Its opposite half is produced
once by:

`(u,v,w) -> (-u,v,w)`.

The completed face must contain one division and one motif.

### R10-S01-B02 — Strike-Face / Stone Ownership Boundary

`C04` and `C05` are declared joined exterior owner surfaces of their
corresponding stone volumes, not independently backed plates.

- The original right/left source scanline boundary owns the complete visible
  outward Y/Z face contour.
- The approved C02/C03 X domains own the stone volume behind that contour.
- The strike-face owner replaces the stone's outward exterior faces at the
  shared boundary; it does not add a coplanar facade, backing card, second
  shell, or hidden plate.
- The interface is therefore the same topological boundary, with one exterior
  face occurrence and no unmeasured strike-plate thickness.

This preserves the documented single-closed-half rule and removes the need to
invent a hidden strike-face/backing thickness.

### R10-S01-B03 — Rotational Radius Authority

For C06, C09, C10, C11, and C12, the radius at each approved R10 Z station is
the positive-half distance from the owning front-source structural axis to the
exact selected visible envelope edge:

`r_raw(z) = abs(x_edge(z) - x_axis_front) * (170 / 1111)`.

The recorded radius ratios are preserved. Only the two explicit physical locks
may uniformly register a profile:

- C10/C11 combined pommel interval: `18 cm` long, `11 cm` maximum diameter;
- C07 true haft: constant radius `2.5 cm`.

The rotational surface equation is:

`P(z,theta) = (r(z)cos(theta), r(z)sin(theta), z)`.

No silhouette extrusion, ellipse, hand-selected taper, or R8 radius is
permitted.

### R10-S01-B04 — Front/Back Rotational Residuals

The documented front-half process controls physical rotational geometry:

- original front scanlines own `r(z)` and longitudinal station geometry;
- original back pixels own back-facing color registration only;
- back-envelope residuals are audit evidence and may not average, stretch, or
  elliptically rescale the front-derived physical solid.

This is the same source-ownership rule already used by the approved
front-half/depth-duplicate process.

### R10-S01-B05 — Component Stations

Semantic transitions use the exact R10
`component_station_measurements` and `approved_lock_projections` table.

- C08 grip length remains exactly `42 cm`.
- C10/C11 combined pommel interval remains exactly `0..18 cm`.
- C07 true-cylinder structural volume continues between the declared pommel
  and head contact stations.
- C06/C09 decorative collars remain distinct rotational owner surfaces at
  their exact recorded front-source transition rows.
- If two decorative envelopes overlap at a transition row, the lower
  half-open interval owns the shared row and the upper interval begins at the
  next exact row. No averaging or visually chosen cut is permitted.

### R10-S01-B06 — Hidden-Surface Closure

The documented single-closed-half rule controls closure:

1. Build only source-visible component boundary faces.
2. Connect corresponding measured boundary edges by ruled faces inside the
   approved component domain.
3. A ruled closure may not exceed the measured envelope, cross another
   component domain, occupy a source-connected negative space, or create a
   second exterior face.
4. Shared component contacts use one common boundary; coincident independent
   walls are forbidden.
5. Center-plane closure faces are removed before the final approved depth
   duplicate and weld.

This is deterministic topological closure, not a new inferred exterior shape.

### R10-S01-B07 — Axial Translation And Rotation

Apply the approved R10 equation-only transformations to original-source
coordinates:

`p_target = R(-source_axis_angle) * (p_source - internal_center) + outer_center`.

- top: translation `(+1.5,-0.25) px`, rotation `0 degrees`;
- bottom: translation `(-10.5,+31.0) px`,
  rotation `-1.123302714075429 degrees`.

After transformation, the shared internal structural origin is `(0,0)` with
zero unintended rotation. Original pixels remain unchanged.

### R10-S01-B08 — Physical Strike-Face Pitch

Pitch is derived only after the face-local motif center is registered to
`u=0`.

For each side independently, let `c(z)` be the exact midpoint of the
source-owned outward face span at source row `z`. Convert the side-view
horizontal offset and longitudinal row interval with that source's uniform
scale:

`y_world(z) = (c(z) - c_centerline) * source_cm_per_pixel`

`z_world(row) = 170 * (source_bottom_edge - row) / source_object_height`

`pitch = atan2(y_world(z_top)-y_world(z_bottom), z_top-z_bottom)`.

The right equation owns the positive-X strike face and the left equation owns
the negative-X strike face. The prior front-derived `0.907107... degree`
projection consequence is retained only as comparison evidence and is not the
3D pitch.

## Component Construction Order

The R7 order remains unchanged:

1. isolated C04/C05 strike-face half proof;
2. C01/C02/C03/C06 component and negative-space proof;
3. C09/C10/C11/C12 rotational proof;
4. one complete physical front half;
5. exact depth duplicate, weld, component-specific static UVs, and full review.

No later component may be used to repair an earlier failed proof.

## Haft Cylinder And Pixel Wrap

C07 is a true `5 cm` diameter cylinder on `X=0,Y=0`.

For each 180-degree source half:

`theta(U) = -pi/2 + pi*U`

`X = 2.5*cos(theta)`

`Y = 2.5*sin(theta)`

`Z = measured longitudinal coordinate`

The flat-diameter-to-half-circumference factor is exactly:

`pi/2 = 1.5707963267948966`.

Front and back use separate static `UVMap` islands with nearest exact
source-pixel sampling. Generated, Object, Tube, or procedural shader
coordinates are forbidden.

## Fail-Closed Gates

Stop immediately if:

- any immutable source or R10 evidence hash changes;
- an R8 pixel supplies shape, dimension, radius, color, or material;
- a face half contains a complete motif before duplication;
- a completed face contains more than one motif;
- a component exceeds its approved domain;
- source-connected negative space becomes occupied;
- a joined boundary creates a facade, backing plate, duplicate wall, or gap;
- a rotational station differs from its approved source ratio/physical lock;
- the haft differs from a circular `5 cm` diameter or exact `pi/2` wrap;
- the final duplicate differs from `(X,Y,Z)->(X,-Y,Z)`;
- any source-background pixel is mapped;
- an isolated proof or independent audit fails.

## Required Approval And Stop

Approval of this exact Step 02 contract authorizes only R7 Step 03: the
isolated strike-face half proof. Steps 04 through 07 remain behind their
documented approval gates. It does not authorize FBX, LOD, collision, Unreal,
game-ready classification, or self-approval.

Blender remains stopped until Flamestrike approves, revises, rejects, or keeps
this Step 02 contract blocked.
