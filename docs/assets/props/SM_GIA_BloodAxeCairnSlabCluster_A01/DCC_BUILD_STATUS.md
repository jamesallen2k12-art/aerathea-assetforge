# SM_GIA_BloodAxeCairnSlabCluster_A01 DCC Build Status

## Status

Built as a Blender art-match source pass and waiting for Flamestrike aesthetic approval of the painted result.

This is structurally ready for paint handoff review: mesh source, LOD sources, FBX handoffs, starter BC/N/ORM texture map outputs, painted preview BC/N/ORM maps, ArmorPaint handoff files, and a collision proxy source exist. It is not approved final canon, final hand-painted art, Unreal implementation, gameplay placement, optimized material consolidation, or collision correctness.

## Source Reference

- Visual board: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_CandidateBoard.png`
- Selected POC crop: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- Candidate status: `A1` is the proof target only. It is not canon-locked until Flamestrike approves it.

## Outputs

- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01.blend`
- Main FBX export with collision: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01.fbx`
- LOD0 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01_LOD0.fbx`
- LOD1 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01_LOD1.fbx`
- LOD2 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01_LOD2.fbx`
- LOD3 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01_LOD3.fbx`
- Base color map: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/T_GIA_BloodAxeCairnSlabCluster_A01_BC.png`
- Normal map: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/T_GIA_BloodAxeCairnSlabCluster_A01_N.png`
- ORM map: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/T_GIA_BloodAxeCairnSlabCluster_A01_ORM.png`
- ArmorPaint handoff folder: `SourceAssets/ArmorPaint/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- ArmorPaint launcher: `Tools/DCC/launch_armorpaint_cairn_A01.sh`
- Painted approval render: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01_PaintedApprovalReview.png`
- DCC proof render: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01_DCCReview.png`
- Game-ready review render: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReadyReview.png`
- Reproducible builder: `Tools/DCC/build_bloodaxe_cairn_slab_cluster_poc.py`

## Faithful Game-Ready Candidate

Follow-up candidate `SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady` exists as the current concept-projection game-ready pass.

- Status doc: `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/GAME_READY_FAITHFUL_STATUS.md`
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_game_ready.py`
- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady.blend`
- Main FBX with collision proxy: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady.fbx`
- LOD0-LOD3 FBX exports: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/`
- Texture maps: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/`
- Front match review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady_FrontMatchReview.png`
- Perspective review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady_PerspectiveReview.png`
- Metrics: LOD0 742 tris; LOD1 636 tris; LOD2 390 tris; LOD3 314 tris; bounds 348.42 cm wide x 65.00 cm deep x 157.92 cm high.
- Approval boundary: DCC candidate package is complete, but A1 still needs Flamestrike aesthetic approval before canon lock, Unreal import, startup placement, material final, or collision correctness claims.

## Build Metrics

- LOD0: 47 mesh objects, 2008 triangles.
- Bounds: 329.57 cm wide x 244.26 cm deep x 153.85 cm high.
- LOD1: 268 triangles.
- LOD2: 212 triangles.
- LOD3: 168 triangles.
- Collision proxy source: 1 UCX-style hull.
- Starter texture maps: 1024 x 1024 BC/N/ORM PNG outputs.
- Painted preview maps: 2048 x 2048 BC/N/ORM PNG outputs in both the texture source folder and ArmorPaint handoff folder.
- Material strategy: separate DCC review materials for stone, paint, rawhide, ash, and mud until the manual paint pass is approved.
- Final Unreal material consolidation: pending after painted maps are approved.

## DCC Source Contents

- Faceted low slab cluster matching the `A1` collapsed cairn direction.
- Ash/mud grounding disc.
- Oxide-red Blood Axe paint geometry.
- Rawhide strap and cord geometry.
- Multiple temporary DCC materials to preserve the concept-match paint/stone separation before the manual paint pass.
- 1024 x 1024 BC/N/ORM starter texture handoff maps.
- 2048 x 2048 BC/N/ORM painted preview maps for aesthetic review only.
- ArmorPaint package with refreshed paint-target FBX, `A1` concept reference, current review image, starter maps, and export instructions.
- Hidden LOD1, LOD2, and LOD3 source collections.
- Hidden collision proxy source collection.
- Review-only reference plane and scale markers.
- Production metadata empty with Unreal target path.

## Known Limits

- Uses generated starter maps, generated painted preview maps, and DCC review materials. The result is structurally ready for paint handoff, but it does not yet match the concept's hand-painted finish closely enough to call final art.
- ArmorPaint is installed and the paint handoff package is prepared. Final hand-painted BC/N/ORM exports are still pending.
- Collision proxy is a DCC source proxy only and requires Unreal import validation before gameplay use.
- The asset has not been imported into Unreal, placed in startup review, or tested against lighting/collision/navigation.
- The current review render is for subjective art-direction review before the pipeline is scaled or canon-locked.
