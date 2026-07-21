# A005 Visual Correction A08 Output Record

Status: `technical pass; visual decision pending`

Artifact classification: `authoritative technical result record`

Contract ID: `A005-CR-VISUAL-CORRECTION-A08`

Date: 2026-07-21

## Result

A08 completed the required measurement-first restart, constructed a fresh
individual-stone base with zero A07 geometry inputs, preserved the exact A04
C001 plinth, and passed the complete independent audit.

## Measurement And Construction

- Top measurement gate: `pass_authoritative_measurement_gate`.
- C002: 19 source-count individual stones; outer bounds
  `123.846157 x 92.707424 cm`; Z `23.00-34.25 cm`.
- C003: 24 source-count individual stones; outer bounds
  `137.307686 x 105.196507 cm`; Z `9.75-22.25 cm`.
- C004: 32 bounded individual rubble stones; outer bounds
  `140 x 110 cm`; Z `0-9 cm`.
- Stone clearances: C004-to-C003 `0.75 cm`; C003-to-C002 `0.75 cm`.
- Recessed mortar beds: `3`; continuous annular masonry shells: `0`.
- Exact A04 C001 geometry and UV signatures: preserved.

## Package Evidence

- Blender SHA-256:
  `c971915d5f118c8f420eef28c1c7b0692cbaebf77dcaca225f9d13c542aa724f`.
- LOD triangles: `9104 / 4186 / 1910 / 704`.
- LOD3 duplicate decimator faces removed before export: `24`; clean FBX
  reimport agrees at `704` triangles.
- Closed connected components: `79`; topology failures: `0`.
- Collision hulls: `4`; clean FBX re-import: `4/4`.
- Materials: `1`; UV sets: `2` per LOD.
- Source-owned RGB: `154948` pixels compared; mismatches: `0`.
- Fixed proofs: front, left, right, and true orthographic top all pass.
- Full independent audit: `20/20`.
- Unreal outputs: `0`; `Fully game-ready`: `false`.

## Final Review Image

Path:
`Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A08/SM_GIA_BloodAxeCairnstone_A005_FINAL_CORRECTED_3D_A08.png`

SHA-256:
`6c58c364d3522f53b6c2011bf0c5fb09abba3bb44ee6d765be715c31b0dd52b4`

## Internal Attempt Disposition

- Attempts 01-04: `quarantined internal proof`; reasons recorded in
  `manifests/VISUAL_CORRECTION_A08_INTERNAL_ATTEMPT_LOG.json`.
- Attempt05: `proof only`; accepted as the internal visual gate for the exact
  final LOD0 geometry.
- The first rebuild stopped at the 10,000-triangle gate; the unnecessary
  subdivision was removed before candidate creation.
- The first audit run exposed 24 exact duplicate LOD3 triangles; those
  duplicate reduced-LOD faces were removed without changing LOD0.

## Stop Boundary

Flamestrike may approve, reject, or mark blocked only the exact A08 final
image. No Unreal, Step 17, `Fully game-ready`, approved-library, or
visual-canon action is authorized.
