# SM_AET_PortalArch_A01 Production Package

## Asset Brief

- Asset name: `SM_AET_PortalArch_A01`
- Asset type: Static Mesh
- World: Aerathea
- Category: Portal structure / magical traversal prop
- Current status: Blender source and FBX generated, imported to Unreal, startup portal visual replaced, validation passing; final materials, LODs, collision, and visual signoff still pending
- Working selected direction: Chunky ancient stone archway with hand-hewn blocks, dark-iron reinforcement, worn brass insets, and restrained blue Aetherium channel stones.

This asset replaces the portal-arch blockout in `L_Aerathea_Startup` and becomes the static structure used by `BP_AET_Portal_A01`.

## Concept Reference

- Concept sheet: `docs/assets/props/SM_AET_PortalArch_A01/concepts/SM_AET_PortalArch_A01_concept_sheet_A01.png`
- Modeling handoff: `docs/assets/props/SM_AET_PortalArch_A01/MODELING_HANDOFF.md`
- Build/import status: `docs/assets/props/SM_AET_PortalArch_A01/BUILD_IMPORT_STATUS.md`
- Generation mode: built-in image generation tool.
- Review status: usable first-pass reference; final Flamestrike approval still required before treating it as a locked final art target.

## Gameplay Purpose

The portal arch is the first large interactive landmark prop in the startup scene. It should prove:

- Large prop scale and silhouette.
- Stone, metal, and Aetherium material language.
- Collision for player walk-up.
- Portal blueprint attachment points.
- Visual readability from settlement distance.

It should look important without becoming a raid-scale monument.

## Silhouette Notes

- Broad rectangular arch silhouette with slightly rounded inner aperture.
- Two heavy side columns.
- Thick top capstone.
- Tapered foot stones that visually anchor the asset.
- Inner Aetherium channel should guide the eye toward the portal opening.
- Stone blocks should be large and readable, not many tiny bricks.
- Avoid ornate filigree that becomes noisy at distance.

Primary readable shapes:

1. Left column.
2. Right column.
3. Capstone.
4. Inner portal opening.
5. Blue Aetherium channel markers.

## Scale Notes

- Total height: 420 cm.
- Total width: 360 cm.
- Depth: 90 cm.
- Portal aperture: about 190 cm wide x 300 cm tall.
- Pivot: bottom center between both columns.
- Unreal scale: 1 Unreal unit = 1 cm.
- Player should comfortably stand inside the portal opening.

## Materials And Color Palette

Material slot target: 2 material slots.

Materials:

- Stone body: cool gray, hand-painted edge wear, broad cracks in texture.
- Metal accents: dark iron and muted brass.
- Aetherium inserts: blue stone/glass channels, restrained emissive only if needed.

Palette:

- Stone: `#575A5C`
- Shadow stone: `#2F3436`
- Worn edge stone: `#8B8D86`
- Dark iron: `#171D20`
- Brass: `#8A642A`
- Aetherium blue: `#1E86D9`

Use glow sparingly. The arch should be readable from shape and value, not only from blue light.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a stone portal archway for the world of Aerathea. The design should emphasize a chunky readable arch silhouette, large hand-hewn stone blocks, dark-iron reinforcing bands, muted brass insets, restrained blue Aetherium channel stones, ancient settlement craftsmanship, mysterious but practical mood, and magical traversal gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, back, scale reference, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model real geometry for:

- Major stone blocks.
- Column masses.
- Capstone.
- Base stones.
- Large dark-iron bands.
- Aetherium socket stones.
- Beveled inner portal frame.

Fake with texture/normal map:

- Fine cracks.
- Small chips.
- Surface pitting.
- Tiny rivets.
- Engraved shallow runes.
- Stone grain.

Suggested mesh parts:

- `Column_Left`
- `Column_Right`
- `Capstone_Main`
- `Base_Left`
- `Base_Right`
- `Frame_Inner`
- `Bands_Iron`
- `Sockets_Aetherium`

Keep block count low. Use large stones with strong silhouettes rather than many small masonry pieces.

## Texture And Material Notes

Texture target:

- 2K for stone body.
- 1K for metal/Aetherium accents, or packed into one shared 2K set if using one material.

Texture maps:

- `T_AET_PortalArch_A01_BC`
- `T_AET_PortalArch_A01_N`
- `T_AET_PortalArch_A01_ORM`
- Optional: `T_AET_PortalArch_A01_E`

Material instances:

- `MI_AET_PortalArch_A01_Stone`
- `MI_AET_PortalArch_A01_Accent`

If a single material is feasible, use one packed atlas and name it `MI_AET_PortalArch_A01`.

## Triangle Budget

Large prop target range: 4k to 10k tris.

Recommended:

- LOD0: 7k to 9k tris.
- LOD1: 3.5k to 4.5k tris.
- LOD2: 1.4k to 2k tris.
- LOD3: 450 to 800 tris.

Material slots:

- Target: 2.
- Maximum: 3 only if portal inserts require a separate emissive material.

## LOD Plan

LOD0:

- Full block forms, beveled silhouette, metal bands, Aetherium socket forms.

LOD1:

- Reduce bevels and back-side geometry.
- Simplify metal bands.
- Keep inner aperture shape.

LOD2:

- Merge stone block separations into larger masses.
- Flatten smaller Aetherium sockets.
- Preserve arch outline and aperture.

LOD3:

- Very simple arch silhouette.
- Columns, capstone, aperture, and base only.

Do not destroy the portal opening shape before LOD3.

## Collision Notes

Use simple collision primitives:

- Left column box.
- Right column box.
- Capstone box.
- Optional base boxes.

Keep the portal opening walkable unless gameplay requires blocking.

Recommended collision names:

- `UCX_SM_AET_PortalArch_A01_00`: left column.
- `UCX_SM_AET_PortalArch_A01_01`: right column.
- `UCX_SM_AET_PortalArch_A01_02`: capstone.
- `UCX_SM_AET_PortalArch_A01_03`: base stones.

Do not use complex-as-simple for runtime collision.

## Animation Notes

The static mesh does not animate.

Animation and effects belong in `BP_AET_Portal_A01`:

- Portal core material pulse.
- VFX plane or Niagara effect.
- Activation/deactivation state.
- Interaction prompt.

## Unreal Import Notes

- Static mesh path: `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
- Pivot: bottom center at ground contact.
- Scale: centimeters.
- Forward axis: portal faces +X unless the level convention changes.
- Collision: imported UCX or generated simple boxes.
- Nanite: optional later; off for first bootstrap validation unless explicitly tested.
- LODs: import LOD0-LOD3 or generate and inspect manually.
- Place in `L_Aerathea_Startup` near current blockout portal location: roughly `X=350, Y=0`.

## Folder And Naming Recommendation

Unreal content:

- `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
- `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Stone`
- `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Accent`
- `/Game/Aerathea/Textures/Props/Portal/PortalArch_A01/`

External source, if used later:

- `SourceAssets/Blender/Props/Portal/SM_AET_PortalArch_A01.blend`
- `SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01.fbx`

## Quality Gate Checklist

- Original Aerathea design.
- Portal opening reads clearly at 30 m.
- Player can stand inside aperture.
- Stone blocks are chunky and readable.
- No excessive small brickwork.
- Aetherium glow is restrained.
- LOD0 under 10k tris.
- LOD0-LOD3 planned.
- Collision uses simple primitives.
- Material slots no more than 3.
- Pivot is bottom center.
- Imports at correct scale.
- Works as the static arch for `BP_AET_Portal_A01`.
- GUI map check remains `0 Error(s), 0 Warning(s)`.
