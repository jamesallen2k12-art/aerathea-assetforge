# BP_AET_TargetDummy_A01 Implementation Handoff

## Purpose

Create the first resettable combat-test target for `L_Aerathea_Startup` by wrapping `SM_AET_TargetDummy_A01` with the native `AAETTargetDummyActor` class.

## Source References

- Blueprint package: `docs/assets/blueprints/BP_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md`
- Static mesh package: `docs/assets/props/SM_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md`
- Native class:
  - `Source/Aerathea/Public/AETTargetDummyActor.h`
  - `Source/Aerathea/Private/AETTargetDummyActor.cpp`

## Production Target

- Blueprint asset: `BP_AET_TargetDummy_A01`
- Unreal path: `/Game/Aerathea/Blueprints/Props/BP_AET_TargetDummy_A01`
- Parent class: `AAETTargetDummyActor`
- Static mesh: `/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01`
- Current status: Blueprint asset created and compiled; startup actor replaced with `BP_AET_TargetDummy_A01`; validation passing.

## Required Behavior

- Use `TakeDamage` and `RegisterTrainingHit` for controlled test hits.
- Track `MaxTrainingHealth` and `CurrentTrainingHealth`.
- Broadcast `OnTrainingHit`, `OnTrainingBroken`, `OnTrainingReset`, and `OnHitReactionStateChanged`.
- Auto-reset after break only when `bAutoResetAfterBreak` is true.
- Never mutate quests, inventory, progression, or final combat state.

## Blueprint Components

Native components:

- `SceneRoot`
- `DummyMesh`
- `HitVolume`

Blueprint additions are optional:

- Timeline wobble on hit.
- Floating damage number event relay.
- Audio component for impact cues.
- Editor-only debug billboard.

## Validation Steps

1. Compile the native module.
2. Create or reparent `BP_AET_TargetDummy_A01` to `AAETTargetDummyActor`. Complete.
3. Confirm `DummyMesh` resolves to `SM_AET_TargetDummy_A01`.
4. Confirm hit volume covers torso/front target plate.
5. In PIE, apply test damage and verify hit/reaction/break/reset events.
6. Replace the startup static mesh actor only after Blueprint compile and collision checks pass. Complete.

## Acceptance Checklist

- Blueprint compiles without warnings.
- Static mesh scale and collision match the original startup prop.
- Damage intake returns score-style values for testing.
- Hit reaction events do not require final animation systems.
- Auto-reset works and can be disabled.
- Startup scene remains readable and validation passes.
