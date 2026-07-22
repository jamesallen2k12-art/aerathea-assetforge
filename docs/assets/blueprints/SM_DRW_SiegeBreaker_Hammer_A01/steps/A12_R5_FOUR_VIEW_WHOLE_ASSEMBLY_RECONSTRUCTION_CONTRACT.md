# A12 R5 Four-View Whole-Assembly Reconstruction Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract ID: `SB-AXIAL-A12-R5-FOUR-VIEW-WHOLE-ASSEMBLY`
- Date: `2026-07-22`
- Status: `executed through cylindrical-haft A04; technical pass; Flamestrike visual decision pending`
- Artifact ceiling: `DCC source candidate pending Flamestrike visual decision`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Flamestrike Approval

Flamestrike identified three visible R4D defects: two differently scaled handle
facets, residual rock between the apparent handle/haft surfaces, and a handle
that is not aligned. Flamestrike approved replacing the stopped handle-only R5
proposal with a fresh whole-assembly four-view pixel reconstruction. R4D is
preserved only as quarantined evidence.

## Preserved Authority

- original front, back, left, and right source pixels and their recorded hashes;
- `170 cm` overall world-Z scale;
- bottom-center origin and one registered shaft centerline;
- construction of one `X>=0` half followed by an exact `X=0` mirror;
- A11 true-axial source evidence remains measurement authority for head depth
  only where it is consistent with the four-view registered component;
- Blender-only software boundary.

No R4D mesh is construction geometry. R4D may be read only to preserve its exact
state and to compare the corrected result against the identified defect.

## Four-View Registration Rule

1. Recompute exact source membership directly from the immutable front, back,
   left, and right PNGs.
2. Normalize each source's exact full-object Z interval to `0..170 cm`.
3. Derive each view's transverse origin from the median center of the stable
   shaft rows at common world stations `Z=90,95,100 cm`. A whole-head crop
   midpoint is forbidden as a shaft origin.
4. Measure matching component transitions and outer intervals at identical
   world-Z stations. Record source pixels, world-centimeter consequences, and
   center offsets separately for every view.
5. Front/back own X silhouette and their visible surfaces. Left/right own Y
   silhouette and their visible surfaces. No face may be locally stretched to
   hide a disagreement.
6. Trace the two stone masses, centered metal core/shaft mount, required empty
   space, handle, and pommel as separate components. A constant whole-head
   width band is not a component boundary.
7. Only after registration passes may a fresh `X>=0` assembly be constructed
   and mirrored. Surface UVs must use fixed registered world coordinates and
   common Z landmarks.

## Fail-Closed Conflict Rule

Corresponding opposite views must reverse around the registered shaft axis and
agree within the previously accepted one-pixel boundary tolerance at a given
owner surface. If they do not, stop at a measurement-only proof with:

`Blueprint block: source authority conflict`

Do not average, stretch, center by eye, infer a hidden correction, preserve
R4D geometry, or create a Blender solution until Flamestrike approves an exact
reconciliation rule.

## Approved One-Half Mirror Reconciliation

Flamestrike resolved the observed left/right same-facing conflict by approving
one complete physical half followed by duplication to the opposite side.

1. Construct only the complete `X>=0` half from fresh source pixels.
2. The front source's positive half owns the visible front silhouette and
   surface. The back source's corresponding image-left half is reversed into
   the same world-positive-X coordinate frame and owns the visible back
   surface.
3. The right source is the sole Y-depth geometry authority for the `+X` half.
   Register it around its measured shaft axis; its source-pixel scale may not
   be stretched to the conflicting A11 depth.
4. Mirror the completed geometry at `X=0`. A 180-degree Z rotation is forbidden
   because it would swap the distinct front and back surfaces.
5. Reverse the left source around its measured shaft axis for `-X` visible
   pixels and comparison. It does not independently alter the mirrored
   geometry.
6. The A11 `44.299176584 cm` depth remains historical axial evidence but is
   superseded for R5 geometry wherever it conflicts with the newly approved
   right-view half authority.
7. Preserve exact source-connected empty space in the front positive-half mask;
   do not fill it with stone, projected side wall, or transition geometry.

This approved rule clears the left/right registration block. Any different
front/back contradiction that cannot fit the one-half geometry without local
stretch remains fail-closed.

## Approved Cylindrical-Haft Static-UV Amendment

Flamestrike supplied and approved the production method for the hammer haft:

1. Replace the rectangular/front-back extruded haft solution with a true
   Blender cylinder on the registered shaft axis. Construct its `X>=0` half
   inside the approved R5 half and complete it only through the exact `X=0`
   mirror.
2. Split the cylinder by physical orientation into front `180 degrees` and
   back `180 degrees`. Assign separate `Front_Material` and `Back_Material`
   slots so neither texture can bleed onto the opposite half.
3. Use one exported static `UVMap`; Blender Generated, Object, Tube, or other
   procedural shader coordinates are forbidden for the haft.
4. Map each half-cylinder island horizontally from exact `U=0` to `U=1` and
   vertically across the measured haft interval. The named `157.08%` widening
   is implemented as a deterministic technical resize of the exact source
   crop, not as generated or repainted imagery.
5. The cylinder axis must remain exactly registered in front, back, left, and
   right views. It may not be split into independently scaled front/side/back
   slabs.
6. For the haft only, a true circular cylinder makes its Y radius equal to its
   front-owned X radius. Derive that radius from the front positive-half pixel
   boundary at each Z row; `157.08%` is the declared half-circumference to
   diameter factor. The right source still owns the shaft axis and remains a
   comparison view, but its narrower drawn diameter may not elliptically scale
   or split the true cylinder. This narrow exception does not change right-view
   depth ownership for the head, pommel, or other non-haft geometry.
7. This amendment authorizes only the Blender haft geometry, its deterministic
   derived texture crops, static UVs, proof renders, manifest, and audit. The
   supplied FBX and Unreal settings are recorded for a later gate; export and
   Unreal execution remain unauthorized now.

## Required Outputs

If registration passes:

- fresh whole-assembly Blender source;
- exact front, back, left, and right source-versus-render proofs;
- center-seam and component-gap proof;
- colored and independent gray three-quarter proofs;
- validation and independent audit;
- one visible review board and stop for Flamestrike.

If registration fails:

- exact pixel-only four-view registration measurements;
- one measurement board containing only unchanged source pixels, exact axis and
  boundary marks, formulas, numeric consequences, and the blocked unknown;
- validation/audit of the source conflict;
- visible board and stop for Flamestrike reconciliation authority.

## Explicit Exclusions

- no image generation, diffusion, TRELLIS, image-to-3D, or generated views;
- no repair-forward from R4D geometry;
- no unapproved averaging, smoothing, local texture scaling, or freehand fill;
- no export, whole-asset UV-production pass beyond the explicitly approved
  haft static UVs, LOD, collision, Unreal, or game-ready work;
- no technical self-approval.
