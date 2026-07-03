# SM_AET_PortalArch_A01 Production Package

## Asset Brief

- Asset name: `SM_AET_PortalArch_A01`
- Asset type: Static Mesh
- World: Aerathea
- Category: Portal structure / magical traversal prop
- Current status: 10 m universal scale rebuild complete; Blender source and FBX regenerated, imported to Unreal, startup portal visual replaced, sockets/LODs/UCX collision present, focused portal validation passing, and startup validation passing. Final art direction approval, material polish, tangent cleanup, VFX/audio, and traversal signoff remain pending.
- Working selected direction: First-pass ancient megalith / deep-vault threshold with hand-hewn stone masses, dark-iron reinforcement, and restrained blue Aetherium channel stones. Treat this as a validated scale-and-composition pass, not the final locked portal style.

This asset replaces the portal-arch blockout in `L_Aerathea_Startup` and becomes the static structure used by `BP_AET_Portal_A01`. The base portal is universal rather than race-specific; race or faction portal variants should inherit this gameplay scale and use visual skins or alternate meshes on top of the shared portal logic.

## Concept Reference

- Concept sheet: `docs/assets/props/SM_AET_PortalArch_A01/concepts/SM_AET_PortalArch_A01_concept_sheet_A01.png`
- Exploration directions: `docs/assets/props/SM_AET_PortalArch_A01/PORTAL_EXPLORATION_DIRECTIONS.md`
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

It should feel old, mysterious, awe-inspiring, and world-scale. Normal players should feel small beside it. It should be large enough to support epic dungeon, raid, city, Giant, major NPC, and large enemy traversal without relying on excessive particles or over-dense micro-detail.

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

Final universal portal target:

- Minimum clear traversal height: 1000 cm / 10 m / about 33 ft.
- Recommended total height: 1200-1400 cm.
- Recommended total width: 1200-1400 cm.
- Recommended depth: 280-360 cm.
- Recommended portal aperture: about 650-800 cm wide x 1000 cm tall.
- Pivot: bottom center between both columns.
- Unreal scale: 1 Unreal unit = 1 cm.
- The portal should comfortably accommodate beings up to 33 ft tall, including Giants, major NPCs, large enemies, and raid/dungeon-scale characters.
- Normal player characters should feel small when standing in front of it.

Current imported startup mesh note:

- The current first-pass 10 m rebuild is approximately 1360 cm wide x 1270 cm tall x 340 cm deep.
- Clear aperture is approximately 788 cm wide by 1000 cm high, with the portal core centered at Z 500 cm.
- The import is valid for startup-scale review and production planning.
- Treat the mesh as first-pass generated geometry; final sculpt/retopo/UVs/textures, tangent cleanup, and Flamestrike visual approval remain required before final art signoff.

## Materials And Color Palette

Material slot target: 2-3 material slots.

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

Create an original stylized fantasy MMORPG concept image of a universal stone portal archway for the world of Aerathea. The design should emphasize an epic 10 m / 33 ft clear traversal opening, an old and mysterious monumental arch silhouette, large ancient stone masses, restrained blue Aetherium channel stones, dark-iron or ancient-metal reinforcement, age-worn craftsmanship, awe-inspiring world-scale magic, and a traversal role for players, Giants, large NPCs, enemies, dungeons, raids, and cities. Normal player characters should feel small beside it. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, back, a 180 cm humanoid scale reference, a 470 cm Giant reference, a 1000 cm clearance marker, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive particles or micro-detail that would not translate to a mid-poly Unreal asset.

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

Large monument prop target range: 8k to 16k tris for the final 10 m portal.

Recommended:

- LOD0: 10k to 14k tris.
- LOD1: 5k to 7k tris.
- LOD2: 2k to 3k tris.
- LOD3: 700 to 1200 tris.

Material slots:

- Target: 2 for final atlas efficiency.
- Current 10 m review import: 3, split across stone, dark iron, and Aetherium.
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
- Left and right base boxes.

Keep the portal opening walkable unless gameplay requires blocking.

Recommended collision names:

- `UCX_SM_AET_PortalArch_A01_00`: left column.
- `UCX_SM_AET_PortalArch_A01_01`: right column.
- `UCX_SM_AET_PortalArch_A01_02`: capstone.
- `UCX_SM_AET_PortalArch_A01_03`: left base stone.
- `UCX_SM_AET_PortalArch_A01_04`: right base stone.

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
- Current build script: `Tools/DCC/build_portal_arch.py`.
- Current import script: `Tools/Unreal/import_portal_10m.py`.
- Focused validator: `Tools/Unreal/validate_portal_10m_scale.py`.
- Startup validator: `Tools/Unreal/validate_startup_scene.py`.
- Place in `L_Aerathea_Startup` through `BP_AET_Portal_A01` / `AET_PROD_Portal_A01`.
- Current startup placement is validated for scale/composition; final visual approval still needs a focused live review capture before final signoff.

## Folder And Naming Recommendation

Unreal content:

- `/Game/Aerathea/Props/Portal/SM_AET_PortalArch_A01`
- `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Stone`
- `/Game/Aerathea/Materials/Props/Portal/MI_AET_PortalArch_A01_Accent`
- `/Game/Aerathea/Textures/Props/Portal/PortalArch_A01/`

External source, if used later:

- `SourceAssets/Blender/Props/Portal/SM_AET_PortalArch_A01/SM_AET_PortalArch_A01.blend`
- `SourceAssets/Exports/Props/Portal/SM_AET_PortalArch_A01/SM_AET_PortalArch_A01.fbx`

## Quality Gate Checklist

- Original Aerathea design.
- Portal opening reads clearly at 30 m.
- Clear portal opening supports beings up to 1000 cm / 10 m / about 33 ft tall.
- Normal players feel small beside the portal.
- Final direction feels old, mysterious, awe-inspiring, and suitable for epic-scale dungeons, raids, and cities.
- Stone blocks are chunky and readable.
- No excessive small brickwork.
- Aetherium glow is restrained.
- LOD0 target fits the approved large monument budget.
- LOD0-LOD3 planned.
- Collision uses simple primitives.
- Material slots no more than 3.
- Pivot is bottom center.
- Imports at correct scale.
- `Tools/Unreal/validate_portal_10m_scale.py` passes.
- `Tools/Unreal/validate_startup_scene.py` passes.
- Works as the static arch for `BP_AET_Portal_A01`.
- GUI map check remains `0 Error(s), 0 Warning(s)`.
