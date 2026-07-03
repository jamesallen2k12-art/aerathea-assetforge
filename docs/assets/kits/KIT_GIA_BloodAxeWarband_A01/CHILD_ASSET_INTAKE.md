# KIT_GIA_BloodAxeWarband_A01 Child Asset Intake

## Source

- Source routing: `docs/assets/intake/ACIQ-P02_01_GIANT_BLOODAXE_SLATE.md`
- Source folder: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Parent kit: `KIT_GIA_BloodAxeWarband_A01`
- Intake status: docs-only child split created for planning; no child build target selected
- Scale dependency: validated `SK_GIA_Base_A01` female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"
- Source-storage guardrail: external source concepts remain in the external concept folder only. Do not copy, move, edit, embed, or commit source images for this docs-only package.

## Notes

This child intake splits the Blood Axe warband into visual/production planning rows only. The row names are not final gameplay troop roles, AI classes, combat stats, ability kits, encounter waves, spawn groups, loot rules, or first DCC build targets.

Blood Axe warband rows must stay separate from neutral/civilized Giant culture. They may use red banners, blackened iron, dark steel, rough hide, scorched leather, soot, ash, controlled trophy shapes, and hostile camp-read silhouettes. They must not convert all Giants into Blood Axe raiders or reuse civilized Giant cave-town stoneworker language as the default for this sub-faction.

Existing armory planning provides reusable dependencies for weapons, quivers, banners, trophy helm, raider chest, harness, trophy belt, greaves, and reforged-metal material language. This child intake does not create or select any of those assets for implementation.

## Child Asset Table

| Child ID | Primary sources | Visual planning scope | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| `KIT_GIA_BloodAxeWarband_A01#Chieftain` | `BloodAxeChieftan.png`, `BloodAxeLeaderMale.png`, `Bloodaxe Army.png` | Chieftain and leader silhouette planning | `SK_GIA_BloodAxeChieftain_A01` | Package ready | `docs/assets/characters/SK_GIA_BloodAxeChieftain_A01/PRODUCTION_PACKAGE.md` is ready as planning only for authority read, heavier trophy/armor mass, and red cloth hierarchy. Throne hall or room dressing routes to later camp/stronghold packages. No boss mechanics, AI, combat stats, abilities, loot, or first build selection. |
| `KIT_GIA_BloodAxeWarband_A01#Shaman` | `GiantBloodAxeMaleShaman.png`, `BloodAxeShamanHut.png`, `BloodAxeRitual.png` | Shaman/cult visual planning | `SK_GIA_BloodAxeShaman_A01` | Package ready | `docs/assets/characters/SK_GIA_BloodAxeShaman_A01/PRODUCTION_PACKAGE.md` is ready as planning only for ritual staff, ash, bone/horn accents, sockets, and restrained shamanic glow language. Hut and ritual-stone structures route to camp or ritual packages. No spell behavior, aura rules, VFX graph, AI, or ability timing. |
| `KIT_GIA_BloodAxeWarband_A01#Hunters` | `Blood Axe Fist Hunting Party.png`, `GiantBloodAxeHuntersMale.png`, `GiantBloodAxeMaleandFemale.png` | Hunter and hunting-party silhouette planning | `KIT_GIA_BloodAxeHunters_A01` | Kit package ready | `docs/assets/kits/KIT_GIA_BloodAxeHunters_A01/PRODUCTION_PACKAGE.md` and child intake are ready as planning only for hunter role/loadout variants; a single `SK_GIA_BloodAxeHunter_A01` skeletal mesh package remains separate if later needed. No projectile behavior, patrol logic, aggro rules, combat stats, or animation timing. |
| `KIT_GIA_BloodAxeWarband_A01#Raiders` | `BloodAxeGiantMale.png`, `BloodAxeGiantMale2.png`, `GiantBloodAxeMale3.png`, `GiantBloodAxeMale4.png`, `GiantFemaleBloodAxe1.png`, `GiantBloodAxeMaleandFemale.png` | Common raider visual baseline planning | `SK_GIA_BloodAxeRaider_A01` | Package ready | `docs/assets/characters/SK_GIA_BloodAxeRaider_A01/PRODUCTION_PACKAGE.md` is ready as planning only for repeatable Blood Axe hostile Giant body/outfit language across male and female baselines. Do not treat as the final default troop role or select it as first build target. |
| `KIT_GIA_BloodAxeWarband_A01#ShieldCarriers` | `Bloodaxe Army.png`, `GiantBloodAxeMale4.png`, `GiantBloodAxeMaleandFemale.png` | Shield-bearing silhouette planning | `SK_GIA_BloodAxeShieldCarrier_A01` | Package ready | `docs/assets/characters/SK_GIA_BloodAxeShieldCarrier_A01/PRODUCTION_PACKAGE.md` is ready as planning only for broad front-facing shield mass, braced stance, and heavy shoulder read. Shield mesh, blocking behavior, hit volumes, stamina rules, and encounter role are out of scope. |
| `KIT_GIA_BloodAxeWarband_A01#BannerBearers` | `Bloodaxe Army.png`, `Blood Axe Fist Hunting Party.png`, `BloodAxeArmory.png#Banner_WarCamp` | Banner carrier silhouette planning | `SK_GIA_BloodAxeBannerBearer_A01` | Package ready | `docs/assets/characters/SK_GIA_BloodAxeBannerBearer_A01/PRODUCTION_PACKAGE.md` is ready as planning only for carried red banner height, pole grip, harness clearance, and formation readability. Reuse `SM_GIA_BloodAxeWarBanner_A01` planning later. No cloth simulation, faction aura, capture mechanic, buffs, debuffs, or AI behavior. |
| `KIT_GIA_BloodAxeWarband_A01#ForgeGuards` | `BloodAxeForge.png`, `BloodAxeArmory.png`, `BloodAxeCamp.png` | Forge-adjacent guard visual planning | `SK_GIA_BloodAxeForgeGuard_A01` | Package ready | `docs/assets/characters/SK_GIA_BloodAxeForgeGuard_A01/PRODUCTION_PACKAGE.md` is ready as planning only for soot-dark armor, scorched leather, heavy tools, hammer/cleaver carry language, and forge-camp guard read. Forge modules, crafting, workstation, economy, salvage, and heat gameplay are out of scope. |
| `KIT_GIA_BloodAxeWarband_A01#TrophyCarriers` | `BloodAxeChieftan.png`, `Bloodaxe Army.png`, `BloodAxeArmory.png#Armor_TrophyHelmFaceGuard`, `BloodAxeArmory.png#Armor_TrophyBeltTassets` | Trophy carrier and intimidation silhouette planning | `SK_GIA_BloodAxeTrophyCarrier_A01` | Package ready | `docs/assets/characters/SK_GIA_BloodAxeTrophyCarrier_A01/PRODUCTION_PACKAGE.md` is ready as planning only for restrained trophy racks, belts, back loads, and camp intimidation read. Keep gore implied and non-graphic. No loot rules, dismemberment, inventory behavior, or trophy collection mechanics. |
| `KIT_GIA_BloodAxeWarband_A01#CampSentries` | `BloodAxeGate.png`, `BloodAxeCamp.png`, `BloodAxecamp.png`, `GiantBloodAxeHuntersMale.png` | Camp perimeter sentry visual planning | `SK_GIA_BloodAxeCampSentry_A01` | Package ready | `docs/assets/characters/SK_GIA_BloodAxeCampSentry_A01/PRODUCTION_PACKAGE.md` is ready as planning only for gate-watch posture, spear/bow read, lighter camp kit, and perimeter silhouette. Gate/camp props route to `KIT_GIA_BloodAxeCamp_A01`. No patrol paths, AI perception, aggro radii, encounter scripting, or spawn rules. |
| `KIT_GIA_BloodAxeWarband_A01#FormationDressing` | `Bloodaxe Army.png`, `Blood Axe Fist Hunting Party.png`, `BloodAxeStronghold.png`, `BloodAxeCamp.png` | Non-gameplay formation and composition dressing | `KIT_GIA_BloodAxeFormationDressing_A01` | Package ready | `docs/assets/kits/KIT_GIA_BloodAxeFormationDressing_A01/PRODUCTION_PACKAGE.md` and child intake are ready as planning only for grouped silhouettes, spacing references, banner/weapon height reads, and review-scene composition. This is not encounter design and does not define waves, ranks, combat roles, AI groups, nav behavior, or first implementation target. |

## Dependency Notes

- `SK_GIA_Base_A01` provides scale, skeleton policy, capsule expectations, sockets, and body proportions.
- `KIT_GIA_BloodAxeArmory_A01` and its child packages provide weapon, bow, quiver, banner, armor, trophy, and material planning dependencies.
- `KIT_GIA_BloodAxeCamp_A01` and `KIT_GIA_BloodAxeCampShelters_A01` provide camp and shelter planning dependencies; `KIT_GIA_BloodAxeRitualStones_A01` and stronghold/gate packages remain separate future environment work.
- `GiantFemaleShaman.png` remains routed to neutral/civilized Giant body/style unless a later culture decision explicitly assigns a Blood Axe variant.
- No row in this table is approved as the first DCC, Unreal, runtime, or gameplay target.

## Approval Gates

- Lead approval is required before selecting any first Blood Axe warband child package or build target.
- Visual approval is required before final chieftain, shaman, hunter, raider, shield carrier, banner bearer, forge guard, trophy carrier, camp sentry, or formation dressing silhouettes are locked.
- DCC approval is required before creating source folders, Blender files, proof renders, LOD sources, collision proxies, or FBX exports.
- Unreal approval is required before importing meshes, materials, textures, Blueprints, validators, or startup actors.
- Gameplay approval is required before defining final troop roles, AI, combat stats, abilities, projectile rules, shield behavior, aura effects, spawn rules, patrol paths, loot, crafting, economy, interaction, or encounter composition.
- Animation approval is required before authoring bow draw timing, melee swings, shield brace, banner motion, shaman casting, cloth, physics, or montage timing.
- Source-storage approval is required before any external concept image enters the repository.
- Culture approval is required if Blood Axe visual language starts replacing neutral/civilized Giant culture.

## Quality Gate Checklist

- Child rows are planning-only and do not define final gameplay troop roles.
- Chieftain, shaman, hunters, raiders, shield carriers, banner bearers, forge guards, trophy carriers, camp sentries, and formation dressing are all split.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Blood Axe remains a hostile Giant sub-faction, not default Giant culture.
- Warband composition stays visual/production planning, not gameplay encounter design.
- No source concept files are copied, moved, edited, embedded, or committed.
- No DCC, FBX, Unreal Content, runtime source, validators, startup placements, global indexes, task-board changes, AI, combat stats, abilities, loot, crafting, economy, patrol logic, spawn logic, or first build target is claimed.
