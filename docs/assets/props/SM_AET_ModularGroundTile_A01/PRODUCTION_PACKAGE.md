# SM_AET_ModularGroundTile_A01 Production Package

## Asset Brief

- Asset name: `SM_AET_ModularGroundTile_A01`
- Asset type: Static Mesh
- World: Aerathea
- Category: Modular ground / startup scene test tile
- Current status: Concept sheet generated, modeling handoff ready

This asset replaces the flat startup ground plane with a reusable modular tile that can test scale, collision, material readability, and early settlement dressing.

## Concept Reference

- Concept sheet: `docs/assets/props/SM_AET_ModularGroundTile_A01/concepts/SM_AET_ModularGroundTile_A01_concept_sheet_A01.png`
- Modeling handoff: `docs/assets/props/SM_AET_ModularGroundTile_A01/MODELING_HANDOFF.md`
- Generation mode: built-in image generation tool.
- Review status: usable first-pass reference; final Flamestrike approval still required before treating it as a locked final art target.

## Gameplay Purpose

The modular ground tile is the first controlled walking surface for Aerathea production validation. It should prove:

- Reliable walkable collision.
- Texture scale.
- Material readability.
- Modular snapping.
- Simple light/shadow behavior.

It is not a final terrain system. It is a repeatable test tile for asset review and early scene assembly.

## Silhouette Notes

- Mostly flat rectangular or square tile.
- Slightly beveled edges.
- Subtle raised stone/dirt variation.
- Optional corner chips or edge breaks, kept broad.
- No high-frequency pebble geometry.
- Tile should not visibly pop or create snag points for player movement.

Primary readable shapes:

1. Square tile boundary.
2. Broad stone slabs or packed earth patches.
3. Slight beveled outer edge.
4. Low-height surface variation.

## Scale Notes

- Recommended size: 400 cm x 400 cm.
- Height thickness: 10 cm to 20 cm.
- Pivot: tile center at top walking surface or bottom center by project convention. Use one convention consistently.
- Preferred pivot for modular snapping: center of tile at `Z=0` top surface.
- Unreal scale: 1 Unreal unit = 1 cm.
- Snaps to 400 cm grid.

## Materials And Color Palette

Material slot target: 1.

Material language:

- Packed earth base.
- Broad embedded stone slabs.
- Soft moss or grass edge tint only if needed.
- Hand-painted AO around slab edges.

Palette:

- Packed earth: `#4A3B2B`
- Warm stone: `#6A6659`
- Dark crevice: `#24231F`
- Dry grass tint: `#6E7442`
- Cool gray highlight: `#8A897C`

Avoid beige-dominant output. Keep enough gray/green/dark contrast that it does not become a flat tan tile.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a modular ground tile for the world of Aerathea. The design should emphasize a clean 400 cm square gameplay footprint, broad packed-earth and stone-slab shapes, low beveled edges, hand-painted surface contrast, subtle moss or dry grass accents, practical starter-settlement identity, grounded exploration mood, and walkable collision gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive effects, and MMO-friendly production design. Present it as a top-down asset sheet with side profile, tiling preview, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model real geometry for:

- Tile base.
- Outer bevel.
- A few broad raised slab edges if needed.
- Major broken corner shapes.

Fake with texture/normal map:

- Pebbles.
- Dirt grain.
- Small cracks.
- Moss pattern.
- Minor chips.
- Fine height variation.

Suggested mesh parts:

- `Tile_Base`
- `Edge_Bevel`
- `Slab_BroadShapes`

The mesh must stay walkable. Any raised stone detail should be low enough to avoid collision snagging or should not affect collision.

## Texture And Material Notes

Texture target:

- 1K for initial tile.
- 2K only if tile becomes a primary terrain module.

Texture maps:

- `T_AET_ModularGroundTile_A01_BC`
- `T_AET_ModularGroundTile_A01_N`
- `T_AET_ModularGroundTile_A01_ORM`

Material instance:

- `MI_AET_ModularGroundTile_A01`

Texture requirements:

- Should tile cleanly when repeated.
- Avoid obvious directional streaks.
- Include broad hand-painted AO around major slab seams.
- Keep normal intensity modest for readable stylized terrain.

## Triangle Budget

Small prop / modular environment piece:

- LOD0: 300 to 900 tris.
- LOD1: 150 to 350 tris.
- LOD2: 50 to 120 tris.
- LOD3: 2 to 20 tris, depending on distance use.

Material slots:

- Target: 1.

## LOD Plan

LOD0:

- Tile bevel, broad slab surface forms, simple edge breakup.

LOD1:

- Reduce bevel subdivisions.
- Simplify slab surface forms.

LOD2:

- Mostly flat tile with preserved boundary shape.

LOD3:

- Flat plane or simple box.

Keep the tile footprint exact across LODs to avoid visible snapping issues.

## Collision Notes

Collision should be simple and stable:

- One box collision matching the tile footprint.
- Top surface at consistent walk height.

Recommended:

- `UCX_SM_AET_ModularGroundTile_A01_00`

Avoid per-slab collision. Collision should not match small visual cracks or surface texture.

## Animation Notes

No animation.

Future variants can include:

- Grass overlay decals.
- Dirt path decals.
- Snow/sand material variant.

Do not animate the base tile.

## Unreal Import Notes

- Static mesh path: `/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01`
- Pivot: center at top surface `Z=0` for grid snapping, unless project adopts bottom-center for all modular pieces.
- Scale: centimeters.
- Snap grid: 400 cm.
- Collision: simple box.
- LODs: LOD0-LOD3.
- Nanite: off for initial tile.
- Replace or supplement the current startup ground plane after validation.

## Folder And Naming Recommendation

Unreal content:

- `/Game/Aerathea/Props/Environment/SM_AET_ModularGroundTile_A01`
- `/Game/Aerathea/Materials/Environment/MI_AET_ModularGroundTile_A01`
- `/Game/Aerathea/Textures/Environment/ModularGroundTile_A01/`

External source, if used later:

- `SourceAssets/Blender/Props/Environment/SM_AET_ModularGroundTile_A01.blend`
- `SourceAssets/Exports/Props/Environment/SM_AET_ModularGroundTile_A01.fbx`

## Quality Gate Checklist

- Exact 400 cm modular footprint.
- Walkable collision is simple and stable.
- No collision snagging from decorative detail.
- Texture tiles cleanly.
- Material reads as Aerathea hand-painted ground.
- LOD footprints remain consistent.
- 1 material slot.
- No emissive effects.
- Pivot supports snapping.
- GUI map check remains `0 Error(s), 0 Warning(s)`.
