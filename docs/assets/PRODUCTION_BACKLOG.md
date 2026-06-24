# Aerathea Production Backlog

## Scan Sources

- `AGENTS.md`
- `docs/PRODUCTION_BOOTSTRAP.md`
- `docs/assets/ASSET_INDEX.md`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`
- `docs/assets/ASSET_CONCEPTS_MANIFEST.md`

This file tracks approved races, creatures, buildings, props, armory assets, UI assets, and blueprint candidates that still need production packages or game-ready assets. It does not replace `docs/assets/ASSET_INDEX.md`; the asset index tracks packages that already exist.

## Asset Concepts Intake Rule

Everything in `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS` is treated as build-bound source material unless Flamestrike explicitly rejects or retires it.

Current scan:

- 289 PNG source concept files.
- The source-file count is not the final asset count.
- Some images are collages, catalogs, contact sheets, or multi-panel boards with many child assets.
- Each source image must be visually inspected and expanded into child assets before it is marked complete.

Collage examples:

- Armory sheets can expand into weapons, armor pieces, shields, tools, grenades, backpacks, power cores, racks, display props, and outfit configurations.
- Portrait sheets can expand into many UI portrait assets.
- Creature sheets can expand into multiple variants or body-part references.
- Building and interior boards can expand into modular walls, doors, roofs, pillars, props, lamps, banners, collision pieces, and material sets.
- Gnome Mek sheets can expand into multiple armor classes, weapons, mechanical limbs, backpacks, sockets, and VFX points.

Tracking source:

- `docs/assets/ASSET_CONCEPTS_MANIFEST.md`

## Current Packaged Assets

These have production package documentation in `docs/assets/`:

| Asset | Current state | Next action |
| --- | --- | --- |
| `SM_AET_TargetDummy_A01` | Concept sheet generated, modeling handoff ready, build/import blocked on approved DCC mesh | Create approved DCC mesh, then build/import and replace startup blockout |
| `SM_AET_PortalArch_A01` | Concept sheet generated, modeling handoff ready, build/import blocked on approved DCC mesh | Create approved DCC mesh, then build/import for portal Blueprint |
| `BP_AET_Portal_A01` | Concept state sheet generated, implementation handoff ready, final Blueprint blocked on portal arch mesh import | Build Blueprint after portal arch mesh exists |
| `SM_MKG_WorkshopPropCrate_A01` | Concept sheet generated, modeling handoff ready | Build/import after DCC mesh is approved |
| `SM_AET_ModularGroundTile_A01` | Concept sheet generated, modeling handoff ready | Build/import after DCC mesh is approved |
| `KIT_MKG_Armory_A01` | Kit package ready, child asset intake complete, child packages needed | Create first child packages from `Gnome Armory.png` |

## Existing Startup Scene Blockouts

These exist in `L_Aerathea_Startup` as validation/blockout content, not final production assets:

| Blockout | Production need |
| --- | --- |
| `AET_BOOT_PlayerScale_180cm` | Keep as scale reference until playable humanoid package exists |
| `AET_BOOT_GnomeScale_110cm` | Replace or supplement after gnome body reference package exists |
| `AET_BOOT_MinotaurScale_270cm` | Replace or supplement after minotaur body reference package exists |
| `AET_BOOT_PortalArch_*` | Replace with `SM_AET_PortalArch_A01` |
| `AET_BOOT_PortalCore_Aetherium_A01` | Replace or wrap with `BP_AET_Portal_A01` |
| `AET_BOOT_TargetDummy_*` | Replace with `SM_AET_TargetDummy_A01` |
| `AET_BOOT_GroundTile_20m_A01` | Replace or supplement with `SM_AET_ModularGroundTile_A01` |

## Race Anchors Needing Production Packages

All approved races below need concept sheets, body proportion sheets, starter outfit packages, material language sheets, Unreal import specs, and eventually skeletal mesh packages.

| Race | Approved anchor | Missing production packages |
| --- | --- | --- |
| Gnomes | Compact 3-4 ft inventors with large heads, expressive ears, sturdy legs, oversized boots, tools, goggles, brass/copper/dark iron/leather/blue Aetherium | Base body sheet, male/female or modular body package, starter outfit, Mekgineer tool kit, goggles/accessory kit |
| Dwarves | Broad dense mountain-forged weaponsmiths/runesmiths/guardians with stone, steel, brass, blue runes, fur, leather | Base body sheet, male/female body package, beard variants for males, starter armor, runesmith/weapon kit |
| Elves | Tall graceful ancient nature/moon/star culture with living wood, silver, moonstone, silverleaf, blue-white Aetherium | Base body sheet, starter outfit, ranger kit, runesinger/moonblade kit, living-architecture material sheet |
| Dark Elves | Elegant shadowed oath-bound culture with dark silver, obsidian, violet glow, crescent motifs | Base body sheet, starter outfit, shadowblade kit, priestess/spellbow kit, dark hall material sheet |
| Orcs | Noble upright powerful clan culture with honor, spirituality, shamanism, disciplined warriors | Base body sheet, starter outfit, clan warrior kit, shaman kit, weapon/material sheet |
| Minotaurs | 8-9 ft plains/lowlands strength culture, simple brutal weapons, magic resistant, hide/bone/raw iron/fur/leather | Base body sheet, starter outfit, barbarian/berserker kit, simple heavy weapon kit, tribal marking sheet |
| Drakhar Lizardfolk | 4-5 ft desert lizardfolk obsessed with magic, Volcreon-linked, scales/bone/leather/sun-baked stone/ember/relics | Base body sheet, scale/material sheet, starter outfit, relic/magic-item kit, rogue/wizard/shaman variants |

Suggested first race package:

- `SK_GNM_Base_A01` or `SK_GNM_Male_A01`, because gnome scale is already represented in the startup map and the Mekgineer crate starts their prop language.

## Armory, Arsenal, And Gear Concepts Needing Production Packages

Armory concepts are not single assets. Treat each armory or gear sheet as a kit source that must be broken into child production packages for weapons, armor pieces, props, materials, sockets, attachment rules, and Unreal import specs.

| Source concept | Faction/theme | Required expansion |
| --- | --- | --- |
| `Gnome Armory.png` | Gnome/Mekgineer | Kit package and child intake complete in `KIT_MKG_Armory_A01`; next create child packages for weapons, Mek-linked gear, pistols, rifles, tools, grenades, armor modules, armor configurations, backpacks, power modules, Aetherium core variants |
| `Dwarven Armory.png` | Dwarven | Weapons, shields, armor pieces, runic details, display props, material set |
| `Dwarven Armory2.png` | Dwarven | Additional armory variants and display-ready weapons/armor |
| `Dwarven Ancestral Armor.png` | Dwarven | Hero armor set, modular armor pieces, rune/metal/fur material set |
| `Elven Armory.png` | Elven | Moonblade/ranger weapons, elegant armor pieces, living-wood/silver/moonstone material set |
| `Dark Elven Armory.png` | Dark Elven | Shadowblade/spellbow gear, crescent motifs, obsidian/dark silver/violet material set |
| `Orc Arsenal.png` | Orc | Clan weapons, shields, shaman/warrior gear, hide/bone/iron material set |
| `Minotaur Arsenal.png` | Minotaur | Simple heavy brutal weapons, hide/bone/raw iron gear, scale rules for 8-9 ft bodies |
| `Drakhar Arms Relics and Field Gear.png` | Drakhar | Relics, arcane charms, field gear, bone/leather/ember/sun-baked material set |
| `Anubisath Armaments.png` | Anubisath/Sutekh | Enemy/faction weapons, armor pieces, seal/necropolis material set |
| `Valararmory.png` | Valar | Valar weapons, armor pieces, oath/warden/ranger variants |
| `Armorer Workshop.png` | Aerathea/Common | Workshop environment kit, racks, benches, tools, display props, forge-adjacent materials |
| `Relic Seekers and Arcane Trails.png` | Aerathea/Common | Relic props, trail markers, arcane field gear, exploration kit |

Suggested first armory package:

- `KIT_MKG_Armory_A01`, because `Gnome Armory.png` is a detailed catalog and connects directly to the existing `SM_MKG_WorkshopPropCrate_A01` and future gnome/Mekgineer production.

## Creature Anchors Needing Production Packages

All approved creatures need concept sheets, scale sheets, skeletal mesh packages, animation lists, collision/physics notes, LOD budgets, and material plans.

| Creature | Approved anchor | Variant backlog |
| --- | --- | --- |
| Gryphon | Eagle front, lion rear, noble mountain/sky guardian with strong feather silhouette, talons, lion tail | Golden, white, storm, forest, desert, royal, moonlit |
| Manticore | Lion body, bat/draconic wings, scorpion tail, dangerous ruin/desert predator | Base manticore first, then biome or threat variants after approval |
| Hippogryph | Eagle front, horse rear, elegant swift mount/creature with horse back legs/tail and eagle head/wings/front talons | Mountain, forest, white, autumn, storm, moonlit |
| Western Dragon | Four legs plus two wings, large reptilian powerful long-tail horned silhouette | Fire, forest, storm, frost, gold, swamp, moonlit, ocean, ruin, desert, raid boss hero |

Suggested first creature package:

- `SK_CRE_Gryphon_A01`, because it gives Aerathea a readable heroic fantasy creature without the high cost of a dragon.

## Building And Settlement Assets Needing Production Packages

The following buildings are approved as established Aerathea settlement assets but do not yet have individual production packages unless noted.

| Building or area | Current state | Missing production work |
| --- | --- | --- |
| House | Approved building anchor only | Production package, concept sheet, modular kit, materials, LOD/collision/import notes |
| Church | Approved building anchor only | Production package, concept sheet, modular kit, interior notes |
| Wizard Tower | Approved building anchor only | Production package, concept sheet, modular kit, Aetherium/rune material notes |
| Town Hall | Approved building anchor only | Production package, concept sheet, modular kit, large-building LOD plan |
| Barracks | Approved building anchor only | Production package, concept sheet, modular kit, training-yard dressing |
| Mine Entrance | Approved building anchor only | Production package, concept sheet, rock/timber modular kit |
| Smithy | Approved building anchor only | Production package, concept sheet, forge/props/VFX notes |
| Target Dummy Area | Partially covered by `SM_AET_TargetDummy_A01` | Area layout package, ground dressing, rack/fence/sign props |
| Portal with Stone Archway | Partially covered by `SM_AET_PortalArch_A01` and `BP_AET_Portal_A01` | Final arch mesh, portal blueprint, VFX/audio/interact notes |
| Mekgineer Workshop | Partially seeded by `SM_MKG_WorkshopPropCrate_A01` | Building package, interior prop set, machines, tool racks, lamps |
| Inn | Approved building anchor only | Production package, concept sheet, modular kit, interior notes |
| Lumber Mill | Approved building anchor only | Production package, concept sheet, modular kit, saw/log props |
| Palisade | Approved building anchor only | Production package, concept sheet, modular wall/gate/corner set |

Suggested first building package:

- `SM_AET_Palisade_A01` or `SM_AET_House_A01`. Palisade is lower risk for modular collision and LOD validation; house is more representative for settlement style.

## Prop And Blueprint Candidates Found During Scan

These are referenced by existing packages or startup docs and should be promoted when needed.

| Candidate | Reason to create |
| --- | --- |
| `BP_AET_TargetDummy_A01` | Hit reaction, damage numbers, training scoring, and audio cues after the static dummy mesh exists |
| `SM_AET_TargetDummyArea_A01` | Converts the target dummy into a dressed training-yard area |
| `SM_MKG_Goggles_A01` | Core gnome/Mekgineer identity prop |
| `SM_MKG_Toolkit_A01` | Supports Mekgineer workshop and gnome character identity |
| `SM_AET_WeaponRack_A01` | Useful for barracks, target dummy area, and early combat testing |
| `SM_AET_Lantern_A01` | Common settlement prop and lighting/material test |
| `SM_AET_Banner_A01` | Common faction/culture readability prop |

## Recommended Next Backlog Actions

1. Finish the first-slice mesh path: build/import `SM_AET_TargetDummy_A01`.
2. Perform a collage-aware intake pass for `ASSET CONCEPTS`, starting with armory sheets and first-slice overlaps.
3. Add modeling handoffs for `SM_AET_PortalArch_A01`, `SM_AET_ModularGroundTile_A01`, and `SM_MKG_WorkshopPropCrate_A01`.
4. Create first child production packages from `KIT_MKG_Armory_A01`, starting with `SM_MKG_AetherKnife_A01`, `SM_MKG_AetherCoreUnit_A01`, `SM_MKG_SparkPistol_A01`, and `SM_MKG_AetheriumGrenade_A01`.
5. Create the first race production package for gnomes, starting with a base body/style sheet.
6. Create the first settlement modular package, either `SM_AET_Palisade_A01` or `SM_AET_House_A01`.
7. Create the first creature package, likely `SK_CRE_Gryphon_A01`.

## Production Rule

Do not turn backlog entries directly into final assets. Each source concept and each child asset from a collage must move through the approved Aerathea pipeline: asset brief, gameplay purpose, silhouette/material direction, concept prompts or reference, production sheet, modeling notes, UV/material plan, LOD/collision plan, Unreal import notes, and quality checklist.
