# A10 Derived Orthographics A01 Output Record

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract: `SB-ORTHO-A10-DERIVED-A01`
- Date: 2026-07-22
- Artifact status: `candidate derived orthographic review pending Flamestrike decision`
- Independent audit: `pass 25/25; proof only`

## Result

Blender rendered six true orthographic views from the approved A09 source:
front, back, left, right, top, and bottom. Every view uses the same `190 cm`
orthographic scale, the same `1200 x 1600 px` frame, and the evaluated model
bounds center at `0, 0, 85 cm`.

The approved A09 source SHA-256 was
`06ffb121d00cddb7b9e30a60067a5036a851d285f15daca3bffe3a663fd6d78f`
both before and after rendering. The source was not saved or modified.

## Verified Model Identity

- dimensions: `75.130516 x 32.957619 x 170.000000 cm`;
- vertices: `435278`;
- polygons: `435276`;
- location and rotation: identity;
- scale: `1, 1, 1`.

## Outputs and Hashes

- front: `9081a024b26eb1075cc46663617cc7862ab1a171d95e6be38ea362491e934d5b`;
- back: `8803cd319f66346fe1a5a4bbd06d2520d4bd5c0abf0acfa5df94c5b2e7fe7878`;
- left: `040a91417e4fa14725fee16a2cfdbfab135a38bfe1ad3b8795df5b369f76f67e`;
- right: `d38003a668d98499c769d5ffebd6baabe355b3e67e46cb31d965e04e74a7f58e`;
- top: `6914415b5cfe855b6c3b9bf0d3d8f685caba66bd8ca7f6a62b8ecc9716d54d75`;
- bottom: `fe9e6f4ff51d5a9eca58f4b87d50f62c0a2d45f582bf302688e6d9643ef39ab0`;
- six-view review board:
  `537dc63f1701adbca061efd8416061b56d455a5ea865c7e917902e33c0ef1704`.

## Boundary

- Blender 3.0.1: used.
- Image-generation software: not used.
- TRELLIS/TRELLIS.2: not used.
- Image-to-3D: not used.
- Mesh, material, UV, scale, or transform edits: none.
- Export, retopology, LOD, collision, and Unreal authority: `false`.
- `Fully game-ready`: `false`.

## Decision Gate

The board accurately exposes the approved source from all six axes, including
previously unreviewed top and bottom structure. Technical validation cannot
approve those visible surfaces. Flamestrike must decide `approved`, `revise`,
`rejected`, or `blocked` before any next production step.

## Source-Authority Recovery Addendum

Flamestrike identified that `siege_breaker_top_view.png` and
`siege_breaker_bottom_view.png` are not true axial top/bottom projections.
Repository inspection found no genuine original axial end views. The A10
`+Z/-Z` renders remain exact views of the approved A09 model, but they are not
source-matched evidence. See
`manifests/A10_SOURCE_TOP_BOTTOM_PROJECTION_AUTHORITY_CONFLICT_RECOVERY.md`.

That missing-source gate was later resolved when Flamestrike supplied genuine
axial top/bottom sources. The A10 top/bottom views do not match those source
pixels and remain model-derived proof only. Flamestrike subsequently resolved
the pixel-ownership conflict by approving the centered-mean top/bottom
footprint and axial depth ownership. A10 remains unchanged proof; a separate
Blender reconstruction contract is required before geometry changes.
