# KIT_ORC_Shields_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_ORC_Shields_A01`
- Asset type: Shield mini-kit
- Source: `Orc Arsenal.png#Shields`
- Parent kit: `KIT_ORC_Arsenal_A01`
- Status: Production package ready; DCC build not started

Original Orc shield set with disciplined clan construction, hide, iron, bronze, bone, and spirit-stone motifs.

## Gameplay Purpose

Reusable shield variants for Orc warriors, wardens, NPCs, clan displays, and future defensive socket tests.

## Silhouette Notes

Use broad round, kite, and hide-shield variants with strong rims and readable clan emblems. Avoid crude trash-shield reads.

## Scale Notes

60-95 cm tall depending on variant. Fit powerful Orc forearms and upright posture.

## Materials And Color Palette

Dark iron, bronze, hide, bone, leather, muted clan paint, blue-green rune or spirit-stone accents.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_ORC_Shields_A01` for the world of Aerathea. The design should emphasize broad disciplined shield silhouettes, iron and bronze rims, hide and leather surfaces, bone clan tokens, muted clan paint, blue-green spirit rune accents, noble upright Orc identity, protective warrior culture, and defensive gameplay roles. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a shield mini-catalog with three variants, front/back views, scale callouts, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model shield plates, rims, bosses, straps, and major clan tokens. Fake tiny stitch lines, paint chips, and scratches in textures.

## Texture And Material Notes

- `T_ORC_Shields_A01_BC`
- `T_ORC_Shields_A01_N`
- `T_ORC_Shields_A01_ORM`
- `T_ORC_Shields_A01_E` for spirit rune accents only

## Triangle Budget

LOD0 2.5k-6k tris per shield, 1-2 material slots.

## LOD Plan

LOD0 full variant detail; LOD1 removes minor trim; LOD2 simplifies straps/tokens; LOD3 preserves shield outline and boss.

## Collision Notes

Equipped collision disabled. World display uses simple convex/box collision.

## Animation Notes

Static mesh variants. Block/parry animations belong to character systems.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Shields/Orc/KIT_ORC_Shields_A01`
- Pivot: back grip center per shield.
- Scale: centimeters.
- Sockets: optional spirit-stone glow sockets.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_ORC_Shields_A01/`
- Source: `SourceAssets/Blender/Kits/Orc/Arsenal/KIT_ORC_Shields_A01/`
- Export: `SourceAssets/Exports/Kits/Orc/Arsenal/KIT_ORC_Shields_A01/`
- Unreal: `/Game/Aerathea/Shields/Orc/`

## Quality Gate Checklist

- Shields reflect honorable Orc clan culture.
- Variants have distinct readable silhouettes.
- Material slots remain controlled.
- Collision and pivots are equipment-safe.
- LODs preserve shield outlines.
