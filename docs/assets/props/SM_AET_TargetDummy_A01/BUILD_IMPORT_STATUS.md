# SM_AET_TargetDummy_A01 Build And Import Status

## Current Result

- Build/import status: imported and startup blockout replaced
- Blender availability: `/usr/bin/blender` exists but fails locally with a USD/MaterialX symbol lookup error
- Source mesh status: fallback OBJ/MTL and FBX generated from the approved production handoff
- Unreal replacement status: `AET_PROD_TargetDummy_A01` exists in `L_Aerathea_Startup`
- Validation: `Tools/Unreal/validate_startup_scene.py` passes through `UnrealEditor-Cmd`

## Reason

The target dummy has a concept sheet and modeling handoff. The local Blender binary is blocked by a runtime library issue, so `Tools/DCC/generate_first_slice_meshes.py` generated a deterministic OBJ/FBX fallback source mesh from the approved handoff to keep Unreal validation moving. This mesh is suitable for startup scene integration and collision/import testing, but it should be replaced by an approved Blender-authored source mesh before final art signoff.

## Completed Prerequisites

- Production package exists:
  - `docs/assets/props/SM_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md`
- Concept reference exists:
  - `docs/assets/props/SM_AET_TargetDummy_A01/concepts/SM_AET_TargetDummy_A01_concept_sheet_A01.png`
- Modeling handoff exists:
  - `docs/assets/props/SM_AET_TargetDummy_A01/MODELING_HANDOFF.md`
- Fallback source/export exists:
  - `SourceAssets/Blender/Props/Training/SM_AET_TargetDummy_A01/SM_AET_TargetDummy_A01.obj`
  - `SourceAssets/Exports/Props/Training/SM_AET_TargetDummy_A01/SM_AET_TargetDummy_A01.fbx`
- Unreal asset exists:
  - `/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01`

## Remaining To Finalize

1. Repair Blender or use another approved DCC path.
2. Create approved Blender source file:
   - `SourceAssets/Blender/Props/Training/SM_AET_TargetDummy_A01.blend`
3. Re-export approved FBX:
   - `SourceAssets/Exports/Props/Training/SM_AET_TargetDummy_A01.fbx`
4. Reimport into Unreal at:
   - `/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01`
5. Assign final material instance:
   - `/Game/Aerathea/Materials/Props/MI_AET_TargetDummy_A01`
6. Import or generate LOD0-LOD3.
7. Verify simple collision primitives.
8. Run startup scene validator.
9. Run GUI map check and confirm `0 Error(s), 0 Warning(s)`.

## Acceptance Gate

The target dummy can be treated as imported for startup-scene validation. Do not mark it as final art until approved Blender source, final textures/materials, LODs, collision, and visual inspection are complete.
