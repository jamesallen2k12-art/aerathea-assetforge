# KIT_GIA_BloodAxeCairnGuideposts_A01 Child Asset Intake

## Source

- Parent planning source: future `KIT_GIA_BloodAxeRitualStones_A01` and current Blood Axe stronghold/camp approach packages
- Related existing package: `SM_GIA_BloodAxeApproachCairnMarker_A01`
- Related existing kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock with female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft and males 14'10"-16'0"
- Intake status: docs-only planning child breakdown
- Source-storage guardrail: do not copy, move, edit, embed, or commit external source concept images for this task

## Notes

This intake splits `KIT_GIA_BloodAxeCairnGuideposts_A01` into planning-only child rows. The kit owns low and mid-height cairn guideposts used as visual memory markers and route-edge dressing only. It does not own tall banner lines, objective signage, readable text, gameplay markers, neutral/civilized Giant culture, or final ritual-stone language.

Blood Axe cairn guideposts may use rough field stone, soot, ash, trampled mud, oxide red cloth, hide ties, rope lashings, blackened iron scraps, sparse horn, and aged bone. They must not use blue-gray civic masonry, refined cave-town carving, waterwork motifs, warm hearth settlement language, restrained blue runes, or peaceful highland trail markers from neutral/civilized Giant culture.

No child row selects a first implementation target. No row authorizes DCC, FBX, Unreal asset creation, startup placement, source folder creation, validator work, runtime behavior, readable text, waypoint behavior, quest logic, nav/pathfinding behavior, interaction behavior, objective markers, pickup behavior, loot behavior, resource behavior, VFX, audio, or final art signoff.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeRitualStones.png#Guideposts_SingleCairn_A01` | Single cairns | `SM_GIA_BloodAxeGuidepostCairnSingle_A01` | Package candidate; planning only | One crude Giant-built stack of 4-8 large stones, 100-220 cm tall, with soot and mud at the base. Visual memory marker only; no waypoint, quest, nav/pathfinding, readable text, interaction behavior, objective marker, DCC, FBX, Unreal, startup placement, or first implementation target selection. |
| `BloodAxeStronghold.png#Guideposts_SingleCairnLean_A01` | Single cairns | `SM_GIA_BloodAxeGuidepostCairnLeaning_A01` | Package candidate; planning only | Leaning cairn with one dominant tilted stone and a broad ash-dark base. Use for route-edge dressing only; not a pointer, sign, interactable, or gameplay marker. |
| `BloodAxeRitualStones.png#Guideposts_PairedCairns_A01` | Paired cairns | `KIT_GIA_BloodAxeGuidepostCairnPair_A01` | Package candidate; planning only | Uneven pair of cairns framing a rough edge or remembered passage without becoming a gate, objective frame, or pathfinding aid. Sized beside the 442 cm and 470 cm Giant baselines. |
| `BloodAxeStronghold.png#Guideposts_PairedCairnRouteEdge_A01` | Paired cairns | `KIT_GIA_BloodAxeGuidepostRouteEdgePair_A01` | Package candidate; planning only | Two separated cairns with staggered height, ash staining, and small cloth remnants for repeated route-edge rhythm. No trail gameplay, boundary logic, collision gate, or startup placement. |
| `BloodAxeRitualStones.png#Guideposts_ClothTiedStone_A01` | Cloth-tied guideposts | `SM_GIA_BloodAxeClothTiedStoneGuidepost_A01` | Package candidate; planning only | Single stone guidepost with broad oxide red cloth tied under a heavy capstone. Cloth is fixed visual geometry only; no cloth simulation, wind, UI color coding, or interaction prompt. |
| `BloodAxeCamp.png#Guideposts_ClothTiedStake_A01` | Cloth-tied guideposts | `SM_GIA_BloodAxeClothTiedStakeGuidepost_A01` | Package candidate; planning only | Short scorched timber or stone-and-stake hybrid with one or two large torn cloth strips. Keep it smaller than banner-line assets and separate from quest or waypoint language. |
| `BloodAxeRitualStones.png#Guideposts_AshBaseCairnFoot_A01` | Ash-stained bases | `SM_GIA_BloodAxeAshStainedGuidepostBase_A01` | Package candidate; planning only | Low ash, soot, charcoal, and trampled mud base used to ground single cairns, paired cairns, and cloth guideposts. Ground dressing only; no trail tracking, gatherable ash, damage field, decal gameplay, or VFX. |
| `BloodAxeStronghold.png#Guideposts_AshBaseSet_A01` | Ash-stained bases | `KIT_GIA_BloodAxeGuidepostAshBaseSet_A01` | Package candidate; planning only | Small set of varied low bases for old camp edges, switchback sides, and ritual-stone approach dressing. Collision disabled by default and not a route-validation surface. |
| `BloodAxeRitualStones.png#Guideposts_MovedCampCollapsed_A01` | Moved-camp markers | `SM_GIA_BloodAxeMovedCampCollapsedCairn_A01` | Package candidate; planning only | Partially collapsed cairn left behind after a Blood Axe camp moved, with shifted stones, old cloth, and dull ash. Visual memory only; not loot, salvage, breadcrumb, or objective state. |
| `BloodAxeCamp.png#Guideposts_MovedCampClothRemnant_A01` | Moved-camp markers | `SM_GIA_BloodAxeMovedCampClothRemnant_A01` | Package candidate; planning only | Weathered cloth remnant tied to a low cairn or stake, implying an abandoned route edge. No readable message, faction buff, signal behavior, patrol marker, or interaction behavior. |
| `BloodAxeStronghold.png#Guideposts_MemoryCluster_A01` | Mixed guidepost cluster | `KIT_GIA_BloodAxeCairnGuidepostMemoryCluster_A01` | Package candidate; planning only | Composed cluster using one single cairn, one cloth-tied guidepost, one ash-stained base, and one moved-camp remnant. For visual composition planning only; no first implementation target. |
| `BloodAxeRitualStones.png#Review_ScaleRows_A01` | Review rows | `DOC_GIA_BloodAxeCairnGuidepostScaleRows_A01` | Planning row | Non-shipping scale rows comparing single cairns, paired cairns, cloth-tied guideposts, ash bases, and moved-camp markers against female 442 cm and male 470 cm Giant baselines. No scale-lock change or shipped asset approval. |
| `BloodAxeRitualStones.png#Review_RouteRhythmRows_A01` | Review rows | `DOC_GIA_BloodAxeCairnGuidepostRouteRhythmRows_A01` | Planning row | Non-shipping rows showing marker repetition, route-edge spacing, moved-camp memory beats, and silhouette variation. No Unreal actor, validator, capture, startup placement, objective marker, or final art signoff. |
| `BloodAxeRitualStones.png#MaterialDiscipline_A01` | Material discipline | `DOC_GIA_BloodAxeCairnGuidepostMaterialDiscipline_A01` | Planning row | Shared material discipline for rough stone, soot, ash, mud, oxide red cloth, hide ties, rope, sparse blackened iron, aged horn, and dull bone. Explicitly excludes neutral/civilized Giant culture materials and default emissive. |
| `BloodAxeRitualStones.png#LODCollisionPlanning_A01` | LOD/collision planning | `DOC_GIA_BloodAxeCairnGuidepostLODAndCollision_A01` | Planning row | Docs-only LOD0-LOD3 and collision-limit planning for single cairns, paired cairns, cloth-tied guideposts, ash-stained bases, moved-camp markers, mixed clusters, and review rows. No collision proxies, nav blockers, gameplay volumes, DCC, FBX, Unreal, validators, or runtime files. |

## Dependency Notes

- `SM_GIA_BloodAxeApproachCairnMarker_A01` anchors the single static cairn-marker language for approach dressing.
- `KIT_GIA_BloodAxePathMarkers_A01` owns broader camp path markers such as bone/horn markers, broken shield markers, cloth stakes, and mixed marker clusters.
- `KIT_GIA_BloodAxeBannerLine_A01` owns taller banner-line rhythm, rope spans, and threshold banners; this kit must remain lower and cairn-focused.
- Future `KIT_GIA_BloodAxeRitualStones_A01` owns altars, standing stones, ritual channels, and final ritual-site composition; this kit provides guidepost planning only.
- The validated `SK_GIA_Base_A01` scale lock remains authoritative for Giant planning: female baseline 442 cm and male baseline 470 cm.

## Unordered Future Package Candidates

No first implementation target is selected by this intake. If a later lead-approved package lane opens, candidates may be promoted independently:

- `SM_GIA_BloodAxeGuidepostCairnSingle_A01`
- `KIT_GIA_BloodAxeGuidepostCairnPair_A01`
- `SM_GIA_BloodAxeClothTiedGuidepost_A01`
- `SM_GIA_BloodAxeAshStainedGuidepostBase_A01`
- `KIT_GIA_BloodAxeMovedCampGuideposts_A01`
- `KIT_GIA_BloodAxeCairnGuidepostMemoryCluster_A01`
- `DOC_GIA_BloodAxeCairnGuidepostScaleRows_A01`
- `DOC_GIA_BloodAxeCairnGuidepostRouteRhythmRows_A01`
- `DOC_GIA_BloodAxeCairnGuidepostMaterialDiscipline_A01`
- `DOC_GIA_BloodAxeCairnGuidepostLODAndCollision_A01`

## Approval Gates

- Stop before any DCC source, sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material instance, texture asset, validator, runtime source, Blueprint, socket authoring, physics setup, animation asset, startup placement, or implementation target selection.
- Stop before copying, moving, editing, embedding, or committing external source concept files.
- Stop before waypoint behavior, quest logic, nav/pathfinding behavior, readable text, interaction behavior, objective markers, pickup behavior, loot behavior, resource behavior, crafting behavior, faction buff behavior, AI behavior, patrol or spawn logic, encounter scripting, aura volumes, UI markers, VFX, or audio.
- Stop if guideposts stop functioning as visual memory markers and route-edge dressing only.
- Stop if Blood Axe guidepost dressing starts replacing neutral/civilized Giant culture.
- Stop if any row changes the validated `SK_GIA_Base_A01` female baseline 442 cm or male baseline 470 cm.

## Quality Gate Checklist

- Intake is docs-only and limited to the two allowed kit files.
- Child rows cover single cairns, paired cairns, cloth-tied guideposts, ash-stained bases, moved-camp markers, review rows, material discipline, and LOD/collision planning.
- Blood Axe remains a hostile Giant sub-faction and is separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: `SK_GIA_Base_A01` female baseline 442 cm and male baseline 470 cm.
- Rows provide future package candidates without selecting a first implementation target.
- No waypoint, quest, nav/pathfinding, readable text, interaction behavior, objective markers, DCC, FBX, Unreal asset creation, startup placement, runtime work, or final art signoff is defined.
- Review rows are non-shipping planning rows and do not imply validators, captures, scene placement, or shipped assets.
- Material discipline stays on rough stone, ash, mud, oxide red cloth, hide, rope, sparse blackened iron, horn, and aged bone with no default emissive.
- Tiny stone chips, cracks, soot speckles, ash flecks, cloth weave, fray, rope fibers, mud streaks, and paint chips are reserved for future texture or normal detail.
