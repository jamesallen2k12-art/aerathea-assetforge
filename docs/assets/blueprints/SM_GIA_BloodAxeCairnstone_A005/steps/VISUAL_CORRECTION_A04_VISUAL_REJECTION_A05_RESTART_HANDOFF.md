# A005 A04 Visual Rejection / A05 Restart Handoff

Status: `Core Recovery save point complete; A04 rejected; A05 measurement-first retry pending resume`

Artifact classification: `authoritative`

Date: 2026-07-21

Recovery checkpoint:
`Saved/ProjectRecovery/20260721-065312/`

Checkpoint note: `A005 A04 rejected; plinth approved reference; A05 oval
replacement-base pixel-measurement guidance attached`

## Resume Goal

Correct only the rejected base while preserving the exact A04 plinth visual
result. The next base must replace the rejected cumulative rectangular stack,
match the source's more oval footprint, and restore correct component-local
pixel/color correspondence.

## Flamestrike Decision And Exact Guidance

A04 is not approved. Flamestrike stated:

> This is better the Plinth looks perfect but the issue is still the base
> although better the base layers look like they were added to the previous
> base layer as opposed to replacing it ... they are also rectangular where
> they should be a more oval shape ... this is where the pixel perfect
> measurements may be needed to determine actual dimensions, pixel
> colorations are off on the new base but I believe this is a result of
> improper geometry shifting the actual pixel alignments ... we are seeing
> improvements though so while I cannot approve the A04 candidate we are
> making progress ... lets create a save point so we can reset context and try
> again .... make sure that the save point has the information I just provided
> attached for additional guidance

## Controlling Truths

- Project goal: match the approved A005 concept as a buildable Steps 01-16
  DCC game-ready candidate without advancing to Unreal.
- Source authority: the unchanged A005 concept image and its explicit
  source-pixel evidence.
- Approved sub-result: the exact A04 plinth looks perfect and is the visual
  reference to preserve.
- Rejected result: the complete A04 candidate and base.
- Proven evidence: A04 passed its 17 technical gates, but those gates prove
  neither an oval planform nor replacement-base visual equivalence.
- User observation: the base reads as added layers, is too rectangular, and
  has off pixel coloration.
- User hypothesis: improper base geometry shifted the source-pixel/UV
  alignment and caused the color discrepancy. This must be tested.

## Artifact Classification

- A005 source and source-pixel records: `authoritative`.
- Exact A04 plinth visual result: `authoritative visual reference`.
- Complete A04 Blender/FBX/render package: `quarantined`.
- A04 base geometry: `invalid as A05 construction authority`.
- A04 validation: `proof only` for its recorded technical scope.
- A04 texture pixels: `reference only`; no A04 base placement may be treated
  as correct correspondence.
- A01-A03: remain `quarantined`.
- A05: not yet created.

## Required First Action After Resume

Perform a measurement-only A05 source audit before editing geometry:

1. Reopen the authoritative source and identify exact upper- and lower-base
   ownership boundaries in every useful source view.
2. Measure major/minor extents, oval contour stations, centers, heights,
   contact relationships, and any occluded/unknown spans.
3. Separate exact source pixels from inferred hidden contour. Mark insufficient
   authority as blocked; do not fill it with a rectangular approximation.
4. Establish component-local source-pixel/color correspondence for each base
   surface after the contour measurements are locked.
5. Produce a measurement approval/blocked decision before building A05.

No candidate fill, inferred geometry overlay, smoothing envelope, or visual
solution preview is authorized during this measurement gate.

## A05 Build Constraints After Measurement Authority Exists

- Preserve the approved A04 plinth visual result.
- Build a replacement base; do not retain or visually reproduce the rejected
  cumulative A04/A03 base stack.
- Base layers must use source-measured oval contours, not rectangular slabs
  with rounded/noisy edges.
- Remove superseded base geometry from the A05 candidate rather than hiding it
  beneath new layers.
- Correct geometry and UV correspondence first, then compare corresponding
  pixels. Do not color-grade around a geometry defect.
- Preserve overall scale/pivot and non-conflicting Steps 01-16 technical
  requirements only where the measurement evidence does not supersede them.
- Preserve all A01-A04 files; use A05-only output paths.
- Unreal/Step 17 remains forbidden; `Fully game-ready` remains `false`.

## Resume Read Order

1. `SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md`
2. this handoff
3. `review/VISUAL_CORRECTION_A04_FINAL_REVIEW.md`
4. authoritative source image and current front/left/top measurement records
5. relevant Step 11/14 records only after checking them for conflict with this
   newer authority

## Next Decision Gate

End the first resumed action as exactly one of:

- `authoritative measurement record ready for A05 contract`; or
- `Blueprint block: source authority missing`, identifying the unmeasurable
  contour/dimension and proposing the smallest rule needed for approval.

Do not present another 3D candidate until that gate is resolved.
