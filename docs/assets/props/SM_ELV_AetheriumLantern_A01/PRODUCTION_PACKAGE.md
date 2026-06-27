# SM_ELV_AetheriumLantern_A01 Production Package

## Art Direction Summary

- Asset name: `SM_ELV_AetheriumLantern_A01`
- Asset type: Static Mesh prop
- Source: `Elven Armory.png#Lantern_Aetherium`
- Parent kit: `KIT_ELV_Armory_A01`
- Status: Production package ready; DCC build not started

Original Elven lantern with moonstone housing, silverleaf cage, living whitewood handle, and soft blue-white Aetherium glow.

## Gameplay Purpose

Exploration prop, settlement dressing, handheld item, and lighting/material test for Elven spaces.

## Silhouette Notes

Small elegant lantern frame, crescent handle, central crystal chamber, and open readable cage. Avoid dense micro filigree.

## Scale Notes

35-50 cm tall. Grip must support hand carry and hanging socket variants.

## Materials And Color Palette

Polished silver, moonstone, living whitewood, pale leather, glass/crystal Aetherium core, blue-white emissive accent.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_ELV_AetheriumLantern_A01` for the world of Aerathea. The design should emphasize an elegant crescent lantern silhouette, polished silverleaf cage, moonstone housing, living whitewood handle, clear Aetherium crystal core, soft blue-white glow, Elven moonlit culture, and exploration or settlement-lighting gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, hanging/carrying callouts, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model frame, handle, cage ribs, crystal chamber, and base. Fake small engravings and surface scratches in texture maps.

## Texture And Material Notes

- `T_ELV_AetheriumLantern_A01_BC`
- `T_ELV_AetheriumLantern_A01_N`
- `T_ELV_AetheriumLantern_A01_ORM`
- `T_ELV_AetheriumLantern_A01_E` for the crystal core

## Triangle Budget

LOD0 3k-5k tris, 1-2 material slots.

## LOD Plan

LOD0 full cage; LOD1 removes minor trim; LOD2 reduces cage ribs; LOD3 preserves lantern outline and glow core.

## Collision Notes

Simple box/capsule pickup bounds. No blocking collision when equipped.

## Animation Notes

Static mesh baseline. Optional hanging sway or carried idle belongs to Blueprint/animation later.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Props/Elven/SM_ELV_AetheriumLantern_A01`
- Pivot: bottom center for world placement or handle center for handheld variant.
- Scale: centimeters.
- Sockets: `socket_light_core`, optional `socket_hang`.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_ELV_AetheriumLantern_A01/`
- Source: `SourceAssets/Blender/Kits/Elven/Armory/SM_ELV_AetheriumLantern_A01/`
- Export: `SourceAssets/Exports/Kits/Elven/Armory/SM_ELV_AetheriumLantern_A01/`
- Unreal: `/Game/Aerathea/Props/Elven/SM_ELV_AetheriumLantern_A01`

## Quality Gate Checklist

- Elven lantern silhouette and culture read clearly.
- Glow is soft and localized.
- Cage remains MMO-safe mid-poly geometry.
- Carry/hanging pivots are specified.
- LOD and collision plans are defined.
