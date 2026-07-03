# SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01 Build Import Status

## Status

- Current task: `AET-MA-20260629-579`
- Result: first-pass Unreal static mesh import remains valid, and the asset is now placed as a startup review actor.
- Scope: DCC FBX vertex colors, one combined static mesh, one Blood Axe vertex-color blockout material parent, one material instance, LOD0-LOD3 review LODs, first-pass visual approval, exact startup review placement, and non-final metadata are validated.
- Startup status: placed in `/Game/Aerathea/Maps/L_Aerathea_Startup` as review actor `AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01` at location `1280.0, 430.0, 0.0`, yaw `-18.0`.
- Final art status: final sculpt, UVs, authored BC/N/ORM textures, tuned collision, final material polish, final shipped startup composition, and shipped dressing status are not authored or approved.
- Collision status: static mesh collision is disabled for the startup review actor; no collision correctness claim.
- Gameplay status: static environmental storytelling only; no route, waypoint, breadcrumb, tracking, pickup, loot, salvage, resource, objective, nav/pathfinding, runtime, VFX/audio, combat, playstyle, economy, backend, or interaction behavior.

## Unreal Assets

- Static mesh: `/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- Material parent: `/Game/Aerathea/Materials/Giants/BloodAxe/M_GIA_BloodAxeMovedCampVertexColor_Blockout_A01`
- Material instance: `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- Startup map: `/Game/Aerathea/Maps/L_Aerathea_Startup`
- Startup review actor: `AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01`

## Source Inputs

- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.fbx`
- DCC proof render: `Saved/Automation/DCC/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01_DCCReview.png`
- Production package: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PRODUCTION_PACKAGE.md`
- DCC build status: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/DCC_BUILD_STATUS.md`
- Unreal import packet: `docs/agents/AET-MA-20260629-574_UNREAL_IMPORT_TASK_PACKET.md`
- Startup placement packet: `docs/agents/AET-MA-20260629-578_STARTUP_REVIEW_TASK_PACKET.md`
- Startup validation summary: `docs/agents/AET-MA-20260629-579_VALIDATION_SUMMARY.md`

## Authoring And Validation

- DCC builder: `Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py`
- Unreal import: `Tools/Unreal/import_bloodaxe_moved_camp_low_cairn_remnant.py`
- Startup placement: `Tools/Unreal/place_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py`
- Focused asset validator: `Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- Focused startup validator: `Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py`
- Generic startup validator: `Tools/Unreal/validate_startup_scene.py`
- Compile check: `python -m py_compile Tools/Unreal/place_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- Placement run: `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/place_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py`
- Asset validation run: `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- Startup placement validation run: `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py`
- Generic startup validation run: `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_startup_scene.py`

Focused asset validation output:

```text
Blood Axe low cairn remnant validation passed: 130.35h x 330.00w x 236.00d cm, 4 review LODs, 1 vertex-color material, no sockets, startup review metadata present, final art not authored.
```

Focused startup validation output:

```text
Blood Axe low cairn startup review validation passed: AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01 placed at 1280.0, 430.0, 0.0, yaw -18.0, no collision, first-pass visual approved not final art.
```

Generic startup validation output:

```text
Aerathea startup validation complete: 233 assets, 55 expected actors, 25 ground tiles.
```

## Visual Marker Preservation

The DCC FBX was refreshed during the Unreal import lane to add `AET_VertexColor` data. This preserves the first-pass stone, ash, mud, faded Blood Axe red residue, and rawhide color reads while keeping the one-material budget intact.

Flamestrike approved the first-pass visual/readability direction on 2026-06-30. This approval allows startup-review placement only; the prop remains a review target, not final art.

## Notes

- Blender reported the same nonfatal OpenColorIO fallback warning and thumbnail-cache write warning seen in the DCC lane; the `.blend`, `.fbx`, and proof PNG were produced.
- Unreal placement saved the startup map and static mesh metadata; source control remained disabled and Unreal emitted a non-blocking checkout dialog warning.
- The focused Unreal validators reported deprecated Editor Scripting Utilities warnings; validation still passed.
- Startup validation passed after placement, but final shipped startup composition still requires visual approval.

## Remaining Work

- Final sculpt/bevel cleanup and authored UVs.
- Authored BC/N/ORM textures and final material polish.
- Collision decision only if a future placement or gameplay task requires it.
- Final startup composition review and shipped dressing decision.
- Next Blood Axe moved-camp implementation target selection under a separate approval gate.
