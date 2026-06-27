# SM_MKG_ToolPack_A01 Build And Import Status

## Current Result

- Build/import status: Blender source generated, FBX exported, imported to Unreal, material instances assigned, generated LOD0-LOD3, and preview-fit to the gnome `back_pack` socket in the startup review scene
- Source mesh status: first-pass DCC review source generated from the approved production package
- Unreal placement status: `AET_PROD_MKG_ToolPack_BackFit_A01` exists in `L_Aerathea_Startup` as a socket-fit preview on `AET_PROD_GnomeBase_A01`
- Validation: `Tools/Unreal/validate_startup_scene.py` passes through `UnrealEditor-Cmd` and verifies the preview actor is within 2 cm of the `back_pack` socket

## Completed Prerequisites

- Production package:
  - `docs/assets/props/SM_MKG_ToolPack_A01/PRODUCTION_PACKAGE.md`
- Modeling handoff:
  - `docs/assets/props/SM_MKG_ToolPack_A01/MODELING_HANDOFF.md`
- Blender source/export:
  - `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_ToolPack_A01/SM_MKG_ToolPack_A01.blend`
  - `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_ToolPack_A01/SM_MKG_ToolPack_A01.fbx`
- Unreal asset:
  - `/Game/Aerathea/Props/Mekgineer/Armory/SM_MKG_ToolPack_A01`

## Remaining To Finalize

1. Inspect the ToolPack on `SK_GNM_Base_A01` in the GUI startup scene and approve or adjust scale/offset.
2. Replace first-pass blockout forms with approved art-model geometry.
3. Create final UVs and `BC/N/ORM/E` texture set.
4. Inspect and tune generated LOD0-LOD3 against the final art model.
5. Tune world-display collision and confirm equipped collision remains disabled.
6. Confirm final attachment rules after gnome body proportions and starter outfit are approved.

## Acceptance Gate

The ToolPack is imported for startup validation and gnome back-slot review. Do not mark it final until GUI art review, scale/offset approval, UVs, textures, tuned LODs, and equipped collision rules are complete.
