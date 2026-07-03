# SM_AET_PortalArch_A01 Build And Import Status

## Current Result

- Build/import status: 10 m universal scale rebuild complete; Blender source regenerated, FBX exported, imported to Unreal, startup portal visual replaced, focused portal validation passing, and startup validation passing
- Source mesh status: Blender `.blend` source and FBX export generated from the current 10 m portal handoff
- Unreal replacement status: `AET_PROD_Portal_A01` exists in `L_Aerathea_Startup` as an `AAETPortalActor` review actor using the imported arch/core visuals
- Blueprint dependency: `BP_AET_Portal_A01` exists and is reparented to `AAETPortalActor`; final VFX/audio/destination behavior remains pending
- Validation: `Tools/Unreal/validate_portal_10m_scale.py` and `Tools/Unreal/validate_startup_scene.py` pass through `UnrealEditor-Cmd`

## Reason

The portal arch has a concept sheet, production package, DCC modeling handoff, Blender source, FBX export, Unreal import, startup-scene placement, mesh sockets, generated LOD0-LOD3, and UCX collision. The first-pass 10 m rebuild is suitable for scale/composition review and production planning. Final signoff still requires Flamestrike visual approval, final sculpt/retopo/UVs/textures, tangent cleanup, final material polish, VFX/audio, and approved traversal behavior.

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
- Build/import automation:
  - `Tools/DCC/build_portal_arch.py`
  - `Tools/Unreal/import_portal_10m.py`
  - `Tools/Unreal/validate_portal_10m_scale.py`

## Remaining To Finalize

1. Assign final materials:
   - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Stone`
   - `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Accent`
2. Review several old, mysterious, awe-inspiring portal visual directions before final art lock.
3. Replace the generated block geometry with final sculpt/retopo/UVs/textures while preserving the validated 10 m scale and aperture.
4. Clean up any final-art tangent/normal warnings from the generated prism/block source.
5. Inspect and tune LOD0-LOD3 against the final art mesh.
6. Validate simple collision and walkable aperture for players, Giants, large NPCs, and large enemies in a live review pass.
7. Complete final `BP_AET_Portal_A01` trigger/VFX/audio/destination behavior around the rebuilt mesh.
8. Run focused portal validator and startup scene validator after each final-art import.
9. Run GUI map check and confirm `0 Error(s), 0 Warning(s)`.

## Acceptance Gate

The portal arch can be treated as imported and validated for 10 m startup-scale review. Do not mark the portal slice as final until the visual direction is approved, final materials, final-art LODs, collision/aperture inspection, VFX/audio, and `BP_AET_Portal_A01` traversal behavior are complete.
