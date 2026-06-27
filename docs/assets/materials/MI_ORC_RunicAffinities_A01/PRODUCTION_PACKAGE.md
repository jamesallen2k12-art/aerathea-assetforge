# MI_ORC_RunicAffinities_A01 Production Package

## Art Direction Summary

- Asset name: `MI_ORC_RunicAffinities_A01`
- Asset type: Material instance set
- Source: `Orc Arsenal.png#RunicAffinities`
- Parent kit: `KIT_ORC_Arsenal_A01`
- Status: Production package ready; Unreal material authoring not started

Reusable Orc rune and spirit-stone material states for clan weapons, shields, talismans, and shamanic props.

## Gameplay Purpose

Material language for warrior, warden, ranger, and shamanic affinity variants.

## Silhouette Notes

Glow should mark carved channels, stones, or clan emblems. Do not flood entire blades or shields.

## Scale Notes

Rune marks must read on weapon heads, shield bosses, and small talisman stones.

## Materials And Color Palette

Blue-green spirit glow, muted teal, deep green, aged bronze, dark iron, bone, and clan-color masks.

## Concept Image Prompt

Create an original stylized fantasy MMORPG material concept sheet of `MI_ORC_RunicAffinities_A01` for the world of Aerathea. The design should emphasize Orc clan rune masks, blue-green spirit-stone glow, dark iron, aged bronze, bone, leather, muted clan colors, honorable shamanic culture, and readable affinity states for warriors, wardens, rangers, and shamans. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a material board with weapon, shield, talisman, and rune swatches on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Material set only. Assets should provide carved channels, sockets, or stones for readable glow placement.

## Texture And Material Notes

- `MI_ORC_Rune_Warrior_A01`
- `MI_ORC_Rune_Warden_A01`
- `MI_ORC_Rune_Ranger_A01`
- `MI_ORC_Rune_Shaman_A01`
- Shared mask: `T_ORC_RunicAffinities_A01_E`

## Triangle Budget

Not applicable. Keep material instructions suitable for common low-cost props.

## LOD Plan

At distance, simplify emissive pulse and rely on base color/mask contrast.

## Collision Notes

Not applicable.

## Animation Notes

Optional scalar pulse for shamanic active state only.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Materials/Orc/MI_ORC_RunicAffinities_A01`
- Parent materials: shared Aerathea opaque and emissive parents.
- Parameters: rune color, emissive strength, pulse speed, clan tint.

## Folder And Naming Recommendation

- Docs: `docs/assets/materials/MI_ORC_RunicAffinities_A01/`
- Textures: `/Game/Aerathea/Textures/Orc/Runes/`
- Unreal: `/Game/Aerathea/Materials/Orc/`

## Quality Gate Checklist

- Orc runes feel spiritual and disciplined.
- Glow remains localized.
- Variants are reusable across weapons, shields, and talismans.
- Runtime cost is controlled.
- Naming and parameter strategy are defined.
