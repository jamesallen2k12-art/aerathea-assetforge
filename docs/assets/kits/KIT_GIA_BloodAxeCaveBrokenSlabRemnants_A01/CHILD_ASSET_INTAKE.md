# KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01 Child Asset Intake

## Source

- Parent backlog row: `Blood Axe Nomad Ritual Stones`
- Parent package: `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- Related package: `KIT_GIA_BloodAxeCaveRemnantCluster_A01`
- Supporting reference: `SM_GIA_BloodAxeCaveAshRemnantBase_A01`
- Material reference: `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01`
- Current package: `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only planning child breakdown; no row may proceed to DCC, FBX, Unreal, startup placement, runtime work, final cave approval, final visual approval, or first implementation target selection
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture
- Scale dependency: Giant scale lock from `SK_GIA_Base_A01` uses female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges remain females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm
- Source-storage guardrail: external source concepts remain external. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This intake splits `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01` into planning-only child rows for primary broken slab cluster, split slab pair, ash-grounded slab, painted slab, small chock stones, review row, material reference, and LOD/collision reference.

The kit is static cave-edge memory dressing only. Rows may describe how broad broken threshold stones, chipped red paint, ash, mud, soot, and cave grit read visually, but they must not define cave compatibility proof, traversal proof, route blocker behavior, interaction behavior, cave gameplay, path widths as gameplay values, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, readable signage, VFX/audio, destructible behavior, physics collapse, DCC, FBX, Unreal, startup placement, final cave approval, final visual approval, or first implementation target selection.

Blood Axe broken slab dressing must stay separate from neutral/civilized Giant culture. It may use rough highland stone, soot, ash, trampled mud, cave grit, chipped oxide red paint, sparse rope or rawhide residue, blackened iron, old horn, and dull bone. It must not use refined Giant cave-town masonry, blue-gray civic stonework, terrace/waterwork forms, warm hearth identity, peaceful highland wayfinding, carved civic ornament, or restrained blue-rune culture as the default read.

Every row below is marked `package-needed`, `planned`, or `reference-only`. No row creates or authorizes source assets, DCC, FBX, Unreal Content, runtime source, tools, validators, material instances, textures, VFX/audio, startup placement, source concept movement, final cave approval, final visual approval, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeCaveBrokenSlabRemnants_A01#PrimaryBrokenSlabCluster_A01` | Primary broken slab cluster | `SM_GIA_BloodAxeCaveBrokenSlabCluster_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeCaveBrokenSlabCluster_A01/PRODUCTION_PACKAGE.md` is ready for a broad cluster of one to three heavy threshold slab remnants with chipped edges, cold ash, trampled mud, cave grit, and restrained red paint scarring. Static visual history only; no cave compatibility proof, traversal proof, route blocker behavior, interaction behavior, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveBrokenSlabRemnants_A01#SplitSlabPair_A01` | Split slab pair | `SM_GIA_BloodAxeCaveSplitSlabPair_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeCaveSplitSlabPair_A01/PRODUCTION_PACKAGE.md` is ready for two large snapped slab pieces with offset rotation and a readable break relationship. Visual threshold memory only; no functional doorway, blocker, nav/pathfinding value, route validation, puzzle state, DCC, FBX, Unreal, startup placement, or implementation target. |
| `BloodAxeCaveBrokenSlabRemnants_A01#AshGroundedSlab_A01` | Ash-grounded slab | `SM_GIA_BloodAxeCaveAshGroundedSlab_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeCaveAshGroundedSlab_A01/PRODUCTION_PACKAGE.md` is ready for a single broad slab seated into cold ash, soot, trampled mud, and cave grit using the restraint from `SM_GIA_BloodAxeCaveAshRemnantBase_A01`. Grounded dressing only; no trigger area, damage field, aura, objective zone, collision correctness claim, DCC, FBX, Unreal, startup placement, final approval, or implementation target. |
| `BloodAxeCaveBrokenSlabRemnants_A01#PaintedSlab_A01` | Painted slab | `SM_GIA_BloodAxeCavePaintedSlab_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeCavePaintedSlab_A01/PRODUCTION_PACKAGE.md` is ready for a static slab variant with chipped dirty red paint and worn Blood Axe warning swipes. Paint is visual history only; no readable text, UI arrow, quest symbol, magic glyph, emissive map, material pulse, DCC, FBX, Unreal, startup placement, final visual approval, or implementation target. |
| `BloodAxeCaveBrokenSlabRemnants_A01#SmallChockStones_A01` | Small chock stones | `SM_GIA_BloodAxeCaveChockStones_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeCaveChockStones_A01/PRODUCTION_PACKAGE.md` is ready for sparse wedge-like stones jammed beside larger slabs to imply crude Giant handling and old threshold repair. Accent stones only; no climb assist, cover rule, physics prop, route blocker behavior, interaction behavior, collision proof, DCC, FBX, Unreal, startup placement, or implementation target. |
| `BloodAxeCaveBrokenSlabRemnants_A01#ReviewRow_ScalePaintGrounding_A01` | Review row | `DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01/PRODUCTION_PACKAGE.md` is ready for non-shipping rows comparing slab widths, split-pair stance, red paint density, ash/mud grounding, chock stone restraint, and Giant scale beside female 442 cm and male 470 cm baselines. No DCC, Unreal actor, validator, capture, startup placement, final cave approval, final visual approval, or implementation target. |
| `BloodAxeCaveBrokenSlabRemnants_A01#MaterialReference_A01` | Material reference | `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01` | reference-only | Use the cave-approach material discipline for rough highland stone, soot, ash, cave grit, trampled mud, chipped oxide red paint, rope/rawhide restraint, blackened iron, old horn, and dull bone. Reference only; no material instance creation, texture creation, material graph authoring, VFX/audio, DCC, FBX, Unreal, final color approval, or first implementation target. |
| `BloodAxeCaveBrokenSlabRemnants_A01#LODCollisionReference_A01` | LOD/collision reference | `DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01/PRODUCTION_PACKAGE.md` is ready as a docs-only reference row for future broken slab LOD0-LOD3 reduction order and disabled/simple collision policy, aligned to parent cave approach planning. No collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, route blocker setup, validators, DCC, FBX, Unreal Content, runtime implementation, or implementation target. |

## Dependency Notes

- `SK_GIA_Base_A01` owns Giant scale. This intake repeats the female 442 cm and male 470 cm baselines for broken slab scale comparison but does not change race scale, sockets, skeleton policy, collision capsules, or character proportions.
- `KIT_GIA_BloodAxeCaveApproachMarkers_A01` owns the broader cave approach marker planning lane. This broken slab remnant kit is a child lane for static threshold memory dressing only.
- `KIT_GIA_BloodAxeCaveRemnantCluster_A01` provides adjacent cave-edge remnant language. Broken slab remnants should read heavier, broader, and more threshold-specific than general cairn/standing-stone remnants.
- `SM_GIA_BloodAxeCaveAshRemnantBase_A01` provides ash, soot, mud, and cave-grit grounding discipline. Broken slab remnants should use that language without becoming gameplay zones or trigger areas.
- `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01` provides material restraint and neutral/civilized Giant separation.
- No row in this table is approved as a first DCC, FBX, Unreal, runtime, source asset, gameplay, final cave, final visual, or implementation target.

## Unordered Future Package Candidates

No first DCC target, source asset target, Unreal target, runtime target, gameplay target, cave approval target, final visual target, or implementation target is selected by this intake. If a later lead-approved package lane is opened, these may be promoted independently:

- `SM_GIA_BloodAxeCaveBrokenSlabCluster_A01`
- `SM_GIA_BloodAxeCaveSplitSlabPair_A01`
- `SM_GIA_BloodAxeCaveAshGroundedSlab_A01`
- `SM_GIA_BloodAxeCavePaintedSlab_A01`
- `SM_GIA_BloodAxeCaveChockStones_A01`
- `DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01`
- `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01`
- `DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01`

## Approval Gates

- Stop before DCC source, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content asset, material instance, texture asset, material graph, import script, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, startup placement, or any source asset creation.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before selecting a first DCC, FBX, Unreal, source asset, runtime, gameplay, cave approval, final visual, or implementation target from any row.
- Stop before cave compatibility proof, traversal proof, path widths as gameplay values, nav/pathfinding, route validation, route blocker behavior, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, UI arrows, spawn logic, patrol logic, AI spaces, damage values, aura behavior, projectile behavior, cover rules, trap behavior, destructible behavior, loot, inventory, rewards, crafting, economy, resource behavior, salvage, pickup behavior, VFX, audio, or material-state animation.
- Stop before claiming collision correctness, cave compatibility, terrain integration, runtime performance validation, marker validation, final silhouette approval, final cave approval, final Blood Axe approval, final Giant culture approval, or final visual approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, VFX/audio asset, global index, task board, backlog, bootstrap, or unrelated package file.
- Rows cover primary broken slab cluster, split slab pair, ash-grounded slab, painted slab, small chock stones, review row, material reference, and LOD/collision reference.
- Every row is marked `package-needed`, `planned`, or `reference-only`; no row claims permission to proceed to DCC, FBX, Unreal, final cave approval, final visual approval, implementation, or first target selection.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Approved Giant ranges are explicit: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Broken slab remnants remain broad static threshold memory dressing with chipped red paint and ash/mud cave-edge grounding.
- No cave compatibility proof, traversal proof, route blocker behavior, interaction behavior, cave gameplay, collision correctness, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, readable signage, path widths as gameplay values, VFX/audio, DCC, FBX, Unreal, source asset creation, startup placement, final cave approval, or final visual approval is defined.
- Review rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, marker validation, camera approval, final cave approval, or final visual signoff.
- Materials use rough highland stone, soot, ash, trampled mud, cave grit, chipped oxide red paint, sparse rope/rawhide residue, blackened iron, old horn, and dull bone consistently.
- Default emissive, glow, animated material states, gameplay VFX, audio cues, UI-like markers, readable text, route blockers, objective cues, neutral/civilized Giant language, and graphic gore are absent and approval-gated.
- Tiny stone chips, cracks, soot speckles, ash flecks, paint chips, lichen, mud streaks, grit, scratches, horn rings, bone pores, and rope fibers are assigned to textures or normals in future packages.
