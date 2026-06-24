# SM_MKG_AetherCoreUnit_A01 Production Package

## Art Direction Summary

- Asset name: `SM_MKG_AetherCoreUnit_A01`
- Asset type: Static Mesh power module / equipment prop
- Source: `Gnome Armory.png#Gear_AetherCoreUnit`
- Faction: Gnome / Mekgineer
- Status: Production package ready

Boxy backpack-scale power unit with brass/dark-iron housing, compact side cylinders, leather carry straps, and a protected blue Aetherium crystal core. The silhouette should read as portable gnome engineering, not a magical gem on a box.

## Gameplay Purpose

Supports Mekgineer gear identity, workshop dressing, backpack attachment planning, powered-device VFX tests, and future crafting/quest props.

## Silhouette Notes

Use a squat rectangular housing with rounded cylinders, handle loops, and a central crystal window. The Aetherium core should be obvious from MMO camera distance but protected by metal framing.

## Scale Notes

- Target height: 45-60 cm.
- Gnome back attachment candidate; do not lock final skeletal fit until base gnome body is approved.
- Pivot: lower rear center for backpack socketing and shelf placement.

## Materials And Color Palette

Worn brass and copper plates, dark iron frame, leather straps, glass/crystal blue Aetherium core. Use dark grime in seams and warm edge highlights.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a gnome Mekgineer Aether core unit for the world of Aerathea. The design should emphasize a squat portable power-module silhouette, brass and dark iron casing, leather carry straps, a protected blue Aetherium crystal chamber, compact engineering culture, and practical field-use mood. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a front/back/side equipment concept sheet on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model the housing, metal frame, handle loops, large tubes, core glass frame, strap blocks, and rear mounting lugs as real geometry. Texture small screws, tiny vents, gauge ticks, leather stitching, and panel scratches.

## Texture And Material Notes

- `T_MKG_AetherCoreUnit_A01_BC`
- `T_MKG_AetherCoreUnit_A01_N`
- `T_MKG_AetherCoreUnit_A01_ORM`
- `T_MKG_AetherCoreUnit_A01_E`

Use 1-2 material slots: shared Mekgineer metal/leather plus Aetherium glass/emissive if needed.

## Triangle Budget

LOD0 target: 3k-6k tris. Upper range is acceptable if used as an inspected hero gear prop.

## LOD Plan

- LOD0: full casing, tubes, core frame, straps.
- LOD1: reduce tube bevels and handle loops.
- LOD2: merge strap and vent details into normal maps.
- LOD3: boxed silhouette with core plane/inset.

## Collision Notes

Attachment collision disabled by default. World prop uses simple box collision plus optional small interaction bounds.

## Animation Notes

Static mesh baseline. Future Blueprint/material states may pulse the core, but no moving parts in this first package.

## Unreal Import Notes

- Folder: `/Game/Aerathea/Props/Mekgineer/Armory/`
- Mesh: `SM_MKG_AetherCoreUnit_A01`
- Material instance: `MI_MKG_AetherCoreUnit_A01`
- Pivot: lower rear center
- Socket notes: future `back_pack` and display shelf sockets
- Collision: simple box when world-placed

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_MKG_AetherCoreUnit_A01/`
- Source: `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01/`
- Export: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetherCoreUnit_A01/`

## Quality Gate Checklist

- Original Aerathea gnome/Mekgineer identity.
- Readable portable power-module silhouette.
- Core glow is clear but restrained.
- Backpack/display pivot needs are documented.
- Material slots, textures, LODs, collision, and Unreal paths are defined.
