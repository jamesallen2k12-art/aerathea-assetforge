# SK_INF_Rogue_A01 Animation Overlay Packet

## Purpose

Define the docs-only first animation overlay packet for `SK_INF_Rogue_A01`. The Rogue overlay makes the class a compact Infernal ambusher that uses folded wings, low posture, claws, pounce, tail balance, invisible sight, and brief brand pulses instead of daggers or mortal stealth weapons.

This packet is practical production guidance for later authored animation and ABP work. It does not modify Unreal assets.

## Runtime Contract

| Field | Contract |
| --- | --- |
| Mesh | `/Game/Aerathea/Characters/Infernals/Rogue/SK_INF_Rogue_A01` |
| ABP target | `/Game/Aerathea/Characters/Infernals/Rogue/ABP_INF_Rogue_A01` |
| Skeleton | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Compact_A01_Skeleton` |
| Existing focused validator | `Tools/Unreal/validate_infernal_rogue.py` |
| Validated sockets | 25 required sockets |
| VFX dependency | `VFX_INF_AbyssalSpellcasting_A01` |
| Material dependency | `MI_INF_BrandGlowStates_A01` |
| Authority expectation | Local animation and cosmetic notifies first; stealth state, target reveal, ambush hit, displacement, and replication must be owned by gameplay ability logic later. |

## Overlay States

| State | Motion read | Root, wing, and tail constraints |
| --- | --- | --- |
| `Idle_LowStalk` | Compact crouched readiness, claws visible, eyes scanning. | In-place. Wings tightly folded. Tail acts as low balance bar. |
| `Crouch_Turn` | Pelvis low, head still, shoulders and tail rotate with intent. | In-place. Tail must not clip through wraps or tail-root guard. |
| `SilentStep_WalkRun` | Light footfalls, open claw hands, reduced vertical bounce. | In-place. Wings folded tight. Tail counters lateral movement. |
| `AmbushReady` | Wings compress, tail loads, claws spread. | Root commit requires approval. Keep silhouette readable from gameplay camera. |
| `InvisibleSightFocus` | Head stills, eyes and brow glow, hand triangulates target. | In-place. Wings and tail freeze for a short focus beat. |
| `HitReact_Light` | Compact recoil and quick reset. | No broad wing spread except heavy hits. |
| `Death_Rogue` | Fast collapse, wings fold under, glow cuts out. | Keep compact body inside capsule. |

## Combat Montage Set

Frame ranges are draft authoring windows at 30 fps. They are not final combat balance.

| Montage | Draft sections | Notify windows | Notes |
| --- | --- | --- | --- |
| `M_INF_Rogue_SilentStep_A01` | `Step` 0-24, `Settle` 25-34 | foot audio at 6, 18; material dim start 0 | Locomotion additive or short utility montage. Stealth rules require approval. |
| `M_INF_Rogue_Pounce_A01` | `Load` 0-14, `Commit` 15-28, `Impact` 29-38, `Recover` 39-58 | `RootCommit` 15-32, `pounce_trace` 26-38 | Root motion or ability displacement is approval-gated. |
| `M_INF_Rogue_ClawRake_A01` | `Rake1` 0-20, `Rake2` 21-42, `Recover` 43-60 | `ClawTrace` 8-16, 29-38; `claw_rake_trace` 8-38 | Uses `NS_INF_ClawSlashCast_A01` as brief claw arc. |
| `M_INF_Rogue_WingReposition_A01` | `Compress` 0-10, `Burst` 11-24, `Land` 25-42 | wing VFX 11, `RootCommit` 11-26 if approved | Wings assist reposition without reading as flight. |
| `M_INF_Rogue_AmbushStrike_A01` | `Still` 0-12, `Strike` 13-28, `Exit` 29-50 | `vfx_ambush_mark` at 8, `ClawTrace` 15-28 | Ambush bonus, stealth break, and target lock are approval-gated. |
| `M_INF_Rogue_InvisibleSight_A01` | `Focus` 0-16, `Reveal` 17-26, `Release` 27-40 | `InvisibleSightPulse` 16, VFX at `vfx_invisible_sight_focus` 17 | Uses `NS_INF_InvisibleSightReveal_A01`. Reveal duration requires approval. |
| `M_INF_Rogue_TailBalanceTurn_A01` | `Load` 0-8, `Pivot` 9-22, `Settle` 23-34 | `TailTrace` cosmetic 9-22 | Tail is balance, not a high-damage sweep unless approved. |
| `M_INF_Rogue_ControlledRetreat_A01` | `Guard` 0-10, `BackStep` 11-26, `Settle` 27-44 | optional `RootCommit` 11-26 | Movement distance and i-frames are approval-gated. |

## Socket, VFX, And Audio Cue Map

| Use | Socket(s) | VFX/material hook | Audio hook proposal |
| --- | --- | --- | --- |
| Ambush mark | `vfx_ambush_mark`, `vfx_brand_chest` | brief `MI_INF_BrandGlowStates_A01_Smolder` or `SorcererFocus` pulse | `A_INF_Rogue_AmbushPulse_A01` |
| Invisible sight | `vfx_eye_l`, `vfx_eye_r`, `vfx_invisible_sight_focus` | `NS_INF_InvisibleSightReveal_A01` | `A_INF_InvisibleSight_Pulse_A01` |
| Pounce | `pounce_trace`, `hand_l_claw`, `hand_r_claw` | `NS_INF_ClawSlashCast_A01` on impact only | `A_INF_Rogue_Pounce_A01` |
| Claw rake | `claw_rake_trace`, `hand_l_claw`, `hand_r_claw` | `NS_INF_ClawSlashCast_A01` | `A_INF_Rogue_ClawRake_A01` |
| Tail balance | `tail_balance_trace`, `tail_tip`, `vfx_tail_tip` | low tail-tip ember or none | `A_INF_TailBalance_Swish_A01` |
| Crouch center | `crouch_center` | debug trace or ability origin only; no VFX by default | none by default |
| Wing reposition | `vfx_wing_root_l`, `vfx_wing_root_r`, `wing_l_tip`, `wing_r_tip` | brief `NS_INF_WingMantleCast_A01` burst at reduced scale | `A_INF_Rogue_WingBurst_A01` |
| Regeneration | `vfx_regen_core`, `vfx_brand_chest` | `NS_INF_RegenerationFlare_A01` | `A_INF_Regen_CorePulse_A01` |

Audio hooks are proposed names only; no audio asset is required by this packet.

## Root, Wing, And Tail Rules

- Rogue locomotion uses the compact skeleton and should stay low without hiding the race silhouette.
- Wings stay tighter than Mage, Warrior, or Hunter except in short reposition windows.
- Pounce, retreat, and wing reposition displacement are approval-gated.
- Tail is essential for crouch and pounce balance; avoid excessive idle wag or decorative motion.
- Wraps, claw guards, wing anchors, and tail-root guard must clear crouch, pounce, rake, and tail-balance poses.

## LOD And Performance Notes

- LOD0: full crouch, pounce, claw rake, ambush, invisible-sight, tail-balance, and wing-root notify support.
- LOD1: reduce finger detail, wrap secondary motion, and tiny wing membrane adjustments.
- LOD2: preserve pounce body arc, claw-rake silhouette, eyes, and ambush mark; reduce VFX to primary pulses.
- LOD3: material-only eye/ambush pulses; no decorative ash or continuous stealth particles.
- Stealth readability should come from silhouette and timing, not constant VFX.

## Approval-Gated Items

- Final Rogue skill identity and whether the first kit prioritizes stealth, pounce, claw rake, anti-stealth, or retreat.
- Combat pace for pounce travel, rake hit windows, ambush recovery, and retreat distance.
- Stealth entry/exit, reveal duration, target lock, and anti-stealth interaction rules.
- Root motion versus gameplay displacement for pounce, wing reposition, and controlled retreat.
- PvP/MMO authority for stealth, trace hits, reveal, movement commits, and network correction.
- Final audio cue names, mix priority, and attenuation.

## Implementation Handoff

When implementation begins:

1. Keep `ABP_INF_Rogue_A01` derived from the future shared Infernal base locomotion with compact-body overrides.
2. Add crouch/stalk locomotion states before full combat tuning.
3. Use current validated socket names exactly.
4. Trigger VFX and material state changes through notifies or gameplay ability events.
5. Run `Tools/Unreal/validate_infernal_rogue.py` and startup validation after any ABP, socket, mesh, or placement change.

## Quality Gate

- Rogue reads as a weaponless Infernal ambusher, not a dagger assassin.
- Compact folded wings, tail balance, black claws, red skin, horns, and invisible-sight focus stay readable.
- Sockets, VFX, material, audio hooks, montage windows, LOD behavior, and approval gates are documented.
- Combat timing remains draft-only pending approval.
