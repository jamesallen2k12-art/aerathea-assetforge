# SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial

## Status

Final-trial game-ready candidate generated from A01. Technical Unreal validation passed; final aesthetic approval remains with Flamestrike.

## Source

- Visual canon source: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- Method: hand-authored 360 DCC reconstruction with A01 front projection guidance and inferred side/back forms.

## Outputs

- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial.blend`
- FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial.fbx`
- LOD FBXs: `_LOD0`, `_LOD1`, `_LOD2`, `_LOD3`
- Textures: 18 PNG source textures under `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial/`
- Unreal mesh: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial`
- Startup review actor: `AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial`

## DCC Build Summary

- LOD0: 5,178 tris
- LOD1: 2,808 tris
- LOD2: 1,190 tris
- LOD3: 704 tris
- DCC bounds: 381.44w x 227.02d x 187.42h cm
- Collision proxies: 1 broad simple static-prop proxy

## Unreal Validation

Focused validator:

`Tools/Unreal/validate_bloodaxe_cairn_final_trial.py`

Result:

`Blood Axe final-trial cairn validation passed: 176.97h x 380.31w x 227.02d cm, 4 LODs, 6 materials, 18 textures, startup actor AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial, broad collision enabled.`

## Review Evidence

- DCC review board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial/SM_GIA_BloodAxeCairnSlabCluster_A01_FinalTrial_FinalGameReadyReviewBoard.png`
- Unreal startup capture path: `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeCairn_FinalTrial.png`

Note: the generic startup capture camera is not a reliable final visual approval shot for this specific asset because the startup review lineup still contains older cairn review actors. Use the DCC multi-angle review board for visual approval and the focused Unreal validator for engine-readiness proof.
