# SM_INF_BalgorothSigil_A01 Modeling Handoff

## Purpose

Create the first-pass DCC source for the reusable Balgoroth cult sigil relief. This pass validates broad symbol readability, scale, material lanes, collision policy, and Unreal import readiness.

## Source References

- Production package: `docs/assets/props/SM_INF_BalgorothSigil_A01/PRODUCTION_PACKAGE.md`
- Material package: `docs/assets/materials/MI_INF_CultStone_Set_A01/PRODUCTION_PACKAGE.md`
- Material build status: `docs/assets/materials/MI_INF_CultStone_Set_A01/BUILD_IMPORT_STATUS.md`
- Kit readiness matrix: `docs/assets/kits/KIT_INF_BalgorothCult_A01/IMPLEMENTATION_READINESS_MATRIX.md`

## Production Target

- Asset: `SM_INF_BalgorothSigil_A01`
- Type: Static Mesh wall-relief sigil source.
- Size: roughly 320 cm wide, 300 cm high, and 28 cm collision depth.
- Unreal target path: `/Game/Aerathea/Props/Infernals/BalgorothCult/Sigils/SM_INF_BalgorothSigil_A01`
- DCC state: first-pass Blender source, FBX export, and proof render generated; Unreal import and final art remain pending.

## DCC Output

- Builder: `Tools/DCC/build_infernal_balgoroth_sigil.py`
- Blender source: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/SM_INF_BalgorothSigil_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_BalgorothSigil_A01/SM_INF_BalgorothSigil_A01.fbx`
- Proof render: `Saved/Automation/InfernalBalgorothSigilReview/SM_INF_BalgorothSigil_A01_DCCReview.png`

## Geometry Notes

- Built as a wall-relief plate carrying the approved horned crown, split wing, ember eye, broken circle, hooked-tail crescent, and broad claw-slash language.
- Relief pieces are intentionally large and blocky for MMO-distance readability.
- No readable text, tiny rune clusters, rivet fields, or dense micro-detail were modeled.
- Final sculpt, bevel polish, UV art pass, and texture authoring remain pending.

## Material Slots

Current DCC material lanes are named to consume the first-pass CultStone material set:

- `MI_INF_CultStone_Basalt_A01`
- `MI_INF_CultStone_ScorchedRed_A01`
- `MI_INF_CultStone_ObsidianInset_A01`
- `MI_INF_CultStone_EmissiveChannel_A01`

Unreal import should assign the existing first-pass material instances rather than creating duplicate sigil-specific materials in this lane.

## Collision

- Authored simple wall collision only: `UCX_SM_INF_BalgorothSigil_A01_00`.
- Relief pieces remain visual-only to avoid movement snagging and to allow reuse as wall dressing.
- Floor-insert collision should be handled by a future floor variant if needed.

## LOD Plan

- LOD0: full relief geometry from the first-pass source.
- LOD1: 55-60 percent; reduce secondary bevels and minor relief thickness.
- LOD2: 25-35 percent; flatten minor grooves while preserving crown, wing, eye, circle, crescent, and claw silhouettes.
- LOD3: 10-15 percent; preserve only broad color/silhouette blocks and emissive channel positions.

## Socket Plan For Unreal Import

- `vfx_sigil_core`
- `vfx_eye_core`
- `vfx_rejected_break`
- `snap_floor_center`

For this wall-relief source, `snap_floor_center` should be placed at the asset pivot until a floor insert variant is split out.

## Validation Evidence

- `python -m py_compile Tools/DCC/build_infernal_balgoroth_sigil.py`
  - Passed.
- `blender --background --python Tools/DCC/build_infernal_balgoroth_sigil.py`
  - Passed and generated source, export, and proof render.
- Output file sizes:
  - `.blend`: 122774 bytes
  - `.fbx`: 101804 bytes
  - proof render: 1506522 bytes

Blender emitted an OpenColorIO fallback warning and a thumbnail-cache write warning outside the project. Both were non-blocking; the requested project outputs were generated.

## Remaining Work

- Final sculpt and bevel pass.
- Authored UVs and texture maps.
- Final material polish.
- Optional split into wall relief, floor insert, and altar inset variants.
- Startup or review-scene placement only after a dedicated placement task.

## DCC And Unreal Pass - 2026-06-29

- Built first-pass Blender source and FBX export using `Tools/DCC/build_infernal_balgoroth_sigil.py`.
- Generated DCC proof render at `Saved/Automation/InfernalBalgorothSigilReview/SM_INF_BalgorothSigil_A01_DCCReview.png`.
- Imported to `/Game/Aerathea/Props/Infernals/BalgorothCult/Sigils/SM_INF_BalgorothSigil_A01` with `Tools/Unreal/import_infernal_balgoroth_sigil.py`.
- Assigned four first-pass CultStone material lanes: basalt, scorched red, obsidian inset, and emissive channel.
- Generated LOD0-LOD3 and added `vfx_sigil_core`, `vfx_eye_core`, `vfx_rejected_break`, and `snap_floor_center`.
- Focused validator passed: `343.82h x 352.00w x 51.50d cm`, 4 material lanes, 4 sockets.
- Startup placement was not performed.
