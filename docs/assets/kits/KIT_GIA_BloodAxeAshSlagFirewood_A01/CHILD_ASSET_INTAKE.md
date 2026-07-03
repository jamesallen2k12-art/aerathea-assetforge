# KIT_GIA_BloodAxeAshSlagFirewood_A01 Child Asset Intake

## Source

- Parent kit: `KIT_GIA_BloodAxeCamp_A01`
- Source route reference: `BloodAxeForge.png#Clutter_AshSlagFirewood`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction.
- Intake status: first-pass planning-only child breakdown complete.
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep this sub-faction separate from neutral/civilized Giant culture.
- Source-storage guardrail: source concepts remain in the external concept folder only. Do not copy, move, edit, crop, embed, inspect for visual approval, rename, or commit source images for this docs-only package.

## Notes

This intake splits ash, slag, charcoal, firewood, scorched debris, and review composition rows into buildable future child assets. It supports hostile Blood Axe camp and forge-yard dressing while keeping every child static, inert, and non-interactive.

All child assets must use the validated `SK_GIA_Base_A01` scale lock before DCC work: female Giant baseline 442 cm / 14'6", male Giant baseline 470 cm / 15'5", with approved race ranges of females 14-15 ft and males 14'10"-16'0". Blood Axe camp clutter should feel Giant-built, hostile, soot-heavy, and temporary while remaining visually separate from neutral/civilized Giant cave-town masonry, blue-gray stoneworker craft, warm civic hearths, restrained blue runes, terraces, and waterworks.

This intake does not select a first DCC target, approve a final visual direction, create source folders, define gatherable resource behavior, define heat or damage behavior, author VFX or material graphs, define crafting or economy behavior, define interaction behavior, create startup placement, or authorize Unreal implementation.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeForge.png#Clutter_AshPiles_LowBanks` | Ash piles | `SM_GIA_BloodAxeAshPiles_A01` | Package-ready; docs-only | Low wind-swept ash banks, shoveled mounds, dark soot cores, and pale edges for forge and cooking-pit dressing. Static visual clutter only; no heat, ash drift, damage, gatherable resource, crafting, or interaction behavior. |
| `BloodAxeForge.png#Clutter_AshPiles_FootprintDrifts` | Ash piles | `SM_GIA_BloodAxeAshDrifts_A01` | Package-ready; docs-only | Thin ash drifts for hearth base edges, path corners, and shelter thresholds. Keep low, broad, and cheap; no terrain blending, startup placement, VFX, or collision proxy approval. |
| `BloodAxeForge.png#Clutter_SlagLumps_CooledClumps` | Slag lumps | `SM_GIA_BloodAxeSlagLumps_A01` | Package-ready; docs-only | Cooled black-gray slag clumps and rough spill clusters with matte crusts. Must not read as ore, loot, salvage, crafting input, harvestable resource, or economy item. |
| `BloodAxeForge.png#Clutter_SlagLumps_SpillStrips` | Slag lumps | `SM_GIA_BloodAxeSlagSpillStrips_A01` | Package-ready; docs-only | Low elongated slag spill strips for edges near forge hearth and anvil/quench props. Keep separate from `SM_GIA_BloodAxeAnvilQuench_A01`; no heat damage, VFX, or material graph authoring. |
| `BloodAxeForge.png#Clutter_CharcoalHeaps_CrushedFuel` | Charcoal heaps | `SM_GIA_BloodAxeCharcoalHeaps_A01` | Package-ready; docs-only | Broken matte black charcoal chunks in broad heaps with a few large top pieces. Static fuel residue only; no pickup, fuel count, crafting, cooking, economy, or interaction behavior. |
| `BloodAxeForge.png#Clutter_CharcoalHeaps_ShallowBins` | Charcoal heaps | `SM_GIA_BloodAxeCharcoalBins_A01` | Package-ready; docs-only | Shallow crude tray or half-bin variants for charcoal and black dust. Use simple forms and one material where possible; no workstation, inventory, resource, heat, or VFX behavior. |
| `BloodAxeForge.png#Clutter_FirewoodStacks_GiantLogs` | Firewood stacks | `SM_GIA_BloodAxeFirewoodStacks_A01` | Package-ready; docs-only | Giant-scale stacked logs, split trunks, crib stacks, and charred end caps sized against female 442 cm and male 470 cm Giants. Do not make them gatherable, consumable, pickup-enabled, destructible, or craftable. |
| `BloodAxeForge.png#Clutter_FirewoodStacks_TiedBundles` | Firewood stacks | `SM_GIA_BloodAxeFirewoodBundles_A01` | Package-ready; docs-only | Tied rough log bundles and kindling groups using heavy rope, hide straps, and sparse red tags. Keep bundle silhouettes broad; no physics simulation, inventory, economy, resource, or interaction behavior. |
| `BloodAxeForge.png#Clutter_ScorchedDebris_BurntBeams` | Scorched debris | `SM_GIA_BloodAxeScorchedDebris_A01` | Package-ready; docs-only | Burned beams, snapped stakes, broken planks, ash-stained stones, and rare bent metal scraps for camp-edge dressing. Static non-graphic debris only; no destructible, cover, loot, resource, heat, damage, or startup behavior. |
| `BloodAxeForge.png#Clutter_ScorchedDebris_EdgeScatter` | Scorched debris | `SM_GIA_BloodAxeDebrisEdgeScatter_A01` | Package-ready; docs-only | Low edge scatter rows for forge perimeter and path corners, with restrained red cloth tags and blackened hardware fragments. Keep separate from path markers, barricades, and scrap sorting; no nav, collision, interaction, or economy behavior. |
| `BloodAxeForge.png#Review_Row_AshSlagCharcoal` | Review composition rows | `KIT_GIA_BloodAxeAshSlagReviewRows_A01` | Package-ready; docs-only | Ordered review row comparing ash piles, slag lumps, and charcoal heaps at consistent scale and material density. Review composition only; no startup placement, final visual approval, DCC target selection, or gameplay behavior. |
| `BloodAxeForge.png#Review_Row_FirewoodDebris` | Review composition rows | `KIT_GIA_BloodAxeFirewoodDebrisReviewRows_A01` | Package-ready; docs-only | Ordered review row comparing Giant logs, tied bundles, scorched beams, and debris-edge scatter against the 442 cm female and 470 cm male Giant baselines. Review composition only; no Unreal placement, nav, collision, interaction, or resource behavior. |
| `BloodAxeForge.png#Review_Row_ComposedForgeClutter` | Review composition rows | `SM_GIA_BloodAxeForgeClutterCluster_A01` | Package-ready; docs-only | Optional composed static cluster for later review of ash, slag, charcoal, firewood, and scorched debris beside forge-adjacent space. Do not merge forge hearth, anvil/quench, scrap sorting, cooking, or path-marker content into this cluster. |

## Review Composition Rows

Future review rows should remain layout aids, not gameplay scenes.

- Row A: ash piles, ash drifts, slag lumps, slag spill strips, and charcoal heaps arranged in a flat comparison line.
- Row B: firewood stacks, firewood bundles, scorched debris, and debris-edge scatter arranged in a second comparison line.
- Row C: composed forge-clutter cluster with enough negative space to show Giant-scale work-lane clearance, but no startup placement.
- Row D: material-density comparison row showing low, medium, and high soot/ash coverage without changing the child asset identity.
- Row E: LOD-read row where the broad ash/slag/charcoal/wood/debris silhouettes remain readable after small details are removed.

Review rows must include explicit scale comparison to female 442 cm / 14'6" and male 470 cm / 15'5" Giants before any future DCC or Unreal review. They must not include interaction markers, resource icons, heat warnings, VFX sockets, crafting signs, loot beams, quest labels, or final visual approval framing.

## Dependency Boundaries

- `SM_GIA_BloodAxeForgeHearth_A01` owns the main forge hearth, windbreak, basin, and forge focal silhouette.
- `SM_GIA_BloodAxeAnvilQuench_A01` owns the anvil block, quench trough, slag tray, cooling rack, and workstation-adjacent silhouette.
- `KIT_GIA_BloodAxeForgeScrapSorting_A01` owns organized metal stock, bent plate stacks, crude bins, broken weapon bundles, sorted scrap, and path-safe metal rows.
- `SM_GIA_BloodAxeCookingPit_A01` owns the cooking pit and non-graphic cooking fire composition.
- `KIT_GIA_BloodAxeAshSlagFirewood_A01` owns only ash piles, slag lumps, charcoal heaps, firewood stacks, scorched debris, and review composition rows.

Do not collapse these sibling packages into one mesh or one behavior definition. This intake is a planning split only.

## Immediate Package Priority

The kit-level production package, child package rows, review rows, policy rows, implementation readiness matrix, and package closure note are package-ready at docs-only level after `AET-MA-20260629-449` validation. This is not an implementation approval. Future work should choose a child build lane only after lead approval, visual direction approval, and confirmation that the selected child does not require new Giant scale assumptions.

No first DCC target or implementation target is selected by this intake.

## Approval Gates

- Stop before any DCC, FBX, Unreal Content, runtime, source asset, validator, material graph, Blueprint, VFX, or startup-scene work.
- Stop before copying, embedding, moving, cropping, editing, inspecting for visual approval, renaming, or committing source concept images.
- Stop before final camp visual approval, final clutter visual approval, first playable visual approval, or first DCC target selection.
- Stop before defining gatherable resources, firewood pickups, charcoal pickups, slag harvesting, loot, salvage, crafting, cooking, economy, inventory, vendors, workstation behavior, interaction prompts, heat damage, burn damage, damage volumes, destructible behavior, physics simulation, cover behavior, nav/pathfinding, or encounter behavior.
- Stop before authoring active flames, smoke, sparks, heat shimmer, ash drift, ember particles, emissive maps, material graph behavior, Niagara systems, audio cues, or animation.
- Stop if Blood Axe visual language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock or socket assumptions from `SK_GIA_Base_A01`.

## Quality Gate Checklist

- Child intake covers ash piles, slag lumps, charcoal heaps, firewood stacks, scorched debris, and review composition rows.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Validated Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- All children are static visual camp/forge clutter only.
- No child row defines gatherable resource behavior, heat or damage behavior, VFX or material graph authoring, crafting or economy behavior, interaction behavior, startup placement, or first DCC target selection.
- Forge hearth, anvil/quench, scrap sorting, cooking pit, path marker, barricade, and shelter ownership boundaries are preserved.
- Child names use `GIA` and `BloodAxe` naming to keep hostile Blood Axe culture distinct from neutral/civilized Giant culture.
- Review rows are described as future layout aids only, not final visual approval or Unreal startup placement.
- Source concept storage guardrail is explicit.
