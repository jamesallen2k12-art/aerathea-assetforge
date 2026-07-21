# A005 Visual Correction A10 Pixel-Exact Base Reconciliation

Status: `approved authoritative pixel ratios with conditional physical conversion`

Artifact classification: `authoritative measurement record`

Date: 2026-07-21

## Decision

The approved front-X and left-Y native-pixel owner samples prove that A09 overstates depth for every structural interface. This is the measured cause of the circular base read.

Flamestrike approved this measurement package on 2026-07-21, including the explicit C002 height interval of `8.235294-11.666667 cm`. No single course height or geometry was approved.

## Pixel-Exact Ratios

- C001 contact: `194/288` in X and `115/221` in Y.
- C002 exterior: `244/288` in X and `155/221` in Y.
- C003 exterior: `276/288` in X and `193/221` in Y.
- C004 exterior normalization: `288/288` in X and `221/221` in Y.

## Conditional Physical Conversion

These values are conditional on retaining the current `140 x 110 cm` C004 production envelope:

- C001 contact: `94.305556 x 57.239819 cm`.
- C002 exterior: `118.611111 x 77.149321 cm`.
- C003 exterior: `134.166667 x 96.063348 cm`.
- C004 exterior: `140 x 110 cm`.

## Remaining Blocks

- The source proves height intervals, not one exact per-course height allocation.
- The 48 exact top contacts remain discrete; no hidden contour closure is claimed.
- Socket clearances and hidden interface profiles remain construction decisions for the next approved geometry contract.

## Evidence

- Manifest: `manifests/VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION.json`
- Independent validation: `manifests/VISUAL_CORRECTION_A10_PIXEL_EXACT_BASE_RECONCILIATION_VALIDATION.json`
- Review board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A10_Measurement/SM_GIA_BloodAxeCairnstone_A005_A10_PIXEL_EXACT_BASE_RECONCILIATION.png`
- Review board SHA-256: `f1003ba699b6accb11b1ba29874ca59e83a750a6f4d82e7f9b1efb5291743031`

No source, geometry, Blender, FBX, texture, material, or Unreal artifact was modified.
