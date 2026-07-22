# A12 Axial Pixel Reconstruction Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract ID: `SB-AXIAL-A12-RECONSTRUCTION`
- Date: `2026-07-22`
- Status: `approved for execution`
- Output ceiling: `DCC source candidate pending Flamestrike visual decision`

## Flamestrike Authority

Flamestrike approved the A11 centered-mean axial reconciliation and then said
`proceed` in direct response to the separate Blender reconstruction step.

## Source Authority

- Front source SHA-256:
  `d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95`.
- Back source SHA-256:
  `15b4633f2df4ee06115ef4a7e238f287ebece1bae514ad4005c1036a57359799`.
- Left source SHA-256:
  `1a23e0c24f7be4b12df93e2509b9d300acc9161a21a32b336f7cf63c1288d91b`.
- True axial top source SHA-256:
  `aee612d9bed74e4f861576f926fe9d75de00f80dc416e3a6ba66a75247c00e98`.
- True axial bottom source SHA-256:
  `874a9e7c7713c7edbcf1030486d3988a54e8499ee697e316ec82a013fdb9d746`.
- A11 authority manifest SHA-256:
  `46877ab4b0142d8141deb4feab234f461a31e61e118d3ce7b41e0b3679786096`.

## Locked Reconstruction Rule

1. Rebuild the proven A09 front/back/left source half fresh; do not load an old
   candidate mesh.
2. Preserve overall length `170 cm` and front-pixel width
   `75.130513051 cm`.
3. In the head interval `Z=132..170 cm`, replace the left-view depth scale with
   the approved centered top/bottom footprint:
   `1012.5 x 597 px = 75.130513051 x 44.299176584 cm`.
4. Derive the head's X-dependent front/back depth boundary by center-registering
   the exact top and bottom source masks and taking their arithmetic mean at
   each sampled X position. No hand-drawn contour or estimated envelope is
   allowed.
5. Preserve the A09 visible front/back relief and side/profile design while
   remapping head depth to the approved axial boundary. The side view does not
   control head-depth scale.
6. Build the source-visible top and bottom faces from their exact source pixels
   as closed, inward-relieved Blender surface volumes. Build only `X>=0`, then
   apply the exact Blender mirror at `X=0`.
7. Relief must remain inward from the locked envelope. No geometry may exceed
   `75.130513051 x 44.299176584 x 170 cm` except the accepted per-source axial
   residual recorded by A11.

## Proof Requirements

- completed colored front, top, bottom, and three-quarter renders;
- untextured three-quarter geometry proof;
- source-versus-candidate top and bottom comparisons;
- exact source hashes, pixel rectangles, bounds, symmetry, and software audit;
- proof that A09's hash remains unchanged;
- visible final review board.

## Prohibited Work

- image generation, generated views, TRELLIS/TRELLIS.2, or image-to-3D;
- old candidate geometry as a construction input;
- printed `52 x 32 cm` labels as geometry authority;
- independent-axis image stretching, hand-drawn masks, or estimated contours;
- LODs, collision, exports, Unreal, or `Fully game-ready` classification.

Stop after opening the final A12 review board for Flamestrike. Technical audits
cannot grant visual approval.
