# SM_DWR_StonewallShield_A01 Production Package

## Art Direction Summary

- Asset name: `SM_DWR_StonewallShield_A01`
- Asset type: Static Mesh shield
- Source: `Dwarven Armory.png#Shield_Stonewall`
- Parent kit: `KIT_DWR_Armory_A01`
- Status: Production package ready; DCC build not started

Original Dwarven tower shield built from dark steel, stone-faced plates, brass reinforcement, and restrained blue rune channels.

## Gameplay Purpose

Tank shield for Dwarven guardians, armory display, blocking silhouette tests, and future shield socket validation.

## Silhouette Notes

Tall compact tower shield with squared shoulders, broad base, central rune boss, and heavy reinforced rim. Preserve the wall-like mass.

## Scale Notes

95-125 cm tall, 45-65 cm wide. Author to Dwarven body scale.

## Materials And Color Palette

Slate stone face, dark steel rim, brass rivet plates, dark leather straps, blue rune glow in narrow channels.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_DWR_StonewallShield_A01` for the world of Aerathea. The design should emphasize a stout tower-shield silhouette, stone-faced plates, dark steel rim, aged brass reinforcement, dark leather arm straps, blue runic Aetherium channels, Dwarven fortress culture, and guardian tank gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, back, side, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model shield slab, rim, boss, major straps, and raised rune channels. Fake tiny rivets, chips, stone grain, and scratch fields through texture maps.

## Texture And Material Notes

- `T_DWR_StonewallShield_A01_BC`
- `T_DWR_StonewallShield_A01_N`
- `T_DWR_StonewallShield_A01_ORM`
- `T_DWR_StonewallShield_A01_E` for rune channels only

## Triangle Budget

LOD0 3k-6k tris, 1-2 material slots.

## LOD Plan

LOD0 full slab and strap detail; LOD1 removes minor bevels; LOD2 simplifies straps and rune channels; LOD3 preserves shield outline and center boss.

## Collision Notes

Equipped collision disabled by default. World placement uses simplified convex or box collision.

## Animation Notes

Static mesh. Blocking, bash, and idle movement belongs to character animation.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Shields/Dwarven/SM_DWR_StonewallShield_A01`
- Pivot: inside grip/forearm strap center.
- Scale: centimeters.
- Sockets: optional `socket_rune_glow`.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_DWR_StonewallShield_A01/`
- Source: `SourceAssets/Blender/Kits/Dwarven/Armory/SM_DWR_StonewallShield_A01/`
- Export: `SourceAssets/Exports/Kits/Dwarven/Armory/SM_DWR_StonewallShield_A01/`
- Unreal: `/Game/Aerathea/Shields/Dwarven/SM_DWR_StonewallShield_A01`

## Quality Gate Checklist

- Original Dwarven fortress identity is clear.
- Shield reads as a heavy wall, not a thin plate.
- Rune glow is sparing.
- Collision and pivot are equipment-safe.
- LODs preserve the primary shield outline.
