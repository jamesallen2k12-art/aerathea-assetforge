# KIT_GIA_BloodAxeCaveApproachStandingPair_A01 Child Asset Intake

## Source

- Parent package: `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- Current package: `KIT_GIA_BloodAxeCaveApproachStandingPair_A01`
- Primary restraint reference: `docs/assets/props/SM_GIA_BloodAxeCaveApproachStandingPair_A01/PRODUCTION_PACKAGE.md`
- Material discipline reference: `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01/PRODUCTION_PACKAGE.md`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake scope: docs-only child planning. No child row may proceed to source asset creation, DCC, FBX, Unreal, startup placement, runtime work, functional doorway behavior, objective frame, nav gate, encounter trigger, interaction target, collision correctness claim, material graph, VFX/audio, final cave approval, final visual approval, or first implementation target selection.
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture.
- Scale dependency: Giant scale lock from `SK_GIA_Base_A01` uses female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges remain females 14-15 ft and males 14'10"-16'0".
- Source-storage guardrail: external source concepts remain external. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This intake splits `KIT_GIA_BloodAxeCaveApproachStandingPair_A01` into planning-only child rows for a static cave-threshold standing-pair family: primary pair context, leaning pair, broken pair, cloth-tied pair, low chock stones/base, spacing review row, material discipline reference, and LOD/collision reference.

The kit is static cave-threshold visual framing only. Rows may describe how paired stones frame a cave mouth, cliff opening, or abandoned shelter edge as Blood Axe territory, but they must not define functional doorway behavior, route validation, path widths as gameplay values, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, interaction targets, readable signage, spawn logic, patrol logic, damage/aura behavior, VFX/audio, DCC, FBX, Unreal, startup placement, final cave approval, final visual approval, or first implementation target selection.

Blood Axe standing-pair dressing must stay separate from neutral/civilized Giant culture. It may use rough highland stone, soot, ash, trampled mud, cave grit, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, and dull bone. It must not use refined Giant cave-town masonry, blue-gray civic stonework, terrace/waterwork forms, warm hearth identity, peaceful highland wayfinding, carved civic ornament, or restrained blue-rune culture as the default read.

Every row below is marked only `package-needed`, `planned`, or `reference-only`. No row creates or authorizes implementation status, source assets, DCC, FBX, Unreal Content, runtime source, tools, validators, material instances, textures, VFX/audio, startup placement, source concept movement, final approval, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeCaveApproachStandingPair_A01#PrimaryPairContext_A01` | Primary pair context | `SM_GIA_BloodAxeCaveApproachStandingPair_A01` | reference-only | Use the existing static mesh prop production package as the restraint reference for tall/short asymmetry, Giant-scale slab massing, broad base chock stones, restrained oxide red accents, and static visual threshold framing. This row does not select a DCC target, FBX target, Unreal target, startup target, final cave approval, final visual approval, or first implementation target. |
| `BloodAxeCaveApproachStandingPair_A01#LeaningPair_A01` | Leaning pair | `KIT_GIA_BloodAxeLeaningCaveStandingPair_A01` | planned | Controlled static leaning variant with broad chipped planes, embedded base weight, old mud/ash grounding, and optional restrained cloth. Planning only; no collapse behavior, traversal clearance, route validation, nav gate, collision correctness claim, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachStandingPair_A01#BrokenPair_A01` | Broken pair | `KIT_GIA_BloodAxeBrokenCaveStandingPair_A01` | planned | Static broken pair with one upright slab and one snapped, shortened, or fallen companion stone. Visual history only; no destructible state, puzzle state, objective frame, encounter trigger, interaction target, physics behavior, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachStandingPair_A01#ClothTiedPair_A01` | Cloth-tied pair | `KIT_GIA_BloodAxeClothTiedCaveStandingPair_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeClothTiedCaveStandingPair_A01/PRODUCTION_PACKAGE.md` is ready for a pair variant focused on broad static oxide red cloth, rawhide lashings, and thick Giant-tied knots at readable height. Static Blood Axe accent only; no cloth simulation, wind sway, UI marker, quest pointer, objective cue, material pulse, VFX/audio, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachStandingPair_A01#LowChockStonesBase_A01` | Low chock stones/base | `SM_GIA_BloodAxeCaveStandingPairChockStoneBase_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeCaveStandingPairChockStoneBase_A01/PRODUCTION_PACKAGE.md` is ready as a reusable support set for a few large wedge stones, buried base forms, mud pads, cold ash pads, cave grit, and contact-shadow grounding beneath paired standing stones. Grounding support only; no route blocker, collision correctness claim, terrain integration proof, cave compatibility proof, interaction behavior, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachStandingPair_A01#SpacingReviewRow_A01` | Spacing review row | `DOC_GIA_BloodAxeCaveApproachStandingPairSpacingReview_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachStandingPairSpacingReview_A01/PRODUCTION_PACKAGE.md` is ready for non-shipping review rows comparing visual gaps, tall/short height rhythm, cloth density, base footprint, and readability beside female 442 cm and male 470 cm Giant baselines. No gameplay lane, path-width promise, nav/pathfinding value, encounter spacing, trigger size, validator, capture, Unreal actor, startup placement, final approval, or implementation target. |
| `BloodAxeCaveApproachStandingPair_A01#MaterialDisciplineReference_A01` | Material discipline reference | `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01` | reference-only | Use the material discipline package for rough highland stone, soot, ash, cave grit, trampled mud, oxide red cloth, rope, rawhide, blackened iron, old horn, and dull bone. This row excludes neutral/civilized Giant culture, default emissive, material instance creation, texture creation, material graph authoring, VFX/audio, DCC, FBX, Unreal, final color approval, final visual approval, and first implementation target. |
| `BloodAxeCaveApproachStandingPair_A01#LODCollisionReference_A01` | LOD/collision reference | `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01` | reference-only | Use as a future documentation reference for LOD0-LOD3 reduction order and disabled/simple collision policy across standing-pair variants. This row does not create collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, objective volumes, validators, DCC, FBX, Unreal Content, runtime implementation, final approval, or first implementation target. |

## Dependency Notes

- `SK_GIA_Base_A01` owns Giant scale. This intake repeats the female 442 cm and male 470 cm baselines for standing-pair scale comparison but does not change race scale, sockets, skeleton policy, collision capsules, or character proportions.
- `KIT_GIA_BloodAxeCaveApproachMarkers_A01` owns the broader cave approach marker planning kit. This package is a child lane for static paired standing-stone cave-threshold visual framing only.
- `SM_GIA_BloodAxeCaveApproachStandingPair_A01` owns the single static prop restraint. This kit uses it as context while adding variant and reference rows.
- `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01` owns the shared material policy for rough highland stone, soot, ash, cave grit, trampled mud, oxide red cloth, rope, rawhide, blackened iron, old horn, and dull bone.
- No row in this table is approved as a first source asset, DCC, FBX, Unreal, runtime, gameplay, final cave, final visual, or implementation target.

## Unordered Future Package Candidates

No first DCC target, source asset target, Unreal target, runtime target, gameplay target, or implementation target is selected by this intake. If a later lead-approved package lane is opened, these may be promoted independently:

- `KIT_GIA_BloodAxeLeaningCaveStandingPair_A01`
- `KIT_GIA_BloodAxeBrokenCaveStandingPair_A01`
- `KIT_GIA_BloodAxeClothTiedCaveStandingPair_A01`
- `SM_GIA_BloodAxeCaveStandingPairChockStoneBase_A01`
- `DOC_GIA_BloodAxeCaveApproachStandingPairSpacingReview_A01`
- `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01`

## Approval Gates

- Stop before DCC source, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content asset, material instance, texture asset, material graph, import script, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, startup placement, or any source asset creation.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before selecting a first DCC, FBX, Unreal, source asset, runtime, gameplay, or implementation target from any row.
- Stop before functional doorway behavior, cave gameplay, traversal proof, path widths as gameplay values, nav/pathfinding, route validation, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, UI arrows, spawn logic, patrol logic, AI spaces, damage values, aura behavior, projectile behavior, cover rules, trap behavior, destructible behavior, loot, inventory, rewards, crafting, economy, resource behavior, salvage, pickup behavior, VFX, audio, or material-state animation.
- Stop before claiming collision correctness, cave compatibility, terrain integration, runtime performance validation, marker validation, final silhouette approval, final cave approval, final Blood Axe approval, final Giant culture approval, or final visual approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, VFX/audio asset, global index, task board, backlog, bootstrap, or unrelated package file.
- Rows cover primary pair context, leaning pair, broken pair, cloth-tied pair, low chock stones/base, spacing review row, material discipline reference, and LOD/collision reference.
- Every row is marked only `package-needed`, `planned`, or `reference-only`; no row claims permission to proceed to DCC, FBX, Unreal, final approval, implementation, or first target selection.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5"; approved ranges remain females 14-15 ft and males 14'10"-16'0".
- Standing pairs remain static cave-threshold visual framing only.
- No functional doorway behavior, cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, path widths as gameplay values, VFX/audio, DCC, FBX, Unreal, source asset creation, startup placement, final visual approval, final cave approval, or first implementation target is defined.
- Review rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, marker validation, camera approval, or final visual signoff.
- Materials use rough highland stone, soot, ash, trampled mud, cave grit, oxide red cloth, rope, rawhide, blackened iron, old horn, and dull bone consistently.
- Default emissive, glow, animated material states, gameplay VFX, UI-like markers, readable text, and neutral/civilized Giant language are absent and approval-gated.
- Tiny stone chips, cloth weave, fray, scratches, pitting, soot speckles, ash flecks, paint chips, horn rings, bone pores, lichen, mud streaks, and rope fibers are assigned to textures or normals in future packages.
