# Asset Concepts Manifest

## Source

- Source folder: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`
- Source concepts scanned: 547 source files, including 546 PNG files and 1 JPG file
- Intake rule: every image in this folder is treated as a build-bound source concept unless Flamestrike explicitly rejects or retires it.
- Collage rule: one PNG can contain multiple buildable assets. Treat the source-file count as the floor, not the final asset count.
- Build rule: concept images are source references only; each buildable item still needs an Aerathea production package before mesh, Blueprint, UI, material, or environment work.
- Storage rule: source images remain in the desktop concept folder for now; do not copy all 547 files into Git until the project asset-storage policy is approved.

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
| Abyss/enemy creature concepts | 45 |
| Armory/weapons/gear | 14 |
| Building/settlement/environment | 100 |
| Character/NPC/class | 184 |
| Creature/mount | 46 |
| Cross-faction encounter reference | 23 |
| General concept/world reference | 16 |
| Interior/environment set | 41 |
| Mek suit/mechanical companion | 65 |
| Pipeline/reference | 6 |
| UI/portrait icons | 7 |

## Faction Or Theme Summary

| Faction or theme | Concept count |
| --- | ---: |
| Abyss/Anathema | 45 |
| Aerathea/Common | 102 |
| Anubisath/Sutekh | 47 |
| Basari | 24 |
| Blood Axe Tribe | 22 |
| Dark Elven | 10 |
| Drakhar | 7 |
| Dwarven | 27 |
| Elven | 10 |
| Giant | 26 |
| Gnome/Mekgineer | 77 |
| Gnome/Mekgineer + Abyss encounter | 1 |
| Gnome/Mekgineer + Ogre encounter | 21 |
| Infernal/Balgoroth cult | 63 |
| Minotaur | 9 |
| Ogre | 31 |
| Orc | 9 |
| Valar | 16 |

## Ogre Intake Delta 2026-06-26

The Ogre addendum contains 31 source concepts added after the previous manifest scan. These files establish Ogres as a large war-created race with female scale 10'0"-10'6" and male scale 10'4"-11'0". They support `SK_OGR_Base_A01` plus class, Teknomancy, fortification, and settlement follow-up packages.

| Source concept | Category | Faction/theme | Build interpretation |
| --- | --- | --- | --- |
| `Ogre Female.png` | Character/NPC/class | Ogre | Female Ogre body reference for `SK_OGR_Base_A01`; package ready |
| `OgreFemale2.png` | Character/NPC/class | Ogre | Female Ogre body and class silhouette reference for `SK_OGR_Base_A01` |
| `OgreMale1.png` | Character/NPC/class | Ogre | Male body and Teknomancy hardware reference for `SK_OGR_Base_A01` and future `SK_OGR_Teknomancer_A01` |
| `OgreMale2.png` | Character/NPC/class | Ogre | Male necromantic body/outfit reference for future `SK_OGR_Necromancer_A01` |
| `Ogremale4.png` | Character/NPC/class | Ogre | Male warrior/body reference for future `SK_OGR_Warrior_A01` |
| `OgreMaleTek.png` | Character/NPC/class | Ogre | Teknomancer class source; create `SK_OGR_Teknomancer_A01` and `KIT_OGR_Teknomancy_A01` |
| `OgreWarrior.png` | Character/NPC/class | Ogre | Warrior class source; create `SK_OGR_Warrior_A01` |
| `OgreShaman.png` | Character/NPC/class | Ogre | Shaman class source; package ready in `docs/assets/characters/SK_OGR_Shaman_A01/` |
| `OgreNecromancer.png` | Character/NPC/class | Ogre | Necromancer class source; package ready in `docs/assets/characters/SK_OGR_Necromancer_A01/` |
| `OgreSentinel.png` | Character/NPC/class | Ogre | Sentinel/formation source; create `SK_OGR_Sentinel_A01` or `KIT_OGR_Warband_A01` |
| `OgreSentinels.png` | Character/NPC/class | Ogre | Sentinel group source; create `KIT_OGR_Warband_A01` |
| `OgreSmiths.png` | Character/NPC/class | Ogre | Smith/forge NPC source; route to `KIT_OGR_Teknomancy_A01` and forge props |
| `OgreTekvsGnomeMek.png` | Cross-faction encounter reference | Ogre + Gnome/Mekgineer | Ogre Teknomancer versus Gnome Mek rivalry reference; use for encounter scale and class rivalry |
| `OgreBarracks.png` | Building/settlement/environment | Ogre | Ogre barracks/defense interior or compound source; route to `KIT_OGR_CairnFortifications_A01` |
| `OgreForge.png` | Building/settlement/environment | Ogre | Forge source; create `SM_OGR_Forge_A01` and forge prop kit |
| `OgreFortress.png` | Building/settlement/environment | Ogre | Fortress exterior source; create `KIT_OGR_CairnFortifications_A01` |
| `OgreGate.png` | Building/settlement/environment | Ogre | Heavy gate source; create `SM_OGR_Gate_A01` |
| `OgreInn.png` | Building/settlement/environment | Ogre | Settlement inn source; create `SM_OGR_Inn_A01` |
| `OgreNecropolis.png` | Building/settlement/environment | Ogre | Necropolis/cairn grave source; create `KIT_OGR_Necropolis_A01` |
| `OgreShamanHut.png` | Building/settlement/environment | Ogre | Shaman hut source; create `SM_OGR_ShamanHut_A01` |
| `Ogres2.png` | Building/settlement/environment | Ogre | Ogre settlement exterior source; route to settlement kit |
| `Ogres3.png` | Building/settlement/environment | Ogre | Cairn field/settlement source; route to `KIT_OGR_CairnFortifications_A01` |
| `Ogres6.png` | Building/settlement/environment | Ogre | Settlement building source; route to `KIT_OGR_Settlement_A01` |
| `Ogres7.png` | Building/settlement/environment | Ogre | Fortress/cairn exterior source; route to `KIT_OGR_CairnFortifications_A01` |
| `Ogres8 .png` | Building/settlement/environment | Ogre | Gate/stronghold exterior source; filename normalization needed |
| `Ogres11.png` | Building/settlement/environment | Ogre | Siege yard or fortified courtyard source; route to `SM_OGR_SiegeCannon_A01` and fortification kit |
| `Ogres1.png` | Interior/environment set | Ogre | Settlement interior source; route to `KIT_OGR_SettlementInteriors_A01` |
| `Ogres5.png` | Interior/environment set | Ogre | Forge/interior source; route to `SM_OGR_Forge_A01` and forge props |
| `Ogres9.png` | Interior/environment set | Ogre | Interior hall source; route to `KIT_OGR_SettlementInteriors_A01` |
| `Ogres10.png` | Interior/environment set | Ogre | Tek/forge workshop source; route to `KIT_OGR_Teknomancy_A01` and siege weapon props |
| `OgreTekShop.png` | Interior/environment set | Ogre | Tek shop/interior source; create `SM_OGR_TekShop_A01` and `KIT_OGR_Teknomancy_A01` |

## Infernal And Gnome/Ogre Intake Delta 2026-06-27

The current source folder adds 88 files after the 2026-06-26 Ogre pass: 63 Infernal/Balgoroth references, 21 Gnome-vs-Ogre encounter references, and 4 Gnome heavy Mek references. The Infernal set confirms adult body, Lesser lifecycle, sorcerer, lit-brand, gate-guard, clutch, and cult-space routing. The Gnome/Ogre set establishes a dedicated rivalry encounter package instead of treating these images as standalone Gnome or Ogre body references.

All Infernal/Balgoroth references in this section route through `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md` before becoming modeling, prompt, VFX, or texture requirements.

| Source concept | Category | Faction/theme | Build interpretation |
| --- | --- | --- | --- |
| `INfernalBoy2.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal boy stage reference; route to `SK_INF_Lesser_A01` Spawn or 1st Kill variants |
| `INfernalBoy5.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal boy stage reference; route to `SK_INF_Lesser_A01` Blooded variant matrix |
| `Infernal Children.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal group reference; route to lifecycle staging and cult den child scale |
| `InfernalBoy1.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal boy stage reference; route to `SK_INF_Lesser_A01` Spawn or 1st Kill variants |
| `InfernalBoy3.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal boy stage reference; route to `SK_INF_Lesser_A01` Blooded posture language |
| `InfernalBoy4.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal boy stage reference; route to `SK_INF_Lesser_A01` Blooded or Elder bridge |
| `InfernalClutch.png` | Character/NPC/class | Infernal/Balgoroth cult | Clutch and early lifecycle group source; route to `SK_INF_Lesser_A01` and `KIT_INF_BalgorothCult_A01` trial spaces |
| `InfernalFemale.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult female body reference; route to `SK_INF_Base_A01` sex-variant and class sheet |
| `InfernalFemale1.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult female body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalFemale2.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult female body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalFemale4.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult female body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalFemale5.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult female body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalFemale6.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult female body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalFemale7.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult female body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalFemale8.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult female body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalFemaleLit.png` | Character/NPC/class | Infernal/Balgoroth cult | Female lit-brand material and emissive reference; route to `SK_INF_Base_A01` and `MI_INF_BrandGlowStates_A01` |
| `InfernalFemaleLit1.png` | Character/NPC/class | Infernal/Balgoroth cult | Female lit-brand material and emissive reference; route to adult brand states |
| `InfernalFemaleLit2.png` | Character/NPC/class | Infernal/Balgoroth cult | Female lit-brand material and emissive reference; route to adult brand states |
| `InfernalFemaleLit3.png` | Character/NPC/class | Infernal/Balgoroth cult | Female lit-brand material and emissive reference; route to adult brand states |
| `InfernalGirl1.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal girl stage reference; route to `SK_INF_Lesser_A01` Spawn or 1st Kill variants |
| `InfernalGirl2.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal girl stage reference; route to `SK_INF_Lesser_A01` Blooded variants |
| `InfernalGirl3.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal girl stage reference; route to `SK_INF_Lesser_A01` Blooded variants |
| `InfernalGirl5.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal girl stage reference; route to `SK_INF_Lesser_A01` Elder bridge |
| `InfernalGirls5.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal group reference; route to lifecycle sex-variant staging |
| `InfernalMale.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult male body reference; route to `SK_INF_Base_A01` sex-variant and class sheet |
| `InfernalMale0.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult male body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalMale1.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult male body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalMale2.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult male body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalMale3.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult male body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalMale4.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult male body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalMale5.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult male body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalMale6.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult male body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalMale7.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult male body/reference outfit source; route to `SK_INF_Base_A01` |
| `InfernalMaleLit.png` | Character/NPC/class | Infernal/Balgoroth cult | Male lit-brand material and emissive reference; route to adult brand states |
| `InfernalMaleSorcerer2.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult sorcerer class source; route to future `SK_INF_Mage_A01` and cult VFX |
| `InfernalMaleSorcerer3.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult sorcerer class source; route to future `SK_INF_Mage_A01` |
| `InfernalMaleSorcererLit.png` | Character/NPC/class | Infernal/Balgoroth cult | Lit sorcerer material and VFX source; route to future `SK_INF_Mage_A01` and brand states |
| `Infernalfemale3.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult female body/reference outfit source; naming normalization needed |
| `Infernals Guarding a Gate.png` | Building/settlement/environment | Infernal/Balgoroth cult | Gate guard scene and arch source; route to `SM_INF_HornWingArch_A01` and cult encounter dressing |
| `Infernals Guarding a Gate2.png` | Building/settlement/environment | Infernal/Balgoroth cult | Gate guard scene and arch variant source; route to future cult gate package |
| `Infernals.png` | Character/NPC/class | Infernal/Balgoroth cult | Adult group hierarchy source; route to `SK_INF_Base_A01` body/class matrix |
| `Lesser Infernal15.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; filename normalization needed |
| `LesserInfernal10.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal11.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal13.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal14.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal15.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; compare with spaced duplicate name |
| `LesserInfernal17.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal18.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal19.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal20.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal21.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal22.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal23.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal24.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal3.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal5.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal6.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal7.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal8.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernal9.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal stage variant; route to `SK_INF_Lesser_A01` |
| `LesserInfernalFemale.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal female body reference; route to lifecycle sex-variant matrix |
| `LesserInfernalMale.png` | Character/NPC/class | Infernal/Balgoroth cult | Lesser Infernal male body reference; route to lifecycle sex-variant matrix |
| `Gnome Vs Ogre.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome heavy Mek versus Ogre rivalry source; route to `KIT_GNM_OGR_RivalryEncounter_A01` |
| `GnomeFemaleHeavyMek.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Additional female heavy Mek variant; route to `KIT_GNM_IonaSiegebreaker_A01` and rivalry kit |
| `GnomeFemaleHeavyMek0.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Additional female heavy Mek variant; route to heavy Mek variant matrix |
| `GnomeFemaleHeavyMek10.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Additional female heavy Mek variant; route to heavy Mek variant matrix |
| `GnomeFemaleHeavyMek8.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Additional female heavy Mek variant; route to heavy Mek variant matrix |
| `GnomeFemalevsOgre11.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Female gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomeFemalevsOgre14.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Female gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomeFemalevsOgre15.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Female gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre1.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre10.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre11.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre12.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre13.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre14.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre15.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre16.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre2.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre3.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre4.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre5.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre6.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre7.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgre9.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome Mek versus Ogre encounter source; route to rivalry kit |
| `GnomevsOgreandManticore8.png` | Cross-faction encounter reference | Gnome/Mekgineer + Ogre encounter | Gnome/Ogre/Manticore battlefield interrupt source; route to rivalry kit as future creature encounter variant |

## Required Armory And Gear Concepts

| Source concept | Faction/theme | Build interpretation |
| --- | --- | --- |
| `Anubisath Armaments.png` | Anubisath/Sutekh | Create Anubisath/Sutekh armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Armorer Workshop.png` | Aerathea/Common | Create Aerathea/Common armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `BloodAxeArmory.png` | Blood Axe Tribe | Create Blood Axe armory kit: giant weapons, trophy armor, bows, quivers, bowyer tools, reforged-metal process reference, and MMO-safe material set |
| `Dark Elven Armory.png` | Dark Elven | Child intake and kit production package complete in `docs/assets/kits/KIT_DEL_Armory_A01/`; priority child package docs ready; DCC builds pending |
| `Drakhar Arms Relics and Field Gear.png` | Drakhar | Child intake and kit production package complete in `docs/assets/kits/KIT_DKH_FieldGear_A01/`; priority child package docs ready; DCC builds pending; source scale conflicts with approved Drakhar anchor |
| `Dwarven Ancestral Armor.png` | Dwarven | Create Dwarven armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Dwarven Armory.png` | Dwarven | Child intake and kit production package complete in `docs/assets/kits/KIT_DWR_Armory_A01/`; priority child package docs ready; DCC builds pending |
| `Dwarven Armory2.png` | Dwarven | Create Dwarven armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Elven Armory.png` | Elven | Child intake and kit production package complete in `docs/assets/kits/KIT_ELV_Armory_A01/`; priority child package docs ready; DCC builds pending |
| `Gnome Armory.png` | Gnome/Mekgineer | Kit package and child asset intake complete in `docs/assets/kits/KIT_MKG_Armory_A01/`; all catalog child production packages and handoffs documented; first ten child DCC meshes, Unreal imports, and startup placements or socket-fit previews complete |
| `Minotaur Arsenal.png` | Minotaur | Child intake and kit production package complete in `docs/assets/kits/KIT_MIN_Arsenal_A01/`; priority child package docs ready; DCC builds pending |
| `Orc Arsenal.png` | Orc | Child intake and kit production package complete in `docs/assets/kits/KIT_ORC_Arsenal_A01/`; priority child package docs ready; DCC builds pending |
| `Relic Seekers and Arcane Trails.png` | Aerathea/Common | Create Aerathea/Common armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Valararmory.png` | Valar | Create Valar armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |

## Live Refresh Delta 2026-06-25

The initial live refresh recorded 91 source files not yet represented in the full intake table below. The Abyss/Anathema set, `Gnome Mek fighting Demon.png`, and `Iona.png` have now received visual intake and package routing; the remaining delta files still need visual inspection and child-asset expansion before any production package is created.

| Source concept | Category | Faction/theme | Build interpretation |
| --- | --- | --- | --- |
| `AbysalDemon4.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as distinct polearm elite source in `KIT_ABY_ShadowFlame_A01` |
| `Abyssal Demon6.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as horned caster/brute source with spacing drift in filename |
| `Abyssal1.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as spear lordling or elite demon source |
| `Abyssal2.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as firewheel brute source |
| `Abyssal3.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as rift/tendril entity source |
| `Abyssal4.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as green-flame glaive reaver source |
| `AbyssalDemon1.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as formation/spawn reference |
| `AbyssalDemon2.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_BlackPikeTrooper_A01` variant source |
| `AbyssalDemon3.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_WardbreakerMage_A01` variant source |
| `AbyssalDemon4.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_BulwarkDemon_A01` variant source |
| `AbyssalDemon5.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_WingedRavager_A01` variant source |
| `AbyssalDemon7.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as torn-standard/banner caster source |
| `AbyssalDemon8.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_RiftHound_A01` priority source |
| `AbyssalDemon9.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as shadowstorm caster source |
| `AbyssalDemon10.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_VoidbowStalker_A01` priority source |
| `AbyssalDemon11.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_WardbreakerMage_A01` priority source |
| `AbyssalDemon12.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_CrescentReaver_A01` priority source |
| `AbyssalDemon13.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_BulwarkDemon_A01` priority source |
| `AbyssalDemon14.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_WingedRavager_A01` priority source |
| `AbyssalDemon15.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_SiegeBrute_A01` variant source |
| `AbyssalDemon16.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as carapace crawler package source |
| `AbyssalDemon17.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as warbanner wraith package source |
| `AbyssalDemon18.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_CrescentReaver_A01` variant source |
| `AbyssalDemon20.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_VoidbowStalker_A01` variant source; expected sequence number 19 was not present |
| `AbyssalLord.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_CinderLord_A01` priority source |
| `AbyssalLord1.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_CinderLord_A01` winged-lord variant |
| `AbyssalLord2.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as future `SK_ABY_VoidTyrant_A01` source |
| `AbyssalLord3.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_CinderLord_A01` strongest war-host commander source |
| `AbyssalLord4.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as lord/beast variant for `SK_ABY_RiftHound_A01` |
| `AbyssalLordHound.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_RiftHound_A01` priority source |
| `AbyssalSieger.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_SiegeBrute_A01` priority source |
| `AbyssalTroops1.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_WardbreakerMage_A01` formation/caster reference |
| `AbyssalTroops2.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_BlackPikeTrooper_A01` banner-line variant |
| `AbyssalTroops3.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_BlackPikeTrooper_A01` priority source |
| `AbyssalTroops4.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_WardbreakerMage_A01` ranged/caster reference |
| `AbyssalTroops5.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_WingedRavager_A01` variant source |
| `AbyssalTroops6.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_BlackPikeTrooper_A01` warband reference |
| `AbyssalTroops7.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as ashglaive/banner officer source |
| `AbyssalTroops8.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_BlackPikeTrooper_A01` shield-line source |
| `AbyssalTroops9.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; classified as lesser spawn/riftborn variant |
| `AbyssalTroops10.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ABY_BlackPikeTrooper_A01` axe troop variant |
| `Anathema1.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ANA_SiegeDrake_A01` variant source |
| `Anathema2.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ANA_SiegeDrake_A01` twin-cannon variant; near-duplicate of `Anathema3.png` |
| `Anathema3.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ANA_SiegeDrake_A01` twin-cannon near-duplicate |
| `Anathema4.png` | Abyss/enemy creature concepts | Abyss/Anathema | Visual intake complete; routed as `SK_ANA_SiegeDrake_A01` cleanest priority source |
| `Gnome Mek fighting Demon.png` | Cross-faction encounter reference | Gnome/Mekgineer + Abyss encounter | Visual intake complete; routed as encounter reference in `KIT_GNM_IonaSiegebreaker_A01` and winged-demon reference for `KIT_ABY_ShadowFlame_A01` |
| `Aerathea Basari Female.png` | Character/NPC/class | Basari | Basari character source; create race/culture anchor before body package |
| `Basamet Basari Priestess.png` | Character/NPC/class | Basari | Basari priestess character source; package needed after Basari anchor |
| `Basari Female 1.png` | Character/NPC/class | Basari | Basari female body/outfit source; package needed |
| `Basari Female 5.png` | Character/NPC/class | Basari | Basari female body/outfit source; package needed |
| `Basari Female6.png` | Character/NPC/class | Basari | Basari female body/outfit source; naming normalization needed |
| `Basari Female 10.png` | Character/NPC/class | Basari | Basari female body/outfit source; package needed |
| `BasariFemale3.png` | Character/NPC/class | Basari | Basari female body/outfit source; naming normalization needed |
| `Basarifemale4.png` | Character/NPC/class | Basari | Basari female body/outfit source; naming normalization needed |
| `Basarifemale7.png` | Character/NPC/class | Basari | Basari female body/outfit source; naming normalization needed |
| `Basarifemale8.png` | Character/NPC/class | Basari | Basari female body/outfit source; naming normalization needed |
| `Basarifemale9.png` | Character/NPC/class | Basari | Basari female body/outfit source; naming normalization needed |
| `Basarifemale10.png` | Character/NPC/class | Basari | Basari female body/outfit source; naming normalization needed |
| `Basari Male1.png` | Character/NPC/class | Basari | Basari male body/outfit source; package needed |
| `Basari Male2.png` | Character/NPC/class | Basari | Basari male body/outfit source; package needed |
| `BasariMale4.png` | Character/NPC/class | Basari | Basari male body/outfit source; naming normalization needed |
| `basarimale7.png` | Character/NPC/class | Basari | Basari male body/outfit source; naming normalization needed |
| `basarimale8.png` | Character/NPC/class | Basari | Basari male body/outfit source; naming normalization needed |
| `basarimale9.png` | Character/NPC/class | Basari | Basari male body/outfit source; naming normalization needed |
| `Basarimale10.png` | Character/NPC/class | Basari | Basari male body/outfit source; naming normalization needed |
| `Basarimale12.png` | Character/NPC/class | Basari | Basari male body/outfit source; naming normalization needed |
| `Basari male and female2.png` | Character/NPC/class | Basari | Basari male/female comparison source; package or reference after visual inspection |
| `Basarimaleandfemale.png` | Character/NPC/class | Basari | Basari male/female comparison source; naming normalization needed |
| `Basari Sentinels.png` | Character/NPC/class | Basari | Basari sentinel class/guard source; package needed |
| `Basari Temple.png` | Building/settlement/environment | Basari | Basari temple environment source; building package needed after culture anchor |
| `Gnome Female 12.png` | Character/NPC/class | Gnome/Mekgineer | Gnome character variant; compare with existing gnome body work before package |
| `GnomeFemaleHeavyMek11.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; child package needed after Mek suit kit intake |
| `GnomeFemaleHeavyMek17.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomeFemaleHeavyMek19.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomefemaleHeavyMek12.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; naming normalization needed |
| `GnomefemaleHeavyMek13.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomefemaleHeavyMek14.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomefemaleHeavyMek15.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomefemaleHeavyMek16.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomefemaleHeavyMek18.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomefemaleHeavyMek20.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomefemaleMediumMek11.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Medium Mek variant; package needed |
| `GnomefemalemediumMek12.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Medium Mek variant; naming normalization needed |
| `GnomemaleHeavyMek11.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomemaleHeavyMek12.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomemaleHeavyMek13.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomemaleHeavyMek14.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomemaleHeavyMek15.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `GnomemaleHeavyMek16.png` | Mek suit/mechanical companion | Gnome/Mekgineer | Heavy Mek variant; package needed |
| `Iona.png` | Character/NPC/class | Gnome/Mekgineer | Visual intake complete in `KIT_GNM_IonaSiegebreaker_A01`; named gnome hero-pilot, heavy Mek, arc cannon, and encounter child items proposed |
| `Kittehbee.jpg` | Creature/mount | Aerathea/Common | Non-PNG creature/pet source; visually inspect before deciding whether to accept, retire, or package |

## Visual Intake Completion 2026-06-25

| Source group | Intake result | Package location | Approval state |
| --- | --- | --- | --- |
| Abyss/Anathema source set | 45 source concepts classified into rank troops, elite demons, casters, hounds, siege threats, lords, and Anathema siege-drake variants | `docs/assets/kits/KIT_ABY_ShadowFlame_A01/CHILD_ASSET_INTAKE.md` | First ten child packages are proposed only; DCC build approval pending |
| Generated Abyss lore images | 10 generated lore images compared against live source concepts; retained as named elite/boss mood references | `docs/assets/kits/KIT_ABY_ShadowFlame_A01/SOURCE_COMPARISON.md` | Reference only until individual entity approval |
| `Gnome Mek fighting Demon.png` | Routed as cross-faction encounter reference for Gnome heavy Mek versus winged Abyss demon | `docs/assets/kits/KIT_GNM_IonaSiegebreaker_A01/CHILD_ASSET_INTAKE.md` | Reference only |
| `Iona.png` | Classified as named Gnome/Mekgineer hero-pilot plus heavy Mek and arc cannon encounter kit | `docs/assets/kits/KIT_GNM_IonaSiegebreaker_A01/PRODUCTION_PACKAGE.md` | Concept direction proposed; DCC build approval pending |

## Live Refresh Delta 2026-06-25 - Giant And Blood Axe Addendum

A same-day follow-up scan found 48 additional Giant, Blood Axe Tribe, and named Giant source concepts. A visual contact sheet and the late-added `BloodAxeArmory.png` collage were reviewed before classification. Source-level intake is recorded in `docs/assets/intake/ACIQ-P02_01_GIANT_BLOODAXE_SLATE.md`; `SK_GIA_Base_A01` now has a production package and modeling handoff, while Blood Axe armory, warband, camp, ritual-stone, and Giant environment children still need expansion before DCC or Unreal work.

| Source concept | Category | Faction/theme | Build interpretation |
| --- | --- | --- | --- |
| `Blood Axe Fist Hunting Party.png` | Character/NPC/class | Blood Axe Tribe | Blood Axe hunting warband reference; route through `KIT_GIA_BloodAxeWarband_A01` after Giant body/scale anchor |
| `BloodAxe Village.png` | Building/settlement/environment | Blood Axe Tribe | Blood Axe camp/village kit source with red banners, bone markers, and rough highland structures |
| `BloodAxeArmory.png` | Armory/weapons/gear | Blood Axe Tribe | Collage-heavy Blood Axe armory and bowyer workshop source; route to `KIT_GIA_BloodAxeArmory_A01` before child packages |
| `BloodAxeCamp.png` | Building/settlement/environment | Blood Axe Tribe | Blood Axe fortified camp board; route to `KIT_GIA_BloodAxeCamp_A01` |
| `BloodAxeChieftan.png` | Character/NPC/class | Blood Axe Tribe | Chieftain/throne hall source; route to `SK_GIA_BloodAxeChieftain_A01` and hall dressing references |
| `BloodAxeForge.png` | Building/settlement/environment | Blood Axe Tribe | Forge and brutal camp-crafting reference; route to Blood Axe camp/forge modules |
| `BloodAxeGate.png` | Building/settlement/environment | Blood Axe Tribe | Gatehouse/entry marker source; route to Blood Axe defensive modules |
| `BloodAxeGiantMale.png` | Character/NPC/class | Blood Axe Tribe | Male Blood Axe giant body/armor variant; route through Giant body/style package |
| `BloodAxeGiantMale2.png` | Character/NPC/class | Blood Axe Tribe | Alternate male Blood Axe giant with heavy axe silhouette; variant source |
| `BloodAxeLeaderMale.png` | Character/NPC/class | Blood Axe Tribe | Male leader/champion source; package candidate after chieftain and warband hierarchy |
| `BloodAxeRitual.png` | Building/settlement/environment | Blood Axe Tribe | Ritual altar/standing-stone source; route to `KIT_GIA_BloodAxeRitualStones_A01` |
| `BloodAxeShamanHut.png` | Building/settlement/environment | Blood Axe Tribe | Shaman hut and ritual camp structure; route to Blood Axe camp modules |
| `BloodAxeShelter.png` | Building/settlement/environment | Blood Axe Tribe | Nomad shelter/tent structure source; route to camp kit |
| `BloodAxeStronghold.png` | Building/settlement/environment | Blood Axe Tribe | Blood Axe stronghold/approach environment source; route to hostile settlement variant |
| `BloodAxecamp.png` | Building/settlement/environment | Blood Axe Tribe | Lowercase duplicate-name camp source; compare with `BloodAxeCamp.png` during child expansion |
| `Bloodaxe Army.png` | Character/NPC/class | Blood Axe Tribe | Blood Axe army formation source; route as hierarchy and scale reference for warband package |
| `Giant Fortress Entrance.png` | Building/settlement/environment | Giant | Hidden mountain fortress entrance source; route to `KIT_GIA_MountainCaveTown_A01` |
| `Giant Settlement.png` | Building/settlement/environment | Giant | Civilized cave settlement interior/terrace source; route to Giant cave-town kit |
| `Giant Settlement1.png` | Building/settlement/environment | Giant | Exterior cliff settlement and monumental masonry source; route to Giant cave-town kit |
| `Giant.png` | Character/NPC/class | Giant | General Giant body/weapon/lion-shield silhouette source; route to Giant body/style anchor |
| `Giant1.png` | Character/NPC/class | Giant | Alternate Giant warrior/champion body source; variant for body/style anchor |
| `Giant2.png` | Character/NPC/class | Giant | Alternate Giant warrior with heavy weapon and shield/lion motif; variant source |
| `GiantBloodAxeHuntersMale.png` | Character/NPC/class | Blood Axe Tribe | Male Blood Axe hunter group source; route to warband and hunting-party hierarchy |
| `GiantBloodAxeMale3.png` | Character/NPC/class | Blood Axe Tribe | Male Blood Axe giant with paired hunters/warriors; variant source |
| `GiantBloodAxeMale4.png` | Character/NPC/class | Blood Axe Tribe | Male Blood Axe giant champion with chained shield/lion motif; variant source |
| `GiantBloodAxeMaleShaman.png` | Character/NPC/class | Blood Axe Tribe | Blood Axe male shaman/cult leader source; route to shaman class package |
| `GiantBloodAxeMaleandFemale.png` | Character/NPC/class | Blood Axe Tribe | Blood Axe male/female comparison source; use for scale and outfit variant matrix |
| `GiantFemale.png` | Character/NPC/class | Giant | Female Giant named/hero-style body source; route to Giant body/style anchor |
| `GiantFemale1.png` | Character/NPC/class | Giant | Female Giant variant with heavy weapon and shield/lion motif; body/style source |
| `GiantFemale3.png` | Character/NPC/class | Giant | Female Giant battlefield/warrior variant; body/style source |
| `GiantFemale4.png` | Character/NPC/class | Giant | Female Giant hunter/warrior variant; body/style source |
| `GiantFemale5.png` | Character/NPC/class | Giant | Female Giant body/outfit variant; body/style source |
| `GiantFemaleBloodAxe1.png` | Character/NPC/class | Blood Axe Tribe | Female Blood Axe giant variant; route to Blood Axe body/outfit matrix |
| `GiantFemaleShaman.png` | Character/NPC/class | Giant | Female Giant shaman/mystic source; separate civilized/neutral shaman from Blood Axe cult roles |
| `GiantMale1.png` | Character/NPC/class | Giant | Male Giant body/warrior variant; route to Giant base style matrix |
| `GiantMale2.png` | Character/NPC/class | Giant | Male Giant heavy hammer variant; route to Giant weapon scale and body style |
| `GiantMale3.png` | Character/NPC/class | Giant | Male Giant with blue-glow weapon source; use sparingly as Giant magic/hero variant |
| `GiantMale4.png` | Character/NPC/class | Giant | Male Giant heavy hammer/stonework silhouette source; route to body/style anchor |
| `GiantMaleandFemale.png` | Character/NPC/class | Giant | Male/female comparison source; use for base proportion and scale sheet |
| `GiantMaleandFemale3.png` | Character/NPC/class | Giant | Male/female battlefield comparison source; use for body/gear scale matrix |
| `GiantSettlement3.png` | Building/settlement/environment | Giant | Giant cave-town interior bridge/hall source; route to cave-town kit |
| `GiantSettlement4.png` | Building/settlement/environment | Giant | Snow cliff hidden settlement source; route to camouflaged exterior modules |
| `GiantSettlement5.png` | Building/settlement/environment | Giant | Forge/workshop cave settlement source; route to Giant masonry and craft modules |
| `GiantSettlement6.png` | Building/settlement/environment | Giant | Mountain gate/fortress approach source; route to entrance and wall modules |
| `GiantSettlement7.png` | Building/settlement/environment | Giant | Terraced hidden city source; route to cave-town vertical layout modules |
| `GiantSettlement8.png` | Building/settlement/environment | Giant | Interior processional hall/source; route to halls, stairs, and visitor paths |
| `GiantSettlement9.png` | Building/settlement/environment | Giant | Deep cave district source; route to bridge, lighting, and cliff-home modules |
| `Yiva.png` | Character/NPC/class | Giant | Named Giant character source; proposed future `SK_GIA_Yiva_A01` after Giant body/style approval |

## Full Intake List

| Source concept | Category | Faction/theme | Build interpretation |
| --- | --- | --- | --- |
| `Armorer Workshop.png` | Armory/weapons/gear | Aerathea/Common | Create Aerathea/Common armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Relic Seekers and Arcane Trails.png` | Armory/weapons/gear | Aerathea/Common | Create Aerathea/Common armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Anubisath Armaments.png` | Armory/weapons/gear | Anubisath/Sutekh | Create Anubisath/Sutekh armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Dark Elven Armory.png` | Armory/weapons/gear | Dark Elven | Child intake and kit production package complete in `docs/assets/kits/KIT_DEL_Armory_A01/`; priority child package docs ready; DCC builds pending |
| `Drakhar Arms Relics and Field Gear.png` | Armory/weapons/gear | Drakhar | Child intake and kit production package complete in `docs/assets/kits/KIT_DKH_FieldGear_A01/`; priority child package docs ready; DCC builds pending; source scale conflicts with approved Drakhar anchor |
| `Dwarven Ancestral Armor.png` | Armory/weapons/gear | Dwarven | Create Dwarven armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Dwarven Armory.png` | Armory/weapons/gear | Dwarven | Child intake and kit production package complete in `docs/assets/kits/KIT_DWR_Armory_A01/`; priority child package docs ready; DCC builds pending |
| `Dwarven Armory2.png` | Armory/weapons/gear | Dwarven | Create Dwarven armory kit: weapons, armor silhouettes, racks/displays, material set, and Unreal import specs |
| `Elven Armory.png` | Armory/weapons/gear | Elven | Child intake and kit production package complete in `docs/assets/kits/KIT_ELV_Armory_A01/`; priority child package docs ready; DCC builds pending |
| `Gnome Armory.png` | Armory/weapons/gear | Gnome/Mekgineer | Kit package and child asset intake complete in `docs/assets/kits/KIT_MKG_Armory_A01/`; all catalog child production packages and handoffs documented; first ten child DCC meshes, Unreal imports, and startup placements or socket-fit previews complete |
| `Minotaur Arsenal.png` | Armory/weapons/gear | Minotaur | Child intake and kit production package complete in `docs/assets/kits/KIT_MIN_Arsenal_A01/`; priority child package docs ready; DCC builds pending |
| `Orc Arsenal.png` | Armory/weapons/gear | Orc | Child intake and kit production package complete in `docs/assets/kits/KIT_ORC_Arsenal_A01/`; priority child package docs ready; DCC builds pending |
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
| `Gryphon.png` | Creature/mount | Aerathea/Common | Base gryphon family package ready in `docs/assets/creatures/SK_CRE_Gryphon_A01/`; variant-specific packages pending |
| `Gryphon1.png` | Creature/mount | Aerathea/Common | Base gryphon family package ready in `docs/assets/creatures/SK_CRE_Gryphon_A01/`; variant-specific packages pending |
| `Gryphon10.png` | Creature/mount | Aerathea/Common | Base gryphon family package ready in `docs/assets/creatures/SK_CRE_Gryphon_A01/`; variant-specific packages pending |
| `Gryphon2.png` | Creature/mount | Aerathea/Common | Base gryphon family package ready in `docs/assets/creatures/SK_CRE_Gryphon_A01/`; variant-specific packages pending |
| `Gryphon5.png` | Creature/mount | Aerathea/Common | Base gryphon family package ready in `docs/assets/creatures/SK_CRE_Gryphon_A01/`; variant-specific packages pending |
| `Gryphon6.png` | Creature/mount | Aerathea/Common | Base gryphon family package ready in `docs/assets/creatures/SK_CRE_Gryphon_A01/`; variant-specific packages pending |
| `Gryphon7.png` | Creature/mount | Aerathea/Common | Base gryphon family package ready in `docs/assets/creatures/SK_CRE_Gryphon_A01/`; variant-specific packages pending |
| `Gryphon8.png` | Creature/mount | Aerathea/Common | Base gryphon family package ready in `docs/assets/creatures/SK_CRE_Gryphon_A01/`; variant-specific packages pending |
| `Gryphon9.png` | Creature/mount | Aerathea/Common | Base gryphon family package ready in `docs/assets/creatures/SK_CRE_Gryphon_A01/`; variant-specific packages pending |
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
