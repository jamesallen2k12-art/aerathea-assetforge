# SM_MIN_CrushingMaul_A01 Production Package

## Art Direction Summary

- Asset name: `SM_MIN_CrushingMaul_A01`
- Asset type: Static Mesh two-handed maul
- Source: `Minotaur Arsenal.png#Maul_01`
- Parent kit: `KIT_MIN_Arsenal_A01`
- Status: Production package ready; DCC build not started

Original Minotaur crushing maul with raw iron head, simple brutal flanges, heavy wood haft, hide binding, and bone/fur accents.

## Gameplay Purpose

Two-handed blunt weapon for Minotaur berserker and warrior roles, NPC attacks, display, and impact VFX socket planning.

## Silhouette Notes

Oversized blunt head, short heavy spikes/flanges, thick haft, and readable impact face. Avoid delicate engraving.

## Scale Notes

160-220 cm long. Fit approved Minotaur scale: females 7-8 ft, males 8-9 ft.

## Materials And Color Palette

Raw iron, dark wood, hide, bone, fur, leather, simple tribal paint.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_MIN_CrushingMaul_A01` for the world of Aerathea. The design should emphasize an oversized brutal maul silhouette, raw iron head, simple heavy flanges, dark wood haft, hide and leather bindings, bone and fur accents, ruthless Minotaur strength culture, and two-handed crushing melee gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, three-quarter view, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model head, flanges, haft, wraps, and large tokens. Fake dents, scratches, wood grain, and leather wear in texture maps.

## Texture And Material Notes

- `T_MIN_CrushingMaul_A01_BC`
- `T_MIN_CrushingMaul_A01_N`
- `T_MIN_CrushingMaul_A01_ORM`
- No emissive texture by default

## Triangle Budget

LOD0 3k-8k tris, 1 material slot.

## LOD Plan

LOD0 full maul head; LOD1 removes minor bevels; LOD2 simplifies wraps and flanges; LOD3 preserves blunt head and haft.

## Collision Notes

Equipped collision disabled. World placement uses simple box/capsule collision.

## Animation Notes

Static mesh. Impact, ground slam, and carry motion belong to character animation and combat systems.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/Minotaur/SM_MIN_CrushingMaul_A01`
- Pivot: main hand grip.
- Scale: centimeters.
- Sockets: optional `socket_impact_vfx` after combat VFX rules are approved.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_MIN_CrushingMaul_A01/`
- Source: `SourceAssets/Blender/Kits/Minotaur/Arsenal/SM_MIN_CrushingMaul_A01/`
- Export: `SourceAssets/Exports/Kits/Minotaur/Arsenal/SM_MIN_CrushingMaul_A01/`
- Unreal: `/Game/Aerathea/Weapons/Minotaur/SM_MIN_CrushingMaul_A01`

## Quality Gate Checklist

- Brutal Minotaur identity is clear.
- Silhouette reads as a crushing weapon.
- No unnecessary ornament or magic glow.
- Collision and pivot are safe.
- LODs preserve head mass.
