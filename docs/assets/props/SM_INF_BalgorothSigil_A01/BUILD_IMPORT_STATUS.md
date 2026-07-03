# SM_INF_BalgorothSigil_A01 Build Import Status

## Status

- Task: `AET-MA-20260628-029`
- Result: first-pass Unreal static mesh import complete and focused validation passed.
- Scope: imported static mesh, assigned first-pass CultStone material instances, generated LOD0-LOD3, and added required sockets.
- Startup status: not placed in the startup scene.
- Final art status: final sculpt, UVs, authored textures, tuned collision, and final material polish are not authored.

## Unreal Assets

- Static mesh: `/Game/Aerathea/Props/Infernals/BalgorothCult/Sigils/SM_INF_BalgorothSigil_A01`
- Material instances assigned:
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_Basalt_A01`
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_ScorchedRed_A01`
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_ObsidianInset_A01`
  - `/Game/Aerathea/Materials/Instances/MI_INF_CultStone_EmissiveChannel_A01`

## Source Inputs

- Blender source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/SM_INF_BalgorothSigil_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/SM_INF_BalgorothSigil_A01.fbx`
- Proof render: `Saved/Automation/InfernalBalgorothSigilReview/SM_INF_BalgorothSigil_A01_DCCReview.png`

## Authoring And Validation

- DCC builder: `Tools/DCC/build_infernal_balgoroth_sigil.py`
- Unreal import: `Tools/Unreal/import_infernal_balgoroth_sigil.py`
- Focused validator: `Tools/Unreal/validate_infernal_balgoroth_sigil.py`
- Compile check: `python -m py_compile Tools/Unreal/import_infernal_balgoroth_sigil.py Tools/Unreal/validate_infernal_balgoroth_sigil.py`
- Import run: `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/import_infernal_balgoroth_sigil.py`
- Validation run: `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_infernal_balgoroth_sigil.py`

Focused validation output:

```text
Infernal BalgorothSigil validation passed: 343.82h x 352.00w x 51.50d cm, 4 material lanes, 4 sockets.
```

## Socket Contract

- `vfx_sigil_core`
- `vfx_eye_core`
- `vfx_rejected_break`
- `snap_floor_center`

## Notes

- Unreal emitted degenerate tangent / near-zero tangent warnings on import. This is acceptable for the first-pass hard-edged blockout but should be cleaned in final DCC bevel/normal/UV work.
- No startup scene placement was performed, so startup validation was not required for this lane.

## Remaining Work

- Final sculpt and bevel pass.
- Authored UVs and texture maps.
- Optional split into wall relief, floor insert, and altar inset variants.
- Startup or review-scene placement only after a dedicated placement task.
