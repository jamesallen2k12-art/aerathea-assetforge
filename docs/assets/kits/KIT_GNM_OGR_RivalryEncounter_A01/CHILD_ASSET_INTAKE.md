# KIT_GNM_OGR_RivalryEncounter_A01 Child Asset Intake

## Intake Summary

This intake routes the 2026-06-27 Gnome-vs-Ogre source concepts into reusable production children. The images should be treated as encounter references first, not as final one-to-one dioramas. The strongest first production target is `BP_GNM_HeavyMekShieldwall_A01`, because it validates Mek scale, blue Aetherium shield language, Ogre pressure readability, and future combat staging.

## Source Inventory

| Source concept | Child routing |
| --- | --- |
| `Gnome Vs Ogre.png` | Core encounter staging for `KIT_GNM_OGR_RivalryEncounter_A01` |
| `GnomevsOgre.png` | Core encounter staging and shield-wall composition |
| `GnomevsOgre1.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre2.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre3.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre4.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre5.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre6.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre7.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre9.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre10.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre11.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre12.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre13.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre14.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre15.png` | Gnome Mek versus Ogre pressure variant |
| `GnomevsOgre16.png` | Gnome Mek versus Ogre pressure variant |
| `GnomeFemalevsOgre11.png` | Female gnome heavy Mek pilot and shield pose reference |
| `GnomeFemalevsOgre14.png` | Female gnome heavy Mek pilot and shield/cannon reference |
| `GnomeFemalevsOgre15.png` | Female gnome heavy Mek pilot and battle stance reference |
| `GnomeFemaleHeavyMek.png` | Heavy Mek variant matrix; route also to `KIT_GNM_IonaSiegebreaker_A01` |
| `GnomeFemaleHeavyMek0.png` | Heavy Mek variant matrix; route also to `KIT_GNM_IonaSiegebreaker_A01` |
| `GnomeFemaleHeavyMek8.png` | Heavy Mek variant matrix; route also to `KIT_GNM_IonaSiegebreaker_A01` |
| `GnomeFemaleHeavyMek10.png` | Heavy Mek variant matrix; route also to `KIT_GNM_IonaSiegebreaker_A01` |
| `GnomevsOgreandManticore8.png` | Optional Manticore interrupt variant after base rivalry kit approval |

## Proposed Child Assets

| Child asset | Type | Source support | Status | Notes |
| --- | --- | --- | --- | --- |
| `BP_GNM_HeavyMekShieldwall_A01` | Blueprint Actor/VFX | `GnomevsOgre*.png`, `GnomeFemalevsOgre*.png` | First-pass DCC/Unreal review complete | Creates reusable shield-wall field using Mek projectors and blue Aetherium arcs |
| `SK_GNM_HeavyMek_Rivalry_A01` | Skeletal Mesh | `GnomeFemaleHeavyMek*.png`, encounter sheets | First-pass DCC/Unreal review import complete | Shared heavy Mek variant for encounter staging; generic rivalry Mek, not the named Iona hero Mek |
| `SM_GNM_AetherShieldProjector_A01` | Static Mesh | shield-wall images | First-pass DCC/Unreal review complete | Ground or Mek-mounted projector prop with socketed VFX |
| `VFX_GNM_AetherShieldWall_A01` | Niagara/VFX | shield-wall images | First-pass placeholder VFX complete | Blue shield arc, pulse, impact ripple, and failure state |
| `SK_OGR_Teknomancer_A01` | Skeletal Mesh | `OgreTekvsGnomeMek.png`, encounter sheets | First-pass DCC/Unreal review import complete | Ogre class opponent with crude oversized Teknomancy hardware |
| `SK_OGR_Warrior_Rival_A01` | Skeletal Mesh | encounter sheets | First-pass DCC/Unreal review import complete | Brutal melee pressure unit using simple heavy weapons |
| `SM_OGR_CairnBattleGate_A01` | Static Mesh kit | gate and battlefield framing in encounter sheets | First-pass DCC/Unreal review import complete | Ogre cairn gate/wall dressing scaled for 10-11 ft Ogres |
| `SM_OGR_CrudeTekPylon_A01` | Static Mesh/VFX hook | Ogre Teknomancer pressure references | Package needed | Large unstable power pylon or coil for encounter objectives |
| `BP_GNM_OGR_BattlefieldEncounter_A01` | Blueprint Actor | full source group | Blocked | Assembly Blueprint after first Mek, Ogre, shield, and gate children exist |
| `SK_CRE_Manticore_Interrupt_A01` | Creature variant reference | `GnomevsOgreandManticore8.png` | Planning package ready | Do not build until base `SK_CRE_Manticore_A01` direction, skeleton, and proportions are approved |

## First Child Recommendation

Start with `BP_GNM_HeavyMekShieldwall_A01` as a controlled technical concept package:

- It can be built from one Mek projector mesh plus VFX, without requiring a full animated Mek body first.
- It creates a clear visual contrast against Ogre forward pressure.
- It gives Gnome/Mekgineer gameplay a reusable defensive identity.
- It can later attach to Iona-style heavy Mek sockets or standalone field projectors.

## Dependency Notes

- `KIT_GNM_IonaSiegebreaker_A01` should own named hero-pilot and hero heavy Mek decisions.
- `SK_OGR_Base_A01` should own Ogre base body proportions before final `SK_OGR_Teknomancer_A01` sculpt.
- `SM_OGR_CairnBattleGate_A01` provides the first imported Ogre gate review module; `KIT_OGR_CairnFortifications_A01` should own expanded reusable wall, tower, and gate variants when that package is created.
- `SK_CRE_Manticore_A01` must exist before the Manticore interrupt is more than a reference.

## Quality Gate Checklist

- Every new source image has a routing target.
- The first child can be built without blocking on full encounter AI.
- Gnome, Ogre, and optional Manticore responsibilities remain separated.
- Scale, sockets, VFX hooks, collision expectations, and package dependencies are clear.
