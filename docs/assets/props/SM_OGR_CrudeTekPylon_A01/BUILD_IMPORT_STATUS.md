# SM_OGR_CrudeTekPylon_A01 Build And Import Status

## Current Status

- Build/import status: production package and modeling handoff complete; DCC build not started.
- Source mesh status: no Blender source or FBX export yet.
- Unreal state: not imported.
- Review scope: static mesh direction, material plan, sockets, collision, LODs, future Blueprint states, and Unreal path are ready for approval.

## Planned Source Outputs

- Blender source: `SourceAssets/Blender/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/SM_OGR_CrudeTekPylon_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/SM_OGR_CrudeTekPylon_A01.fbx`
- DCC review render: `Saved/Automation/OgreCrudeTekPylonReview/SM_OGR_CrudeTekPylon_A01_DCCReview.png`

## Planned Unreal Assets

- `/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01`
- Future `/Game/Aerathea/Blueprints/Props/Ogres/BP_OGR_CrudeTekPylon_A01`
- `/Game/Aerathea/Materials/Instances/MI_OGR_Teknomancy_Iron_A01`
- `/Game/Aerathea/Materials/Instances/MI_OGR_Teknomancy_Brass_A01`
- `/Game/Aerathea/Materials/Instances/MI_OGR_Teknomancy_RuneHeat_A01`
- Optional `/Game/Aerathea/Materials/Instances/MI_OGR_CrudeTekPylon_A01_Damaged`

## Completed Prerequisites

- Production package: `docs/assets/props/SM_OGR_CrudeTekPylon_A01/PRODUCTION_PACKAGE.md`
- Modeling handoff: `docs/assets/props/SM_OGR_CrudeTekPylon_A01/MODELING_HANDOFF.md`
- Parent kit: `docs/assets/kits/KIT_OGR_Teknomancy_A01/PRODUCTION_PACKAGE.md`
- Source concepts visually inspected: `OgreTekShop.png`, `Ogres10.png`, `Ogres11.png`, `OgreMaleTek.png`, `OgreTekvsGnomeMek.png`, `GnomevsOgre3.png`

## Blocking Items

- Needs approval before DCC build.
- Final mesh, authored UVs, texture set, material instances, LODs, UCX collision, sockets, import, and Blueprint wrapper are not started.
- Future Blueprint behavior depends on encounter assembly rules from `BP_GNM_OGR_BattlefieldEncounter_A01`.

## Remaining To Finalize

1. Approve the pylon static mesh silhouette and material-state direction.
2. Build first-pass DCC source and UCX collision.
3. Export FBX and import to `/Game/Aerathea/Props/Ogres/Teknomancy/`.
4. Generate material instances, LOD0-LOD3, and static mesh sockets.
5. Add optional `BP_OGR_CrudeTekPylon_A01` wrapper after encounter objective states are approved.
