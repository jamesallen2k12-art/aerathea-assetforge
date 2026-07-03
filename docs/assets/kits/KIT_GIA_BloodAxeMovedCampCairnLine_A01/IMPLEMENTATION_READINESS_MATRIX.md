# KIT_GIA_BloodAxeMovedCampCairnLine_A01 Implementation Readiness Matrix

## Scope

- Task: `AET-MA-20260629-463`
- Scope type: docs-only implementation readiness matrix.
- Owned file: `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/IMPLEMENTATION_READINESS_MATRIX.md`
- Source parent package: `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/PRODUCTION_PACKAGE.md`
- Source child intake: `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/CHILD_ASSET_INTAKE.md`
- Source index rows: `docs/assets/ASSET_INDEX.md` rows for `KIT_GIA_BloodAxeMovedCampCairnLine_A01`, all moved-camp cairn-line children, policy rows, and review rows.

This matrix classifies the moved-camp cairn-line package set by documentation readiness and remaining blockers. It does not select a first implementation target, implementation order, source folder, DCC target, Unreal target, validator target, startup placement, final camp-route approval target, or final visual approval target.

## Source Of Truth References

- `KIT_GIA_BloodAxeMovedCampCairnLine_A01` parent package and child intake are the immediate source of truth for this matrix.
- `KIT_GIA_BloodAxeRitualStones_A01` is the parent ritual-stone planning source and owns the original moved-camp cairn-line child row.
- `KIT_GIA_BloodAxeCairnGuideposts_A01` provides related cairn guidepost language; this matrix preserves the moved-camp kit as older, sparser, and less directive.
- `SM_GIA_BloodAxeRitualCairnGuidepost_A01` anchors the single static cairn guidepost material and silhouette language; this matrix keeps the moved-camp line more collapsed and abandoned.
- `KIT_GIA_BloodAxePathMarkers_A01` owns broader Blood Axe path-marker dressing; this matrix blocks the moved-camp cairn line from becoming a path, route, waypoint, or tracking system.
- `SK_GIA_Base_A01` is the validated Giant scale dependency.

## Scale And Culture Lock

- Giant scale lock: female baseline 442 cm / 14'6"; male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Future work, if separately assigned outside this matrix, must preserve centimeter scale with 1 Unreal unit = 1 cm.
- Blood Axe is a hostile Giant sub-faction only.
- Blood Axe is a hostile Giant sub-faction only and must not replace neutral/civilized Giant culture, cave-town masonry, blue-gray civic stonework, terraces/waterworks, warm hearth settlement identity, peaceful highland markers, or restrained blue rune culture.
- Moved-camp cairn-line dressing may use rough highland stone, soot, ash, trampled mud, burned grass, oxide red cloth, rawhide ties, rope lashings, sparse blackened iron, old horn, and aged bone.
- Neutral/civilized Giant culture remains separate: cave-town masonry, blue-gray civic stonework, terraces/waterworks, warm hearth settlement identity, peaceful highland markers, restrained blue rune culture, hidden highland settlement polish, and civic stoneworker identity are not Blood Axe defaults.

## Readiness Key

- `Package-ready`: production package exists or is recorded as ready in the source intake/index and can be referenced by a later separately approved lane; implementation remains blocked.
- `Policy-ready`: docs-only material, LOD, collision, or review policy exists for consistency; it is not a buildable mesh target.
- `Review-only`: package supports non-shipping comparison rows; it does not create an Unreal actor, validator, capture, startup placement, final visual approval, or route approval.
- `Implementation blocked`: no source folder, DCC source, FBX export, Unreal Content, runtime source, validator file, startup placement, material instance, texture asset, final approval, first implementation target, or implementation order exists.

## Child-Intake Readiness Matrix

| Child intake row | Package/review/policy ID | Source status | Package readiness | Art/scale guardrails | Material/LOD/collision guardrails | Blocked implementation decisions | Validator gaps | Approval gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BloodAxeRitualStones_A01#MovedCamp_CairnLineSparseSegment_A01` | `KIT_GIA_BloodAxeMovedCampSparseCairnSegment_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Short broken span of 2-4 low cairn remnants with uneven spacing, missing beats, cold ash, trampled mud, and Giant scale lock | Preserve few large stones, broad ash/mud base, LOD0-LOD3 expectation, collision disabled by default | No source folder, DCC target, Unreal target, route, waypoint, spawn guide, patrol guide, or first target selection | Later validators must check scale, spacing irregularity, no path read, material restraint, and collision policy; validator target unselected | Future lane needs separate visual/source approval; final camp-route approval blocked |
| `BloodAxeRitualStones_A01#MovedCamp_CairnLineSparseSegment_B01` | `KIT_GIA_BloodAxeMovedCampSparseCairnSegment_B01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Wider sparse span with one dominant collapsed cairn, one low support pile, long empty ash gap, and no guide-line read | Keep ash gap flat and non-directional; preserve material slot restraint and LOD reduction order | No traversal hint, waypoint chain, UI path, source folder, DCC, Unreal, or implementation order | Later validators must check no guide line, no traversal cue, scale, material palette, and LOD/collision limits | Separate approval required before any source or visual implementation claim |
| `BloodAxeRitualStones_A01#MovedCamp_CairnLineCollapsedEnd_A01` | `SM_GIA_BloodAxeMovedCampCollapsedLineEnd_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Final-looking broken end with stones sliding into mud and cloth partly buried; must not imply destination or route completion | Model future large stones and broad cloth only; small wear stays texture/normal detail; collision disabled or simple only if separately approved | No endpoint, objective, portal clue, trigger, startup placement, Unreal asset, or first implementation target | Later validators must check no endpoint language, no objective read, no portal/trigger affordance, scale, and collision limits | Final visual approval and final camp-route approval blocked |
| `BloodAxeRitualStones_A01#MovedCamp_BrokenMemoryCluster_A01` | `KIT_GIA_BloodAxeMovedCampBrokenMemoryCluster_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | One collapsed cairn, two displaced stones, low soot, old lashings, abandoned Blood Axe memory read | Use rough stone, soot, ash, rawhide; preserve chunky cluster silhouette; no per-stone collision | No loot, salvage, interaction, ritual activation, DCC target, Unreal target, or source folder | Later validators must check non-interactive read, Blood Axe material language, LOD0-LOD3, and collision-disabled defaults | Separate source/art approval required before any build lane |
| `BloodAxeRitualStones_A01#MovedCamp_BrokenMemoryCluster_B01` | `KIT_GIA_BloodAxeMovedCampBrokenMemoryCluster_B01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Wider cluster with short stake remnant and one trapped cloth strip; no readable text or signal behavior | Cloth remains static and subordinate; no emissive; no active material state; collision disabled on cloth/rope/scraps | No faction buff, AI marker, gameplay state, Blueprint, socket authoring, material graph, or implementation order | Later validators must check no signal/faction/gameplay read, static cloth, red restraint, and scale | Final visual approval and runtime behavior blocked |
| `BloodAxeRitualStones_A01#MovedCamp_LowCairnRemnant_A01` | `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Single low remnant, 60-180 cm tall, sized against female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5" | One material target; LODs preserve primary low-cairn mass; no collision correctness claim | No pickup behavior, gameplay behavior, collision proxy, Unreal Content, or first target selection | Later validators must check dimensions, material count, disabled/simple collision, and no pickup affordance | Separate DCC/Unreal approval required |
| `BloodAxeRitualStones_A01#MovedCamp_AshGap_A01` | `SM_GIA_BloodAxeMovedCampAshGap_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Flat cold ash and trampled mud between remnants; ground residue only | Matte ash/mud, one material target, collision disabled, no VFX/audio or hazard state | No decal trail behavior, damage field, aura field, gatherable ash, route validation, DCC, or Unreal target | Later validators must check no route read, no hazard read, no gatherable affordance, and collision disabled | Final camp-route approval and final Blood Axe ritual approval blocked |
| `BloodAxeRitualStones_A01#MovedCamp_AshGapBrokenRing_A01` | `SM_GIA_BloodAxeMovedCampBrokenAshRing_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Incomplete ash-dark footprint from old camp fire or stone cluster; broken open shape must not read as objective ring | Keep ash ring irregular, flat, and non-emissive; no gameplay volume or ritual boundary collision | No interaction prompt, ritual boundary, gameplay area, VFX state, Unreal Content, or material instance | Later validators must check incomplete ring read, no objective marker, no VFX, no collision volume, and scale | Separate visual approval required before any implementation claim |
| `BloodAxeRitualStones_A01#MovedCamp_AshGapMudScuff_A01` | `SM_GIA_BloodAxeMovedCampMudScuff_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Broad low mud and soot scuff separating cairn beats; not footprints or travel instructions | Use mud/soot roughness, low profile, one material target, collision disabled | No tracking mechanic, route validation, source folder, DCC, Unreal, startup placement, or first target selection | Later validators must check no footprint chain, no readable travel instruction, material restraint, and collision disabled | Route/tracking approval blocked |
| `BloodAxeRitualStones_A01#MovedCamp_ClothRemnantStoneTie_A01` | `SM_GIA_BloodAxeMovedCampClothStoneTie_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Fixed oxide red cloth tied around or trapped under a low cairn stone; red accent must stay subordinate | Static broad cloth; no cloth simulation, wind, emissive, or unique material sprawl; collision disabled | No UI color coding, faction buff, readable message, interaction behavior, physics setup, or animation asset | Later validators must check static cloth, no UI marker read, no interaction affordance, and material slot limits | Final visual approval and runtime interaction blocked |
| `BloodAxeRitualStones_A01#MovedCamp_ClothRemnantBuriedStrip_A01` | `SM_GIA_BloodAxeMovedCampBuriedClothStrip_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Weathered cloth strip partially buried in ash and mud; old Blood Axe residue only | Cloth/ash/mud share restrained material language; small fray stays texture/normal; collision disabled | No breadcrumb, clickable object, pickup, objective marker, DCC target, Unreal target, or implementation order | Later validators must check no breadcrumb/objective read, static cloth, red restraint, and no pickup collision | Separate approval required before any source or engine work |
| `BloodAxeRitualStones_A01#MovedCamp_ShortStakeRemnant_A01` | `SM_GIA_BloodAxeMovedCampShortStakeRemnant_A01` | Source intake and ASSET_INDEX row recorded; docs-only source status | Package-ready; implementation blocked | Short scorched stake or splintered post with one cloth scrap and rawhide tie; smaller than banner-line assets | Model broad stake/cloth forms only; no active signal material; LODs simplify ties before silhouette | No active signal, route flag, banner-line promotion, UI marker, socket, Blueprint, or startup placement | Later validators must check subordinate height, no active marker read, material restraint, and disabled/simple collision | Final visual approval and route-flag approval blocked |
| `BloodAxeRitualStones_A01#MovedCamp_MaterialDiscipline_A01` | `DOC_GIA_BloodAxeMovedCampCairnLineMaterialDiscipline_A01` | Source intake and ASSET_INDEX row recorded; policy source only | Policy-ready; not a buildable mesh target | Locks hostile Blood Axe material read away from neutral/civilized Giant culture | Rough stone, soot, ash, mud, oxide red cloth, rawhide, rope, sparse blackened iron, old horn, aged bone; no default emissive | No material instance, texture asset, material graph, shader, VFX/audio, Unreal Content, or first material target | Later validators must check material palette, no emissive baseline, red restraint, and culture separation | Material implementation approval blocked |
| `BloodAxeRitualStones_A01#MovedCamp_LODCollisionPlanning_A01` | `DOC_GIA_BloodAxeMovedCampCairnLineLODAndCollision_A01` | Source intake and ASSET_INDEX row recorded; policy source only | Policy-ready; not a buildable mesh target | Preserves Giant-scale remnant read, broken/missing rhythm, abandoned-camp history, and Blood Axe red/black identity through LODs | LOD0-LOD3 required for shipping children; collision disabled by default except separately approved simple broad hulls | No LOD source, collision proxy, UCX mesh, nav blocker, gameplay volume, validator file, DCC, or Unreal Content | Later validators must check LOD presence, reduction order, collision disabled/simple policy, and no gameplay volumes | Collision correctness and LOD source approval blocked |
| `BloodAxeRitualStones_A01#ReviewOnly_MovedCampSpacingRows_A01` | `DOC_GIA_BloodAxeMovedCampCairnLineReviewRows_A01` | Source intake and ASSET_INDEX row recorded; review-only source | Review-only; non-shipping planning row | Compare interrupted spacing, missing beats, collapse density, camera readability, and female/male Giant baselines | Review row is not an asset target; no collision, material instance, texture asset, or LOD source | No Unreal actor, validator, capture, startup placement, final visual signoff, route approval, or first target selection | Later validators, if separately assigned, must check review-only status and no route approval claim | Review/capture/startup approval blocked |
| `BloodAxeRitualStones_A01#ReviewOnly_MovedCampAshGapRows_A01` | `DOC_GIA_BloodAxeMovedCampCairnLineReviewRows_A01` | Source intake and ASSET_INDEX row recorded; review-only source | Review-only; non-shipping planning row | Compare ash gaps, mud scuffs, and low residue between cairn remnants; must not imply footprints or navigation | No material graph, VFX, collision, gameplay volume, DCC source, or Unreal Content from this matrix | No tracking UI, navigation line, objective ring, encounter lane, validator target, or startup placement | Later validators must check no tracking/navigation/objective read and no shipped asset claim | Route, tracking, and final visual approvals blocked |
| `BloodAxeRitualStones_A01#ReviewOnly_MovedCampClothRows_A01` | `DOC_GIA_BloodAxeMovedCampCairnLineReviewRows_A01` | Source intake and ASSET_INDEX row recorded; review-only source | Review-only; non-shipping planning row | Compare cloth-remnant restraint, color balance, and Blood Axe identity at MMO camera distance | Static cloth review only; no cloth simulation, no material instance, no texture asset, no collision setup | No active signal, UI marker, banner-line promotion, DCC, Unreal, implementation order, or first target selection | Later validators must check red accent restraint, no signal/readability overclaim, and review-only status | Final visual approval and implementation target approval blocked |

## Unique Package And Policy Coverage

The matrix covers all 15 unique package/review/policy IDs required by the child intake and ASSET_INDEX rows:

- `KIT_GIA_BloodAxeMovedCampSparseCairnSegment_A01`
- `KIT_GIA_BloodAxeMovedCampSparseCairnSegment_B01`
- `SM_GIA_BloodAxeMovedCampCollapsedLineEnd_A01`
- `KIT_GIA_BloodAxeMovedCampBrokenMemoryCluster_A01`
- `KIT_GIA_BloodAxeMovedCampBrokenMemoryCluster_B01`
- `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- `SM_GIA_BloodAxeMovedCampAshGap_A01`
- `SM_GIA_BloodAxeMovedCampBrokenAshRing_A01`
- `SM_GIA_BloodAxeMovedCampMudScuff_A01`
- `SM_GIA_BloodAxeMovedCampClothStoneTie_A01`
- `SM_GIA_BloodAxeMovedCampBuriedClothStrip_A01`
- `SM_GIA_BloodAxeMovedCampShortStakeRemnant_A01`
- `DOC_GIA_BloodAxeMovedCampCairnLineMaterialDiscipline_A01`
- `DOC_GIA_BloodAxeMovedCampCairnLineLODAndCollision_A01`
- `DOC_GIA_BloodAxeMovedCampCairnLineReviewRows_A01`

## DCC Readiness Preconditions

A later DCC lane must explicitly approve and own all of the following before any source work begins:

- Exact source scope and export scope; neither is selected here.
- Chosen DCC target or targets; none are selected here.
- Per-child module split, mesh naming, pivot, orientation, centimeter scale proof, and scale comparison against female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5".
- LOD0-LOD3 source expectations and reduction order from `DOC_GIA_BloodAxeMovedCampCairnLineLODAndCollision_A01`.
- Material-slot discipline from `DOC_GIA_BloodAxeMovedCampCairnLineMaterialDiscipline_A01`.
- Static-shape policy for cloth, rope, ash, mud, stone, stake remnants, old horn, aged bone, and sparse blackened iron.
- Culture-separation review against neutral/civilized Giant cave-town and peaceful highland marker language.
- Review artifact plan that remains non-final until separate visual approval exists.

## Unreal Readiness Preconditions

A later Unreal lane must explicitly approve and own all of the following before engine work begins:

- Import path, asset ownership, and file scope; none are selected here.
- Whether any row becomes a shipping static mesh, remains a docs-only package, or becomes a non-shipping review artifact; this matrix does not decide.
- Import scale proof at 1 Unreal unit = 1 cm.
- LOD0-LOD3 presence for any separately approved shipping static mesh candidate.
- Material instance and texture ownership, with no default emissive unless a separate active ritual or signal variant is approved.
- Disabled-by-default collision or a separately approved simple broad-hull exception.
- Focused validation plan owned by a future Unreal/QA task; no validator target is selected here.
- Any startup placement, review capture, marker pass, final visual approval, final camp-route approval, or final package implementation approval in separately assigned tasks only.

This matrix does not create Unreal Content, material instances, textures, Blueprints, sockets, collision proxies, validators, review actors, startup actors, runtime source, or Hermes work.

## Validator Gaps And Future Checks

No validator file is authored by this matrix. Future implementation lanes should add focused validators only when they own the affected docs, DCC, Unreal, or QA paths.

| Future lane | Validator need | Current status |
| --- | --- | --- |
| Package inventory | Confirm all 17 child-intake rows and 15 unique package/review/policy IDs remain represented | Gap documented; validator target unselected |
| Giant scale | Confirm female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", and approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm | Gap documented; validator target unselected |
| Culture separation | Confirm Blood Axe is a hostile Giant sub-faction only and does not replace neutral/civilized Giant culture | Gap documented; validator target unselected |
| DCC source/export | Confirm source scope, export scope, centimeters, pivots, dimensions, LOD0-LOD3 source, material slots, and no micro-detail geometry misuse | Gap documented; source target unselected |
| Unreal import | Confirm import path, scale, LODs, material slots, disabled/simple collision, texture references, no Blueprint, and no gameplay marker logic | Gap documented; Unreal target unselected |
| Material validation | Confirm rough stone, soot, ash, mud, oxide red cloth, rawhide, rope, sparse blackened iron, old horn, aged bone, no default emissive, and no civic Giant material drift | Gap documented; material target unselected |
| Collision validation | Confirm collision disabled by default or separately approved simple broad hulls only; no nav blockers, gameplay volumes, trigger volumes, pickup volumes, route volumes, damage volumes, or aura volumes | Gap documented; collision target unselected |
| Route/gameplay guardrail | Confirm no functional trail, route, waypoint chain, breadcrumb, tracking mechanic, UI path, spawn guide, patrol guide, encounter lane, objective line, quest marker, or final camp-route approval claim | Gap documented; gameplay target unselected |
| Source-storage | Confirm external concept art was not copied, embedded, moved, edited, renamed, inspected for final approval, or committed | Gap documented; source-storage target unselected |
| Matrix maintenance | Confirm no first implementation target, implementation order, source folder, DCC target, Unreal target, validator target, startup placement, final camp-route approval target, or final visual approval target is selected | Gap documented; maintenance target unselected |

## Global Stop Gates

- No-route guardrail: Stop before functional trail, route, waypoint chain, breadcrumb, tracking mechanic, UI path, spawn guide, patrol guide, encounter lane, objective line, quest marker, final camp-route approval.
- No-build guardrail: Stop before DCC source, source-folder creation, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content, material instance, texture asset, validator file, startup placement, runtime source, Blueprint, socket authoring, physics setup, animation asset, material graph, VFX/audio, final visual approval, first implementation target selection, Hermes work.
- No-target-selected guardrail: Stop before source folder creation, DCC target selection, Unreal target selection, validator target selection, startup placement selection, implementation order selection, package implementation target selection, or final approval target selection.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing external source concept files.
- Stop before waypoint behavior, breadcrumb behavior, tracking mechanic, UI path, objective logic, navigation behavior, interaction behavior, pickup/loot behavior, resource behavior, crafting/economy behavior, faction buff behavior, AI behavior, patrol logic, spawn logic, encounter scripting, cover behavior, damage volumes, aura volumes, VFX, audio, destructible behavior, physics collapse, route gameplay, or runtime behavior.
- Stop before claiming collision correctness, runtime performance validation, camera approval, marker validation, final camp-route approval, final Blood Axe ritual approval, final Giant culture approval, or final visual approval.
- Stop if Blood Axe hostile raider identity starts replacing neutral/civilized Giant culture, cave-town masonry, blue-gray civic stonework, terraces/waterworks, warm hearth settlement identity, peaceful highland markers, or restrained blue rune culture.
- Stop if any row changes the Giant scale lock from female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", or approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.

## Matrix Maintenance Validation

Use these docs-only checks after edits to this matrix:

- File existence scan: confirm `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/IMPLEMENTATION_READINESS_MATRIX.md` exists.
- Matrix completeness scan: confirm all 17 child-intake rows and all 15 unique package/review/policy IDs are represented.
- Giant scale scan: confirm female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", and approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm remain present.
- Culture separation scan: confirm Blood Axe is a hostile Giant sub-faction only and neutral/civilized Giant culture remains explicitly separate.
- No-target-selected scan: confirm no first implementation target, implementation order, source folder, DCC target, Unreal target, validator target, startup placement, final camp-route approval target, or final visual approval target is selected.
- Guardrail scan: confirm docs-only, no DCC, no Unreal, no route, no waypoint, no tracking, no UI path, and no spawn/patrol guardrails remain present.
- Whitespace and diff validation: run `rg -n "[[:blank:]]$" docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/IMPLEMENTATION_READINESS_MATRIX.md` and `git diff --check -- docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/IMPLEMENTATION_READINESS_MATRIX.md`.

## Quality Gate Checklist

- Matrix is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, material graph, VFX/audio asset, global index, task board, backlog, bootstrap, child intake doc, source folder, image, unrelated package file, or production package.
- All 17 child-intake rows are represented in the readiness matrix, including the three separate review-only rows that share `DOC_GIA_BloodAxeMovedCampCairnLineReviewRows_A01`.
- All 15 unique package/review/policy IDs are represented.
- Source status, package readiness, art/scale guardrails, material/LOD/collision guardrails, blocked implementation decisions, validator gaps, and approval gates are present for each child-intake row.
- Giant scale lock is explicit: female baseline 442 cm / 14'6"; male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction only and stays separate from neutral/civilized Giant culture, cave-town masonry, blue-gray civic stonework, terraces/waterworks, warm hearth settlement identity, peaceful highland markers, and restrained blue rune culture.
- Package inventory does not imply build order, implementation order, source-folder selection, DCC target selection, Unreal target selection, validator target selection, startup placement, final camp-route approval, or final visual approval.
- Functional trail, route, waypoint chain, breadcrumb, tracking mechanic, UI path, spawn guide, patrol guide, encounter lane, objective line, quest marker, route gameplay, waypoint behavior, trail tracking, encounter behavior, AI behavior, VFX/audio, material-state behavior, cloth/physics, source asset creation, startup placement, and final approval are explicitly excluded.
- Source concept material remains external and is not copied, moved, edited, embedded, cropped, renamed, inspected for final approval, or committed.

## Non-Authorization Statement

This readiness matrix is a documentation artifact only. It authorizes no source folder, DCC target, implementation order, Blender work, mesh work, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content import, material instance, texture asset, material graph, runtime source, Blueprint, socket authoring, physics setup, animation asset, validator file, startup placement, final visual approval, final camp-route approval, Hermes work, or final Giant culture approval.
