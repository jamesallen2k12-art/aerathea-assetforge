# VFX_GNM_AetherShieldWall_A01 Build And Import Status

## Current Status

- Review helper status: implemented as static helper panels, material state instances, and native parameter contract.
- Final Niagara art-pass status: handoff ready.
- Unreal Niagara status: `NS_GNM_AetherShieldWall_A01` not authored.
- Native Niagara hook status: implemented in `AAETHeavyMekShieldwallActor`; helper panels remain the visible fallback until an authored Niagara system exists.

## Existing Unreal Assets

- `/Game/Aerathea/VFX/GnomeOgre/VFX_GNM_AetherShieldWall_A01`
- `/Game/Aerathea/VFX/GnomeOgre/SM_GNM_AetherShieldWall_A01`
- `/Game/Aerathea/Materials/M_GNM_AetherShieldWall_Review_A01`
- `/Game/Aerathea/Materials/Instances/MI_GNM_AetherShieldWall_A01_Idle`
- `/Game/Aerathea/Materials/Instances/MI_GNM_AetherShieldWall_A01_Impact`
- `/Game/Aerathea/Materials/Instances/MI_GNM_AetherShieldWall_A01_Failing`

## Planned Final Niagara Assets

- `/Game/Aerathea/VFX/GnomeOgre/NS_GNM_AetherShieldWall_A01`
- `/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldEdgeBands_A01`
- `/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldSurfacePulse_A01`
- `/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldImpactRipple_A01`
- `/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldOverloadSparks_A01`
- `/Game/Aerathea/VFX/GnomeOgre/NE_GNM_ShieldFailingFragments_A01`

## Completed Prerequisites

- Production package: `docs/assets/vfx/VFX_GNM_AetherShieldWall_A01/PRODUCTION_PACKAGE.md`
- Niagara art-pass handoff: `docs/assets/vfx/VFX_GNM_AetherShieldWall_A01/NIAGARA_ART_PASS_HANDOFF.md`
- Blueprint/native consumer package: `docs/assets/blueprints/BP_GNM_HeavyMekShieldwall_A01/PRODUCTION_PACKAGE.md`
- Native material/state contract: `AAETHeavyMekShieldwallActor`
- Native Niagara hook: `UNiagaraComponent` on `AAETHeavyMekShieldwallActor`
- Module dependency: `Niagara` added to `Source/Aerathea/Aerathea.Build.cs`
- Project plugin: `Niagara` enabled in `Aerathea.uproject`
- Startup validation checks the current material/scalar parameter contract.

## Blocking Items

- Final Niagara system is not authored in Unreal.
- Final VFX visual approval must happen after the actual Niagara asset exists and is captured from the review camera.

## Remaining To Finalize

1. Author `NS_GNM_AetherShieldWall_A01` and its emitters in Unreal.
2. Bind the authored system to the existing `User.*` shieldwall state/impact/overload parameters.
3. Add validation for the Niagara component once the system asset exists.
4. Validate startup capture and performance before marking the final art pass visually complete.
