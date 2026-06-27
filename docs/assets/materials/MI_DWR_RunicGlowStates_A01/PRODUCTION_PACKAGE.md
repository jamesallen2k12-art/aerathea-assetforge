# MI_DWR_RunicGlowStates_A01 Production Package

## Art Direction Summary

- Asset name: `MI_DWR_RunicGlowStates_A01`
- Asset type: Material instance set
- Source: `Dwarven Armory.png#RunicGlowStates`
- Parent kit: `KIT_DWR_Armory_A01`
- Status: Production package ready; Unreal material authoring not started

Dwarven blue runic glow states for weapons, shields, armor plates, forge props, and guardian effects.

## Gameplay Purpose

Reusable material states for inactive, active, charged, and overcharged Dwarven runes.

## Silhouette Notes

Glow should sit inside carved rune channels or stone/metal seams. It must not flood the whole asset.

## Scale Notes

Rune channels need readable line width at third-person camera distance and item preview distance.

## Materials And Color Palette

Deep blue inactive rune, blue-white active core, cyan edge pulse for charged, and low-opacity overcharge bloom for hero moments only.

## Concept Image Prompt

Create an original stylized fantasy MMORPG material concept sheet of `MI_DWR_RunicGlowStates_A01` for the world of Aerathea. The design should emphasize Dwarven carved rune channels, slate stone and dark steel surfaces, blue Aetherium glow states, mountain-forged restraint, guardian and runesmith gameplay roles, and clear inactive, active, charged, and overcharged state swatches. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a material board with rune strips, shield/hammer samples, value ranges, and emissive notes on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Material only. Meshes using it need real recessed rune channels for major glow shapes.

## Texture And Material Notes

- `MI_DWR_RunicGlow_Inactive_A01`
- `MI_DWR_RunicGlow_Active_A01`
- `MI_DWR_RunicGlow_Charged_A01`
- `MI_DWR_RunicGlow_Overcharged_A01`
- Shared mask texture: `T_DWR_RunicGlow_A01_E`

## Triangle Budget

No triangle budget. Material should support low-cost static and skeletal assets.

## LOD Plan

At distance, reduce emissive intensity and rely on base color/rune mask readability.

## Collision Notes

Not applicable.

## Animation Notes

Optional scalar pulse parameter for charged states; avoid expensive per-pixel animation on common assets.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Materials/Dwarven/MI_DWR_RunicGlowStates_A01`
- Parent material: shared Aerathea emissive material or material function.
- Parameters: emissive color, emissive strength, pulse speed, pulse amount.

## Folder And Naming Recommendation

- Docs: `docs/assets/materials/MI_DWR_RunicGlowStates_A01/`
- Textures: `/Game/Aerathea/Textures/Dwarven/Runes/`
- Unreal: `/Game/Aerathea/Materials/Dwarven/`

## Quality Gate Checklist

- Blue rune language matches Dwarven anchor.
- States are readable and restrained.
- Overcharge is reserved for special effects.
- Material parameters are reusable.
- Emissive maps and performance notes are defined.
