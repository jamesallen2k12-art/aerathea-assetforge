# SM_AET_PortalArch_A01 Build And Import Status

## Current Result

- Build/import status: imported and startup blockout replaced
- Source mesh status: fallback OBJ/MTL and FBX generated from the approved production handoff
- Unreal replacement status: `AET_PROD_PortalArch_A01` and `AET_PROD_PortalCore_Aetherium_A01` exist in `L_Aerathea_Startup`
- Blueprint dependency: `BP_AET_Portal_A01` asset shell exists; behavior implementation remains pending
- Validation: `Tools/Unreal/validate_startup_scene.py` passes through `UnrealEditor-Cmd`

## Reason

The portal arch has a concept sheet, production package, and DCC modeling handoff. The local Blender binary is blocked by a runtime library issue, so `Tools/DCC/generate_first_slice_meshes.py` generated a deterministic OBJ/FBX fallback source mesh from the approved handoff to keep Unreal validation moving. This mesh is suitable for portal composition and startup map validation, but should be replaced by an approved Blender-authored source mesh before final art signoff.

## Completed Prerequisites

- Production package:
  - `docs/assets/props/SM_AET_PortalArch_A01/PRODUCTION_PACKAGE.md`
- Concept reference:
  - `docs/assets/props/SM_AET_PortalArch_A01/concepts/SM_AET_PortalArch_A01_concept_sheet_A01.png`
- Modeling handoff:
  - `docs/assets/props/SM_AET_PortalArch_A01/MODELING_HANDOFF.md`
- Fallback source/export:
  - `SourceAssets/Blender/Props/Portal/SM_AET_PortalArch_A01/SM_AET_PortalArch_A01.obj`
  - `SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01/SM_AET_PortalArch_A01.fbx`
- Unreal asset:
  - `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
- Blueprint asset shell:
  - `/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01`

## Remaining To Finalize

1. Repair Blender or use another approved DCC path.
2. Create approved Blender source:
   - `SourceAssets/Blender/Props/Portal/SM_AET_PortalArch_A01.blend`
3. Re-export approved FBX:
   - `SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01.fbx`
4. Reimport static mesh into Unreal:
   - `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
5. Assign final materials:
   - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Stone`
   - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Accent`
6. Import or generate LOD0-LOD3.
7. Validate simple collision and walkable aperture.
8. Complete `BP_AET_Portal_A01` trigger/VFX/audio/state behavior around the imported mesh.
9. Run startup scene validator.
10. Run GUI map check and confirm `0 Error(s), 0 Warning(s)`.

## Acceptance Gate

The portal arch can be treated as imported for startup-scene validation. Do not mark the portal slice as final until approved Blender source, final materials, LODs, collision, aperture inspection, and `BP_AET_Portal_A01` behavior are complete.
