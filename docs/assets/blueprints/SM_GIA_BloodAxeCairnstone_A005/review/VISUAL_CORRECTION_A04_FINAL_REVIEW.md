# A005 Visual Correction A04 Final Review

Status: `candidate pending Flamestrike visual review`

Artifact classification: `candidate`

Date: 2026-07-21

Contract ID: `A005-CR-VISUAL-CORRECTION-A04`

## Decision

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

Approval accepts only this exact A04 DCC candidate and review image. Unreal,
Step 17, `Fully game-ready`, approved-library, and visual-canon promotion
remain unauthorized and false.
