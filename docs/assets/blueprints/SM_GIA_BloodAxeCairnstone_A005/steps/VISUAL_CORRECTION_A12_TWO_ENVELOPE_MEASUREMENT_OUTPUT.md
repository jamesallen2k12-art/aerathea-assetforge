# A005 Visual Correction A12 Two-Envelope Measurement Output

Status: `approved authoritative multi-row dimension statistics`

Artifact classification: `authoritative measurement record`

Contract ID: `A005-CR-VISUAL-CORRECTION-A12-MEASUREMENT`

## Result

The direct `120 x 90 cm` labels cannot authorize C003: the approved source records explicitly assign them to C001 maximum width/depth. The tested structural-plinth mapping is rejected as an authority conflict.

The evidence-backed alternative is the median of every approved C002/C003 row sample rather than A10's single widest row. Conditional on C004 remaining `140 x 110 cm`, the approved median extents are:

- C002: `112.291667 x 76.651584 cm`.
- C003: `129.548611 x 96.063348 cm`.
- C004: direct label authority remains `140 x 110 cm`.

Flamestrike approved these median values as dimensional authority for a separate geometry contract. They do not authorize a geometry rebuild by themselves.

## Evidence

- Manifest: `manifests/VISUAL_CORRECTION_A12_TWO_ENVELOPE_MEASUREMENT.json`
- Validation: `manifests/VISUAL_CORRECTION_A12_TWO_ENVELOPE_MEASUREMENT_VALIDATION.json`
- Review board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A12_Measurement/SM_GIA_BloodAxeCairnstone_A005_A12_TWO_ENVELOPE_RECONCILIATION.png`
- Board SHA-256: `8e49df2da9140d60f0ac337c4c0b9e1d05940380182bae5ee5c3958bb7f248b0`
- Post-audit checkpoint: `Saved/ProjectRecovery/20260721-121816/`
- Approval/renewal checkpoint: `Saved/ProjectRecovery/20260721-122558/`

No source, Blender, FBX, texture, material, collision, LOD, Unreal, or canon artifact was modified.

## Decision Gate

A separate visible geometry-correction contract must be drafted and approved before any rebuild. No rebuild is authorized by this output alone.
