# KIT_GIA_BloodAxeStrongholdApproach_A01 Child Asset Intake

## Source

- Parent kit: `KIT_GIA_BloodAxeStrongholdApproach_A01`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Gate_StrongholdApproach`
- Source route reference: `BloodAxeStronghold.png#Gate_StrongholdApproach` as listed by the existing Blood Axe camp intake docs
- Related docs: `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeWarband_A01`, `KIT_GIA_BloodAxeFormationDressing_A01`, `KIT_GIA_BloodAxeArmory_A01`, `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeTrophyGate_A01`, and `SM_GIA_BloodAxeWatchPlatform_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only child split complete for stronghold approach planning; no child build target selected
- Scale dependency: validated `SK_GIA_Base_A01` female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: external source concepts remain in the external concept folder only. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This child intake splits the Blood Axe stronghold approach into planning-only rows. The rows describe environment approach modules, material discipline, visual scale, review composition, LOD/collision assumptions, and future package routing. They are not final stronghold approval, final visual approval, first DCC targets, terrain implementation, nav paths, encounter routes, AI spaces, destructible assets, gameplay systems, loot/crafting/economy/resource loops, or implementation tickets.

Blood Axe approach dressing must stay separate from neutral/civilized Giant culture. It may use rough cliffs, raw palisades, blackened iron, dark steel, chained scrap, scorched hide, soot, ash, packed earth, rough timber, oxide red cloth, and sparse non-graphic bone or horn warnings. It must not reuse civilized Giant cave-town, blue-gray masonry, terrace, waterwork, warm hearth, civic stoneworker, or restrained blue-rune language as the default read.

No row below creates or authorizes DCC source, FBX export, Unreal import, source asset creation, runtime source, validators, startup placement, source concept movement, final visual approval, final stronghold approval, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeStronghold.png#Cliffs_WallSegments` | Cliff wall segments | `KIT_GIA_BloodAxeApproachCliffWalls_A01` | Package ready | `docs/assets/kits/KIT_GIA_BloodAxeApproachCliffWalls_A01/PRODUCTION_PACKAGE.md` and child intake are ready for modular vertical cliff faces, fractured highland rock, overhang shadows, ledge backs, dark recesses, scale/review rows, material discipline, and LOD/collision planning. Planning only; no terrain sculpt, landscape import, collision proxy, HLOD, nav/pathfinding, DCC, Unreal, final visual approval, or final stronghold approval. |
| `BloodAxeStronghold.png#Cliffs_LedgeCaps` | Cliff ledge caps and shelves | `SM_GIA_BloodAxeApproachCliffLedgeCap_A01` | Package ready | `docs/assets/props/SM_GIA_BloodAxeApproachCliffLedgeCap_A01/PRODUCTION_PACKAGE.md` is ready for local ledge caps, rubble shelves, and rock lips that frame switchbacks and overlooks. Visual scale only; no traversal proof, climb route, nav/pathfinding, walkable collision implementation, DCC, Unreal, or startup placement. |
| `BloodAxeStronghold.png#Palisade_WallSegments` | Approach palisades | `SM_GIA_BloodAxeApproachPalisadeWall_A01` | Package ready | `docs/assets/props/SM_GIA_BloodAxeApproachPalisadeWall_A01/PRODUCTION_PACKAGE.md` is ready for Giant-scale raw-log wall runs with uneven spike crowns, rough braces, blackened iron bands, chained scrap, and torn red cloth. Static visual planning only; no destructible wall, cover rule, nav blocker behavior, collision proxy, DCC, Unreal, or startup placement. |
| `BloodAxeStronghold.png#Palisade_GateFlankReturns` | Gate-flank palisade returns | `SM_GIA_BloodAxeApproachGateFlank_A01` | Package ready | `docs/assets/props/SM_GIA_BloodAxeApproachGateFlank_A01/PRODUCTION_PACKAGE.md` is ready for wall-return modules that visually funnel the route toward a Blood Axe gate. Gate relationship only; no final gate approval, stronghold layout, open/close state, interaction, lock, nav link, DCC, Unreal, or startup placement. |
| `BloodAxeStronghold.png#Paths_SwitchbackMain` | Switchback path sections | `KIT_GIA_BloodAxeSwitchbackPathSections_A01` | Package ready | `docs/assets/kits/KIT_GIA_BloodAxeSwitchbackPathSections_A01/PRODUCTION_PACKAGE.md` and child intake are ready for straight shelf, packed-earth strip, stone-chocked edge, log-edged segment, visual choke, widened shelf, scale/review rows, material discipline, and LOD/collision planning. Visual route planning only; widths are not nav, spawn, patrol, or encounter values. |
| `BloodAxeStronghold.png#Paths_ShelfTurns` | Switchback hairpin turns | `SM_GIA_BloodAxeSwitchbackTurn_A01` | Package ready | `docs/assets/props/SM_GIA_BloodAxeSwitchbackTurn_A01/PRODUCTION_PACKAGE.md` is ready for broad shelf-turn modules, hairpin bends, mud banks, and edge silhouettes for approach composition. No pathfinding, traversal validation, slope rule, collision correctness, route scripting, DCC, Unreal, or startup placement. |
| `BloodAxeStronghold.png#Markers_WarningStakes` | Warning markers | `KIT_GIA_BloodAxeApproachWarningMarkers_A01` | Package ready | `docs/assets/kits/KIT_GIA_BloodAxeApproachWarningMarkers_A01/PRODUCTION_PACKAGE.md` and child intake are ready for red cloth stakes, horn markers, broken shield tokens, blade fragments, rough warning posts, mixed marker clusters, scale rows, review composition rows, material discipline, and LOD/collision planning. Non-graphic visual warnings only; no objective marker, quest marker, UI symbol, aura, damage, loot, pickup, interaction, DCC, Unreal, or startup behavior. |
| `BloodAxeStronghold.png#Markers_CairnClothLine` | Cairn and cloth-line markers | `SM_GIA_BloodAxeApproachCairnMarker_A01` | Package ready | `docs/assets/props/SM_GIA_BloodAxeApproachCairnMarker_A01/PRODUCTION_PACKAGE.md` is ready for crude cairns, tied cloth strips, ash-stained stones, and route-edge warning beats. Visual approach rhythm only; no readable text, waypoint logic, trail marker gameplay, objective logic, source concept embedding, DCC, Unreal, or startup placement. |
| `BloodAxeStronghold.png#Overlook_Silhouettes` | Overlook silhouettes | `KIT_GIA_BloodAxeApproachOverlookSilhouettes_A01` | Package ready | `docs/assets/kits/KIT_GIA_BloodAxeApproachOverlookSilhouettes_A01/PRODUCTION_PACKAGE.md` and child intake are ready for shadowed ledge outlines, crude rail shapes, banner poles, post clusters, upper-path silhouettes, silhouette-only platform cutouts, scale rows, review composition rows, material discipline, and LOD/collision planning. Intimidation silhouette only; no AI sightline, sentry behavior, climb access, patrol perch, encounter scripting, walkable platform approval, DCC, Unreal, or startup placement. |
| `BloodAxeStronghold.png#Overlook_WatchCutouts` | Watch cutout silhouettes | `SM_GIA_BloodAxeOverlookWatchSilhouette_A01` | Package ready | `docs/assets/props/SM_GIA_BloodAxeOverlookWatchSilhouette_A01/PRODUCTION_PACKAGE.md` is ready for a simplified watch-platform or lookout profile that can reference Blood Axe watch-platform language without approving a tower. Static visual read only; no walkable platform, ladder, ramp, nav link, startup placement, AI sightline, sentry behavior, DCC, or Unreal work. |
| `BloodAxeStronghold.png#Barricade_ChainedPlate` | Chained plate accents | `SM_GIA_BloodAxeChainedPlateBarricade_A01` | Package ready | `docs/assets/props/SM_GIA_BloodAxeChainedPlateBarricade_A01/PRODUCTION_PACKAGE.md` is ready for heavy chained plate, broken shield, blade-fence, and blackened scrap modules for approach choke silhouettes. Static dressing only; no destructible state, damage volume, weak point, cover behavior, loot, salvage, resource behavior, DCC, Unreal, or startup placement. |
| `BloodAxeStronghold.png#Barricade_BladeFenceAccent` | Barricade accents | `SM_GIA_BloodAxeBladeFenceAccent_A01` | Package ready | `docs/assets/props/SM_GIA_BloodAxeBladeFenceAccent_A01/PRODUCTION_PACKAGE.md` is ready for short blade-fence inserts, log chokers, red-marked scrap plates, and rough stone weights. Visual edge control only; no physics, collapse, trap, interaction, collision implementation, destructible behavior, damage behavior, DCC, Unreal, or startup placement. |
| `BloodAxeStronghold.png#GateRelationship_FrameMarkers` | Gate relationship planning | `DOC_GIA_BloodAxeApproachGateRelationship_A01` | Package ready | `docs/assets/kits/DOC_GIA_BloodAxeApproachGateRelationship_A01/PRODUCTION_PACKAGE.md` is ready as docs-only relationship planning for how cliff, palisade, switchback, markers, and barricades frame a future gate. Does not approve final gate art, final stronghold art, entry behavior, nav route, startup placement, DCC, Unreal, final visual approval, or implementation target. |
| `BloodAxeStronghold.png#Review_CompositionMarkers` | Review composition markers | `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01` | Package ready | `docs/assets/kits/KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01/PRODUCTION_PACKAGE.md` and child intake are ready for non-shipping height rods, cliff/palisade silhouette blocks, gate-frame thumbnails, ground ticks, scale rods, camera-composition notes, material discipline markers, and LOD/collision planning rows. No Unreal actor, validator, capture automation, startup scene, final visual signoff, DCC, Unreal, or implementation target. |
| `BloodAxeStronghold.png#Review_ScaleRods` | Giant scale review markers | `SM_GIA_BloodAxeApproachScaleRod_A01` | Package ready | `docs/assets/props/SM_GIA_BloodAxeApproachScaleRod_A01/PRODUCTION_PACKAGE.md` is ready as review-only marker planning for female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines near cliff, wall, and gate-facing silhouettes. No shipped asset, collision, gameplay marker, scale-lock change, DCC, Unreal, startup placement, or implementation target. |
| `BloodAxeStronghold.png#MaterialDiscipline` | Material discipline planning | `DOC_GIA_BloodAxeApproachMaterialDiscipline_A01` | Package ready | `docs/assets/kits/DOC_GIA_BloodAxeApproachMaterialDiscipline_A01/PRODUCTION_PACKAGE.md` is ready as swatch and usage guidance for fractured rock, packed earth, raw timber, blackened iron, chained scrap, scorched hide, oxide red cloth, soot, ash, sparse non-graphic trophies, and excluded neutral/civilized Giant materials. No material instances, textures, material graph, VFX, DCC, Unreal, or final visual approval. |
| `BloodAxeStronghold.png#LODCollisionPlanning` | LOD and collision planning | `DOC_GIA_BloodAxeApproachLODAndCollision_A01` | Package ready | `docs/assets/kits/DOC_GIA_BloodAxeApproachLODAndCollision_A01/PRODUCTION_PACKAGE.md` is ready as LOD0-LOD3 and disabled/simple collision policy for future static modules and review markers. No collision proxies, nav blockers, gameplay volumes, validators, DCC, Unreal, runtime source, or implementation files are created. |

## Dependency Notes

- `SK_GIA_Base_A01` owns Giant scale, skeleton policy, capsule expectations, body proportions, and future character collision assumptions.
- `KIT_GIA_BloodAxeCamp_A01` owns the broader camp route and lists this package as the stronghold approach split.
- `SM_GIA_BloodAxeCampGate_A01` and `SM_GIA_BloodAxeTrophyGate_A01` own camp/trophy gate package planning. This intake only describes approach-to-gate relationship.
- `SM_GIA_BloodAxeWatchPlatform_A01` owns the raised watch-platform package. This intake may reference overlook silhouettes but does not approve walkable platforms.
- `KIT_GIA_BloodAxeFormationDressing_A01` owns non-gameplay review composition marker language.
- `KIT_GIA_BloodAxeArmory_A01` owns Blood Axe chained scrap, weapon, banner, and reforged material language referenced by barricade accents.
- No row in this table is approved as a first DCC, Unreal, runtime, source asset, gameplay, final visual, final stronghold, or implementation target.

## Immediate Package Priority

The kit-level production package and this child intake are ready for docs-only planning review. Later work should choose one planning lane only after lead approval and should remain docs-only unless a new task explicitly expands ownership.

Recommended next docs-only lanes, if requested later:

- Expand `#Cliffs_WallSegments` and `#Palisade_WallSegments` into separate production packages for modular approach walls.
- Expand `#Review_CompositionMarkers` only if art direction needs a tighter A/B gate-framing plan before DCC work.
- Expand `#Barricade_ChainedPlate` only if a separate static barricade child package is approved.

No first implementation target is selected by this intake.

## Approval and Stop Gates

- Stop before final Blood Axe stronghold approval, final approach visual approval, hero screenshot approval, or first playable visual approval.
- Stop before any DCC source, Blender file, terrain sculpt, mesh, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material instance, texture asset, import script, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, or startup placement work.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before selecting a first DCC, Unreal, source asset, or implementation target from any row.
- Stop before defining nav/pathfinding, traversal proofs, climb logic, path widths as gameplay values, encounter design, AI groups, patrol routes, spawn logic, perception, damage values, projectile behavior, cover rules, gate interaction, destructible behavior, objective logic, loot, inventory, rewards, crafting, economy, resource behavior, salvage, pickup behavior, VFX, audio, or interaction behavior.
- Stop before claiming collision correctness, HLOD implementation, terrain integration, gate compatibility, camera-capture approval, marker validation, runtime performance validation, or final silhouette approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Child rows are planning-only and do not define final stronghold approval, final visual approval, implementation targets, terrain work, nav paths, encounter routes, AI spaces, destructible assets, gameplay systems, loot, crafting, economy, or resource loops.
- Rows cover cliff wall segments, approach palisades, switchback path sections, warning markers, overlook silhouettes, chained plate/barricade accents, gate relationship planning, material discipline, LOD/collision planning, and review composition markers.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5", with approved Giant ranges of females 14-15 ft and males 14'10"-16'0".
- Blood Axe remains a hostile Giant sub-faction, not default Giant culture.
- No source concept files are copied, moved, edited, embedded, cropped, renamed, inspected for final approval, or committed.
- No DCC, FBX, Unreal Content, runtime source, validators, startup placements, global indexes, task-board changes, backlog changes, bootstrap changes, AI, combat stats, abilities, loot, crafting, economy, patrol logic, spawn logic, nav/pathfinding, destructible behavior, final visual approval, final stronghold approval, or first build target is claimed.
- Primary approach read stays clear at MMO camera distance: vertical cliffs, rough palisades, switchback shelves, warning markers, overlook silhouettes, chained plate accents, red cloth rhythm, and gate-facing compression.
- Materials use fractured rock, packed earth, raw timber, blackened iron, dark steel, chained scrap, scorched hide, soot, ash, oxide red cloth, and sparse non-graphic bone or horn markers consistently.
- Default emissive, animated material states, gameplay VFX, UI-like route markers, readable tactical text, final gate approval, and neutral/civilized Giant stoneworker language are absent and approval-gated where applicable.
