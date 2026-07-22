# A11 True Axial Top/Bottom Pixel-Measurement Output Record

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: `2026-07-22`
- Artifact status: `candidate measurement; source pixels authoritative`
- Geometry authority: `false`
- Independent audit: `pass 19/19; proof only`

## Authority

Flamestrike supplied two source images and declared Image 1 `Top View`, Image 2
`Bottom View`, and directed `use pixel measurements`. The printed `52 x 32 cm`
labels are retained as `reference only`; they do not control geometry.

## Exact Measurement

The established A06/A09 adaptive-luma greatest non-edge 8-connected component
method measured:

- top rectangle `[94, 330, 1106, 921)` = `1012 x 591 px`;
- bottom rectangle `[93, 330, 1106, 933)` = `1013 x 603 px`.

The top and bottom widths differ by `1 px`; their depths differ by `12 px`.
Using the approved A09 front-pixel width consequence
`491 * 170 / 1111 = 75.130513051 cm` as the shared X registration gives:

- top depth consequence: `43.875625705 cm`;
- bottom depth consequence: `44.722309348 cm`.

Both conflict with the A09 left-view pixel depth consequence
`215 * 170 / 1109 = 32.957619477 cm`.

## Decision

The missing-source block is resolved. The measurement gate stops with
`Blueprint block: pixel ownership/reconciliation rule missing`. No average,
independent-axis rescale, crop adjustment, or geometry repair has been applied.
Flamestrike must approve which pixel view owns head depth, or approve an exact
reconciliation formula, before Blender geometry changes.

## Outputs

- source measurement:
  `manifests/A11_TRUE_AXIAL_TOP_BOTTOM_PIXEL_MEASUREMENT.json`;
- independent audit:
  `manifests/A11_TRUE_AXIAL_TOP_BOTTOM_PIXEL_MEASUREMENT_INDEPENDENT_AUDIT.json`;
- measurement tool:
  `Tools/DCC/measure_siegebreaker_a11_true_axial_pixel_sources.py`;
- independent audit tool:
  `Tools/DCC/audit_siegebreaker_a11_true_axial_pixel_sources.py`.

No image generation, TRELLIS, image-to-3D, procedural overlay, Blender geometry
change, export, Unreal work, or game-ready escalation occurred.
