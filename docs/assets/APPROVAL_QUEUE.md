# Aerathea Approval Queue

This queue tracks decisions that must come from Flamestrike before the next DCC,
Unreal, or final-art implementation pass. Documentation and planning can continue
around these items, but the listed work should not move into build production
until the approval is explicit.

## Active Approval Gates

| Priority | Gate | Required approval | Recommended default | Why this default helps production | Source docs |
| ---: | --- | --- | --- | --- | --- |
| 1 | Abyss/Anathema first child | Choose one of the first ten proposed Abyss/Anathema child packages to move from concept direction to approved DCC modeling | `SK_ABY_BlackPikeTrooper_A01` | Standard infantry establishes the first Abyss scale, shared material language, weapon sockets, rig expectations, and troop variants before expensive elite, winged, siege, or boss work | `docs/assets/kits/KIT_ABY_ShadowFlame_A01/CHILD_ASSET_INTAKE.md` |
| 2 | Iona Siegebreaker first child | Choose whether Iona's heavy Mek, pilot, or arc cannons become the first child production package | `SK_GNM_IonaSiegebreakerMek_A01` | The child intake already identifies the heavy Mek as the first build if approved; it locks the cockpit, harness, weapon sockets, pilot scale envelope, and encounter mass | `docs/assets/kits/KIT_GNM_IonaSiegebreaker_A01/CHILD_ASSET_INTAKE.md` |
| 3 | Giant base scale and body lock | Approve rebuilding/rescaling the staged Giant base to the current A04 scale baselines, or request proportion changes before Blood Axe and Giant environment work | Rebuild/rescale to female 442 cm and male 470 cm baselines | Giant weapons, Blood Axe armory, doors, stairs, cave-town interiors, and hand/body sockets depend on this lock; the current import is documented as review-only | `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md` |
| 4 | Portal gameplay rules and scale | Approve final traversal, destination, VFX, audio, failure-state rules, multi-direction visual exploration, and the 10 m / about 33 ft universal portal scale for `BP_AET_Portal_A01` | Explore several old, mysterious, awe-inspiring portal silhouettes, rebuild/rescale the chosen arch to a 1000 cm clear traversal opening, keep preview/overlap/cooldown behavior, then add a single startup-test destination registry before expanding | The native portal actor and Blueprint are already validating; the portal should remain race-neutral and epic-scale so players feel small while Giants, major NPCs, large enemies, dungeons, raids, and cities are supported | `docs/assets/blueprints/BP_AET_Portal_A01/PRODUCTION_PACKAGE.md` |
| 5 | Infernal starter class and cult child signoff | Approve starter class packages, first class DCC child, first cult prop child, combat VFX direction, and animation direction before Infernal DCC production starts | Approve all four starter classes; first DCC `SK_INF_Mage_A01`; first cult prop `SM_INF_HornWingArch_A01`; approve VFX and animation handoffs | The docs are ready, but DCC work should not begin until class silhouettes, weaponless doctrine, cult threshold scale, spell intensity, and animation rules are approved together | `docs/assets/characters/INFERNAL_APPROVAL_QUEUE.md` |

## Abyss/Anathema Candidate List

Choose one before DCC modeling starts:

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

## Ready Reply Format

To clear all current approval gates, reply with decisions like:

`Abyss: BlackPikeTrooper; Iona: SiegebreakerMek; Giant: rebuild at 442/470 cm; Portal: explore old/mysterious 10 m universal scale, traversal defer`

The portal decision can be deferred without blocking creature, Mek, Giant, or
Infernal package approval. Abyss, Iona, Giant, and Infernal decisions each
unblock separate production lanes.
