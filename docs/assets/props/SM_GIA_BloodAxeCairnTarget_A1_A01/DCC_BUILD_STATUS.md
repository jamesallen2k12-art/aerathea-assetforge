# SM_GIA_BloodAxeCairnTarget_A1_A01 DCC Build Status

## Current Status

- Status: `DCC source candidate pending concept-geometry review`
- Source target: `docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTarget_A1.png`
- Brief: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/CONCEPT_GEOMETRY_BRIEF.md`
- Unreal status: not imported
- Final approval status: not approved

## Latest Build

- Build date: 2026-07-03
- Build script: `Tools/DCC/build_bloodaxe_cairn_target_a1.py`
- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/CairnTargets/A1/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01.blend`
- FBX export root: `SourceAssets/Exports/Props/Giants/BloodAxe/CairnTargets/A1/SM_GIA_BloodAxeCairnTarget_A1_A01/`
- Texture root: `SourceAssets/Textures/Props/Giants/BloodAxe/CairnTargets/A1/SM_GIA_BloodAxeCairnTarget_A1_A01/`
- DCC render root: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnTarget_A1_A01/`
- Concept comparison: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_ConceptGeometryCompare.png`
- DCC target-layout proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_DCCProofTargetLayout.png`
- LOD0: 3144 tris
- LOD1: 1488 tris
- LOD2: 636 tris
- LOD3: 524 tris

## Second Geometry Pass

- Rebuilt primary stones as irregular extruded slab outlines instead of simple tapered boxes.
- Added light/dark stone facet planes to expose the major chipped planes in DCC review.
- Reworked the main front slab, rear oath slab, right uprights, left lashed stack bindings, Blood Axe red paint layout, and front rubble scatter.
- Added deterministic UV0 smart projection to LOD0-LOD3.
- Switched DCC proof renders to Workbench/material preview with cavity shading so geometry reads clearly in concept comparisons.
- Regenerated source `.blend`, FBX, LOD0-LOD3, broad UCX collision export, DCC proof renders, target-layout proof, and concept comparison sheet.

## Gate

The current proof must be evaluated against the A1 target image side by side. If the DCC candidate does not match the dominant A1 geometry, revise the DCC source before any Unreal import, texture polish, or batch expansion.

## Required Outputs

- Blender source: complete for source candidate
- FBX export: complete for source candidate
- LOD0-LOD3 exports: complete for source candidate
- Broad UCX collision export: complete for source candidate
- DCC front/right/back/left/hero proof renders: complete for source candidate
- Concept-vs-DCC comparison sheet: complete for source candidate

## Notes

This asset intentionally starts a new clean lane instead of reusing the older `SM_GIA_BloodAxeCairnSlabCluster_A01_*` repair lineage. The older files remain useful historical evidence and automation references, but the clearer `BloodAxe A1` target is now the source of truth.

## Review Result

The second-pass A1 DCC source candidate is useful as a geometry planning proof, but it should not pass concept-geometry approval yet.

What it captures:

- Low cairn cluster footprint with irregular terrain contact.
- Dominant front slab lane.
- Tall rear slab lane.
- Left lashed stack lane.
- Right support-stone lane.
- Rear/side authored massing instead of a front-only plane.
- Clearer chipped-plane read through large facet geometry.
- More reviewable DCC proof captures for front/right/back/left/hero orientation.

Remaining gaps before approval:

- Stone forms are improved but still too clean and planar compared with the concept's fractured natural slabs.
- Front slab still needs a sculpt/detail pass for chipped edges, concave breaks, and broken face planes.
- Rear and side stones are in the right lane, but need better organic proportion and less blockout-like vertical massing.
- Red paint placement is improved, but still reads as raised bars instead of worn hand-painted Blood Axe pigment integrated into the stone surface.
- Rope bindings need rounder volume and wrapped-material read.
- Ground rubble density is improved but still below the concept target.

Decision: hold at `DCC source candidate pending concept-geometry review`; do not import to Unreal yet. This is not a `DCC game-ready candidate` and not `Fully game-ready`.

## Reference Benchmark Link

- Benchmark doc: `docs/assets/benchmarks/STATIC_PROP_REFERENCE_BENCHMARKS_A01.md`
- Applied process lesson: keep the A1 production package complete and reviewable like the reference packages, but keep the `BloodAxe A1` concept image as the only visual target.
- Next build should preserve source, exports, LODs, UCX, proof images, status notes, and deterministic rebuild script while improving the actual concept match.
