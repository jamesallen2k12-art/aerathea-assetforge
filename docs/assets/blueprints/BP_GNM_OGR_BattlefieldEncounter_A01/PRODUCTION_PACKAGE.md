# BP_GNM_OGR_BattlefieldEncounter_A01 Production Package

## 1. Art Direction Summary

- Asset name: `BP_GNM_OGR_BattlefieldEncounter_A01`
- Asset type: Blueprint Actor / encounter coordinator
- Parent kit: `KIT_GNM_OGR_RivalryEncounter_A01`
- World: Aerathea
- Theme: Gnome Heavy Mek shield line versus Ogre warband pressure
- Current status: native-backed coordinator implemented; Blueprint asset created and compiled; startup placement deferred until all optional branch imports can be assigned cleanly

`BP_GNM_OGR_BattlefieldEncounter_A01` coordinates the reusable Gnome/Ogre rivalry scene. It should not become a monolithic art asset. Its job is to place, reference, configure, and sequence existing child actors: Gnome Heavy Mek, Heavy Mek shieldwall, Ogre Teknomancer, Ogre Warrior, Cairn Battle Gate, crude Tek pylon objective, optional Ogre caster variants, and optional Manticore interrupt.

The encounter must keep the faction reads separated: Gnome precision, brass/dark-iron hardware, and blue Aetherium shields versus Ogre mass, blackened iron, cairn fortification, forge-orange crude Teknomancy, and brutal forward pressure.

## 2. Gameplay Purpose

- Provides a reusable encounter coordinator for review scenes, quests, events, dungeon pulls, and future combat prototypes.
- Establishes actor slots, dependency validation, phase sequencing, and VFX/audio hooks for the Gnome/Ogre rivalry.
- Allows imported first-pass assets to be reviewed together without hard-coding every child into the level.
- Supports optional branches for crude Tek pylon objective, Ogre Shaman/Necromancer reinforcement, and Manticore interrupt after those assets are approved/imported.
- Creates a single production handoff for designers and programmers before gameplay combat rules are final.

## 3. Silhouette Notes

The Blueprint itself has no authored mesh silhouette. It preserves scene readability by controlling actor placement:

- Gnome Heavy Mek and shieldwall should occupy the defensive line.
- Ogre Warrior and Teknomancer should pressure from the opposing side.
- Cairn Battle Gate should frame the Ogre side without blocking combat silhouettes.
- Crude Tek pylon should sit behind or beside Ogre pressure as a readable objective, not in front of primary characters.
- Optional Manticore interrupt should enter from background/flank and never replace the Gnome/Ogre identity.

## 4. Scale Notes

- Encounter footprint target: 2200-3600 cm wide by 1600-2800 cm deep for a compact review scene.
- Root pivot: center of the encounter footprint.
- Gnome Heavy Mek and shieldwall line: near/front side of the root.
- Ogre pressure line: opposite side, with 10-11 ft Ogre clearance.
- Gate/background prop clearance: keep at least 400 cm behind active Ogre actors.
- Optional Manticore lane: side or rear entry path with enough room for a 900-1100 cm wingspan once imported.

## 5. Materials And Color Palette

The Blueprint does not define new material art. It enforces dependency palette separation:

| Faction/element | Palette rule |
| --- | --- |
| Gnome/Mekgineer | Brass, copper, dark iron, leather, blue Aetherium |
| Gnome shieldwall | Blue, cyan, blue-white shield states |
| Ogre Teknomancy | Blackened iron, crude brass, scorched leather, forge orange, restrained blue-white anti-Mek arcs |
| Ogre fortification | Blue-gray cairn stone, blackened iron, bone, red banners, forge-orange accents |
| Ogre Shaman | Hide, fur, cairn stone, bone, ember orange, storm white |
| Ogre Necromancer | Black cloth, bone, tomb metal, grave green, black-green |
| Manticore | Tawny hide, dark mane, leathery wings, dark chitin, muted venom |

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG encounter Blueprint sheet of `BP_GNM_OGR_BattlefieldEncounter_A01` for the world of Aerathea. The design should emphasize a staged Gnome Heavy Mek shield line with compact blue Aetherium shieldwall projectors, a broad Ogre Teknomancer and Ogre Warrior advancing from cairn fortifications, a crude forge-orange Tek pylon objective behind the Ogre line, optional Ogre Shaman and Necromancer reinforcement slots, optional Manticore interrupt lane, clear top-down encounter layout, readable faction color separation, production-safe collision zones, and MMO-friendly VFX timing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and production-friendly design. Present it as a clean Blueprint encounter board with top-down layout, front scale lineup, actor slots, phase diagram, VFX socket links, dependency table, and collision/trigger volumes. Avoid copied franchise designs, excessive particles, unreadable battlefield clutter, text-heavy UI, photoreal micro-detail, and watermarks.

## 7. Modeling Notes

- No new mesh is required for the Blueprint actor.
- Use child meshes and skeletal actors as placed components, child actor components, soft references, or spawn classes.
- Add simple editor-only marker meshes or billboards only if useful for layout; keep them hidden in runtime review.
- Do not create crude placeholder fantasy art to stand in for missing children.
- Missing dependencies should remain disabled slots until their production assets exist.

## 8. Texture And Material Notes

No new texture set is required.

Runtime material/VFX control should forward parameters to child actors:

- Shieldwall: `ShieldState`, `ImpactIntensity`, `OverloadPercent`, `ImpactLocationNormalized`, state materials.
- Crude Tek pylon: future `PylonState`, `CoreIntensity`, `OverloadPercent`, `bAntiMekDischarge`.
- Ogre casters: future shamanic or necromantic cast VFX intensity only after class actors exist.
- Manticore: future venom/arrival VFX only after creature import.

## 9. Triangle Budget

Blueprint adds no unique triangle budget. It must keep aggregate scene cost reviewable:

- Startup/review slice should use the currently imported first-pass actors and keep optional package-only actors disabled.
- Do not spawn every optional branch at once.
- Use HLOD or manual review layout later if the encounter becomes a full battlefield set piece.

## 10. LOD Plan

- Child actors keep their own LOD plans.
- Blueprint should expose per-branch enable toggles so distant/review modes can disable optional casters, pylon VFX, Manticore interrupt, and extra set dressing.
- VFX should reduce ripple, spark, smoke, and arc density before removing primary faction reads.

## 11. Collision Notes

Blueprint collision components:

- `EncounterBounds`: non-blocking BoxComponent for editor review and activation area.
- `GnomeLineTrigger`: optional phase trigger.
- `OgreAdvanceTrigger`: optional phase trigger.
- `PylonObjectiveVolume`: disabled until pylon gameplay is implemented.
- `ManticoreInterruptVolume`: disabled until Manticore import and encounter rules are approved.

Do not use the Blueprint root as blocking collision. Child actors keep their own collision.

## 12. Animation Notes

Blueprint phase plan:

1. `Setup`: validate dependencies, place actors, idle VFX.
2. `GnomeHoldLine`: shieldwall active, Mek braced.
3. `OgreAdvance`: Ogre Warrior/Teknomancer pressure line active.
4. `ShieldImpact`: shieldwall impact material/VFX event.
5. `PylonOverload`: optional crude Tek pylon charge/discharge event.
6. `CasterReinforcement`: optional Shaman/Necromancer slot activation.
7. `ManticoreInterrupt`: optional creature interrupt after base/interrupt assets are approved/imported.
8. `Resolution`: shutdown, retreat, or reset state for review.

Use short, inspectable Blueprint events first. Do not script final combat AI in this package.

## 13. Unreal Import Notes

- Blueprint path: `/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_OGR_BattlefieldEncounter_A01`
- Native class: `AAETGnomeOgreBattlefieldEncounterActor`.
- Root component: `DefaultSceneRoot` or custom `SceneComponent`.
- Editor label if placed: `AET_PROD_GNM_OGR_BattlefieldEncounter_A01`.
- Map target: optional placement in `/Game/Aerathea/Maps/L_Aerathea_Startup` only after dependency review.

Required child/dependency slots:

- `ShieldwallActor`: `BP_GNM_HeavyMekShieldwall_A01`
- `GnomeHeavyMekActor`: `SK_GNM_HeavyMek_Rivalry_A01` actor or future class wrapper
- `OgreTeknomancerActor`: `SK_OGR_Teknomancer_A01` actor or future class wrapper
- `OgreWarriorActor`: `SK_OGR_Warrior_Rival_A01` actor or future class wrapper
- `CairnGateActor`: `SM_OGR_CairnBattleGate_A01` actor
- `CrudeTekPylonActor`: future `SM_OGR_CrudeTekPylon_A01` or `BP_OGR_CrudeTekPylon_A01`
- `OgreShamanActor`: future `SK_OGR_Shaman_A01`
- `OgreNecromancerActor`: future `SK_OGR_Necromancer_A01`
- `ManticoreInterruptActor`: future `SK_CRE_Manticore_Interrupt_A01` or creature Blueprint

Editor-exposed variables:

- `EncounterState`
- `bAutoStart`
- `bUsePlacedActors`
- `bEnablePylonObjective`
- `bEnableCasterReinforcements`
- `bEnableManticoreInterrupt`
- `bLoopForReview`
- `EncounterWidthCm`
- `EncounterDepthCm`
- `ShieldImpactLocationNormalized`
- `PylonOverloadPercent`

Blueprint functions/events:

- `ValidateDependencies`
- `ConfigureEncounter`
- `SetEncounterState`
- `TriggerShieldImpact`
- `TriggerPylonOverload`
- `TriggerCasterReinforcement`
- `TriggerManticoreInterrupt`
- `ResetEncounter`
- `OnEncounterPhaseChanged`

## 14. Folder And Naming Recommendation

- Docs: `docs/assets/blueprints/BP_GNM_OGR_BattlefieldEncounter_A01/`
- Implementation handoff: `docs/assets/blueprints/BP_GNM_OGR_BattlefieldEncounter_A01/IMPLEMENTATION_HANDOFF.md`
- Build/import status: `docs/assets/blueprints/BP_GNM_OGR_BattlefieldEncounter_A01/BUILD_IMPORT_STATUS.md`
- Unreal Blueprint: `/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_OGR_BattlefieldEncounter_A01`
- Native class files:
  - `Source/Aerathea/Public/AETGnomeOgreBattlefieldEncounterActor.h`
  - `Source/Aerathea/Private/AETGnomeOgreBattlefieldEncounterActor.cpp`
- Blueprint creation script: `Tools/Unreal/create_gnome_ogre_encounter_blueprint.py`

## 15. Quality Gate Checklist

- Encounter remains a coordinator, not a monolithic art asset.
- Gnome and Ogre visual languages remain separated.
- Optional package-only dependencies are soft-gated until imported.
- Actor slots, phase states, variables, events, collision volumes, and Unreal paths are defined.
- Shieldwall, pylon, caster, and Manticore branches have explicit dependency gates.
- No final combat AI, quest logic, loot, or travel rules are hard-coded in this package.
- Useful for production assembly without forcing placeholder art.
