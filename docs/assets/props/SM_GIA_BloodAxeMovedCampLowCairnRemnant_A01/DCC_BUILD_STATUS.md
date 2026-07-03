# SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01 DCC Build Status

## Scope

- Task: `AET-MA-20260629-573`
- Target: `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- DCC packet: `docs/agents/AET-MA-20260629-572_DCC_TASK_PACKET.md`
- Source package: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PRODUCTION_PACKAGE.md`
- Build script: `Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py`

This is a first-pass DCC review build for the approved Blood Axe moved-camp low cairn remnant. It is not final visual approval, not Unreal import approval, and not collision correctness approval.

## Outputs

| Output | Path | Status |
| --- | --- | --- |
| Blender source | `SourceAssets/Blender/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.blend` | Created, 118595 bytes |
| FBX export | `SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.fbx` | Created, 49708 bytes |
| DCC proof render | `Saved/Automation/DCC/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01_DCCReview.png` | Created, 1082116 bytes |

## DCC Metrics

| Metric | Result |
| --- | --- |
| LOD0 mesh objects | 9 |
| LOD0 triangles | 420 |
| LOD1 source mesh objects | 5 |
| LOD1 source triangles | 132 |
| LOD2 source mesh objects | 5 |
| LOD2 source triangles | 132 |
| LOD3 source mesh objects | 4 |
| LOD3 source triangles | 112 |
| LOD0 bounds | 330.0 cm wide, 236.0 cm deep, 130.35 cm tall |
| Scale target | Within the approved 60-180 cm height range and close to the 110-140 cm first-pass preference |
| Giant scale comparison | Proof render includes 132 cm remnant, 442 cm female Giant, and 470 cm male Giant scale bars |
| Export material target | LOD0 export meshes use `M_GIA_BloodAxeMovedCampLowCairnRemnant_Blockout_A01` |
| Source material caveat | Blender retains an unused default `Material` with 0 users; LOD0 export meshes use only the target material |
| Collision | No UCX collision created; collision remains disabled-by-default / future-gated |

## Visual Read

- Reads as one low collapsed cairn remnant, wider than tall.
- Uses five large rough stone masses, a broad ash/mud base, one faded Blood Axe red residue beat, and a low rawhide residue strip.
- The red beat is fixed low against the stone mass and does not read as a banner, route flag, UI marker, waypoint, or active signal.
- The proof render frames the prop against Giant scale bars and keeps the remnant far below the 442 cm and 470 cm Giant baselines.
- The asset remains static environmental storytelling only.

## Validation Notes

- `python -m py_compile Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py` passed.
- Blender build completed and created the approved `.blend`, `.fbx`, and proof render outputs.
- Blender reported a nonfatal OpenColorIO config-version warning and used fallback color management.
- Blender reported a nonfatal thumbnail-cache write warning under `/home/Flamestrike/.cache`; the requested proof PNG still saved at the approved path.
- DCC source includes LOD1-LOD3 source meshes in hidden collections. The first FBX export contains LOD0 only to avoid ambiguous multi-mesh LOD import behavior before the Unreal import packet.

## Still Blocked

Unreal import, Unreal Content edits, material instance creation, texture asset creation, runtime source, validators outside the validation summary, startup placement, review actors, final visual approval, final collision approval, route approval, gameplay behavior, pickup behavior, loot behavior, salvage behavior, resource behavior, navigation/pathfinding, waypoint behavior, breadcrumb behavior, tracking behavior, objective logic, VFX/audio, cloth simulation, wind animation, physics behavior, source concept movement, Hermes work, and global docs integration remain blocked until later packets explicitly authorize them.

## DCC Decision

`AET-MA-20260629-573` passes first-pass DCC build validation as a review target. The output is suitable for a future Unreal import packet, subject to the unresolved blockers above and no final visual approval claim.
