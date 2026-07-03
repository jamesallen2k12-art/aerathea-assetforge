# Aerathea Approval Queue

This queue tracks decisions that must come from Flamestrike before the next DCC,
Unreal, or final-art implementation pass. Documentation and planning can continue
around these items, but the listed work should not move into build production
until the approval is explicit.

## Current Approval Status

All approval gates listed below were cleared by Flamestrike on 2026-06-28. The
approved production order is:

1. Finish the Gnome/Ogre encounter final-art foundation.
2. Complete the Ogre shared rig/art-model fit.
3. `SK_GNM_IonaSiegebreakerMek_A01` completed the first Iona child production lane as a validated first-pass DCC/Unreal review asset.
4. Infernal starter class review lanes are complete for `SK_INF_Mage_A01`, `SK_INF_Warrior_A01`, `SK_INF_Rogue_A01`, and `SK_INF_Hunter_A01`; `SM_INF_HornWingArch_A01` remains the validated first cult prop.
5. Rebuild/rescale `SK_GIA_Base_A01` to the Giant A04 baselines: female 442 cm, male 470 cm.
6. Explore and rebuild the universal portal around old, mysterious, awe-inspiring 10 m scale; traversal expansion can defer.
7. `SK_ABY_BlackPikeTrooper_A01` completed the first Abyss/Anathema child production lane as a validated first-pass DCC/Unreal review asset.
8. `SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual` is approved as the A01 Blood Axe cairn proof-of-concept game-ready static prop and placed in Unreal.

## Resolved Approval Gates

| Priority | Gate | Approved decision | Production effect | Source docs |
| ---: | --- | --- | --- | --- |
| 1 | Gnome/Ogre final-art foundation | Continue the existing final-art replacement plan before branching to unrelated DCC | Locks the encounter as the active foundation lane and keeps phase review, pylon, shieldwall, Manticore, Ogre, and Mek dependencies in order | `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/FINAL_ART_REPLACEMENT_PLAN.md` |
| 2 | Ogre shared rig/art-model fit | Complete the shared Ogre rig and final-art model fit after baseline validation | Keeps `SK_OGR_Base_A01`, Teknomancer, Warrior, Shaman, and Necromancer on a reusable male Ogre skeleton before final class art expands | `docs/assets/characters/SK_OGR_Base_A01/PRODUCTION_PACKAGE.md` |
| 3 | Iona Siegebreaker first child | Start with `SK_GNM_IonaSiegebreakerMek_A01`; first-pass DCC/Unreal review lane complete | Locks cockpit, harness, weapon sockets, pilot scale envelope, and encounter mass before pilot and cannon variants | `docs/assets/characters/SK_GNM_IonaSiegebreakerMek_A01/BUILD_IMPORT_STATUS.md` |
| 4 | Infernal starter class and cult child signoff | Approve all starter classes; first-pass DCC/Unreal review lanes complete for Mage, Warrior, Rogue, and Hunter; first cult prop `SM_INF_HornWingArch_A01`; approve VFX and animation handoffs | Clears Infernal class silhouettes, weaponless doctrine, cult threshold scale, spell intensity, and animation rules for final material, VFX, animation, and art-model production | `docs/assets/characters/INFERNAL_APPROVAL_QUEUE.md` |
| 5 | Giant base scale and body lock | Rebuild/rescale to female 442 cm and male 470 cm baselines | Locks Giant hand/body scale for Blood Axe armory, cave-town architecture, stairs, doors, sockets, and environment modules | `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md` |
| 6 | Portal gameplay rules and scale | Explore old, mysterious, awe-inspiring portal silhouettes and rebuild around a 1000 cm clear traversal opening; traversal registry expansion can defer | Keeps the portal race-neutral and epic-scale while preserving validated preview/overlap/cooldown behavior for the next build pass | `docs/assets/blueprints/BP_AET_Portal_A01/PRODUCTION_PACKAGE.md` |
| 7 | Abyss/Anathema first child | Start with `SK_ABY_BlackPikeTrooper_A01` | Established first Abyss scale, material language, weapon sockets, rig expectations, and troop variant boundaries with a validated first-pass DCC/Unreal review asset | `docs/assets/kits/KIT_ABY_ShadowFlame_A01/CHILD_ASSET_INTAKE.md` |
| 8 | Blood Axe cairn A01 proof-of-concept | Approve `SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual` brightened Test 2 as the A01 static prop direction | Locks the A1/Test2 bright visual match/readability lane for static environmental storytelling placement in Unreal; gameplay behavior, VFX/audio, destruction, quest markers, and combat remain out of scope | `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/TEST2_MANUAL_ASSET_STATUS.md`, `docs/assets/VISUAL_CANON_REGISTRY.md` |

## Abyss/Anathema Candidate List

Approved first child is `SK_ABY_BlackPikeTrooper_A01`, now validated in the startup scene. The remaining candidates stay available as later variants:

1. `SK_ABY_BlackPikeTrooper_A01` - standard polearm infantry.
2. `SK_ABY_CrescentReaver_A01` - agile melee elite.
3. `SK_ABY_VoidbowStalker_A01` - ranged void archer.
4. `SK_ABY_WardbreakerMage_A01` - anti-ward caster.
5. `SK_ABY_BulwarkDemon_A01` - shield-bearing elite.
6. `SK_ABY_WingedRavager_A01` - air assault demon.
7. `SK_ABY_RiftHound_A01` - beast or crawler pursuit unit.
8. `SK_ABY_SiegeBrute_A01` - large wall-breaker.
9. `SK_ABY_CinderLord_A01` - boss-class commander.
10. `SK_ANA_SiegeDrake_A01` - bound siege construct or drake.

## Active Approval Gates

| Priority | Gate | Required Flamestrike decision | Production effect | Source docs |
| ---: | --- | --- | --- | --- |
| - | None | No active global approval gate is open for the approved A01 Blood Axe cairn proof-of-concept static prop. | Additional Blood Axe cairn variants, gameplay behavior, VFX/audio, destruction, quest markers, combat use, and broader kit rollout still require separate approval if requested. | `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/TEST2_MANUAL_ASSET_STATUS.md` |

Package-specific future Infernal visual gates are separated in `docs/assets/characters/INFERNAL_APPROVAL_QUEUE.md`. New approval gates should be added here only when a later package needs a fresh visual, gameplay, backend, economy, audio, or implementation decision from Flamestrike.
