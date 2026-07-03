# Infernal Starter Class Animation Overlay Index

## Purpose

This index defines the shared animation-overlay contract for the first four Infernal starter class packets:

- `SK_INF_Mage_A01/ANIMATION_OVERLAY_PACKET.md`
- `SK_INF_Warrior_A01/ANIMATION_OVERLAY_PACKET.md`
- `SK_INF_Rogue_A01/ANIMATION_OVERLAY_PACKET.md`
- `SK_INF_Hunter_A01/ANIMATION_OVERLAY_PACKET.md`

This is a docs-only planning pass for task `AET-MA-20260628-005`. It does not create or modify Unreal assets, DCC sources, validators, source code, or global indexes.

Implementation readiness for the next DCC/Unreal lane is tracked in `docs/assets/characters/SK_INF_Base_A01/ANIMATION_IMPLEMENTATION_READINESS.md`.

## Source Documents Read

- `docs/assets/characters/INFERNAL_STARTER_CLASS_MATRIX.md`
- `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`
- `docs/assets/characters/SK_INF_Mage_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Mage_A01/MODELING_HANDOFF.md`
- `docs/assets/characters/SK_INF_Mage_A01/BUILD_IMPORT_STATUS.md`
- `docs/assets/characters/SK_INF_Warrior_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Warrior_A01/MODELING_HANDOFF.md`
- `docs/assets/characters/SK_INF_Warrior_A01/BUILD_IMPORT_STATUS.md`
- `docs/assets/characters/SK_INF_Rogue_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Rogue_A01/MODELING_HANDOFF.md`
- `docs/assets/characters/SK_INF_Rogue_A01/BUILD_IMPORT_STATUS.md`
- `docs/assets/characters/SK_INF_Hunter_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Hunter_A01/MODELING_HANDOFF.md`
- `docs/assets/characters/SK_INF_Hunter_A01/BUILD_IMPORT_STATUS.md`
- `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`
- Socket and ABP references in `Tools/Unreal/validate_infernal_mage.py`, `validate_infernal_warrior.py`, `validate_infernal_rogue.py`, `validate_infernal_hunter.py`, and matching import scripts.

## Shared Runtime Targets

| Class | ABP target | Skeleton target | First-pass validation |
| --- | --- | --- | --- |
| Mage | `/Game/Aerathea/Characters/Infernals/Mage/ABP_INF_Mage_A01` | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton` | `Tools/Unreal/validate_infernal_mage.py`, 21 sockets |
| Warrior | `/Game/Aerathea/Characters/Infernals/Warrior/ABP_INF_Warrior_A01` | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton` | `Tools/Unreal/validate_infernal_warrior.py`, 23 sockets |
| Rogue | `/Game/Aerathea/Characters/Infernals/Rogue/ABP_INF_Rogue_A01` | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Compact_A01_Skeleton` | `Tools/Unreal/validate_infernal_rogue.py`, 25 sockets |
| Hunter | `/Game/Aerathea/Characters/Infernals/Hunter/ABP_INF_Hunter_A01` | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton` | `Tools/Unreal/validate_infernal_hunter.py`, 27 sockets |

The existing ABPs are placeholders. The overlay packets define what future authored animation, notifies, and gameplay hooks should bind to after combat pacing and class identity are approved.

## Shared Motion Identity

- Infernals move as intelligent mortal-descended predators, not mindless monsters.
- Natural weapons remain primary: claws, horns, wings, tail, body power, brands, and magic.
- Default locomotion keeps wings folded and tail non-blocking.
- Rage, regeneration, invisible sight, and brand state changes must be readable but restrained.
- All class overlays inherit base claw, wing, tail, rage, regeneration, and invisible-sight rules from `ANIMATION_HANDOFF.md`.

## Root Motion Policy

Default MMO locomotion should stay in-place and network-friendly until the multiplayer authority model is approved.

Root motion is allowed only as an approval-gated exception for:

- short pounce commits
- body-check or execute displacement
- wing-assisted pursuit burst
- ambush leap or controlled retreat

If root motion is rejected for production, those same moves should use authored in-place montages with Gameplay Ability or Blueprint displacement windows.

## Wing Constraints

- Folded wings are the default for idle, walk, run, turn, and most combat loops.
- Spread wings only during named windows: wing mantle, wing buffet, pursuit burst, pounce anticipation, hit-react spread, intimidation flare, or boss-only display.
- Wings remain non-blocking in locomotion and normal casts.
- Wing collision or traces may be enabled only during montage windows that explicitly name `wing_buffet_trace`, `wing_burst_trace`, `wing_l_tip`, `wing_r_tip`, `vfx_wing_root_l`, or `vfx_wing_root_r`.
- Avoid constant membrane flutter. Use low-frequency root tension and brief snaps.

## Tail Constraints

- Tail is thick, muscular, and used for counterbalance.
- Idle tail motion is restrained and purposeful.
- Tail trace or auxiliary collision is enabled only in named attack, balance, or hit-react windows.
- Tail sweep and pounce balance must preserve the primary silhouette before decorative tail-tip motion.
- Tail motion should not drag through cloth panels, wing harness straps, skull belts, or tail-root armor.

## Shared Socket Contract

All starter overlays should treat these sockets as stable first-pass contract points:

- `hand_l_claw`
- `hand_r_claw`
- `hand_l_cast`
- `hand_r_cast`
- `vfx_hand_l`
- `vfx_hand_r`
- `vfx_eye_l`
- `vfx_eye_r`
- `vfx_brand_chest`
- `vfx_brand_forearm_l`
- `vfx_brand_forearm_r`
- `vfx_wing_root_l`
- `vfx_wing_root_r`
- `wing_l_tip`
- `wing_r_tip`
- `tail_tip`
- `vfx_tail_tip`
- `vfx_regen_core`
- `vfx_mouth`

Class-specific sockets are listed in each packet and match the current focused validators.

## Shared VFX And Material Hooks

Use existing asset names from `VFX_INF_AbyssalSpellcasting_A01` and `MI_INF_BrandGlowStates_A01`:

- `NS_INF_AbyssalHandCharge_A01`
- `NS_INF_AbyssalBolt_A01`
- `NS_INF_ClawSlashCast_A01`
- `NS_INF_BrandChannel_A01`
- `NS_INF_RegenerationFlare_A01`
- `NS_INF_InvisibleSightReveal_A01`
- `NS_INF_WingMantleCast_A01`
- `NS_INF_RageSurge_A01`
- `MI_INF_BrandGlowStates_A01_Inactive`
- `MI_INF_BrandGlowStates_A01_Smolder`
- `MI_INF_BrandGlowStates_A01_TrialActive`
- `MI_INF_BrandGlowStates_A01_Accepted`
- `MI_INF_BrandGlowStates_A01_Rejected`
- `MI_INF_BrandGlowStates_A01_SorcererFocus`

The current Niagara systems are first-pass/template-derived review foundations. Animation packets should bind to names and sockets now, while final Niagara graph art remains a later VFX task.

## Shared Notify Vocabulary

These are proposed notify names for future ABP/montage authoring. They are not implemented by this docs pass.

| Notify | Purpose |
| --- | --- |
| `AnimNotify_INF_MaterialState` | Set or pulse one `MI_INF_BrandGlowStates_A01_*` state. |
| `AnimNotify_INF_VFX_Spawn` | Spawn one named Niagara system at a named socket. |
| `AnimNotify_INF_Audio_OneShot` | Play one optional future audio cue hook. |
| `AnimNotifyState_INF_ClawTrace` | Enable/disable claw trace windows. |
| `AnimNotifyState_INF_TailTrace` | Enable/disable tail sweep, tail balance, or tail hit windows. |
| `AnimNotifyState_INF_WingTrace` | Enable/disable wing buffet or wing burst trace windows. |
| `AnimNotifyState_INF_RootCommit` | Mark approval-gated movement displacement or root-motion commit windows. |
| `AnimNotify_INF_RegenPulse` | Trigger regeneration material/VFX/audio sync. |
| `AnimNotify_INF_InvisibleSightPulse` | Trigger eye/brow/sight reveal material/VFX sync. |

Audio cue names in the class packets are hook proposals only. Final audio assets, mix levels, attenuation, and replication behavior require an audio pass.

## LOD And Performance Rules

- LOD0: full authored overlay animation, finger/hand silhouette, wing root tension, tail counterbalance, all approved VFX notify hooks.
- LOD1: preserve combat silhouettes; reduce finger detail, secondary wing membrane motion, and minor tail oscillation.
- LOD2: preserve root, hands, eyes, wing mass, tail line, and major attack arcs; disable decorative ash and secondary sparks.
- LOD3: in-place locomotion and broad attack reads only; use material glow blocks instead of particles where possible.
- Disable constant particle loops on idle classes unless a gameplay state explicitly requires them.
- Do not scale particle density linearly for Greater or Exalted bodies.
- Keep trace windows deterministic and short. No mesh collision should define gameplay hits.

## Approval Gates

Stop for approval before locking any of these:

- final class skill identity
- combat pace, frame counts, hit timing, and recovery timing
- root-motion versus in-place displacement policy
- stealth reveal duration or anti-stealth rules
- rage, regeneration, and execute gameplay impact
- PvP/MMO replication authority for traces, notifies, buffs, and movement commits
- final audio cue set and mix priority

## Implementation Checks Later

When the animation overlays move from docs to implementation, run or add checks in this order:

1. Confirm ABP assets compile and still load at their current paths.
2. Run each focused class validator after any socket or skeleton change.
3. Run startup validation after any class ABP, mesh, or scene placement change.
4. Add a dedicated overlay validator only after montage assets or ABP state names exist.
5. Confirm `VFX_INF_AbyssalSpellcasting_A01` and `MI_INF_BrandGlowStates_A01` asset names remain unchanged.

## Quality Gate

- The overlays make the classes feel different without breaking the shared Infernal race read.
- No class depends on mortal weapons for its primary combat identity.
- Wings and tail support motion, balance, threat display, and ability windows.
- Sockets, VFX hooks, material hooks, audio hooks, montage windows, LOD behavior, and approval gates are documented.
- Combat pace remains explicitly approval-gated.
