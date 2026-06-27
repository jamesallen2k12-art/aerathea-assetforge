# SK_INF_Base_A01 Build And Import Status

## Current State

`SK_INF_Base_A01` has a first-pass deterministic DCC blockout, FBX export set, Unreal skeletal imports, material instances, generated physics assets, generated animation Blueprint placeholders, LOD0-LOD3, review sockets, and startup-scene placement.

The first-pass scale/silhouette review was approved by Flamestrike on 2026-06-27. This approves the compact/tall adult blockout targets for continued production planning; it is not final sculpted or hand-painted character art approval.

## DCC Source

- Build script: `Tools/DCC/build_infernal_base.py`
- Blender source: `SourceAssets/Blender/Characters/Infernals/SK_INF_Base_A01/SK_INF_Base_A01.blend`
- DCC review image: `Saved/Automation/InfernalBaseReview/SK_INF_Lifecycle_A01_DCCReview.png`

## FBX Exports

- `SourceAssets/Exports/Characters/Infernals/SK_INF_Base_A01/SK_INF_Base_Compact_A01.fbx`
- `SourceAssets/Exports/Characters/Infernals/SK_INF_Base_A01/SK_INF_Base_Tall_A01.fbx`

## Unreal Assets

Unreal folder: `/Game/Aerathea/Characters/Infernals/Base/`

- `SK_INF_Base_Compact_A01`
- `SK_INF_Base_Compact_A01_Skeleton`
- `PHYS_INF_Base_Compact_A01`
- `ABP_INF_Base_Compact_A01`
- `SK_INF_Base_Tall_A01`
- `SK_INF_Base_Tall_A01_Skeleton`
- `PHYS_INF_Base_Tall_A01`
- `ABP_INF_Base_Tall_A01`

## Materials

Base materials:

- `M_INF_Skin_Blockout_A01`
- `M_INF_HornClaw_Blockout_A01`
- `M_INF_Wing_Blockout_A01`
- `M_INF_Wrap_Blockout_A01`
- `M_INF_BrandGlow_Blockout_A01`
- `M_INF_ElderAsh_Blockout_A01`
- `M_INF_ReviewScale_Humanoid_A01`
- `M_INF_ReviewScale_MaxAdult_A01`

Material instances were generated per imported mesh under `/Game/Aerathea/Materials/Instances/`.

## Review Actors

Startup map: `/Game/Aerathea/Maps/L_Aerathea_Startup`

- `AET_PROD_InfernalBaseCompact_A01`
- `AET_PROD_InfernalBaseTall_A01`
- `AET_PROD_InfernalScale_Humanoid180_A01`
- `AET_PROD_InfernalScale_MaxAdult274_A01`

Review capture:

- `Saved/Automation/StartupReview/AeratheaStartupReview_InfernalScale_A01.png`

## Generated Runtime Support

- LODs: LOD0-LOD3 generated for both adult review meshes.
- Physics: first-pass generated physics assets assigned to both meshes.
- Animation: placeholder animation Blueprints created for both meshes.
- Sockets:
  - `hand_l_claw`
  - `hand_r_claw`
  - `claw_l`
  - `claw_r`
  - `tail_tip`
  - `wing_l_tip`
  - `wing_r_tip`
  - `vfx_eye_l`
  - `vfx_eye_r`
  - `vfx_brand_chest`
  - `vfx_mouth`
  - `vfx_regen_core`

## Verification

- Blender DCC generation completed for adult and Lesser Infernal review meshes.
- Unreal import completed for compact and tall adult review meshes.
- Offscreen Unreal review capture completed and approved at `Saved/Automation/StartupReview/AeratheaStartupReview_InfernalScale_A01.png`.
- Startup scene validation passed after overview-camera restore: 63 assets, 34 expected actors, and 25 ground tiles.
- Rerun `Tools/Unreal/validate_startup_scene.py` after any further map, import, or camera edits.

## Remaining Work

- Replace blockout geometry with approved sculpt/retopo.
- Author final UVs and texture sets.
- Tune physics bodies for tail and wings.
- Build real class animation sets for warrior, rogue, hunter, and mage variants.
- Decide final sex/body-type split within the 5'0"-9'0" adult range.
