# SK_INF_Hunter_A01 Animation Overlay Packet

## Purpose

Define the docs-only first animation overlay packet for `SK_INF_Hunter_A01`. The Hunter overlay makes the class a weaponless Infernal tracker and pursuit predator: invisible sight, target mark, wing-assisted bursts, pounce, tail balance, claw takedown, and controlled kill poses replace bows, rifles, traps, spears, and nets.

This packet is practical production guidance for later authored animation and ABP work. It does not modify Unreal assets.

## Runtime Contract

| Field | Contract |
| --- | --- |
| Mesh | `/Game/Aerathea/Characters/Infernals/Hunter/SK_INF_Hunter_A01` |
| ABP target | `/Game/Aerathea/Characters/Infernals/Hunter/ABP_INF_Hunter_A01` |
| Skeleton | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton` |
| Existing focused validator | `Tools/Unreal/validate_infernal_hunter.py` |
| Validated sockets | 27 required sockets |
| VFX dependency | `VFX_INF_AbyssalSpellcasting_A01` |
| Material dependency | `MI_INF_BrandGlowStates_A01` |
| Authority expectation | Local animation and cosmetic notifies first; target mark, reveal, pursuit movement, pounce hit, takedown, and replication must be owned by gameplay ability logic later. |

## Overlay States

| State | Motion read | Root, wing, and tail constraints |
| --- | --- | --- |
| `Idle_AlertTracking` | Head scans, brow/eye readiness, hands open, tail poised. | In-place. Wings folded but ready. Tail aligns with gaze changes. |
| `TargetLock` | Head stills, brow sight activates, one claw triangulates target. | In-place. Wings and tail freeze for a short focus beat. |
| `Locomotion_PursuitWalkRun` | Longer stride than Rogue, lighter than Warrior, direct pursuit energy. | In-place. Wings folded; tail counters fast turns. |
| `WingBurstReady` | Wing roots load, shoulders drop, claws ready. | Root commit requires approval. Wing spread stays short. |
| `PounceReady` | Tail loads, chest lowers, eyes lock. | Root motion or ability displacement requires approval. |
| `HitReact_Pursuit` | Fast recoil with tail recovery and wing-root twitch. | Keep root inside capsule unless hit system owns displacement. |
| `Death_Hunter` | Collapse forward or to side, target mark fades, wings fold. | Avoid wide wing sprawl unless physics review approves it. |

## Combat Montage Set

Frame ranges are draft authoring windows at 30 fps. They are not final combat balance.

| Montage | Draft sections | Notify windows | Notes |
| --- | --- | --- | --- |
| `M_INF_Hunter_TargetLock_A01` | `Scan` 0-14, `Lock` 15-30, `Release` 31-42 | `InvisibleSightPulse` 14, `vfx_target_mark` 15 | Uses `vfx_brow_sight`, `vfx_eye_l`, `vfx_eye_r`, and `vfx_target_mark`. Targeting rules require approval. |
| `M_INF_Hunter_TrackingGesture_A01` | `ScentRead` 0-16, `BrandPing` 17-26, `Reset` 27-42 | material pulse 17, optional VFX at `tracking_center` | Tracking info, range, and cooldown are approval-gated. |
| `M_INF_Hunter_WingPursuitBurst_A01` | `Load` 0-12, `Burst` 13-28, `Settle` 29-48 | `RootCommit` 13-30, `WingTrace` 13-28, VFX at `vfx_pursuit_burst` | Movement displacement is approval-gated. Wings assist pursuit without reading as sustained flight. |
| `M_INF_Hunter_Pounce_A01` | `CrouchLoad` 0-16, `Commit` 17-30, `Impact` 31-40, `Recover` 41-62 | `RootCommit` 17-34, `pounce_trace` 28-40 | Uses body, claws, and tail balance. Travel distance requires approval. |
| `M_INF_Hunter_ClawTakedown_A01` | `Hook` 0-18, `Drive` 19-36, `Control` 37-58 | `claw_takedown_trace` 12-34, audio 19 | Takedown rules, hold duration, and target eligibility are approval-gated. |
| `M_INF_Hunter_TailBalanceTurn_A01` | `Load` 0-8, `Pivot` 9-24, `Settle` 25-38 | `TailTrace` cosmetic 9-24 | Tail stabilizes fast pursuit turns, not a default damage sweep. |
| `M_INF_Hunter_AntiStealthReveal_A01` | `Focus` 0-18, `Reveal` 19-32, `Release` 33-48 | `InvisibleSightPulse` 18, VFX 19 | Uses `NS_INF_InvisibleSightReveal_A01`. Reveal gameplay is approval-gated. |
| `M_INF_Hunter_ControlledKill_A01` | `Stillness` 0-14, `Strike` 15-30, `Reset` 31-52 | `claw_takedown_trace` 17-30, target mark dim 31 | Finisher/execute rules are not locked here. |

## Socket, VFX, And Audio Cue Map

| Use | Socket(s) | VFX/material hook | Audio hook proposal |
| --- | --- | --- | --- |
| Target mark | `vfx_target_mark`, `vfx_brow_sight`, `vfx_eye_l`, `vfx_eye_r` | `NS_INF_InvisibleSightReveal_A01`, `MI_INF_BrandGlowStates_A01_SorcererFocus` | `A_INF_Hunter_TargetLock_A01` |
| Tracking gesture | `tracking_center`, `vfx_brand_chest`, `vfx_brand_forearm_l`, `vfx_brand_forearm_r` | brief `NS_INF_BrandChannel_A01` or material pulse | `A_INF_Hunter_TrackingPing_A01` |
| Pursuit burst | `vfx_pursuit_burst`, `wing_burst_trace`, `vfx_wing_root_l`, `vfx_wing_root_r` | reduced-scale `NS_INF_WingMantleCast_A01` | `A_INF_Hunter_PursuitBurst_A01` |
| Pounce | `pounce_trace`, `hand_l_claw`, `hand_r_claw`, `tail_balance_trace` | brief `NS_INF_ClawSlashCast_A01` on impact | `A_INF_Hunter_Pounce_A01` |
| Claw takedown | `claw_takedown_trace`, `hand_l_claw`, `hand_r_claw` | `NS_INF_ClawSlashCast_A01`; optional target-mark dim | `A_INF_Hunter_Takedown_A01` |
| Anti-stealth reveal | `vfx_brow_sight`, `vfx_eye_l`, `vfx_eye_r`, `vfx_target_mark` | `NS_INF_InvisibleSightReveal_A01` | `A_INF_InvisibleSight_Pulse_A01` |
| Tail balance | `tail_balance_trace`, `tail_tip`, `vfx_tail_tip` | low tail-tip ember or none | `A_INF_TailBalance_Swish_A01` |
| Regeneration | `vfx_regen_core`, `vfx_brand_chest` | `NS_INF_RegenerationFlare_A01` | `A_INF_Regen_CorePulse_A01` |

Audio hooks are proposed names only; no audio asset is required by this packet.

## Root, Wing, And Tail Rules

- Hunter locomotion is more direct than Rogue and lighter than Warrior.
- Wing burst and pounce displacement are approval-gated and should be owned by gameplay ability logic if root motion is not approved.
- Wings spread only during pursuit burst, pounce anticipation, or hit reaction, then return to folded non-blocking state.
- Tail controls high-speed turns and pounce landings. Tail trace is cosmetic or balance-only unless gameplay approves damage.
- Wing harness straps, claw guards, pursuit armor, and tail bands must clear pursuit burst, pounce, and takedown poses.

## LOD And Performance Notes

- LOD0: full target-mark, brow-sight, pursuit-burst, pounce, claw-takedown, tail-balance, and regeneration notify support.
- LOD1: reduce finger detail, wing strap motion, minor tail oscillation, and small trophy movement.
- LOD2: preserve target mark, eyes/brow, pounce silhouette, wing burst silhouette, and claw takedown; reduce secondary particles.
- LOD3: material-only eye/brow/target pulses; no decorative tracking particles.
- Target-mark VFX must not become a constant screen clutter layer.

## Approval-Gated Items

- Final Hunter skill identity and whether the first kit prioritizes target mark, pursuit burst, pounce, takedown, or anti-stealth.
- Combat pace for target lock, pounce travel, takedown hit window, and recovery.
- Tracking data, reveal duration, target-mark persistence, and cooldowns.
- Root motion versus gameplay displacement for pursuit burst and pounce.
- PvP/MMO authority for target mark, reveal, movement commits, trace hits, and network correction.
- Final audio cue names, mix priority, and attenuation.

## Implementation Handoff

When implementation begins:

1. Keep `ABP_INF_Hunter_A01` derived from the future shared Infernal base locomotion.
2. Add target-lock and pursuit-burst states before tuning combat numbers.
3. Use current validated socket names exactly.
4. Trigger VFX and material state changes through notifies or gameplay ability events.
5. Run `Tools/Unreal/validate_infernal_hunter.py` and startup validation after any ABP, socket, mesh, or placement change.

## Quality Gate

- Hunter reads as a weaponless Infernal tracker, not an archer.
- Eye/brow sight, target mark, wing burst, tail balance, pounce, and claw takedown carry the class identity.
- Sockets, VFX, material, audio hooks, montage windows, LOD behavior, and approval gates are documented.
- Combat timing remains draft-only pending approval.
