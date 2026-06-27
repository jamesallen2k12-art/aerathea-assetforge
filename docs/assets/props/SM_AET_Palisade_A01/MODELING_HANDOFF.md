# SM_AET_Palisade_A01 Modeling Handoff

## Purpose

Create the first modular Aerathea settlement defense kit for DCC review and Unreal import. The kit should prove 400 cm snapping, simple collision, material reuse, LOD consistency, and town-edge readability.

## Source References

- Production package: `docs/assets/props/SM_AET_Palisade_A01/PRODUCTION_PACKAGE.md`
- Supporting visual reference: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gatehouse Approved.png`
- Existing ground module reference: `docs/assets/props/SM_AET_ModularGroundTile_A01/PRODUCTION_PACKAGE.md`

## Production Target

Five modular static mesh pieces:

- `SM_AET_Palisade_Wall_A01`
- `SM_AET_Palisade_Post_A01`
- `SM_AET_Palisade_Corner_A01`
- `SM_AET_Palisade_Gate_A01`
- `SM_AET_Palisade_EndCap_A01`

## Modeling Constraints

- Snap on a 400 cm grid.
- Keep module footprints exact across LODs.
- Model main logs, braces, footings, gate planks, large hinges, and iron straps.
- Texture wood grain, small cracks, mud, nail heads, scratches, and rope fibers.
- Avoid complex collision and per-stake collision.

## Blender Setup

- Scene scale: centimeters.
- Collection: `SM_AET_Palisade_A01`.
- Subcollections per module.
- Use object names matching Unreal asset names.
- Add UCX collision objects in the same file or create Unreal-generated simple collision notes per module.

## Modeling Sequence

1. Block wall, post, corner, gate, and end cap modules on a 400 cm grid.
2. Verify module pivots and snapping before detail work.
3. Add broad log silhouettes and brace beams.
4. Add stone footings and large iron straps.
5. Add gate planks and hinge blocks as real geometry.
6. Add material IDs and UVs for shared palisade atlas.
7. Build LOD0-LOD3 for each module.
8. Build simple UCX collision primitives.
9. Export each module as FBX or export one kit FBX with separate named meshes, depending on current import tool preference.

## Triangle Budget

- Wall module LOD0: 4k-8k tris.
- Post/end cap LOD0: 1.5k-4k tris.
- Corner module LOD0: 5k-10k tris.
- Gate module LOD0: 6k-12k tris.
- Full review set: under 35k tris at LOD0.

## Texture Deliverables

- `T_AET_Palisade_A01_BC`
- `T_AET_Palisade_A01_N`
- `T_AET_Palisade_A01_ORM`
- Optional detail trim set only if the shared atlas cannot carry all modules cleanly.

## Collision Deliverables

- Wall: simple blocking boxes.
- Post: one box/capsule.
- Corner: two wall boxes plus post collision.
- Gate: closed blocking collision; open variant or Blueprint later.
- No complex-as-simple collision.

## Export Targets

- Blender source: `SourceAssets/Blender/Buildings/Common/Palisade/SM_AET_Palisade_A01/SM_AET_Palisade_A01.blend`
- FBX export folder: `SourceAssets/Exports/Buildings/Common/Palisade/SM_AET_Palisade_A01/`
- Unreal folder: `/Game/Aerathea/Buildings/Common/Palisade/`

## Unreal Validation

- Modules snap cleanly on 400 cm grid.
- Pivots are consistent.
- Collision blocks player movement without snagging.
- Gate opening respects player capsule width when open.
- LODs keep matching module footprints.
- Material slots stay at 1-2 per module.

## Acceptance Checklist

- Wall, post, corner, gate, and end cap modules are present.
- Strong readable timber barrier silhouette.
- Hand-painted timber/stone/iron material language.
- No excessive small modeled detail.
- Collision is simple and runtime-safe.
- Ready to place a small palisade test line in `L_Aerathea_Startup` after DCC source is approved.
