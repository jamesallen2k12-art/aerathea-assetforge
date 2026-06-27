# BP_GNM_HeavyMekShieldwall_A01 Implementation Handoff

## Purpose

Create the first reusable Gnome-vs-Ogre encounter child as a Blueprint Actor that assembles Mekgineer shield projectors and blue Aetherium shield VFX into a tactical defensive wall.

## Source References

- Kit package: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/CHILD_ASSET_INTAKE.md`
- Production package: `docs/assets/blueprints/BP_GNM_HeavyMekShieldwall_A01/PRODUCTION_PACKAGE.md`
- Related Gnome/Mek anchor: `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md`

## Blueprint Components

| Component | Type | Notes |
| --- | --- | --- |
| `Root` | Scene Component | ground center of shield-wall arc |
| `Projector_01..05` | Static Mesh Component | optional slots; hide unused projectors by `ProjectorCount` |
| `ShieldSpline` | Spline Component | defines arc between emitters |
| `ShieldVFX` | Niagara or VFX Component | idle, impact, overload, and failing states |
| `ShieldCollision` | Box or custom volume | disabled by default; enabled by gameplay state |
| `ImpactLocator` | Scene Component | temporary hit response position |
| `AudioShieldLoop` | Audio Component | optional hum loop |

## State Contract

| State | Visual | Gameplay |
| --- | --- | --- |
| `Inactive` | cores dark, projectors idle | no collision, no mitigation |
| `Booting` | cores brighten, shield segments connect | collision off or partial |
| `Braced` | stable blue arc, low pulse | optional projectile blocking |
| `Impact` | localized ripple and spark | mitigation or reflected-hit event |
| `Overload` | stronger core pulse, unstable ripple | warning state |
| `Failing` | broken shield segments | collision disabled after delay |
| `Shutdown` | arc collapses to projectors | cleanup state |

## Required Projector Sockets

- `vfx_core`
- `vfx_shield_emit_l`
- `vfx_shield_emit_r`
- `attach_mek_l`
- `attach_mek_r`
- `damage_spark`

## Data Parameters

- `ShieldWidthCm`: default 700
- `ArcHeightCm`: default 340
- `ProjectorCount`: default 3, valid 3-5
- `ShieldState`: enum listed above
- `ImpactIntensity`: 0.0-1.0
- `OverloadPercent`: 0.0-1.0
- `ImpactLocationNormalized`: -1.0 to 1.0 across the shield width
- `ShieldIdleMaterial`: idle/braced helper-panel material
- `ShieldImpactMaterial`: impact/overload helper-panel material
- `ShieldFailingMaterial`: failing helper-panel material

## Blueprint Callable Functions

- `SetShieldState`
- `SetImpactIntensity`
- `SetOverloadPercent`
- `SetImpactLocationNormalized`
- `TriggerImpact`
- `ConfigureShieldwall`

## Native VFX Contract

- The native actor assigns idle, impact, and failing materials by shield state.
- The native actor moves `ImpactLocator` from `ImpactLocationNormalized` and current shield width.
- The native actor pushes `ImpactIntensity`, `OverloadPercent`, and `ImpactLocationNormalized` scalar parameters onto shield panels and projectors.
- Final Niagara should consume the same state and parameter names rather than inventing a parallel contract.
- `bBlocksProjectiles`: default true
- `bBlocksPawns`: default false

## Validation Checklist

- Blueprint compiles with no missing dependencies.
- Projector sockets exist before VFX binding.
- Projector count changes do not move the Blueprint pivot.
- Shield VFX remains visible from gameplay camera distance but does not overwhelm the scene.
- Collision state is disabled in `Inactive`, `Failing`, and `Shutdown`.
- Heavy Mek socket attachment remains optional, so the package can be reviewed before final Mek skeletal work.
- Material state bindings and impact parameter ranges are covered by `Tools/Unreal/validate_startup_scene.py`.
