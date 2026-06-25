# Asset Concepts Manifest

## Source

- Source folder: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`
- PNG concepts scanned: 289 source files
- Intake rule: every image in this folder is treated as a build-bound source concept unless Flamestrike explicitly rejects or retires it.
- Collage rule: one PNG can contain multiple buildable assets. Treat the source-file count as the floor, not the final asset count.
- Build rule: concept images are source references only; each buildable item still needs an Aerathea production package before mesh, Blueprint, UI, material, or environment work.
- Storage rule: source PNGs remain on the desktop concept folder for now; do not copy all 289 files into Git until the project asset-storage policy is approved.

## Collage Expansion Rule

Many `ASSET CONCEPTS` images are catalogs, turnarounds, contact sheets, or multi-panel environment boards. Do not close a source concept as complete just because one package exists for the filename.

For each source concept:

1. Inspect the image visually before production planning.
2. List each distinct buildable child item, panel, variant, module, weapon, armor piece, prop, character, interior zone, UI icon, or environment component.
3. Give each child item a proposed asset name or package name.
4. Mark child items as one of:
   - `Package needed`
   - `Covered by existing package`
   - `Variant of existing package`
   - `Reference only`
   - `Rejected or retired by Flamestrike`
5. Only then create production packages, modeling handoffs, UI sheets, or Unreal implementation tasks.

Use child IDs when a single image expands into many assets:

- `Gnome Armory.png#Weapons_AetherKnife`
- `Gnome Armory.png#Gear_AetherCoreUnit`
- `Gnome Armory.png#Armor_HelmetModule`
- `Portrait Icons for Mobs.png#Icon_01`
- `Dwarven Armory.png#Weapon_01`

Known collage-heavy source types:

- Armory, arsenal, armaments, relic, weapon, armor, and field gear catalogs.
- Portrait icon sheets.
- Creature variant sets such as Dragon, Gryphon, Hippogryph, and Manticore sheets.
- Gnome Mek suit variant sheets.
- Building, interior, settlement, and environment boards that show modular pieces or multiple views.
- Pipeline/reference boards that should become rules, checklists, or production templates rather than meshes.

Example: `Gnome Armory.png` is a catalog with multiple child assets, including weapons, Mek-linked gear, pistols, rifles, engineer tools, grenades, armor modules, armor configurations, backpacks, power modules, and Aetherium core variants. It requires a Gnome armory kit intake pass before individual production packages are created.

## Category Summary

| Category | Concept count |
| --- | ---: |
| Armory/weapons/gear | 13 |
| Building/settlement/environment | 66 |
| Character/NPC/class | 57 |
| Creature/mount | 45 |
| General concept/world reference | 16 |
| Interior/environment set | 36 |
| Mek suit/mechanical companion | 43 |
| Pipeline/reference | 6 |
| UI/portrait icons | 7 |

## Faction Or Theme Summary

| Faction or theme | Concept count |
| --- | ---: |
| Aerathea/Common | 100 |
| Anubisath/Sutekh | 47 |
| Dark Elven | 10 |
| Drakhar | 7 |
| Dwarven | 27 |
| Elven | 10 |
| Gnome/Mekgineer | 54 |
| Minotaur | 9 |
| Orc | 9 |
| Valar | 16 |

## Required Armory And Gear Concepts

| Source concept | Faction/theme | Build interpretation |
| --- | --- | --- |
| `Anubisath Armaments.png` | Anubisath/Sutekh | Create Anubisath/Sutekh armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Armorer Workshop.png` | Aerathea/Common | Create Aerathea/Common armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Dark Elven Armory.png` | Dark Elven | Child intake and kit production package complete in `docs/assets/kits/KIT_DEL_Armory_A01/`; priority child packages needed |
| `Drakhar Arms Relics and Field Gear.png` | Drakhar | Child intake and kit production package complete in `docs/assets/kits/KIT_DKH_FieldGear_A01/`; priority child packages needed; source scale conflicts with approved Drakhar anchor |
| `Dwarven Ancestral Armor.png` | Dwarven | Create Dwarven armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Dwarven Armory.png` | Dwarven | Child intake and kit production package complete in `docs/assets/kits/KIT_DWR_Armory_A01/`; priority child packages needed |
| `Dwarven Armory2.png` | Dwarven | Create Dwarven armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Elven Armory.png` | Elven | Child intake and kit production package complete in `docs/assets/kits/KIT_ELV_Armory_A01/`; priority child packages needed |
| `Gnome Armory.png` | Gnome/Mekgineer | Kit package and child asset intake complete in `docs/assets/kits/KIT_MKG_Armory_A01/`; first four child packages, handoffs, DCC meshes, Unreal imports, and startup placements complete |
| `Minotaur Arsenal.png` | Minotaur | Child intake and kit production package complete in `docs/assets/kits/KIT_MIN_Arsenal_A01/`; priority child packages needed |
| `Orc Arsenal.png` | Orc | Child intake and kit production package complete in `docs/assets/kits/KIT_ORC_Arsenal_A01/`; priority child packages needed |
| `Relic Seekers and Arcane Trails.png` | Aerathea/Common | Create Aerathea/Common armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Valararmory.png` | Valar | Create Valar armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |

## Full Intake List

| Source concept | Category | Faction/theme | Build interpretation |
| --- | --- | --- | --- |
| `Armorer Workshop.png` | Armory/weapons/gear | Aerathea/Common | Create Aerathea/Common armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Relic Seekers and Arcane Trails.png` | Armory/weapons/gear | Aerathea/Common | Create Aerathea/Common armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Anubisath Armaments.png` | Armory/weapons/gear | Anubisath/Sutekh | Create Anubisath/Sutekh armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Dark Elven Armory.png` | Armory/weapons/gear | Dark Elven | Child intake and kit production package complete in `docs/assets/kits/KIT_DEL_Armory_A01/`; priority child packages needed |
| `Drakhar Arms Relics and Field Gear.png` | Armory/weapons/gear | Drakhar | Child intake and kit production package complete in `docs/assets/kits/KIT_DKH_FieldGear_A01/`; priority child packages needed; source scale conflicts with approved Drakhar anchor |
| `Dwarven Ancestral Armor.png` | Armory/weapons/gear | Dwarven | Create Dwarven armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Dwarven Armory.png` | Armory/weapons/gear | Dwarven | Child intake and kit production package complete in `docs/assets/kits/KIT_DWR_Armory_A01/`; priority child packages needed |
| `Dwarven Armory2.png` | Armory/weapons/gear | Dwarven | Create Dwarven armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Elven Armory.png` | Armory/weapons/gear | Elven | Child intake and kit production package complete in `docs/assets/kits/KIT_ELV_Armory_A01/`; priority child packages needed |
| `Gnome Armory.png` | Armory/weapons/gear | Gnome/Mekgineer | Kit package and child asset intake complete in `docs/assets/kits/KIT_MKG_Armory_A01/`; first four child packages, handoffs, DCC meshes, Unreal imports, and startup placements complete |
| `Minotaur Arsenal.png` | Armory/weapons/gear | Minotaur | Child intake and kit production package complete in `docs/assets/kits/KIT_MIN_Arsenal_A01/`; priority child packages needed |
| `Orc Arsenal.png` | Armory/weapons/gear | Orc | Child intake and kit production package complete in `docs/assets/kits/KIT_ORC_Arsenal_A01/`; priority child packages needed |
| `Valararmory.png` | Armory/weapons/gear | Valar | Create Valar armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Ancestral Shrine.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Barracks.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Barracks1png.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Church 3.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Church reference.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Church Reference.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Church.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Citadel of the Shattered Seal.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Gatehouse Approved.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Great Forge.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Great Workshop Gno9me.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Great Workshop.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Mine 2.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Mine Entrance.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `MountainGate Fortress.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Seagate Bastion.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Smithy 2.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Target Dummy Area.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Temple of Radiant Oath.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `The Spark and Screw Inn.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Warpaths.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Wizard's Tower.png` | Building/settlement/environment | Aerathea/Common | Create Aerathea/Common environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath AirBarge.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath Barge Full Power.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath Barracks.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath Great Pyramid Fortress.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath Housing District.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath INN.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath Necropolis.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath Portal Pyramid 2.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath Portal Pyramid.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath Quarry.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Anubisath Soulforge.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Sutekh's Temple Pyramid.png` | Building/settlement/environment | Anubisath/Sutekh | Create Anubisath/Sutekh environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dark Elven Citadel.png` | Building/settlement/environment | Dark Elven | Create Dark Elven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Night Grove.png` | Building/settlement/environment | Dark Elven | Create Dark Elven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Shadow Gatehouse.png` | Building/settlement/environment | Dark Elven | Create Dark Elven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Drakhar Homeland.png` | Building/settlement/environment | Drakhar | Create Drakhar environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Barracks.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Buildings.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Buildings2.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Clan Hall 2.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Forge.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Forge2.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Fortress.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven House.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Houses2.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Housing.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven INN.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Dwarven Stronghold.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `The Great Forge Karvagg.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `The Walls of Korval.png` | Building/settlement/environment | Dwarven | Create Dwarven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Aerathean Elven Citadel.png` | Building/settlement/environment | Elven | Create Elven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Elven Gatehouse.png` | Building/settlement/environment | Elven | Create Elven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Elven Grove.png` | Building/settlement/environment | Elven | Create Elven environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Cogspire Enclave.png` | Building/settlement/environment | Gnome/Mekgineer | Create Gnome/Mekgineer environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Gnomish Cogspire Enclave.png` | Building/settlement/environment | Gnome/Mekgineer | Create Gnome/Mekgineer environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Gnomish Inn.png` | Building/settlement/environment | Gnome/Mekgineer | Create Gnome/Mekgineer environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Sentinels of Cogspire.png` | Building/settlement/environment | Gnome/Mekgineer | Create Gnome/Mekgineer environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Minotaur Great Herd Camp.png` | Building/settlement/environment | Minotaur | Create Minotaur environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Minotaur Lowlands.png` | Building/settlement/environment | Minotaur | Create Minotaur environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Orc Fortress.png` | Building/settlement/environment | Orc | Create Orc environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Orc Homeland.png` | Building/settlement/environment | Orc | Create Orc environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Valar Arcane Spire.png` | Building/settlement/environment | Valar | Create Valar environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Valar Watchtower Spire.png` | Building/settlement/environment | Valar | Create Valar environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Valarbarracksandtrainingyard.png` | Building/settlement/environment | Valar | Create Valar environment kit or building package with modular parts, materials, LOD/collision/import notes |
| `Volcreon Ancient God.png` | Character/NPC/class | Aerathea/Common | Create Aerathea/Common character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `VyraelithWardenofSerapentil.png` | Character/NPC/class | Aerathea/Common | Create Aerathea/Common character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Anubaroth.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Anubisath Necromancer.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Anubisath Ranger.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Anubisath SandShaper.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Anubisath Sekhmetra.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Anubisath Senathet.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Anubisath Sentinel Female.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Anubisath Warrior.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekh Minion1.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekhminion10.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekhminion11.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekhminion2.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekhminion3.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekhminion4.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekhminion5.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekhminion6.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekhminion7.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Sutekhminion9.png` | Character/NPC/class | Anubisath/Sutekh | Create Anubisath/Sutekh character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Dark Elf Female Approved.png` | Character/NPC/class | Dark Elven | Create Dark Elven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Dark Elf Male Approved.png` | Character/NPC/class | Dark Elven | Create Dark Elven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Dark Elven Sentinels.png` | Character/NPC/class | Dark Elven | Create Dark Elven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Drakhar Approved.png` | Character/NPC/class | Drakhar | Create Drakhar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Drakhar Female.png` | Character/NPC/class | Drakhar | Create Drakhar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Drakhar Male.png` | Character/NPC/class | Drakhar | Create Drakhar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Dwarf Female1.png` | Character/NPC/class | Dwarven | Create Dwarven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `DwarfMale1.png` | Character/NPC/class | Dwarven | Create Dwarven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Dwarven Female Paladin.png` | Character/NPC/class | Dwarven | Create Dwarven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Dwarven Runesmith.png` | Character/NPC/class | Dwarven | Create Dwarven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Dwarven Warrior.png` | Character/NPC/class | Dwarven | Create Dwarven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Runesmith Approved.png` | Character/NPC/class | Dwarven | Create Dwarven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Elven Female Approved.png` | Character/NPC/class | Elven | Create Elven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Elven Male Approved.png` | Character/NPC/class | Elven | Create Elven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Elven Sentinels.png` | Character/NPC/class | Elven | Create Elven character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Gnome Female.png` | Character/NPC/class | Gnome/Mekgineer | Create Gnome/Mekgineer character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Gnome Male.png` | Character/NPC/class | Gnome/Mekgineer | Create Gnome/Mekgineer character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `GnomeMale1.png` | Character/NPC/class | Gnome/Mekgineer | Create Gnome/Mekgineer character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Gnomish Sentinels.png` | Character/NPC/class | Gnome/Mekgineer | Create Gnome/Mekgineer character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Female Minotaur.png` | Character/NPC/class | Minotaur | Create Minotaur character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Minotaur Approved.png` | Character/NPC/class | Minotaur | Create Minotaur character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Minotaur Sentinels.png` | Character/NPC/class | Minotaur | Create Minotaur character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Minotaur Shaman.png` | Character/NPC/class | Minotaur | Create Minotaur character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Minotaur Shaman1.png` | Character/NPC/class | Minotaur | Create Minotaur character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Orc Approved.png` | Character/NPC/class | Orc | Create Orc character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Orc Female Approved.png` | Character/NPC/class | Orc | Create Orc character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Orc Sentinels.png` | Character/NPC/class | Orc | Create Orc character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Orc Shaman.png` | Character/NPC/class | Orc | Create Orc character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Orc War Leaders.png` | Character/NPC/class | Orc | Create Orc character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Valar Female Approved.png` | Character/NPC/class | Valar | Create Valar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Valar Male Approved.png` | Character/NPC/class | Valar | Create Valar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Valarmale1.png` | Character/NPC/class | Valar | Create Valar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Valarmalemage1.png` | Character/NPC/class | Valar | Create Valar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `ValarNobility.png` | Character/NPC/class | Valar | Create Valar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Valarpaladinandpriest.png` | Character/NPC/class | Valar | Create Valar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Valarranger1.png` | Character/NPC/class | Valar | Create Valar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Valarwardensofthenorth.png` | Character/NPC/class | Valar | Create Valar character/NPC/class package: body or outfit sheet, skeletal mesh plan, materials, animation list |
| `Dragon.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon1.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon10.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon2.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon3.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon4.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon5.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon6.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon7.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon8.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dragon9.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Gryphon.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Gryphon1.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Gryphon10.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Gryphon2.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Gryphon5.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Gryphon6.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Gryphon7.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Gryphon8.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Gryphon9.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Grypon3.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Grypon4.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph1.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph10.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph2.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph3.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph4.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph5.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph6.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph7.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph8.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Hipogryph9.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore1.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore10.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore2.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore3.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore4.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore5.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore6.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore7.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore8.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Manticore9.png` | Creature/mount | Aerathea/Common | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Dwarf Riding a Yak.png` | Creature/mount | Dwarven | Create creature package: concept sheet, skeletal mesh, materials, animations, collision, LODs |
| `Aerathean Dwarves.png` | General concept/world reference | Aerathea/Common | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Target Dummy.png` | General concept/world reference | Aerathea/Common | Classify with Flamestrike if unclear, then create a production package before asset work |
| `The Great Sealing.png` | General concept/world reference | Aerathea/Common | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Anubisath.png` | General concept/world reference | Anubisath/Sutekh | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Anubisath1.png` | General concept/world reference | Anubisath/Sutekh | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Sutekh Breaker of Seals.png` | General concept/world reference | Anubisath/Sutekh | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Dark Elven Magecraft.png` | General concept/world reference | Dark Elven | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Arathean Drakhar.png` | General concept/world reference | Drakhar | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Drakhar Obsession.png` | General concept/world reference | Drakhar | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Dwarf1.png` | General concept/world reference | Dwarven | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Hold of Korvad.png` | General concept/world reference | Dwarven | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Elven Magecraft.png` | General concept/world reference | Elven | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Elven MoonRunes.png` | General concept/world reference | Elven | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Gnome.png` | General concept/world reference | Gnome/Mekgineer | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Minotaur Tribal Markings.png` | General concept/world reference | Minotaur | Classify with Flamestrike if unclear, then create a production package before asset work |
| `Valar.png` | General concept/world reference | Valar | Classify with Flamestrike if unclear, then create a production package before asset work |
| `house interior 1.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `house interior 2.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `house interior 3.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `house interior 4.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `house interior 5.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `house interior 6.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `house interior 7.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `House Interior7.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `House interior8.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `House Interior9.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Meeting Hall.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Ranger Lodge and Hunt Hall.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Throne Room Approved.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Town Hall.png` | Interior/environment set | Aerathea/Common | Create Aerathea/Common interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Anubisath Barracks Interior.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Anubisath Hall of Seals.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Anubisath INN Interior.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekh Temple Interior1.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekhtempleinterior10.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekhtempleinterior2.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekhtempleinterior3.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekhtempleinterior4.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekhtempleinterior5.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekhtempleinterior6.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekhtempleinterior7.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekhtempleinterior8.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Sutekhtempleinterior9.png` | Interior/environment set | Anubisath/Sutekh | Create Anubisath/Sutekh interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Great veiled Hall.png` | Interior/environment set | Dark Elven | Create Dark Elven interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Shadow Atelier.png` | Interior/environment set | Dark Elven | Create Dark Elven interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Dwarven Clan Hall.png` | Interior/environment set | Dwarven | Create Dwarven interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Great Moon Hall.png` | Interior/environment set | Elven | Create Elven interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Gnome Atelier.png` | Interior/environment set | Gnome/Mekgineer | Create Gnome/Mekgineer interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Orc Great Hall.png` | Interior/environment set | Orc | Create Orc interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Valar Hall of Oaths.png` | Interior/environment set | Valar | Create Valar interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `ValarHall.png` | Interior/environment set | Valar | Create Valar interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `ValarMeadhall.png` | Interior/environment set | Valar | Create Valar interior kit: modular room pieces, props, lighting notes, materials, LOD/collision specs |
| `Gnome Heavy Mek Suit.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `Gnome Pet Scrapper.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleHeavyMek1.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleHeavyMek2.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleHeavyMek3.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleHeavyMek4.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleHeavyMek5.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleHeavyMek6.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleHeavyMekAxe.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleLightMek.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleLightMek2.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleLightMek3.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleLightMek4.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleLightMek5.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleMediumMek1.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleMediumMek3.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleMediumMek4.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleMediumMek5.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleMediumMek6.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeFemaleMediumMekSword.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleHaeavyMek6.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleHeavyMek1.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleHeavyMek2.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleHeavyMek4.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleHeavyMek5.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleHeavyMekSword.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleLightMek.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleLightMek2.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleLightMek3.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleLightMek4.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleLightMek5.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleMediumMek2.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleMediumMek3.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleMediumMek4.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleMediumMek5.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleMediumMek6.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMaleMediumMekSword.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `GnomeMediumMek1.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `Gnomish Teknomancy.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `Rift Touched Mek.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `Scrapper Gyro's Pet.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `Scrapper2.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `Teknomancy.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Create gnome Mek suit or mechanical companion package with skeletal/static mesh split, sockets, materials, LODs |
| `Asset Pipeline1.png` | Pipeline/reference | Aerathea/Common | Use as pipeline/style reference; convert into project rules or checklists, not a mesh by itself |
| `Asset Pipeline2.png` | Pipeline/reference | Aerathea/Common | Use as pipeline/style reference; convert into project rules or checklists, not a mesh by itself |
| `Asset1.png` | Pipeline/reference | Aerathea/Common | Use as pipeline/style reference; convert into project rules or checklists, not a mesh by itself |
| `Asset2.png` | Pipeline/reference | Aerathea/Common | Use as pipeline/style reference; convert into project rules or checklists, not a mesh by itself |
| `Asset3.png` | Pipeline/reference | Aerathea/Common | Use as pipeline/style reference; convert into project rules or checklists, not a mesh by itself |
| `Concept Art Approved.png` | Pipeline/reference | Aerathea/Common | Use as pipeline/style reference; convert into project rules or checklists, not a mesh by itself |
| `Portrait Icons for Mobs 6.png` | UI/portrait icons | Aerathea/Common | Create UI portrait icon sheet/package and individual mob portrait assets |
| `Portrait Icons for Mobs.png` | UI/portrait icons | Aerathea/Common | Create UI portrait icon sheet/package and individual mob portrait assets |
| `Portrait Icons for Mobs1.png` | UI/portrait icons | Aerathea/Common | Create UI portrait icon sheet/package and individual mob portrait assets |
| `Portrait Icons for Mobs2.png` | UI/portrait icons | Aerathea/Common | Create UI portrait icon sheet/package and individual mob portrait assets |
| `Portrait Icons for Mobs3.png` | UI/portrait icons | Aerathea/Common | Create UI portrait icon sheet/package and individual mob portrait assets |
| `Portrait Icons for Mobs4.png` | UI/portrait icons | Aerathea/Common | Create UI portrait icon sheet/package and individual mob portrait assets |
| `Portrait Icons for Mobs5.png` | UI/portrait icons | Aerathea/Common | Create UI portrait icon sheet/package and individual mob portrait assets |
