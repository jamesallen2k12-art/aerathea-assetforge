# SM_GIA_BloodAxeCairnSlabCluster_A01 Test 2 Manual Asset Status

## Status

Unreal game-ready Test 2 candidate generated, technically validated, and repainted with Paint-01 after Flamestrike's in-game review feedback on 2026-07-01.

`SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual` is a front-faithful deep image-relief reconstruction of A01: the approved concept is alpha-matted, traced into major visible mesh layers, projected onto those layers, deepened for walk-around inspection, exported with LOD0-LOD3 FBXs, imported into Unreal, assigned masked projection and side-stone materials, given broad collision, and placed in the startup review map.

This pass intentionally prioritizes A01 front/angled fidelity. It is a game-ready static prop candidate for proof-of-concept and set dressing, not a hand-sculpted hero prop.

Paint correction pass `A01-Test2-Paint-01` replaces the prior brightness/readability treatment. The corrective pass darkens stone albedo, strengthens Blood Axe red paint, warms rawhide and earth, adds texture-space AO/normal detail, removes review-material emissive compensation, lowers DCC review exposure, and keeps the A01-aligned traced geometry intact. It is technically validated and pending aesthetic reapproval in Unreal.

Approval scope: Flamestrike approved the Test 2 geometry/match direction, then flagged the in-game Paint/lighting read as over-bright. Paint-01 is pending Flamestrike reapproval for final color/aesthetic signoff. This scope does not add gameplay interaction, quest marker behavior, destruction, VFX/audio, or combat behavior.

## Timing

- Test 2 start: `2026-07-01T11:36:04-04:00`
- Validation complete: `2026-07-01T12:01:40-04:00`
- Brightness pass validated: `2026-07-01T12:15:50-04:00`
- Flamestrike approval recorded: `2026-07-01T12:18:33-04:00`
- Approved Unreal placement validated: `2026-07-01T12:21:42-04:00`
- In-game color feedback recorded: `2026-07-01T12:56:00-04:00`
- Paint-01 correction pass validated: `2026-07-01T13:12:02-04:00`
- Initial asset elapsed: `25m36s`
- Total elapsed through brightness pass: `39m46s`
- Total elapsed through Paint-01 validation: `1h35m58s`

## Outputs

- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_test2_manual.py`
- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual.blend`
- Main FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual.fbx`
- LOD FBXs: `SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_LOD0|LOD1|LOD2|LOD3.fbx`
- Texture set: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_BC|N|ORM.png`
- Review board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_FinalGameReadyReviewBoard.png`

## Unreal Outputs

- Import script: `Tools/Unreal/import_bloodaxe_cairn_test2_manual.py`
- Startup placement script: `Tools/Unreal/place_bloodaxe_cairn_test2_manual_startup_review.py`
- Focused validator: `Tools/Unreal/validate_bloodaxe_cairn_test2_manual.py`
- Static mesh: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual/T_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_BC|N|ORM`
- Parent materials: `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_Test2ManualProjection_A01` and `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_Test2ManualSideStone_A01`
- Material instances: `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_Projection` and `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual_SideStone`
- Startup actor: `AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual`
- Startup placement: `/Game/Aerathea/Maps/L_Aerathea_Startup` at `X=12880, Y=10000, Z=0`, yaw `-18`.
- Approval metadata: `Aerathea.StaticMesh.FinalVisualApproval=pending_flamestrike_reapproval_after_in_game_color_feedback`, `Aerathea.StaticMesh.ApprovedPass=A01-Test2-Paint-01`.

## Validation

Focused validator passed:

`Blood Axe test2-manual cairn validation passed: 209.00h x 323.00w x 156.00d cm, 4 LODs, 2 materials, 3 textures, startup actor AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual, broad collision enabled.`

Startup scene validator passed after restoring the global review camera to the standard `overview` preset:

`Aerathea startup validation complete: 233 assets, 55 expected actors, 25 ground tiles.`

## Build Metrics

- LOD0: 228 triangles.
- LOD1: 108 triangles.
- LOD2: 80 triangles.
- LOD3: 68 triangles.
- Bounds: 323.00 cm wide x 156.00 cm deep x 209.00 cm high.
- Material slots: masked A01 projection plus opaque side-stone.
- Collision: broad simple collision in Unreal.
- Gameplay behavior: none; static environmental storytelling prop.

## Review Boundary

Use this candidate to judge whether the A01 front-faithful projection workflow is acceptable as a practical game-ready static prop lane. Do not treat this as proof that a single image can produce perfect hero-quality 360 sculpt geometry without manual sculpting or additional approved side/back concept art.
