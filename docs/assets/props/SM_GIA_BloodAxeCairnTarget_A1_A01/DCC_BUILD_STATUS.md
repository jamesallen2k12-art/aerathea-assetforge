# SM_GIA_BloodAxeCairnTarget_A1_A01 DCC Build Status

## Current Status

- Status: `DCC source candidate pending concept-geometry and paint review`
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
- Strict front paint comparison: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_StrictFrontPaintCompare.png`
- DCC target-layout proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_DCCProofTargetLayout.png`
- Material/texture proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_MaterialTextureProof.png`
- Rejected clean baseline proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_RejectedCleanBaseline_A02.png`
- A1 front trace guide: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_A1_FrontTraceGuide.png`
- Traced geometry proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_TracedGeometryPass_A03.png`
- Fractured face proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_FracturedFacePass_A04.png`
- Traced outline proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_TracedOutlinePass_A05.png`
- Reclined multi-pass proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_ReclinedMultiPass_A08.png`
- Authored multi-plane proof: `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_AuthoredMultiPlanePass_A09.png`
- LOD0: 4496 tris
- LOD1: 2472 tris
- LOD2: 1542 tris
- LOD3: 1228 tris

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

## Strict Paint Correction Pass

- Flamestrike rejected the prior material proof because the painted rock marks read as raised red sticks.
- Production lesson recorded: concept paint must stay surface pigment unless the concept clearly shows attached geometry.
- Replaced the raised/extruded red paint patch meshes with no-thickness surface pigment ribbon meshes.
- Changed red material metadata to `worn_oxide_pigment_surface_decal` and kept the red treatment opaque so it reads as visible painted stone rather than semi-transparent UI markup.
- Reduced dash-like breakup after the first correction pass made the red marks too faint and fragmented.
- Regenerated the Blender source, FBX exports, LOD exports, textures, DCC proof renders, target-layout proof, concept comparison, material proof, and strict front paint comparison.
- Latest triangle counts: LOD0 5914 tris, LOD1 3132, LOD2 1376, LOD3 1104.
- Status remains `DCC source candidate pending concept-geometry and paint review`.

## Strict A1 Rejection Learning Pass

- Flamestrike rejected the latest A1 image as not approved.
- Revision attempt tested darker stone/earth/rawhide texture ranges, a lower/wider dominant front slab, thinner darkened lashings, and more visible worn red pigment.
- A crack/highlight overlay attempt failed because the flat surface accent planes read as white/black graphic shards instead of natural hand-painted stone breakup.
- Failed overlay accent planes were removed from the active clean baseline; their lesson is retained in source history, not in the current proof.
- Latest clean baseline proof is saved as `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_RejectedCleanBaseline_A02.png`.
- Latest triangle counts: LOD0 4356 tris, LOD1 2168, LOD2 1396, LOD3 1116.
- Status remains `DCC source candidate pending concept-geometry and paint review`; final approval status is `not approved`.

## A1 Front Trace Guide Pass

- Added a technical front trace guide derived from the approved A1 target crop.
- Locked review landmarks for the ground line, dominant front slab, tall rear slab, left lashed stack, right bound support, red paint lanes, and rope binding zones.
- Rebuilt the front composition against those trace landmarks instead of adding more texture or crack overlays.
- Lowered and sharpened the dominant front slab so it is less broad/wall-like than the rejected clean baseline.
- Shortened the rear slab, reduced right-side vertical clutter, reduced the left stack mass, darkened the rawhide material, and removed the prior X-like lashing read.
- Saved the latest in-progress trace proof as `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_TracedGeometryPass_A03.png`.
- Latest triangle counts: LOD0 4172 tris, LOD1 2012, LOD2 1300, LOD3 1028.
- Status remains `DCC source candidate pending concept-geometry and paint review`; final approval status is `not approved`.
- Review note: this pass is improved but still not strict enough. The front stone needs more hand-authored fractured plane geometry, the rear slab still reads too isolated, rope bindings still read too rod-like, and red paint remains too graphic.

## Fractured Face And Offset Paint Pass

- Tested mesh-level face perturbation inside `add_fractured_slab` instead of adding separate black/light crack overlay planes.
- Added curved rawhide rope meshes to replace the straight cylinder rope pass.
- Fixed a generator bug where `add_surface_stroke` accepted a surface offset value but ignored it; paint strokes now use the offset field to reduce z-fighting.
- Adjusted the dominant front slab to stand more upright, shortened the tall rear slab, reduced the isolated right rear shard, and regenerated the Blender source plus FBX/LOD exports.
- Saved the latest in-progress proof as `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_FracturedFacePass_A04.png`.
- Latest triangle counts: LOD0 4458 tris, LOD1 2222, LOD2 1484, LOD3 1156.
- Status remains `DCC source candidate pending concept-geometry and paint review`; final approval status is `not approved`.
- Review note: this pass fixed part of the previous surface-plane failure, but the front still reads as one broad tabletop slab. The next pass must replace the one-piece dominant slab with a stricter multi-plane stone construction matching the A1 front target before paint polish continues.

## Traced Outline Front Slab Learning Pass

- Replaced the dominant front slab outline with a stricter traced A1 polygon and reduced the mesh face perturbation so the silhouette could be judged without heavy procedural noise.
- Made the red pigment material opaque and removed alpha coupling in the proof material so paint is treated as surface pigment instead of semi-transparent decal markup.
- Softened the DCC review world light and fill light to reduce false black tearing in proof renders.
- Saved the latest in-progress proof as `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_TracedOutlinePass_A05.png`.
- Latest triangle counts: LOD0 4170 tris, LOD1 2018, LOD2 1354, LOD3 1044.
- Status remains `DCC source candidate pending concept-geometry and paint review`; final approval status is `not approved`.
- Review note: this pass is useful failure evidence, not an approval candidate. The traced front silhouette moved closer to the A1 crop, but the 3D read became too upright, front-facing, smooth, and shield-like instead of a low collapsed slanted cairn stone integrated into the mound.
- Next pass should use the trace polygon as a proportion guide only: lean the slab back/down, lower it into the pile, restore low collapsed massing, and hold red pigment until the stone geometry reads correctly.

## Reclined Slab Multi-Pass Learning Pass

- Iterated through A06-A08 after A05: A06 overcorrected into a flat raft/tabletop, A07 found a better angle but stayed oversized and oval, and A08 narrowed/thinned the slab while reducing black graphic paint artifacts.
- Reduced the dominant slab from a vertical traced shield shape into a reclined chipped stone face, narrowed the left bundled stack, added smaller shoulder/foot wedges, and reduced paint strokes to keep geometry readable.
- Saved the latest in-progress proof as `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_ReclinedMultiPass_A08.png`.
- Latest triangle counts: LOD0 4288 tris, LOD1 2280, LOD2 1334, LOD3 1028.
- Status remains `DCC source candidate pending concept-geometry and paint review`; final approval status is `not approved`.
- Review note: this pass improves the A05/A06 angle problem and reduces the paint artifact, but it is still not close enough to the A1 concept. The main face remains one broad procedural slab with a smooth/oval read, the underside still reads too black, and the concept's chipped multi-plane slate fracture language is missing.
- Next pass must stop rotating one monolithic slab. Build the dominant A1 face as multiple authored stone planes: upper-left shoulder, central painted face, right broken cheek, front lower lip, and embedded support wedges, each with separate chipped outlines and shallow depth.

## Authored Multi-Plane Front Learning Pass

- Replaced the single dominant slab with separate authored front planes: central painted face, upper-left shoulder plane, right broken cheek plane, lower front lip plane, and embedded support wedges.
- This moved the structure away from the one-piece slab failure and made the front read more broken, but the result still does not match the A1 concept.
- Saved the latest in-progress proof as `docs/assets/props/SM_GIA_BloodAxeCairnTarget_A1_A01/SM_GIA_BloodAxeCairnTarget_A1_A01_AuthoredMultiPlanePass_A09.png`.
- Latest triangle counts: LOD0 4496 tris, LOD1 2472, LOD2 1542, LOD3 1228.
- Status remains `DCC source candidate pending concept-geometry and paint review`; final approval status is `not approved`.
- Review note: the multi-plane structure is directionally better, but the face now reads as layered shingles with harsh black seams rather than a chipped painted stone. The target requires a more faithful volumetric guide before further hand-authored tuning.
- Next pass should use the existing TRELLIS-AMD multi-view research path or a generated multi-view A1 reference to extract volume proportions and plane landmarks, then rebuild the DCC source from those landmarks. Do not repeat the single-view TRELLIS.2 flat-relief path.

## Gate

The current proof must be evaluated against the A1 target image side by side. If the DCC candidate does not match the dominant A1 geometry or if the red paint still reads as separate geometry, revise the DCC source before any Unreal import, final texture polish, or batch expansion.

## Required Outputs

- Blender source: complete for source candidate
- FBX export: complete for source candidate
- LOD0-LOD3 exports: complete for source candidate
- Broad UCX collision export: complete for source candidate
- DCC front/right/back/left/hero proof renders: complete for source candidate
- Concept-vs-DCC comparison sheet: complete for source candidate
- Strict front paint comparison sheet: complete for source candidate
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
- Red markings are now no-thickness surface pigment patches instead of raised strip/slab geometry.

Remaining gaps before approval:

- Stone silhouette is much closer, but still lacks the concept's hand-authored natural stone breakup and texture-level chipped erosion.
- Red paint no longer uses raised strip geometry, but the corrected surface-paint treatment still needs Flamestrike approval against the strict front comparison.
- Rope bindings have round volume, but their contact and wrapping paths should be refined after geometry approval.
- Ground rubble density is better, but the mound still needs a more natural dirt/stone blend around the footprint.
- Current proof material is a first-pass DCC texture integration pass; final Unreal material instances and import validation are still pending.
- Latest rejected proof remains too broad and wall-like compared with A1; next correction must start from traced front proportions before adding any further texture/detail overlays.
- Latest traced proof improves the A1 proportions, but it is still not visually approved and should continue through stricter fractured-plane geometry before paint polish.
- Latest fractured-face proof reduces the rope/stroke implementation problems, but the dominant stone construction is still not faithful enough to A1.

Decision: hold at `DCC source candidate pending concept-geometry and paint review`; do not import to Unreal yet. This is not a `DCC game-ready candidate` and not `Fully game-ready`.

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
