# A005 Visual Correction A07 Output Record

Status: `technical pass; visually rejected and quarantined`

Artifact classification: `authoritative historical technical/rejection record`

Contract ID: `A005-CR-VISUAL-CORRECTION-A07`

Date: 2026-07-21

## Result

A07 returns to the exact A04 plinth plus unchanged source and exterior-edge
measurement authority. It does not load A06 geometry. The source-derived
exterior spans now occur on the top-visible outer crown edges of C002, C003,
and C004 rather than only on lower sidewalls.

The isolated Blender, texture, LOD, collision, FBX, render, and independent
audit package passes `20/20` gates with zero failures.

## Corrected Top-Visible Crown Geometry

- C002: `123.846157 x 92.707424 cm`; target
  `123.846154 x 92.707424 cm`.
- C003: `137.307686 x 105.196507 cm`; target
  `137.307692 x 105.196507 cm`.
- C004: `140 x 110 cm`; target `140 x 110 cm`.
- Tolerance: `0.01 cm`.
- A06 geometry inputs: `0`.
- Exact A04 plinth geometry and UV signatures: preserved.

## Package Evidence

- Blender SHA-256:
  `c9e07506a5adb77e55f87db9c956c2797ccbfe8038e350661c50f1029fe73aa3`.
- LOD triangles: `8704 / 4002 / 1826 / 696`.
- Four disconnected watertight primary shells; boundary, non-manifold, and
  degenerate failures: `0 / 0 / 0`.
- Collision hulls: `4`; clean FBX re-import: `4/4`.
- Materials: `1`; UV sets: `2` per LOD.
- Source-owned RGB: `154948` pixels compared; mismatches: `0`.
- True orthographic top proof SHA-256:
  `6ba08c3b8d77def4c463ff664c7ba462438de99c56ae13e554640d9767e9f7a7`.
- Front projected hierarchy: `398 / 508 / 564 / 574 px` for plinth, C002,
  C003, and C004.
- Final displayed stone RGB distance: `8.1240`; bright fringe fraction: `0`.

## Final Review Image

Path:
`Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A07/SM_GIA_BloodAxeCairnstone_A005_FINAL_CORRECTED_3D_A07.png`

SHA-256:
`a1e90a69e1784650c9b6040f59e3f33cb0332f62c5760db88ab8542111cd3044`

## Internal Attempt Disposition

- `Attempt01_TopVisibleCrowns`: `proof only`; accepted as the deterministic
  pre-final render from the same audited A07 build.
- The first technical audit stopped at `15/16` because its C004 diagnostic
  band began above deliberately uneven crown vertices. Geometry was not
  changed. The diagnostic band was corrected to include the full visible
  crown, after which the pre-render result passed `16/16` and the complete
  result passed `20/20`.

## Stop Boundary

Flamestrike may approve, reject, or mark blocked only the exact final A07
image above. No Unreal, Step 17, `Fully game-ready`, approved-library, or
visual-canon action is authorized.

## Visual Rejection Supersession

Flamestrike rejected the exact A07 final image. The bottom ring rises above
the upper course on the right, deforms on the left, and exhibits vertically
stretched mapping. The top view does not match the concept's geometry or
individual-stone construction. The package is `quarantined`; this record's
technical evidence remains `proof only` for A08 defect analysis.
