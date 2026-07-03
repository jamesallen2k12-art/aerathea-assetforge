# MI_INF_CultStone_Set_A01 Build Import Status

## Status

- Task: `AET-MA-20260628-026`
- Result: first-pass Unreal material set implemented and focused validation passed.
- Scope: reusable parent material and seven material instances for Balgoroth cult stone, iron, bone/horn, ash cloth, and emissive channel use.
- Final art status: final authored textures, final shader polish, and broad environment material art pass are not authored.

## Unreal Assets

- Parent material: `/Game/Aerathea/Materials/Infernals/M_INF_CultStone_Master_A01`
- Material instances:
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_Basalt_A01`
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_ScorchedRed_A01`
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_ObsidianInset_A01`
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_BlackIron_A01`
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_BoneHorn_A01`
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_AshCloth_A01`
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_EmissiveChannel_A01`

## Authoring And Validation

- Unreal authoring: `Tools/Unreal/import_infernal_cult_stone_materials.py`
- Focused validator: `Tools/Unreal/validate_infernal_cult_stone_materials.py`
- Compile check: `python -m py_compile Tools/Unreal/import_infernal_cult_stone_materials.py Tools/Unreal/validate_infernal_cult_stone_materials.py`
- Import run: `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/import_infernal_cult_stone_materials.py`
- Validation run: `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_infernal_cult_stone_materials.py`

Focused validation output:

```text
Infernal CultStone material validation passed: 1 master material, 7 first-pass material instances, final textures not authored.
```

## Contract Notes

- The material set is state-ready through scalar parameters: `StateIndex`, `GlowIntensity`, `ChannelOpacity`, `RejectedVioletMix`, `AshWearAmount`, `EdgeWearAmount`, `HeatCrackAmount`, `Roughness`, `Metallic`, `RoughnessBias`, and `FinalTexturesAuthored`.
- `FinalTexturesAuthored` remains `0.0` and metadata `Aerathea.Material.FinalTexturesAuthored` remains `false`.
- `MI_INF_CultStone_EmissiveChannel_A01` is the only high-glow instance and is constrained to restrained ember/deep-red channels with limited violet mix.
- No startup scene placement was performed for this material-only lane.

## Remaining Work

- Final texture maps: `T_INF_CultStone_A01_BC/N/ORM/E`, `T_INF_BlackIron_A01_BC/N/ORM`, `T_INF_ObsidianBone_A01_BC/N/ORM`, `T_INF_AshCloth_A01_BC/N/ORM`, and `T_INF_BrandGlow_A01_E`.
- Final shader polish and material function extraction, if needed.
- Assignment to consuming meshes during their own DCC/Unreal import lanes.
