# KIT_GIA_BloodAxeReforging_A01 Child Asset Intake

## Source

- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/BloodAxeArmory.png`
- Source region: `BloodAxeArmory.png#Forge_RaidedReforged_Process`
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Related feedstock kit: `KIT_GIA_BloodAxeScrapPile_A01`
- Material dependency: `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Intake status: first-pass reforging-process child breakdown complete
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in asset names to keep this hostile sub-faction separate from neutral/civilized Giant culture
- Source-storage guardrail: source concept remains in the external concept folder only. Do not copy, move, edit, embed, or commit the source image for this docs-only package.

## Notes

This intake covers the Blood Axe reforging-process subset from the armory catalog. It is a process storytelling kit, not a gameplay object. Children should support reusable forge-yard and armory layouts while staying clearly non-interactive.

Giant scale lock: female Giants 14-15 ft / 427-457 cm; male Giants 14'10"-16'0" / 452-488 cm. Use the `SK_GIA_Base_A01` baselines where applicable: female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5".

All children must preserve Blood Axe hostile raider identity through blackened iron, dark steel, hammered stolen scrap, soot, ash, chipped oxide-red paint, torn red cloth warnings, heavy chain, crude forge marks, and scorched support materials. They must not import neutral/civilized Giant blue-gray stoneworker language, warm hearth identity, peaceful highland craft, or restrained blue rune language into this sub-faction kit.

Docs-only guardrails: no DCC, FBX, Unreal import, crafting system, economy/resource behavior, material graph authoring, source concept copying, startup placement, or final visual approval.

This package does not create DCC source, FBX exports, Unreal Content assets, runtime source, startup-scene placement, gameplay pickups, loot nodes, resource harvesting, salvage systems, destructible props, crafting systems, economy data, material graphs, shaders, copied concept art, or final visual approval.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Variant scope | Material dependency | LOD0 target | Material slots | Collision and pivot plan | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BloodAxeArmory.png#Reforging_StolenScrapIntake_A01` | Stolen scrap intake | `SM_GIA_BloodAxeStolenScrapIntake_A01` | Seized shields, armor plates, hacked weapon bundles, chain-bound piles, red warning tags, and receiving ground cluster | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional support cloth/leather | 5k-12k tris | 1-2 | Grouped low-count convex hulls or boxes; pivot at ground center of cluster footprint | Defined in kit package | Reads as stolen metal arriving for breakdown, not loot, treasure, resource stock, or pickup. Keep seized pieces Giant-readable and hostile. |
| `BloodAxeArmory.png#Reforging_BrokenMetalSorting_A01` | Broken metal sorting | `SM_GIA_BloodAxeBrokenMetalSorting_A01` | Sorting surface, ground sort, split blade arcs, cracked plates, snapped spearheads, and sorted bins | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional scorched support material | 4k-10k tris | 1-2 | Simple table/bin footprint boxes or low-count hulls; pivot at ground center | Defined in kit package | Shows the Blood Axe process of breaking stolen metal apart. Avoid dwarven precision or neutral Giant craft symbols. |
| `BloodAxeArmory.png#Reforging_BilletIngotStacks_A01` | Billets and ingots | `SM_GIA_BloodAxeBilletIngotStacks_A01` | Rough bars, billet stacks, ingot slabs, cut plates, transport bundles, and prepared Giant-scale stock | `MI_GIA_BloodAxeReforgedMetal_A01` | 1.5k-5k tris per stack set | 1 | Grouped box or low-count convex hull per stack; pivot at stack base/contact center | Defined in kit package | Bridges scrap pile feedstock and heated blanks. Do not attach inventory, economy, crafting, or resource-node behavior. |
| `BloodAxeArmory.png#Reforging_HeatedBlanks_A01` | Heated blanks | `SM_GIA_BloodAxeHeatedBlanks_A01` | Axe-head blanks, cleaver slabs, hammer blocks, hook-spear forms, socket collars, and plate blanks in hot-work stage | `MI_GIA_BloodAxeReforgedMetal_A01`; future heat state approval-gated | 2k-7k tris per blank-stage set | 1-2 | Simple bounds for display placement only; pivot at blank underside or support contact point | Defined in kit package | Baseline is visual storytelling only. No burn damage, hazard volume, heat shader, material graph, crafting trigger, or gameplay interaction is included. |
| `BloodAxeArmory.png#Reforging_RemadeWeaponStages_A01` | Remade weapon stages | `KIT_GIA_BloodAxeRemadeWeaponStages_A01` | Progression pieces from rough blank to Blood Axe axe head, cleaver blade, hammer face, hook spear head, and fittings | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional handle/support material | 6k-14k tris for staged set | 1-2 | Simple box/capsule/convex hull per displayed stage; pivots at display support contact centers | Defined in kit package | Communicates remaking process before final weapon packages. Functional grip pivots and combat traces belong to future weapon tasks. |
| `BloodAxeArmory.png#Reforging_CoolingRack_A01` | Cooling racks | `SM_GIA_BloodAxeCoolingRack_A01` | Wide Giant rack frame, heavy hooks, crossbars, blank rests, cooling rows, and red cloth safety tags | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional scorched support material | 5k-12k tris | 1-2 | Rack footprint collision and optional upper bounds; pivot at ground center of rack footprint | Defined in kit package | Static display rack only. No per-hook collision, physics hanging, heat timing, or interaction prompt. |
| `BloodAxeArmory.png#Reforging_QuenchTrough_A01` | Quench trough | `SM_GIA_BloodAxeQuenchTrough_A01` | Long dark trough, reinforced rim, residue plane, ash crust, tongs/rest points, quench staining, and soot | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional dark water/residue material | 4k-9k tris | 1-2 | Outer trough hull and optional shell blocking; pivot at ground center aligned to long axis | Defined in kit package | Set dressing only. No water interaction, steam VFX, burn volume, crafting trigger, hazard damage, or resource behavior. |
| `BloodAxeArmory.png#Reforging_ProcessMarkers_A01` | Process signage and markers | `SM_GIA_BloodAxeProcessMarkers_A01` | Crude red-cloth tags, hammered metal direction markers, tally stakes, warning plaques, and Blood Axe sub-faction marks | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional red cloth/support material | 800-3k tris per marker set | 1-2 | Simple box/capsule only if standalone; pivot at stake/plaque base center | Defined in kit package | Use large symbols and broad marks instead of small readable text. Do not add quest, crafting, recipe, vendor, or resource labels. |
| `BloodAxeArmory.png#Reforging_ProcessComposed_A01` | Composed process layout | `SM_GIA_BloodAxeReforgingProcess_A01` | Optional ready-to-place non-interactive layout assembled from child props | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional support material | 18k-35k tris | 1-2 | Grouped display collision with walkable collision disabled by default; pivot at ground center of full process footprint | Defined in kit package | Optional assembly for level dressing. Must remain inert set dressing unless a later task approves gameplay behavior. |

## Placement and Use Rules

- Use child meshes near Blood Axe armories, forge yards, barracks, weapon racks, scrap piles, camp work areas, and boss staging spaces.
- Keep the process readable beside a 470 cm male Giant and within the approved Giant scale lock.
- Use the kit to communicate hostile Blood Axe reforging practice, not player crafting or economy value.
- Keep flow order legible when used as a layout: stolen scrap, broken metal, billets/ingots, heated blanks, remade weapon stages, cooling racks, quench trough, process signage/markers.
- Use `MI_GIA_BloodAxeReforgedMetal_A01` as a docs-only material dependency for primary metal surfaces. Do not author material graphs, shaders, material instances, or texture assets from this intake.
- Do not place neutral Giant blue-gray stoneworker ornament, warm hearth presentation, peaceful masonry motifs, highland nomad craft marks, or restrained blue rune language in this hostile sub-faction kit.
- Keep gore absent or only implied through non-graphic hostile camp dressing. The process should primarily read as metal reforging.
- Keep collision simple and display-only. No per-shard, per-chain, pickup, harvest, crafting, hazard, or destructible collision.

## Immediate Package Priority

Suggested promotion order for future child package or DCC work:

1. `SM_GIA_BloodAxeBilletIngotStacks_A01`
2. `SM_GIA_BloodAxeHeatedBlanks_A01`
3. `KIT_GIA_BloodAxeRemadeWeaponStages_A01`
4. `SM_GIA_BloodAxeCoolingRack_A01`
5. `SM_GIA_BloodAxeQuenchTrough_A01`
6. `SM_GIA_BloodAxeBrokenMetalSorting_A01`
7. `SM_GIA_BloodAxeStolenScrapIntake_A01`
8. `SM_GIA_BloodAxeProcessMarkers_A01`
9. `SM_GIA_BloodAxeReforgingProcess_A01`

## Approval Gates

- Stop before DCC source creation, FBX export, Unreal Content asset creation, runtime source changes, Unreal import, startup-scene placement, final visual approval, or source-concept copying.
- Stop before adding gameplay pickup, loot, resource harvesting, salvage, crafting, economy, vendor, inventory, destructible, physics-simulation, heat hazard, water interaction, recipe, upgrade, or encounter-cover behavior.
- Stop before authoring material graphs, shaders, texture assets, material instances, heat-state effects, emissive maps, VFX, or validators.
- Stop if the kit collapses stolen scrap, broken metal, billets/ingots, heated blanks, remade weapon stages, cooling racks, quench trough, and process signage/markers into one uneditable mesh assumption.
- Stop if collision becomes dense per-shard, per-chain, per-hook, or interaction-volume collision rather than simple display collision.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock or `SK_GIA_Base_A01` assumptions without a new approval task.
