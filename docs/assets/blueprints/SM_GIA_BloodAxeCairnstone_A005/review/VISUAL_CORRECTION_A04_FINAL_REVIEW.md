# A005 Visual Correction A04 Final Review

Status: `visually rejected by Flamestrike; quarantined`

Artifact classification: `quarantined`

Date: 2026-07-21

Contract ID: `A005-CR-VISUAL-CORRECTION-A04`

## Flamestrike Decision

Rejected on 2026-07-21. The A04 plinth is visually approved as the exact
reference to preserve, but the complete A04 candidate is not approved.

Flamestrike's exact guidance:

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

Decision consequences:

- Preserve the exact A04 plinth as an `authoritative visual reference`.
- Quarantine the complete A04 DCC candidate, final render, and base geometry.
- Treat the A04 `17/17` validation as `proof only` for its technical scope.
- Do not use A04's rectangular base footprints or cumulative stacked-base
  read as A05 geometry authority.
- Begin the next attempt with source-pixel measurement of the base contours,
  oval footprint, and component-local color correspondence before geometry.
- Treat geometry/UV displacement as the current user-supplied causal
  hypothesis for the base color mismatch; verify it after geometry correction
  rather than applying unproven color grading.

## Historical Decision Target

Decide whether the exact A04 review image provides the required descending
three-mass structure:

1. one central tapered plinth;
2. one slab directly supporting the plinth; and
3. one visibly larger slab directly below the first slab.

The shallow peripheral ground rubble is non-structural and does not constitute
a fourth slab.

## Exact Review Artifact

`Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A04/SM_GIA_BloodAxeCairnstone_A005_FINAL_CORRECTED_3D_A04.png`

SHA-256:

`e2e62ac9a7a8ad17aa56200c6e3d2f155927498c0068cb345af45b51dd53aff1`

The exact image is opened in a visible foreground desktop window after the
independent audit pass. No internal attempt is approval authority.

## Structural Evidence

- Front proof widths: plinth `398 px`; upper slab `485 px`; larger lower slab
  `549 px`.
- Connected-shell footprints: plinth `108 x 78 cm`; upper slab
  `120.01 x 89.92 cm`; lower slab `135.84 x 103.89 cm`; shallow apron
  `140 x 110 cm`.
- Overall bounds: exact `140 x 110 x 220 cm`.
- Pivot: bottom center at `[0,0,0]`.
- Four independently closed primary shells; boundary, non-manifold, and
  degenerate failures: `0`.

## Technical Evidence

- Independent audit: `17/17` pass.
- LOD triangles: `9856 / 4532 / 2068 / 788`.
- UVs: `UVMap` and `LightmapUV` on all LODs.
- Runtime materials: `1`.
- Collision hulls: `4`.
- Clean FBX re-import: `4/4`.
- Source-owned Base Color: `154948` pixels compared; mismatches `0`.
- Final bright-fringe fraction: `0.0`.
- Source/final median stone RGB distance: `1.0`.
- A01-A03 preservation hashes: all pass.
- Unreal outputs: `0`; `Fully game-ready`: `false`.

## Internal Rejection Record

- Attempt01: `quarantined`; stopped before output at `10320` LOD0 triangles,
  above the `10000` hard cap.
- Attempt02: `quarantined`; structural read passed, but bright source-sampling
  bands contaminated non-owner faces.
- Attempt03: `quarantined`; contamination removed, but authored faces became
  nearly black and visually flat.
- Attempt04: `quarantined`; authored projections were clean but underlit.
- Attempt05: `proof only`; passed internal visual review and was rendered
  byte-identically to the final path before independent audit.
- First independent audit execution: `proof only`; stopped before Gate 1 on a
  Blender 3.0 bound-box vector compatibility defect.
- First complete audit: `proof only`; `16/17` with a false block because an
  arbitrary recessed rubble row was required to exceed the lower slab by one
  pixel. The physical footprint hierarchy already passed. The validator was
  corrected to apply the contract's non-structural rubble rule.
- Final audit: `17/17` pass.

## Boundary

The exact A04 DCC candidate and review image were not approved and are now
`quarantined`. The plinth alone remains an `authoritative visual reference`.
Unreal, Step 17, `Fully game-ready`, approved-library, and visual-canon
promotion remain unauthorized and false.
