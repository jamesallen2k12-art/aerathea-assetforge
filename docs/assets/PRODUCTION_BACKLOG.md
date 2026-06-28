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

- 547 source concept files: 546 PNG files and 1 JPG file.
- The source-file count is not the final asset count.
- Some images are collages, catalogs, contact sheets, or multi-panel boards with many child assets.
- Each source image must be visually inspected and expanded into child assets before it is marked complete.
- The 2026-06-25 refresh tracks 139 live source files not yet represented in the full manifest intake table: the initial 91-file refresh plus a 48-file Giant/Blood Axe addendum. The 2026-06-26 Ogre addendum adds 31 Ogre source files. The 2026-06-27 addendum adds 63 Infernal/Balgoroth source files, 21 Gnome-vs-Ogre encounter references, and 4 Gnome heavy Mek variants. All addenda are tracked in `docs/assets/ASSET_CONCEPTS_MANIFEST.md`.

Collage examples:

- Armory sheets can expand into weapons, armor pieces, shields, tools, grenades, backpacks, power cores, racks, display props, and outfit configurations.
- Portrait sheets can expand into many UI portrait assets.
- Creature sheets can expand into multiple variants or body-part references.
- Abyss, Anathema, demon, lord, and troop sheets can expand into hierarchy packages: lesser spawn, troops, hounds, siegers, lords, bound servitors, and boss-class entities.
- Giant and Blood Axe sheets can expand into body/scale packages, named NPCs, warbands, armory/weapon kits, cave-town modules, nomad camps, ritual stones, gates, forge props, and settlement camouflage rules.
- Ogre sheets can expand into body/scale packages, Warrior/Teknomancer/Shaman/Necromancer variants, Teknomancy kits, forge props, siege weapons, cairn fortifications, stone gates, barracks, necropolises, and settlement interiors.
- Infernal sheets can expand into adult body bands, Lesser lifecycle stages, sorcerer and lit-brand class variants, cult gate scenes, culling trial floors, horn-wing arches, brand materials, and Balgoroth ritual props.
- Gnome-vs-Ogre encounter sheets can expand into heavy Mek variants, shield-wall Blueprint/VFX tests, Ogre Teknomancer opponents, Ogre warrior waves, cairn gate set dressing, and Manticore interrupt variants.
- Building and interior boards can expand into modular walls, doors, roofs, pillars, props, lamps, banners, collision pieces, and material sets.
- Gnome Mek sheets can expand into multiple armor classes, weapons, mechanical limbs, backpacks, sockets, and VFX points.

Tracking source:

- `docs/assets/ASSET_CONCEPTS_MANIFEST.md`
- `docs/assets/APPROVAL_QUEUE.md`

## Current Packaged Assets

These have production package documentation in `docs/assets/`:

| Asset | Current state | Next action |
| --- | --- | --- |
| `SM_AET_TargetDummy_A01` | Blender source and FBX generated, imported to Unreal, startup blockout replaced, validation passing | Keep as reusable static mesh dependency for `BP_AET_TargetDummy_A01` |
| `SM_AET_PortalArch_A01` | Blender source and FBX generated, imported to Unreal, startup portal visual replaced, validation passing; current import uses older smaller scale assumptions | Explore several old, mysterious, awe-inspiring 10 m / 33 ft universal portal directions, then rebuild/rescale before final signoff |
| `BP_AET_Portal_A01` | Native preview state, focus overlap, use-request cooldown, destination validation, and Blueprint events implemented; Blueprint compiled; startup validation passing; final portal target is universal, race-neutral, and 10 m clear traversal scale | Add final traversal, VFX, audio, and destination registry once gameplay rules and final portal visual direction are approved |
| `BP_AET_TargetDummy_A01` | Native training hit/break/reset behavior implemented; Blueprint asset created and compiled; startup actor replaced with Blueprint; validation passing | Add optional visual/audio/UI feedback after training interaction rules are approved |
| `SM_MKG_WorkshopPropCrate_A01` | Blender source and FBX generated, imported to Unreal, placed in startup scene, validation passing | Use as Mekgineer material/style reference for workshop props |
| `SM_AET_ModularGroundTile_A01` | Blender source and FBX generated, imported to Unreal, placed as 5x5 startup ground-tile layout, validation passing | Use for early scene layout and collision/material validation |
| `KIT_MKG_Armory_A01` | Kit package ready, child asset intake complete, all catalog child production packages documented; first eleven child DCC meshes/imports/startup placements or socket-fit previews complete, including `SM_MKG_GrappleHook_A01` with cable/muzzle sockets | Review GrappleHook in the startup scene, then choose the next armory child only after final-art priority is clear |
| `KIT_DWR_Armory_A01` | Child intake and kit production package ready; priority child packages ready | Choose first DCC build from Oathkeeper hammer, Stonewall shield, Stonebound helm, or runic glow states |
| `KIT_ELV_Armory_A01` | Child intake and kit production package ready; priority child packages ready | Choose first DCC build from Moonblade, Silverleaf Recurve, Moonward buckler, or Aetherium lantern |
| `KIT_DEL_Armory_A01` | Child intake and kit production package ready; priority child packages ready | Choose first DCC build from Duskspite blade, Veilstrider bow, Aegis of Eternal Dusk, or Shadow Armory material set |
| `KIT_ORC_Arsenal_A01` | Child intake and kit production package ready; priority child packages ready | Choose first DCC build from GreatAxe A01, shields, shamanic talismans, or runic affinities |
| `KIT_MIN_Arsenal_A01` | Child intake and kit production package ready; priority child packages ready | Choose first DCC build from GreatAxe A01, CrushingMaul A01, hide shields, or helmets |
| `KIT_DKH_FieldGear_A01` | Child intake and kit production package ready; priority child packages ready; package uses approved A04 Drakhar scale: females 3'6"-4'2", males 4'0"-4'6" over conflicting source-sheet scale | Choose first DCC build from Riversind Recurve, curved daggers, ReedShell shield, or magic tracking charms |
| `KIT_ABY_ShadowFlame_A01` | Visual intake complete; Abyss/Anathema hierarchy, generated-lore comparison, and first ten proposed child creature packages ready for approval review | Choose which proposed Abyss or Anathema creature moves to approved DCC modeling |
| `KIT_GNM_IonaSiegebreaker_A01` | Visual intake complete for `Iona.png`; named gnome hero, heavy Mek, twin arc cannon, and encounter child items proposed | Choose whether Iona's heavy Mek, pilot, or arc cannons should become the first approved child package |
| `KIT_GNM_OGR_RivalryEncounter_A01` | Source intake and production package ready for 21 Gnome-vs-Ogre encounter images plus 4 added heavy Mek variants; first-pass Unreal implementation now includes shieldwall Blueprint/VFX contract polish, Ogre Teknomancer, Heavy Mek, Ogre Warrior, Ogre cairn gate, crude Tek pylon, base/interrupt Manticore, Ogre Shaman, Ogre Necromancer, pylon and Manticore wrapper Blueprints, wired native encounter coordinator, template-derived branch Niagara targets, validated shield shutdown-collapse VFX target coverage, auto-advancing review phases, phase-specific focused capture hooks, a dedicated phase sequence validator, pylon/Manticore gameplay timing trace validation, and a final-art replacement dependency plan | Follow the final-art replacement plan while continuing final branch VFX graph polish and future gameplay rule binding |
| `VFX_GNM_AetherShieldWall_A01` | First-pass helper mesh/material-state implementation, native shieldwall VFX parameter contract, native Niagara component hook, assigned `NS_GNM_AetherShieldWall_A01` Unreal target, and validated template-derived named shield emitter assets exist including `NE_GNM_ShieldShutdownCollapse_A01`; bespoke graph polish still pending | Polish the final Niagara graph inside `NS_GNM_AetherShieldWall_A01` against the existing native `User.*` parameter contract |
| `KIT_OGR_Teknomancy_A01` | Production package and child intake ready; `SM_OGR_CrudeTekPylon_A01` first-pass DCC/Unreal import exists; other Teknomancy children pending | Choose the next Teknomancy child after the pylon Blueprint behavior is wired into the encounter coordinator |
| `SM_OGR_CairnBattleGate_A01` | First-pass Blender source and FBX generated, imported to Unreal, material instances and LOD0-LOD3 generated, static mesh sockets and simple collision added, startup review actor placed, validation passing | Replace blockout topology with final sculpt/retopo, authored UVs/textures, tuned collision, modular wall variants, and Blueprint gate behavior |
| `SM_OGR_CrudeTekPylon_A01` | First-pass Blender source/FBX generated, imported to Unreal, material instances assigned, LOD0-LOD3 generated, static mesh sockets added, startup review actor placed, validation passing; `BP_OGR_CrudeTekPylon_A01` wrapper now exists | Replace blockout mesh with final sculpt/retopo and author final pylon Niagara after wrapper review |
| `BP_OGR_CrudeTekPylon_A01` | Native-backed pylon state wrapper created, compiled, placed in startup, wired to the Gnome/Ogre encounter coordinator with Idle/Charged/Overload/Damaged/Destroyed states, assigned `NS_OGR_CrudeTekPylon_A01`, and gameplay damage/repair windows plus trace radii exposed | Polish final pylon VFX graph and define final quest repair/destroy rules after gameplay design approval |
| `BP_CRE_ManticoreInterrupt_A01` | Native-backed Manticore interrupt wrapper created, compiled, placed in startup, wired to the encounter coordinator with Hidden/Stalking/Telegraph/LeapImpact/ThreatHold/Retreat states, assigned `NS_CRE_Manticore_Impact_A01`, and deterministic interrupt timeline plus trace radii exposed | Polish impact Niagara and bind final animation/damage rules after gameplay design approval |
| `BP_GNM_OGR_BattlefieldEncounter_A01` | Native-backed encounter coordinator implemented; Blueprint asset created, compiled, placed in startup, assigned to required and branch actors, and validated with shieldwall impact, pylon, caster, Manticore event hooks, auto-advancing review phases, phase-specific focused/offscreen capture hooks, a dedicated phase sequence validator, and gameplay timing/trace validator | Polish branch VFX graph targets, then move to final Ogre rig warnings and art-model replacement planning |
| `SK_GNM_Base_A01` | First-pass DCC review body/skeleton generated, imported as skeletal mesh, material instances assigned, LOD0-LOD3 generated, gear/VFX sockets added, `PHYS_GNM_Base_A01` assigned, `ABP_GNM_Base_A01` created, startup and focused follow-up readiness validation passing | Replace blockout geometry with approved sculpt/retopo, UVs, authored textures, tuned physics, and animation set |
| `SK_GNM_HeavyMek_Rivalry_A01` | First-pass DCC review source and FBX generated, imported as skeletal mesh, material instances assigned, LOD0-LOD3 generated, Mek/VFX sockets added, `PHYS_GNM_HeavyMek_Rivalry_A01` assigned, `ABP_GNM_HeavyMek_Rivalry_A01` created, startup actor placed | Validate the startup capture with the Ogre Teknomancer and shield wall, then replace blockout geometry with final sculpt/retopo, UVs, textures, tuned physics, and animation set |
| `SK_GIA_Base_A01` | Giant scale superseded by A04 review data: females 14-15 ft, males 14'10"-16'0"; previous first-pass DCC/Unreal import used older scale assumptions | Rebuild or rescale Giant base after A04 scale chart is approved; do not use the current import as final hand/body scale lock |
| `SK_OGR_Base_A01` | First-pass male/female Ogre body sources generated, imported to Unreal, material instances and LOD0-LOD3 generated, sockets/physics/ABP placeholders created, startup validation passing, and focused male shared-skeleton validator passing | Replace blockout geometry with approved sculpt/retopo, UVs, authored textures, tuned physics, and animation set |
| `SK_OGR_Teknomancer_A01` | First-pass Ogre Teknomancer class-fit source generated, imported to Unreal on the shared Ogre male skeleton, material instances and LOD0-LOD3 generated, sockets/physics/ABP placeholder created, startup review actor placed, and focused shared-skeleton validation passing | Review combined startup capture, then complete final Ogre rig fit, sculpt/retopo, UVs/textures, tuned physics, and animation set |
| `SK_OGR_Warrior_Rival_A01` | First-pass Ogre Warrior source generated, imported to Unreal, material instances and LOD0-LOD3 generated, shield/hammer/VFX sockets added, physics asset and ABP placeholder created, startup review actor placed | Replace blockout geometry with approved sculpt/retopo, UVs, authored textures, tuned physics, shield/hammer traces, and animation set |
| `SK_OGR_Shaman_A01` | First-pass class-fit Blender source/FBX generated, imported to Unreal on shared Ogre male skeleton, material instances assigned, LOD0-LOD3 generated, sockets/physics/ABP placeholder created, startup review actor placed, validation passing | Tune class sockets and create real animation/ability Blueprint behavior after final Ogre rig pass |
| `SK_OGR_Necromancer_A01` | First-pass class-fit Blender source/FBX generated, imported to Unreal on shared Ogre male skeleton, material instances assigned, LOD0-LOD3 generated, sockets/physics/ABP placeholder created, startup review actor placed, validation passing | Tune class sockets and create real animation/ability Blueprint behavior after final Ogre rig pass |
| `SK_INF_Base_A01` | First-pass compact/tall adult Infernal DCC source and FBX exports generated, imported to Unreal as skeletal meshes with material instances, LOD0-LOD3, sockets, physics assets, ABP placeholders, and scale/silhouette review approved; 2026-06-27 adult, lit-brand, gate-guard, and sorcerer sources routed | Replace blockout geometry with approved sculpt/retopo, UVs, authored textures, tuned wing/tail physics, and class animation sets |
| `SK_INF_Lesser_A01` | First-pass Lesser Infernal lifecycle DCC source and FBX exports generated for Spawn, 1st Kill, Blooded, Elder, and Ancient; imported to Unreal with material instances, LOD0-LOD3, sockets, physics assets, ABP placeholders, and lifecycle silhouette review approved; 2026-06-27 child, clutch, and Lesser variants routed | Replace blockout geometry with approved sculpt/retopo, UVs, authored textures, tuned per-stage capsules/physics, and stage animation sets |
| `SM_INF_CullingTrialFloor_A01` | Blender source and FBX generated, imported to Unreal, material instances assigned, LOD0-LOD3 generated, static mesh sockets added; first-pass DCC/Unreal visual review accepted | Polish final sculpted slab edges, authored UVs/textures, VFX state Blueprint, and collision fit after cult kit layout is approved |
| `SM_AET_Palisade_A01` | Five-module DCC source set generated, imported, placed in startup scene, simple UCX collision included, material instances assigned, LOD0-LOD3 generated, validation passing | Polish final UV atlas, texture set, collision fit, and snap review in GUI |
| `SK_CRE_Gryphon_A01` | First-pass DCC review mesh/skeleton generated, imported as skeletal mesh, material instances assigned, LOD0-LOD3 generated, creature sockets added, `PHYS_CRE_Gryphon_A01` assigned, `ABP_CRE_Gryphon_A01` created, wing-spread animation blockout imported, startup and focused follow-up readiness validation passing | Replace blockout with approved sculpt/skin/UVs, tuned physics bodies, and full animation set |
| `SK_CRE_Manticore_A01` | First-pass base Blender source/FBX generated, imported to Unreal with generated skeleton, material instances, LOD0-LOD3, sockets, physics asset, ABP placeholder, startup review actor, and validation passing | Review scale/silhouette, then replace blockout with final sculpt/skin/UVs/textures and real animation set |
| `SK_CRE_Manticore_Interrupt_A01` | First-pass encounter variant Blender source/FBX generated, imported to Unreal against the base Manticore skeleton, material instances, LOD0-LOD3, sockets, physics asset, startup review actor, and validation passing | Add encounter Blueprint/VFX timing after the coordinator assigns Manticore branch references |

## Existing Startup Scene Blockouts

These exist in `L_Aerathea_Startup` as validation/blockout content, not final production assets:

| Blockout | Production need |
| --- | --- |
| `AET_BOOT_PlayerScale_180cm` | Keep as scale reference until playable humanoid package exists |
| `AET_BOOT_GnomeScale_110cm` | Replace or supplement after gnome body reference package exists |
| `AET_BOOT_MinotaurScale_270cm` | Replace or supplement after minotaur body reference package exists |
| `AET_BOOT_PortalArch_*` | Retired in startup scene; replaced by production portal actor using `SM_AET_PortalArch_A01` |
| `AET_BOOT_PortalCore_Aetherium_A01` | Retired in startup scene; replaced by production portal actor core component |
| `AET_BOOT_TargetDummy_*` | Replaced by `BP_AET_TargetDummy_A01` using `SM_AET_TargetDummy_A01` |
| `AET_BOOT_GroundTile_20m_A01` | Replaced by 5x5 `SM_AET_ModularGroundTile_A01` layout |

## Race Anchors Needing Production Packages

All approved races below need concept sheets, body proportion sheets, starter outfit packages, material language sheets, Unreal import specs, and eventually skeletal mesh packages.

| Race | Approved anchor | Missing production packages |
| --- | --- | --- |
| Gnomes | Compact inventors with large heads, compact expressive ears that do not inflate measured height, sturdy legs, oversized boots, tools, goggles, brass/copper/dark iron/leather/blue Aetherium; females 3'0"-3'6", males 3'4"-4'0" | First-pass `SK_GNM_Base_A01` body/skeleton/physics import exists; approved sculpt/retopo, starter outfit build, and goggles/accessory mesh still needed |
| Dwarves | Broad dense mountain-forged weaponsmiths/runesmiths/guardians with stone, steel, brass, blue runes, fur, leather; female faces clean-shaven, male dwarves have practical full beards with armor clearance; females 4'2"-4'6", males 4'4"-5'0" | Base body sheet, male/female body package, starter armor, runesmith/weapon kit |
| Elves | Tall graceful ancient nature/moon/star culture with living wood, silver, moonstone, silverleaf, blue-white Aetherium; females 5'2"-5'8", males 5'8"-6'0" | Base body sheet, starter outfit, ranger kit, runesinger/moonblade kit, living-architecture material sheet |
| Dark Elves | Elegant shadowed oath-bound culture with dark silver, obsidian, violet glow, crescent motifs; females 5'2"-5'8", males 5'8"-6'0" | Base body sheet, starter outfit, shadowblade kit, priestess/spellbow kit, dark hall material sheet |
| Infernals | Mortal-descended demonic race blessed by Balgoroth, with reddish skin, required horns, large leathery wings, long thick tails, black claws, regeneration, invisible sight, natural-weapon doctrine, contempt for weakness, Lesser Infernal culling temper, and locked Compact/Standard/Greater/Exalted adult body bands within 5'0"-9'0" | First-pass `SK_INF_Base_A01` and `SK_INF_Lesser_A01` DCC/Unreal scale review approved; 63 new source concepts routed into adult, Lesser, sorcerer, brand, clutch, and cult-gate follow-up packages; approved visual cleanse standard locked in `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`; `SK_INF_Mage_A01` package and handoff ready; needs final sculpt/retopo/UVs/textures, horn/wing/tail rig polish, warrior/rogue/hunter class variants, mage DCC build, and first cult DCC child import |
| Orcs | Noble upright powerful clan culture with honor, spirituality, shamanism, disciplined warriors; females 6'2"-6'8", males 6'6"-7'0" | Base body sheet, starter outfit, clan warrior kit, shaman kit, weapon/material sheet |
| Minotaurs | Plains/lowlands strength culture, simple brutal weapons, magic resistant, hide/bone/raw iron/fur/leather; females 7-8 ft, males 8-9 ft | Base body sheet, starter outfit, barbarian/berserker kit, simple heavy weapon kit, tribal marking sheet |
| Ogres | War-created, heavily muscled, very broad battlefield terrors with instinctive crude Teknomancy, shamans, necromancers, sentinels, stone cairns, defensive fortifications, and jealousy of Gnome Mekgineer creations; females 10'0"-10'6", males 10'4"-11'0" | First-pass `SK_OGR_Base_A01`, `SK_OGR_Teknomancer_A01`, `SK_OGR_Warrior_Rival_A01`, `SK_OGR_Shaman_A01`, `SK_OGR_Necromancer_A01`, `SM_OGR_CairnBattleGate_A01`, and `SM_OGR_CrudeTekPylon_A01` review imports exist; needs final sculpt/retopo/UVs/textures, animation, and expanded cairn/Teknomancy kits |
| Drakhar Lizardfolk | Desert lizardfolk obsessed with magic, Volcreon-linked, scales/bone/leather/sun-baked stone/ember/relics; females must read clearly female while remaining lizardfolk; females 3'6"-4'2", males 4'0"-4'6" | Base body sheet, scale/material sheet, starter outfit, relic/magic-item kit, rogue/wizard/shaman variants |
| Giants | Remote mountain people with civilized master stoneworkers, hidden cave towns, nomadic highland bands, and the brutal Blood Axe Tribe as a hostile sub-faction; females 14-15 ft, males 14'10"-16'0" | `SK_GIA_Base_A01` package exists but its first-pass DCC/Unreal import used older scale assumptions; rebuild/rescale after A04 review approval, then proceed with Blood Axe warband kit, armory kit, and named Giant NPC packages |
| Valar | Human-like highborn northern people, not elven/Tolkien-like; rounded human ears, strong human faces, broad athletic frames, fur-trimmed blue/silver/gold armor, cloaks, oath symbols; females 6'6"-7'0", males 6'10"-7'4" | Base body sheet, starter outfit, armory kit, settlement/material language |
| Anubisath/Sutekh | Scale anchor established: females 7'6"-8'0", males 7'10"-8'4"; full culture/material/silhouette anchor pending | Race/culture anchor, base body sheet, starter outfit, armory kit, temple/settlement material language |
| Basari | Scale anchor established: females 6-7 ft, males 7-8 ft; full culture/material/silhouette anchor pending | Race/culture anchor, base body sheet, starter outfit, sentinel/priestess kit, temple material language |

Suggested first race package:

- `SK_GNM_Base_A01` or `SK_GNM_Male_A01`, because gnome scale is already represented in the startup map and the Mekgineer crate starts their prop language.

## Armory, Arsenal, And Gear Concepts Needing Production Packages

Armory concepts are not single assets. Treat each armory or gear sheet as a kit source that must be broken into child production packages for weapons, armor pieces, props, materials, sockets, attachment rules, and Unreal import specs.

| Source concept | Faction/theme | Required expansion |
| --- | --- | --- |
| `Gnome Armory.png` | Gnome/Mekgineer | Kit package and child intake complete in `KIT_MKG_Armory_A01`; all catalog child production packages and handoffs documented; first ten DCC imports or fit-previews complete |
| `Dwarven Armory.png` | Dwarven | Child intake and kit production package complete in `KIT_DWR_Armory_A01`; priority child package docs ready; DCC builds pending |
| `Dwarven Armory2.png` | Dwarven | Additional armory variants and display-ready weapons/armor |
| `Dwarven Ancestral Armor.png` | Dwarven | Hero armor set, modular armor pieces, rune/metal/fur material set |
| `Elven Armory.png` | Elven | Child intake and kit production package complete in `KIT_ELV_Armory_A01`; priority child package docs ready; DCC builds pending |
| `Dark Elven Armory.png` | Dark Elven | Child intake and kit production package complete in `KIT_DEL_Armory_A01`; priority child package docs ready; DCC builds pending |
| `Orc Arsenal.png` | Orc | Child intake and kit production package complete in `KIT_ORC_Arsenal_A01`; priority child package docs ready; DCC builds pending |
| `Minotaur Arsenal.png` | Minotaur | Child intake and kit production package complete in `KIT_MIN_Arsenal_A01`; priority child package docs ready; DCC builds pending |
| `Drakhar Arms Relics and Field Gear.png` | Drakhar | Child intake and kit production package complete in `KIT_DKH_FieldGear_A01`; priority child package docs ready; DCC builds pending; source scale conflicts with approved female 3'6"-4'2" and male 4'0"-4'6" Drakhar anchor |
| `Anubisath Armaments.png` | Anubisath/Sutekh | Enemy/faction weapons, armor pieces, seal/necropolis material set |
| `BloodAxeArmory.png` | Blood Axe Tribe | Giant double axes, cleavers, hammers, spears, knives, bows, quivers, bowyer tools, trophy armor, and reforged-metal process reference; create `KIT_GIA_BloodAxeArmory_A01` after Giant hand/body scale is approved |
| `Valararmory.png` | Valar | Valar weapons, armor pieces, oath/warden/ranger variants |
| `Armorer Workshop.png` | Aerathea/Common | Workshop environment kit, racks, benches, tools, display props, forge-adjacent materials |
| `Relic Seekers and Arcane Trails.png` | Aerathea/Common | Relic props, trail markers, arcane field gear, exploration kit |

Suggested first armory package:

- `KIT_MKG_Armory_A01`, because `Gnome Armory.png` is a detailed catalog and connects directly to the existing `SM_MKG_WorkshopPropCrate_A01` and future gnome/Mekgineer production.

## Creature Anchors Needing Production Packages

All approved creatures need concept sheets, scale sheets, skeletal mesh packages, animation lists, collision/physics notes, LOD budgets, and material plans.

| Creature | Approved anchor | Variant backlog |
| --- | --- | --- |
| Abyss/Anathema | Ancient entropic beings of shadow and flame, sealed in the Abyss, destructive to creation, bindable by sorcerers but hostile to binders | Visual intake complete in `KIT_ABY_ShadowFlame_A01`; first ten proposed packages documented for troops, elites, casters, hound, siege brute, lord, and Anathema siege drake; final selection approval pending |
| Gryphon | Eagle front, lion rear, noble mountain/sky guardian with strong feather silhouette, talons, lion tail | First-pass base mesh/skeleton/physics/animation blockout imported in `SK_CRE_Gryphon_A01`; approved golden sculpt pass next, then white, storm, forest, desert, royal, and moonlit variants |
| Manticore | Lion body, bat/draconic wings, scorpion tail, dangerous ruin/desert predator | First-pass base `SK_CRE_Manticore_A01` and encounter `SK_CRE_Manticore_Interrupt_A01` imports exist with shared skeleton, material instances, sockets, physics assets, and validation passing; final sculpt/skin/animation and encounter VFX timing pending |
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
| Portal with Stone Archway | Partially covered by `SM_AET_PortalArch_A01` and `BP_AET_Portal_A01`; final portal should be old, mysterious, awe-inspiring, race-neutral, and large enough for a 10 m / 33 ft clear traversal opening | Explore several final portal directions, then rebuild arch mesh, portal blueprint scale, VFX/audio/interact notes |
| Mekgineer Workshop | Partially seeded by `SM_MKG_WorkshopPropCrate_A01` | Building package, interior prop set, machines, tool racks, lamps |
| Inn | Approved building anchor only | Production package, concept sheet, modular kit, interior notes |
| Lumber Mill | Approved building anchor only | Production package, concept sheet, modular kit, saw/log props |
| Giant Hidden Cave Town | Lore image set exists in `docs/lore/images/giant-stone-caves/`; Giant culture anchor and final direction are not yet approved for DCC | Create `KIT_GIA_MountainCaveTown_A01` after Giant culture/settlement direction approval; split into cave gates, terraces, halls, waterworks, market props, nomad links, Blood Axe variant modules, and Blood Axe Nomad ritual-stone markers |
| Blood Axe Nomad Ritual Stones | Lore added under Giant cave-town notes; standing stones and altars are ritual sites, warnings, memory markers, and guideposts left behind after nomad camps move on | Create future `KIT_GIA_BloodAxeRitualStones_A01` after Blood Axe direction approval; split into altars, standing-stone rings, cairn guideposts, ritual channels, banner poles, and cave approach markers |
| Blood Axe Camp, Armory, And Warband | 22 live source concepts now tracked in the Giant/Blood Axe slate; Blood Axe should remain a hostile Giant sub-faction, not the default Giant culture | Create `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeArmory_A01`, and `KIT_GIA_BloodAxeWarband_A01` after `SK_GIA_Base_A01`; split chieftain, shaman, hunters, troop formations, giant weapons, bows, armor trophies, banners, gates, shelters, forge, and stronghold modules |
| Ogre Cairn Fortifications And Settlement | 31 Ogre source concepts now tracked; visual language includes stone cairns, rough walls, gates, barracks, forge interiors, Tek shops, necropolis, shaman hut, inn, and siege yards; `SM_OGR_CairnBattleGate_A01` provides the first imported gate review module | Create expanded `KIT_OGR_CairnFortifications_A01`, `KIT_OGR_Teknomancy_A01`, `KIT_OGR_Necropolis_A01`, and `KIT_OGR_SettlementInteriors_A01` packages after the rivalry gate module is reviewed against final settlement needs |
| Palisade | Five-module DCC source/import/startup placement complete in `SM_AET_Palisade_A01`; material instances and generated LOD0-LOD3 complete | Polish final UV atlas, texture set, collision fit, and snap review |

Suggested first building package:

- `SM_AET_Palisade_A01` or `SM_AET_House_A01`. Palisade is lower risk for modular collision and LOD validation; house is more representative for settlement style.

## Prop And Blueprint Candidates Found During Scan

These are referenced by existing packages or startup docs and should be promoted when needed.

| Candidate | Reason to create |
| --- | --- |
| `BP_AET_TargetDummy_A01` | Native training hit/break/reset behavior and Blueprint startup actor exist; next pass should add optional visual/audio/UI feedback |
| `SM_AET_TargetDummyArea_A01` | Converts the target dummy into a dressed training-yard area |
| `SM_MKG_Goggles_A01` | Core gnome/Mekgineer identity prop |
| `SM_MKG_Toolkit_A01` | Supports Mekgineer workshop and gnome character identity |
| `SM_AET_WeaponRack_A01` | Useful for barracks, target dummy area, and early combat testing |
| `SM_AET_Lantern_A01` | Common settlement prop and lighting/material test |
| `SM_AET_Banner_A01` | Common faction/culture readability prop |

## Recommended Next Backlog Actions

1. Use `Tools/Unreal/launch_startup_review_editor.sh` when interactive manual inspection is needed for first-pass import scale, silhouette, collision, sockets, and LOD transitions.
2. Review the updated startup scene with `SM_MKG_GrappleHook_A01`, `BP_GNM_HeavyMekShieldwall_A01`, `SK_OGR_Teknomancer_A01`, and `SK_GNM_HeavyMek_Rivalry_A01` visible together.
3. Polish the final pylon, shieldwall, and Manticore Niagara graphs against the native `User.*` contracts, including pylon objective-window and Manticore impact-window parameters.
4. Complete the final Ogre shared-rig/art-model fit after `Tools/Unreal/validate_ogre_shared_skeletons.py` confirms current first-pass skeleton binding.
5. Follow `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/FINAL_ART_REPLACEMENT_PLAN.md` when replacing first-pass review meshes with approved art-model geometry, final UVs, authored texture sets, and tuned collision.
6. Use `docs/assets/GNOME_GRYPHON_FOLLOWUP_READINESS.md` and `Tools/Unreal/validate_gnome_gryphon_followup_readiness.py` before tuning sockets, physics bodies, and animation Blueprint logic for `SK_GNM_Base_A01` and `SK_CRE_Gryphon_A01` after approved final sculpt, skin, and animation direction are available.
7. Use `docs/assets/APPROVAL_QUEUE.md` to clear the remaining approval-gated production lanes.
8. Review and approve one proposed Abyss/Anathema child from `KIT_ABY_ShadowFlame_A01` before any DCC build; production-efficient default is `SK_ABY_BlackPikeTrooper_A01`.
9. Review `KIT_GNM_IonaSiegebreaker_A01` and choose whether Iona's pilot, heavy Mek, or arc cannons should become a child production package; package docs recommend starting with `SK_GNM_IonaSiegebreakerMek_A01`.
10. Approve rebuilding/rescaling `SK_GIA_Base_A01` to the current A04 Giant baselines, or request scale/proportion changes before Blood Axe armory, cave-town, or Giant environment work.
11. Continue Ogre final-art planning from the imported `SK_OGR_Base_A01`, `SK_OGR_Teknomancer_A01`, `SK_OGR_Warrior_Rival_A01`, `SK_OGR_Shaman_A01`, and `SK_OGR_Necromancer_A01` review slices, then resolve the final shared Ogre rig and art-model handoff order.
12. Split `BloodAxeArmory.png` into `KIT_GIA_BloodAxeArmory_A01` child IDs after the Giant rebuild/rescale decision is approved.
13. Review Giant cave-town lore images and approve whether `KIT_GIA_MountainCaveTown_A01` or `KIT_GIA_BloodAxeRitualStones_A01` should become the first Giant environment production package.
14. Explore several old, mysterious, awe-inspiring universal portal directions, then rebuild/rescale `SM_AET_PortalArch_A01` and `BP_AET_Portal_A01` around a 10 m / about 33 ft clear traversal opening after gameplay rules are approved.

## Production Rule

Do not turn backlog entries directly into final assets. Each source concept and each child asset from a collage must move through the approved Aerathea pipeline: asset brief, gameplay purpose, silhouette/material direction, concept prompts or reference, production sheet, modeling notes, UV/material plan, LOD/collision plan, Unreal import notes, and quality checklist.
