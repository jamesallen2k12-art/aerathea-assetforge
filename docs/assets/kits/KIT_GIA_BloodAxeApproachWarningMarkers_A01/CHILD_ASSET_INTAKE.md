# KIT_GIA_BloodAxeApproachWarningMarkers_A01 Child Asset Intake

## Source

- Parent kit: `KIT_GIA_BloodAxeStrongholdApproach_A01`
- Parent intake row: `BloodAxeStronghold.png#Markers_WarningStakes`
- Source route reference: `BloodAxeStronghold.png#Gate_StrongholdApproach` as listed by the existing Blood Axe stronghold approach intake docs
- Related docs: `KIT_GIA_BloodAxeStrongholdApproach_A01`, `KIT_GIA_BloodAxePathMarkers_A01`, `SM_GIA_BloodAxeBoneHornMarker_A01`, `KIT_GIA_BloodAxeApproachCliffWalls_A01`, `KIT_GIA_BloodAxeSwitchbackPathSections_A01`, `SM_GIA_BloodAxeApproachPalisadeWall_A01`, and `KIT_GIA_BloodAxeFormationDressing_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only child split complete for approach warning-marker planning; no child build target selected
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture
- Scale dependency: validated `SK_GIA_Base_A01` female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: external source concepts remain in the external concept folder only. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This child intake splits `KIT_GIA_BloodAxeApproachWarningMarkers_A01` into planning-only rows for red cloth stakes, horn markers, broken shield tokens, blade fragments, rough warning posts, mixed marker clusters, scale rows, review composition rows, material discipline, and LOD/collision planning.

Blood Axe warning-marker dressing must stay separate from neutral/civilized Giant culture. It may use scorched timber, rough field stone, hide ties, rope, blackened iron, dark steel, blade scraps, broken shield fragments, soot, ash, mud, oxide red cloth, and sparse non-graphic horn or bone markers. It must not reuse civilized Giant cave-town masonry, blue-gray civic stonework, terrace/waterwork forms, warm hearth identity, refined stoneworker craft language, peaceful highland wayfinding, or restrained blue-rune culture as the default read.

`KIT_GIA_BloodAxePathMarkers_A01` owns the broader low route-marker language for camp paths. This approach warning-marker kit owns harsher threshold and stronghold-approach warnings only, with no objective marker, quest marker, UI symbol, aura behavior, damage behavior, pickup behavior, loot behavior, or interaction behavior.

Every row below is planning only. No row creates or authorizes DCC source, FBX export, Unreal Content, runtime source, tools, validators, startup placement, source concept movement, final visual approval, final stronghold approval, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeStronghold.png#Markers_RedClothStakes_A01` | Red cloth stakes | `SM_GIA_BloodAxeRedClothWarningStake_A01` | Planning row ready; planning only | Scorched timber stake with one broad torn oxide red cloth piece, hide wrap, soot-dark base, and irregular Giant-made placement. Static visual warning only; no objective marker, quest marker, UI symbol, aura, damage, pickup, loot, interaction behavior, cloth simulation, DCC, Unreal, startup placement, or first implementation target. |
| `BloodAxeStronghold.png#Markers_RedClothStakeRow_A01` | Red cloth stakes | `KIT_GIA_BloodAxeRedClothWarningStakeSet_A01` | Planning row ready; planning only | Two to five uneven red cloth stakes for approach rhythm near switchback bends or palisade flanks. Must not become a fence, route arrow, capture flag line, waypoint path, objective boundary, nav blocker, collision claim, DCC target, Unreal target, or final visual approval. |
| `BloodAxeStronghold.png#Markers_HornWarningMarker_A01` | Horn markers | `SM_GIA_BloodAxeHornWarningMarker_A01` | Planning row ready; planning only | One dominant old horn fork or blunt horn pair lashed to a stake, low cairn, or mud base. Sparse non-graphic warning only; no gore escalation, ritual behavior, signal device, aura, VFX pulse, loot, pickup, crafting resource, DCC, Unreal, or startup placement. |
| `BloodAxeStronghold.png#Markers_LowHornToken_A01` | Horn markers | `SM_GIA_BloodAxeLowHornWarningToken_A01` | Planning row ready; planning only | Low horn token or horn cap tied to stone, shield scrap, or post base for near-ground approach reads. Visual hostility only; no collectible token, inventory item, resource node, trail gameplay, objective logic, source concept movement, or first implementation target. |
| `BloodAxeStronghold.png#Markers_BrokenShieldToken_A01` | Broken shield tokens | `SM_GIA_BloodAxeBrokenShieldWarningToken_A01` | Planning row ready; planning only | Large broken shield shard, dull rim, rope tie, and chipped red paint used as a static warning token. No usable shield, pickup, loot, salvage, crafting/economy behavior, destructible behavior, cover rule, interaction behavior, DCC, Unreal, or final approval. |
| `BloodAxeStronghold.png#Markers_ShieldScrapPair_A01` | Broken shield tokens | `KIT_GIA_BloodAxeShieldScrapWarningPair_A01` | Planning row ready; planning only | Pair of shield fragments at a cliff base or switchback edge, sized against 442 cm and 470 cm Giant baselines. Static composition only; no collision correctness, nav/pathfinding, objective marker, item affordance, startup placement, or first build target. |
| `BloodAxeStronghold.png#Markers_BladeFragment_A01` | Blade fragments | `SM_GIA_BloodAxeBladeFragmentWarning_A01` | Planning row ready; planning only | Dull blade shard embedded in timber, mud, stone, or shield scrap as intimidation dressing. No weapon pickup, loot drop, damage volume, trap behavior, combat cover, salvage resource, crafting material, physics setup, DCC, Unreal, or interaction behavior. |
| `BloodAxeStronghold.png#Markers_BladeShardCluster_A01` | Blade fragments | `KIT_GIA_BloodAxeBladeShardWarningCluster_A01` | Planning row ready; planning only | Small cluster of two or three large dull blade fragments with soot, mud, and red cloth support accents. Visual warning cluster only; no hazard, damage, destructible behavior, loot, pickup, objective marker, nav helper, final visual approval, or first implementation target. |
| `BloodAxeStronghold.png#Markers_RoughWarningPost_A01` | Rough warning posts | `SM_GIA_BloodAxeRoughWarningPost_A01` | Planning row ready; planning only | Taller split-log or scorched post with hide wraps, rope, optional horn cap, and one broad red cloth or shield scrap accent. Static post only; no banner-line ownership, cloth wind, interaction prompt, waypoint logic, quest symbol, startup placement, DCC, or Unreal. |
| `BloodAxeStronghold.png#Markers_PostWithScrapCap_A01` | Rough warning posts | `SM_GIA_BloodAxeScrapCapWarningPost_A01` | Planning row ready; planning only | Rough post with blackened iron scrap, dull blade cap, or broken shield rim at the top. Keep as visual approach dressing; no trap, damage, destructible setup, salvage, loot, pickup, resource behavior, source asset creation, or final stronghold approval. |
| `BloodAxeStronghold.png#Markers_MixedWarningCluster_A01` | Mixed marker clusters | `KIT_GIA_BloodAxeApproachWarningCluster_A01` | Planning row ready; planning only | Composed warning cluster using one red cloth stake, one horn marker, one broken shield token, one blade fragment, and ash/mud base. Review composition only until later approval; no DCC, Unreal, startup placement, final visual approval, final stronghold approval, or first implementation target. |
| `BloodAxeStronghold.png#Markers_ThresholdCluster_A01` | Mixed marker clusters | `KIT_GIA_BloodAxeThresholdWarningCluster_A01` | Planning row ready; planning only | Wider hostile threshold cluster for the approach foreground, palisade flank, or cliff choke. Must stay sparse and readable; no gate approval, nav/pathfinding, encounter scripting, AI space, collision proxy, objective logic, UI symbol, or implementation claim. |
| `BloodAxeStronghold.png#Markers_ScaleRows_A01` | Scale rows | `DOC_GIA_BloodAxeApproachWarningScaleRows_A01` | Planning row ready; planning only | Non-shipping scale rows showing female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines beside red cloth stakes, horn markers, shield tokens, blade fragments, rough posts, and mixed clusters. No shipped marker, scale-lock change, Unreal actor, validator, capture, startup placement, or final approval. |
| `BloodAxeStronghold.png#Markers_ReviewCompositionRows_A01` | Review composition rows | `DOC_GIA_BloodAxeApproachWarningReviewRows_A01` | Planning row ready; planning only | Docs-only review rows comparing approach rhythm, foreground/midground marker density, cliff-base readability, palisade-flank readability, and camera-distance silhouette separation. No capture approval, Unreal actor, validator, source concept movement, final visual signoff, or first implementation target. |
| `BloodAxeStronghold.png#Markers_MaterialDiscipline_A01` | Material discipline | `DOC_GIA_BloodAxeApproachWarningMaterialDiscipline_A01` | Planning row ready; planning only | Planning only for scorched timber, oxide red cloth, old horn, dull bone, broken shield wood, blackened iron, dark steel, blade fragments, rough field stone, mud, soot, ash, hide, and rope. Excludes neutral/civilized Giant cave-town materials, refined wayfinding, blue runes, default emissive, material instance creation, or texture creation. |
| `BloodAxeStronghold.png#Markers_LODCollisionPlanning_A01` | LOD/collision planning | `DOC_GIA_BloodAxeApproachWarningLODAndCollision_A01` | Planning row ready; planning only | Planning only for LOD0-LOD3 reduction order and disabled/simple collision policy for future static warning markers and review rows. No collision proxies, nav blockers, gameplay volumes, damage volumes, aura volumes, objective volumes, validators, Unreal Content, DCC source, or source asset creation. |

## Dependency Notes

- `KIT_GIA_BloodAxeStrongholdApproach_A01` owns the broader stronghold approach split. This child intake only expands the `#Markers_WarningStakes` lane.
- `KIT_GIA_BloodAxePathMarkers_A01` owns broad camp path-marker language. This warning-marker kit should stay harsher, more threshold-focused, and more approach-facing.
- `SM_GIA_BloodAxeBoneHornMarker_A01` owns the existing sparse bone/horn territory-marker package. Horn marker rows here may reference its material and silhouette discipline but do not replace it.
- `KIT_GIA_BloodAxeApproachCliffWalls_A01` and `KIT_GIA_BloodAxeSwitchbackPathSections_A01` own cliff and path-section planning. Warning marker rows may sit visually near those modules but do not define terrain, nav, route widths, traversal, or collision correctness.
- `SM_GIA_BloodAxeApproachPalisadeWall_A01` owns approach palisade wall planning. Warning marker rows may support palisade-flank dressing but do not approve wall art, gate art, destructible behavior, or cover rules.
- `KIT_GIA_BloodAxeFormationDressing_A01` owns non-gameplay review composition language. This intake borrows docs-only review discipline without creating Unreal actors, validators, captures, or startup placement.
- `SK_GIA_Base_A01` owns Giant scale, skeleton policy, capsule expectations, and character collision assumptions. This intake does not change those contracts.
- No row in this table is approved as a first DCC, Unreal, runtime, source asset, gameplay, final visual, final stronghold, or implementation target.

## Unordered Future Package Candidates

No first DCC target, source asset target, Unreal target, or implementation target is selected by this intake. If a later lead-approved package lane is opened, any of these may be promoted independently:

- `SM_GIA_BloodAxeRedClothWarningStake_A01`
- `KIT_GIA_BloodAxeRedClothWarningStakeSet_A01`
- `SM_GIA_BloodAxeHornWarningMarker_A01`
- `SM_GIA_BloodAxeLowHornWarningToken_A01`
- `SM_GIA_BloodAxeBrokenShieldWarningToken_A01`
- `KIT_GIA_BloodAxeShieldScrapWarningPair_A01`
- `SM_GIA_BloodAxeBladeFragmentWarning_A01`
- `KIT_GIA_BloodAxeBladeShardWarningCluster_A01`
- `SM_GIA_BloodAxeRoughWarningPost_A01`
- `SM_GIA_BloodAxeScrapCapWarningPost_A01`
- `KIT_GIA_BloodAxeApproachWarningCluster_A01`
- `KIT_GIA_BloodAxeThresholdWarningCluster_A01`
- `DOC_GIA_BloodAxeApproachWarningScaleRows_A01`
- `DOC_GIA_BloodAxeApproachWarningReviewRows_A01`
- `DOC_GIA_BloodAxeApproachWarningMaterialDiscipline_A01`
- `DOC_GIA_BloodAxeApproachWarningLODAndCollision_A01`

## Approval Gates

- Stop before final Blood Axe stronghold approval, final approach visual approval, hero screenshot approval, camera-capture approval, or first playable visual approval.
- Stop before DCC source, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content asset, material instance, texture asset, material graph, import script, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, startup placement, or any source asset creation.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before selecting a first DCC, Unreal, source asset, or implementation target from any row.
- Stop before defining objective markers, quest markers, UI symbols, waypoint logic, trail-marker gameplay, nav/pathfinding, traversal proofs, climb logic, path widths as gameplay values, encounter design, AI spaces, patrol routes, spawn logic, perception, damage values, aura behavior, projectile behavior, cover rules, trap behavior, destructible behavior, objective logic, loot, inventory, rewards, crafting, economy, resource behavior, salvage, pickup behavior, VFX, audio, or interaction behavior.
- Stop before claiming collision correctness, terrain integration, gate compatibility, runtime performance validation, marker validation, final silhouette approval, or final stronghold approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, bootstrap, or unrelated package file.
- Rows cover red cloth stakes, horn markers, broken shield tokens, blade fragments, rough warning posts, mixed marker clusters, scale rows, review composition rows, material discipline, and LOD/collision planning.
- Every child row is marked planning only and avoids objective markers, quest markers, UI symbols, aura behavior, damage behavior, pickup behavior, loot behavior, interaction behavior, DCC, FBX, Unreal, startup placement, source concept movement, final visual approval, final stronghold approval, and first implementation claims.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Rows are useful for future package planning without selecting a first DCC, Unreal, source asset, or implementation target.
- Review rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, marker validation, camera approval, or final visual signoff.
- Materials use scorched timber, oxide red cloth, old horn, dull bone, broken shield wood, blackened iron, dark steel, blade fragments, rough field stone, mud, soot, ash, hide, and rope consistently.
- Default emissive, ritual glow, shamanic glow, signal glow, animated material states, gameplay VFX, UI-like markers, readable text, and neutral/civilized Giant language are absent and approval-gated.
- Tiny cloth weave, fray, stitches, scratches, pitting, soot speckles, ash flecks, paint chips, horn rings, blade nicks, shield dents, and wood grain are assigned to textures or normals in future packages.
- No terrain sculpt, landscape import, nav/pathfinding, traversal proof, collision correctness, collision proxy creation, encounter scripting, AI behavior, destructible behavior, gameplay/loot/economy/crafting/resource behavior, startup placement, source concept movement, final stronghold approval, final visual approval, or implementation claim is made.
