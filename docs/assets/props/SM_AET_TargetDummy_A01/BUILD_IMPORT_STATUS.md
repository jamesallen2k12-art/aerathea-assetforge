# SM_AET_TargetDummy_A01 Build And Import Status

## Current Result

- Build/import status: blocked on approved DCC mesh
- Blender availability: `/usr/bin/blender` exists
- Source mesh status: no approved `.blend` or `.fbx` exists in the project
- Unreal replacement status: startup blockout remains in `L_Aerathea_Startup`

## Reason

The target dummy has a concept sheet and modeling handoff, but it does not yet have an approved modeled source asset. Creating a procedural placeholder mesh and importing it as the production target would violate the Aerathea production rule against skipping from concept to fake final art.

## Completed Prerequisites

- Production package exists:
  - `docs/assets/props/SM_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md`
- Concept reference exists:
  - `docs/assets/props/SM_AET_TargetDummy_A01/concepts/SM_AET_TargetDummy_A01_concept_sheet_A01.png`
- Modeling handoff exists:
  - `docs/assets/props/SM_AET_TargetDummy_A01/MODELING_HANDOFF.md`

## Required To Unblock

1. Create or receive the approved Blender source file:
   - `SourceAssets/Blender/Props/Training/SM_AET_TargetDummy_A01.blend`
2. Export the approved FBX:
   - `SourceAssets/Exports/Props/Training/SM_AET_TargetDummy_A01.fbx`
3. Import into Unreal at:
   - `/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01`
4. Assign material instance:
   - `/Game/Aerathea/Materials/Props/MI_AET_TargetDummy_A01`
5. Import or generate LOD0-LOD3.
6. Add simple collision primitives.
7. Replace the startup-scene blockout.
8. Run startup scene validator.
9. Run GUI map check and confirm `0 Error(s), 0 Warning(s)`.

## Acceptance Gate

Do not mark `SM_AET_TargetDummy_A01` as imported until the source mesh, textures/materials, LODs, collision, and startup-scene replacement are all validated.
