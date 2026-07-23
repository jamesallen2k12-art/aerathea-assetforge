# A12 R8 Six-View Visual Reference Reset Handoff

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: `2026-07-22`
- Handoff status: `authoritative reset-safe state record`
- Current production route: `stopped in Core Recovery`
- DCC / Unreal authority: `false / false`
- Fully game-ready: `false`
- Manual recovery checkpoint: `Saved/ProjectRecovery/20260722-233320`

## Where We Left Off

Flamestrike identified that the original true axial bottom center assembly was
above/right of the approved outer center and visibly rotated. Its internal
diamonds did not align with the true axial top, and the outward hammer-face
diamonds were shown face-on in both axial views even though true `+Z/-Z`
projections should see those `+X/-X` features edge-on.

The A12 R7 Step 01 measurement candidate was therefore quarantined. Its
independent `40/40` audit remains `proof only` for deterministic replay; it did
not prove internal axial registration or projection consistency.

Flamestrike then requested a fresh image-generated six-view set with corrected
measurements. Codex used the available built-in image generator through the
imagegen skill. The requested `Sol5.6 Ultra High` model selector was not exposed
and was not falsely claimed.

Six sheets were created and opened visibly. Flamestrike responded `looks great`
and asked that the images and context be saved for a fresh start. This is
recorded as positive visual-direction feedback, not as a formal promotion to
visual canon or pixel-measurement authority.

## Saved Six-View Images

Stable local directory:
`Saved/AssetForgeResearch/SiegeBreaker/A12_R8_SixViewGeneration/VisualReference_A01/`

| View | File | SHA-256 |
|---|---|---|
| Front | `SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_FRONT_A01.png` | `9a34588afd4fef32001cd9cb2115699e7506ef1e90331c19f4d32483c60aab8c` |
| Back | `SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_BACK_A01.png` | `f09dd1ad3978f39e10ecee8ea7efa84336520f0cea4921fe3c410dfd04019694` |
| Left | `SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_LEFT_A01.png` | `7215495802065bb1907ec67f46e6f7c622b9beaf768eb710a5fc12880a6b1cc5` |
| Right | `SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_RIGHT_A01.png` | `58f3199babbcf9323751d04f0ffafa4316048243cf2f39992cdb6b04176306e8` |
| True axial top | `SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_TOP_A01.png` | `be3e0b70de7a6e4fad025315f22feb21dc948ea9c3e7efb0adb63a983f190f9c` |
| True axial bottom | `SM_DRW_SiegeBreaker_Hammer_A01_A12_R8_BOTTOM_A01.png` | `d2a32732fd480a0556e882e304bcfbff1dd82d0a913ad4c36117109406de988e` |

The generator-default copies under `/home/james/.codex/generated_images/` are
not the project recovery authority. Use the stable `Saved/AssetForgeResearch/`
copies above.

## Measurements Included In The Generation Contract

- Overall length: `170.000000 cm`.
- Head width: `75.130513051 cm`.
- Head depth: `44.299176584 cm`.
- Center core width: `34.675621408 cm`.
- Left stone width: `20.227445822 cm`.
- Right stone width: `20.227445822 cm`.
- Shaft diameter: `5 cm`.
- Grip length: `42 cm`.
- Pommel length: `18 cm`.
- Pommel maximum width: `11 cm`.
- Axial origin: `(X,Y)=(0,0)`.
- Top/bottom internal center: shared origin with zero unintended rotation.
- Outward face diamonds: face-on only in left/right views and edge-on/occluded
  in true axial views.

The old printed `52 x 32 cm` labels remain `reference only` and are not
geometry authority.

## Critical Evidence Boundary

The generated sheets render the corrected numbers and materially improve the
visual center/orientation language, but deterministic scans show that their
actual object pixels do not obey those labels:

- front/back head-width-to-length error: approximately `+30.27%/+31.96%`;
- left/right depth-to-length error: approximately `-9.66%/-12.46%`;
- top/bottom width-to-depth error: approximately `+18.78%/+24.43%`.

Two bounded front-only image-generation corrections also failed to converge.
Therefore:

- visual appearance: `reference only; positive Flamestrike feedback`;
- six-view pixel source: `invalid`;
- visual canon: `not registered`;
- geometry/DCC/UV/Unreal input: `forbidden`;
- image files: preserved unchanged and hash-locked.

Do not treat printed dimension text as proof that the rendered silhouette has
that dimension.

## Required Resume Read Order

On resume, inspect only:

1. the latest entry in `docs/projects/assetforge/RECOVERY_JOURNAL.md` and its
   snapshot;
2. `SM_DRW_SiegeBreaker_Hammer_A01_RESET_RESUME_STATE.md`;
3. `steps/A12_R6_A05_CORE_REASSESSMENT_AND_RECOVERY.md`;
4. `manifests/A12_R7_STEP01_AXIAL_INTERNAL_REGISTRATION_CONFLICT_RECOVERY.md`;
5. `manifests/A12_R8_SIX_VIEW_ORTHOGRAPHIC_GENERATION_INTERNAL_REJECTIONS.md`;
6. this handoff.

Do not inspect or reuse any old `.blend` file during the resume handshake.

## Tomorrow's Exact Opening Summary

Report to Flamestrike:

1. A05 A01-A03 remain `invalid/quarantined`.
2. R7 Step 01 is quarantined; its audit is narrow `proof only`.
3. The six A12 R8 images are safely preserved and received positive visual
   feedback.
4. They are `reference only`, not pixel authority, because their actual ratios
   do not match their printed measurements.
5. DCC, Blender, FBX, Unreal, UV, LOD, collision, and game-ready authority are
   all false.

## Next Approval Gate

The next proposed production route is one fresh, dimension-locked physical
master followed by six parallel-camera renders at one common scale. Generated
images may guide visual appearance only. Before any construction, Codex must
present a new bounded contract that declares:

- exact world frame and dimensions;
- component-local axes and ownership;
- one coherent physical volume per component;
- center/core/stone separation and zero inter-cap stone occupancy;
- strike-face plane and motif orientation;
- top/bottom center registration;
- six camera transforms and one shared orthographic scale;
- pixel audit formulas and fail-closed tolerances;
- no reuse of invalid A04/A05/R5/R6 geometry.

Flamestrike must explicitly approve or revise that contract. `Looks great`
does not authorize this construction step.

## Prohibited Resume Actions

Until the next exact contract is approved, do not:

- generate another orthographic set;
- alter, crop, warp, or overwrite the saved six images;
- convert them into pixel measurements or geometry authority;
- open or repair an old Siege Breaker blend;
- create geometry, UVs, materials, FBX, or Unreal assets;
- use TRELLIS, diffusion, image-to-3D, or any prohibited generator;
- reclassify the images as visual canon or game-ready.

## Review Command

To reopen the six saved images visibly after the resume handshake:

`eog Saved/AssetForgeResearch/SiegeBreaker/A12_R8_SixViewGeneration/VisualReference_A01/*.png`

This command is review-only and grants no production authority.
