# A12 R3 Component-Separation Output Record

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract: `SB-AXIAL-A12-RECONSTRUCTION`
- Correction: `SB-AXIAL-A12-R3-COMPONENT-SEPARATION`
- Date: `2026-07-22`
- Artifact status: `DCC source candidate pending Flamestrike visual decision`
- Unreal authority: `false`
- Fully game-ready: `false`

## Result

The R3 rebuild replaces the invalid monolithic head-depth application with two
source-built candidate components:

1. centered metal core and complete shaft;
2. one X-positive stone region mirrored at X=0 to create the two strike stones.

The component boundary uses the approved pixel width and the recorded
`24:14:14` core/stone/stone ratio:

- core width: `34.675621408 cm`;
- each stone width: `20.227445822 cm`;
- measured Blender split edge: `X=+/-17.367237091 cm`, within one front-source
  pixel of the exact ratio boundary `X=+/-17.337810704 cm`.

The A11 centered-mean depth is applied across the complete source-visible stone
silhouettes. The centered core/shaft retains the proven A09 depth. No global
`Z=132..138 cm` blend is used.

## Technical Evidence

- candidate objects: `2`;
- vertices: `436670`;
- polygons: `436664`;
- evaluated bounds:
  `75.130516052 x 44.299175262 x 170.000000000 cm`;
- missing mirrored vertices: `0` for both candidate components;
- A09 hash after build:
  `06ffb121d00cddb7b9e30a60067a5036a851d285f15daca3bffe3a663fd6d78f`
  (`unchanged`);
- independent audit: `pass 25/25`;
- image generation: `false`;
- TRELLIS/image-to-3D: `false`;
- Unreal/export/LOD/collision work: `false`.

## Visual Gate

Internal review confirms that the R2 horizontal ledge is absent and the
untextured proof now reads as two mirrored outer stones around one centered
core/shaft. Technical evidence cannot grant visual approval. The exact R3
review board is pending Flamestrike's decision.

## Hash Locks

- builder:
  `097431d756c23d5bda39f0d63d61730e896c568ec957e884a1aa2238b674db80`;
- independent auditor:
  `c6ecaad7a195d91fd5f3e2ae6950fdb5bb694f4ea0b9d640f9dce608ee6033fa`;
- correction contract:
  `353fa042f87997f9d4642e35da24c93638b2c101707e449d0c8b2a7af917f301`;
- local Blender candidate:
  `7490516c746646d095af970836b75283048a3b7dce19d7c262ac8f2a3a7bc706`;
- review board:
  `621c361e809d11d775c3aa7aca476fdad4c3962cd76997cf763d0edb4d1ad5c6`;
- validation:
  `bf4009a7dde2a191d816a4b83a28fa496fc8535b8a0adc8d5607a37ee08fa1d5`;
- independent audit:
  `5d1a85110e38c1dd47b177793aa38d4bf010847ae1191d88f7041cfd15a5e6f2`.

## Decision Required

Flamestrike must classify the exact visible R3 candidate as `approved`,
`revise`, `rejected`, or `blocked`. Approval would apply only to this reviewed
DCC source appearance and component correction, not game-ready escalation.
