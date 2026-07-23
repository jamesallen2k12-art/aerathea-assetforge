# A12 R6 Single Closed Half Recovery Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract ID: `SB-AXIAL-A12-R6-SINGLE-CLOSED-HALF`
- Date: `2026-07-22`
- Status: `approved for exact execution by Flamestrike on 2026-07-22`
- Artifact ceiling if approved: `DCC source candidate pending Flamestrike visual decision`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Controlling Goal

Create one coherent physical `X>=0` half of Siege Breaker, then duplicate it by
the exact `X -> -X` mirror and weld the center seam. The input half must already
be a valid closed three-dimensional object. Mirroring may not be used to hide a
facade, card, wall, overlay, source composite, or missing surface.

The exact X mirror is retained instead of a 180-degree Z rotation because a Z
rotation would exchange the distinct front and back surfaces.

## Last Core-Valid Evidence

- immutable front, back, left, right, true axial top, and true axial bottom
  source pixels and their existing hash locks;
- `170 cm` overall world-Z frame and bottom-center origin;
- measured front/back/left/right shaft axes;
- Flamestrike's requirement that the asset be made from one complete physical
  half, duplicated/mirrored, and connected exactly;
- Flamestrike's findings that R5A04 contains layered faces and white lines and
  is not a valid one-half construction;
- Blender-only software boundary.

No R5A01-R5A04 geometry, UV, material, composite texture, or Blender collection
is a construction input.

## Proposed Construction Rule

1. Start in a fresh Blender scene and rebuild only `X>=0`.
2. Build each physical component as one closed boundary volume. A visible
   location may have exactly one exterior face; coplanar facade/under-face
   pairs, projection cards, and owner-face overlays are forbidden.
3. Use source views only as boundary evidence on the single volume:
   front pixels own front-facing exterior boundaries; reversed back pixels own
   back-facing exterior boundaries; right pixels own the outward `+X` boundary;
   true axial pixels constrain the head's exposed axial boundary. These owners
   may not create additional geometry over an existing boundary.
4. Build the haft as one half-cylinder integrated into the same registered
   component frame. All source component transitions use one common world-Z
   landmark table before UV construction; independent full-height
   normalization is forbidden.
5. Use static UVs only. Separate materials may meet only at declared physical
   seams whose corresponding source landmarks have identical world-Z values.
   Source-sheet white background may not be mapped onto any exterior face.
6. Delete all center-plane closure faces from the construction half, duplicate
   by exact X mirror, and weld corresponding `X=0` vertices. The final center
   seam must have no gap, doubled face, or internal wall.
7. Do not add a hidden backing face, side card, corrective overlay, composited
   image, painted seam, averaged texture, or repair surface.

## Fail-Closed Technical Gates

Before any colored review is valid, an independent audit must prove:

- one source half exists before duplication;
- every source-half mesh component is closed except its declared X=0 weld
  boundary;
- after mirror/weld, every mesh edge has exactly two incident faces;
- zero duplicate or near-coplanar exterior faces;
- zero internal center-plane faces;
- zero self-intersection between independently owned visible surfaces;
- zero missing mirrored vertices and one registered center axis;
- one occurrence of every exterior surface;
- all shared material-boundary landmarks agree in world Z;
- zero source-background/white-line pixels inside the rendered asset silhouette;
- colored and flat-gray three-quarter proofs are materially independent.

Any failure makes the attempt `invalid` and stops production. A technical pass
does not grant visual approval.

## Proposed Review Output

- one standalone high-resolution complete colored three-quarter render showing
  the outward `+X` hammer face;
- one independent flat-gray render from the identical camera;
- front, back, left, and right source-versus-render comparisons;
- one audit manifest and one visible review board;
- stop for Flamestrike approval, revision, rejection, or blocked decision.

## Explicit Exclusions

- no reuse or repair-forward from R5 geometry, UVs, materials, or composites;
- no image generation, TRELLIS, diffusion, image-to-3D, or generated views;
- no FBX, LOD, collision, Unreal, or game-ready work;
- no technical or visual self-approval.

## Approval Gate

Flamestrike approved this exact single-closed-half recovery contract on
`2026-07-22`. Blender execution is authorized only inside the construction,
audit, review-output, and explicit-exclusion boundaries above.

## A01 Execution Outcome

- Date: `2026-07-22`.
- Status: `invalid; fail-closed topology stop; no blend, UV, material, render,
  manifest candidate, or review output created`.
- The exact source half had `1,074,899` edges with two incident faces,
  `3,198` allowed open center-plane edges, and `110` edges with four incident
  faces.
- Every four-face edge was the same single X/Z diagonal source-pixel saddle
  extruded through 110 valid right-view depth cells: grid edge `X=1 px`,
  `Z=1102 px`, or `X=0.153015302 cm`, `Z=168.622862286 cm`.
- The front-owned pixel at half-grid cell `(X=0,Z-layer=1101)` is exact object
  evidence (`RGB 212,192,169`; integer luma `195 <= 234`) but the initial
  front/back silhouette intersection excluded it. The adjacent cells then
  touched only at a corner, which is not a valid manifold solid.
- The approved contract did not state which view wins this one-pixel
  front/back topology conflict. Production stopped instead of filling,
  deleting, beveling, or remeshing the source pixels.
