# SM_AET_PortalArch_A01 Build And Import Status

## Current Result

- Build/import status: blocked on approved DCC mesh
- Source mesh status: no approved `.blend` or `.fbx` exists in the project
- Unreal replacement status: startup portal blockout remains in `L_Aerathea_Startup`
- Blueprint dependency: `BP_AET_Portal_A01` cannot complete final validation until this mesh is imported

## Reason

The portal arch has a concept sheet, production package, and DCC modeling handoff, but no approved modeled source asset exists yet. Creating a procedural placeholder mesh and treating it as the production portal arch would violate the Aerathea production rule against skipping from concept to fake final art.

## Completed Prerequisites

- Production package:
  - `docs/assets/props/SM_AET_PortalArch_A01/PRODUCTION_PACKAGE.md`
- Concept reference:
  - `docs/assets/props/SM_AET_PortalArch_A01/concepts/SM_AET_PortalArch_A01_concept_sheet_A01.png`
- Modeling handoff:
  - `docs/assets/props/SM_AET_PortalArch_A01/MODELING_HANDOFF.md`

## Required To Unblock

1. Create or receive approved Blender source:
   - `SourceAssets/Blender/Props/Portal/SM_AET_PortalArch_A01.blend`
2. Export approved FBX:
   - `SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01.fbx`
3. Import static mesh into Unreal:
   - `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
4. Assign materials:
   - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Stone`
   - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Accent`
5. Import or generate LOD0-LOD3.
6. Validate simple collision and walkable aperture.
7. Replace startup portal blockout.
8. Complete `BP_AET_Portal_A01` around the imported mesh.
9. Run startup scene validator.
10. Run GUI map check and confirm `0 Error(s), 0 Warning(s)`.

## Acceptance Gate

Do not mark the portal slice as final until `SM_AET_PortalArch_A01` is imported, validated, and used by `BP_AET_Portal_A01`.
