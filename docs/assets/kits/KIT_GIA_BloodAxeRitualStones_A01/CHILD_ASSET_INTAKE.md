# KIT_GIA_BloodAxeRitualStones_A01 Child Asset Intake

## Source

- Parent backlog row: `Blood Axe Nomad Ritual Stones`
- Parent package: `KIT_GIA_BloodAxeRitualStones_A01`
- Related docs: `SK_GIA_Base_A01`, `KIT_GIA_BloodAxeStrongholdApproach_A01`, `KIT_GIA_BloodAxePathMarkers_A01`, `KIT_GIA_BloodAxeBannerLine_A01`, `SM_GIA_BloodAxeBoneHornMarker_A01`, and child package lanes for tasks `AET-MA-20260629-171` through `AET-MA-20260629-193`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only planning child breakdown; no row may proceed to DCC or Unreal
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture
- Scale dependency: Giant scale lock from `SK_GIA_Base_A01` uses female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges remain females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: external source concepts remain external. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This intake splits `KIT_GIA_BloodAxeRitualStones_A01` into planning-only child rows for standing-stone rings, altar stones, cairn guideposts, ritual channel stones, ritual banner poles, cave approach markers, scale rows, material discipline, LOD/collision planning, and review-only rows.

Keep ritual stones as non-graphic warning, memory, guidepost, and moved-camp remnants only. These rows are static worldbuilding and visual route memory, not ritual gameplay. They must not define VFX/audio, objective logic, encounter behavior, damage/aura behavior, quest/UI markers, readable rune text, navigation/pathfinding, or interaction behavior.

Blood Axe ritual-stone dressing must stay separate from neutral/civilized Giant culture. It may use rough highland stone, soot, ash, trampled mud, scorched timber, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, and dull bone. It must not reuse civilized Giant cave-town masonry, blue-gray civic stonework, terrace/waterwork forms, warm hearth identity, refined stoneworker craft language, peaceful highland wayfinding, or restrained blue-rune culture as the default read.

Every row below remains docs-only. `package-ready` means a planning package exists; it does not create or authorize DCC source, FBX export, Unreal Content, runtime source, tools, validators, material instances, textures, VFX/audio, startup placement, source concept movement, final visual approval, final Blood Axe ritual approval, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeRitualStones_A01#StandingStoneRing_Primary_A01` | Standing-stone rings | `KIT_GIA_BloodAxeStandingStoneRing_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeStandingStoneRing_A01/PRODUCTION_PACKAGE.md` and child intake are ready for tall anchor stones, secondary stones, broken/fallen stones, partial ring arcs, ring-gap variants, review rows, material discipline, and LOD/collision planning. No ritual gameplay, VFX/audio, objective logic, encounter behavior, damage/aura, quest/UI marker, navigation/pathfinding, interaction behavior, DCC, Unreal, startup placement, or final approval. |
| `BloodAxeRitualStones_A01#StandingStone_SingleTall_A01` | Standing-stone rings | `SM_GIA_BloodAxeStandingStone_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeStandingStone_A01/PRODUCTION_PACKAGE.md` is ready as docs-only static marker-stone planning sized against female 442 cm and male 470 cm Giant baselines. No readable rune text, magic device behavior, objective marker, VFX, DCC, Unreal, or first implementation target. |
| `BloodAxeRitualStones_A01#StandingStone_BrokenRing_A01` | Standing-stone rings | `KIT_GIA_BloodAxeBrokenStandingStoneRing_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeBrokenStandingStoneRing_A01/PRODUCTION_PACKAGE.md` and child intake are ready for broken partial arcs, fallen stones, missing segments, gap markers, scale rows, and review-only layout rows. Review planning only; no final ring approval, collision correctness, navigation/pathfinding, ritual boundary, or gameplay arena. |
| `BloodAxeRitualStones_A01#AltarStone_Primary_A01` | Altar stones | `SM_GIA_BloodAxeAltarStone_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeAltarStone_A01/PRODUCTION_PACKAGE.md` is ready as docs-only static non-graphic memory/warning object planning. No ritual interaction, offering mechanics, activation, VFX/audio, damage/aura, readable text, DCC, Unreal, or startup placement. |
| `BloodAxeRitualStones_A01#AltarStone_LowMemorySlab_A01` | Altar stones | `SM_GIA_BloodAxeLowMemorySlab_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeLowMemorySlab_A01/PRODUCTION_PACKAGE.md` is ready for lower slab moved-camp memory dressing with soot, ash, chipped edges, old red cloth tie, and Giant scale lock. No offering slot, loot, pickup, interaction, damage, aura, VFX, DCC, Unreal, or final visual approval. |
| `BloodAxeRitualStones_A01#AltarStone_TippedRemnant_A01` | Altar stones | `SM_GIA_BloodAxeTippedAltarRemnant_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeTippedAltarRemnant_A01/PRODUCTION_PACKAGE.md` is ready for a tipped or partially sunk abandoned-camp altar remnant with static tilt language. No destructible state, physics fall, puzzle state, interaction prompt, offering mechanics, DCC, Unreal, or implementation claim. |
| `BloodAxeRitualStones_A01#CairnGuideposts_Primary_A01` | Cairn guideposts | `KIT_GIA_BloodAxeCairnGuideposts_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeCairnGuideposts_A01/PRODUCTION_PACKAGE.md` and child intake are ready for single cairns, paired cairns, cloth-tied guideposts, ash-stained bases, and moved-camp markers. No waypoint behavior, quest marker behavior, readable text, navigation/pathfinding, DCC, Unreal, or startup placement. |
| `BloodAxeRitualStones_A01#CairnGuidepost_Single_A01` | Cairn guideposts | `SM_GIA_BloodAxeRitualCairnGuidepost_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeRitualCairnGuidepost_A01/PRODUCTION_PACKAGE.md` is ready for a single crude cairn guidepost built from a few large stones, red cloth, and ash base. Visual guidepost only; no trail gameplay, objective logic, navigation/pathfinding, pickup/loot behavior, VFX, or interaction. |
| `BloodAxeRitualStones_A01#CairnGuidepost_Paired_A01` | Cairn guideposts | `KIT_GIA_BloodAxePairedCairnGuideposts_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxePairedCairnGuideposts_A01/PRODUCTION_PACKAGE.md` and child intake are ready for close pairs, staggered pairs, cave-threshold pairs, moved-camp pairs, and review-only spacing rows. Planning only; no waypoint pair, nav gate, encounter lane, quest pointer, collision correctness, DCC, Unreal, or final approval. |
| `BloodAxeRitualStones_A01#MovedCamp_CairnLine_A01` | Cairn guideposts | `KIT_GIA_BloodAxeMovedCampCairnLine_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/PRODUCTION_PACKAGE.md` and child intake are ready for sparse line segments, broken memory clusters, ash gaps, cloth remnants, material discipline, LOD/collision planning, and review-only composition rows. Non-graphic environmental history only; no pathfinding route, tracking mechanic, UI path, spawn logic, patrol route, DCC, or Unreal. |
| `BloodAxeRitualStones_A01#RitualChannelStone_Primary_A01` | Ritual channel stones | `SM_GIA_BloodAxeRitualChannelStone_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeRitualChannelStone_A01/PRODUCTION_PACKAGE.md` is ready for dry channel-stone planning with shallow eroded grooves and inactive stone mass. No liquid flow, VFX, material graph authoring, damage volume, ritual gameplay, DCC, Unreal, or startup placement. |
| `BloodAxeRitualStones_A01#RitualChannelStone_Set_A01` | Ritual channel stones | `KIT_GIA_BloodAxeDryChannelStoneSet_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeDryChannelStoneSet_A01/PRODUCTION_PACKAGE.md` and child intake are ready for dry channel stones, capped ends, broken channel sections, corner/turn pieces, low support stones, ash fill variants, review rows, material discipline reference, and LOD/collision policy reference. No flow logic, spline path, aura line, gameplay conduit, readable rune text, VFX/audio, DCC, or Unreal. |
| `BloodAxeRitualStones_A01#RitualChannelStone_BrokenEnd_A01` | Ritual channel stones | `SM_GIA_BloodAxeBrokenChannelEnd_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeBrokenChannelEnd_A01/PRODUCTION_PACKAGE.md` is ready for a broken end-cap stone for inactive channel arrangements. Static visual damage only; no destructible state, liquid endpoint, damage path, interaction behavior, collision proxy, or implementation target. |
| `BloodAxeRitualStones_A01#RitualBannerPoles_Primary_A01` | Ritual banner poles | `KIT_GIA_BloodAxeRitualBannerPoles_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeRitualBannerPoles_A01/PRODUCTION_PACKAGE.md` and child intake are ready for tall poles, static cloth strips, rope lashings, stone weights, and sparse horn markers. No cloth physics, animation, buff, morale, AI, aura, VFX, interaction, DCC, Unreal, or startup placement. |
| `BloodAxeRitualStones_A01#RitualBannerPole_Tall_A01` | Ritual banner poles | `SM_GIA_BloodAxeRitualBannerPole_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeRitualBannerPole_A01/PRODUCTION_PACKAGE.md` is ready for a tall static pole with stone-weighted base, rope lashings, old red cloth, and optional horn cap. Static warning and memory dressing only; no banner animation, faction buff, AI/morale behavior, VFX/audio, DCC, or Unreal. |
| `BloodAxeRitualStones_A01#RitualBannerPole_WeightedBase_A01` | Ritual banner poles | `SM_GIA_BloodAxeRitualPoleStoneBase_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeRitualPoleStoneBase_A01/PRODUCTION_PACKAGE.md` is ready for a heavy stone base and lashing support module for banner-pole clusters. Planning only; no physics, cloth setup, collision correctness, interaction, pickup, DCC, Unreal, or final visual approval. |
| `BloodAxeRitualStones_A01#CaveApproachMarkers_LowThreshold_A01` | Cave approach markers | `KIT_GIA_BloodAxeCaveApproachMarkers_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachMarkers_A01/PRODUCTION_PACKAGE.md` and child intake are ready for low threshold cairns, paired standing stones, cave remnant clusters, red cloth threshold markers, review rows, material discipline, and LOD/collision planning. Visual threshold only; no navigation/pathfinding, quest/UI marker, encounter trigger, interaction, DCC, Unreal, or startup placement. |
| `BloodAxeRitualStones_A01#CaveApproachMarkers_StandingPair_A01` | Cave approach markers | `SM_GIA_BloodAxeCaveApproachStandingPair_A01` | package-ready | `docs/assets/props/SM_GIA_BloodAxeCaveApproachStandingPair_A01/PRODUCTION_PACKAGE.md` is ready for a pair of rough standing stones framing a cave approach without defining traversal, path widths, or objective entry. No pathfinding, collision guarantee, gate logic, readable rune text, VFX, DCC, Unreal, or final cave approval. |
| `BloodAxeRitualStones_A01#CaveApproachMarkers_RemnantCluster_A01` | Cave approach markers | `KIT_GIA_BloodAxeCaveRemnantCluster_A01` | package-ready | `docs/assets/kits/KIT_GIA_BloodAxeCaveRemnantCluster_A01/PRODUCTION_PACKAGE.md` and child intake are ready for a mixed cave threshold cluster with cairn, low standing stone, old cloth, ash/mud base, threshold variants, material discipline, LOD/collision planning, and review-only cluster rows. Static memory dressing only; no encounter behavior, spawn marker, damage/aura, route scripting, DCC, or Unreal. |
| `BloodAxeRitualStones_A01#ScaleRows_GiantBaselines_A01` | Scale rows | `DOC_GIA_BloodAxeRitualStoneScaleRows_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneScaleRows_A01/PRODUCTION_PACKAGE.md` is ready as non-shipping scale-row planning for female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines beside ritual-stone children. No scale-lock change, shipped marker approval, DCC, Unreal actor, validator, capture, or startup placement. |
| `BloodAxeRitualStones_A01#MaterialDiscipline_A01` | Material discipline | `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01/PRODUCTION_PACKAGE.md` is ready as shared material discipline for rough highland stone, soot, ash, mud, scorched timber, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, dull bone, excluded neutral/civilized Giant materials, and no-emissive baseline. No material instance creation, texture creation, VFX/audio, DCC, or Unreal. |
| `BloodAxeRitualStones_A01#LODCollisionPlanning_A01` | LOD/collision planning | `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01/PRODUCTION_PACKAGE.md` is ready as docs-only LOD0-LOD3 reduction order and disabled/simple collision policy for future static ritual-stone modules and review rows. No collision proxies, nav blockers, gameplay volumes, damage volumes, aura volumes, objective volumes, validators, DCC, Unreal Content, or runtime implementation. |
| `BloodAxeRitualStones_A01#ReviewOnly_RingRhythmRows_A01` | Review-only rows | `DOC_GIA_BloodAxeRitualStoneReviewRows_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneReviewRows_A01/PRODUCTION_PACKAGE.md` is ready as consolidated non-shipping review-row planning for ring density, standing-stone height variation, broken gaps, camera readability, and Blood Axe/neutral Giant separation. No Unreal actor, validator, capture automation, startup placement, final visual signoff, or first implementation target. |
| `BloodAxeRitualStones_A01#ReviewOnly_MovedCampLayoutRows_A01` | Review-only rows | `DOC_GIA_BloodAxeRitualStoneReviewRows_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneReviewRows_A01/PRODUCTION_PACKAGE.md` is ready as consolidated non-shipping review-row planning for moved-camp remnants: cairn lines, cold ash bases, broken stones, old cloth, and cave approach memory beats. No encounter layout, navigation/pathfinding, objective path, spawn logic, DCC, Unreal, startup placement, or final approval. |
| `BloodAxeRitualStones_A01#ReviewOnly_CaveApproachRows_A01` | Review-only rows | `DOC_GIA_BloodAxeRitualStoneReviewRows_A01` | package-ready | `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneReviewRows_A01/PRODUCTION_PACKAGE.md` is ready as consolidated non-shipping review-row planning for cave approach readability rows showing low threshold markers, standing pairs, banner-pole silhouettes, and scale bars. No cave gameplay, traversal proof, collision correctness, quest/UI marker, validator, DCC, Unreal, or startup placement. |

## Dependency Notes

- `SK_GIA_Base_A01` owns Giant scale, skeleton policy, capsule expectations, and character collision assumptions. This intake does not change those contracts.
- `KIT_GIA_BloodAxeStrongholdApproach_A01` owns stronghold approach cliffs, palisades, switchback paths, overlook silhouettes, gate relationship planning, and approach warning markers. This ritual-stone kit may visually relate to cave or approach thresholds but does not approve terrain, stronghold layout, nav/pathfinding, or gate behavior.
- `KIT_GIA_BloodAxePathMarkers_A01` owns broad camp path-marker language. Cairn guideposts here should read older and more memory-oriented, not waypoint or objective markers.
- `KIT_GIA_BloodAxeBannerLine_A01` owns broad camp banner-line rhythm. Ritual banner poles here are static remnant and warning poles only, not animated banners, morale devices, or faction buff markers.
- `SM_GIA_BloodAxeBoneHornMarker_A01` owns sparse bone/horn territory-marker language. Ritual-stone rows may reuse its restraint but must not escalate into graphic gore or ritual gameplay.
- No row in this table is approved as a first DCC, Unreal, runtime, source asset, gameplay, final visual, final Blood Axe ritual, or implementation target.

## Unordered Future Package Candidates

No first DCC target, source asset target, Unreal target, runtime target, or implementation target is selected by this intake. If a later lead-approved package lane is opened, these may be promoted independently:

- `KIT_GIA_BloodAxeStandingStoneRing_A01`
- `KIT_GIA_BloodAxeBrokenStandingStoneRing_A01`
- `SM_GIA_BloodAxeStandingStone_A01`
- `SM_GIA_BloodAxeAltarStone_A01`
- `SM_GIA_BloodAxeLowMemorySlab_A01`
- `SM_GIA_BloodAxeTippedAltarRemnant_A01`
- `KIT_GIA_BloodAxeCairnGuideposts_A01`
- `SM_GIA_BloodAxeRitualCairnGuidepost_A01`
- `KIT_GIA_BloodAxePairedCairnGuideposts_A01`
- `KIT_GIA_BloodAxeMovedCampCairnLine_A01`
- `SM_GIA_BloodAxeRitualChannelStone_A01`
- `KIT_GIA_BloodAxeDryChannelStoneSet_A01`
- `SM_GIA_BloodAxeBrokenChannelEnd_A01`
- `KIT_GIA_BloodAxeRitualBannerPoles_A01`
- `SM_GIA_BloodAxeRitualBannerPole_A01`
- `SM_GIA_BloodAxeRitualPoleStoneBase_A01`
- `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- `SM_GIA_BloodAxeCaveApproachStandingPair_A01`
- `KIT_GIA_BloodAxeCaveRemnantCluster_A01`
- `DOC_GIA_BloodAxeRitualStoneScaleRows_A01`
- `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01`
- `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`
- `DOC_GIA_BloodAxeRitualStoneReviewRows_A01`

## Approval Gates

- Stop before DCC source, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content asset, material instance, texture asset, material graph, import script, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, startup placement, or any source asset creation.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before selecting a first DCC, Unreal, source asset, runtime, gameplay, or implementation target from any row.
- Stop before ritual gameplay, offering mechanics, activation states, liquid flow, readable rune text, objective markers, quest/UI symbols, waypoint logic, trail-marker gameplay, navigation/pathfinding, traversal proofs, climb logic, path widths as gameplay values, encounter design, AI spaces, patrol routes, spawn logic, perception, damage values, aura behavior, projectile behavior, cover rules, trap behavior, destructible behavior, loot, inventory, rewards, crafting, economy, resource behavior, salvage, pickup behavior, VFX, audio, or interaction behavior.
- Stop before claiming collision correctness, terrain integration, cave compatibility, runtime performance validation, marker validation, final silhouette approval, final Blood Axe ritual approval, or final visual approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, VFX/audio asset, global index, task board, backlog, bootstrap, or unrelated package file.
- Rows cover standing-stone rings, altar stones, cairn guideposts, ritual channel stones, ritual banner poles, cave approach markers, scale rows, material discipline, LOD/collision planning, and review-only rows.
- Every row remains docs-only; `package-ready` rows do not claim permission to proceed to DCC, Unreal, final approval, implementation, or first target selection.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Ritual stones remain non-graphic warning, memory, guidepost, and moved-camp remnants only.
- No ritual gameplay, VFX/audio, objective logic, encounter behavior, damage/aura behavior, quest/UI markers, readable rune text, navigation/pathfinding, interaction behavior, pickup/loot behavior, resource/crafting/economy behavior, cloth physics, animation, DCC, Unreal, source asset creation, startup placement, or final visual approval is defined.
- Review-only rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, marker validation, camera approval, or final visual signoff.
- Materials use rough highland stone, soot, ash, trampled mud, scorched timber, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, and dull bone consistently.
- Default emissive, ritual glow, shamanic glow, signal glow, animated material states, gameplay VFX, UI-like markers, readable text, and neutral/civilized Giant language are absent and approval-gated.
- Tiny stone chips, cloth weave, fray, scratches, pitting, soot speckles, ash flecks, paint chips, horn rings, lichen, mud streaks, and wood grain are assigned to textures or normals in future packages.
