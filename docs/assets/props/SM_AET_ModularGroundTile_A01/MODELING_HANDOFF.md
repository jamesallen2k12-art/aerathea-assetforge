# SM_AET_ModularGroundTile_A01 Modeling Handoff

## Purpose

Create the first-slice DCC handoff for `SM_AET_ModularGroundTile_A01`, a repeatable walkable ground tile for Aerathea startup-scene validation. The asset should prove modular snapping, collision stability, texture scale, material readability, and low-cost LOD behavior without becoming a final terrain system.

## Source References

- Production package: `docs/assets/props/SM_AET_ModularGroundTile_A01/PRODUCTION_PACKAGE.md`
- Concept sheet: `docs/assets/props/SM_AET_ModularGroundTile_A01/concepts/SM_AET_ModularGroundTile_A01_concept_sheet_A01.png`
- Review state: usable first-pass reference; not final locked art until Flamestrike approval.

Reference read notes:

- Concept sheet defines a 400 cm x 400 cm tile with top, side, scale, tiling preview, and material callouts.
- The side profile visually reads as a low 6 cm slab; the production package allows a 10 to 20 cm thickness. Keep the top surface and 400 cm footprint authoritative, and flag thickness choice for review if it must differ from the concept.
- Surface language is broad gray stone slabs embedded in packed brown earth, with sparse moss/dry grass accents.
- The 2x2 tiling preview shows that edge continuity matters more than individual rock detail.

## Production Target

- Asset type: Static Mesh
- Unreal path: `/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01`
- Source file target: `SourceAssets/Blender/Props/Environment/SM_AET_ModularGroundTile_A01.blend`
- FBX export target: `SourceAssets/Exports/Props/Environment/SM_AET_ModularGroundTile_A01.fbx`
- Footprint: exactly 400 cm x 400 cm
- Visual thickness: target 6 cm if following the concept, up to 10 to 20 cm only if art direction confirms the package thickness
- Pivot: center of tile at top walking surface, `Z=0`
- Snap grid: 400 cm
- Material slot target: 1

## Modeling Constraints

- Preserve exact square footprint across all LODs.
- Keep the top walkable surface low and stable.
- Model real geometry for the tile base, outer bevel, broad slab lips, and major broken-corner silhouette only.
- Use textures and normal maps for pebbles, dirt grain, minor cracks, moss, fine chips, and small height variation.
- Avoid per-pebble or per-crack geometry.
- Do not create raised forms that snag player collision.
- Avoid directional streaks or unique edge marks that make repeated tiles obvious.
- Keep color balance earthy but not beige-dominant; use gray stone, darker crevices, and restrained green accents.

## Blender Setup

- Unit system: Metric, centimeters. Verify the tile measures exactly 400 x 400 cm.
- Object origin: center of tile at top surface `Z=0`.
- Tile underside should sit below `Z=0`; visual relief should not push collision above a smooth walk plane unless approved.
- Recommended collections:
  - `SM_AET_ModularGroundTile_A01_LOD0`
  - `SM_AET_ModularGroundTile_A01_LOD1`
  - `SM_AET_ModularGroundTile_A01_LOD2`
  - `SM_AET_ModularGroundTile_A01_LOD3`
  - `UCX_Collision`
  - `Tiling_Test_2x2`
- Suggested object names:
  - `Tile_Base`
  - `Edge_Bevel`
  - `Slab_BroadShapes`
  - `Surface_Relief`
- Add a temporary 2x2 linked-instance tiling test in the source file, but do not export those duplicates as part of the asset.

## Modeling Sequence

1. Block out an exact 400 x 400 cm tile with the pivot at top center.
2. Establish underside thickness. Use the concept's 6 cm side profile unless art direction requests the package's 10 to 20 cm thickness.
3. Add a low, broad outer bevel. Keep all edges compatible with clean 400 cm grid snapping.
4. Lay out broad stone slab regions on the top surface with large readable shapes.
5. Keep slab relief shallow. Any visual height change should be texture-driven or low enough to avoid movement issues.
6. Add optional broken-corner silhouette only where it does not break the exact collision footprint.
7. Assign one material ID for the full tile.
8. Test 2x2 and 3x3 repetition in Blender with linked instances. Check that border seams do not create obvious repeating seams.
9. Create LOD1-LOD3 while preserving the exact 400 cm footprint.
10. Build one UCX box collision matching the footprint and top walk plane.
11. Export FBX with LODs and collision.

## Triangle Budget

- LOD0: 300 to 900 tris
- LOD1: 150 to 350 tris
- LOD2: 50 to 120 tris
- LOD3: 2 to 20 tris

LOD reduction priority:

1. Minor bevel segments.
2. Non-silhouette slab relief.
3. Broken-corner geometry.
4. Surface variation geometry.

Every LOD must retain the exact 400 x 400 cm footprint to prevent snapping gaps or overlaps.

## Texture Deliverables

Required textures:

- `T_AET_ModularGroundTile_A01_BC`
- `T_AET_ModularGroundTile_A01_N`
- `T_AET_ModularGroundTile_A01_ORM`

Material instance:

- `MI_AET_ModularGroundTile_A01`

Texture plan:

- 1K texture target for first-slice validation.
- 2K only if promoted to primary terrain module.
- Hand-painted AO around slab seams and tile edge.
- Modest normal intensity, no spiky pebble normals that imply collision problems.
- Texture must tile cleanly when repeated.
- No emissive texture.

## Collision Deliverables

Use one simple box:

- `UCX_SM_AET_ModularGroundTile_A01_00`

Collision rules:

- Collision should match the 400 x 400 cm footprint.
- Top walking surface should be flat and consistent at `Z=0`.
- Do not add per-slab or per-pebble collision.
- Collision must not create seams or step-ups between adjacent snapped tiles.

## Export Targets

- Blender: `SourceAssets/Blender/Props/Environment/SM_AET_ModularGroundTile_A01.blend`
- FBX: `SourceAssets/Exports/Props/Environment/SM_AET_ModularGroundTile_A01.fbx`
- Export contents: LOD0-LOD3, UCX collision, one material slot, applied transforms
- FBX scale: centimeters to Unreal, import result should match exactly 400 x 400 cm
- Mesh name in FBX: `SM_AET_ModularGroundTile_A01`

## Unreal Validation

- Imports to `/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01`
- Pivot is center-top at `Z=0`.
- Tile snaps cleanly on a 400 cm grid.
- LODs switch without visible gaps, overlaps, or footprint changes.
- Material slot count is 1.
- UCX collision imports as a single stable walkable box.
- Repeated 2x2 and 3x3 placement shows no severe texture seams.
- Nanite remains off for initial validation.

## Acceptance Checklist

- Exact 400 cm modular footprint.
- Walkable collision is simple, flat, and stable.
- Pivot supports grid snapping.
- No collision snagging from decorative forms.
- Texture tiles cleanly.
- Material reads as Aerathea hand-painted ground, not beige filler.
- LOD0 stays under 900 tris.
- LOD0-LOD3 are present.
- One material slot.
- BC, N, ORM textures are planned.
- No emissive effects.
- Ready to replace or supplement the startup ground plane for validation.
