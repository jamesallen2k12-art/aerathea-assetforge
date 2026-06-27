# SM_OGR_CrudeTekPylon_A01 Modeling Handoff

## Purpose

Create the DCC source, static mesh, material slots, LODs, sockets, collision, and Unreal import path for an Ogre crude Teknomancy battlefield pylon.

## Source References

- Production package: `docs/assets/props/SM_OGR_CrudeTekPylon_A01/PRODUCTION_PACKAGE.md`
- Parent kit: `docs/assets/kits/KIT_OGR_Teknomancy_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_OGR_Teknomancy_A01/CHILD_ASSET_INTAKE.md`
- Rivalry kit: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/PRODUCTION_PACKAGE.md`
- Source concepts:
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreTekShop.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Ogres10.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Ogres11.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreMaleTek.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreTekvsGnomeMek.png`

## Production Target

- Asset: `SM_OGR_CrudeTekPylon_A01`
- Type: Static Mesh prop / future Blueprint objective.
- Height target: 360-520 cm.
- Footprint target: 260-380 cm wide.
- Unreal path: `/Game/Aerathea/Props/Ogres/Teknomancy/`
- DCC state: not started.

## Modeling Constraints

- Build large readable shapes first: base skids, stone ballast, central reactor column, pressure tanks, conductor arms, top lightning rods, large vents, thick cables, and main rune windows.
- Keep the prop heavy enough for Ogres to operate and too crude to be gnomish.
- Avoid thin elegant antennae, tiny wire fields, clean symmetry, and polished magical obelisk shapes.
- Use kit material families from `KIT_OGR_Teknomancy_A01`.
- Author damage-state break points as optional mesh pieces only if they preserve clean LODs.

## Blender Setup

- Collection: `SM_OGR_CrudeTekPylon_A01`
- Mesh groups:
  - `Base_Skids_StoneBallast`
  - `Reactor_Column`
  - `Pressure_Tanks`
  - `Conductors_Top`
  - `Cables_Chains`
  - `RuneHeat_Windows`
  - `Damage_Optional`
- Pivot: bottom center at world origin.
- Unit scale: centimeters.
- Add named empties for Unreal sockets.
- Author simple UCX collision meshes if building the DCC source.

## Modeling Sequence

1. Block height, footprint, and bottom-center pivot.
2. Build the base skids and stone ballast first.
3. Add the central reactor column and main core window.
4. Add side tanks, straps, brackets, and thick cables.
5. Add top conductor arms and forked rods.
6. Add sockets for core, vents, cables, top arcs, repair panel, and overload burst.
7. Add optional skull plate/banner accent only if it does not clutter silhouette.
8. Build LOD0-LOD3 and UCX collision.
9. Export FBX after scale and silhouette approval.

## Triangle Budget

- LOD0: 8k-16k tris.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.
- Hero ceiling: 20k tris only for a promoted encounter objective.

## Texture Deliverables

Shared kit materials:

- `T_OGR_Teknomancy_Iron_A01_BC/N/ORM`
- `T_OGR_Teknomancy_Brass_A01_BC/N/ORM`
- `T_OGR_Teknomancy_Leather_A01_BC/N/ORM`
- `T_OGR_Teknomancy_RuneHeat_A01_BC/N/ORM/E`

Optional dedicated maps:

- `T_OGR_CrudeTekPylon_A01_BC`
- `T_OGR_CrudeTekPylon_A01_N`
- `T_OGR_CrudeTekPylon_A01_ORM`
- `T_OGR_CrudeTekPylon_A01_E`

## Collision Deliverables

- `UCX_SM_OGR_CrudeTekPylon_A01_Base`
- `UCX_SM_OGR_CrudeTekPylon_A01_Column`
- `UCX_SM_OGR_CrudeTekPylon_A01_Tank_L`
- `UCX_SM_OGR_CrudeTekPylon_A01_Tank_R`
- `UCX_SM_OGR_CrudeTekPylon_A01_Top`

Cables, chains, banners, trophies, and small conductor details remain non-blocking.

## Socket Deliverables

- `socket_core`
- `socket_top_arc`
- `socket_conductor_l`
- `socket_conductor_r`
- `socket_vent_l`
- `socket_vent_r`
- `socket_cable_in`
- `socket_cable_out`
- `socket_hit_core`
- `socket_repair_panel`
- `socket_ground_sparks`
- `socket_overload_burst`

## Export Targets

- Blender source: `SourceAssets/Blender/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/SM_OGR_CrudeTekPylon_A01.blend`
- FBX export: `SourceAssets/Exports/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/SM_OGR_CrudeTekPylon_A01.fbx`
- DCC review render: `Saved/Automation/OgreCrudeTekPylonReview/SM_OGR_CrudeTekPylon_A01_DCCReview.png`
- Unreal static mesh: `/Game/Aerathea/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01`
- Future Blueprint: `/Game/Aerathea/Blueprints/Props/Ogres/BP_OGR_CrudeTekPylon_A01`

## Unreal Validation

- Imports at intended Ogre prop scale.
- Pivot is bottom center.
- LODs preserve base footprint, central column, side tanks, top conductor, and core glow read.
- Material slots are 3 target, 4 maximum.
- Socket names are present and correctly oriented for future Niagara arcs and interaction traces.
- Collision blocks the base/column without snagging on cables or chains.

## Acceptance Checklist

- Reads as crude Ogre Teknomancy, not gnome precision or a generic magic tower.
- Fit and interaction scale support Ogre operators.
- Pylon can function as encounter objective, siege-yard prop, or Tek shop device.
- Static mesh package includes material, LOD, collision, socket, and future Blueprint state plans.
- Final DCC mesh, authored UVs/textures, import, and Blueprint behavior remain pending.
