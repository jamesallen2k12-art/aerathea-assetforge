# Infernal Starter Class Matrix

## Purpose

This matrix ties the first four approved Infernal starter class packages to the approved adult body bands, natural-weapon doctrine, animation overlays, VFX dependencies, and Unreal package paths.

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
| Warrior | `SK_INF_Warrior_A01` | Standard, Greater, Exalted | claw/shock fighter, tail sweep, wing guard, controlled rage | claw combo, wing buffet, tail sweep, execute, rage surge | `VFX_INF_AbyssalSpellcasting_A01`, `MI_INF_BrandGlowStates_A01`, rage/regeneration notifies |
| Rogue | `SK_INF_Rogue_A01` | Compact, Standard | stealth ambusher, pounce, rake, anti-stealth focus | stalk, crouch, pounce, claw rake, invisible-sight reveal | `VFX_INF_AbyssalSpellcasting_A01`, `MI_INF_BrandGlowStates_A01`, eye/ambush glow |
| Hunter | `SK_INF_Hunter_A01` | Standard, Greater | tracker, pursuit, anti-stealth, pounce takedown | tracking idle, target lock, wing burst, pounce, target-mark cast | `VFX_INF_AbyssalSpellcasting_A01`, `MI_INF_BrandGlowStates_A01`, target-mark/brow-sight glow |

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
| Warrior | `vfx_rage_core`, `tail_sweep_trace`, `wing_buffet_trace`, `body_check_trace` |
| Rogue | `vfx_ambush_mark`, `vfx_invisible_sight_focus`, `pounce_trace`, `claw_rake_trace`, `tail_balance_trace`, `crouch_center` |
| Hunter | `vfx_target_mark`, `vfx_brow_sight`, `vfx_pursuit_burst`, `pounce_trace`, `claw_takedown_trace`, `tail_balance_trace`, `tracking_center`, `wing_burst_trace` |

## Production Order

1. Starter class production packages approved by Flamestrike on 2026-06-28.
2. Build one shared final Infernal base skeleton and socket pass.
3. `SK_INF_Mage_A01` first-pass DCC/Unreal review fit is complete and validates the shared tall Infernal skeleton binding plus brand, hand, eye, wing, tail, sorcerer-focus, and worthiness sockets.
4. `VFX_INF_AbyssalSpellcasting_A01` first-pass material/Niagara review assets are complete and validate the shared spellcasting asset names plus Mage socket-facing contract.
5. `SK_INF_Warrior_A01` first-pass DCC/Unreal review fit is complete and validates claw/tail/wing natural-weapon melee, rage core, body-check, tail-sweep, and wing-buffet sockets.
6. `SK_INF_Rogue_A01` first-pass DCC/Unreal review fit is complete and validates compact Infernal skeleton binding plus ambush, invisible-sight, pounce, claw-rake, tail-balance, and crouch sockets.
7. `SK_INF_Hunter_A01` first-pass DCC/Unreal review fit is complete and validates tall Infernal skeleton binding plus pursuit, target-mark, brow-sight, pounce, claw-takedown, tail-balance, tracking-center, and wing-burst sockets.
8. `MI_INF_BrandGlowStates_A01` first-pass Unreal material-state authoring is complete and validates the shared master material, material function placeholder, six state instances, and starter-class socket-facing contract.
9. Build class animation overlays and final VFX graph hooks after final base skeleton naming, socket contracts, and shared material-state names are locked.

## Quality Gate

- Every class still reads as Infernal before it reads as class costume.
- No class depends on mortal weapons as the primary silhouette.
- Body band fit, sockets, animation overlay, VFX dependency, material dependency, LOD, and Unreal path are documented.
