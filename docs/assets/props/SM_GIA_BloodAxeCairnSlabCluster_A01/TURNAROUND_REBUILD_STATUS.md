# SM_GIA_BloodAxeCairnSlabCluster_A01 Turnaround Rebuild Status

## Status

Created a turnaround-guided DCC candidate package after the front-only projection attempt was rejected as insufficiently close to the approved concept language.

This pass uses the approved A1 multi-angle turnaround draft as the rebuild guide. It is a real static-mesh candidate with Blender source, FBX export, LOD0-LOD3 exports, review renders, guide-point render, and a UCX-style collision proxy in the main FBX.

This is not final visual canon and is not Unreal-imported yet. Flamestrike aesthetic approval is required before this candidate should replace the prior faithful/front-projection attempts or be imported for gameplay review.

## Source Reference

- Original A1 crop: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- Approved turnaround rebuild guide: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_TurnaroundDraft_A01.png`
- Review comparison board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild_ConceptVsDCCReview.png`

## Outputs

- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_turnaround_rebuild.py`
- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild.blend`
- Main FBX with collision proxy: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild.fbx`
- LOD0 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild_LOD0.fbx`
- LOD1 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild_LOD1.fbx`
- LOD2 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild_LOD2.fbx`
- LOD3 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild_LOD3.fbx`
- Review renders: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild/`

## Build Metrics

- LOD0: 3430 triangles.
- LOD1: 2130 triangles.
- LOD2: 1008 triangles.
- LOD3: 456 triangles.
- LOD0 bounds: 381.44 cm wide x 227.02 cm deep x 174.66 cm high.
- Collision proxy source: 1 UCX-style hull in the main FBX.
- Material slots: stone, dark stone, ash/mud, oxide paint, rawhide, highlight/crack detail, guide/collision review materials.

## Production Notes

- The corrected process is multi-view: A1 was redrawn as a turnaround, then DCC geometry was rebuilt from shared landmark points rather than from a single front projection.
- Main readable forms are real geometry: central fallen slab, rear standing slab, right upright, left stone stack, support stones, ground base, pebble scatter, lashings, and red Blood Axe paint.
- Small chips, cracks, hand-painted stone color variation, dirt, rope fibers, and final side/back polish remain paint/material work.
- Current DCC candidate is production-valid as a lightweight static mesh proof, but it still reads more blockout-like than the approved concept sheet.

## Approval Boundary

Flamestrike approval is required for:

- whether the DCC candidate is close enough to continue into Unreal import;
- whether the stone geometry needs another Blender art pass before import;
- whether the final paint should be authored in Blender/ArmorPaint before Unreal review;
- whether this A1 turnaround guide should become final visual canon for this prop family.
