# SM_ELV_MoonwardBuckler_A01 Production Package

## Art Direction Summary

- Asset name: `SM_ELV_MoonwardBuckler_A01`
- Asset type: Static Mesh shield
- Source: `Elven Armory.png#Shield_MoonwardBuckler`
- Parent kit: `KIT_ELV_Armory_A01`
- Status: Production package ready; DCC build not started

Original Elven buckler with crescent rim, silverleaf surface, moonstone boss, and pale wood or leather back straps.

## Gameplay Purpose

Light shield for Elven wardens and spellblades, armory display, and future blocking socket validation.

## Silhouette Notes

Round or crescent-round outline, moonstone center, slim rim, and clean negative space. Avoid bulky tower-shield mass.

## Scale Notes

35-45 cm diameter, fitted to graceful Elven proportions.

## Materials And Color Palette

Polished silver, silverleaf, moonstone, pale leather, living whitewood, blue-white glow only at the boss or inlay.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_ELV_MoonwardBuckler_A01` for the world of Aerathea. The design should emphasize a light crescent buckler silhouette, polished silver, silverleaf inlay, moonstone central boss, pale leather straps, living whitewood back support, blue-white Aetherium accents, Elven moon-warden identity, and agile defensive gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, back, side, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model shield disk, rim, boss, strap anchors, and major inlay bands. Fake tiny leaf engravings and metal wear in texture maps.

## Texture And Material Notes

- `T_ELV_MoonwardBuckler_A01_BC`
- `T_ELV_MoonwardBuckler_A01_N`
- `T_ELV_MoonwardBuckler_A01_ORM`
- `T_ELV_MoonwardBuckler_A01_E` for moonstone only

## Triangle Budget

LOD0 2k-3.5k tris, 1 material slot.

## LOD Plan

LOD0 full disk and trim; LOD1 removes minor engraving geometry; LOD2 simplifies rim and strap anchors; LOD3 preserves round silhouette and boss.

## Collision Notes

Equipped collision disabled. Pickup/display uses simple convex or box bounds.

## Animation Notes

Static mesh. Blocking and parry motion belongs to character animation.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Shields/Elven/SM_ELV_MoonwardBuckler_A01`
- Pivot: back grip center.
- Scale: centimeters.
- Sockets: optional `socket_moonstone_glow`.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_ELV_MoonwardBuckler_A01/`
- Source: `SourceAssets/Blender/Kits/Elven/Armory/SM_ELV_MoonwardBuckler_A01/`
- Export: `SourceAssets/Exports/Kits/Elven/Armory/SM_ELV_MoonwardBuckler_A01/`
- Unreal: `/Game/Aerathea/Shields/Elven/SM_ELV_MoonwardBuckler_A01`

## Quality Gate Checklist

- Light Elven shield read is clear.
- Moonstone glow is sparing.
- Back straps are equipment-friendly.
- LODs preserve the buckler outline.
- Collision and pivot are defined.
