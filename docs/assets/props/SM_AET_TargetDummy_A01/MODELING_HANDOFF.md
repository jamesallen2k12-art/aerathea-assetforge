# SM_AET_TargetDummy_A01 Modeling Handoff

## Purpose

Create the first game-ready target dummy mesh for Aerathea from the approved first-pass concept reference and production package. This is a manual DCC production handoff for Blender or equivalent modeling software; do not treat any procedural placeholder mesh as final art.

## Source References

- Concept sheet: `docs/assets/props/SM_AET_TargetDummy_A01/concepts/SM_AET_TargetDummy_A01_concept_sheet_A01.png`
- Production package: `docs/assets/props/SM_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md`
- Startup map target location: `/Game/Aerathea/Maps/L_Aerathea_Startup`

## Production Target

- Asset name: `SM_AET_TargetDummy_A01`
- Asset type: Static Mesh
- Visual role: starter-town training-yard prop
- Total height: 185 cm
- Crossbar width: 130 cm
- Base footprint: about 110 cm x 110 cm
- Pivot: bottom center at floor contact, `Z=0`
- Forward axis: X forward, matching project convention
- Material slots: 1 target, 2 maximum
- Texture target: 1K baseline, 2K only if the prop becomes a close-view hero asset

## Modeling Constraints

Model as real geometry:

- Central timber post.
- Thick hand-hewn crossbar.
- Broad wrapped straw torso.
- Front target plate or padded leather shield.
- X-foot base.
- Large dark-iron bands.
- Large leather straps and buckles if they affect silhouette.

Fake with texture, normal map, and baked detail:

- Fine straw fibers.
- Wood grain.
- Leather stitching.
- Small nails and rivets.
- Minor scratches and cracks.
- Painted target rings.
- Frayed wrap ends.

Avoid:

- Thin loose strings that shimmer at distance.
- Dense nail, rivet, or straw geometry.
- Bright emissive materials.
- Designs copied from existing franchise target dummies.

## Blender Setup

- Use metric scene units.
- Model to real scale and verify export converts cleanly to Unreal centimeters.
- Keep transforms applied before export.
- Use weighted normals on chunky timber, leather, and iron forms.
- Keep bevels broad and readable; avoid tiny bevel loops that vanish after LOD1.
- Suggested collection: `SM_AET_TargetDummy_A01`

Suggested object names:

- `Post_Main`
- `Crossbar_Main`
- `Torso_StrawWrap`
- `TargetPlate_Front`
- `Base_XFeet`
- `Bands_Iron`
- `Straps_Leather`
- `UCX_SM_AET_TargetDummy_A01_00`
- `UCX_SM_AET_TargetDummy_A01_01`
- `UCX_SM_AET_TargetDummy_A01_02`

## Modeling Sequence

1. Block out the 185 cm height, 130 cm crossbar, and 110 cm base footprint.
2. Match the concept sheet silhouette in front, side, and back views.
3. Separate major material zones: timber, straw, leather, dark iron, painted marks.
4. Add broad bevels and hand-hewn asymmetry without weakening the primary silhouette.
5. Create final low-poly LOD0 within the triangle budget.
6. Create UV0 for the shared texture set and UV1 for lightmaps if needed.
7. Bake high-to-low detail only for broad AO, normals, straps, straw clumps, and surface wear.
8. Author Base Color, Normal, and ORM textures.
9. Create LOD1, LOD2, and LOD3, preserving crossbar width, torso mass, and base footprint.
10. Add simple UCX collision primitives.
11. Export FBX and import into Unreal for scale, collision, material, and LOD validation.

## Triangle Budget

- LOD0: 2.5k to 3.5k tris
- LOD1: 1.4k to 1.8k tris
- LOD2: 600 to 900 tris
- LOD3: 180 to 300 tris

Reduction order:

1. Remove tiny strap thickness and minor band bevels.
2. Simplify underside and backside details.
3. Reduce target plate bevels.
4. Flatten side straps.
5. Simplify torso roundness.
6. Preserve crossbar width, torso mass, post height, and base footprint until the final LOD.

## Texture Deliverables

Required:

- `T_AET_TargetDummy_A01_BC`
- `T_AET_TargetDummy_A01_N`
- `T_AET_TargetDummy_A01_ORM`

Optional only after approval:

- `T_AET_TargetDummy_A01_E`

Material instance:

- `MI_AET_TargetDummy_A01`

Texture notes:

- Hand-painted timber, straw, leather, and dark iron should remain readable at gameplay camera distance.
- Use broad value grouping and baked-AO-style depth.
- Blue Aetherium scoring marks are painted pigment unless a later gameplay requirement needs emissive response.

## Collision Deliverables

Use simple primitives:

- `UCX_SM_AET_TargetDummy_A01_00`: torso and central post.
- `UCX_SM_AET_TargetDummy_A01_01`: crossbar.
- `UCX_SM_AET_TargetDummy_A01_02`: base footprint.

Collision should block pawn movement. Do not use complex-as-simple collision for runtime.

## Export Targets

Source file target:

- `SourceAssets/Blender/Props/Training/SM_AET_TargetDummy_A01.blend`

FBX export target:

- `SourceAssets/Exports/Props/Training/SM_AET_TargetDummy_A01.fbx`

Unreal content targets:

- `/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01`
- `/Game/Aerathea/Materials/Props/MI_AET_TargetDummy_A01`
- `/Game/Aerathea/Textures/Props/TargetDummy_A01/`

Do not commit large binary source files until the source-asset storage policy is approved.

## Unreal Validation

After import:

- Confirm height is 185 cm in Unreal.
- Confirm pivot is bottom center at floor contact.
- Confirm collision blocks pawn movement.
- Confirm LOD0-LOD3 exist and preserve silhouette.
- Confirm material slot count is 1, or 2 maximum with justification.
- Confirm textures use BC, N, and ORM naming.
- Replace the target-dummy blockout in `L_Aerathea_Startup`.
- Run the startup scene validator.
- Run GUI map check and confirm `0 Error(s), 0 Warning(s)`.

## Acceptance Checklist

- Original Aerathea design.
- Matches the concept sheet closely enough for first playable slice.
- Reads as a target dummy from 20 m.
- Chunky timber, straw, leather, and dark iron are clear.
- No copied franchise details.
- No excessive micro-geometry.
- LOD0 is under 4k tris.
- LOD3 still reads as crossbar, torso, post, and base.
- Pivot, scale, collision, and material slots match the production package.
- Ready to replace the startup-scene blockout.
