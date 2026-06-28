# KIT_GNM_OGR_RivalryEncounter_A01 Production Package

## Art Direction Summary

`KIT_GNM_OGR_RivalryEncounter_A01` is the encounter kit for Gnome/Mekgineer heavy Mek forces clashing with Ogre warbands and Teknomancers. The new source concepts show a repeatable battlefield language: small brilliant pilots inside oversized brass-and-dark-iron Mek suits, blue Aetherium shield and cannon effects, huge broad Ogres pressing forward with crude oversized weapons, and stone cairn or gate fortifications framing the fight.

The kit should make the rivalry readable immediately. Gnomes win by precision, layered machinery, shield geometry, and tactical range. Ogres win by mass, instinctive Teknomancy, brutal armor, and overwhelming forward pressure. Neither side should look like a copied franchise army.

## Gameplay Purpose

- Battlefield encounter staging for Gnome Mekgineer versus Ogre raids.
- Prototype package for a heavy Mek shield-wall and Ogre Teknomancer counterplay.
- Visual bridge between `KIT_GNM_IonaSiegebreaker_A01`, `SK_OGR_Base_A01`, and future Ogre class packages.
- Reusable source for quest scenes, zone events, dungeon pulls, and world-object set dressing.
- Cross-race scale validation: 3'0"-4'0" gnomes, large Mek frames, and 10'0"-11'0" Ogres.

## Silhouette Notes

- Gnome heavy Meks should read as compact pilots surrounded by thick mechanical limbs, high shoulder armor, squat reactor packs, blue shield vanes, cannon barrels, and tool-like weapon assemblies.
- Ogre warriors should read as taller than the Mek pilot and physically broad, with heavy shoulders, thick necks, large hands, brutal melee profiles, and crude armor plates.
- Ogre Teknomancers should look less precise than gnomes but dangerous: oversized coils, scavenged engines, stone-metal power frames, unstable forge-orange or sickly green energy, and reinforced gauntlets.
- The encounter composition should stage Gnome shield arcs against Ogre forward momentum.
- The Manticore interrupt source is a variant hook only; it must not become the core encounter identity.

## Scale Notes

- Female Gnomes: 91-107 cm. Male Gnomes: 102-122 cm.
- Heavy Mek frames: 240-420 cm depending on role. Keep the visible pilot scale clear through cockpit, hatch, or seat silhouette.
- Female Ogres: 305-320 cm. Male Ogres: 315-335 cm.
- Siege gate/cairn structures should be built for Ogre clearance while still letting Mek cannons read at gameplay camera distance.

## Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Gnome brass/copper | warm brass, copper, edge-worn gold | Mek armor plates, pistons, cockpit rings |
| Gnome dark iron | charcoal, dark blue-gray, blackened edges | joint housings, cannon frames, shield braces |
| Aetherium | blue, blue-white, cyan highlights | shields, reactor cores, cannon charge, sensor lenses |
| Ogre stone/iron | cairn gray, black iron, rust, hammer-burnished steel | armor plates, fortification blocks, crude weapons |
| Ogre Teknomancy | forge orange, muted red, unstable green accents | large weapon cores, rough engines, ritualized tech parts |
| Battlefield ground | packed dirt, broken stone, ash, dust | neutral read between both factions |

## Source Concept Routing

| Source group | Routed use |
| --- | --- |
| `GnomevsOgre*.png`, `Gnome Vs Ogre.png` | Core encounter staging, Mek shield versus Ogre melee pressure, battlefield camera composition |
| `GnomeFemalevsOgre*.png` | Female gnome heavy Mek pilot variants and shield/cannon pose language |
| `GnomeFemaleHeavyMek*.png` | Heavy Mek variant matrix shared with `KIT_GNM_IonaSiegebreaker_A01` |
| `GnomevsOgreandManticore8.png` | Optional creature interrupt scenario after the base rivalry kit is stable |

## Concept Image Prompt

Create an original stylized fantasy MMORPG encounter kit board of Gnome/Mekgineer heavy Meks battling Ogre warriors and Teknomancers for the world of Aerathea. The design should emphasize tiny brilliant gnome pilots inside oversized brass, copper, dark-iron, and blue-Aetherium Mek suits; broad heavily muscled Ogres with crude oversized armor, brutal weapons, instinctive Teknomancy engines, and stone cairn battlefield fortifications; blue shield-wall arcs against Ogre forward pressure; readable height contrast between gnomes, Mek frames, and 10-11 ft Ogres; dust, stone, cannon glow, and restrained MMO-friendly effects. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and production-friendly geometry. Present it as a clean encounter production sheet with top-down staging, front-view scale lineup, child asset callouts, material swatches, and VFX state notes. Avoid copied franchise designs, excessive particles, unreadable clutter, photoreal micro-detail, text, and watermarks.

## Modeling Notes

- Build this as a kit of reusable child assets rather than a single diorama.
- Heavy Mek parts should use large readable mechanical forms: legs, gauntlets, shield vanes, shoulder reactors, cockpit rings, and cannons.
- Fake tiny rivets, scratches, cloth, soot, and micro-gears in texture and normal maps.
- Ogre Teknomancy hardware should be larger, rougher, and less elegant than gnome machinery.
- Build cairn walls and gates as modular stone blocks with broad bevels and simple snap dimensions.
- Keep VFX emitters and shield arcs as Blueprint/VFX children, not embedded into static mesh geometry.

## Texture And Material Notes

Texture set families:

- `T_GNM_HeavyMek_A01_BC`
- `T_GNM_HeavyMek_A01_N`
- `T_GNM_HeavyMek_A01_ORM`
- `T_GNM_HeavyMek_A01_E`
- `T_OGR_CrudeTek_A01_BC`
- `T_OGR_CrudeTek_A01_N`
- `T_OGR_CrudeTek_A01_ORM`
- `T_OGR_CairnStone_A01_BC`
- `T_OGR_CairnStone_A01_N`
- `T_OGR_CairnStone_A01_ORM`
- `T_GNM_AetherShield_A01_E`

Use 2K texture sets for common characters and props. Use 4K only for a named hero Mek, named Ogre champion, or cinematic boss. Pack ORM maps and keep emissive masks focused on Aetherium cores, shield rims, Teknomancy coils, eyes, lamps, or weapon charge points.

## Triangle Budget

- Heavy Mek skeletal hero frame: 35k-70k tris, 3-5 materials.
- Heavy Mek common encounter variant: 28k-45k tris, 3-4 materials.
- Ogre warrior or Teknomancer character: 28k-50k tris, 3-4 materials.
- Cairn gate module: 12k-22k tris, 2-3 materials.
- Shield projector prop: 3k-8k tris, 1-2 materials.
- Full encounter review cluster: keep under 120k visible LOD0 tris before characters animate in gameplay.

## LOD Plan

- LOD0: full silhouettes, cockpit, major limbs, shields, Ogre armor mass, cairn wall breaks, weapon profiles, sockets.
- LOD1: 55-60 percent; reduce bevels, small pipes, secondary straps, minor stone chips, small engine decorations.
- LOD2: 25-35 percent; merge simple plates, remove small brace pieces, flatten minor grooves, simplify shield projector hardware.
- LOD3: 10-15 percent; preserve Mek mass, blue shield read, Ogre body mass, broad weapons, gate silhouette, and faction colors.

## Collision Notes

- Mek and Ogre characters use skeletal mesh capsules plus simplified physics bodies.
- Cairn wall and gate modules use simple box or convex blocking collision.
- Shield VFX uses gameplay volumes or Blueprint collision only where mechanics require it.
- Loose debris, cables, banners, sparks, and small stones are non-blocking dressing.

## Animation Notes

- Gnome heavy Mek: idle reactor hum, brace, shield deploy, cannon charge, recoil, stomp, overheat, shutdown, pilot hatch gesture.
- Ogre warrior: charge, heavy swing, shield slam, stagger, roar, leap strike, death.
- Ogre Teknomancer: crude engine start, power overload, coil smash, unstable beam, repair-by-impact gesture.
- Encounter VFX: blue shield pulse, aether cannon windup, crude Teknomancy overload, stone dust impacts, restrained smoke.

## Unreal Import Notes

- Kit type: Mixed kit with Skeletal Mesh, Static Mesh, Blueprint Actor, Material, and VFX children.
- Root folder: `/Game/Aerathea/Kits/GnomeOgre/RivalryEncounter/`
- Gnome Mek folder: `/Game/Aerathea/Characters/Gnomes/Meks/`
- Ogre character folder: `/Game/Aerathea/Characters/Ogres/`
- Cairn props folder: `/Game/Aerathea/Props/Ogres/CairnFortifications/`
- VFX folder: `/Game/Aerathea/VFX/GnomeOgre/`
- Primary Blueprint candidates:
  - `BP_GNM_HeavyMekShieldwall_A01`
  - `BP_GNM_AetherShieldProjector_A01`
  - `BP_OGR_CrudeTekOverload_A01`
- Required sockets:
  - Mek: `vfx_reactor_core`, `vfx_shield_l`, `vfx_shield_r`, `weapon_cannon_muzzle`, `pilot_hatch`, `foot_l`, `foot_r`
  - Ogre Teknomancer: `vfx_tek_core`, `weapon_socket_r`, `hand_l`, `hand_r`, `back_pack`, `head_fx`

## Folder And Naming Recommendation

- Package folder: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/`
- Source DCC root: `SourceAssets/Blender/Kits/GnomeOgre/RivalryEncounter/`
- Export root: `SourceAssets/Exports/Kits/GnomeOgre/RivalryEncounter/`
- Unreal root: `/Game/Aerathea/Kits/GnomeOgre/RivalryEncounter/`
- Recommended first child:
  - `BP_GNM_HeavyMekShieldwall_A01`
  - Alternative: `SK_OGR_Teknomancer_A01` if the next priority is Ogre class validation.

## Implementation Status

- `BP_GNM_HeavyMekShieldwall_A01`, `SM_GNM_AetherShieldProjector_A01`, `SM_GNM_AetherShieldWall_A01`, and `VFX_GNM_AetherShieldWall_A01` have approved first-pass review implementations, a validated native Blueprint/VFX contract for state material switching, impact location, impact intensity, overload, a native Niagara component hook, and an empty Niagara target system. The final shieldwall Niagara emitter art pass is still pending.
- `SK_OGR_Teknomancer_A01` has a first-pass class-fit DCC/Unreal review import.
- `SK_GNM_HeavyMek_Rivalry_A01` has a first-pass DCC/Unreal review import with required Mek, weapon, pilot, and VFX sockets.
- `SK_OGR_Warrior_Rival_A01` has a first-pass DCC/Unreal review import with shield, hammer, belt, stomp, head, and weapon grip sockets.
- `SK_OGR_Shaman_A01` has a first-pass DCC/Unreal review import with shamanic material instances, sockets, physics asset, anim Blueprint, startup placement, validation, and build/import status.
- `SK_OGR_Necromancer_A01` has a first-pass DCC/Unreal review import with necromantic material instances, sockets, physics asset, anim Blueprint, startup placement, validation, and build/import status.
- `SM_OGR_CairnBattleGate_A01` has a first-pass DCC/Unreal review import with material instances, LOD0-LOD3, static mesh sockets, simple collision, startup review placement, validation, and offscreen capture coverage.
- `SM_OGR_CrudeTekPylon_A01` has a first-pass DCC/Unreal review import with material instances, LOD0-LOD3, static mesh sockets, simple collision, startup placement, validation, and build/import status.
- `SK_CRE_Manticore_A01` has a first-pass DCC/Unreal review import with skeleton, physics asset, anim Blueprint, material instances, sockets, startup placement, validation, and build/import status.
- `SK_CRE_Manticore_Interrupt_A01` has a first-pass DCC/Unreal review import as an encounter variant with material instances, physics asset, sockets, startup placement, validation, and build/import status.
- `BP_OGR_CrudeTekPylon_A01` and `BP_CRE_ManticoreInterrupt_A01` have native-backed wrapper Blueprints, startup review actors, state contracts, and coordinator wiring.
- `BP_GNM_OGR_BattlefieldEncounter_A01` has a native-backed coordinator class and compiled Blueprint asset with dependency validation, phase-state controls, actor slots, trigger volumes, optional-branch gates, shieldwall impact/pylon/caster/Manticore event hooks, startup placement, and assigned required/branch actor references.
- Final-art replacement dependency order is documented in `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/FINAL_ART_REPLACEMENT_PLAN.md`.
- Current approved sequence is complete through first-pass startup wiring. Next work should follow the final-art replacement plan: lock shared character foundations, replace class/vehicle blockouts, then tune static props, textures, collision, physics, animation, and final VFX.

## Quality Gate Checklist

- Gnome/Ogre scale contrast is readable at gameplay distance.
- Heavy Mek design is Gnome/Mekgineer and not generic steampunk armor.
- Ogre Teknomancy is bigger, cruder, and instinctive, not as refined as gnome engineering.
- Blue Aetherium shield language and Ogre crude-tech language remain visually separate.
- Manticore involvement is optional encounter variation, not the base kit identity.
- Mesh budgets, materials, collisions, LODs, sockets, VFX hooks, and Unreal paths are defined.
