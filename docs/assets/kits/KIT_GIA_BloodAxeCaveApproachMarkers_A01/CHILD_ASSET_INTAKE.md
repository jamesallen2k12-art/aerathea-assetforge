# KIT_GIA_BloodAxeCaveApproachMarkers_A01 Child Asset Intake

## Source

- Parent backlog row: `Blood Axe Nomad Ritual Stones`
- Parent package: `KIT_GIA_BloodAxeRitualStones_A01`
- Current package: `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- Related package: `KIT_GIA_BloodAxeCairnGuideposts_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only planning child breakdown; no row may proceed to DCC, FBX, Unreal, startup placement, runtime work, final approval, or first implementation target selection
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture
- Scale dependency: Giant scale lock from `SK_GIA_Base_A01` uses female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges remain females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: external source concepts remain external. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This intake splits `KIT_GIA_BloodAxeCaveApproachMarkers_A01` into planning-only child rows for low threshold cairns, paired standing stones, cave remnant clusters, red cloth threshold markers, review rows, material discipline, and LOD/collision planning.

The kit is static threshold readability only. Rows may describe how a cave edge, cliff opening, or abandoned shelter threshold reads visually, but they must not define cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, route validation, path widths as gameplay values, spawn logic, patrol logic, damage/aura behavior, VFX/audio, DCC, FBX, Unreal, startup placement, final approval, or first implementation target selection.

Blood Axe cave approach dressing must stay separate from neutral/civilized Giant culture. It may use rough highland stone, soot, ash, trampled mud, cave grit, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, and dull bone. It must not use refined Giant cave-town masonry, blue-gray civic stonework, terrace/waterwork forms, warm hearth identity, peaceful highland wayfinding, carved civic ornament, or restrained blue-rune culture as the default read.

Every row below is marked `package-needed`, `planned`, or `reference-only`. No row creates or authorizes source assets, DCC, FBX, Unreal Content, runtime source, tools, validators, material instances, textures, VFX/audio, startup placement, source concept movement, final visual approval, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeCaveApproachMarkers_A01#LowThresholdCairn_Primary_A01` | Low threshold cairns | `SM_GIA_BloodAxeLowThresholdCairn_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeLowThresholdCairn_A01/PRODUCTION_PACKAGE.md` is ready for a single squat cairn made from a few large stones, cold ash, soot, cave grit, and optional restrained red cloth. Static threshold readability only; no cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI marker, encounter trigger, objective marker, interaction behavior, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#LowThresholdCairn_Paired_A01` | Low threshold cairns | `KIT_GIA_BloodAxeLowThresholdCairns_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeLowThresholdCairns_A01/PRODUCTION_PACKAGE.md` and `CHILD_ASSET_INTAKE.md` are ready for paired low cairn threshold rhythm. Visual framing only; no gate behavior, route validation, path-width rule, nav/pathfinding, encounter lane, quest pointer, collision guarantee, DCC, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#LowThresholdCairn_Collapsed_A01` | Low threshold cairns | `SM_GIA_BloodAxeCollapsedThresholdCairn_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeCollapsedThresholdCairn_A01/PRODUCTION_PACKAGE.md` is ready for a weathered collapsed cairn with shifted large stones and low ash base. Static abandoned remnant only; no destruction, physics, pickup, interaction, traversal proof, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#PairedStandingStones_Primary_A01` | Paired standing stones | `KIT_GIA_BloodAxeCaveApproachStandingPair_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachStandingPair_A01/PRODUCTION_PACKAGE.md` and `CHILD_ASSET_INTAKE.md` are ready for asymmetric tall/short standing-stone pair variants that frame a visual threshold without becoming a functional doorway, objective frame, nav gate, encounter trigger, interaction target, DCC target, Unreal target, final cave approval, final visual approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#PairedStandingStones_Leaning_A01` | Paired standing stones | `KIT_GIA_BloodAxeLeaningCaveStandingPair_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeLeaningCaveStandingPair_A01/PRODUCTION_PACKAGE.md` is ready for leaning paired stones with broad chipped planes and old cloth ties. Static visual history only; no collision correctness, traversal clearance, route validation, readable text, VFX, DCC, FBX, Unreal, startup placement, final cave approval, final visual approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#PairedStandingStones_Broken_A01` | Paired standing stones | `KIT_GIA_BloodAxeBrokenCaveStandingPair_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeBrokenCaveStandingPair_A01/PRODUCTION_PACKAGE.md` is ready for a broken pair with one standing stone and one snapped or fallen companion stone. Static memory marker only; no destructible state, puzzle state, objective marker, trigger volume, interaction behavior, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#CaveRemnantCluster_Primary_A01` | Cave remnant clusters | `KIT_GIA_BloodAxeCaveRemnantCluster_A01` | package-needed | Mixed low cairn, broken slab, ash base, rope, and sparse horn or dull bone arranged as old cave-edge dressing. No encounter behavior, spawn marker, patrol point, damage/aura, nav/pathfinding, route scripting, DCC, Unreal, startup placement, or final visual approval. |
| `BloodAxeCaveApproachMarkers_A01#CaveRemnantCluster_AshBase_A01` | Cave remnant clusters | `SM_GIA_BloodAxeCaveAshRemnantBase_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeCaveAshRemnantBase_A01/PRODUCTION_PACKAGE.md` is ready for low cold ash, soot, mud, and cave grit base supporting static markers. Ground dressing only; no decal gameplay, trigger area, damage field, aura, objective zone, collision claim, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#CaveRemnantCluster_BrokenSlabs_A01` | Cave remnant clusters | `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01/PRODUCTION_PACKAGE.md` and `CHILD_ASSET_INTAKE.md` are ready for broken threshold slab clusters with broad stone masses and chipped red paint. Static visual history only; no cave compatibility proof, traversal proof, route blocker, interaction, DCC, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#RedClothThresholdMarker_Tied_A01` | Red cloth threshold markers | `SM_GIA_BloodAxeRedClothThresholdMarker_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeRedClothThresholdMarker_A01/PRODUCTION_PACKAGE.md` is ready for broad oxide red cloth tied to stone, short stake, or rope binding. Static Blood Axe accent only; no flag animation, wind simulation, UI marker, quest pointer, objective marker, VFX/audio, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#RedClothThresholdMarker_Draped_A01` | Red cloth threshold markers | `SM_GIA_BloodAxeDrapedThresholdCloth_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeDrapedThresholdCloth_A01/PRODUCTION_PACKAGE.md` is ready for a static draped cloth band over a low stone or slab, with faded red and soot wear. Static dressing only; no cloth simulation, interaction behavior, readable signage, objective cue, material pulse, DCC, Unreal, startup placement, final visual approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#RedClothThresholdMarker_PaintOnly_A01` | Red cloth threshold markers | `SM_GIA_BloodAxePaintedThresholdStone_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxePaintedThresholdStone_A01/PRODUCTION_PACKAGE.md` is ready for a stone marker variant using chipped dirty red paint instead of cloth where cloth density would be too high. Static texture-led marker only; no readable text, UI arrow, quest symbol, magic glyph, emissive map, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#ReviewRows_ScaleReadability_A01` | Review rows | `DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01/PRODUCTION_PACKAGE.md` is ready for non-shipping scale rows showing low cairns, paired stones, remnant clusters, and red cloth markers beside female 442 cm and male 470 cm Giant baselines. No DCC, Unreal actor, validator, capture, startup placement, final visual approval, or implementation target. |
| `BloodAxeCaveApproachMarkers_A01#ReviewRows_ThresholdRhythm_A01` | Review rows | `DOC_GIA_BloodAxeCaveApproachThresholdRhythmRows_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachThresholdRhythmRows_A01/PRODUCTION_PACKAGE.md` is ready for non-shipping rows comparing threshold density, paired-stone spacing, low cairn rhythm, red cloth restraint, and cave-edge readability. No cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI marker, encounter trigger, objective marker, DCC, Unreal, or startup placement. |
| `BloodAxeCaveApproachMarkers_A01#MaterialDiscipline_A01` | Material discipline | `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01/PRODUCTION_PACKAGE.md` is ready as shared material discipline for rough highland stone, soot, ash, cave grit, trampled mud, oxide red cloth, rope, rawhide, blackened iron, old horn, and dull bone. Excludes neutral/civilized Giant culture, default emissive, material instance creation, texture creation, material graph authoring, VFX/audio, DCC, FBX, Unreal, final color approval, or first implementation target. |
| `BloodAxeCaveApproachMarkers_A01#LODCollisionPlanning_A01` | LOD/collision planning | `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01/PRODUCTION_PACKAGE.md` is ready as docs-only LOD0-LOD3 reduction order and disabled/simple collision policy for future static cave approach modules and review rows. No collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, objective volumes, validators, DCC, FBX, Unreal Content, or runtime implementation. |
| `BloodAxeCaveApproachMarkers_A01#Reference_CairnGuidepostDiscipline_A01` | Material and silhouette reference | `KIT_GIA_BloodAxeCairnGuideposts_A01` | reference-only | Use the cairn guidepost package as a restraint reference for few-large-stones construction, oxide red cloth restraint, and route-edge visual memory. This row does not create new assets, implementation order, DCC, Unreal, startup placement, or final approval. |

## Dependency Notes

- `SK_GIA_Base_A01` owns Giant scale. This intake repeats the female 442 cm and male 470 cm baselines for marker scale comparison but does not change race scale, sockets, skeleton policy, collision capsules, or character proportions.
- `KIT_GIA_BloodAxeRitualStones_A01` owns the broader ritual-stone planning kit. This cave approach package is a child lane for static threshold readability only.
- `KIT_GIA_BloodAxeCairnGuideposts_A01` owns general cairn guidepost discipline. Cave approach cairns should share its few-large-stones restraint while reading lower, threshold-focused, and older.
- No row in this table is approved as a first DCC, FBX, Unreal, runtime, source asset, gameplay, final visual, final cave, or implementation target.

## Unordered Future Package Candidates

No first DCC target, source asset target, Unreal target, runtime target, gameplay target, or implementation target is selected by this intake. If a later lead-approved package lane is opened, these may be promoted independently:

- `SM_GIA_BloodAxeLowThresholdCairn_A01`
- `KIT_GIA_BloodAxeLowThresholdCairns_A01`
- `KIT_GIA_BloodAxeCaveApproachStandingPair_A01`
- `KIT_GIA_BloodAxeLeaningCaveStandingPair_A01`
- `KIT_GIA_BloodAxeBrokenCaveStandingPair_A01`
- `KIT_GIA_BloodAxeCaveRemnantCluster_A01`
- `SM_GIA_BloodAxeCaveAshRemnantBase_A01`
- `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01`
- `SM_GIA_BloodAxeRedClothThresholdMarker_A01`
- `SM_GIA_BloodAxeDrapedThresholdCloth_A01`
- `SM_GIA_BloodAxePaintedThresholdStone_A01`
- `DOC_GIA_BloodAxeCaveApproachReviewRows_A01`
- `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01`
- `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01`

## Approval Gates

- Stop before DCC source, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content asset, material instance, texture asset, material graph, import script, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, startup placement, or any source asset creation.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before selecting a first DCC, FBX, Unreal, source asset, runtime, gameplay, or implementation target from any row.
- Stop before cave gameplay, traversal proof, path widths as gameplay values, nav/pathfinding, route validation, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, UI arrows, spawn logic, patrol logic, AI spaces, damage values, aura behavior, projectile behavior, cover rules, trap behavior, destructible behavior, loot, inventory, rewards, crafting, economy, resource behavior, salvage, pickup behavior, VFX, audio, or material-state animation.
- Stop before claiming collision correctness, cave compatibility, terrain integration, runtime performance validation, marker validation, final silhouette approval, final cave approval, final Blood Axe approval, final Giant culture approval, or final visual approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, VFX/audio asset, global index, task board, backlog, bootstrap, or unrelated package file.
- Rows cover low threshold cairns, paired standing stones, cave remnant clusters, red cloth threshold markers, review rows, material discipline, and LOD/collision planning.
- Every row is marked `package-needed`, `planned`, or `reference-only`; no row claims permission to proceed to DCC, FBX, Unreal, final approval, implementation, or first target selection.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Cave approach markers remain static threshold readability only.
- No cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, path widths as gameplay values, VFX/audio, DCC, FBX, Unreal, source asset creation, startup placement, or final visual approval is defined.
- Review rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, marker validation, camera approval, or final visual signoff.
- Materials use rough highland stone, soot, ash, trampled mud, cave grit, oxide red cloth, rope, rawhide, blackened iron, old horn, and dull bone consistently.
- Default emissive, glow, animated material states, gameplay VFX, UI-like markers, readable text, and neutral/civilized Giant language are absent and approval-gated.
- Tiny stone chips, cloth weave, fray, scratches, pitting, soot speckles, ash flecks, paint chips, horn rings, lichen, mud streaks, and rope fibers are assigned to textures or normals in future packages.
