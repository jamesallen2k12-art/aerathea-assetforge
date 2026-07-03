# Infernal Approval Queue

## Purpose

This queue records Infernal package approvals that must be resolved before DCC
builds, Unreal imports, authored VFX, or animation production starts.

## Current Approval Status

Flamestrike approved the Infernal starter lane on 2026-06-28:

- Starter classes approved: `SK_INF_Mage_A01`, `SK_INF_Warrior_A01`, `SK_INF_Rogue_A01`, and `SK_INF_Hunter_A01`.
- First class DCC child: `SK_INF_Mage_A01`, now validated as a first-pass DCC/Unreal review implementation.
- Second class DCC child: `SK_INF_Warrior_A01`, now validated as a first-pass DCC/Unreal review implementation.
- Third class DCC child: `SK_INF_Rogue_A01`, now validated as a first-pass DCC/Unreal review implementation.
- Fourth class DCC child: `SK_INF_Hunter_A01`, now validated as a first-pass DCC/Unreal review implementation.
- First cult prop DCC child: `SM_INF_HornWingArch_A01`, now validated as a first-pass DCC/Unreal review implementation.
- Combat VFX direction approved: `VFX_INF_AbyssalSpellcasting_A01`, now validated as first-pass Unreal material/Niagara review assets.
- Animation direction approved: `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`.

This queue now separates approved work, package-ready deferred work, and fresh
approval gates so the next production sprint can advance without confusing
validated first-pass assets with final art, final VFX, final animation, or new
gameplay behavior.

## Resolved Approval Gates

| Gate | Approved decision | Production effect |
| --- | --- | --- |
| Starter class direction | Approve `SK_INF_Mage_A01`, `SK_INF_Warrior_A01`, `SK_INF_Rogue_A01`, and `SK_INF_Hunter_A01` as the starter class set | Locks class silhouettes and prevents weapon-dependent drift before DCC fit work |
| First class DCC child | Start with `SK_INF_Mage_A01`; first-pass DCC/Unreal review lane complete | Uses the approved A03 sorcerer references and validates brand, hand, eye, wing, tail, and combat VFX sockets |
| Second class DCC child | Continue with `SK_INF_Warrior_A01`; first-pass DCC/Unreal review lane complete | Validates the Greater-band natural-weapon melee silhouette, claw/tail/wing traces, rage core, regeneration hook, body-check trace, shared skeleton binding, and startup placement |
| Third class DCC child | Continue with `SK_INF_Rogue_A01`; first-pass DCC/Unreal review lane complete | Validates the Compact-band stealth silhouette, compact Infernal skeleton binding, tight folded wings, pounce/rake traces, invisible-sight focus, tail-balance trace, and startup placement |
| Fourth class DCC child | Continue with `SK_INF_Hunter_A01`; first-pass DCC/Unreal review lane complete | Validates the Standard/Greater-band pursuit silhouette, tall Infernal skeleton binding, target-mark, brow-sight, pursuit-burst, pounce, claw-takedown, tail-balance, tracking-center, wing-burst sockets, and startup placement |
| First cult prop DCC child | Start with `SM_INF_HornWingArch_A01`; first-pass DCC/Unreal review lane complete | Validates gate/threshold scale, cult architecture language, authored collision, LODs, sockets, and snap alignment with `SM_INF_CullingTrialFloor_A01` |
| Combat VFX direction | Approve `VFX_INF_AbyssalSpellcasting_A01`; first-pass material/Niagara review assets complete | Gives Mage, Hunter, Rogue, and base body states stable asset names, material instances, socket validation, and shared rules for flame, lightning-like arcs, eye glow, regeneration, and rage without noisy screen clutter |
| Animation direction | Approve `ANIMATION_HANDOFF.md` | Locks claw, wing, tail, rage, regeneration, and invisible-sight motion rules before animation authoring |

## Active Approval Gates

No active approval gates remain for the Infernal starter lane. The items below
are separated by production status so follow-up work can be scheduled without
reopening already-cleared decisions.

## Approved / Cleared For Current Production Use

| Item | Current status | What this clears | What this does not clear |
| --- | --- | --- | --- |
| `SK_INF_Mage_A01` | First-pass DCC/Unreal review implementation complete and validated | Starter class silhouette, tall Infernal socket layout, Mage spell/VFX socket contract | Final sculpt, final materials, final animation clips, combat balance |
| `SK_INF_Warrior_A01` | First-pass DCC/Unreal review implementation complete and validated | Greater-band natural-weapon melee silhouette and sockets | Final sculpt, final animation clips, damage timing, displacement rules |
| `SK_INF_Rogue_A01` | First-pass DCC/Unreal review implementation complete and validated | Compact-band stealth silhouette and ambush/pounce socket contract | Final stealth rules, root commitment, final animation clips |
| `SK_INF_Hunter_A01` | First-pass DCC/Unreal review implementation complete and validated | Pursuit/tracking silhouette and target-mark socket contract | Final target-mark gameplay, pursuit movement rules, final animation clips |
| `SM_INF_HornWingArch_A01` | First-pass DCC/Unreal review implementation complete and validated | Cult threshold scale, collision, LODs, sockets, and startup placement | Final art replacement, VFX states, gate behavior Blueprint |
| `VFX_INF_AbyssalSpellcasting_A01` | First-pass material/Niagara review assets complete and validated | Shared Infernal spell/VFX names and socket-facing contract | Final bespoke Niagara graph art or final combat readability tuning |
| `ANIMATION_HANDOFF.md` | Approved animation direction | Claw, wing, tail, rage, regeneration, invisible-sight motion rules | Final authored animation assets, montage timing, gameplay authority |

## Package-Ready / Deferred Before DCC Or Unreal

| Item | Status | Next allowed step | Gate before implementation |
| --- | --- | --- | --- |
| `MI_INF_CultStone_Set_A01` | Production package ready | Select for material authoring task | Stop before final shader polish, texture production, or Unreal material import without task ownership |
| `SM_INF_BalgorothSigil_A01` | Production package ready | Select for DCC modeling-prep task | Stop before DCC/Unreal build until selected in task order |
| `SM_INF_BrandingStone_A01` | Package needed | Create production package next if selected | Stop before DCC/Unreal and before changing Balgoroth symbol/material identity |
| `VFX_INF_RegenerationBrand_A01` | Package needed | Create after BrandingStone package | Stop before authored Niagara or gameplay healing/regeneration rules |
| `SM_INF_AshBasin_A01` | Package needed | Create after material/sigil rules are locked | Stop before VFX density or final prop set dressing pass |
| `SM_INF_WitnessChains_A01` | Package needed | Create after material/sigil rules are locked | Stop before gameplay restraint/collision behavior |
| `SM_INF_TrialBanner_A01` | Package needed | Create after symbol package | Stop before cloth animation or final banner variants |

## Fresh Approval Required Before Work Starts

| Item | Why approval is required | Current blocker |
| --- | --- | --- |
| `BP_INF_CultGate_A01` | Adds behavior states to the already-covered HornWingArch visual language | Needs explicit behavior approval for inactive, guarded, locked, trial-open, and rejected-snap states |
| `KIT_INF_LesserTrialDen_A01` | Expands from current child props into a new environment mini-kit | Needs approval for den scope, Spawn-scale staging, and encounter use |
| `VFX_INF_WorthinessJudgment_A01` final bespoke graph | Current assets are contract-ready but still `GraphStatus=template_derived_contract_ready` and `FinalGraphAuthored=false` | Needs manual Niagara graph art pass and visual approval before final-art claim |
| Infernal starter animation imports | Current task created implementation readiness only | Needs approval for final animation source authoring, montage timing, combat pace, and root-motion rules |
| `BP_INF_RitualAltar_A01` quest/audio/UI runtime binding | Current task created the integration packet only | Needs approval for final quest copy, rewards, backend authority, telemetry schema, audio middleware, and UI art |

## Current Package Links

- `docs/assets/characters/SK_INF_Mage_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Mage_A01/BUILD_IMPORT_STATUS.md`
- `docs/assets/characters/SK_INF_Warrior_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Warrior_A01/BUILD_IMPORT_STATUS.md`
- `docs/assets/characters/SK_INF_Rogue_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Rogue_A01/BUILD_IMPORT_STATUS.md`
- `docs/assets/characters/SK_INF_Hunter_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_INF_Hunter_A01/BUILD_IMPORT_STATUS.md`
- `docs/assets/characters/INFERNAL_STARTER_CLASS_MATRIX.md`
- `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`
- `docs/assets/characters/SK_INF_Base_A01/ANIMATION_IMPLEMENTATION_READINESS.md`
- `docs/assets/props/SM_INF_HornWingArch_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_INF_HornWingArch_A01/BUILD_IMPORT_STATUS.md`
- `docs/assets/materials/MI_INF_CultStone_Set_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_INF_BalgorothSigil_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_INF_BalgorothCult_A01/REMAINING_CHILD_PACKAGE_INTAKE.md`
- `docs/assets/blueprints/BP_INF_RitualAltar_A01/GAMEPLAY_INTEGRATION_PACKET.md`
- `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/BUILD_IMPORT_STATUS.md`
