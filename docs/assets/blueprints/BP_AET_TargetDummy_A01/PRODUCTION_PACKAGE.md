# BP_AET_TargetDummy_A01 Production Package

## Art Direction Summary

- Asset name: `BP_AET_TargetDummy_A01`
- Asset type: Blueprint Actor / native-backed training prop
- Native class: `AAETTargetDummyActor`
- Static mesh dependency: `SM_AET_TargetDummy_A01`
- World: Aerathea
- Current status: Native gameplay class implemented; Blueprint asset created/compiled; startup actor replaced with the Blueprint; validation passing

This Blueprint wraps the imported target dummy static mesh with safe training behavior: damage intake, hit reaction events, break/reset state, and score-style callbacks. It does not own the final combat system.

## Gameplay Purpose

Supports early combat, damage, ability, hit-reaction, and training-yard tests without binding Aerathea to final combat math. The actor gives designers a stable target for:

- Melee/ranged/spell damage experiments.
- Hit feedback and audio cue hooks.
- Floating damage number prototypes.
- Training score events.
- Resettable tutorial or practice-yard targets.

## Silhouette Notes

The Blueprint preserves `SM_AET_TargetDummy_A01` exactly. Do not add large visible components that change the dummy silhouette. Feedback should come from small wobble, material flash, sound, or UI events.

## Scale Notes

- Uses `SM_AET_TargetDummy_A01` at 1.0 scale.
- Total static mesh target height: 185 cm.
- Pivot: bottom center at ground contact.
- Hit volume target: centered around the torso and front hit plate.

## Materials And Color Palette

Use the static mesh material plan from `SM_AET_TargetDummy_A01`: timber, straw, leather, dark iron, painted target marks, and restrained non-emissive blue scoring marks. Any runtime feedback should be subtle and temporary.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of an interactive training target dummy Blueprint for the world of Aerathea. The design should emphasize a rugged timber-and-straw target dummy, clear hit zones, subtle hit feedback states, practical starter-town training-yard identity, readable MMO silhouette, and safe combat-testing gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing non-emissive blue score marks, and MMO-friendly production design. Present it as a small state sheet showing idle, hit reaction, broken, and reset-ready states on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

No new mesh modeling is required for the Blueprint. The actor uses `SM_AET_TargetDummy_A01`. Optional future visual pieces, such as a score sign or training marker, should be separate props and not baked into the dummy.

## Texture And Material Notes

- Uses `MI_AET_TargetDummy_A01`.
- Optional runtime material flash should use dynamic material parameters on the existing material instance.
- Do not create an emissive-heavy damage state unless combat readability testing proves it is needed.

## Triangle Budget

The Blueprint mesh budget is the static mesh budget:

- LOD0: 2.5k-3.5k tris.
- LOD1: 1.4k-1.8k tris.
- LOD2: 600-900 tris.
- LOD3: 180-300 tris.

Blueprint components should add no visible mesh cost.

## LOD Plan

Use the LODs from `SM_AET_TargetDummy_A01`. Runtime feedback must not depend on geometry that disappears at medium range.

## Collision Notes

- `DummyMesh`: blocks pawn/world using imported or generated simple collision.
- `HitVolume`: query-only torso/front-plate volume for traces and test overlap behavior.
- Do not use complex-as-simple collision.
- Final projectile and ability collision remains combat-system owned.

## Animation Notes

Native class supports hit-reaction begin/end events. Blueprint may add:

- Small timeline wobble.
- Material flash.
- Impact sound.
- Floating damage number event.
- Reset visual cue.

No skeletal animation is required.

## Unreal Import Notes

- Blueprint path: `/Game/Aerathea/Blueprints/Props/BP_AET_TargetDummy_A01`
- Parent class: `AAETTargetDummyActor`
- Static mesh dependency: `/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01`
- Recommended startup actor label: `AET_PROD_TargetDummy_A01`
- Blueprint asset has been created, compiled, and placed as `AET_PROD_TargetDummy_A01` in the startup scene.

## Folder And Naming Recommendation

- Docs: `docs/assets/blueprints/BP_AET_TargetDummy_A01/`
- Unreal Blueprint: `/Game/Aerathea/Blueprints/Props/BP_AET_TargetDummy_A01`
- Native class files:
  - `Source/Aerathea/Public/AETTargetDummyActor.h`
  - `Source/Aerathea/Private/AETTargetDummyActor.cpp`

## Quality Gate Checklist

- Uses the production target dummy mesh.
- Receives test damage without final combat-system assumptions.
- Broadcasts hit, broken, reset, and reaction events for Blueprint/UI/audio hooks.
- Auto-reset behavior is optional and tunable.
- Collision stays simple and runtime safe.
- No permanent quest, inventory, progression, or combat balance side effects.
- Startup map validation remains clean after placement.
