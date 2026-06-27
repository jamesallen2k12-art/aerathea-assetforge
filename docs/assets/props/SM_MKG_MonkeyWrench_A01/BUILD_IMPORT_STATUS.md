# SM_MKG_MonkeyWrench_A01 Build And Import Status

## Current Result

- Build/import status: Blender source generated, FBX exported, imported to Unreal, material instances assigned, generated LOD0-LOD3, and placed in the startup review scene
- Source mesh status: first-pass DCC review source generated from the approved production package
- Unreal placement status: `AET_PROD_MKG_MonkeyWrench_A01` exists in `L_Aerathea_Startup`
- Validation: `Tools/Unreal/validate_startup_scene.py` passes through `UnrealEditor-Cmd`; `Tools/Unreal/validate_review_alignment_markers.py` also passes after the overview camera restoration

## Completed Prerequisites

- Production package:
  - `docs/assets/props/SM_MKG_MonkeyWrench_A01/PRODUCTION_PACKAGE.md`
- Modeling handoff:
  - `docs/assets/props/SM_MKG_MonkeyWrench_A01/MODELING_HANDOFF.md`
- Blender source/export:
  - `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_MonkeyWrench_A01/SM_MKG_MonkeyWrench_A01.blend`
  - `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_MonkeyWrench_A01/SM_MKG_MonkeyWrench_A01.fbx`
- Unreal asset:
  - `/Game/Aerathea/Weapons/Mekgineer/SM_MKG_MonkeyWrench_A01`

## Remaining To Finalize

1. Replace first-pass blockout forms with approved art-model geometry.
2. Create final UVs and `BC/N/ORM/E` texture set.
3. Inspect and tune generated LOD0-LOD3 against the final art model.
4. Confirm grip pivot and `hand_r_weapon` fit against `SK_GNM_Base_A01`.
5. Tune pickup/display collision and keep equipped collision disabled.
6. Confirm final material-slot budget after texture authoring.

## Acceptance Gate

The Monkey Wrench is imported for startup validation and production review. Do not mark it final until art review, UVs, textures, tuned LODs, socket inspection, and collision review are complete.
