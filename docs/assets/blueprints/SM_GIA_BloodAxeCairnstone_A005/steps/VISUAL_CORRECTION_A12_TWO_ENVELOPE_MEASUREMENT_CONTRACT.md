# A005 Visual Correction A12 Two-Envelope Measurement Contract

Status: `approved for measurement-only execution`

Artifact classification: `authoritative execution boundary`

Contract ID: `A005-CR-VISUAL-CORRECTION-A12-MEASUREMENT`

Date: 2026-07-21

## Approval

Flamestrike approved an A12 measurement-only two-envelope reconciliation after
the A11 candidate remained visually unresolved at the base.

## Authority

- Exact STEP_03 front and left source panels and their approved manual row
  samples.
- Approved A10 owner-view reconciliation and pixel-center-delta convention.
- Direct source labels: C004 base footprint `140 x 110 cm`, total base height
  `35 cm`, and C001 maximum width/depth `120 x 90 cm`.
- Exact A04 C001 remains preserved and is not modified by this pass.

## Required Test

1. Test whether `120 x 90 cm` can authorize a structural-plinth envelope.
2. Preserve the source record's actual label ownership; do not silently move
   C001 labels to C003.
3. Compare A10's widest-row C002/C003 spans with the median of every approved
   row sample for the same component and owner view.
4. Express median width/depth relative to the `35 cm` base-height label and
   conditionally in centimeters against C004 `140 x 110 cm`.
5. Present source pixels, exact row marks, formulas, pass/fail findings, and
   blocked unknowns only.

## Prohibited

- Candidate fills, closed contours, fitted ovals, smoothed envelopes, or
  geometry previews.
- Blender, FBX, texture, material, collision, LOD, Unreal, canon, or library
  changes.
- Reclassification of a tested hypothesis as authority without Flamestrike's
  explicit approval.

## Required Outputs

- A12 measurement manifest.
- Independent validation manifest.
- One visible technical review board.
- A12 measurement output record.

## Stop Boundary

Stop after the audited measurement board. Flamestrike may approve the
multi-row statistic as later construction authority, reject it, or mark the
measurement blocked. No geometry rebuild is authorized by this contract.
