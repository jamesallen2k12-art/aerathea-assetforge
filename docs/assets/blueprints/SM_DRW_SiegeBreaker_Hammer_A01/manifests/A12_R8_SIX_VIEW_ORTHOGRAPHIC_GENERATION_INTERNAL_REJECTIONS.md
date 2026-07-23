# A12 R8 Six-View Orthographic Generation Internal Rejections

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: `2026-07-22`
- User authority: redraw front, back, left, right, true axial top, and true
  axial bottom with corrected measurements and present them for approval
- Generator: `Codex built-in image generation through the imagegen skill`
- Requested model label: `Sol5.6 Ultra High`
- Model-selection result: `not exposed by the available generator; no false
  model claim made`
- Artifact status: `quarantined internal rejection; reference only`
- DCC / Unreal authority: `false / false`

## Approved Input Measurements Used In Every Prompt

- Overall longitudinal length: `170.000000 cm`.
- Head width: `75.130513051 cm`.
- Head depth: `44.299176584 cm`.
- Center core width: `34.675621408 cm`.
- Left stone width: `20.227445822 cm`.
- Right stone width: `20.227445822 cm`.
- Shaft diameter: `5 cm`.
- Grip length: `42 cm`.
- Pommel length: `18 cm`.
- Pommel maximum width: `11 cm`.
- Axial structural origin: `(X,Y)=(0,0)` with no unintended center-section
  translation or rotation.
- Outward `+X/-X` face diamonds: face-on only in left/right projections and
  edge-on or occluded in true `+Z/-Z` projections.

The obsolete printed `52 x 32 cm` labels were explicitly forbidden as
proportion authority.

## Preserved Local Outputs

Directory:
`Saved/AssetForgeResearch/SiegeBreaker/A12_R8_SixViewGeneration/InternalRejected_A01/`

- FRONT SHA `9a34588afd4fef32001cd9cb2115699e7506ef1e90331c19f4d32483c60aab8c`.
- BACK SHA `f09dd1ad3978f39e10ecee8ea7efa84336520f0cea4921fe3c410dfd04019694`.
- LEFT SHA `7215495802065bb1907ec67f46e6f7c622b9beaf768eb710a5fc12880a6b1cc5`.
- RIGHT SHA `58f3199babbcf9323751d04f0ffafa4316048243cf2f39992cdb6b04176306e8`.
- TOP SHA `be3e0b70de7a6e4fad025315f22feb21dc948ea9c3e7efb0adb63a983f190f9c`.
- BOTTOM SHA `d2a32732fd480a0556e882e304bcfbff1dd82d0a913ad4c36117109406de988e`.

Two targeted FRONT correction attempts are preserved beside the set. They are
also `quarantined` and demonstrate non-convergent prompt-only dimension control.

## Internal Technical Rejection

The generator rendered the requested dimension text correctly and materially
improved the axial center/orientation language, but the visible object pixels
do not obey those labels. Greatest non-edge object scans and direct visual
extent checks produced these consequences:

| View | Required ratio | Observed ratio | Relative error |
|---|---:|---:|---:|
| Front head width / full length | `0.441944194` | `0.575729069` | `+30.27%` |
| Back head width / full length | `0.441944194` | `0.583175803` | `+31.96%` |
| Left depth / full length | `0.260583392` | `0.235401460` | `-9.66%` |
| Right depth / full length | `0.260583392` | `0.228102190` | `-12.46%` |
| Top width / depth | `1.695979900` | `2.014492754` | `+18.78%` |
| Bottom width / depth | `1.695979900` | `2.110389610` | `+24.43%` |

The left/right depth silhouettes also disagree, and the top/bottom depth
silhouettes do not share one footprint. Therefore the six images cannot be
used for accurate pixel math even though their printed numbers are correct.

The first targeted FRONT edit changed the observed head-width/full-length ratio
from `0.575729069` to `0.396363636`, overshooting the requested correction. A
second exact-pixel retry changed it to approximately `0.538244`, moving away
again. This proves that prompt-only numeric correction is not deterministic
enough for the requested authority.

## Classification

- Visual style and material exploration: `reference only; positive Flamestrike
  feedback ("looks great")`.
- Six-view orthographic production set: `invalid`.
- Pixel-measurement source: `invalid`.
- Geometry, UV, DCC, or Unreal input: `forbidden`.
- Visible image-viewer gallery: `quarantined review support only`; it is not an
  approval candidate.

The exact six image hashes were copied unchanged to the stable recovery path
`Saved/AssetForgeResearch/SiegeBreaker/A12_R8_SixViewGeneration/VisualReference_A01/`
at Flamestrike's request. The positive feedback does not supersede the ratio
failures or promote the set to visual canon.

## Stop Gate

Do not iterate prompt-only orthographics or repair these images forward. Exact
six-view pixel authority requires one dimension-locked physical master, then
six parallel-camera renders at one common scale. A new Blender/DCC recovery
contract is required before constructing that master. Image generation may
remain a visual-style reference input only.
