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
- Material/texture proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_MaterialTextureProof.png`
- LOD0: 6196 tris
- LOD1: 3264 tris
- LOD2: 1376 tris
- LOD3: 1104 tris

## Second Geometry Pass

- Rebuilt primary stones as irregular extruded slab outlines instead of simple tapered boxes.
- Added light/dark stone facet planes to expose the major chipped planes in DCC review.
- Reworked the main front slab, rear oath slab, right uprights, left lashed stack bindings, Blood Axe red paint layout, and front rubble scatter.
- Added deterministic UV0 smart projection to LOD0-LOD3.
- Switched DCC proof renders to Workbench/material preview with cavity shading so geometry reads clearly in concept comparisons.
- Regenerated source `.blend`, FBX, LOD0-LOD3, broad UCX collision export, DCC proof renders, target-layout proof, and concept comparison sheet.

## Third Sculpt/Detail Pass

- Integrated lessons from the saved BloodAxe Cairnstone Asset reference as support reference only, not as visual canon.
- Added more chipped light/dark fracture facets on the main slab, right support, front foot stone, and rear oath slab.
- Replaced rectangular rawhide blocks with rounder rope/lash cylinders and knot forms.
- Reworked red marks as thinner worn paint patches instead of heavy raised bars.
- Increased loose ground rubble density and regenerated all DCC proof captures.
- Kept the asset in the small prop budget at LOD0 3832 tris.

## Fourth Geometry Pass

- Converted the left lashed stack, rear counterweight, front foot stones, rear lock stones, and side buttresses from clean beveled boxes into fractured slab meshes.
- Recut the dominant front slab, tall rear oath slab, and right support stones with sharper jagged outlines so the silhouette changes, not only the surface detail.
- Replaced rectangular-looking chipped facet patches with lower-contrast jagged fracture patches.
- Increased DCC review camera framing so the tall rear slab is no longer clipped in front, side, back, left, hero, or turntable proof images.
- Regenerated the Blender source, FBX exports, LOD exports, DCC proof renders, target-layout proof, and concept comparison sheet.
- Triangle budget moved from small-prop range into the approved large-prop range from the concept brief: LOD0 6196 tris, LOD1 3264, LOD2 1376, LOD3 1104.

## First Material/Texture Integration Pass

- Generated 1K Base Color, Normal, and packed ORM texture maps for Stone, Earth, Rawhide, and RedPaint.
- Wired the generated BC/N/ORM maps into the Blender proof materials so the DCC renders now show texture integration rather than flat review colors.
- Switched proof rendering to lit EEVEE with ambient occlusion, broad fill lighting, and stable gray review background.
- Regenerated front, right, back, left, hero, turntable, concept-comparison, target-layout, and material/texture proof images.
- Geometry and LOD counts are unchanged from the fourth geometry pass: LOD0 6196 tris, LOD1 3264, LOD2 1376, LOD3 1104.
- Red paint remains a proof treatment for review; final stained/dry-brushed texture art should be refined only after concept-geometry approval.
- Status remains `DCC source candidate pending concept-geometry review`.

## Gate

The current proof must be evaluated against the A1 target image side by side. If the DCC candidate does not match the dominant A1 geometry, revise the DCC source before any Unreal import, final texture polish, or batch expansion.

## Required Outputs

- Blender source: complete for source candidate
- FBX export: complete for source candidate
- LOD0-LOD3 exports: complete for source candidate
- Broad UCX collision export: complete for source candidate
- DCC front/right/back/left/hero proof renders: complete for source candidate
- Concept-vs-DCC comparison sheet: complete for source candidate
- Material/texture proof sheet: complete for source candidate

## Notes

This asset intentionally starts a new clean lane instead of reusing the older `SM_GIA_BloodAxeCairnSlabCluster_A01_*` repair lineage. The older files remain useful historical evidence and automation references, but the clearer `BloodAxe A1` target is now the source of truth.

## Review Result

The fourth-pass A1 DCC source candidate is now a useful concept-geometry review candidate, but it should not move to Unreal import or `DCC game-ready candidate` status without Flamestrike approval against the A1 target.

What it captures:

- Low cairn cluster footprint with irregular terrain contact.
- Dominant front slab lane.
- Tall rear slab lane.
- Left lashed stack lane.
- Right support-stone lane.
- Rear/side authored massing instead of a front-only plane.
- Clearer chipped-plane read through large facet geometry.
- More reviewable DCC proof captures for front/right/back/left/hero orientation.
- Rounder rope binding volumes and more rubble density than the second pass.
- Red marks now read more like worn applied pigment than the earlier raised bars.
- Major secondary stones now use fractured silhouettes instead of clean beveled box silhouettes.
- Review captures are fully framed and no longer clip the tall rear slab.
- First-pass BC/N/ORM textures are now present and wired into the Blender proof materials.

Remaining gaps before approval:

- Stone silhouette is much closer, but still lacks the concept's hand-authored natural stone breakup and texture-level chipped erosion.
- Red paint is readable and now textured, but still needs final stained/dry-brushed material polish after geometry approval.
- Rope bindings have round volume, but their contact and wrapping paths should be refined after geometry approval.
- Ground rubble density is better, but the mound still needs a more natural dirt/stone blend around the footprint.
- Current proof material is a first-pass DCC texture integration pass; final Unreal material instances and import validation are still pending.

Decision: hold at `DCC source candidate pending concept-geometry review`; do not import to Unreal yet. This is not a `DCC game-ready candidate` and not `Fully game-ready`.

## Reference Benchmark Link

- Benchmark doc: `docs/assets/benchmarks/STATIC_PROP_REFERENCE_BENCHMARKS_A01.md`
- Applied process lesson: keep the A1 production package complete and reviewable like the reference packages, but keep the `BloodAxe A1` concept image as the only visual target.
- Next build should preserve source, exports, LODs, UCX, proof images, status notes, and deterministic rebuild script while improving the actual concept match.

## Cairnstone Asset Reference Intake

- Reference intake: `docs/assets/reference/bloodaxe_cairnstone_asset/README.md`
- Curated support sheet: `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A01_CuratedReferenceSheet.png`
- Payload limitation: the saved HTML mentioned `BloodAxe_Cairnstone_Asset_Package.zip`, `.glb` LODs, and a UCX `.obj`, but those actual files were not present locally. This is therefore image reference only, not a verified 3D benchmark.
- Applied A1 lessons: make stone planes more fractured and chipped, make red paint thinner/worn into the stone surface, replace rectangular rawhide blocks with rounder rope/wrap forms, densify ground rubble, and keep authored side/back massing.
- Boundary: the A1 visual-canon target remains `docs/assets/visual_canon/BloodAxeCairnTargets_A01/VC_GIA_BloodAxe_CairnTarget_A1.png`. Do not use the larger shrine, throne, camp, or stacked-cairn references to redefine the A1 silhouette.
