# SK_INF_Warrior_A01 Animation Overlay Packet

## Purpose

Define the docs-only first animation overlay packet for `SK_INF_Warrior_A01`. The Warrior overlay makes the class a weaponless Infernal shock fighter: claws, horns, tail sweeps, wing pressure, pounce, regeneration, and controlled rage.

This packet is practical production guidance for later authored animation and ABP work. It does not modify Unreal assets.

## Runtime Contract

| Field | Contract |
| --- | --- |
| Mesh | `/Game/Aerathea/Characters/Infernals/Warrior/SK_INF_Warrior_A01` |
| ABP target | `/Game/Aerathea/Characters/Infernals/Warrior/ABP_INF_Warrior_A01` |
| Skeleton | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton` |
| Existing focused validator | `Tools/Unreal/validate_infernal_warrior.py` |
| Validated sockets | 23 required sockets |
| VFX dependency | `VFX_INF_AbyssalSpellcasting_A01` |
| Material dependency | `MI_INF_BrandGlowStates_A01` |
| Authority expectation | Local animation and cosmetic notifies first; combat authority must own trace activation, damage, stagger, movement commits, and replication later. |

## Overlay States

| State | Motion read | Root, wing, and tail constraints |
| --- | --- | --- |
| `Idle_ControlledRage` | Heavy stillness, claw flex, eye lock, chest/rage core contained. | In-place. Wings folded but tense. Tail low and ready. |
| `Idle_WingGuard` | Wing roots lift into protective pressure without full spread. | In-place. Wing collision disabled unless a montage window enables it. |
| `Locomotion_ShockFighterWalkRun` | Broad chest, heavy footfall, hands free for claws. | In-place. Tail counters turns. Wings remain folded. |
| `Turn_HeavyPredator` | Head and shoulders lead; tail whips only after root turn. | In-place unless movement system approves root turns. |
| `Pounce_Ready` | Shoulder drop, claw spread, tail loads, wings brace. | Root motion or ability displacement requires approval. |
| `HitReact_ArmoredLightHeavy` | Bracer guard, wing-root recoil, rage flicker. | Keep root inside capsule. Tail absorbs heavy hits. |
| `Death_Warrior` | Delayed collapse, wings fold over body, rage glow dies. | No large ragdoll wing spread without physics review. |

## Combat Montage Set

Frame ranges are draft authoring windows at 30 fps. They are not final combat balance.

| Montage | Draft sections | Notify windows | Notes |
| --- | --- | --- | --- |
| `M_INF_Warrior_ClawCombo_A01` | `Hit1` 0-22, `Hit2` 23-46, `Hit3` 47-76, `Recover` 77-96 | `ClawTrace` 9-15, 33-40, 58-68; VFX at each trace start | Uses `hand_l_claw`, `hand_r_claw`, and `NS_INF_ClawSlashCast_A01`. Combo speed and chaining are approval-gated. |
| `M_INF_Warrior_BodyCheck_A01` | `Brace` 0-12, `Commit` 13-24, `Impact` 25-32, `Recover` 33-54 | `RootCommit` 13-28, `body_check_trace` 21-31 | Short displacement only if approved. Uses chest/body read, not weapon impact. |
| `M_INF_Warrior_TailSweep_A01` | `Load` 0-18, `Sweep` 19-36, `Recover` 37-60 | `TailTrace` 20-34, VFX at `tail_sweep_trace` 20 | Tail stays broad and readable. Hit arc and knockdown rules require approval. |
| `M_INF_Warrior_WingBuffet_A01` | `RootLift` 0-14, `Buffet` 15-34, `Fold` 35-58 | `WingTrace` 17-32, VFX at `wing_buffet_trace` 15 | Wings are attack display and pressure, not flight. |
| `M_INF_Warrior_Pounce_A01` | `CrouchLoad` 0-16, `Commit` 17-30, `Impact` 31-38, `Recover` 39-66 | `RootCommit` 17-34, `ClawTrace` 28-38 | Root motion or Gameplay Ability displacement must be approved. |
| `M_INF_Warrior_Execute_A01` | `ThreatStillness` 0-18, `Strike` 19-34, `RoarReset` 35-64 | `ClawTrace` 22-34, `RageSurge` 18, mouth audio 35 | Execute availability and combat impact are approval-gated. |
| `M_INF_Warrior_RegenerationFlare_A01` | `PainLock` 0-10, `CorePulse` 11-24, `Reset` 25-44 | `RegenPulse` 11, material pulse 11-24 | Uses `vfx_regen_core`; healing amount is not defined here. |
| `M_INF_Warrior_RageSurge_A01` | `Still` 0-16, `Surge` 17-30, `Release` 31-52 | `MaterialState` 12, `VFX_Spawn` 17, audio 17 | Uses `vfx_rage_core`, `vfx_brand_chest`, and `NS_INF_RageSurge_A01`. |

## Socket, VFX, And Audio Cue Map

| Use | Socket(s) | VFX/material hook | Audio hook proposal |
| --- | --- | --- | --- |
| Claw combo | `hand_l_claw`, `hand_r_claw` | `NS_INF_ClawSlashCast_A01`, brief `MI_INF_BrandGlowStates_A01_Smolder` pulse | `A_INF_Warrior_ClawSwipe_A01` |
| Body check | `body_check_trace`, `vfx_brand_chest` | Brand chest pulse; optional ash impact | `A_INF_Warrior_BodyCheck_A01` |
| Tail sweep | `tail_sweep_trace`, `tail_tip`, `vfx_tail_tip` | Tail-tip ember streak, not constant trail | `A_INF_TailSweep_Heavy_A01` |
| Wing buffet | `wing_buffet_trace`, `vfx_wing_root_l`, `vfx_wing_root_r` | `NS_INF_WingMantleCast_A01` scaled as pressure burst | `A_INF_WingBuffet_A01` |
| Rage surge | `vfx_rage_core`, `vfx_brand_chest`, `vfx_mouth` | `NS_INF_RageSurge_A01`, `MI_INF_BrandGlowStates_A01_TrialActive` | `A_INF_Warrior_RageSurge_A01` |
| Regeneration | `vfx_regen_core`, `vfx_brand_chest` | `NS_INF_RegenerationFlare_A01`, `MI_INF_BrandGlowStates_A01_Smolder` | `A_INF_Regen_CorePulse_A01` |
| Hand threat | `vfx_hand_l`, `vfx_hand_r` | Low hand ember or claw flash only during attack windows | `A_INF_ClawFlex_Threat_A01` |

Audio hooks are proposed names only; no audio asset is required by this packet.

## Root, Wing, And Tail Rules

- Warrior locomotion is in-place by default with heavy stance and strong foot plants.
- Body check and pounce displacement are approval-gated and should be owned by gameplay ability logic if root motion is not approved.
- Wing buffet enables wing trace only for the named montage window, then immediately returns to folded non-blocking state.
- Tail sweep enables tail trace only during the sweep window; idle tail is controlled and heavy.
- Armor, bracers, wing-root guards, tail-root armor, and skull belt must clear all attack windows.

## LOD And Performance Notes

- LOD0: full claw, tail, wing, rage, mouth, and regeneration notify support.
- LOD1: reduce finger detail, secondary wing membrane motion, armor strap motion, and minor tail oscillation.
- LOD2: preserve claw arcs, tail sweep silhouette, wing buffet silhouette, and rage core color block; reduce secondary particles.
- LOD3: broad attack silhouettes and material pulses only; no decorative persistent embers.
- Trace windows must be deterministic and independent of visible VFX.

## Approval-Gated Items

- Final Warrior skill identity and whether the first kit prioritizes claw combo, pounce, tail sweep, or rage.
- Combat pace for combo chain windows, hit confirms, recovery, and interruptibility.
- Root motion versus gameplay displacement for body check and pounce.
- Knockback, stun, execute, rage, regeneration, and threat rules.
- PvP/MMO authority for traces, hit reactions, and movement commits.
- Final audio cue names, mix priority, and attenuation.

## Implementation Handoff

When implementation begins:

1. Keep `ABP_INF_Warrior_A01` derived from the future shared Infernal base locomotion.
2. Add montage slots for full-body claw combo, tail sweep, wing buffet, pounce, execute, regeneration, and rage.
3. Use current validated socket names exactly.
4. Trigger VFX and material state changes through notifies or gameplay ability events, never by mesh collision.
5. Run `Tools/Unreal/validate_infernal_warrior.py` and startup validation after any ABP, socket, mesh, or placement change.

## Quality Gate

- Warrior reads as a natural-weapon Infernal, not a mortal soldier.
- Claws, tail, wing pressure, body mass, rage, and regeneration drive the combat read.
- Sockets, VFX, material, audio hooks, montage windows, LOD behavior, and approval gates are documented.
- Combat timing remains draft-only pending approval.
