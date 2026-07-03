# KIT_GIA_BloodAxePathMarkers_A01 Child Asset Intake

## Source

- Parent planning row: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md` entry `Blood Axe Village.png#Path_CairnMarkers`
- Source references recorded in existing camp intake docs: `Blood Axe Village.png`, `BloodAxeCamp.png`, `BloodAxecamp.png`, `BloodAxeGate.png`, and `BloodAxeStronghold.png`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only planning child breakdown ready; first path-marker child package wave validated in `AET-MA-20260629-359`; second package wave validated in `AET-MA-20260629-369`; material/LOD policy and closure docs validated in `AET-MA-20260629-379`
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture
- Scale dependency: validated `SK_GIA_Base_A01` female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: source concepts remain in the external concept folder only. Do not copy, move, edit, embed, inspect for visual approval, or commit source images for this docs-only package.

## Notes

This intake splits the Blood Axe path-marker kit into planning-only child rows. The cairn, cloth stake, low rag, bone/horn, horn fork, token, broken shield, ash base, mixed cluster, review-row, scale-row, material-discipline, LOD/collision, implementation-readiness, and package-closure docs are package-ready at docs-only level.

Blood Axe path-marker dressing must stay separate from neutral/civilized Giant culture. It may use rough field stone, scorched timber, hide ties, rope, oxide red cloth, blackened iron, broken shield scrap, soot, ash, mud, and sparse non-graphic horn or bone markers. It must not reuse civilized Giant cave-town, blue-gray masonry, terrace, warm hearth, civic stoneworker, refined highland route-marker, or restrained blue-rune language as the default read.

`KIT_GIA_BloodAxeBannerLine_A01` owns taller banner poles, rope-line variants, tattered banner spans, warning pennants, and threshold banner rhythm. This path-marker kit owns lower route readability and ground-adjacent hostile camp dressing only.

This intake does not select a first DCC target, approve final visual art, create source folders, create FBX exports, create Unreal Content, place startup actors, define waypoint behavior, define trail-marker gameplay, define objective logic, define nav/pathfinding behavior, define pickup/loot behavior, or define runtime gameplay.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- |
| `Blood Axe Village.png#PathMarkers_CairnSingle_A01` | Cairns | `SM_GIA_BloodAxeCairnPathMarker_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-359`. Single crude stacked cairn, 80-180 cm tall, using a few large field stones with soot and mud at the base. Visual route readability only; no waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, DCC, Unreal, startup placement, final approval, or implementation target. |
| `BloodAxeCamp.png#PathMarkers_CairnCluster_A01` | Cairns | `KIT_GIA_BloodAxeCairnPathMarkerCluster_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-359`. Two to five varied cairns arranged as a rough camp path bend or approach compression beat, sized against the 442 cm and 470 cm Giant baselines. Static visual composition only; no marker actor, nav helper, encounter lane, first DCC target selection, DCC, Unreal, startup placement, or implementation target. |
| `BloodAxeStronghold.png#PathMarkers_CairnScrapCap_A01` | Cairns | `SM_GIA_BloodAxeCairnScrapCap_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-359`. Cairn variant with one dull shield rim, scrap cap, or blackened iron plate wedged between large stones. Warning dressing only; no salvage, loot, destructible scrap, resource gameplay, DCC, FBX, Unreal, startup placement, final approval, or implementation target. |
| `Blood Axe Village.png#PathMarkers_ClothStake_A01` | Cloth stakes | `SM_GIA_BloodAxeClothStakeMarker_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-359`. Short scorched timber stake with hide wrap and one broad oxide red cloth strip, 140-280 cm high. Static route dressing only; no cloth simulation, wind animation, UI arrow, waypoint logic, interaction behavior, DCC, Unreal, startup placement, final approval, or implementation target. |
| `BloodAxeCamp.png#PathMarkers_ClothStakePair_A01` | Cloth stakes | `KIT_GIA_BloodAxeClothStakeMarkerSet_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-359`. Pair or loose row of two to four cloth stakes for repeated camp path rhythm. Uneven spacing only; no fence collision, pathfinding blocker, tripwire, trap, objective boundary, DCC, Unreal, startup placement, final approval, or implementation target. |
| `BloodAxecamp.png#PathMarkers_LowRedRag_A01` | Cloth stakes | `SM_GIA_BloodAxeLowRedRagMarker_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-359`. Low torn red rag on a stub stake or stone-tied stick for near-ground visual direction changes. Broad sparse cloth only; no collectible flag, capture marker, patrol marker, trail gameplay, DCC, Unreal, startup placement, final approval, or implementation target. |
| `BloodAxeCamp.png#PathMarkers_BoneHornMarker_A01` | Bone/horn markers | `SM_GIA_BloodAxeBoneHornPathMarker_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-359`. Sparse non-graphic horn or old bone lashed to a stake or cairn side, 80-220 cm tall. Visual hostility only; no gore escalation, loot drop, pickup, crafting resource, ritual mechanic, DCC, Unreal, startup placement, final approval, or implementation target. |
| `BloodAxeStronghold.png#PathMarkers_HornFork_A01` | Bone/horn markers | `SM_GIA_BloodAxeHornForkMarker_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-359`. Forked horn silhouette used near stronghold approaches or camp threshold turns, with rope lashings and ash-dark base. Static warning silhouette only; no signal device, faction aura, VFX pulse, shamanic state, DCC, Unreal, startup placement, final approval, or implementation target. |
| `Blood Axe Village.png#PathMarkers_BoneTokenSet_A01` | Bone/horn markers | `KIT_GIA_BloodAxeBoneHornTokenSet_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-369`. Small reusable set of blunt horn caps, old bone tokens, hide ties, and rope knots for marker variants. Visual parts only; no pickups, inventory items, trophies, crafting ingredients, loot, ritual mechanics, DCC, Unreal, startup placement, final approval, or implementation target. |
| `BloodAxeCamp.png#PathMarkers_BrokenShieldMarker_A01` | Broken shield markers | `SM_GIA_BloodAxeBrokenShieldPathMarker_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-369`. Large broken shield fragment, dull scrap plate, rope-tied stake, and red paint smear used as a sparse hostile warning. No usable shield, pickup, loot, destructible behavior, inventory behavior, combat cover definition, DCC, Unreal, startup placement, or implementation target. |
| `BloodAxeGate.png#PathMarkers_ScrapShieldLean_A01` | Broken shield markers | `SM_GIA_BloodAxeScrapShieldLeanMarker_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-369`. Leaning shield rim and blackened plate against a low cairn or stake for gate-adjacent route dressing. Static prop only; no blocker behavior, gate logic, nav hint, objective marker, pickup, loot, DCC, Unreal, startup placement, or implementation target. |
| `BloodAxeStronghold.png#PathMarkers_AshBase_A01` | Ash-stained bases | `SM_GIA_BloodAxeAshStainedBase_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-369`. Low ash, soot, charcoal, and trampled mud base for grounding cairns and stakes. Ground dressing only; no decal gameplay, trail tracking, gatherable ash, damage field, VFX, material-state behavior, DCC, Unreal, startup placement, or implementation target. |
| `BloodAxeCamp.png#PathMarkers_AshTrailPad_A01` | Ash-stained bases | `KIT_GIA_BloodAxeAshPathBaseSet_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-369`. Set of low ash-stained base pads and burned-earth footprints for visual route rhythm. No trail-marker gameplay, navigation hints, objective pathing, footprints-as-tracking, pickup/loot behavior, startup placement, DCC, Unreal, final approval, or implementation target. |
| `Blood Axe Village.png#PathMarkers_MixedCluster_A01` | Mixed marker cluster | `KIT_GIA_BloodAxePathMarkerCluster_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-369`. Composed visual cluster combining one cairn, one cloth stake, one horn/bone marker, one broken shield accent, and one ash-stained base. Review composition only; no review actor, implementation task, objective cluster, route scripting, encounter setup, DCC, Unreal, startup placement, or implementation target. |
| `Blood Axe Village.png#Review_CompositionRows_A01` | Review composition rows | `DOC_GIA_BloodAxePathMarkerReviewRows_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-369`. Docs-only review rows showing route rhythm, marker repetition, low/mid-height silhouette variation, camp approach bends, mixed clusters, and camera readability. No Unreal actor, validator, capture automation, startup placement, final visual signoff, first DCC target selection, DCC, or Unreal work. |
| `Blood Axe Village.png#Review_ScaleRows_A01` | Review composition rows | `DOC_GIA_BloodAxePathMarkerScaleRows_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-369`. Non-shipping scale rows for female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines beside path-marker families. No scale-lock change, shipped marker approval, DCC, FBX, Unreal, validator, capture, startup placement, final approval, or implementation target. |
| `Blood Axe Village.png#Review_LODCollisionRows_A01` | Review composition rows | `DOC_GIA_BloodAxePathMarkerLODAndCollision_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-379`. Docs-only LOD0-LOD3 and collision-limit rows for cairns, stakes, horn/bone warnings, shield scraps, ash bases, mixed clusters, and review markers. No collision proxies, nav blockers, gameplay volumes, validator files, DCC, Unreal Content, startup placement, final approval, or implementation target. |
| `Blood Axe Village.png#MaterialDiscipline_A01` | Material discipline row | `DOC_GIA_BloodAxePathMarkerMaterialDiscipline_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-379`. Shared material discipline for rough field stone, scorched timber, hide, rope, blackened iron, ash, mud, oxide red cloth, dull bone, and horn. Explicitly excludes neutral/civilized Giant cave-town materials, refined route markers, default emissive, material instances, texture assets, material graphs, DCC, Unreal Content, final approval, or implementation target. |

## Dependency Notes

- `KIT_GIA_BloodAxeCamp_A01` owns the broad camp split and identifies this kit as the path-marker child lane.
- `KIT_GIA_BloodAxeBannerLine_A01` owns tall banner lines, rope spans, tattered banner panels, warning pennants, and threshold banner rhythm. This kit should stay lower, smaller, and more ground-adjacent.
- `KIT_GIA_BloodAxeStrongholdApproach_A01` owns cliffs, palisade walls, switchback paths, overlook silhouettes, and stronghold approach composition. This kit may provide static warning markers only as visual dressing.
- Future `KIT_GIA_BloodAxeRitualStones_A01` owns ritual stones, altars, standing-stone rings, ritual channels, and guidepost lore. This path-marker kit must not define ritual behavior or final ritual-stone language.
- `KIT_GIA_BloodAxeForgeScrapSorting_A01` owns scrap piles and forge sorting language. Broken shield markers here are sparse warning dressing, not salvage, loot, or crafting resources.

## Remaining Future Package Candidates

No remaining docs-only path-marker package candidates are open in this intake after `AET-MA-20260629-379`.

No first DCC target, first implementation target, build order, source folder, DCC scope, FBX export, Unreal Content, validator, startup placement, final approval, or Hermes work is selected by this intake.

## Approval Gates

- Stop before any DCC source, sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material instance, texture asset, validator, runtime source, Blueprint, socket authoring, physics setup, animation asset, or startup placement work.
- Stop before copying, moving, editing, embedding, inspecting for visual approval, or committing external source concepts.
- Stop before waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, resource nodes, harvesting, salvage rules, crafting/economy behavior, faction buff behavior, morale behavior, AI behavior, patrol/spawn logic, encounter scripting, capture mechanics, aura volumes, UI markers, VFX pulses, or audio cues.
- Stop before selecting a first DCC target or first package implementation target.
- Stop before final visual approval claims.
- Stop if Blood Axe path-marker dressing starts replacing neutral/civilized Giant culture.
- Stop if any row requires changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5".

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, or bootstrap file.
- Child rows include cairns, cloth stakes, bone/horn markers, broken shield markers, ash-stained bases, mixed marker clusters, and review composition rows.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Rows are useful for future package planning without selecting a first DCC target.
- No waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, cloth/physics setup, banner animation, faction buff behavior, morale/AI behavior, encounter behavior, interaction behavior, resource behavior, crafting/economy behavior, VFX, audio, or startup placement is defined.
- Review composition rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, or final visual signoff.
- Materials use rough field stone, scorched timber, hide, rope, blackened iron, soot, ash, mud, oxide red cloth, and sparse non-graphic bone or horn consistently.
- Default emissive, ritual glow, shamanic glow, signal glow, animated material states, gameplay VFX, UI-like markers, readable text, and neutral/civilized Giant language are absent and approval-gated.
- Tiny stone chips, cloth weave, fray, stitches, scratches, pitting, soot speckles, ash flecks, paint chips, and wood grain are assigned to textures or normals in future packages.
