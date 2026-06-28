# SM_AET_PortalArch_A01 Build And Import Status

## Current Result

- Build/import status: Blender source generated, FBX exported, imported to Unreal, and startup portal visual replaced; current import uses older smaller scale assumptions
- Source mesh status: Blender `.blend` source and FBX export generated from the approved production handoff
- Unreal replacement status: `AET_PROD_Portal_A01` exists in `L_Aerathea_Startup` as an `AAETPortalActor` review actor using the imported arch/core visuals
- Blueprint dependency: `BP_AET_Portal_A01` exists and is reparented to `AAETPortalActor`; final VFX/audio/destination behavior remains pending
- Validation: `Tools/Unreal/validate_startup_scene.py` passes through `UnrealEditor-Cmd`

## Reason

The portal arch has a concept sheet, production package, DCC modeling handoff, Blender source, FBX export, Unreal import, and startup-scene placement. This mesh is suitable for production review and startup validation only. Final signoff now requires visual exploration plus a rebuild or rescale to the approved universal portal target: a 10 m / about 33 ft clear traversal opening that can accommodate Giants, large NPCs, enemies, and epic dungeon/raid/city traversal.

## Completed Prerequisites

- Production package:
  - `docs/assets/props/SM_AET_PortalArch_A01/PRODUCTION_PACKAGE.md`
- Concept reference:
  - `docs/assets/props/SM_AET_PortalArch_A01/concepts/SM_AET_PortalArch_A01_concept_sheet_A01.png`
- Modeling handoff:
  - `docs/assets/props/SM_AET_PortalArch_A01/MODELING_HANDOFF.md`
- Blender source/export:
  - `SourceAssets/Blender/Props/Portal/SM_AET_PortalArch_A01/SM_AET_PortalArch_A01.blend`
  - `SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01/SM_AET_PortalArch_A01.fbx`
- Unreal asset:
  - `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
- Blueprint asset shell:
  - `/Game/Aerathea/Blueprints/Props/BP_AET_Portal_A01`

## Remaining To Finalize

1. Assign final materials:
   - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Stone`
   - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Accent`
2. Review several old, mysterious, awe-inspiring portal visual directions before final art lock.
3. Rebuild or rescale the mesh to the approved 10 m / about 33 ft clear traversal target.
4. Import or generate LOD0-LOD3.
5. Validate simple collision and walkable aperture for players, Giants, large NPCs, and large enemies.
6. Complete final `BP_AET_Portal_A01` trigger/VFX/audio/destination behavior around the rebuilt mesh.
7. Run startup scene validator.
8. Run GUI map check and confirm `0 Error(s), 0 Warning(s)`.

## Acceptance Gate

The portal arch can be treated as imported for startup-scene validation and production review. Do not mark the portal slice as final until the visual direction is approved, the 10 m scale rebuild is complete, and final materials, LODs, collision, aperture inspection, and `BP_AET_Portal_A01` behavior are complete.
