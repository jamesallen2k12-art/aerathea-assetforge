# SM_AET_TargetDummy_A01 Production Package

## Asset Brief

- Asset name: `SM_AET_TargetDummy_A01`
- Asset type: Static Mesh
- World: Aerathea
- Category: Training prop / combat-readability test prop
- Current status: Concept sheet generated, modeling handoff ready
- Working selected direction: Rugged militia training dummy with chunky timber frame, wrapped straw core, patched leather hit zones, dark-iron bracing, and painted blue Aetherium scoring marks.

This asset replaces the current target-dummy blockout in `L_Aerathea_Startup` after concept approval and modeling.

## Concept Reference

- Concept sheet: `docs/assets/props/SM_AET_TargetDummy_A01/concepts/SM_AET_TargetDummy_A01_concept_sheet_A01.png`
- Modeling handoff: `docs/assets/props/SM_AET_TargetDummy_A01/MODELING_HANDOFF.md`
- Generation mode: built-in image generation tool.
- Review status: usable first-pass reference; final Flamestrike approval still required before treating it as a locked final art target.

## Gameplay Purpose

The target dummy is the first combat-readability prop for Aerathea. It should support early melee, ranged, spell, hit-reaction, collision, material, and scale checks without becoming visually noisy.

Primary uses:

- Training-yard prop in starter settlements.
- Combat ability testing target.
- Scale and silhouette reference beside player and race markers.
- Material and damage-decal test object.
- Early collision validation object.

It should read immediately as an interactive target from medium distance and still feel like an original Aerathea world prop.

## Silhouette Notes

- Strong vertical central post.
- Broad shoulder crossbar with slightly uneven hand-hewn timber ends.
- Rounded straw torso mass bound with leather belts.
- Circular or shield-like front hit plate for clear player aim.
- Short base tripod or X-foot support to keep the dummy grounded.
- No tiny spikes, excessive nails, or overbuilt mechanical parts.
- Shape should read from the side as a practice dummy, not a scarecrow.
- Top profile can include a simple cloth hood, tied straw bundle, or carved wooden head cap.

Readable primary shapes:

1. Wide crossbar.
2. Straw torso oval.
3. Central timber post.
4. Stable base feet.
5. High-contrast front target plate.

## Scale Notes

- Total height: 185 cm.
- Torso center height: 120 cm.
- Crossbar width: 130 cm.
- Base footprint: about 110 cm x 110 cm.
- Pivot: center bottom at floor contact, `Z=0`.
- Unreal scale: 1 Unreal unit = 1 cm.
- Should look correct beside:
  - Human player marker: 180 cm.
  - Gnome marker: 110 cm.
  - Minotaur marker: 270 cm.

## Materials And Color Palette

Material slot target: 1 material slot if practical, 2 maximum.

Primary material language:

- Weathered timber: warm brown, hand-painted edge highlights.
- Straw wrap: muted golden tan, clumped broad shapes rather than fine individual strands.
- Leather straps: dark umber, worn edges, large buckles faked in normal/texture where possible.
- Dark iron bracing: low-saturation charcoal, slightly blue-tinted worn edges.
- Paint marks: desaturated training-yard red and restrained blue Aetherium scoring marks.

Palette:

- Timber: `#6A3F21`
- Straw: `#B88A3A`
- Leather: `#3B2418`
- Dark iron: `#1D2224`
- Cloth wraps: `#6D6A5C`
- Training red: `#8C2D22`
- Aetherium mark blue: `#1E7FD1`

Avoid strong emissive on this asset. If a blue mark is used, it should be painted pigment or very faint non-emissive magic chalk, not a glowing lamp.

## Visual Exploration Prompts

Use these for concept exploration if generating images. All prompts must produce original Aerathea designs and avoid copying existing franchise training dummies.

1. Create an original stylized fantasy MMORPG concept image of a rugged wooden target dummy for the world of Aerathea. The design should emphasize a chunky crossbar silhouette, weathered timber, wrapped straw torso, dark leather belts, frontier training-yard culture, practical militia mood, and melee practice gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing non-emissive blue scoring marks, and MMO-friendly production design. Present it as a single hero render on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.
2. Create an original stylized fantasy MMORPG concept image of a settlement training dummy for the world of Aerathea. The design should emphasize a shield-shaped front target, rough-hewn timber spine, straw padding, patched leather impact zones, warm brown and tan color language, human frontier identity, workmanlike mood, and combat tutorial gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing blue chalk target marks, and MMO-friendly production design. Present it as a concept sheet with front and side views on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.
3. Create an original stylized fantasy MMORPG concept image of a dwarven-influenced target dummy for the world of Aerathea. The design should emphasize a compact heavy silhouette, stone-weighted base, iron bands, stout timber post, muted brass fasteners faked as texture detail, mountain-forged practicality, sturdy mood, and weapon-testing gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, restrained blue rune paint, and MMO-friendly production design. Present it as an asset board on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.
4. Create an original stylized fantasy MMORPG concept image of a gnome workshop target dummy for the world of Aerathea. The design should emphasize a short clever silhouette, compact brass scoring plates, timber frame, leather straps, simple spring-loaded arms, blue Aetherium calibration marks, Mekgineer culture, curious testing-lab mood, and gadget practice gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, very sparing emissive accents only on tiny calibration pips, and MMO-friendly production design. Present it as a concept sheet on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.
5. Create an original stylized fantasy MMORPG concept image of an elven training dummy for the world of Aerathea. The design should emphasize graceful curved living-wood supports, woven target wraps, silverleaf binding motifs, pale moonlit color language, elegant ranger-yard identity, calm disciplined mood, and archery practice gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, non-emissive blue-white paint accents, and MMO-friendly production design. Present it as a clean turnaround. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.
6. Create an original stylized fantasy MMORPG concept image of an orc clan training dummy for the world of Aerathea. The design should emphasize an upright powerful silhouette, thick timber trunk, hide-wrapped torso, bone-colored target plates, red clan paint, honorable warrior-yard identity, disciplined combat mood, and heavy-weapon practice gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no excessive gore or spikes, and MMO-friendly production design. Present it as an asset board on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.
7. Create an original stylized fantasy MMORPG concept image of a minotaur training dummy for the world of Aerathea. The design should emphasize a massive reinforced silhouette, raw iron bands, hide padding, bone lashings, heavy base stakes, plains-warrior identity, brutal strength-testing mood, and boss-scale impact gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, simple efficient construction, and MMO-friendly production design. Present it as a scale comparison sheet on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.
8. Create an original stylized fantasy MMORPG concept image of a dark elf dueling dummy for the world of Aerathea. The design should emphasize a narrow elegant silhouette, dark stained wood, obsidian target plate, violet painted crescent marks, refined oath-bound culture, tense moonlit mood, and precision-strike gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, restrained non-glowing accents, and MMO-friendly production design. Present it as a single hero render on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.
9. Create an original stylized fantasy MMORPG concept image of a Drakhar desert target dummy for the world of Aerathea. The design should emphasize a sun-baked post, wrapped reptile-hide practice pads, bone charm silhouette, ember-colored paint, relic-hunter identity, dry arcane mood, and magic-sensing practice gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, tiny non-emissive arcane charms, and MMO-friendly production design. Present it as a concept sheet on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.
10. Create an original stylized fantasy MMORPG concept image of a universal starter-town target dummy for the world of Aerathea. The design should emphasize a clean readable silhouette, broad straw torso, timber crossbar, sturdy base, patched leather target zones, neutral settlement color language, practical training-yard mood, and early combat tutorial gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing blue painted score marks, and MMO-friendly production design. Present it as a production asset sheet with front, side, back, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Recommended Concept Direction

Use prompt 10 as the first production direction.

Reason:

- It is faction-neutral and suitable for the first playable slice.
- It proves core material language: timber, straw, leather, dark iron, painted marks.
- It keeps silhouette readability high.
- It avoids overcommitting the first prop to a single race culture.
- It can be reused in human, dwarf, gnome, or mixed settlement training yards with small material variants later.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a universal starter-town target dummy for the world of Aerathea. The design should emphasize a clean readable silhouette, broad wrapped straw torso, thick hand-hewn timber crossbar, sturdy X-foot base, patched leather target zones, dark iron reinforcing bands, warm timber and straw color language, practical frontier training-yard identity, grounded heroic-fantasy mood, and early combat tutorial gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing blue painted Aetherium score marks, and MMO-friendly production design. Present it as a production asset sheet with front, side, back, scale reference, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model real geometry for:

- Central timber post.
- Crossbar beam.
- Straw torso mass.
- Front target plate or padded leather shield.
- Base feet.
- Major iron bands.
- Large leather strap shapes.

Fake with texture/normal map:

- Wood grain.
- Straw fibers.
- Leather stitching.
- Scratches.
- Small nails.
- Minor cracks.
- Painted target rings.
- Fine frayed wrap detail.

Suggested mesh parts:

- `Post_Main`
- `Crossbar_Main`
- `Torso_StrawWrap`
- `TargetPlate_Front`
- `Base_XFeet`
- `Bands_Iron`
- `Straps_Leather`

Keep proportions chunky. Do not add thin dangling strings that will shimmer at distance unless they are broad enough to survive LODs.

## UV, Texture, And Material Notes

Texture set target: 1K for baseline, 2K if the asset becomes a frequently viewed hero prop.

Texture maps:

- `T_AET_TargetDummy_A01_BC`
- `T_AET_TargetDummy_A01_N`
- `T_AET_TargetDummy_A01_ORM`

Optional only if later approved:

- `T_AET_TargetDummy_A01_E` for faint magical scoring marks. Default target is no emissive map.

UV plan:

- Single 0-1 UV set for material textures.
- Second UV channel for lightmap if required by project lighting workflow.
- Prioritize front torso, target plate, and top silhouette.
- Mirror base-foot undersides only if needed.
- Avoid tiny unique UV islands for nails or stitches; bake those into larger strap/wood islands.

Material instances:

- `MI_AET_TargetDummy_A01`
- Optional future variants:
  - `MI_AET_TargetDummy_A01_Dwarven`
  - `MI_AET_TargetDummy_A01_Gnome`
  - `MI_AET_TargetDummy_A01_Orc`

## Triangle Budget

Small prop target range: 500 to 4k tris.

Recommended:

- LOD0: 2.5k to 3.5k tris.
- LOD1: 1.4k to 1.8k tris.
- LOD2: 600 to 900 tris.
- LOD3: 180 to 300 tris.

Material slots:

- Target: 1.
- Maximum: 2 if straw/leather/wood packing becomes impractical.

## LOD Plan

LOD0:

- Full silhouette.
- Modeled post, crossbar, torso, base feet, large straps, major iron bands.
- Broad target-plate bevels.

LOD1:

- Reduce bevel loops.
- Merge minor strap thickness.
- Simplify base feet and iron bands.
- Preserve torso/crossbar silhouette.

LOD2:

- Simplify target plate to broad slab.
- Remove or flatten minor side straps.
- Reduce torso roundness.
- Keep crossbar width and base footprint readable.

LOD3:

- Billboard-like simple mesh silhouette.
- Crossbar, torso, post, and base only.
- No small bands or separate strap details.

Never reduce the crossbar width, torso mass, or base footprint first.

## Collision Notes

Use simple collision:

- One capsule or box for central post/torso.
- One box for crossbar.
- One box for base footprint.

Recommended collision asset:

- `UCX_SM_AET_TargetDummy_A01_00`: torso/post.
- `UCX_SM_AET_TargetDummy_A01_01`: crossbar.
- `UCX_SM_AET_TargetDummy_A01_02`: base.

Gameplay notes:

- Collision should block pawn movement.
- Weapon hit traces can target the mesh or a future `BP_AET_TargetDummy_A01`.
- Do not use complex-as-simple for runtime collision.

## Animation Notes

Static mesh baseline has no required animation.

Future optional blueprint behavior:

- Small hit wobble using timeline rotation.
- Floating damage numbers.
- Hit decal spawn.
- Training score event.
- Audio cue for wood/straw impact.

If wobble is needed later, create a blueprint actor:

- `BP_AET_TargetDummy_A01`

and keep `SM_AET_TargetDummy_A01` static and reusable.

## Unreal Import Notes

- Static mesh path: `/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01`
- Material path: `/Game/Aerathea/Materials/Props/MI_AET_TargetDummy_A01`
- Texture path: `/Game/Aerathea/Textures/Props/TargetDummy_A01/`
- Pivot: bottom center at ground contact.
- Scale: centimeters.
- Forward axis: X forward if exported from Blender using project convention.
- Collision: imported UCX primitives or generated simple collision in Unreal.
- Nanite: off for this small prop unless project policy changes.
- Generate lightmap UVs if baked lighting is used.
- LOD import: import LOD0-LOD3 from source DCC or generate LODs in Unreal and inspect silhouette.
- Place replacement in `L_Aerathea_Startup` near current blockout location: roughly `X=-50, Y=350`.

Recommended names:

- `SM_AET_TargetDummy_A01`
- `MI_AET_TargetDummy_A01`
- `T_AET_TargetDummy_A01_BC`
- `T_AET_TargetDummy_A01_N`
- `T_AET_TargetDummy_A01_ORM`
- Optional: `BP_AET_TargetDummy_A01`

## Folder And Naming Recommendation

Source docs:

- `docs/assets/props/SM_AET_TargetDummy_A01/PRODUCTION_PACKAGE.md`

Unreal content:

- `/Game/Aerathea/Props/Training/SM_AET_TargetDummy_A01`
- `/Game/Aerathea/Materials/Props/MI_AET_TargetDummy_A01`
- `/Game/Aerathea/Textures/Props/TargetDummy_A01/T_AET_TargetDummy_A01_BC`
- `/Game/Aerathea/Textures/Props/TargetDummy_A01/T_AET_TargetDummy_A01_N`
- `/Game/Aerathea/Textures/Props/TargetDummy_A01/T_AET_TargetDummy_A01_ORM`
- `/Game/Aerathea/Blueprints/Props/BP_AET_TargetDummy_A01`

External source files, if used later:

- `SourceAssets/Blender/Props/Training/SM_AET_TargetDummy_A01.blend`
- `SourceAssets/Exports/Props/Training/SM_AET_TargetDummy_A01.fbx`

Do not commit large external source files until project source-asset policy is decided.

## Quality Gate Checklist

- Original to Aerathea.
- Reads as a target dummy from 20 m.
- Primary silhouette survives LOD3.
- Fits 185 cm height target.
- Does not copy existing franchise target dummies.
- Uses timber, straw, leather, and dark iron clearly.
- No excessive micro-detail.
- No unnecessary emissive effects.
- LOD0 under 4k tris.
- LOD0-LOD3 present or planned.
- 1 material slot target met, 2 maximum.
- BC, N, ORM texture set planned.
- Collision uses simple primitives.
- Pivot is bottom center.
- Imports at correct scale.
- Replaces the startup blockout cleanly.
- GUI map check remains `0 Error(s), 0 Warning(s)`.
