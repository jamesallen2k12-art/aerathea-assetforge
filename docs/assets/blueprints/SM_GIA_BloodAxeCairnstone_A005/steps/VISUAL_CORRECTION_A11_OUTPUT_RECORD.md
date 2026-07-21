# A005 Visual Correction A11 Output Record

Status: `technical pass; candidate pending Flamestrike visual review`

Artifact classification: `authoritative technical result record`

Contract ID: `A005-CR-VISUAL-CORRECTION-A11`

Date: 2026-07-21

## Result

A11 completed the authorized pixel-exact geometry correction. It retains exact
A04 C001, applies the approved A10 owner-view footprint ratios to fresh
C002/C003/C004 construction, closes the owner-view assembly interfaces, and
removes the false circular depth, exposed receiver skirt, and bright rubble
slits found during the internal correction attempts.

## Corrected Construction

- C001 contact authority: `94.305556 x 57.239819 cm`; exact A04 C001 geometry
  and UV signatures preserved.
- C002: `19` visible stones; `118.611111 x 77.149321 cm`; visible height
  `11.25 cm`, inside the approved `8.235294-11.666667 cm` interval.
- C003: `24` visible stones; `134.166667 x 96.063348 cm`.
- C004: `32` rubble stones in `8` clusters and `2` staggered rows;
  `140 x 110 cm` exterior and `0-9 cm` visible Z interval.
- Three source-hidden inset receivers use closed owner-view top caps. The C004
  receiver is limited to `7.75-10.00 cm` behind the C003/C004 contact.
- All hidden construction choices remain declared interpretation; they are not
  reclassified as A10 measurement evidence.
- A09 assembled geometry inputs: `0`.

## Package Evidence

- Blender SHA-256:
  `6d484a452f217eedf5dbee367aacc79db6129305560ed7e20af4599538b06dc5`.
- LOD triangles: `9236 / 4248 / 1938 / 725`.
- Module triangles: C001 `5152`; C002 `1408`; C003 `1716`; C004 `960`.
- Assembled and module clean FBX re-import: `8/8`.
- LOD0 topology: `79` components, `0` boundary edges, `0` nonmanifold edges,
  `0` degenerate faces.
- Collision hulls: `4`; material slots: `1`; UV sets: `2` per LOD/module.
- Source-owned RGB: `154948` pixels compared; mismatches: `0`.
- Declared interface background leaks: `0 / 0 / 0` pixels.
- Independent audit: `26/26`; failures: `0`.
- Post-job checkpoint: `Saved/ProjectRecovery/20260721-114734/`.
- Unreal outputs: `0`; `Fully game-ready`: `false`.

## Final Review Image

Path:
`Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A11/SM_GIA_BloodAxeCairnstone_A005_FINAL_CORRECTED_3D_A11.png`

SHA-256:
`a4a2033e5758e99c3f9cf2d2fffdc60aa213a714f001560246d2ad473e59555b`

## Internal Attempt Disposition

- Attempts 01-06: `quarantined internal proof`; exact defects and smallest
  recovery actions are recorded in
  `manifests/VISUAL_CORRECTION_A11_INTERNAL_ATTEMPT_LOG.json`.
- Attempt07: `proof only`; accepted as the internal visual gate and promoted
  byte-for-byte to the exact final review image.

## Stop Boundary

The exact A11 image and DCC package are a `candidate` / `DCC game-ready
candidate` pending Flamestrike's visual decision. Unreal, Step 17, `Fully
game-ready`, approved-library, and visual-canon promotion remain unauthorized.
