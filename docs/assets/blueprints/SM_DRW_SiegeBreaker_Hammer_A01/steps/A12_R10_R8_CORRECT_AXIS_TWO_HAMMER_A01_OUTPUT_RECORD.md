# A12 R10 R8 Correct-Axis Two-Hammer A01 Output Record

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract:
  `SB-A12-R10-R8-CORRECT-AXIS-TWO-HAMMER-A01`
- Artifact status:
  `two DCC source candidates pending Flamestrike comparison`
- Production decision:
  `BLOCKED pending Flamestrike selection / revision / rejection`

## Result

Two fresh complete hammers were reconstructed from the new R8 scanline
evidence. They differ only in which exact half of the right-view image owns
the source depth profile:

1. Rune-side half: `[557,668)`.
2. Metal-center-piece half: `[418,557)`.

Each source half maps to `Y<=0` and is completed exactly once with:

`Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)`.

This corrects the rejected front-image-X duplication. No rejected geometry
was reused.

Both candidates use the approved new envelope:

`97.873941674506 x 47.479915237376 x 170 cm`.

Their saved floating-point Blender bounds are:

`97.87393951416016 x 47.479915618896484 x 170.0 cm`.

## Corrected Handle

The handle now begins at `A`, including the upper coupler, at:

`Z=132 cm`.

The rejected candidate stopped at `C` and omitted:

`33432/1111 = 30.091809180918 cm`.

The corrected handle uses:

- true straight haft radius: `2.5 cm`;
- cylinder map: `theta(U)=-pi/2+pi*U`;
- surface map:
  `X=r(z)cos(theta)`, `Y=r(z)sin(theta)`;
- exact flat-diameter-to-half-circumference factor: `pi/2`;
- grip `H8..U1`: `42 cm`;
- pommel `U3..terminal`: `18 cm`;
- lower maximum diameter: `11 cm`.

The longitudinal profile was recomputed from the new front-image stations
`A`, `C`, `H1`, `H8`, `U1`, `U3`, `L4`, and terminal. The independent audit
recomputed these stations from their exact fractions.

## Technical Evidence

### Rune-side candidate

- Builder gates: `26/26 PASS`.
- Independent saved-file audit: `52/52 PASS`.
- Complete vertices: `265648`.
- Complete polygons: `265772`.
- Exact Rz180 vertex symmetry: `PASS`.
- Handle station/formula replay: `PASS`.

### Metal-center-piece candidate

- Builder gates: `26/26 PASS`.
- Independent saved-file audit: `52/52 PASS`.
- Complete vertices: `284310`.
- Complete polygons: `284434`.
- Exact Rz180 vertex symmetry: `PASS`.
- Handle station/formula replay: `PASS`.

The final visual rejection check found no wrong-axis duplication, incomplete
half, clipped review view, gray/color duplication, or obvious handle-scale
departure from the declared physical locks.

Technical checks do not grant visual approval.

## Outputs

### Rune-side candidate

- Blender:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8CorrectAxisRuneSide_A01/SM_DRW_SiegeBreaker_Hammer_A01_A12_R10_R8CorrectAxisRuneSide_A01.blend`
- Validation:
  `manifests/A12_R10_R8_CORRECT_AXIS_RUNE_SIDE_A01_VALIDATION.json`
- Independent audit:
  `manifests/A12_R10_R8_CORRECT_AXIS_RUNE_SIDE_A01_INDEPENDENT_AUDIT.json`

### Metal-center-piece candidate

- Blender:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8CorrectAxisMetalCenter_A01/SM_DRW_SiegeBreaker_Hammer_A01_A12_R10_R8CorrectAxisMetalCenter_A01.blend`
- Validation:
  `manifests/A12_R10_R8_CORRECT_AXIS_METAL_CENTER_A01_VALIDATION.json`
- Independent audit:
  `manifests/A12_R10_R8_CORRECT_AXIS_METAL_CENTER_A01_INDEPENDENT_AUDIT.json`

### Shared review

- Comparison board:
  `review/A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01/A12_R10_R8_CORRECT_AXIS_TWO_HAMMER_A01_REVIEW.png`

## Output Hashes

- Comparison board:
  `ae3dbabae8976f52f7ceae3d2f86cc288687608b0a457a47ba41d3441d87bf46`
- Rune Blender:
  `1b272d83269c1d4aac167d95ce5cfeb70766c301d7ae1eb7b7a045c4d441a752`
- Rune validation:
  `bd8a8d77ccaba528e49f9dac96900807acf0de9e62356d42b151fc06f9267bd5`
- Rune audit:
  `ee412d5fd0ed52b22e86e18ac66fc9b609fa59ead33a675b03395e93c9525e9a`
- Metal Blender:
  `36a0ca2e875668bdb21590d3ad9eab54134b735b20e6f9227e34a89bddf6c1a9`
- Metal validation:
  `7660ceb9effe5230789742c13ff223056f5712c94ff62aea8b15d11e30402a59`
- Metal audit:
  `b7238958f81e79466a7e3e5c06e17312d48d4bf1d21bbc65460c7a0c391387b4`

## Decision Gate

Flamestrike may now compare:

- Hammer A: rune-side half rotated to whole;
- Hammer B: metal-center-piece half rotated to whole.

The next decision is:

`select Hammer A / select Hammer B / revise / reject / blocked`.

FBX, Unreal, LOD, collision, material-production, and fully game-ready
authority remain false.
