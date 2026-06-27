# VFX_GNM_AetherShieldWall_A01 Niagara Art Pass Handoff

## Purpose

Author the final Niagara shield-wall effect for `BP_GNM_HeavyMekShieldwall_A01` using the existing shieldwall state and parameter contract. This handoff defines the final art behavior, emitters, user parameters, LOD rules, and required native/Blueprint hook. It does not claim the Unreal Niagara asset already exists.

## Current Contract

Existing native actor: `AAETHeavyMekShieldwallActor`

Current exposed controls:

- `ShieldState`
- `ShieldWidthCm`
- `ProjectorCount`
- `ArcHeightCm`
- `ImpactIntensity`
- `OverloadPercent`
- `ImpactLocationNormalized`
- `ImpactLocator`
- `ShieldIdleMaterial`
- `ShieldImpactMaterial`
- `ShieldFailingMaterial`

Current implementation pushes scalar parameters to shield helper panels and projector materials, owns a native `UNiagaraComponent` named `ShieldNiagara`, exposes `ShieldNiagaraSystem`, and assigns `/Game/Aerathea/VFX/GnomeOgre/NS_GNM_AetherShieldWall_A01`. `Source/Aerathea/Aerathea.Build.cs` already includes the `Niagara` module dependency.

Current native Niagara parameters pushed by `AAETHeavyMekShieldwallActor`:

- `User.ShieldState`
- `User.ShieldWidthCm`
- `User.ArcHeightCm`
- `User.ProjectorCount`
- `User.ImpactIntensity`
- `User.OverloadPercent`
- `User.ImpactLocationNormalized`
- `User.bFailing`
- `User.bOverloaded`
- `User.ImpactWorldLocation`
- `User.EdgeColor`
- `User.FillColor`

## Final Niagara Target

- Niagara system: `NS_GNM_AetherShieldWall_A01`
- Unreal folder: `/Game/Aerathea/VFX/GnomeOgre/`
- Blueprint/native consumer: `BP_GNM_HeavyMekShieldwall_A01` / `AAETHeavyMekShieldwallActor`
- Optional helper mesh fallback: `SM_GNM_AetherShieldWall_A01`
- Current first-pass emitter targets: `NE_GNM_ShieldEdgeBands_A01`, `NE_GNM_ShieldSurfacePulse_A01`, `NE_GNM_ShieldImpactRipple_A01`, `NE_GNM_ShieldOverloadSparks_A01`, and `NE_GNM_ShieldFailingFragments_A01`

## Visual Direction

- Clean segmented crescent shield, not a flat rectangle.
- Blue Aetherium edge bands remain the primary read.
- Transparent fill stays restrained and never hides the Ogre silhouettes behind it.
- Localized impact ripples originate from `ImpactLocator` or `ImpactLocationNormalized`.
- Overload should look unstable but controlled: sharper pulses, sparse blue-white sparks, and edge distortion.
- Failing should break segment continuity and lose energy from the impacted panels.
- Shutdown should collapse back toward projector sockets.

Avoid heavy full-screen bloom, constant dense particles, orange Ogre glow, necromantic green, and noisy tiny spark storms.

## Emitter Plan

| Emitter | Purpose | Notes |
| --- | --- | --- |
| `NE_GNM_ShieldEdgeBands_A01` | Primary crescent edge/ribbon read | Always last emitter to disable by distance |
| `NE_GNM_ShieldSurfacePulse_A01` | Soft transparent segmented fill and slow pulse | Low opacity, low overdraw |
| `NE_GNM_ShieldImpactRipple_A01` | Localized rings or wavefront from hit point | Driven by `ImpactIntensity` and hit location |
| `NE_GNM_ShieldOverloadSparks_A01` | Sparse blue-white crackle during overload | Disable early by distance |
| `NE_GNM_ShieldFailingFragments_A01` | Broken segment flecks and flicker | Active only in `Failing` |
| `NE_GNM_ShieldShutdownCollapse_A01` | Collapse/fade toward projector sockets | Short burst only |

## Niagara User Parameters

- `User.ShieldState` as int or enum-mapped float.
- `User.ShieldWidthCm`
- `User.ArcHeightCm`
- `User.ProjectorCount`
- `User.ImpactIntensity`
- `User.OverloadPercent`
- `User.ImpactLocationNormalized`
- `User.ImpactWorldLocation`
- `User.EdgeColor`
- `User.FillColor`
- `User.bFailing`
- `User.bOverloaded`

Parameter mapping:

- `ImpactIntensity` controls ripple brightness, ring count, and impact lifetime.
- `OverloadPercent` controls edge flicker, spark rate, distortion strength, and warning pulse.
- `ImpactLocationNormalized` maps across the shield width from -1 to 1.
- `ImpactWorldLocation` should use `ImpactLocator` when available.
- `ShieldState` gates emitters and state transitions.

## State Behavior

| Shield state | Niagara behavior |
| --- | --- |
| `Inactive` | Niagara hidden or inactive, projector cores dim |
| `Booting` | Edge bands connect from projectors, fill fades in |
| `Braced` | Stable edge bands, low-frequency fill pulse |
| `Impact` | Localized ripple, short impact flash, nearest edge response |
| `Overload` | Faster edge flicker, sparse sparks, mild distortion |
| `Failing` | Broken segments, intermittent fill loss, unstable edge gaps |
| `Shutdown` | Energy collapses toward projectors and fades |

## Native Hook Status

Implemented native path:

1. `Niagara` is included in `Source/Aerathea/Aerathea.Build.cs`.
2. `UNiagaraComponent* ShieldNiagara` exists on `AAETHeavyMekShieldwallActor`.
3. `UNiagaraSystem* ShieldNiagaraSystem` is exposed and assigned.
4. The Niagara component is attached to `SceneRoot`.
5. `UpdateShieldwallLayout` positions and scales the component to the shield wall.
6. `ApplyShieldState` pushes the documented Niagara user parameters alongside existing material parameter updates.
7. Helper panels remain available as the visible fallback and low-end LOD until the bespoke Niagara graph is validated.

## Texture And Material Requirements

Recommended textures:

- `T_GNM_AetherShieldWall_A01_RippleMask`
- `T_GNM_AetherShieldWall_A01_EdgeMask`
- `T_GNM_AetherShieldWall_A01_Noise`
- `T_GNM_AetherShieldWall_A01_Distortion`

Recommended materials:

- `M_GNM_AetherShieldWall_Niagara_Edge_A01`
- `M_GNM_AetherShieldWall_Niagara_Fill_A01`
- `M_GNM_AetherShieldWall_Niagara_Impact_A01`
- `MI_GNM_AetherShieldWall_A01_Niagara_Idle`
- `MI_GNM_AetherShieldWall_A01_Niagara_Impact`
- `MI_GNM_AetherShieldWall_A01_Niagara_Failing`

Keep emissive intensity restrained and configurable. Avoid dynamic lights by default.

## Performance Budget

- Keep total near-camera particles/ribbon elements modest enough for an MMO encounter with several characters onscreen.
- Disable overload sparks first at distance.
- Reduce fill pulse frequency and alpha at medium distance.
- Keep edge bands as the final far-distance read.
- Avoid collision events, GPU readbacks, and expensive simulation stages unless later justified.
- No per-particle lights.

## Validation Requirements

Before presenting a final Niagara visual approval:

1. Validate shieldwall actor still exposes material/state contract.
2. Confirm Niagara consumes `ImpactIntensity`, `OverloadPercent`, and `ImpactLocationNormalized`.
3. Trigger `Braced`, `Impact`, `Overload`, `Failing`, and `Shutdown` states in editor or review map.
4. Capture at startup review camera and confirm it does not obscure Ogre/Gnome silhouettes.
5. Check mobile/low scalability settings or a low-VFX fallback if applicable.

## Acceptance Checklist

- Final effect reads as Gnome/Mekgineer blue Aetherium, not Ogre Tek or necromancy.
- Segmented crescent silhouette remains readable.
- Impact ripple is localized and parameter-driven.
- Overload/failing states are distinct but restrained.
- The helper mesh can remain as fallback without conflicting with Niagara.
- Native or Blueprint hook is defined before claiming the Niagara asset is implemented.
