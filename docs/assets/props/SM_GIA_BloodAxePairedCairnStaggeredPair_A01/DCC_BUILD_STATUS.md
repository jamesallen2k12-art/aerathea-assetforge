# SM_GIA_BloodAxePairedCairnStaggeredPair_A01 DCC Build Status

Status: `Unreal import candidate`.

Built on 2026-07-03 by `Tools/DCC/build_bloodaxe_cairn_variant_batch.py` as part of `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/DCC_BATCH_STATUS.md`.
Source status remains `DCC game-ready candidate`; Unreal import and validation are recorded in `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/UNREAL_IMPORT_STATUS.md`.

## Outputs

- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnStaggeredPair_A01/SM_GIA_BloodAxePairedCairnStaggeredPair_A01.blend`
- FBX exports: `SourceAssets/Exports/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnStaggeredPair_A01/`
- Proof render: `Saved/Automation/DCC/BloodAxeCairnVariants_A01/SM_GIA_BloodAxePairedCairnStaggeredPair_A01/SM_GIA_BloodAxePairedCairnStaggeredPair_A01_DCCReview.png`

The export folder contains the main FBX, visual-only Unreal import FBX, plus LOD0, LOD1, LOD2, and LOD3 FBXs.

The main FBX and LOD0 FBX include broad UCX-style collision proxies for DCC audit, while Unreal uses the visual-only `*_UnrealImport.fbx` plus scripted broad simple collision fallback. See `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/DCC_GAME_READY_PREP_STATUS.md`, `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/UNREAL_IMPORT_TASK_PACKET.md`, and `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/UNREAL_IMPORT_STATUS.md`.

## Boundary

This is an `Unreal import candidate`. It is not `Fully game-ready`.

## Still Blocked

Final hand-painted textures, final material polish, startup/gameplay placement, final visual approval, route scripting, encounter behavior, lane behavior, and pathfinding behavior remain blocked.
