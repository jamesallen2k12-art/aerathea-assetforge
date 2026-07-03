# SM_GIA_BloodAxeCairnSlabCluster_A01 Pass Timing Log

Purpose: track every A01 asset-production pass from source intake through DCC, texture work, Unreal import, validation, visual review, rejection, and approval.

Timing convention:

- Start/end timestamps use local project time: America/New_York.
- Elapsed time records active agent/tool work when measurable.
- Waiting on user approval, password entry, or unrelated delays is noted separately when known.
- A pass is not accepted just because it exports files; it must state its visual and technical result.

## Pass 00 - Current Run Setup

- Start: 2026-07-02 16:05 EDT
- Goal: restart the A01 Blood Axe cairn asset path from the approved A1 crop and multi-angle turnaround, then iterate until the asset is visually faithful, painted, imported, validated, and observable.
- Primary concept reference: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- Multi-angle reference: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_TurnaroundDraft_A01.png`
- Known rejected technical branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_Complete`
- Known incomplete visual branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundRebuild`
- Result: in progress.

## Pass 01 - Turnaround Painted DCC Candidate

- Start: 2026-07-02 16:16 EDT
- End: 2026-07-02 16:20 EDT
- Elapsed active work: approximately 4 minutes.
- Goal: generate a new DCC branch from the approved A1 crop plus multi-angle turnaround guide, with painted stone, red Blood Axe markings, rawhide wraps, ash/mud base, LODs, collision proxy, proof renders, and FBX exports.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_turnaround_painted.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted`
- Output: Blender source, LOD0-LOD3 FBXs, collision proxy, textures, and Front/Right/Back/Left/Top/Beauty proof renders were generated.
- Technical stats: LOD0 4,178 tris; LOD1 2,250 tris; LOD2 1,086 tris; LOD3 510 tris; LOD0 bounds 426.18w x 273.44d x 178.64h cm.
- Visual result: failed. The proof was too dark, too tall/blocky, and did not sufficiently match the compact A1 cairn silhouette, lighter chipped stone faces, and rawhide wrapping language. Not imported to Unreal.

## Pass 02 - Corrected Turnaround Painted DCC Candidate

- Start: 2026-07-02 16:21 EDT
- End: 2026-07-02 16:24 EDT
- Elapsed active work: approximately 3 minutes.
- Goal: revise the repeatable builder for A1 proportions, brighter hand-painted stone/readable proof lighting, tighter rawhide bands, smaller rear/upright stones, and a more compact footprint before re-exporting the DCC candidate.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_turnaround_painted.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted`
- Output: regenerated Blender source, LOD0-LOD3 FBXs, collision proxy, textures, and proof renders.
- Technical stats: LOD0 4,256 tris; LOD1 2,206 tris; LOD2 1,084 tris; LOD3 528 tris; LOD0 bounds 426.18w x 273.44d x 152.16h cm.
- Visual result: failed. Height improved, but proof remained too dark and the camera was too low to validate the central painted slab. Forms still read as large block slabs instead of compact chipped cairn stones. Not imported to Unreal.

## Pass 03 - Review Visibility and Camera Correction

- Start: 2026-07-02 16:24 EDT
- End: 2026-07-02 16:27 EDT
- Elapsed active work: approximately 3 minutes.
- Goal: add Blender-only proof visibility emission and raise the review camera to the approved A1/front-turnaround angle so the painted surface and stone breakup can be honestly evaluated.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_turnaround_painted.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_TurnaroundPainted`
- Output: regenerated proof renders and exports with corrected proof camera/visibility.
- Technical stats: LOD0 4,256 tris; LOD1 2,206 tris; LOD2 1,084 tris; LOD3 528 tris; LOD0 bounds 426.18w x 273.44d x 152.16h cm.
- Visual result: failed. The painted surface became visible, but the branch still did not resemble the approved A1 closely enough; it read as broad block slabs and did not preserve the approved front identity. Not imported to Unreal.

## Pass 04 - Hybrid360 Front Projection With Authored Backfill

- Start: 2026-07-02 16:28 EDT
- End: 2026-07-02 16:33 EDT
- Elapsed active work: approximately 5 minutes.
- Goal: create a new branch that preserves the front-faithful Test2 projection as the visual anchor while adding omitted authored side/back stone masses for 360-degree review.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_hybrid360.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_Hybrid360`
- Output: generated Blender source, LOD0-LOD3 FBXs, collision proxy, textures, and review board after resolving Blender/Pillow compatibility issues by running the projection branch in system Blender 3.0.
- Technical stats: LOD0 624 tris; LOD1 504 tris; LOD2 80 tris; LOD3 68 tris; LOD0 bounds 331.35w x 206.51d x 209.00h cm.
- Visual result: failed. The front identity was preserved better than the procedural branch, but the authored backfill created large rectangular gray masses that would fail backside approval. Not imported to Unreal.

## Pass 05 - Hybrid360 Smaller Backfill and Brighter Projection

- Start: 2026-07-02 16:34 EDT
- End: 2026-07-02 16:38 EDT
- Elapsed active work: approximately 4 minutes.
- Goal: revise Hybrid360 with smaller chipped backing stones, no large block wall, stronger DCC projection visibility, and preserved A1 front read.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_hybrid360.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_Hybrid360`
- Output: regenerated Blender source, LOD0-LOD3 FBXs, collision proxy, textures, and review board.
- Technical stats: LOD0 580 tris; LOD1 460 tris; LOD2 80 tris; LOD3 68 tris; LOD0 bounds 323.00w x 200.49d x 209.00h cm.
- Visual result: failed. Backfill improved in size but still read as artificial gray block supports; front projection remained too dark for approval-quality review. Not imported to Unreal.

## Pass 06 - Multi-View Projection Shell Candidate

- Start: 2026-07-02 16:39 EDT
- End: 2026-07-02 16:43 EDT
- Elapsed active work: approximately 4 minutes.
- Goal: use the approved multi-angle turnaround directly as front/right/back/left/top projection shells to test view fidelity across all approved angles before continuing true sculpted 360 work.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_multiview_projection_shell.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_MultiViewProjectionShell`
- Output: generated Blender source, LOD0-LOD3 FBXs, collision proxy, extracted multi-view textures, and review board.
- Technical stats: LOD0 186 tris; LOD1 186 tris; LOD2 6 tris; LOD3 6 tris; LOD0 bounds 335.00w x 220.00d x 210.00h cm.
- Visual result: failed as asset candidate, retained as diagnostic. It visibly used image-card shells, retained marker/label artifacts, and is not a believable 3D cairn. Not imported to Unreal.

## Pass 07 - Sculpted Mid-Poly True Geometry Candidate

- Start: 2026-07-02 16:44 EDT
- End: 2026-07-02 16:48 EDT
- Elapsed active work: approximately 4 minutes.
- Goal: generate a true-geometry A1-inspired cairn with authored mid-poly slabs, rubble, rawhide cords, red paint decals, chips, cracks, LODs, collision, and review renders.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_sculpted_midpoly.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_SculptedMidpoly`
- Output: generated Blender source, LOD0-LOD3 FBXs, collision proxy, and Front/Right/Back/Left/Top/Beauty review renders.
- Technical stats: LOD0 2,180 tris; LOD1 1,454 tris; LOD2 522 tris; LOD3 276 tris; LOD0 bounds 361.62w x 224.92d x 161.50h cm.
- Visual result: failed. The branch used true geometry and exportable LOD/collision structure, but the large forms still read as simplified rectangular blocks instead of the approved compact, chipped A1 stone pile. Not imported to Unreal.

## Pass 08 - Sculpted Mid-Poly Shape-Language Correction

- Start: 2026-07-02 16:49 EDT
- End: 2026-07-02 16:53 EDT
- Elapsed active work: approximately 4 minutes.
- Goal: replace cuboid slab forms with irregular sculpted prism/profile stones, increase angular rubble density, brighten proof materials, and re-check against the approved crop and turnaround before any Unreal import.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_sculpted_midpoly_v2.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_SculptedMidpolyV2`
- Output: generated Blender source, LOD0-LOD3 FBXs, collision proxy, and review renders.
- Technical stats: LOD0 3,790 tris; LOD1 2,430 tris; LOD2 918 tris; LOD3 540 tris; LOD0 bounds 354.61w x 220.65d x 161.50h cm.
- Visual result: failed. The irregular footprint improved the support stones and rubble, but the main painted slab was incorrectly modeled as a mostly horizontal slab; the front review showed an unpainted broad side with the red markings trapped on the top edge. Not imported to Unreal.

## Pass 09 - Tilted Painted Face Slab Rebuild

- Start: 2026-07-02 16:53 EDT
- End: 2026-07-02 16:58 EDT
- Elapsed active work: approximately 5 minutes.
- Goal: rebuild the main A1 hero stone as a broad tilted face slab with front-facing red paint, retain the improved irregular supporting stones, and review front/back/side/top fidelity before Unreal import.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_sculpted_midpoly_v3.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_SculptedMidpolyV3`
- Output: generated Blender source, LOD0-LOD3 FBXs, collision proxy, and review renders.
- Technical stats: LOD0 3,796 tris; LOD1 2,424 tris; LOD2 912 tris; LOD3 532 tris; LOD0 bounds 354.61w x 220.65d x 161.50h cm.
- Visual result: failed. The front-facing red paint orientation improved, but oversized support slabs and pale side masses still dominated the silhouette and the asset did not match the approved A1 crop/turnaround closely enough. Not imported to Unreal.

## Pass 10 - Clean Multi-View Relief Candidate

- Start: 2026-07-02 16:58 EDT
- End: 2026-07-02 17:02 EDT
- Elapsed active work: approximately 4 minutes.
- Goal: use the approved multi-angle turnaround as cleaned concept-derived textures on shallow extruded front/right/back/left/top relief meshes, removing marker/label artifacts, to test whether a static cairn can achieve observable concept fidelity from all review angles before a true sculpt/bake pass.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_clean_multiview_relief.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_CleanMultiViewRelief`
- Output: generated cleaned texture crops, Blender source, LOD0-LOD3 FBXs, collision proxy, and review board.
- Technical stats: LOD0 10 tris; LOD1 10 tris; LOD2 6 tris; LOD3 6 tris; LOD0 bounds 335.00w x 220.00d x 210.00h cm.
- Visual result: failed as a game-asset candidate. It confirmed that multi-view relief/card projection can preserve some orthographic concept information, but it still read as dark intersecting flat planes, retained crop/label artifacts, and lacked real mid-poly stone geometry. Not imported to Unreal.

## Pass 11 - Reduced-Block Sculpted Mid-Poly Candidate

- Start: 2026-07-02 17:03 EDT
- Goal: return to real mid-poly geometry but correct the prior sculpt failures: remove the oversized front support block, reduce pale side masses, keep the front-facing painted slab dominant, add smaller rubble, and use fewer/shorter chip decals so the prop reads closer to A1.
- Builder: `Tools/DCC/build_bloodaxe_cairn_a1_sculpted_midpoly_v4.py`
- Asset branch: `SM_GIA_BloodAxeCairnSlabCluster_A01_SculptedMidpolyV4`
- Result: in progress.
