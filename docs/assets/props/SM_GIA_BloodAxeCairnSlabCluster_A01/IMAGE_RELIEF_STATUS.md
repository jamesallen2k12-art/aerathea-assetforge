# SM_GIA_BloodAxeCairnSlabCluster_A01 Image-Relief Status

## Status

Unreal game-ready image-relief proof asset approved by Flamestrike on 2026-06-30.

`SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief` applies the user-requested 2D-to-3D reference workflow to the approved A1 concept crop: the source painting is alpha-matted, traced into shallow mesh layers, projected back onto the traced faces, given limited thickness, exported with LOD0-LOD3 FBXs, and packaged with a UCX collision proxy source.

The asset has now been imported into Unreal, material-configured, assigned LODs, given broad simple collision, placed in the startup review map at an isolated review coordinate, captured for visual approval, validated with a focused Unreal validator, and approved for this proof-of-concept lane.

## Reference Method

- Photo-to-game-asset workflow: trace/model visible forms from the image, project the image texture from view, and add practical depth.
  Source: `https://www.youtube.com/watch?v=ZR_X2OhsteQ`
- 2D-painting-to-3D workflow: separate visual layers, place them in depth, and use painted planes/extrusions for parallax.
  Source: `https://www.youtube.com/watch?v=Ff0aobJRSNc`
- Drawing-to-mesh workflow: convert traced drawing strokes/fills into mesh surfaces, then add extrusion/thickness and cleanup.
  Source: `https://www.youtube.com/watch?v=1gKnwBTWanA`
- User-provided Godot reference: multiple 2D drawings can be aligned in 3D to drive a stylized asset workflow.
  Source: `https://www.reddit.com/r/godot/comments/1txnz5u/how_i_use_a_bunch_of_2d_drawings_to_make_a_3d/`

## Art Direction Summary

- Source of truth: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- Culture and mood: Blood Axe Giant approach-marker cairn, brutal raider culture, dirty cairn stone, red war paint, rawhide lashings, muddy ash base.
- Keeper features: tilted painted center slab, rear upright slab, right standing stone, low rubble base, red painted markings, heavy lashed binding, dirt/stone breakup.
- Cleanup applied: neutral gray concept backdrop removed from the alpha texture so the background does not become part of the mesh.

## Gameplay Purpose

Static environmental storytelling prop for Blood Axe Giant zones, cave approaches, ritual paths, camp edges, and warning-marker set dressing. No animation, sockets, gameplay behavior, or combat interaction is included in this pass.

## Outputs

- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_image_relief_asset.py`
- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief.blend`
- Main FBX with collision proxy: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief.fbx`
- LOD0 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_LOD0.fbx`
- LOD1 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_LOD1.fbx`
- LOD2 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_LOD2.fbx`
- LOD3 FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_LOD3.fbx`
- Base color with alpha: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/T_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_BC.png`
- Normal map: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/T_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_N.png`
- ORM map: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/T_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_ORM.png`
- Review board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_ImageReliefReviewBoard.png`
- Front review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_FrontMatchReview.png`
- Angled review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_AngledParallaxReview.png`
- Side review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_SideDepthReview.png`
- Unreal isolated game-ready review: `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeCairnImageRelief_A01_IsolatedGameReadyReview.png`

## Unreal Outputs

- Import script: `Tools/Unreal/import_bloodaxe_cairn_image_relief.py`
- Startup placement script: `Tools/Unreal/place_bloodaxe_cairn_image_relief_startup_review.py`
- Focused validator: `Tools/Unreal/validate_bloodaxe_cairn_image_relief.py`
- Static mesh: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief/T_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_BC|N|ORM`
- Parent materials: `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_ImageReliefProjection_A01` and `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairn_ImageReliefSideStone_A01`
- Material instances: `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_Projection` and `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief_SideStone`
- Startup actor: `AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief`
- Review camera preset: `bloodaxe_image_relief_cairn`

## Build Metrics

- LOD0: 228 triangles.
- LOD1: 108 triangles.
- LOD2: 80 triangles.
- LOD3: 68 triangles.
- LOD0 bounds: 323.00 cm wide x 120.00 cm deep x 209.00 cm high.
- Pivot: bottom-center ground contact plane.
- Collision proxy source: 1 UCX-style hull in the main FBX.
- Material slots: concept-projected image material plus side-stone material.
- Texture set: 1440 x 1720 BC/N/ORM generated from the 360 x 430 approved source crop.

## Unreal Import Notes

- Asset type: Static Mesh.
- Target path: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_ImageRelief`
- Import scale: project script applies `0.01` uniform FBX import scale to match the current static-mesh import convention.
- Material setup: masked concept-projection parent uses the BC alpha as opacity mask; side-stone parent is opaque, rough, and non-metallic.
- Collision: broad simple box collision is generated in Unreal for static prop blocking.
- LODs: LOD0-LOD3 assigned by the import script.
- Lighting: isolated startup review camera uses lowered review lighting to avoid blowing out the projected painted texture.
- Validation: `Tools/Unreal/validate_bloodaxe_cairn_image_relief.py` passed on 2026-06-30.

## Approval Boundary

Approved use:

- Whether the front/angled image-relief fidelity is close enough to the A1 concept.
- Whether the visible side-card structure is acceptable for set dressing and gameplay camera angles.
- Whether this should become a canon method for concept-faithful background props.
- A true 360 sculpt pass is still required for hero/close-inspection cairns.

## Quality Gate

- Original to Aerathea: pass.
- Blood Axe visual identity: pass.
- Source concept fidelity from front camera: pass for DCC proof.
- All-angle sculpt fidelity: not claimed.
- Mid-poly MMO suitability: pass.
- LOD0-LOD3 source exports: pass.
- Texture maps: pass.
- Broad Unreal collision: pass.
- Unreal implementation: pass as game-ready proof candidate.
- Canon visual approval for proof-of-concept lane: pass, approved by Flamestrike on 2026-06-30.
