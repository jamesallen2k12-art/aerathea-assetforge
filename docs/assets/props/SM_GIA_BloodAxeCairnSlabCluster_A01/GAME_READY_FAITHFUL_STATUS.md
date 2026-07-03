# SM_GIA_BloodAxeCairnSlabCluster_A01 Game-Ready Faithful Status

## Status

Unreal-imported DCC game-ready candidate package, placed on the Aerathea review island for Flamestrike aesthetic approval.

`SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady` converts the approved A1 source-view proof into a buildable static-mesh package with real slab shell depth, concept-projected front UVs, production side/back materials, LOD0-LOD3 FBX exports, texture maps, collision proxy source, Unreal material instances, Unreal LOD setup, broad collision, and review-island placement.

This is not `Fully game-ready` yet. It has passed Unreal import and technical validation, but final visual approval, gameplay collision approval, and library approval are still pending. The source-view match remains the strongest result. The side/back treatment remains an aesthetic approval item because a single concept image cannot define perfect 360-degree geometry by itself.

## Source Reference

- Visual board: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_CandidateBoard.png`
- Selected crop: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- Preceding proof: `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/FAITHFUL_TRACE_STATUS.md`

## Outputs

- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_game_ready.py`
- Unreal importer: `Tools/Unreal/import_bloodaxe_cairn_game_ready.py`
- Unreal validator: `Tools/Unreal/validate_bloodaxe_cairn_game_ready.py`
- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady.blend`
- Main FBX with collision proxy: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady.fbx`
- LOD0 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady_LOD0.fbx`
- LOD1 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady_LOD1.fbx`
- LOD2 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady_LOD2.fbx`
- LOD3 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady_LOD3.fbx`
- Concept projection BC: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/T_GIA_BloodAxeCairnSlabCluster_A01_A1Projection_BC.png`
- Side/back BC: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/T_GIA_BloodAxeCairnSlabCluster_A01_GameReadySide_BC.png`
- Side/back normal: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/T_GIA_BloodAxeCairnSlabCluster_A01_GameReadySide_N.png`
- Side/back ORM: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/T_GIA_BloodAxeCairnSlabCluster_A01_GameReadySide_ORM.png`
- Front match review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady_FrontMatchReview.png`
- Perspective review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady_PerspectiveReview.png`
- Unreal mesh: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady`
- Unreal review island map: `/Game/Aerathea/Maps/L_Aerathea_ReviewIsland`
- Unreal review actor: `AET_REVIEW_CurrentAsset_BloodAxeCairn_A01`
- Unreal material instances:
  - `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_GameReady_A1Projection`
  - `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_GameReady_StoneSide`
  - `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_GameReady_AshMud`
  - `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_GameReady_Rawhide`

## Build Metrics

- LOD0: 742 triangles.
- LOD1: 636 triangles.
- LOD2: 390 triangles.
- LOD3: 314 triangles.
- LOD0 bounds: 348.42 cm wide x 65.00 cm deep x 157.92 cm high.
- Collision proxy source: 1 UCX-style hull in the main FBX.
- Material slots: concept projection front, side/back stone, ash/mud, rawhide.
- Texture maps: 360 x 430 concept projection copy plus 1024 x 1024 side/back BC/N/ORM maps.
- Unreal validated bounds: 170.65 cm high x 351.50 cm wide x 78.00 cm deep.
- Unreal validated setup: 4 LODs, 4 material slots, 4 imported texture assets, broad collision enabled.

## Production Notes

- Front/source-view fidelity is driven by concept-projected UVs.
- Main forms are real low-poly slab shells with tapered/faceted backs.
- Small cracks, chips, paint breakup, dirt speckles, and lashing fibers remain texture work rather than modeled micro-detail.
- The side/back surfaces are production placeholders derived from the concept palette. They should be approved, repainted, or replaced before canon lock.
- The package has completed Unreal import testing with static mesh import, LOD assignment, texture hookup, review-island placement, and broad collision validation.
- The offscreen `-game -RenderOffscreen` capture path crashed before writing a new screenshot, so the latest proof state is validator evidence plus live-editor review access rather than a fresh review PNG.

## Unreal Validation Evidence

Validated on `2026-07-02`.

Focused validator result:

`Blood Axe game-ready cairn validation passed: 170.65h x 351.50w x 78.00d cm, 4 LODs, 4 materials, 4 textures, review island actor AET_REVIEW_CurrentAsset_BloodAxeCairn_A01, broad collision enabled.`

General review island validator result:

`Aerathea review island validation passed: 83 tagged actors, 13 asset slots, fixed-lighting review map /Game/Aerathea/Maps/L_Aerathea_ReviewIsland.`

Open the placed asset for observation with:

`Tools/Unreal/launch_review_island_editor.sh`

## Approval Boundary

Flamestrike approval is still required for:

- whether A1 should become canon for this cairn asset;
- whether the side/back interpretation is acceptable for real gameplay cameras;
- whether the darker DCC render should be brightened during Unreal material setup;
- whether broad collision is acceptable for first gameplay use or needs hand-authored refinement;
- whether to promote the imported review-island candidate from `DCC game-ready candidate` to `Fully game-ready`.
