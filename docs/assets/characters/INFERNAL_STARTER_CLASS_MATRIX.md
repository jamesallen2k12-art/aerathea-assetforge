# Infernal Starter Class Matrix

## Purpose

This matrix ties the first four Infernal starter class packages to the approved adult body bands, natural-weapon doctrine, animation overlays, VFX dependencies, and Unreal package paths.

## Shared Rules

- Parent body: `SK_INF_Base_A01`
- Adult range: 5'0"-9'0" / 152-274 cm
- Required race traits: red skin, black claws, horns, large leathery wings, long thick tail, predatory posture, regeneration, invisible sight
- Weapon rule: no mortal weapon dependency; claws, wings, tail, body power, brands, and magic carry combat identity
- Visual gate: `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`
- Animation gate: `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`

## Class Package Matrix

| Class | Package | First body bands | Combat identity | Main animation overlay | VFX/material dependency |
| --- | --- | --- | --- | --- | --- |
| Mage | `SK_INF_Mage_A01` | Standard, Greater, Exalted leader later | brand-channel caster, hand magic, wing mantle | brand-channel, abyssal bolt, wing-mantle cast, worthiness gesture | `VFX_INF_AbyssalSpellcasting_A01`, `MI_INF_BrandGlowStates_A01` |
| Warrior | `SK_INF_Warrior_A01` | Standard, Greater, Exalted | claw/shock fighter, tail sweep, wing guard, controlled rage | claw combo, wing buffet, tail sweep, execute, rage surge | `MI_INF_BrandGlowStates_A01`, rage/regeneration notifies |
| Rogue | `SK_INF_Rogue_A01` | Compact, Standard | stealth ambusher, pounce, rake, anti-stealth focus | stalk, crouch, pounce, claw rake, invisible-sight reveal | `VFX_INF_AbyssalSpellcasting_A01`, eye/ambush glow |
| Hunter | `SK_INF_Hunter_A01` | Standard, Greater | tracker, pursuit, anti-stealth, pounce takedown | tracking idle, target lock, wing burst, pounce, target-mark cast | `VFX_INF_AbyssalSpellcasting_A01`, target-mark glow |

## Body Band Use

| Body band | Preferred classes | Notes |
| --- | --- | --- |
| Compact 5'0"-5'8" / 152-173 cm | Rogue, scout-like Hunter variants | Tight wing fold, low stance, fast tail balance |
| Standard 5'8"-6'8" / 173-203 cm | All four starter classes | Primary gameplay band for common adult characters |
| Greater 6'8"-8'0" / 203-244 cm | Warrior, Mage, Hunter elites | Stronger horns, wing roots, tail base, armor mass |
| Exalted 8'0"-9'0" / 244-274 cm | Warrior champions, Mage cult lords | Rare leader/boss use; keep navigation and frame clearance explicit |

## Shared Socket Requirements

- `hand_l_claw`
- `hand_r_claw`
- `hand_l_cast`
- `hand_r_cast`
- `tail_tip`
- `vfx_tail_tip`
- `wing_l_tip`
- `wing_r_tip`
- `vfx_wing_root_l`
- `vfx_wing_root_r`
- `vfx_eye_l`
- `vfx_eye_r`
- `vfx_brand_chest`
- `vfx_regen_core`

## Class-Specific Socket Additions

| Class | Additional sockets |
| --- | --- |
| Mage | `vfx_brand_forearm_l`, `vfx_brand_forearm_r`, `vfx_sorcerer_focus`, `vfx_worthiness_mark` |
| Warrior | `vfx_rage_core`, `tail_sweep_trace`, `wing_buffet_trace` |
| Rogue | `vfx_ambush_mark`, `pounce_trace`, `claw_rake_trace` |
| Hunter | `vfx_target_mark`, `vfx_brow_sight`, `vfx_pursuit_burst` |

## Production Order

1. Approve the four starter class production packages.
2. Build one shared final Infernal base skeleton and socket pass.
3. DCC-fit `SK_INF_Mage_A01` first because it consumes the approved A03 sorcerer references and validates brand/VFX sockets.
4. DCC-fit `SK_INF_Warrior_A01` second to validate claw/tail/wing natural-weapon melee.
5. DCC-fit `SK_INF_Rogue_A01` and `SK_INF_Hunter_A01` after crouch, pounce, and wing-burst motion rules are tested.
6. Build class animation overlays and VFX hooks after final base skeleton naming is locked.

## Quality Gate

- Every class still reads as Infernal before it reads as class costume.
- No class depends on mortal weapons as the primary silhouette.
- Body band fit, sockets, animation overlay, VFX dependency, material dependency, LOD, and Unreal path are documented.
