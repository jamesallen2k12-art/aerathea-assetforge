# SK_INF_Base_A01 Starter Class Animation Implementation Readiness

## Purpose

Convert the approved Infernal starter class animation overlay packets into implementation-ready DCC and Unreal planning without authoring final animation assets, locking combat timing, or changing gameplay authority.

This document is the bridge from docs-only overlay packets to later DCC source creation, montage authoring, ABP state work, notifies, and validators.

## Source Packets

- Shared index: `docs/assets/characters/SK_INF_Base_A01/STARTER_CLASS_ANIMATION_OVERLAY_INDEX.md`
- Base handoff: `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`
- Mage: `docs/assets/characters/SK_INF_Mage_A01/ANIMATION_OVERLAY_PACKET.md`
- Warrior: `docs/assets/characters/SK_INF_Warrior_A01/ANIMATION_OVERLAY_PACKET.md`
- Rogue: `docs/assets/characters/SK_INF_Rogue_A01/ANIMATION_OVERLAY_PACKET.md`
- Hunter: `docs/assets/characters/SK_INF_Hunter_A01/ANIMATION_OVERLAY_PACKET.md`
- VFX dependency: `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/BUILD_IMPORT_STATUS.md`
- Material dependency: `docs/assets/materials/MI_INF_BrandGlowStates_A01/BUILD_IMPORT_STATUS.md`

## Implementation Readiness Matrix

| Class | First implementation slice | ABP target | Skeleton | Validator | Current readiness |
| --- | --- | --- | --- | --- | --- |
| Mage | Upper-body brand channel, hand charge, bolt release, invisible-sight pulse | `/Game/Aerathea/Characters/Infernals/Mage/ABP_INF_Mage_A01` | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton` | `Tools/Unreal/validate_infernal_mage.py` | Ready for montage/notify planning; final cast timing approval still required |
| Warrior | Claw combo, tail sweep, wing buffet, rage surge | `/Game/Aerathea/Characters/Infernals/Warrior/ABP_INF_Warrior_A01` | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton` | `Tools/Unreal/validate_infernal_warrior.py` | Ready for montage/notify planning; final hit and displacement rules still required |
| Rogue | Crouch/stalk locomotion additive, pounce, claw rake, invisible-sight focus | `/Game/Aerathea/Characters/Infernals/Rogue/ABP_INF_Rogue_A01` | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Compact_A01_Skeleton` | `Tools/Unreal/validate_infernal_rogue.py` | Ready for compact-body montage/notify planning; stealth and root-commit rules still required |
| Hunter | Target lock, tracking gesture, wing pursuit burst, pounce, claw takedown | `/Game/Aerathea/Characters/Infernals/Hunter/ABP_INF_Hunter_A01` | `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton` | `Tools/Unreal/validate_infernal_hunter.py` | Ready for montage/notify planning; target-mark and pursuit movement rules still required |

## DCC Source Folder Plan

Do not create or overwrite source files until the DCC task is approved. Use these folders when implementation begins:

| Class | Blender source folder | Export folder |
| --- | --- | --- |
| Base shared overlays | `SourceAssets/Blender/Characters/Infernals/Base/AnimationOverlays/` | `SourceAssets/Exports/Characters/Infernals/Base/AnimationOverlays/` |
| Mage | `SourceAssets/Blender/Characters/Infernals/Mage/AnimationOverlays/` | `SourceAssets/Exports/Characters/Infernals/Mage/AnimationOverlays/` |
| Warrior | `SourceAssets/Blender/Characters/Infernals/Warrior/AnimationOverlays/` | `SourceAssets/Exports/Characters/Infernals/Warrior/AnimationOverlays/` |
| Rogue | `SourceAssets/Blender/Characters/Infernals/Rogue/AnimationOverlays/` | `SourceAssets/Exports/Characters/Infernals/Rogue/AnimationOverlays/` |
| Hunter | `SourceAssets/Blender/Characters/Infernals/Hunter/AnimationOverlays/` | `SourceAssets/Exports/Characters/Infernals/Hunter/AnimationOverlays/` |

Source naming recommendation:

- `AN_INF_Mage_BrandChannel_A01.blend`
- `AN_INF_Mage_AbyssalBolt_A01.blend`
- `AN_INF_Warrior_ClawCombo_A01.blend`
- `AN_INF_Warrior_TailSweep_A01.blend`
- `AN_INF_Rogue_Pounce_A01.blend`
- `AN_INF_Rogue_ClawRake_A01.blend`
- `AN_INF_Hunter_TargetLock_A01.blend`
- `AN_INF_Hunter_WingPursuitBurst_A01.blend`

Export naming recommendation:

- `AN_INF_<Class>_<Move>_A01.fbx`
- `AN_INF_<Class>_<Move>_A01_ROOTLOCK.fbx` only if an in-place/root-locked variant is required.

## Unreal Asset Plan

Target paths:

- Mage animations: `/Game/Aerathea/Characters/Infernals/Mage/Animations/`
- Warrior animations: `/Game/Aerathea/Characters/Infernals/Warrior/Animations/`
- Rogue animations: `/Game/Aerathea/Characters/Infernals/Rogue/Animations/`
- Hunter animations: `/Game/Aerathea/Characters/Infernals/Hunter/Animations/`
- Shared notifies: `/Game/Aerathea/Characters/Infernals/Base/Notifies/`
- Shared montages only if reused across classes: `/Game/Aerathea/Characters/Infernals/Base/Montages/`

Recommended first asset names:

- `M_INF_Mage_BrandChannel_A01`
- `M_INF_Mage_AbyssalBolt_A01`
- `M_INF_Warrior_ClawCombo_A01`
- `M_INF_Warrior_TailSweep_A01`
- `M_INF_Rogue_Pounce_A01`
- `M_INF_Rogue_ClawRake_A01`
- `M_INF_Hunter_TargetLock_A01`
- `M_INF_Hunter_WingPursuitBurst_A01`

## Shared Notify Checklist

Create these as shared notify contracts before class-specific montage wiring:

| Notify | Required fields | First consumers |
| --- | --- | --- |
| `AnimNotify_INF_MaterialState` | material state name, intensity scalar, optional duration | all classes |
| `AnimNotify_INF_VFX_Spawn` | Niagara system name, socket name, attach/detach flag, scale scalar | all classes |
| `AnimNotify_INF_Audio_OneShot` | proposed cue name, socket/world location flag | all classes after audio approval |
| `AnimNotifyState_INF_ClawTrace` | trace socket pair, start/end frames, trace profile key | Mage, Warrior, Rogue, Hunter |
| `AnimNotifyState_INF_TailTrace` | tail trace socket, window, cosmetic/gameplay flag | Warrior, Rogue, Hunter |
| `AnimNotifyState_INF_WingTrace` | wing trace socket, window, cosmetic/gameplay flag | Warrior, Rogue, Hunter, Mage wing mantle |
| `AnimNotifyState_INF_RootCommit` | displacement owner, root-motion flag, approval ticket | Warrior, Rogue, Hunter |
| `AnimNotify_INF_RegenPulse` | VFX system, material state, socket | Mage, Warrior, Rogue, Hunter |
| `AnimNotify_INF_InvisibleSightPulse` | VFX system, eye/brow sockets, reveal policy key | Mage, Rogue, Hunter |

Do not implement gameplay damage, buffs, stealth, reveal, or movement authority inside animation notifies. Notifies should signal Gameplay Ability or Blueprint systems after those rules are approved.

## VFX And Material Cue Checklist

Stable first-pass VFX names:

- `NS_INF_AbyssalHandCharge_A01`
- `NS_INF_AbyssalBolt_A01`
- `NS_INF_ClawSlashCast_A01`
- `NS_INF_BrandChannel_A01`
- `NS_INF_RegenerationFlare_A01`
- `NS_INF_InvisibleSightReveal_A01`
- `NS_INF_WingMantleCast_A01`
- `NS_INF_RageSurge_A01`

Stable first-pass brand material states:

- `MI_INF_BrandGlowStates_A01_Inactive`
- `MI_INF_BrandGlowStates_A01_Smolder`
- `MI_INF_BrandGlowStates_A01_TrialActive`
- `MI_INF_BrandGlowStates_A01_Accepted`
- `MI_INF_BrandGlowStates_A01_Rejected`
- `MI_INF_BrandGlowStates_A01_SorcererFocus`

Current VFX status:

- `VFX_INF_AbyssalSpellcasting_A01` is first-pass/template-derived, not final graph art.
- Bind montage notifies to stable names now.
- Final Niagara graph polish remains a VFX task before final visual approval.

## Per-Class Validation Gaps

| Class | Current validator coverage | Missing before final animation implementation |
| --- | --- | --- |
| Mage | Mesh load, skeleton binding, material slots, sockets, startup placement, first-pass VFX socket dependency | ABP state/montage existence, notify placement, hand charge release event, cast cancel policy |
| Warrior | Mesh load, skeleton binding, material slots, sockets, startup placement | montage slots, claw/tail/wing trace notify windows, root-commit policy, hit/knockback authority |
| Rogue | Mesh load, compact skeleton binding, material slots, sockets, startup placement | crouch/stalk locomotion state, pounce/retreat root policy, stealth/reveal policy, ambush notify contract |
| Hunter | Mesh load, skeleton binding, material slots, sockets, startup placement | target-lock state, target-mark persistence policy, pursuit burst root policy, takedown notify contract |

Add a dedicated overlay validator only after montage assets or ABP state names exist. Before that, rely on focused class validators plus docs/source-reference scans.

## Implementation Order

1. Lock shared notify class names and data fields in docs.
2. Build one class vertical slice in docs and DCC first: Mage brand channel or Warrior claw combo.
3. Export a root-locked/in-place montage candidate.
4. Import into the existing class animation folder without changing mesh or skeleton names.
5. Wire notifies as cosmetic-only events.
6. Run the focused class validator.
7. Add an overlay validator once ABP state or montage asset names exist.
8. Stop before final combat timing, movement authority, damage, stealth, target-mark, or PvP replication decisions.

## Approval Gates

Stop for approval before:

- final combat frame counts and hit windows
- root motion versus gameplay displacement
- stealth, reveal, target-mark, rage, regeneration, execute, or takedown gameplay rules
- network authority and PvP replication
- final VFX graph behavior
- final audio cue set and mix priority

## Quality Gate

- Implementation readiness preserves the shared Infernal race motion identity.
- Each class keeps a distinct body-driven combat read without mortal weapons.
- ABP targets, skeletons, sockets, VFX names, material names, source folders, export folders, notify contracts, validators, and approval gates are named.
- No final animation assets, DCC sources, Unreal assets, combat timings, or gameplay authority rules are claimed complete by this handoff.
