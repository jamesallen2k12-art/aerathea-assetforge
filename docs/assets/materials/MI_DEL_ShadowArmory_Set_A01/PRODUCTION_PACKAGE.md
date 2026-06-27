# MI_DEL_ShadowArmory_Set_A01 Production Package

## Art Direction Summary

- Asset name: `MI_DEL_ShadowArmory_Set_A01`
- Asset type: Material instance set
- Source: `Dark Elven Armory.png#Material_ShadowArmory`
- Parent kit: `KIT_DEL_Armory_A01`
- Status: Production package ready; Unreal material authoring not started

Reusable Dark Elven material set for obsidian, dark silver, black leather, veiled cloth, and violet lunar emissive accents.

## Gameplay Purpose

Shared material language for Dark Elven weapons, shields, armor, props, and moonlit hall dressing.

## Silhouette Notes

Material should reinforce form edges with cold highlights and violet focus points, not hide silhouettes in black.

## Scale Notes

Texture detail must read on small weapons and larger shield/armor surfaces.

## Materials And Color Palette

Obsidian black, dark silver, black leather, deep violet glow, blue-gray moonlit edge highlights.

## Concept Image Prompt

Create an original stylized fantasy MMORPG material concept sheet of `MI_DEL_ShadowArmory_Set_A01` for the world of Aerathea. The design should emphasize refined Dark Elven obsidian, dark silver, black leather, veiled cloth, violet lunar glow, crescent motif masks, oath-bound ancient culture, and shadowblade/sentinel/spellbow gameplay roles. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a material board with weapon, shield, cloth, leather, and glow swatches on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Material set only. Assets using it need major crescent plates, carved channels, and clear silhouette geometry.

## Texture And Material Notes

- `MI_DEL_Obsidian_A01`
- `MI_DEL_DarkSilver_A01`
- `MI_DEL_BlackLeather_A01`
- `MI_DEL_VeiledCloth_A01`
- `MI_DEL_VioletLunarGlow_A01`

## Triangle Budget

Not applicable. Material complexity must remain MMO-safe.

## LOD Plan

At distance, reduce emissive pulse and rely on base color/roughness contrast.

## Collision Notes

Not applicable.

## Animation Notes

Optional slow pulse scalar for hero or spell-active states only.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Materials/DarkElven/MI_DEL_ShadowArmory_Set_A01`
- Parent materials: shared Aerathea hand-painted opaque and emissive parents.
- Parameters: tint, roughness, metallic, emissive color, emissive strength.

## Folder And Naming Recommendation

- Docs: `docs/assets/materials/MI_DEL_ShadowArmory_Set_A01/`
- Textures: `/Game/Aerathea/Textures/DarkElven/Armory/`
- Unreal: `/Game/Aerathea/Materials/DarkElven/`

## Quality Gate Checklist

- Dark forms stay readable.
- Violet glow is sparing.
- Material set can serve weapons, armor, and props.
- Runtime cost is controlled.
- Naming and parameter strategy are defined.
