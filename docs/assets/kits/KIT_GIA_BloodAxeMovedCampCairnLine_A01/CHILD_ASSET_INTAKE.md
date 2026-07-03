# KIT_GIA_BloodAxeMovedCampCairnLine_A01 Child Asset Intake

## Source

- Parent planning source: `KIT_GIA_BloodAxeRitualStones_A01`
- Parent child row: `BloodAxeRitualStones_A01#MovedCamp_CairnLine_A01`
- Related packages: `KIT_GIA_BloodAxeCairnGuideposts_A01`, `SM_GIA_BloodAxeRitualCairnGuidepost_A01`, `KIT_GIA_BloodAxePathMarkers_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock with female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft and males 14'10"-16'0"
- Intake status: docs-only planning child breakdown
- Source-storage guardrail: do not copy, move, edit, embed, crop, rename, inspect for final approval, or commit external source concept images for this task

## Notes

This intake splits `KIT_GIA_BloodAxeMovedCampCairnLine_A01` into planning-only child rows for sparse line segments, broken memory clusters, ash gaps, cloth remnants, material discipline, LOD/collision planning, and review-only composition rows.

The cairn line is non-graphic environmental history only. It suggests that a Blood Axe camp once occupied or crossed the area and later moved, leaving interrupted stone and ash evidence behind. It must not become a functional trail, route, navigation aid, waypoint chain, tracking mechanic, UI path, spawn guide, patrol guide, encounter lane, objective line, quest marker system, or final camp-route approval.

Blood Axe cairn-line dressing may use rough highland stone, soot, ash, trampled mud, burned grass, oxide red cloth, rawhide ties, rope lashings, sparse blackened iron, old horn, and aged bone. It must not use blue-gray civic masonry, refined cave-town carving, terrace or waterwork motifs, warm hearth settlement language, restrained blue runes, peaceful highland markers, or neutral/civilized Giant culture as the default read.

Except for the separately promoted `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` startup review row, every row below remains docs-only. `Package candidate; planning only` does not create or authorize DCC source, FBX export, Unreal content, material instances, textures, validators, source folders, runtime files, startup placement, final visual approval, final camp-route approval, or first implementation target selection.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeRitualStones_A01#MovedCamp_CairnLineSparseSegment_A01` | Sparse line segments | `KIT_GIA_BloodAxeMovedCampSparseCairnSegment_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-319`. Short broken span of 2-4 low cairn remnants with uneven spacing, missing beats, cold ash, and trampled mud. Environmental history only; no functional trail, waypoint chain, tracking mechanic, UI path, spawn logic, patrol logic, encounter scripting, DCC, FBX, Unreal, startup placement, or first implementation target selection. |
| `BloodAxeRitualStones_A01#MovedCamp_CairnLineSparseSegment_B01` | Sparse line segments | `KIT_GIA_BloodAxeMovedCampSparseCairnSegment_B01` | package-ready; docs-only | Package validated in `AET-MA-20260629-319`. Wider sparse span with one dominant collapsed cairn, one low support pile, and a long empty ash gap. Use for visual interruption, not a guide line or traversal hint. |
| `BloodAxeRitualStones_A01#MovedCamp_CairnLineCollapsedEnd_A01` | Sparse line segments | `SM_GIA_BloodAxeMovedCampCollapsedLineEnd_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-319`. Final-looking broken end of a cairn line, with stones sliding into mud and cloth partly buried. Must not imply a destination, objective endpoint, portal clue, encounter trigger, or route completion state. |
| `BloodAxeRitualStones_A01#MovedCamp_BrokenMemoryCluster_A01` | Broken memory clusters | `KIT_GIA_BloodAxeMovedCampBrokenMemoryCluster_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-319`. Cluster of one collapsed cairn, two displaced stones, low soot, and old lashings. Reads as abandoned Blood Axe camp memory, not loot, salvage, interaction, or ritual activation. |
| `BloodAxeRitualStones_A01#MovedCamp_BrokenMemoryCluster_B01` | Broken memory clusters | `KIT_GIA_BloodAxeMovedCampBrokenMemoryCluster_B01` | package-ready; docs-only | Package validated in `AET-MA-20260629-319`. Wider cluster with a short stake remnant and one cloth strip caught under a stone. No readable text, signal behavior, faction buff, AI marker, or gameplay state. |
| `BloodAxeRitualStones_A01#MovedCamp_LowCairnRemnant_A01` | Broken memory clusters | `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` | startup review actor placed and validated | Package validated in `AET-MA-20260629-319`; first controlled DCC/Unreal review target validated through `AET-MA-20260629-575`; first-pass visual approval recorded in `AET-MA-20260629-577`; startup review actor placed and validated through `AET-MA-20260629-579`. Single low remnant from a former cairn, imported at 130.35 cm tall and sized against female 442 cm and male 470 cm Giant baselines. Static dressing review only; no final visual art, final shipped startup composition, collision correctness, pickup behavior, gameplay behavior, or next implementation target. |
| `BloodAxeRitualStones_A01#MovedCamp_AshGap_A01` | Ash gaps | `SM_GIA_BloodAxeMovedCampAshGap_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-319`. Flat cold ash and trampled mud patch between visible cairn remnants. Ground residue only; no decal trail behavior, damage field, aura field, gatherable ash, VFX, audio, or route validation. |
| `BloodAxeRitualStones_A01#MovedCamp_AshGapBrokenRing_A01` | Ash gaps | `SM_GIA_BloodAxeMovedCampBrokenAshRing_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-319`. Irregular ash-dark footprint from an old camp fire or stone cluster, broken and incomplete so it does not read as an objective ring. No interaction prompt, ritual boundary, gameplay area, or VFX state. |
| `BloodAxeRitualStones_A01#MovedCamp_AshGapMudScuff_A01` | Ash gaps | `SM_GIA_BloodAxeMovedCampMudScuff_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Low mud and soot scuff used to separate cairn beats. Must remain broad environmental residue, not footprints, tracking marks, or readable travel instructions. |
| `BloodAxeRitualStones_A01#MovedCamp_ClothRemnantStoneTie_A01` | Cloth remnants | `SM_GIA_BloodAxeMovedCampClothStoneTie_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Fixed oxide red cloth tied around or trapped under a low cairn stone. No cloth simulation, wind, UI color coding, faction buff, readable message, or interaction behavior. |
| `BloodAxeRitualStones_A01#MovedCamp_ClothRemnantBuriedStrip_A01` | Cloth remnants | `SM_GIA_BloodAxeMovedCampBuriedClothStrip_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Weathered cloth strip partially buried in ash and mud. It should read as old Blood Axe residue, not a breadcrumb, clickable object, pickup, or objective marker. |
| `BloodAxeRitualStones_A01#MovedCamp_ShortStakeRemnant_A01` | Cloth remnants | `SM_GIA_BloodAxeMovedCampShortStakeRemnant_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Short scorched stake or splintered post with one cloth scrap and rawhide tie. Keep it smaller than banner-line assets and separate from active signal or route-flag language. |
| `BloodAxeRitualStones_A01#MovedCamp_MaterialDiscipline_A01` | Material discipline | `DOC_GIA_BloodAxeMovedCampCairnLineMaterialDiscipline_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Shared material discipline for rough stone, soot, ash, mud, oxide red cloth, rawhide, rope, sparse blackened iron, old horn, and aged bone. Explicitly excludes neutral/civilized Giant material language and default emissive. |
| `BloodAxeRitualStones_A01#MovedCamp_LODCollisionPlanning_A01` | LOD/collision planning | `DOC_GIA_BloodAxeMovedCampCairnLineLODAndCollision_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Docs-only LOD0-LOD3 and collision-limit planning for sparse segments, memory clusters, ash gaps, cloth remnants, short stake remnants, and review rows. No collision proxies, nav blockers, gameplay volumes, DCC, FBX, Unreal, validators, or runtime files. |
| `BloodAxeRitualStones_A01#ReviewOnly_MovedCampSpacingRows_A01` | Review-only composition rows | `DOC_GIA_BloodAxeMovedCampCairnLineReviewRows_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Non-shipping rows comparing interrupted spacing, missing beats, collapse density, and camera readability beside female 442 cm and male 470 cm Giant baselines. No Unreal actor, validator, capture, startup placement, final visual signoff, or route approval. |
| `BloodAxeRitualStones_A01#ReviewOnly_MovedCampAshGapRows_A01` | Review-only composition rows | `DOC_GIA_BloodAxeMovedCampCairnLineReviewRows_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Non-shipping rows focused on ash gaps, mud scuffs, and low residue between cairn remnants. Must not imply footprints, tracking UI, navigation line, objective ring, or encounter lane. |
| `BloodAxeRitualStones_A01#ReviewOnly_MovedCampClothRows_A01` | Review-only composition rows | `DOC_GIA_BloodAxeMovedCampCairnLineReviewRows_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Non-shipping rows comparing small cloth-remnant restraint, color balance, and Blood Axe identity at MMO camera distance. No cloth simulation, active signal, UI marker, banner-line promotion, DCC, or Unreal. |

## Dependency Notes

- `KIT_GIA_BloodAxeRitualStones_A01` owns the parent ritual-stone breakdown and identifies this kit as the moved-camp cairn-line row.
- `KIT_GIA_BloodAxeCairnGuideposts_A01` owns general cairn guidepost language. This kit narrows that language to older, sparser, partially collapsed moved-camp evidence.
- `SM_GIA_BloodAxeRitualCairnGuidepost_A01` anchors the single static cairn guidepost material and silhouette language. This kit may reuse its few-large-stones discipline but should look more abandoned and interrupted.
- `KIT_GIA_BloodAxePathMarkers_A01` owns broader camp path-marker dressing. This moved-camp kit must be less active, less directive, and more broken than normal camp marker dressing.
- Validated `SK_GIA_Base_A01` scale lock remains authoritative: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

## Unordered Future Package Candidates

No first implementation target is selected by this intake. All child package rows in this intake are docs-ready and remain blocked from DCC, FBX, Unreal, startup placement, source concept movement, final approval, or implementation target selection.

## Approval Gates

- Stop before any DCC source, sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal content asset, material instance, texture asset, validator, runtime source, Blueprint, socket authoring, physics setup, animation asset, startup placement, source folder creation, or implementation target selection.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing external source concept files.
- Stop before waypoint behavior, breadcrumb behavior, tracking mechanic, UI path, objective logic, navigation behavior, interaction behavior, pickup/loot behavior, resource behavior, crafting/economy behavior, faction buff behavior, AI behavior, patrol logic, spawn logic, encounter scripting, cover behavior, damage volumes, aura volumes, VFX, audio, destructible behavior, physics collapse, or route gameplay.
- Stop before final camp-route approval, final Blood Axe ritual approval, final visual approval, terrain integration claims, collision correctness claims, runtime performance claims, marker validation claims, or first implementation target selection.
- Stop if the cairn line starts functioning as a guide instead of abandoned environmental history.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row changes the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Intake is docs-only and limited to the two allowed kit files.
- Child rows cover sparse line segments, broken memory clusters, ash gaps, cloth remnants, review-only composition rows, material discipline, and LOD/collision planning.
- Blood Axe remains a hostile Giant sub-faction and is separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved ranges females 14-15 ft and males 14'10"-16'0".
- Rows provide future package candidates without selecting a first implementation target.
- The cairn line remains non-graphic environmental history about a moved camp, not a functional trail or route.
- No waypoint behavior, breadcrumb behavior, tracking mechanic, UI path, objective logic, navigation behavior, interaction behavior, pickup/loot behavior, resource behavior, spawn logic, patrol logic, encounter scripting, DCC, FBX, Unreal asset creation, runtime work, startup placement, final route approval, or final art signoff is defined.
- Review-only rows are non-shipping planning rows and do not imply validators, captures, scene placement, route approval, marker validation, or shipped assets.
- Material discipline stays on rough stone, soot, ash, mud, oxide red cloth, rawhide, rope, sparse blackened iron, old horn, and aged bone with no default emissive.
- Tiny stone chips, cracks, soot speckles, ash flecks, cloth weave, fray, rope fibers, lichen, mud streaks, and paint chips are reserved for future texture or normal detail.
- No source folders, DCC files, Unreal files, validators, images, material instances, texture assets, external source concept movement, global docs, task board, backlog, bootstrap, approval queue, or other workers' package files are edited by this task.
