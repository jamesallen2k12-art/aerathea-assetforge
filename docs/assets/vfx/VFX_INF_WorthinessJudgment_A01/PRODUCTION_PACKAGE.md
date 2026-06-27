# VFX_INF_WorthinessJudgment_A01 Production Package

## Art Direction Summary

`VFX_INF_WorthinessJudgment_A01` defines the restrained ritual VFX for Infernal worthiness trials, Balgoroth cult altars, culling floors, accepted/rejected sacrifice states, and Lesser Infernal blooding scenes.

The effect should feel severe and judgmental: ember channels brighten, a horned/split-wing sigil pulses once, ash motes rise, and a violet-red rejection pulse snaps through the broken circle when the offering or target is unworthy. It must not become constant screen-filling fire.

## Gameplay Purpose

- Provides shared VFX states for `SM_INF_CullingTrialFloor_A01`, future `SM_INF_WorthinessAltar_A01`, and `BP_INF_RitualAltar_A01`.
- Supports trial start, accepted, rejected, regeneration, and culling-temper feedback.
- Gives combat designers a readable ritual-state tell without requiring gore.

## Silhouette Notes

- Primary read is the ring and central sigil, not smoke volume.
- Effects should follow floor channels and sockets, then climb briefly at altar/brand points.
- Rejection should fracture through the broken-circle mark with a short violet-red snap.
- Accepted should be a controlled ember concentration, not a victory explosion.

## Scale Notes

- Floor radius support: 800-1000 cm assembled trial floor.
- Vertical effect height: 80-220 cm for floor-only states, 260-420 cm when attached to altar.
- Must read beside Spawn through 9' adult Infernal scale without hiding character silhouettes.

## Materials And Color Palette

- Ember orange and deep red for normal ritual states.
- Restrained violet-red for rejected/unworthy pulse.
- Ash gray and smoke-brown for short motes.
- No blue Aetherium, no Ogre green necromancy, no heavy white-hot fire bloom.

## Concept Image Prompt

Create an original stylized fantasy MMORPG VFX state sheet of `VFX_INF_WorthinessJudgment_A01` for the Infernals of Aerathea. The design should emphasize Balgoroth cult worthiness judgment, a black basalt culling trial floor, ember-orange ring channels, horned crown and split-wing sigil pulse, accepted warm ember focus, rejected violet-red broken-circle snap, ash motes, restrained smoke wisps, and MMO-friendly readable VFX. Use hand-painted texture detail, readable shapes, baked-AO-style depth, sparing emissive accents, and production-friendly particle density. Present it as a clean VFX board with inactive, smolder, trial active, accepted, rejected, and cooldown frames plus socket callouts for floor and altar use. Avoid copied franchise symbols, gore, excessive particles, full-screen bloom, readable text, watermarks, and photoreal fire simulation.

## Modeling Notes

- VFX attaches to sockets rather than requiring new mesh geometry.
- Use `SM_INF_CullingTrialFloor_A01` sockets: `vfx_center`, `vfx_ring_active`, and `vfx_rejected_gap`.
- Future altar sockets should include `vfx_altar_core`, `vfx_sacrifice_mark`, and `vfx_brand_transfer`.

## Texture And Material Notes

Texture targets:

- `T_INF_WorthinessRing_A01_E`
- `T_INF_WorthinessSigil_A01_E`
- `T_INF_AshMote_A01_BC`
- `T_INF_VioletRejection_A01_E`

Material instances:

- `MI_INF_WorthinessRing_A01`
- `MI_INF_WorthinessSigil_A01`
- `MI_INF_WorthinessAsh_A01`
- `MI_INF_WorthinessRejected_A01`

Niagara parameters:

- `State`
- `RingRadiusCm`
- `PulseIntensity`
- `PulseDuration`
- `AcceptedFocus`
- `RejectedGapLocation`
- `AshDensity`

## Triangle Budget

No static triangle cost beyond optional low-poly ribbon/plane helpers. Keep any helper mesh under 300 tris and reuse it across ring/sigil states.

## LOD Plan

- VFX LOD0: ring pulse, sigil pulse, ash motes, accepted/rejected event burst.
- VFX LOD1: reduce ash density and ripple subdivisions.
- VFX LOD2: keep only ring/sigil emissive pulse and one event sprite.
- VFX LOD3: disable particles, keep material parameter glow on the floor or altar.

## Collision Notes

No collision. Gameplay volumes belong to future ritual Blueprint logic.

## Animation Notes

- `Inactive`: no particles, material glow nearly zero.
- `Smolder`: low ember ring flicker.
- `TrialActive`: ring pulse every 2-4 seconds, center sigil low pulse.
- `Accepted`: one warm pulse from ring to center, then stable ember core.
- `Rejected`: one short violet-red crack through the broken gap, then quick fade.
- `Cooldown`: ash motes and dim ember only.

## Unreal Import Notes

- Asset type: Niagara/VFX plus Material Instances.
- Folder path: `/Game/Aerathea/VFX/Infernals/VFX_INF_WorthinessJudgment_A01`
- Blueprint consumer: future `/Game/Aerathea/Blueprints/Infernals/BP_INF_RitualAltar_A01`
- Mesh/socket consumer: `/Game/Aerathea/Props/Infernals/BalgorothCult/SM_INF_CullingTrialFloor_A01`
- Expose `State` and intensity parameters to Blueprint.
- Use fixed bounds sized to the floor/altar variant to avoid culling artifacts.

## Folder And Naming Recommendation

- Package folder: `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/`
- Unreal VFX folder: `/Game/Aerathea/VFX/Infernals/`
- Unreal material folder: `/Game/Aerathea/Materials/Infernals/`
- Related material package: `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`

## Quality Gate Checklist

- The effect supports worthiness judgment without gore.
- Ember/violet colors match Infernal material rules.
- Particle count and bloom remain restrained.
- Floor and altar sockets are named and usable.
- LOD behavior, texture maps, material instances, Blueprint parameters, and Unreal paths are defined.
