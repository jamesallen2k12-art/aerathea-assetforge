# A12 R4 Side-Owner Strike-Face Reconstruction Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract ID: `SB-AXIAL-A12-R4-SIDE-OWNER-FACES`
- Date: `2026-07-22`
- Status: `approved for exact bounded execution`
- Artifact ceiling: `DCC source candidate pending Flamestrike visual decision`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Flamestrike Approval

Flamestrike rejected the warped colored R3 three-quarter view, clarified that
“faces of the hammer” means the left-side and right-side outward strike faces,
directed that their geometry can be taken from the `-X` and `+X` views, and
approved the bounded R4 correction.

## Preserved Authority

- A09 approved front/three-quarter visual match and fresh half/mirror method.
- A11 centered arithmetic-mean head footprint:
  `75.130513051 x 44.299176584 cm`.
- R3 centered core and separate mirrored stone component partition:
  core `34.675621408 cm`; each stone `20.227445822 cm`.
- Overall `170 cm` longitudinal scale and `X=0` mirror plane.
- No global `6 cm` transition blend.

## New Side-Face Ownership

The original side source pixels now own the visible outward strike faces:

- `-X` owner: `siege_breaker_left_view.png`, SHA-256
  `1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b`,
  exact whole-object rectangle `[397,190,612,1299)`, `215 x 1109 px`;
- `+X` owner: `siege_breaker_right_view.png`, SHA-256
  `04a1e9359d518b1dec35fe161020bd23ab9e2f8d5934f24e4184aecaa91d8330`,
  exact whole-object rectangle `[467,172,681,1270)`, `214 x 1098 px`.

The already-audited exact side-row observations at
`Z={132,136.75,141.5,146.25,151,155.75,160.5,165.25,170} cm` are evidence
anchors. R4 repeats the same exact scan membership for every intervening
source scanline across the complete source-built stone component's measured
`Z` interval. Its lower bound is read from the freshly rebuilt front-source
stone mesh, not hardcoded or taken from prior candidate geometry; the first R4
replay measured `Z=111.089111 cm`. Each row's outer member pixels are source
evidence, not an inferred contour. No printed `32 cm` value controls R4
geometry.

## Reconciliation And Construction Rule

1. Map each source's horizontal side-face coordinate into the authoritative
   A11 depth interval `Y=[-22.149588292,+22.149588292] cm` using that source's
   exact scanned crop width.
2. Preserve every audited `Z` station exactly, extend the scan to the complete
   fresh front-source stone `Z` extent, and sample every intervening source
   scanline without smoothing.
3. At each sampled row, center the left and right observed outer pixel intervals
   and use the arithmetic mean of their normalized `Y` boundaries. This is the
   single common `Y/Z` geometry profile; the one-pixel left/right crop-width
   difference therefore becomes `0.5 px` per side before normalization.
4. Construct the `+X` outward face at the exact envelope boundary
   `X=+37.565256526 cm`, with source-luma relief directed inward only.
5. Mirror that geometric solution exactly at `X=0` to create the `-X` face.
   Geometry must remain symmetric; visible materials may differ because each
   outward face retains its own original source pixels.
6. Apply one fixed crop-width-to-A11-depth coordinate map across every row.
   Apply the right source pixels only to the `+X` face and the left source
   pixels only to the `-X` face. Front/back sources continue to own only the
   visible longitudinal elevations and their connection to the centered core.
   Source-sheet background is not object color and must be removed using only
   the exact replayed source membership; no painted fill or generated pixel is
   permitted.
7. Build inward thickness only along X; Y/Z edge offset is forbidden. Replace
   or recess the former front/back-projected outward wall only where
   required to prevent it from occluding the new owner face. Do not alter the
   centered core, shaft, pommel, A11 overall footprint, or R3 component widths.
   The visible face grid must be one continuous row-connected surface; separate
   raster-cell islands and their internal closure seams are forbidden.

## Required Outputs And Gate

- one fresh-from-source Blender R4 candidate;
- exact `-X` source-versus-render and `+X` source-versus-render proofs;
- updated front, colored three-quarter, and independent gray geometry
  three-quarter proofs;
- validation and independent audit covering source hashes, owner mapping,
  exact dimensions, mirror symmetry, and prohibited-software boundary;
- one visible review board opened automatically.

Stop after the review board is visible. Flamestrike alone may classify R4 as
`approved`, `revise`, `rejected`, or `blocked`.

## Explicit Exclusions

- no image generation, diffusion, TRELLIS, image-to-3D, or generated views;
- no new orthographic art;
- no global smoothing or freehand face redesign;
- no export, UV-production pass, LOD, collision, Unreal, or game-ready work;
- no claim that technical audit success proves visual fidelity.
