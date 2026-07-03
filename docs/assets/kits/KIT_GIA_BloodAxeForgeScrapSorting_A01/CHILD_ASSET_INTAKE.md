# KIT_GIA_BloodAxeForgeScrapSorting_A01 Child Asset Intake

## Source

- Source references recorded in existing intake docs: `BloodAxeForge.png#Zone_ScrapSorting` from `KIT_GIA_BloodAxeCamp_A01`.
- Parent context: camp-local forge dressing related to `KIT_GIA_BloodAxeScrapPile_A01`, `KIT_GIA_BloodAxeReforging_A01`, `SM_GIA_BloodAxeForgeHearth_A01`, and future `SM_GIA_BloodAxeAnvilQuench_A01`.
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction.
- Intake status: planning-only child breakdown complete.
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep this hostile sub-faction separate from neutral/civilized Giant culture.
- Source-storage guardrail: source concepts remain in the external concept folder only. Do not copy, move, edit, embed, inspect for visual approval, or commit source images for this docs-only package.

## Notes

This intake is for forge scrap-sorting production planning only. It splits the camp forge scrap zone into sorted metal piles, bent plate stacks, crude bins, broken weapon bundles, quenched slag, path-safe clutter rows, and supporting markers so later workers can create child packages without treating the whole forge yard as one final asset.

All child assets must use the validated `SK_GIA_Base_A01` scale lock before DCC work: female Giant baseline 442 cm / 14'6", male Giant baseline 470 cm / 15'5", with approved race ranges of females 14-15 ft and males 14'10"-16'0". Blood Axe forge-sorting modules should feel Giant-built and hostile while remaining visually separate from neutral/civilized Giant culture, including cave-town masonry, blue-gray stoneworker craft, warm hearth presentation, restrained blue runes, and peaceful highland settlement language.

This intake does not select a first DCC target, approve a final forge visual, create source folders, define encounter behavior, define nav/pathfinding behavior, define loot/resource/crafting/economy behavior, define interaction behavior, or authorize startup placement.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeForge.png#ScrapSorting_SortedMetalPiles` | Sorted metal piles | `SM_GIA_BloodAxeSortedMetalPiles_A01` | Package needed | Low Giant-scale piles of usable blackened metal, plate chunks, cut bars, and snapped blade arcs; visual dressing only, not loot or resource behavior. |
| `BloodAxeForge.png#ScrapSorting_BentPlateStacks` | Bent plate stacks | `SM_GIA_BloodAxeBentPlateStacks_A01` | Package needed | Leaning and stacked warped armor plates, shield faces, failed plates, and broad slab fragments sized for female 442 cm and male 470 cm Giants. |
| `BloodAxeForge.png#ScrapSorting_CrudeBins` | Crude bins | `SM_GIA_BloodAxeCrudeScrapBins_A01` | Package needed | Oversized dark timber and blackened-plate bins with heavy rims, hide lashings, and a few visible large scrap pieces; avoid chest, vendor, or stash readability. |
| `BloodAxeForge.png#ScrapSorting_BrokenWeaponBundles` | Broken weapon bundles | `SM_GIA_BloodAxeBrokenWeaponBundles_A01` | Package needed | Tied or chained snapped axe heads, cleaver pieces, spear tips, ruined blade fragments, and damaged fittings; no pickup, salvage, or loot behavior. |
| `BloodAxeForge.png#ScrapSorting_QuenchedSlag` | Quenched slag | `SM_GIA_BloodAxeQuenchedSlag_A01` | Package needed | Matte cooled slag, ash banks, shallow crusted trays, dark residue, and quench stains; no heat damage, steam VFX, or resource-node behavior. |
| `BloodAxeForge.png#ScrapSorting_PathSafeClutterRows` | Path-safe clutter rows | `KIT_GIA_BloodAxePathSafeClutterRows_A01` | Package needed | Low row modules that flank Giant-scale forge lanes with deliberate spacing, row end caps, sparse vertical markers, and red cloth tags; visual layout guidance only, not navmesh or pathfinding behavior. |
| `BloodAxeForge.png#ScrapSorting_SortMarkers` | Sorting markers | `SM_GIA_BloodAxeScrapSortMarkers_A01` | Package needed | Crude stakes, hammered plaques, and red tags to separate usable stock, bent plates, broken weapon bundles, and slag without relying on tiny readable text. |
| `BloodAxeForge.png#ScrapSorting_ComposedCluster` | Composed sorting cluster | `SM_GIA_BloodAxeForgeScrapSortingCluster_A01` | Optional package candidate | Optional composed non-interactive layout using the child rows above for a ready-to-place forge-yard dressing cluster; startup placement and first DCC target selection remain out of scope. |

## Immediate Package Priority

The kit-level package is ready for planning review. All child rows are future package candidates only. Future work should choose a child package lane only after lead approval, visual direction approval, and confirmation that the selected child does not require new Giant scale assumptions.

No first DCC target is selected by this intake.

## Approval Gates

- Stop before any DCC, FBX, Unreal Content, runtime, source asset, validator, material graph, Blueprint, VFX, or startup-scene work.
- Stop before copying, embedding, moving, cropping, editing, inspecting for approval, or committing source concept images.
- Stop before final forge visual approval or first playable visual approval.
- Stop before selecting a first DCC target.
- Stop before defining encounter behavior, AI patrols, combat cover, nav/pathfinding behavior, heat damage, damage volumes, destructible behavior, loot tables, pickup behavior, inventory behavior, resource behavior, crafting behavior, salvage behavior, vendor behavior, economy behavior, workstation behavior, or interaction behavior.
- Stop if Blood Axe visual language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock or socket assumptions from `SK_GIA_Base_A01`.
