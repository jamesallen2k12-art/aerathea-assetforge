# SK_INF_Mage_A01 Animation Overlay Packet

## Purpose

Define the docs-only first animation overlay packet for `SK_INF_Mage_A01`. The Mage overlay keeps the Infernal caster identity body-driven: brands, open claws, eyes, wings, tail, and abyssal channeling replace mortal staffs, books, wands, and weapon silhouettes.

This packet is practical production guidance for later authored animation and ABP work. It does not modify Unreal assets.

## Runtime Contract

| Field | Contract |
| --- | --- |
| Mesh | `/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01` |
| ABP target | `/Game/Aerathea/Characters/Infernals/Mage/ABP_INF_Mage_A01` |
| Skeleton | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton` |
| Existing focused validator | `Tools/Unreal/validate_infernal_mage.py` |
| Validated sockets | 21 required sockets |
| VFX dependency | `VFX_INF_AbyssalSpellcasting_A01` |
| Material dependency | `MI_INF_BrandGlowStates_A01` |
| Authority expectation | Local animation and cosmetic notifies first; gameplay ability authority must own damage, projectile spawn, cast success, interruption, and replication later. |

## Overlay States

| State | Motion read | Root, wing, and tail constraints |
| --- | --- | --- |
| `Idle_PredatoryCaster` | Upright, intelligent stillness, semi-open claws, eyes forward. | In-place. Wings folded with low root tension. Tail rests as counterweight, not constant sway. |
| `Idle_BrandSmolder` | Chest and forearm readiness, slight hand flex, controlled breathing. | In-place. No wing spread. Tail stills during brand pulse. |
| `Locomotion_CasterWalkRun` | Standard locomotion with hands ready for spell release. | In-place blendspace. Wings folded. Tail counters turns. |
| `Turn_Caster90_180` | Head and eye lead, shoulder follows, tail anticipates. | In-place unless movement system approves root turn. Wings stay folded. |
| `JumpLand_WingAssist` | Short wing tension on takeoff and landing, not flight. | Root motion approval required for leap distance. Wing spread limited to takeoff/landing window. |
| `HitReact_CasterLightHeavy` | Brand flicker, claw guard, wing-root recoil. | No gameplay displacement unless hit system owns it. Tail recovers first on heavy react. |
| `Death_Caster` | Controlled collapse with wings folding inward and brands dimming. | Root stays inside capsule. Tail and wings settle without blocking. |

## Combat Montage Set

Frame ranges are draft authoring windows at 30 fps. They are not final combat balance.

| Montage | Draft sections | Notify windows | Notes |
| --- | --- | --- | --- |
| `M_INF_Mage_BrandChannel_A01` | `Start` 0-12, `Loop` 13-48, `ReleaseOrCancel` 49-64 | `MaterialState` at 4, `VFX_Spawn` at 8, channel loop 13-48, cooldown 49-64 | Uses `NS_INF_BrandChannel_A01` at `vfx_brand_chest`, then hand sockets. Loop length and cast cancel rules need approval. |
| `M_INF_Mage_AbyssalBolt_A01` | `Windup` 0-16, `Charge` 17-32, `Release` 33-38, `Recover` 39-56 | `HandCharge` 12-32, projectile release at 33, audio release at 33 | Uses `NS_INF_AbyssalHandCharge_A01` then `NS_INF_AbyssalBolt_A01` from `hand_r_cast` or both hands. |
| `M_INF_Mage_OneHandClawCast_A01` | `Windup` 0-10, `SlashCast` 11-20, `Recover` 21-38 | `ClawTrace` 11-18, `VFX_Spawn` 11 | Uses `NS_INF_ClawSlashCast_A01` at `hand_l_claw` or `hand_r_claw`. Damage timing is approval-gated. |
| `M_INF_Mage_WingMantleCast_A01` | `MantleOpen` 0-18, `Channel` 19-46, `Collapse` 47-66 | `WingTrace` cosmetic only 12-24, `VFX_Spawn` 16, 24 | Uses `NS_INF_WingMantleCast_A01` at `vfx_wing_root_l` and `vfx_wing_root_r`. Wings must not block navigation. |
| `M_INF_Mage_InvisibleSight_A01` | `Focus` 0-18, `RevealPulse` 19-28, `Release` 29-44 | `InvisibleSightPulse` 18, `VFX_Spawn` 19 | Uses `vfx_eye_l`, `vfx_eye_r`, `vfx_sorcerer_focus`, and `NS_INF_InvisibleSightReveal_A01`. Reveal rules require gameplay approval. |
| `M_INF_Mage_RegenerationFlare_A01` | `WoundTension` 0-12, `CorePulse` 13-26, `Reset` 27-46 | `RegenPulse` 13, material pulse 13-26 | Uses `vfx_regen_core`, `vfx_brand_chest`, and `NS_INF_RegenerationFlare_A01`. Healing value is not defined here. |
| `M_INF_Mage_RageSurge_A01` | `Stillness` 0-14, `Surge` 15-28, `FocusRecover` 29-48 | `MaterialState` 10, `VFX_Spawn` 15, cooldown 29 | Uses `NS_INF_RageSurge_A01`. Rage gameplay effect is approval-gated. |
| `M_INF_Mage_WorthinessGesture_A01` | `Raise` 0-18, `Judge` 19-34, `Lower` 35-54 | material pulse at 18, optional audio at 19 | Uses `vfx_worthiness_mark` and brand states only unless ritual Blueprint provides WorthinessJudgment VFX. |

## Socket, VFX, And Audio Cue Map

| Use | Socket(s) | VFX/material hook | Audio hook proposal |
| --- | --- | --- | --- |
| Hand charge | `hand_l_cast`, `hand_r_cast`, `vfx_hand_l`, `vfx_hand_r` | `NS_INF_AbyssalHandCharge_A01`, `MI_INF_BrandGlowStates_A01_SorcererFocus` | `A_INF_Mage_HandCharge_A01` |
| Abyssal bolt release | `hand_r_cast`, optional `hand_l_cast` | `NS_INF_AbyssalBolt_A01` | `A_INF_Mage_BoltRelease_A01` |
| Brand channel | `vfx_brand_chest`, `vfx_brand_forearm_l`, `vfx_brand_forearm_r` | `NS_INF_BrandChannel_A01`, `MI_INF_BrandGlowStates_A01_TrialActive` or `SorcererFocus` | `A_INF_Mage_BrandChannel_Loop_A01` |
| Claw cast | `hand_l_claw`, `hand_r_claw` | `NS_INF_ClawSlashCast_A01` | `A_INF_ClawCast_Swipe_A01` |
| Wing mantle | `vfx_wing_root_l`, `vfx_wing_root_r`, `wing_l_tip`, `wing_r_tip` | `NS_INF_WingMantleCast_A01` | `A_INF_WingMantle_Whoosh_A01` |
| Invisible sight | `vfx_eye_l`, `vfx_eye_r`, `vfx_sorcerer_focus` | `NS_INF_InvisibleSightReveal_A01`, `MI_INF_BrandGlowStates_A01_SorcererFocus` | `A_INF_InvisibleSight_Pulse_A01` |
| Regeneration | `vfx_regen_core`, `vfx_brand_chest` | `NS_INF_RegenerationFlare_A01`, `MI_INF_BrandGlowStates_A01_Smolder` | `A_INF_Regen_CorePulse_A01` |
| Worthiness gesture | `vfx_worthiness_mark`, `vfx_brand_chest` | Brand state pulse; ritual Blueprint may add WorthinessJudgment VFX | `A_INF_Worthiness_Gesture_A01` |
| Mouth threat accent | `vfx_mouth` | Optional ember breath flash, no constant fire | `A_INF_Mage_GrowlCast_A01` |

Audio hooks are proposed names only; no audio asset is required by this packet.

## Root, Wing, And Tail Rules

- Mage casting remains mostly in-place so spell readability stays high at MMO camera distance.
- Tail counterbalances hand casts and wing mantle, but should settle during exact release frames.
- Wing mantle cast can spread wings for silhouette and threat, but default locomotion and basic bolt casts keep wings folded.
- Hover or leap cast anticipation from `ANIMATION_HANDOFF.md` remains approval-gated until traversal rules exist.
- Cloth panels, skull belt, and wing mantle must clear cast, hit-react, and tail counterweight poses.

## LOD And Performance Notes

- LOD0: full hand, eye, chest, forearm, wing-root, tail, and mouth notify support.
- LOD1: reduce finger curls and small cloth secondary motion; preserve open claw cast silhouette.
- LOD2: disable decorative ash and secondary sparks; keep hand/eye/chest material pulses.
- LOD3: material-only hand, eye, and chest pulses; no constant particle loops.
- Boss or Exalted variants may scale radius and intensity only after VFX readability approval.

## Approval-Gated Items

- Final Mage skill identity and whether the first offensive spell is bolt, claw cast, channel, or ritual judgment.
- Combat pace for bolt windup/release/recovery, channel cancel timing, and claw-cast trace duration.
- Hover, glide, or leap casting.
- Interrupt, silence, stagger, or channel-break rules.
- Damage, projectile authority, target acquisition, and PvP replication.
- Final audio cue names, mix priority, and attenuation.

## Implementation Handoff

When implementation begins:

1. Keep `ABP_INF_Mage_A01` derived from the future shared Infernal base locomotion.
2. Add montage slots for upper-body casts and full-body wing mantle.
3. Use current validated socket names exactly.
4. Trigger `VFX_INF_AbyssalSpellcasting_A01` and `MI_INF_BrandGlowStates_A01` through notifies or gameplay ability events.
5. Run `Tools/Unreal/validate_infernal_mage.py` and startup validation after any ABP, socket, mesh, or placement change.

## Quality Gate

- Mage reads as an Infernal brand-channel caster, not a mortal wizard.
- Claws, wings, tail, horns, eyes, and brands carry the spell language.
- Sockets, VFX, material, audio hooks, montage windows, LOD behavior, and approval gates are documented.
- Combat timing remains draft-only pending approval.
