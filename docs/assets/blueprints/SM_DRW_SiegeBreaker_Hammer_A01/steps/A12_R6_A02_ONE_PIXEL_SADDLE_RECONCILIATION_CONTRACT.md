# A12 R6 A02 One-Pixel Saddle Reconciliation Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Parent contract: `SB-AXIAL-A12-R6-SINGLE-CLOSED-HALF`
- Amendment ID: `SB-AXIAL-A12-R6-A02-ONE-PIXEL-SADDLE`
- Date: `2026-07-22`
- Status: `draft; Flamestrike approval required before execution`
- Artifact ceiling: `DCC source candidate pending Flamestrike visual decision`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Exact Block

R6A01 stopped before output because one source-pixel checkerboard saddle makes
the otherwise valid open half non-manifold. It produces `110` four-face edges
only because the same X/Z corner is extruded through 110 right-owned Y cells.

- grid edge: `X=1 px`, `Z=1102 px`;
- world edge: `X=0.153015301530 cm`, `Z=168.622862286229 cm`;
- occupied diagonal cells: `(X-cell=1,Z-layer=1101)` and
  `(X-cell=0,Z-layer=1102)`;
- missing center-adjacent cell: `(X-cell=0,Z-layer=1101)`;
- exact front source pixel for that cell: global `(563,202)`,
  `RGB(212,192,169)`, integer luma `195 <= 234`.

The missing cell is therefore front-source-owned object evidence. It was
excluded only by the conservative reversed-back silhouette intersection.

## Proposed Exact Reconciliation

1. At only `(X-cell=0,Z-layer=1101)`, front ownership takes precedence over the
   reversed-back silhouette intersection.
2. Add that one front-owned X/Z cell through only the already authorized
   right-view Y membership at the same registered world Z.
3. Mirror the resulting source half only after the half audit proves the 110
   four-face edges are gone and all remaining open edges lie on `X=0`.
4. On the added cell's back-facing boundary only, sample the nearest exact
   selected back-source pixel at the same common registered component row.
   Do not paint, average, generate, or composite a replacement pixel.
5. Record the exact source coordinate and sampling displacement in the audit.

The geometric consequence is one source pixel, `1.530153015 mm` in X by
`1.530153015 mm` in Z, on the positive half and its exact mirrored counterpart.
No other source cell may be filled, deleted, beveled, smoothed, or remeshed.

## Required Gates

- pre-mirror edge incidence is exactly two except open edges whose two vertices
  are both on `X=0`;
- pre-mirror four-face edges: `0`;
- final mirror/weld edge incidence: exactly two everywhere;
- internal center-plane faces: `0`;
- duplicate faces: `0`;
- all other R6 contract gates remain unchanged;
- if any other topology conflict appears, stop and classify A02 `invalid`.

## Exclusions

- no general morphological fill or hole closing;
- no broad source-owner precedence rule;
- no R5 input or repair-forward;
- no image generation, TRELLIS, image-to-3D, derived source composite, FBX,
  Unreal, LOD, collision, or game-ready work.

## Approval Gate

No further Blender construction is authorized until Flamestrike approves this
exact one-pixel front-owner precedence rule.
