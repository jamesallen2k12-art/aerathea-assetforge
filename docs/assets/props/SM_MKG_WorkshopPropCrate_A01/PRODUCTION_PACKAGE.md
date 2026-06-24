# SM_MKG_WorkshopPropCrate_A01 Production Package

## Asset Brief

- Asset name: `SM_MKG_WorkshopPropCrate_A01`
- Asset type: Static Mesh
- World: Aerathea
- Category: Mekgineer workshop prop / storage crate
- Current status: Concept sheet generated, modeling handoff ready
- Cultural anchor: Gnome Mekgineer

This crate is the first small prop for Mekgineer workshop visual language: compact, clever, sturdy, brass/copper/dark-iron accents, leather handles, and restrained blue Aetherium details.

## Concept Reference

- Concept sheet: `docs/assets/props/SM_MKG_WorkshopPropCrate_A01/concepts/SM_MKG_WorkshopPropCrate_A01_concept_sheet_A01.png`
- Modeling handoff: `docs/assets/props/SM_MKG_WorkshopPropCrate_A01/MODELING_HANDOFF.md`
- Generation mode: built-in image generation tool.
- Review status: usable first-pass reference; final Flamestrike approval still required before treating it as a locked final art target.

## Gameplay Purpose

The crate supports early prop dressing and material validation. It should prove:

- Small prop scale.
- Mekgineer material language.
- Low-cost collision.
- Reusable settlement dressing.
- Hand-painted texture readability.

Potential gameplay uses later:

- Loot container.
- Crafting station dressing.
- Quest-object container.
- Workshop clutter set piece.

## Silhouette Notes

- Compact rectangular crate with slightly exaggerated chunky proportions.
- Reinforced corners.
- Thick lid lip.
- One oversized latch or clamp.
- Side handle loops.
- Small blue Aetherium label, seal, or calibration mark.
- Avoid many tiny gears or bolts.
- A few large fasteners may be modeled; smaller ones go into texture.

Primary readable shapes:

1. Box body.
2. Reinforced corner plates.
3. Lid lip.
4. Oversized latch.
5. Side handle.

## Scale Notes

- Width: 90 cm.
- Depth: 65 cm.
- Height: 55 cm.
- Pivot: bottom center.
- Unreal scale: 1 Unreal unit = 1 cm.
- Should be believable beside a 110 cm gnome and still usable as human-scale workshop clutter.

## Materials And Color Palette

Material slot target: 1.

Material language:

- Timber box panels.
- Brass/copper corner plates.
- Dark iron latch and hinge.
- Worn leather handles.
- Small blue Aetherium inspection mark.

Palette:

- Timber: `#5A351D`
- Copper: `#9A5726`
- Brass: `#B08034`
- Dark iron: `#1A2022`
- Leather: `#362018`
- Aetherium blue: `#1E86D9`

Use blue as a small accent, not a dominant color.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a compact Mekgineer workshop crate for the world of Aerathea. The design should emphasize a chunky readable box silhouette, reinforced brass and copper corners, dark-iron latch, worn timber panels, leather side handles, small blue Aetherium inspection mark, gnome engineering culture, practical inventor-workshop mood, and reusable storage prop gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing blue accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, top, open-lid option, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model real geometry for:

- Crate body.
- Lid lip.
- Large corner plates.
- Main latch.
- Hinge blocks.
- Side handles.
- Broad plank seams if needed for silhouette.

Fake with texture/normal map:

- Tiny nails.
- Fine scratches.
- Wood grain.
- Small stamped labels.
- Minor dents.
- Leather stitching.
- Micro gear marks.

Suggested mesh parts:

- `Body_Box`
- `Lid_Lip`
- `Corners_Brass`
- `Latch_DarkIron`
- `Handles_Leather`
- `Feet_Small`

Keep it modular enough that later variants can swap latch, handle, label, or material color.

## Texture And Material Notes

Texture target:

- 1K texture set.
- 512 if used only as distant clutter.

Texture maps:

- `T_MKG_WorkshopPropCrate_A01_BC`
- `T_MKG_WorkshopPropCrate_A01_N`
- `T_MKG_WorkshopPropCrate_A01_ORM`

Optional:

- `T_MKG_WorkshopPropCrate_A01_E` only if the blue inspection mark becomes emissive. Default is non-emissive paint.

Material instance:

- `MI_MKG_WorkshopPropCrate_A01`

## Triangle Budget

Small prop target range: 500 to 4k tris.

Recommended:

- LOD0: 1.5k to 2.4k tris.
- LOD1: 800 to 1.2k tris.
- LOD2: 300 to 500 tris.
- LOD3: 80 to 160 tris.

Material slots:

- Target: 1.
- Maximum: 2 only if future open/closed variants need separate inner material.

## LOD Plan

LOD0:

- Full shape, large corner plates, latch, handles, lid lip.

LOD1:

- Reduce bevels.
- Simplify handles.
- Merge small feet.

LOD2:

- Flatten latch and handles into broad forms.
- Preserve box proportions and corner plate contrast.

LOD3:

- Simple box with lid/latch silhouette only.

Never remove the main crate box, lid lip, or latch silhouette first.

## Collision Notes

Use one simple box collision for default prop behavior.

Optional:

- Add second small box for protruding latch only if player collision feels wrong.

Recommended:

- `UCX_SM_MKG_WorkshopPropCrate_A01_00`

Do not use complex-as-simple collision.

## Animation Notes

Static mesh baseline has no animation.

Future optional blueprint variant:

- `BP_MKG_WorkshopCrate_A01`
- Open/close lid.
- Lootable state.
- Quest highlight.

Do not make the first static mesh depend on blueprint behavior.

## Unreal Import Notes

- Static mesh path: `/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01`
- Pivot: bottom center.
- Scale: centimeters.
- Collision: simple box.
- LODs: LOD0-LOD3.
- Nanite: off for this small prop.
- Place near future Mekgineer workshop test dressing, not necessarily in the initial portal/target dummy center.

## Folder And Naming Recommendation

Unreal content:

- `/Game/Aerathea/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01`
- `/Game/Aerathea/Materials/Props/Mekgineer/MI_MKG_WorkshopPropCrate_A01`
- `/Game/Aerathea/Textures/Props/Mekgineer/WorkshopPropCrate_A01/`

External source, if used later:

- `SourceAssets/Blender/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01.blend`
- `SourceAssets/Exports/Props/Mekgineer/SM_MKG_WorkshopPropCrate_A01.fbx`

## Quality Gate Checklist

- Reads as a compact workshop crate from 15 m.
- Clearly supports Mekgineer identity.
- Does not overuse gears, bolts, or glow.
- LOD0 under 2.5k tris.
- 1 material slot target met.
- Simple box collision.
- Pivot is bottom center.
- Scale works beside gnome marker.
- BC, N, ORM texture set planned.
- No copied franchise design.
- GUI map check remains `0 Error(s), 0 Warning(s)`.
