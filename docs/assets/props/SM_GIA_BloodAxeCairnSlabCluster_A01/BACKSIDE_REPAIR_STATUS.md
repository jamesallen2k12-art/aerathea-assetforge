# SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair Status

Status: `Unreal import candidate shown for Flamestrike approval; not Fully game-ready until approved`

Date: 2026-07-02

## Reason For Repair

The previous `SM_GIA_BloodAxeCairnSlabCluster_A01_Test2Manual` proof is retained as historical evidence, but Flamestrike identified that the backside was not properly generated as a successful 3D candidate. The repair pass must preserve the approved A1 front identity while replacing the weak rear with authored 360-degree stone massing.

## Corrected Target

- Real rear stone volume, not a front projection or card-like backside.
- Backside support/counterweight slabs that make the cairn believable from gameplay camera angles.
- Rear oxide-red Blood Axe paint marks, rawhide lashing, mud/ash grounding, and loose stone breakup.
- Updated depth/collision envelope for a walk-around environmental prop.
- No emissive, quest-marker, loot-pile, route-marker, or interactive signal read.

## Planned Package

- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair.blend`
- Main FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair.fbx`
- LOD FBXs: `SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair_LOD0|LOD1|LOD2|LOD3.fbx`
- Texture set: `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair/`
- DCC proof renders: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair/`
- Unreal mesh target: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair`
- Startup review actor target: `AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair`

## DCC Build Result

Generated on 2026-07-02 with `Tools/DCC/build_bloodaxe_cairn_a1_backside_repair.py`.

| LOD | Triangles | Purpose |
| --- | ---: | --- |
| LOD0 | 1,844 | close review/gameplay prop |
| LOD1 | 1,152 | medium distance |
| LOD2 | 624 | far distance |
| LOD3 | 552 | very far distance |

Generated files:

- 1 Blender source file.
- 6 FBX exports: main import FBX, LOD0-LOD3 source FBXs, and separated UCX collision proxy FBX.
- 12 PNG texture files: BC/N/ORM for dark Blood Axe stone, earth/ash, rawhide, and Blood Axe red paint.
- DCC proof renders: front, three-quarter, side, back, and turntable review board.

## Unreal Import And Validation

Imported on 2026-07-02 with `Tools/Unreal/import_bloodaxe_cairn_backside_repair.py`.

- Unreal mesh: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair`
- Startup review actor: `AET_PROD_GIA_BloodAxeCairnSlabCluster_A01_BacksideRepair`
- Approval capture: `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeCairnBacksideRepair_A01_BackApproval_CloseLit.png`
- Validator result: `162.36h x 402.18w x 300.58d cm, 4 LODs, 4 materials, 12 textures, broad collision enabled.`
- Collision note: the visible UCX proxy was removed from the render/import FBX and kept as a separated collision source export so it cannot render as a box in Unreal review captures.
- Material note: stone base color was corrected from warm khaki to dark rough Blood Axe stone before final review capture.

## Status Gates

- [x] DCC source candidate generated.
- [x] DCC game-ready candidate generated with FBX, LODs, collision proxy, material plan, textures, and proof renders.
- [x] Unreal import candidate created.
- [x] Startup review actor placed and validated.
- [x] Visual approval capture shown to Flamestrike.
- [ ] Flamestrike approval recorded before library promotion.

## Quality Gate

- Front keeps the A1 low collapsed slab-cluster identity.
- Back reads as authored solid stone construction, not a flat projection.
- Side and rear silhouette remain Blood Axe: rough dark stone, ash/mud, rawhide, and restrained oxide red.
- LOD0-LOD3 preserve primary silhouette before removing minor details.
- Broad simple collision covers the corrected rear depth.
- Texture set remains stylized MMO-friendly and avoids photoreal noise.
