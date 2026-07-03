# SM_GIA_BloodAxeCairnSlabCluster_A01_Complete Status

Status: rejected by Flamestrike for visual/art-match quality.

This static-prop candidate is technically packaged and validated, but it failed the subjective art gate. It should not be treated as canon, final art, or the approved Blood Axe cairn visual target. The rejection reason is not Unreal implementation; it is that the mesh, silhouette, material read, and paint placement do not match the approved A1 concept closely enough.

Keep this branch only as a negative comparison and technical packaging reference.

## Asset Paths

- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Complete/SM_GIA_BloodAxeCairnSlabCluster_A01_Complete.blend`
- FBX and LOD exports: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Complete/`
- Texture sources: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Complete/`
- Unreal mesh: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Complete`
- Startup review actor: `AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_Complete`

## Review Captures

- DCC turntable: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_Complete/SM_GIA_BloodAxeCairnSlabCluster_A01_Complete_CompleteTurntableReview.png`
- Unreal game-ready review: `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeCairnComplete_A01_GameReadyReview.png`

## Implementation Summary

- Asset type: Static Mesh
- Material slots: 4, stone, earth ash, rawhide, Blood Axe red paint
- Texture maps: 12, with Base Color, Normal, and ORM sets for each material family
- LODs: LOD0, LOD1, LOD2, LOD3
- DCC triangle counts: LOD0 1184 tris, LOD1 744 tris, LOD2 392 tris, LOD3 392 tris
- Unreal measured bounds: 162.36 cm high x 402.18 cm wide x 271.80 cm deep
- Collision: broad simple static prop collision
- Gameplay role: non-interactive Blood Axe environmental storytelling prop

## Validation Evidence

Focused validator:

`Tools/Unreal/validate_bloodaxe_cairn_complete.py`

Latest pass summary:

`Blood Axe complete cairn validation passed: 162.36h x 402.18w x 271.80d cm, 4 LODs, 4 materials, 12 textures, startup actor AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_Complete, broad collision enabled.`

## Remaining Approval Gate

- Do not use this candidate as canon.
- Do not scale this method into additional concept-faithful assets.
- Continue from `RECONSTRUCTION_FINDINGS.md` before attempting another game-ready pass.
