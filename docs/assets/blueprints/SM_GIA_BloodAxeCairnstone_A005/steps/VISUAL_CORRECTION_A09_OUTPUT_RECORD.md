# A005 Visual Correction A09 Output Record

Status: `technical pass; candidate pending Flamestrike visual review`

Artifact classification: `authoritative technical result record`

Contract ID: `A005-CR-VISUAL-CORRECTION-A09`

Date: 2026-07-21

## Result

A09 completed the approved modular-base recovery. Exact A04 C001 is retained;
C002, C003, and C004 are independent shared-origin modules with separate FBX
exports and deterministic sockets. The assembled proof has zero background
pixels across all three declared module contacts.

## Corrected Construction

- C001: exact A04 geometry and UV signatures preserved.
- C002: `19` stones plus one hidden open-top receiver; maximum footprint
  `123.846157 x 92.707424 cm`; top-proof ratio `1.33555`.
- C003: `24` stones plus one hidden open-top receiver; maximum footprint
  `137.307686 x 105.196507 cm`; top-proof ratio `1.30454`.
- C004: `32` rubble stones in `8` clusters and `2` staggered rows plus one
  hidden open-top receiver; maximum footprint `140 x 110 cm`; top-proof ratio
  `1.27171`.
- Shared-frame sockets: root, C001, C002, C003, and C004 all resolve to exact
  zero location/rotation and unit scale in the Blender source.
- Interface background leaks: `0 / 0 / 0` pixels for C001/C002, C002/C003,
  and C003/C004.

## Package Evidence

- Blender SHA-256:
  `b31f736b60ee9e6f47af143609426e64fb666bfc9b348d26eb0e27e6465aded6`.
- LOD triangles: `9020 / 4148 / 1894 / 696`.
- Module triangles: C001 `5152`; C002 `1336`; C003 `1652`; C004 `880`.
- Assembled and module clean FBX re-import: `8/8`.
- Collision hulls: `4`; material slots: `1`; UV sets: `2` per LOD/module.
- Source-owned RGB: `154948` pixels compared; mismatches: `0`.
- Required module and assembled proof set: complete.
- Independent audit: `20/20`; failures: `0`.
- Final candidate checkpoint: `Saved/ProjectRecovery/20260721-104614/`.
- Unreal outputs: `0`; `Fully game-ready`: `false`.

## Final Review Image

Path:
`Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A09/SM_GIA_BloodAxeCairnstone_A005_FINAL_CORRECTED_3D_A09.png`

SHA-256:
`33106df764ebaedf25f6aa36e7a69ee88715aa9b62119d69ee41817df8875d0b`

## Internal Attempt Disposition

- Attempts 01-06: `quarantined internal proof`; exact reasons are recorded in
  `manifests/VISUAL_CORRECTION_A09_INTERNAL_ATTEMPT_LOG.json`.
- Attempt07: `proof only`; accepted as the internal visual gate and promoted
  byte-for-byte to the exact final review image.

## Stop Boundary

The exact A09 image is a `candidate` and a `DCC game-ready candidate` pending
Flamestrike's visual decision. Unreal, Step 17, `Fully game-ready`,
approved-library, and visual-canon promotion remain unauthorized.
