# SM_MKG_WorkshopPropCrate_A01 Modeling Handoff

## Purpose

Create the first-slice DCC handoff for `SM_MKG_WorkshopPropCrate_A01`, a compact Mekgineer workshop storage crate. The asset should establish small-prop scale, gnome engineering material language, simple collision, reusable settlement dressing, and hand-painted texture readability.

## Source References

- Production package: `docs/assets/props/SM_MKG_WorkshopPropCrate_A01/PRODUCTION_PACKAGE.md`
- Concept sheet: `docs/assets/props/SM_MKG_WorkshopPropCrate_A01/concepts/SM_MKG_WorkshopPropCrate_A01_concept_sheet_A01.png`
- Review state: usable first-pass reference; not final locked art until Flamestrike approval.

Reference read notes:

- Front view shows a compact wooden crate with chunky copper/brass corner caps, dark-iron front latch, lid lip, and blue Aetherium inspection mark.
- Side view shows a leather handle loop, hinge/strap plates, and the same reinforced corner language.
- Top view confirms four reinforced corners, dark metal bands, and a centered blue mark.
- Open view is useful hinge/lid reference, but the first static mesh target is a closed crate baseline.
- Scale callout places the crate beside a compact gnome, supporting the 90 x 65 x 55 cm package dimensions.

## Production Target

- Asset type: Static Mesh
- Unreal path: `/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01`
- Source file target: `SourceAssets/Blender/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01.blend`
- FBX export target: `SourceAssets/Exports/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01.fbx`
- Dimensions: 90 cm wide, 65 cm deep, 55 cm tall
- Pivot: bottom center
- Material slot target: 1, maximum 2 only if a future open variant requires an interior material
- Cultural anchor: Gnome Mekgineer, using timber, brass/copper, dark iron, leather, and restrained blue Aetherium paint

## Modeling Constraints

- Preserve the compact chunky box silhouette.
- Model real geometry for crate body, lid lip, large corner caps, dark-iron latch, hinge blocks, side handles, and small feet if used.
- Model only a few large fasteners that read on the silhouette or close-up concept callouts.
- Fake tiny nails, wood grain, small scratches, leather stitching, stamped labels, micro gear marks, and minor dents with texture/normal/AO.
- Use the open-lid concept as construction reference, but export the first asset as a closed static mesh.
- Keep optional future animation in mind by making lid, latch, and hinges cleanly separable in the Blender source, without requiring a Blueprint for this baseline asset.
- Blue Aetherium should be a small inspection mark or paint stamp, not a glowing core unless later approved.

## Blender Setup

- Unit system: Metric, centimeters. Verify final bounding box is 90 x 65 x 55 cm.
- Object origin: bottom center at ground contact.
- Recommended collections:
  - `SM_MKG_WorkshopPropCrate_A01_LOD0`
  - `SM_MKG_WorkshopPropCrate_A01_LOD1`
  - `SM_MKG_WorkshopPropCrate_A01_LOD2`
  - `SM_MKG_WorkshopPropCrate_A01_LOD3`
  - `UCX_Collision`
  - `Future_OpenVariant_Reference`
- Suggested object names:
  - `Body_Box`
  - `Lid_Lip`
  - `Corners_Brass`
  - `Latch_DarkIron`
  - `Hinges_DarkIron`
  - `Handles_Leather`
  - `Feet_Small`
  - `Mark_AetheriumPaint`
- Keep the lid origin and hinge line sensible in the source file for later reuse, even though the exported static mesh is closed.

## Modeling Sequence

1. Block out a 90 x 65 x 55 cm closed crate with slightly exaggerated chunky proportions.
2. Add the lid lip and top plank frame so the crate reads as openable.
3. Add broad timber plank divisions. Keep seams large enough to read without making every plank separate high-cost geometry.
4. Build large copper/brass corner caps and dark metal side straps.
5. Add the front latch as a strong dark-iron focal shape.
6. Add side leather handles with simple loop geometry and plate mounts.
7. Add hinge blocks and rear strap logic using the open concept as construction reference.
8. Add small feet only if they support silhouette and collision stability.
9. Place a small blue Aetherium inspection mark on the front or top as non-emissive material detail.
10. Assign one material ID for the first pass, using atlas regions for wood, metal, leather, and blue paint.
11. Create LOD1-LOD3 manually or by controlled simplification, preserving box, lid lip, latch, and corner-cap contrast.
12. Build a simple UCX box collision and export FBX with LODs and collision.

## Triangle Budget

- LOD0: 1.5k to 2.4k tris
- LOD1: 800 to 1.2k tris
- LOD2: 300 to 500 tris
- LOD3: 80 to 160 tris

LOD reduction priority:

1. Small bevel loops and fasteners.
2. Handle roundness and side-strap bevels.
3. Small feet.
4. Secondary plank seam depth.
5. Latch bevels.

Do not remove the main box, lid lip, corner caps, or latch silhouette first.

## Texture Deliverables

Required textures:

- `T_MKG_WorkshopPropCrate_A01_BC`
- `T_MKG_WorkshopPropCrate_A01_N`
- `T_MKG_WorkshopPropCrate_A01_ORM`

Optional texture:

- `T_MKG_WorkshopPropCrate_A01_E`, only if the blue mark later becomes emissive. Default is non-emissive paint.

Material instance:

- `MI_MKG_WorkshopPropCrate_A01`

Texture plan:

- 1K texture target for the first-slice prop.
- 512 only for distant-clutter variants.
- Hand-painted wood grain, edge wear, metal scratches, leather wear, and baked AO around corner plates.
- Tiny nails and stitching should be texture/normal detail, not geometry.
- Blue Aetherium mark should stay small and readable.

## Collision Deliverables

Use one simple box by default:

- `UCX_SM_MKG_WorkshopPropCrate_A01_00`

Optional only if needed after play test:

- A second simple box for the protruding latch.

Collision rules:

- Do not use complex-as-simple collision.
- Collision should support stable placement as workshop clutter.
- Handle loops, rivets, and latch detail should not affect player collision.

## Export Targets

- Blender: `SourceAssets/Blender/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01.blend`
- FBX: `SourceAssets/Exports/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01.fbx`
- Export contents: closed crate LOD0-LOD3, UCX collision, material slot, applied transforms
- FBX scale: centimeters to Unreal, import result should match 90 x 65 x 55 cm
- Mesh name in FBX: `SM_MKG_WorkshopPropCrate_A01`

## Unreal Validation

- Imports to `/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01`
- Pivot appears at bottom center.
- LODs import and preserve the box/lid/latch/corner-cap read.
- Material slot count is 1 unless an approved variant requires 2.
- UCX collision imports as simple box collision.
- Nanite remains off for this small prop.
- Placement beside a 110 cm gnome marker reads as compact but usable workshop storage.

## Acceptance Checklist

- Reads as a compact Mekgineer workshop crate from 15 m.
- Matches gnome engineering identity without overusing gears, bolts, or glow.
- Dimensions match 90 x 65 x 55 cm.
- LOD0 stays under 2.5k tris.
- LOD0-LOD3 are present.
- One material slot target is met.
- BC, N, ORM textures are planned.
- Blue mark is restrained and non-emissive by default.
- Simple UCX collision is present.
- Pivot is bottom center.
- Source keeps lid/hinge structure understandable for later Blueprint variants.
- No copied franchise design.
