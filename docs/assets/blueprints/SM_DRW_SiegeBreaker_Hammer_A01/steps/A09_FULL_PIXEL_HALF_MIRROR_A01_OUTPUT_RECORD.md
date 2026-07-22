# A09 Full Pixel-Half Mirror A01 Output Record

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract: `SB-PHM-A09-FULL-MIRROR`
- Attempt: `A09_PixelHalfMirror_VisualMatch_A01`
- Date: 2026-07-22
- Artifact status: `authoritative for approved A09 visual match; local-only DCC source`
- Technical audit status: `pass 22/22; proof only`

## Result

Blender built one fresh `X>=0` native-source-pixel half from the immutable
front source, used the immutable left source to control depth, used the
immutable back source for rear-facing color, and applied the mirror at `X=0`.
No prior Siege Breaker candidate geometry or `.blend` was a construction input.

The completed evaluated mesh contains `435278` vertices and `435276` polygons.
Its measured envelope is `75.130516 x 32.957619 x 170.000000 cm`. Independent
five-decimal vertex pairing found `0` missing mirrored vertices.

The source-facing front comparison has a right-half mean absolute RGB delta of
`6.140577 / 255`. This is measured visual-match evidence, not a claim of zero
pixel difference. The separate gray three-quarter render is the geometry proof;
source-color projection is explicitly not treated as geometry proof.

## Outputs

- local-only Blender source:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A09_PixelHalfMirror_VisualMatch_A01/SM_DRW_SiegeBreaker_Hammer_A01_A09_PixelHalfMirror_VisualMatch_A01.blend`
- completed front:
  `review/A09_FULL_PIXEL_HALF_MIRROR_A01_FRONT.png`
- completed colored three-quarter:
  `review/A09_FULL_PIXEL_HALF_MIRROR_A01_COLOR_3Q.png`
- untextured geometry three-quarter:
  `review/A09_FULL_PIXEL_HALF_MIRROR_A01_GEOMETRY_3Q.png`
- exact review board:
  `review/A09_FULL_PIXEL_HALF_MIRROR_A01_REVIEW.png`
- builder validation:
  `manifests/A09_FULL_PIXEL_HALF_MIRROR_A01_VALIDATION.json`
- independent audit:
  `manifests/A09_FULL_PIXEL_HALF_MIRROR_A01_INDEPENDENT_AUDIT.json`

## Hash Lock

- `.blend`: `06ffb121d00cddb7b9e30a60067a5036a851d285f15daca3bffe3a663fd6d78f`
- front render: `a8d1cc06b80815d1acfa6cef85c6b48ccdae2828a5f3fb67574a686c5d720d42`
- colored three-quarter: `0a0f59100f02ddc5fe2ca5817add3666be164b3bf6cc778ece04dd85cab0f1f0`
- geometry three-quarter: `1b0d24d98d9a604824f97fa6cdc9ce91f5184722c15c9044924eae311bdb7598`
- review board: `63b52d3f0ebc4c10ff088f0d8a926281e2e136eaa609c2ede77cc19053f1dccf`

## Software and Authority Boundary

- Blender 3.0.1: used.
- Image-generation software: not used.
- TRELLIS/TRELLIS.2: not used.
- Image-to-3D: not used.
- Unreal, exports, UV/texture production, LODs, and collision: not authorized
  and not produced.
- `Fully game-ready`: `false`.

## Decision Record

Flamestrike reviewed the exact hash-locked board visibly and decided
`approved` on 2026-07-22. The approval is recorded in
`review/A09_FULL_PIXEL_HALF_MIRROR_A01_FINAL_REVIEW.md`.

The technical audit remains `proof only`. No further DCC production, exports,
Unreal work, or game-ready escalation is authorized by this decision.
