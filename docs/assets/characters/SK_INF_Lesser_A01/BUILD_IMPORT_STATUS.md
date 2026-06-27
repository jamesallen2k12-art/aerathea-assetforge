# SK_INF_Lesser_A01 Build And Import Status

## Current State

`SK_INF_Lesser_A01` has a first-pass deterministic DCC lifecycle blockout, FBX export set, Unreal skeletal imports, material instances, generated physics assets, generated animation Blueprint placeholders, LOD0-LOD3, review sockets, and startup-scene placement.

The first-pass scale/lifecycle silhouette review was approved by Flamestrike on 2026-06-27. This approves the stage lineup for continued production planning: Spawn, 1st Kill, Blooded, Elder, and Ancient. It is not final sculpted or hand-painted character art approval.

## DCC Source

- Build script: `Tools/DCC/build_infernal_base.py`
- Blender source: `SourceAssets/Blender/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_A01.blend`
- DCC review image: `Saved/Automation/InfernalBaseReview/SK_INF_Lifecycle_A01_DCCReview.png`

## FBX Exports

- `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_Spawn_A01.fbx`
- `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_1stKill_A01.fbx`
- `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_Blooded_A01.fbx`
- `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_Elder_A01.fbx`
- `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_Ancient_A01.fbx`

## Unreal Assets

Unreal folder: `/Game/Aerathea/Characters/Infernals/Lesser/`

- `SK_INF_Lesser_Spawn_A01`
- `SK_INF_Lesser_Spawn_A01_Skeleton`
- `PHYS_INF_Lesser_Spawn_A01`
- `ABP_INF_Lesser_Spawn_A01`
- `SK_INF_Lesser_1stKill_A01`
- `SK_INF_Lesser_1stKill_A01_Skeleton`
- `PHYS_INF_Lesser_1stKill_A01`
- `ABP_INF_Lesser_1stKill_A01`
- `SK_INF_Lesser_Blooded_A01`
- `SK_INF_Lesser_Blooded_A01_Skeleton`
- `PHYS_INF_Lesser_Blooded_A01`
- `ABP_INF_Lesser_Blooded_A01`
- `SK_INF_Lesser_Elder_A01`
- `SK_INF_Lesser_Elder_A01_Skeleton`
- `PHYS_INF_Lesser_Elder_A01`
- `ABP_INF_Lesser_Elder_A01`
- `SK_INF_Lesser_Ancient_A01`
- `SK_INF_Lesser_Ancient_A01_Skeleton`
- `PHYS_INF_Lesser_Ancient_A01`
- `ABP_INF_Lesser_Ancient_A01`

## Materials

Base materials:

- `M_INF_Skin_Blockout_A01`
- `M_INF_HornClaw_Blockout_A01`
- `M_INF_Wing_Blockout_A01`
- `M_INF_Wrap_Blockout_A01`
- `M_INF_BrandGlow_Blockout_A01`
- `M_INF_ElderAsh_Blockout_A01`

Material instances were generated per imported mesh under `/Game/Aerathea/Materials/Instances/`.

## Review Actors

Startup map: `/Game/Aerathea/Maps/L_Aerathea_Startup`

- `AET_PROD_InfernalLesserSpawn_A01`
- `AET_PROD_InfernalLesser1stKill_A01`
- `AET_PROD_InfernalLesserBlooded_A01`
- `AET_PROD_InfernalLesserElder_A01`
- `AET_PROD_InfernalLesserAncient_A01`

Review capture:

- `Saved/Automation/StartupReview/AeratheaStartupReview_InfernalScale_A01.png`

## Generated Runtime Support

- LODs: LOD0-LOD3 generated for all five lifecycle meshes.
- Physics: first-pass generated physics assets assigned to all five meshes.
- Animation: placeholder animation Blueprints created for all five meshes.
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

- Blender DCC generation completed for Lesser lifecycle and adult Infernal review meshes.
- Unreal import completed for all five Lesser lifecycle meshes.
- Offscreen Unreal review capture completed and approved at `Saved/Automation/StartupReview/AeratheaStartupReview_InfernalScale_A01.png`.
- Startup scene validation passed after overview-camera restore: 63 assets, 34 expected actors, and 25 ground tiles.
- Rerun `Tools/Unreal/validate_startup_scene.py` after any further map, import, or camera edits.

## Remaining Work

- Lock final stage proportions after visual review.
- Replace blockout geometry with approved sculpt/retopo.
- Author final UVs and texture sets.
- Tune per-stage physics bodies and movement capsules.
- Build real stage animation sets for Spawn, 1st Kill, Blooded, Elder, and Ancient behavior.
