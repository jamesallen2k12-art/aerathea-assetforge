# Infernal Approval Queue

## Purpose

This queue identifies the Infernal packages that are ready for Flamestrike approval before any DCC build, Unreal import, authored VFX, or animation production starts.

Planning and documentation can continue, but build production should wait for explicit approval of the package direction.

## Approval Gates

| Gate | Required approval | Recommended default | Why this helps production |
| --- | --- | --- | --- |
| Starter class direction | Approve the first four class packages or request changes | Approve `SK_INF_Mage_A01`, `SK_INF_Warrior_A01`, `SK_INF_Rogue_A01`, and `SK_INF_Hunter_A01` as the starter class set | Locks class silhouettes and prevents weapon-dependent drift before DCC fit work |
| First class DCC child | Choose the first class to model | Start with `SK_INF_Mage_A01` | Uses the approved A03 sorcerer references and validates brand, hand, eye, wing, and combat VFX sockets |
| First cult prop DCC child | Choose the next cult prop after the accepted culling floor | Start with `SM_INF_HornWingArch_A01` | Validates gate/threshold scale, cult architecture language, and snap alignment with `SM_INF_CullingTrialFloor_A01` |
| Combat VFX direction | Approve the new combat spellcasting VFX package or request intensity changes | Approve `VFX_INF_AbyssalSpellcasting_A01` | Gives Mage, Hunter, Rogue, and base body states shared rules for flame, lightning-like arcs, eye glow, regeneration, and rage without noisy screen clutter |
| Animation direction | Approve the base animation handoff | Approve `ANIMATION_HANDOFF.md` | Locks claw, wing, tail, rage, regeneration, and invisible-sight motion rules before animation authoring |

## Ready Reply Format

To clear the Infernal lane, reply with:

`Infernal starter classes approved; first DCC: Mage; first cult prop: HornWingArch; VFX approved; animation approved`

If changes are needed, specify the package and change, for example:

`Infernal Hunter: make tracking marks stronger; Rogue: less cloth; first DCC still Mage`

## Current Package Links

- `docs/assets/characters/SK_INF_Mage_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Warrior_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Rogue_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Hunter_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/INFERNAL_STARTER_CLASS_MATRIX.md`
- `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`
- `docs/assets/props/SM_INF_HornWingArch_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/PRODUCTION_PACKAGE.md`
