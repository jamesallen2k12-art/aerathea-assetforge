# SM_GIA_BloodAxeCairnSlabCluster_A01 Faithful Trace Status

## Status

Created as a separate A1 faithful reconstruction proof, not a replacement for the prior procedural DCC proof yet.

This pass proves the concept-first workflow: camera-projected concept art is placed onto a mesh so the approved A1 image can be matched before hand-building final 360-degree geometry.

## Source Reference

- Source concept: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- Candidate status: A1 remains pending Flamestrike approval as canon/final visual direction.

## Outputs

- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_faithful_trace.py`
- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace.blend`
- Main FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace.fbx`
- LOD0-LOD3 FBX exports: same export folder.
- Projection texture copy: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/T_GIA_BloodAxeCairnSlabCluster_A01_A1_ConceptProjection.png`
- Exact projection review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace_ExactProjectionReview.png`
- Cutout trace review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace_ConceptTraceReview.png`
- Overlay fit review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace_OverlayFitReview.png`

## Metrics

- LOD0 trace mesh: 6334 tris.
- LOD1: 1662 tris.
- LOD2: 544 tris.
- LOD3: 194 tris.
- Bounds: 348.00 cm wide x 12.18 cm deep x 152.81 cm high.
- Collision proxy: 1 simple source hull.

## What This Proves

- The concept can be matched visually from the approved camera by projecting the source image onto mesh.
- The exact projection review shows a near-perfect source-view match because it uses the A1 image as the projection texture.
- This is the correct first step before modeling final slabs by eye.

## Known Limits

- The exact projection mesh is a camera-view proof, not a true 360-degree game prop.
- The cutout trace still needs manual stone-by-stone cleanup before it can replace the procedural DCC proof.
- Back, side, underside, and occluded stone forms still need to be inferred or concepted separately.
- The projection material is review-source material only. Final Unreal import needs real authored BC/N/ORM maps, material slots, UV cleanup, and optimized stone shells.

## Recommended Next Step

If Flamestrike approves the faithful projection method, build A1 as traced stone shells:

1. Lock the exact projection view as the front visual target.
2. Trace each visible stone into separate shell geometry.
3. Project the A1 image onto the front faces.
4. Hand-paint sides/back/undersides in ArmorPaint or Blender.
5. Re-render the same camera and compare against A1 before Unreal import.
