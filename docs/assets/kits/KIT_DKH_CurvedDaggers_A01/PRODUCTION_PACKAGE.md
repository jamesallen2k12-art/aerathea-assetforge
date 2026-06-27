# KIT_DKH_CurvedDaggers_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_DKH_CurvedDaggers_A01`
- Asset type: Weapon mini-kit
- Source: `Drakhar Arms Relics and Field Gear.png#Daggers_Curved`
- Parent kit: `KIT_DKH_FieldGear_A01`
- Status: Production package ready; DCC build not started

Original Drakhar curved dagger set with fang-like profiles, bone or dark metal blades, leather wraps, and small magic-tracking relic accents.

## Gameplay Purpose

Rogue/shaman/wizard sidearms for Drakhar characters, NPCs, loot, and dual-wield socket tests.

## Silhouette Notes

Hooked, crescent, and fang-like dagger variants. Keep each profile distinct and readable in inventory and third-person view.

## Scale Notes

25-45 cm long. Fit small clawed Drakhar hands.

## Materials And Color Palette

Bone, dark iron, leather, sun-baked cord, ember stones, small arcane glyph accents.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_DKH_CurvedDaggers_A01` for the world of Aerathea. The design should emphasize hooked and fang-like curved dagger silhouettes, bone and dark iron blades, leather and reed cord wraps, ember relic stones, corrected A04 Drakhar scale, desert-lizard identity, magic-seeking Volcreon-linked culture, and rogue/shaman/wizard gameplay roles. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a dagger mini-catalog with three variants, scale callouts, grip callouts, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model blades, grips, guards, pommels, major wraps, and large relic stones. Fake tiny glyphs, scratches, stitching, and bone pores in textures.

## Texture And Material Notes

- `T_DKH_CurvedDaggers_A01_BC`
- `T_DKH_CurvedDaggers_A01_N`
- `T_DKH_CurvedDaggers_A01_ORM`
- `T_DKH_CurvedDaggers_A01_E` for relic stones only

## Triangle Budget

LOD0 800-2k tris per dagger, 1 material slot.

## LOD Plan

LOD0 full variant; LOD1 removes tiny wraps; LOD2 simplifies relic stones and guards; LOD3 preserves blade curve and grip.

## Collision Notes

Equipped collision disabled. Pickup/display uses simple box/capsule bounds.

## Animation Notes

Static mesh variants. Dual-wield, throw, and spell-channel animations belong to character/combat systems.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/Drakhar/KIT_DKH_CurvedDaggers_A01`
- Pivot: grip center per dagger.
- Scale: centimeters.
- Sockets: optional `socket_relic_glow`.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_DKH_CurvedDaggers_A01/`
- Source: `SourceAssets/Blender/Kits/Drakhar/FieldGear/KIT_DKH_CurvedDaggers_A01/`
- Export: `SourceAssets/Exports/Kits/Drakhar/FieldGear/KIT_DKH_CurvedDaggers_A01/`
- Unreal: `/Game/Aerathea/Weapons/Drakhar/`

## Quality Gate Checklist

- Dagger variants are distinct and readable.
- Correct Drakhar scale and clawed-hand ergonomics are used.
- Glow is limited to relic stones.
- Triangle budgets stay small.
- Pivot/socket strategy is defined.
