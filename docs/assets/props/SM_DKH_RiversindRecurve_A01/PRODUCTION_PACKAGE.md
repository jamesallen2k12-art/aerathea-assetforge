# SM_DKH_RiversindRecurve_A01 Production Package

## Art Direction Summary

- Asset name: `SM_DKH_RiversindRecurve_A01`
- Asset type: Static Mesh bow
- Source: `Drakhar Arms Relics and Field Gear.png#Bow_RiversindRecurve`
- Parent kit: `KIT_DKH_FieldGear_A01`
- Status: Production package ready; DCC build not started

Original Drakhar recurve bow scaled for A04 lizardfolk: females 3'6"-4'2", males 4'0"-4'6", built from sun-baked wood, bone, leather, reed bindings, and ember-lit relic charms.

## Gameplay Purpose

Ranger/rogue field bow for Drakhar scouts, relic seekers, NPCs, armory display, and projectile socket validation.

## Silhouette Notes

Compact crescent recurve, hooked limb tips, wrapped grip, and small hanging relic charm. Avoid oversized human-scale bow proportions.

## Scale Notes

90-125 cm tall, corrected to approved A04 Drakhar scale.

## Materials And Color Palette

Sun-baked wood, bone, leather, reed cord, ember stone, muted desert cloth, sparing orange-blue arcane glow.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_DKH_RiversindRecurve_A01` for the world of Aerathea. The design should emphasize a compact crescent recurve bow silhouette, sun-baked wood, bone limb tips, leather and reed bindings, ember relic charm, corrected A04 Drakhar scale, bearded-dragon desert-lizard identity, magic-seeking culture tied to Volcreon, and ranger/rogue gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, strung/unstrung callouts, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model limbs, grip, nocks, bone tips, major wraps, and one readable charm. Fake reed fiber, scale marks, scratches, and tiny relic glyphs in maps.

## Texture And Material Notes

- `T_DKH_RiversindRecurve_A01_BC`
- `T_DKH_RiversindRecurve_A01_N`
- `T_DKH_RiversindRecurve_A01_ORM`
- `T_DKH_RiversindRecurve_A01_E` for ember charm only

## Triangle Budget

LOD0 2k-5k tris, 1 material slot.

## LOD Plan

LOD0 full bow; LOD1 removes tiny wraps; LOD2 simplifies charm and nocks; LOD3 preserves bow arc and grip.

## Collision Notes

Equipped collision disabled. Display uses simple long box/capsule.

## Animation Notes

Static mesh baseline. Bow draw/string animation waits for weapon systems.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/Drakhar/SM_DKH_RiversindRecurve_A01`
- Pivot: hand grip center.
- Scale: centimeters.
- Sockets: `socket_arrow_rest`, `socket_string_top`, `socket_string_bottom`, optional `socket_relic_charm`.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_DKH_RiversindRecurve_A01/`
- Source: `SourceAssets/Blender/Kits/Drakhar/FieldGear/SM_DKH_RiversindRecurve_A01/`
- Export: `SourceAssets/Exports/Kits/Drakhar/FieldGear/SM_DKH_RiversindRecurve_A01/`
- Unreal: `/Game/Aerathea/Weapons/Drakhar/SM_DKH_RiversindRecurve_A01`

## Quality Gate Checklist

- Corrected A04 Drakhar scale is used.
- Bow silhouette is compact and readable.
- Relic glow is sparing.
- Major forms are geometry; tiny glyphs are texture.
- Socket and LOD plans are defined.
