# SM_AET_PortalArch_A01 Modeling Handoff

## Purpose

Create the first-slice DCC handoff for `SM_AET_PortalArch_A01`, the static stone-and-Aetherium portal arch used by `BP_AET_Portal_A01` in the Aerathea startup scene. The mesh should replace the blockout portal structure with a readable mid-poly monumental prop that proves scale, silhouette, collision, material language, LOD behavior, and portal Blueprint attachment readiness.

## Source References

- Production package: `docs/assets/props/SM_AET_PortalArch_A01/PRODUCTION_PACKAGE.md`
- Concept sheet: `docs/assets/props/SM_AET_PortalArch_A01/concepts/SM_AET_PortalArch_A01_concept_sheet_A01.png`
- Exploration directions: `docs/assets/props/SM_AET_PortalArch_A01/PORTAL_EXPLORATION_DIRECTIONS.md`
- Review state: usable first-pass reference; not final locked art until Flamestrike approval.

Reference read notes:

- Front view shows a chunky rectangular arch, broad stone blocks, iron bands, brass brackets, blue Aetherium stones, and stepped base stones.
- Side view confirms a thick narrow-depth column profile with side-mounted Aetherium diamond detail.
- Back view should remain readable but less ornate, with the aperture and block structure preserved.
- Material callouts establish stone, dark iron, brass, and Aetherium blue as the primary material language.

## Production Target

- Asset type: Static Mesh
- Unreal path: `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
- Source file target: `SourceAssets/Blender/Props/Portal/SM_AET_PortalArch_A01.blend`
- FBX export target: `SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01.fbx`
- Final target dimensions: 900-1100 cm wide, 1200-1400 cm tall, 220-320 cm deep
- Minimum clear traversal height: 1000 cm / 10 m / about 33 ft
- Portal aperture: about 650-800 cm wide by 1000 cm tall
- Pivot: bottom center between both columns, at ground contact
- Forward axis: portal faces +X unless level convention changes
- Material slot target: 2, maximum 3 only if Aetherium needs separate emissive handling
- Current imported startup mesh was built to the older 360 cm x 420 cm x 90 cm target; treat it as review-only and rebuild or rescale before final signoff.

## Modeling Constraints

- Preserve the large arch silhouette before adding decorative forms.
- Model real geometry for columns, capstone, base blocks, beveled inner frame, large iron bands, brass brackets, and Aetherium socket stones.
- Use broad, hand-cut stone blocks. Do not turn the arch into tiny brickwork.
- Fake fine cracks, small chips, stone pitting, shallow rune scratches, and tiny rivets with normal/AO/albedo detail.
- Keep the portal aperture open and clean for player, Giant, large NPC, large enemy, dungeon, raid, and city traversal.
- Normal player characters should feel small beside the arch.
- Final visual direction should feel old, mysterious, awe-inspiring, and discovered in a large world rather than newly built for a small settlement.
- Avoid relying on glow for readability. Blue accents should support, not define, the silhouette.
- Keep backside detail simpler than the front, but do not leave it unfinished.

## Blender Setup

- Unit system: Metric, centimeters. Verify dimensions against a 180 cm humanoid scale marker, a 470 cm Giant scale marker, and a 1000 cm clearance marker.
- Object origin: world origin at bottom center between columns.
- Facing: front of arch along +X.
- Recommended collections:
  - `SM_AET_PortalArch_A01_LOD0`
  - `SM_AET_PortalArch_A01_LOD1`
  - `SM_AET_PortalArch_A01_LOD2`
  - `SM_AET_PortalArch_A01_LOD3`
  - `UCX_Collision`
  - `Reference_Scale`
- Suggested object names:
  - `Column_Left`
  - `Column_Right`
  - `Capstone_Main`
  - `Base_Left`
  - `Base_Right`
  - `Frame_Inner`
  - `Bands_Iron`
  - `Brackets_Brass`
  - `Sockets_Aetherium`
- Apply transforms before export. Keep bevel modifiers unapplied until review if the source remains editable, then apply or bake them for the export mesh.

## Modeling Sequence

1. Block out the full 900-1100 cm x 1200-1400 cm x 220-320 cm bounding form with two columns, stepped base stones, capstone, and the inner aperture.
2. Cut the aperture to the 650-800 cm wide x 1000 cm tall target and check that a 1000 cm clearance marker can pass through it.
3. Build the main stone blocks as large separated masses with bevels that read in silhouette.
4. Add the inner arch ring and Aetherium channel blocks. Keep the channel pieces large enough to read at distance.
5. Add dark-iron bands around columns and capstone. Use a few large modeled rivets only where visible in silhouette or close-up.
6. Add brass corner brackets and diamond-shaped Aetherium sockets on the front and side faces.
7. Simplify the back face into readable stone courses, iron bands, and aperture structure without matching all front ornamentation.
8. Add base stones and small foot anchors, keeping collision-friendly ground contact.
9. Assign material IDs for stone and accent material. If emissive is separated, keep it restricted to Aetherium stones.
10. Create LOD1-LOD3 manually or by controlled decimation, preserving aperture shape and the main arch outline.
11. Build UCX collision boxes and verify the opening remains walkable.
12. Export FBX with LODs and collision included.

## Triangle Budget

- LOD0: 10k to 14k tris
- LOD1: 5k to 7k tris
- LOD2: 2k to 3k tris
- LOD3: 700 to 1200 tris

LOD reduction priority:

1. Tiny rivets and small bevel loops.
2. Backside stone relief.
3. Secondary brass cuts and bracket bevels.
4. Small Aetherium socket bevels.
5. Stone block separation depth.
6. Minor base stone details.

Do not collapse the portal aperture or primary column/capstone silhouette before LOD3.

## Texture Deliverables

Required textures:

- `T_AET_PortalArch_A01_BC`
- `T_AET_PortalArch_A01_N`
- `T_AET_PortalArch_A01_ORM`

Optional texture:

- `T_AET_PortalArch_A01_E`, only for restrained Aetherium emissive.

Material instances:

- `MI_AET_PortalArch_A01_Stone`
- `MI_AET_PortalArch_A01_Accent`

Texture plan:

- Stone body: 2K target, broad hand-painted blocks, chipped edges, baked-AO-style depth.
- Accent material: 1K target or packed into shared 2K atlas, covering dark iron, brass, and Aetherium.
- Fine cracks, shallow runes, pitting, and small edge chips belong in texture and normal maps.

## Collision Deliverables

Use simple UCX primitives:

- `UCX_SM_AET_PortalArch_A01_00`: left column
- `UCX_SM_AET_PortalArch_A01_01`: right column
- `UCX_SM_AET_PortalArch_A01_02`: capstone
- `UCX_SM_AET_PortalArch_A01_03`: base stones

Collision rules:

- Keep the portal aperture walkable.
- Do not use complex-as-simple runtime collision.
- Avoid collision on small decorative sockets or rivets.
- Collision should feel stable when a player approaches and stands inside the opening.

## Export Targets

- Blender: `SourceAssets/Blender/Props/Portal/SM_AET_PortalArch_A01.blend`
- FBX: `SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01.fbx`
- Export contents: LOD0-LOD3, UCX collision, material slots, applied transforms
- FBX scale: centimeters to Unreal, final import result should match the 900-1100 cm x 1200-1400 cm x 220-320 cm target envelope with a 1000 cm clear traversal aperture
- Mesh name in FBX: `SM_AET_PortalArch_A01`

## Unreal Validation

- Imports to `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
- Pivot appears at bottom center ground contact.
- Front faces +X.
- LODs import and switch without destroying the aperture.
- Material slots are 2, or 3 only if emissive is separated.
- UCX collision imports as simple boxes and does not block the portal opening.
- Nanite remains off for first bootstrap validation unless explicitly tested later.
- Placement in `L_Aerathea_Startup` near the current portal blockout reads clearly at settlement distance.

## Acceptance Checklist

- Original Aerathea portal design, not copied franchise architecture.
- Monumental portal silhouette reads from 30 m.
- Dimensions match the package target.
- 1000 cm / 10 m / about 33 ft clear traversal aperture is preserved.
- Normal player characters feel small beside the portal.
- Stone blocks are chunky and readable.
- Blue Aetherium is restrained and purposeful.
- LOD0 fits the 10k-14k final monument target.
- LOD0-LOD3 are present.
- Simple UCX collision is present.
- Material slot count is within target.
- BC, N, ORM textures are planned; emissive is optional and justified.
- Static mesh is ready to support `BP_AET_Portal_A01`.
