# A12 R3 Component-Separation Correction Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Parent contract: `SB-AXIAL-A12-RECONSTRUCTION`
- Correction ID: `SB-AXIAL-A12-R3-COMPONENT-SEPARATION`
- Date: `2026-07-22`
- Status: `approved for execution by Flamestrike`
- Output ceiling: `DCC source candidate pending Flamestrike visual decision`

## Approval

After reviewing the exact-rule R2 render, Flamestrike identified false stone
between the two strike halves and the centered shaft mount. Flamestrike agreed
that the stone must be removed from the center, approved separate stone/core
ownership, and said `proceed`.

## Evidence-Bound Correction

1. Preserve the A09 front/back/left source pixels, A11 top/bottom pixel scale,
   overall `170 cm` length, `75.130513051 cm` width, and exact X=0 mirror.
2. Replace the monolithic head treatment with:
   - one source-built X-positive stone region mirrored to create the two strike
     stones;
   - one centered source-built core/shaft region mirrored at X=0.
3. Use the existing component authority ratio `24:14:14` for
   core:left-stone:right-stone, but apply it to the approved pixel width rather
   than the rejected printed `52 cm` absolute width:
   - centered core width: `75.130513051 * 24/52 = 34.675621408 cm`;
   - each stone width: `75.130513051 * 14/52 = 20.227445822 cm`;
   - core/stone boundaries: `X=+/-17.337810704 cm`.
4. Apply the A11 X-dependent centered-mean depth boundary only to the two stone
   regions and across each stone's complete source-visible front silhouette.
   Do not cut the stones at the declared `Z=132 cm` shaft station.
5. Preserve the centered core and shaft depth from the proven A09 source build.
   Top/bottom source materials may own visible core boundary faces, but their
   flat projection objects remain `proof only` and hidden from completed views.
6. No global `Z=132..138 cm` transition blend is authorized or used.

## Proof Gate

- completed front and three-quarter colored renders;
- untextured three-quarter geometry proof;
- exact top/bottom head-isolated source comparisons;
- component counts, bounds, mirror symmetry, hashes, and A09 immutability;
- no rock-filled central bridge or horizontal R2 ledge;
- visible review board opened only after internal and technical checks pass.

No image generation, TRELLIS, export, LOD, collision, or Unreal work is
authorized.
