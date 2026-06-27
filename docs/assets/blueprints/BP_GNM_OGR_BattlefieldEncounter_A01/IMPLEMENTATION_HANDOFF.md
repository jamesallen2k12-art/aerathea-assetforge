# BP_GNM_OGR_BattlefieldEncounter_A01 Implementation Handoff

## Purpose

Implement a reusable Blueprint encounter coordinator for the Gnome/Ogre rivalry kit. The actor should assemble or reference child actors, validate dependencies, expose phase controls, and trigger review-safe VFX events without final combat AI.

## Source References

- Production package: `docs/assets/blueprints/BP_GNM_OGR_BattlefieldEncounter_A01/PRODUCTION_PACKAGE.md`
- Rivalry kit: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/CHILD_ASSET_INTAKE.md`
- Shieldwall package: `docs/assets/blueprints/BP_GNM_HeavyMekShieldwall_A01/PRODUCTION_PACKAGE.md`
- Ogre Teknomancy kit: `docs/assets/kits/KIT_OGR_Teknomancy_A01/PRODUCTION_PACKAGE.md`

## Dependency Status

| Dependency | Current state | Encounter use |
| --- | --- | --- |
| `BP_GNM_HeavyMekShieldwall_A01` | First-pass Blueprint/VFX contract implemented | Required primary defensive line |
| `SK_GNM_HeavyMek_Rivalry_A01` | First-pass DCC/Unreal import complete | Required Gnome side anchor |
| `SK_OGR_Teknomancer_A01` | First-pass DCC/Unreal import complete | Required Ogre magic-tech pressure unit |
| `SK_OGR_Warrior_Rival_A01` | First-pass DCC/Unreal import complete | Required Ogre melee pressure unit |
| `SM_OGR_CairnBattleGate_A01` | First-pass DCC/Unreal import complete | Required Ogre background/frame prop |
| `SM_OGR_CrudeTekPylon_A01` | First-pass DCC/Unreal import complete; native pylon wrapper exists | Optional pylon objective slot |
| `SK_OGR_Shaman_A01` | First-pass DCC/Unreal import complete | Optional caster reinforcement slot |
| `SK_OGR_Necromancer_A01` | First-pass DCC/Unreal import complete | Optional caster reinforcement slot |
| `SK_CRE_Manticore_A01` | First-pass DCC/Unreal import complete | Base dependency for optional creature branch |
| `SK_CRE_Manticore_Interrupt_A01` | First-pass DCC/Unreal import complete; native interrupt wrapper exists | Optional Manticore branch |

## Implementation Target

- Blueprint: `/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_OGR_BattlefieldEncounter_A01`
- Editor label: `AET_PROD_GNM_OGR_BattlefieldEncounter_A01`
- Map placement: complete in `L_Aerathea_Startup` with required and branch actors assigned.
- Root pivot: encounter center.

## Component Plan

Core components:

- `DefaultSceneRoot`
- `EncounterBounds` BoxComponent, non-blocking.
- `GnomeLineMarker` SceneComponent.
- `OgreLineMarker` SceneComponent.
- `GateMarker` SceneComponent.
- `PylonMarker` SceneComponent.
- `ManticoreEntryMarker` SceneComponent.
- `GnomeLineTrigger` BoxComponent, disabled by default.
- `OgreAdvanceTrigger` BoxComponent, disabled by default.
- `PylonObjectiveVolume` BoxComponent, disabled by default.
- `ManticoreInterruptVolume` BoxComponent, disabled by default.

Child actor references or soft references:

- `ShieldwallActor`
- `GnomeHeavyMekActor`
- `OgreTeknomancerActor`
- `OgreWarriorActor`
- `CairnGateActor`
- `CrudeTekPylonActor`
- `OgreShamanActor`
- `OgreNecromancerActor`
- `ManticoreInterruptActor`

## Blueprint Variables

- `EncounterState`: enum or name, default `Setup`.
- `bAutoStart`: false by default.
- `bUsePlacedActors`: true by default for review scenes.
- `bEnablePylonObjective`: false until pylon import.
- `bEnableCasterReinforcements`: false until Shaman/Necromancer import.
- `bEnableManticoreInterrupt`: false until Manticore import.
- `bLoopForReview`: false by default.
- `EncounterWidthCm`: default 2800.
- `EncounterDepthCm`: default 2200.
- `ShieldImpactLocationNormalized`: default 0.5.
- `PylonOverloadPercent`: default 0.0.
- `PhaseDurationSeconds`: optional array/map for review sequencing.

Use soft object/class references for optional dependencies. Required dependencies can be actor references when using placed review actors.

## Blueprint Functions And Events

- `ValidateDependencies`: checks required actor refs/classes and logs optional missing dependencies without failing.
- `ConfigureEncounter`: positions or validates actor slots from marker transforms.
- `SetEncounterState(NewState)`: central state change function.
- `TriggerShieldImpact(ImpactLocationNormalized, ImpactIntensity)`: forwards values to `BP_GNM_HeavyMekShieldwall_A01`.
- `TriggerPylonOverload(OverloadPercent)`: disabled-safe event for future pylon Blueprint/material VFX.
- `TriggerCasterReinforcement(CasterType)`: disabled-safe event for future Shaman/Necromancer actors.
- `TriggerManticoreInterrupt`: disabled-safe event for future creature branch.
- `ResetEncounter`: returns child actors and VFX to idle review state.
- `OnEncounterPhaseChanged`: BlueprintAssignable event for later UI/debug/audio hooks.

## Phase State Contract

| State | Required dependencies | Behavior |
| --- | --- | --- |
| `Setup` | root only | Validate refs, hide missing optional slots, idle all VFX |
| `GnomeHoldLine` | shieldwall, heavy Mek | Shieldwall active, Mek braced |
| `OgreAdvance` | Ogre Teknomancer, Ogre Warrior | Ogre pressure actors enabled or highlighted |
| `ShieldImpact` | shieldwall | Trigger shieldwall impact parameters |
| `PylonOverload` | optional pylon | If pylon exists, pulse forge-orange core and anti-Mek arc sockets |
| `CasterReinforcement` | optional Shaman/Necromancer | Enable caster markers or actors if imported |
| `ManticoreInterrupt` | optional Manticore | Trigger side/background entry only if imported |
| `Resolution` | required actors | Shutdown, loop, or reset for review |

Missing optional actors must skip cleanly.

## Implementation Constraints

- Do not implement final combat AI in this Blueprint.
- Do not hard-code quest, loot, or persistence rules.
- Do not spawn placeholder meshes for missing optional dependencies.
- Keep event graph readable; move repeated state handling into functions or a native class later.
- Use editor categories for dependency references, phase controls, debug/review, and optional branches.

## Validation Plan

Before placing in the startup scene:

1. Required dependencies resolve or are assigned as placed actors.
2. Optional dependencies are disabled by default.
3. `ValidateDependencies` reports missing optional assets as warnings/log notes only.
4. `TriggerShieldImpact` drives the existing shieldwall contract.
5. Encounter bounds and marker transforms are visible in editor but non-blocking in runtime review.

After Unreal implementation:

- Add `AET_PROD_GNM_OGR_BattlefieldEncounter_A01` to `Tools/Unreal/validate_startup_scene.py` only if the actor is placed in `L_Aerathea_Startup`.
- Validate that optional disabled branches do not fail startup checks.
- Use `Tools/Unreal/validate_gnome_ogre_encounter_phase_sequence.py` after C++ or Blueprint phase edits.
- Use `Tools/Unreal/capture_gnome_ogre_phase_reviews.sh` for shield impact, pylon overload, caster reinforcement, and Manticore interrupt review frames.
- Keep capture orientation rules from `AGENTS.md` before presenting any visual approval.

## Acceptance Checklist

- Blueprint can coordinate required imported Gnome/Ogre actors.
- Optional pylon, caster, and Manticore branches are dependency-gated.
- Shieldwall impact and overload parameters are forwarded rather than duplicated.
- No final combat/quest rules are locked prematurely.
- The implementation supports review staging and future gameplay expansion.
