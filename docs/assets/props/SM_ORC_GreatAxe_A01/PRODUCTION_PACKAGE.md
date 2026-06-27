# SM_ORC_GreatAxe_A01 Production Package

## Art Direction Summary

- Asset name: `SM_ORC_GreatAxe_A01`
- Asset type: Static Mesh two-handed axe
- Source: `Orc Arsenal.png#GreatAxe_01`
- Parent kit: `KIT_ORC_Arsenal_A01`
- Status: Production package ready; DCC build not started

Original Aerathea Orc great axe with disciplined broad-blade silhouette, iron and bronze construction, bone/leather bindings, clan marks, and blue-green spiritual rune accents.

## Gameplay Purpose

Two-handed Orc warrior/champion weapon for combat identity, NPC variants, armory display, and heavy-weapon socket testing.

## Silhouette Notes

Broad axe head, strong haft, clear counterweight, and upright disciplined craft. Avoid savage caricature and chaotic spikes.

## Scale Notes

130-170 cm long. Fit upright powerful Orc proportions.

## Materials And Color Palette

Dark iron, bronze, bone, leather, muted clan cloth, blue-green spirit rune accents.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_ORC_GreatAxe_A01` for the world of Aerathea. The design should emphasize a broad disciplined great-axe silhouette, dark iron blade, bronze reinforcement, bone and leather bindings, muted clan color wraps, blue-green spirit rune accents, noble upright Orc identity, honorable warrior culture, and two-handed melee gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, three-quarter view, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model blade, haft, collar, counterweight, major wraps, and clan-token forms. Fake nicks, wood grain, stitching, and small rune marks in maps.

## Texture And Material Notes

- `T_ORC_GreatAxe_A01_BC`
- `T_ORC_GreatAxe_A01_N`
- `T_ORC_GreatAxe_A01_ORM`
- `T_ORC_GreatAxe_A01_E` for spirit rune accents only

## Triangle Budget

LOD0 3k-7k tris, 1-2 material slots.

## LOD Plan

LOD0 full axe; LOD1 removes small wraps; LOD2 simplifies token and collar detail; LOD3 preserves blade and haft outline.

## Collision Notes

Equipped collision disabled. World pickup/display uses simple long box/capsule.

## Animation Notes

Static mesh. Two-handed swings, blocks, and sheathe motion belong to character animation.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/Orc/SM_ORC_GreatAxe_A01`
- Pivot: main two-handed grip.
- Scale: centimeters.
- Sockets: optional `socket_spirit_rune`.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_ORC_GreatAxe_A01/`
- Source: `SourceAssets/Blender/Kits/Orc/Arsenal/SM_ORC_GreatAxe_A01/`
- Export: `SourceAssets/Exports/Kits/Orc/Arsenal/SM_ORC_GreatAxe_A01/`
- Unreal: `/Game/Aerathea/Weapons/Orc/SM_ORC_GreatAxe_A01`

## Quality Gate Checklist

- Orcs read as noble, disciplined, and upright.
- Broad axe silhouette is readable.
- Glow is restrained.
- Micro damage is texture detail.
- Heavy-weapon pivot and LOD plan are defined.
