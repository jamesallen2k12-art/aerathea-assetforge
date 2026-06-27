# SM_ELV_Moonblade_A01 Production Package

## Art Direction Summary

- Asset name: `SM_ELV_Moonblade_A01`
- Asset type: Static Mesh sword
- Source: `Elven Armory.png#Sword_Moonblade`
- Parent kit: `KIT_ELV_Armory_A01`
- Status: Production package ready; DCC build not started

Original Elven moon-warden blade with a graceful crescent edge, silver metal, moonstone detail, living whitewood grip, and blue-white Aetherium accent.

## Gameplay Purpose

Elegant one-handed sword for Elven wardens, rangers, NPCs, armory display, and future weapon socket validation.

## Silhouette Notes

Long tapering blade, subtle crescent guard, slim grip, and moonstone pommel. Keep the blade readable and avoid fragile over-thin shapes.

## Scale Notes

90-105 cm long. Fit tall Elven proportions in centimeters.

## Materials And Color Palette

Polished silver, moonstone, silverleaf etching, living pale wood, blue-white Aetherium glow.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_ELV_Moonblade_A01` for the world of Aerathea. The design should emphasize an elegant crescent sword silhouette, polished silver, moonstone, living whitewood grip, silverleaf etching, blue-white Aetherium accent, ancient Elven moon-and-star culture, serene warden mood, and agile one-handed sword gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, three-quarter view, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model blade, guard, grip, pommel, and large moonstone setting. Fake fine leaf etching, hairline scratches, and tiny runes with texture/normal maps.

## Texture And Material Notes

- `T_ELV_Moonblade_A01_BC`
- `T_ELV_Moonblade_A01_N`
- `T_ELV_Moonblade_A01_ORM`
- `T_ELV_Moonblade_A01_E` for moonstone/Aetherium accents only

## Triangle Budget

LOD0 2.5k-4k tris, 1 material slot.

## LOD Plan

LOD0 full curve and bevels; LOD1 removes small trim; LOD2 simplifies guard/pommel; LOD3 preserves blade and crescent guard silhouette.

## Collision Notes

Equipped collision disabled. Pickup/display uses simple capsule or box.

## Animation Notes

Static mesh. Combat animations belong to character systems.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/Elven/SM_ELV_Moonblade_A01`
- Pivot: grip center.
- Scale: 1 Unreal unit = 1 cm.
- Sockets: optional `socket_moonstone_glow`.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_ELV_Moonblade_A01/`
- Source: `SourceAssets/Blender/Kits/Elven/Armory/SM_ELV_Moonblade_A01/`
- Export: `SourceAssets/Exports/Kits/Elven/Armory/SM_ELV_Moonblade_A01/`
- Unreal: `/Game/Aerathea/Weapons/Elven/SM_ELV_Moonblade_A01`

## Quality Gate Checklist

- Elven elegance and moon identity are clear.
- Blade reads from MMO camera distance.
- Glow is sparing.
- Fine etching is texture detail.
- LOD, collision, textures, and Unreal path are defined.
