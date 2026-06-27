# SM_ELV_SilverleafRecurve_A01 Production Package

## Art Direction Summary

- Asset name: `SM_ELV_SilverleafRecurve_A01`
- Asset type: Static Mesh bow
- Source: `Elven Armory.png#Bow_SilverleafRecurve`
- Parent kit: `KIT_ELV_Armory_A01`
- Status: Production package ready; DCC build not started

Original Elven recurve bow with living whitewood limbs, silverleaf inlay, moonstone nocks, and restrained blue-white Aetherium focus.

## Gameplay Purpose

Elven ranger/warden bow for ranged combat identity, armory display, and future string/projectile socket validation.

## Silhouette Notes

Tall smooth recurve, leaf-like negative space, clear nocks, and slim central grip. Avoid excessive vine tangles.

## Scale Notes

145-165 cm tall. Author to tall Elven proportions.

## Materials And Color Palette

Living whitewood, polished silver, silverleaf, moonstone, pale leather grip, blue-white Aetherium accents.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_ELV_SilverleafRecurve_A01` for the world of Aerathea. The design should emphasize a tall graceful recurve bow silhouette, living whitewood limbs, polished silverleaf inlay, moonstone nocks, pale leather grip, blue-white Aetherium focus, ancient Elven ranger culture, serene moonlit mood, and ranged gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, strung/unstrung callout, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model limbs, grip, nocks, major silver wraps, and central moonstone. Fake fine leaf veins and wood grain in textures.

## Texture And Material Notes

- `T_ELV_SilverleafRecurve_A01_BC`
- `T_ELV_SilverleafRecurve_A01_N`
- `T_ELV_SilverleafRecurve_A01_ORM`
- `T_ELV_SilverleafRecurve_A01_E` for moonstone accents only

## Triangle Budget

LOD0 3.5k-6k tris, 1 material slot.

## LOD Plan

LOD0 full recurve and trim; LOD1 simplifies trim; LOD2 reduces nock/leaf detail; LOD3 preserves bow arc and grip mass.

## Collision Notes

Equipped collision disabled. Display collision uses simple long box/capsule.

## Animation Notes

Static mesh baseline. Bowstring draw and projectile logic wait for weapon/animation systems.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/Elven/SM_ELV_SilverleafRecurve_A01`
- Pivot: hand grip center.
- Scale: centimeters.
- Sockets: `socket_arrow_rest`, `socket_string_top`, `socket_string_bottom` when bow draw support is built.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_ELV_SilverleafRecurve_A01/`
- Source: `SourceAssets/Blender/Kits/Elven/Armory/SM_ELV_SilverleafRecurve_A01/`
- Export: `SourceAssets/Exports/Kits/Elven/Armory/SM_ELV_SilverleafRecurve_A01/`
- Unreal: `/Game/Aerathea/Weapons/Elven/SM_ELV_SilverleafRecurve_A01`

## Quality Gate Checklist

- Recurve silhouette is readable.
- Elven living wood and silverleaf language is clear.
- Glow is restrained.
- String/projectile socket plan exists.
- LODs preserve the bow arc.
