# SM_AET_TargetDummy_A01 Build And Import Status

## Current Result

- Build/import status: Blender source generated, FBX exported, imported to Unreal, and startup blockout replaced
- Blender availability: `/usr/bin/blender` starts successfully after the local MaterialX package downgrade
- Source mesh status: Blender `.blend` source and FBX export generated from the approved production handoff
- Unreal replacement status: `AET_PROD_TargetDummy_A01` exists in `L_Aerathea_Startup`
- Validation: `Tools/Unreal/validate_startup_scene.py` passes through `UnrealEditor-Cmd`

## Reason

The target dummy has a concept sheet, production package, modeling handoff, Blender source, FBX export, Unreal import, and startup-scene placement. This mesh is suitable for production review and startup validation. Final signoff still requires art review, final materials, LOD inspection, and collision inspection.

## Completed Prerequisites

- Production package exists:
  - `docs/assets/props/SM_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md`
- Concept reference exists:
  - `docs/assets/props/SM_AET_TargetDummy_A01/concepts/SM_AET_TargetDummy_A01_concept_sheet_A01.png`
- Modeling handoff exists:
  - `docs/assets/props/SM_AET_TargetDummy_A01/MODELING_HANDOFF.md`
- Blender source/export exists:
  - `SourceAssets/Blender/Props/Training/SM_AET_TargetDummy_A01/SM_AET_TargetDummy_A01.blend`
  - `SourceAssets/Exports/Props/Training/SM_AET_TargetDummy_A01/SM_AET_TargetDummy_A01.fbx`
- Unreal asset exists:
  - `/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01`

## Remaining To Finalize

1. Assign final material instance:
   - `/Game/Aerathea/Materials/Props/MI_AET_TargetDummy_A01`
2. Import or generate LOD0-LOD3.
3. Verify simple collision primitives.
4. Run startup scene validator.
5. Run GUI map check and confirm `0 Error(s), 0 Warning(s)`.

## Acceptance Gate

The target dummy can be treated as imported for startup-scene validation and production review. Do not mark it as final art until final textures/materials, LODs, collision, and visual inspection are complete.
