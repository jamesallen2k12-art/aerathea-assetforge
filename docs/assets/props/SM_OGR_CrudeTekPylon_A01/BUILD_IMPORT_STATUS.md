# SM_OGR_CrudeTekPylon_A01 Build And Import Status

## Current Status

- Build/import status: first-pass DCC review source generated and imported to Unreal.
- Source mesh status: Blender source and FBX export exist.
- Unreal state: static mesh imported, material instances assigned, LOD0-LOD3 generated, static mesh sockets added, startup review actor placed, startup validation passing.
- Review scope: scale, silhouette, crude Ogre Teknomancy material language, socket layout, simple collision, and encounter-readiness are validated for first-pass production review.

## Source Outputs

- Blender source: `SourceAssets/Blender/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/SM_OGR_CrudeTekPylon_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/SM_OGR_CrudeTekPylon_A01.fbx`
- DCC review render: `Saved/Automation/GnomeOgreRemainingReview/SM_OGR_CrudeTekPylon_A01_DCCReview.png`
- DCC build script: `Tools/DCC/build_gnome_ogre_remaining_assets.py`
- Unreal import script: `Tools/Unreal/import_gnome_ogre_remaining_assets.py`

## Unreal Assets

- `/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01`
- Startup actor: `AET_PROD_OGR_CrudeTekPylon_A01`
- Material instances:
  - `/Game/Aerathea/Materials/Instances/MI_OGR_CrudeTekPylon_A01_CairnStone`
  - `/Game/Aerathea/Materials/Instances/MI_OGR_CrudeTekPylon_A01_Iron`
  - `/Game/Aerathea/Materials/Instances/MI_OGR_CrudeTekPylon_A01_Brass`
  - `/Game/Aerathea/Materials/Instances/MI_OGR_CrudeTekPylon_A01_SootedCopper`
  - `/Game/Aerathea/Materials/Instances/MI_OGR_CrudeTekPylon_A01_TekGlow`
  - `/Game/Aerathea/Materials/Instances/MI_OGR_CrudeTekPylon_A01_Leather`
  - `/Game/Aerathea/Materials/Instances/MI_OGR_CrudeTekPylon_A01_Warpaint`

## Validation

- `Tools/Unreal/validate_startup_scene.py` now checks this mesh, startup actor, material slots, LOD count, static mesh sockets, bounds, and runtime visibility.
- Latest validation result: passing with `121` expected assets, `46` expected actor labels, and `25` ground tiles.

## Completed Prerequisites

- Production package: `docs/assets/props/SM_OGR_CrudeTekPylon_A01/PRODUCTION_PACKAGE.md`
- Modeling handoff: `docs/assets/props/SM_OGR_CrudeTekPylon_A01/MODELING_HANDOFF.md`
- Parent kit: `docs/assets/kits/KIT_OGR_Teknomancy_A01/PRODUCTION_PACKAGE.md`
- Source concepts visually inspected: `OgreTekShop.png`, `Ogres10.png`, `Ogres11.png`, `OgreMaleTek.png`, `OgreTekvsGnomeMek.png`, `GnomevsOgre3.png`

## Remaining To Finalize

1. Replace the first-pass review mesh with approved final sculpt/retopo.
2. Author final UVs, hand-painted textures, packed ORM, and tuned emissive map.
3. Tune collision beyond broad UCX review hulls.
4. Create optional `BP_OGR_CrudeTekPylon_A01` overload/damage/repair wrapper when encounter state behavior is ready.
5. Wire the pylon into `BP_GNM_OGR_BattlefieldEncounter_A01` after final encounter placement is approved.
