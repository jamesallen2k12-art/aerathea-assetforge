# Siege Breaker Visual Fidelity A04 Strict Scanline Reconstruction Contract

- Contract ID: `SB-VF-A04-STRICT-SCANLINE`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-21
- Approver: Flamestrike
- Approval statement: "I want you to use the exact process that we used for the Cairn Stone ... You will again have full authority and approval ... I just want to see the final completed image."
- Artifact status: `authoritative`
- Execution state: `approved and queued for the first post-reset production turn`

## Decision

Rebuild the Siege Breaker in a fresh A04 line using the successful Cairn Stone
strict-pixel procedure as construction authority. The full lossless scan, exact
source-owned pixel contours, component ownership, and exact-copy visible color
data must drive the reconstruction. A03 used pixel-registered comparison but did
not use the complete scan as geometry and texture construction authority; A04
must correct that distinction.

The requested review behavior is also authoritative: do not present intermediate
candidate images. Run internal evidence and validation gates, iterate internally,
and open only the final completed A04 image for Flamestrike unless an evidence
block makes completion impossible.

## Controlling Truths

1. The approved final-package concept sheet is the visual source.
2. The exact physical envelope remains `52 x 32 x 170 cm`.
3. The large three-quarter hammer render is primary visible-projection authority.
4. Orthographic panels may define depth, hidden construction, and component
   structure after normalization to the exact centimeter envelope; their drawn
   scale may not silently override the numeric dimensions.
5. A complete scanline record already proves that the approved sheet can be
   reconstructed with `changed_pixels=0` and `max_rgb_delta=0`; A04 must create
   and verify a fresh A04-owned capture before geometry.
6. A01, A02, and A03 geometry and textures are forbidden as A04 construction
   inputs. They remain negative evidence or review history only.
7. The hidden back, underside, depth, material response, and lighting not encoded
   by source pixels remain documented interpretation. They may not alter the
   primary source-owned projection.

## Exact Cairn Stone Procedure Bound To A04

The authoritative process reference is the successful
`SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21` chain. A04 must reproduce these
controls:

1. **Fresh source-only start**
   - Read the approved source directly.
   - Do not derive geometry, masks, texture pixels, proportions, or camera values
     from any prior generated Hammer candidate.
2. **Lossless scanline capture**
   - Run `Tools/DCC/scanline_image_capture.py` against the approved source.
   - Use the `AET_RGB_SCANLINE_V1` record.
   - Require identical scan, target, and rebuild pixel hashes.
   - Require `pixel_exact=true`, `changed_pixels=0`, `max_rgb_delta=0`, and
     `mean_grayscale_delta=0.0`.
3. **Fresh lossless panel and component evidence**
   - Crop directly by integer source coordinates with no resampling.
   - Record every crop rectangle, mask rule, coordinate origin, pixel span, row
     boundary, landmark, component boundary, and unknown/occluded region.
   - Preserve all visible source RGB values exactly.
4. **Declared coordinate frame and view ownership**
   - Lock world axes, pivot, source-view camera, projection, crop, resolution,
     color management, and component orientation before geometry.
   - The primary three-quarter view owns its visible silhouette, component
     boundaries, ornament placement, cracks, runes, highlights, and color regions.
   - Secondary views own only their visible, non-conflicting depth and hidden-form
     evidence after numeric normalization.
5. **Declared measurement-selection rules**
   - Visible measurements may use only `exact`, `source_priority`,
     `outer_envelope`, `inner_envelope`, or `direct_constraint`.
   - Averaging, smoothing, analytic replacement, nearby-row searches, and
     convenient procedural substitutes are forbidden for visible source-owned
     forms.
6. **Source-owned geometry construction**
   - Generate fresh component contours from exact source masks and scanline runs.
   - Preserve the separate ownership of runestone masses, nested metal frame,
     core, collar, shaft, leather grip, and pommel.
   - Do not replace visible traced contours with boxes, superellipses, generic
     bevel profiles, averaged shells, or an A03-derived silhouette.
   - Classify every seam as visible exterior, interior, occluded contact, or
     inferred hidden.
7. **Exact-copy visible color path**
   - Visible source-owned base-color regions must be copied exactly from source
     pixels.
   - No filtered resize, color repaint, palette approximation, or resampled atlas
     panel is allowed for those regions.
   - Normal, ORM, emissive, and hidden fill may be constructed only after the
     exact-copy visible base-color gate passes; inferred regions must be tagged.
8. **Measured interfaces and production closure**
   - Component contacts must use declared measurements with no artificial gaps,
     lifts, or visual stretch strips.
   - Shipping meshes must be closed, transforms applied, UVs valid, scale exact,
     and LOD/collision/export requirements satisfied.
9. **Fail-closed audit before review**
   - Adapt the Cairn Stone asset audit and
     `Tools/DCC/strict_pixel_asset_gate.py` for A04.
   - Do not render or present the final review image unless every required strict
     gate passes.

## Hammer-Specific Reconstruction Order

1. Lock and hash the exact concept source and numeric package.
2. Produce the fresh A04 scanline capture and zero-difference proof.
3. Extract the full-resolution primary render and secondary panels without
   resampling.
4. Create source-owned component masks and exact per-row/per-column contour data
   for the complete hammer and each major component.
5. Record the source-to-world and source-to-camera formulas and run a pre-geometry
   audit.
6. Build a fresh closed 3D visual hull and component assembly from the traced
   projections, starting with the primary silhouette and then resolving depth
   from compatible secondary evidence.
7. Apply exact-copy visible color regions and construct tagged hidden-surface,
   normal, ORM, and emissive data.
8. Generate LOD0-LOD3, collision, FBX, GLB, and clean-reimport evidence without
   weakening the source-owned LOD0 silhouette.
9. Lock the authority camera and iterate internally until the strict projection,
   component, color, and technical gates pass.
10. Produce and visibly open only the final completed A04 image for Flamestrike.

## Required Gates

### Source and color gates

- Full source scanline reconstruction: exactly zero changed pixels.
- Lossless panel crops: exact integer-coordinate copies.
- Visible source-owned texture regions: exactly zero changed RGB pixels.
- Atlas source regions: exact nearest-copy data with no filtered resampling.
- Source, scan, crop, mask, texture, render, Blender, and export hashes recorded.

### Projected geometry gates

- Primary registered silhouette: direct traced contour, not a proxy envelope.
- Exterior boundary mean displacement: `<= 1.0 source pixel` after registration.
- Exterior boundary 95th-percentile displacement: `<= 2.0 source pixels`.
- Major component-mask IoU: `>= 0.97` for every source-visible major component.
- Major landmark-center error: `<= 2.0 source pixels`.
- No visible measured component is replaced by an analytic or averaged shape.
- No A01/A02/A03 mesh or texture data is used as A04 construction authority.

### Physical and production gates

- Overall dimensions: exactly `52 x 32 x 170 cm` within declared floating-point
  export tolerance.
- Required shaft, grip, pommel, and head intervals remain compliant with the
  final-package numeric authority.
- Visible component contacts have no undeclared gap, lift, or center offset.
- LOD0 remains within the approved large-prop target unless a documented traced
  contour requires a narrowly justified exception.
- LOD0-LOD3, collision, UVs, PBR maps, FBX/GLB, and clean reimport all pass.

### Final visual gate

The strict technical gate proves that the process and measurements are valid; it
does not self-approve artistry. The only user-facing review artifact is the final
completed A04 image opened in a dedicated visible window. Flamestrike remains the
authority for `approved`, `rejected`, or `blocked` visual classification.

## Artifact Status And Boundaries

- Approved source image, numeric specification, fresh A04 scanline proof, and
  this contract: `authoritative`.
- A03 DCC package: `quarantined as an A04 visual solution; reference only for
  defect history`.
- A03 audits and comparisons: `proof only`; they do not authorize A04 geometry.
- A04 working outputs before strict-gate completion: `candidate`.
- A04 final DCC package after strict-gate completion: `DCC game-ready candidate
  pending Flamestrike visual approval`.
- Unreal import: not authorized by this contract.
- `Fully game-ready`: false until a separately authorized Unreal phase passes and
  Flamestrike approves the asset.

## Reset / Resume Instruction

On the first turn after reset:

1. Read `AGENTS.md`.
2. Read the latest recovery-journal entry and checkpoint.
3. Read the Hammer reset state, this contract, approval log, artifact index, and
   source scanline manifest.
4. Report the resume summary required by Core.
5. Execute this contract end-to-end without requesting another approval unless a
   source or technical contradiction creates a genuine evidence block.
6. Do not show intermediate renders. Open only the final completed A04 image.
