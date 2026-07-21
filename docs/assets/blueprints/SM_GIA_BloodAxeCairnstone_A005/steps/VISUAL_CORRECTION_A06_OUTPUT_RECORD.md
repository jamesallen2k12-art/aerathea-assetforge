# A005 Visual Correction A06 Output Record

Status: `candidate pending Flamestrike visual approval`

Artifact classification: `candidate`

Pipeline status: `DCC game-ready candidate`

Date: 2026-07-21

Contract ID: `A005-CR-VISUAL-CORRECTION-A06`

## Result

A06 replaces the invalid A05 structural-base footprints with the exterior-edge dimensions authorized by the A06 measurement gate. The exact A04 plinth is preserved. The complete Blender, texture, LOD, collision, FBX, final-render, and independent-audit package passes `18/18` gates with zero failures.

The result is a `candidate` and a `DCC game-ready candidate` pending Flamestrike visual approval. Unreal, Step 17, `Fully game-ready`, approved-library, and visual-canon promotion remain unauthorized and false.

## Corrected Construction

- C001: exact A04 plinth construction, geometry signature, and UV signature preserved.
- C002 upper course: exterior-measured oval footprint `123.846154 x 92.707424 cm`.
- C003 lower course: exterior-measured oval footprint `137.307692 x 105.196507 cm`.
- C004 apron: approved maximum oval footprint `140 x 110 cm`; shallow peripheral rubble only.
- Overall bounds: exact `140 x 110 x 220 cm`; pivot `[0,0,0]`.
- A05 base geometry retained or hidden in A06: `0`.
- Source-owned RGB pixels compared: `154948`; mismatches: `0`; color grading: `0`.

## Technical Package

- Blender SHA-256: `b88a6398eba9d5fbf38cb27d8b9173ce5587ac06dfe3c44b578f48fb8e94c64a`.
- LOD triangles: `8704 / 4002 / 1826 / 696`.
- Primary shells: `4`; boundary, non-manifold, and degenerate failures: `0`.
- UV layers: `UVMap` and `LightmapUV` on every LOD.
- Runtime materials: `1`; collision hulls: `4`.
- Clean FBX re-import: `4/4`.
- Exact A04 plinth geometry SHA-256: `54ceeba198e8563ea9f92beb0dbdd8f6b22e0ea38fb99591ed0f3b435cc37721`.
- Exact A04 plinth UV SHA-256: `5633bc68f1a29728764b283fb7b84b6df0d6bc3ec79892a35b6096304298104b`.
- Unreal outputs: `0`.

## Final Review Artifact

`Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A06/SM_GIA_BloodAxeCairnstone_A005_FINAL_CORRECTED_3D_A06.png`

SHA-256:
`3173234aa89c5ada67919e5d0dfbe318cc369a76199df02097784b5ac92ef578`

The final image passed every render-dependent gate, shows the complete corrected base and plinth without clipping or underside exposure, and is the only A06 image eligible for Flamestrike approval.

## Internal Attempt Disposition

- `Attempt01_ExteriorDimensions`: `proof only`; visually accepted as the deterministic pre-final render from the same audited A06 build. It is not separate approval authority.

## Stop Boundary

Flamestrike may approve, reject, or mark blocked only the exact final A06 image identified above. No Unreal, Step 17, `Fully game-ready`, approved-library, or visual-canon action is authorized by this output record.
