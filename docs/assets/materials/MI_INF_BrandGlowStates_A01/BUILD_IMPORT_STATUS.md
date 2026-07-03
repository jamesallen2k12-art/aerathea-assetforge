# MI_INF_BrandGlowStates_A01 Build And Import Status

## Current State

First-pass Unreal material-state authoring is complete for the shared Infernal brand glow package.

This pass is not final shader art. It validates stable shared asset names, a master material, a material-function placeholder, six gameplay-state material instances, and the starter-class socket contract that will drive brand, eye, rage, pursuit, and sorcerer-focus glow later.

## Unreal Assets

- Master material: `/Game/Aerathea/Materials/Infernals/M_INF_BrandGlow_Master_A01`
- Material function placeholder: `/Game/Aerathea/Materials/Infernals/MF_INF_BrandGlowStates_A01`
- State instances:
  - `/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Inactive`
  - `/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Smolder`
  - `/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_TrialActive`
  - `/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Accepted`
  - `/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_Rejected`
  - `/Game/Aerathea/Materials/Instances/MI_INF_BrandGlowStates_A01_SorcererFocus`

## Automation

- Unreal authoring: `Tools/Unreal/import_infernal_brand_glow_states.py`
- Focused validator: `Tools/Unreal/validate_infernal_brand_glow_states.py`
- Startup validator: `Tools/Unreal/validate_startup_scene.py`

## Validation Results

- Python compile check passed for the material authoring script, focused validator, and startup validator.
- Unreal authoring completed and saved the master material, material function, and six state instances.
- Focused validator passed: 1 master material, 1 material function, 6 material instances, and 4 class mesh socket contracts.
- Startup validator passed: 206 assets, 54 expected actors, 25 ground tiles.

## First-Pass Parameters

- `BrandBaseColor`
- `EmissiveColor`
- `EmissiveIntensity`
- `PulseSpeed`
- `PulseWidth`
- `VioletMix`
- `ScarDarken`
- `HeatEdgeContrast`
- `StateIndex`
- `Roughness`

## Remaining Work

- Author final `T_INF_BrandGlow_A01_E`, `T_INF_BrandGlow_A01_Mask`, `T_INF_BrandScar_A01_N`, and `T_INF_BrandScar_A01_ORM`.
- Replace placeholder material-function content with the final mask/pulse/scar logic.
- Bind state changes from Animation Blueprints, Gameplay Abilities, worthiness judgment VFX, and cult ritual Blueprints.
- Tune intensity and pulse curves in live review so glow remains restrained at MMO camera distance.
- Assign or blend these states into final Infernal body, class, Lesser, and cult material instances after final texture masks exist.
