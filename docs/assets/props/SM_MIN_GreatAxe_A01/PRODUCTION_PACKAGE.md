# SM_MIN_GreatAxe_A01 Production Package

## Art Direction Summary

- Asset name: `SM_MIN_GreatAxe_A01`
- Asset type: Static Mesh two-handed axe
- Source: `Minotaur Arsenal.png#GreatAxe_01`
- Parent kit: `KIT_MIN_Arsenal_A01`
- Status: Production package ready; DCC build not started

Original Minotaur great axe with simple brutal construction, raw iron blade, heavy wood haft, hide wraps, bone tokens, and no refined magic language.

## Gameplay Purpose

Heavy weapon for Minotaur warriors and berserkers, NPC combat identity, armory display, and large-scale weapon socket tests.

## Silhouette Notes

Huge broad axe head, thick haft, simple counterweight, and efficient brutal profile. Avoid ornate craftsmanship and magical study motifs.

## Scale Notes

170-230 cm long. Fit approved Minotaur scale: females 7-8 ft, males 8-9 ft.

## Materials And Color Palette

Raw iron, dark wood, hide, bone, fur, leather, worn tribal markings.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_MIN_GreatAxe_A01` for the world of Aerathea. The design should emphasize a huge brutal great-axe silhouette, raw iron blade, heavy wood haft, hide and leather wraps, bone tokens, worn tribal markings, ruthless strength-respecting Minotaur identity, and two-handed berserker gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, three-quarter view, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model blade, haft, collar, wraps, bone tokens, and counterweight. Fake scratches, dents, hide grain, and markings in textures.

## Texture And Material Notes

- `T_MIN_GreatAxe_A01_BC`
- `T_MIN_GreatAxe_A01_N`
- `T_MIN_GreatAxe_A01_ORM`
- No emissive texture unless future lore explicitly adds a non-magic effect

## Triangle Budget

LOD0 3k-7k tris, 1 material slot.

## LOD Plan

LOD0 full axe; LOD1 removes minor wrap bevels; LOD2 simplifies tokens/collar; LOD3 preserves axe head and haft.

## Collision Notes

Equipped collision disabled. World pickup/display uses long box/capsule bounds.

## Animation Notes

Static mesh. Heavy swings, impacts, and idle carry belong to Minotaur animation systems.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/Minotaur/SM_MIN_GreatAxe_A01`
- Pivot: main two-handed grip.
- Scale: centimeters.
- Sockets: none required at this stage.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_MIN_GreatAxe_A01/`
- Source: `SourceAssets/Blender/Kits/Minotaur/Arsenal/SM_MIN_GreatAxe_A01/`
- Export: `SourceAssets/Exports/Kits/Minotaur/Arsenal/SM_MIN_GreatAxe_A01/`
- Unreal: `/Game/Aerathea/Weapons/Minotaur/SM_MIN_GreatAxe_A01`

## Quality Gate Checklist

- Minotaur weapon reads simple, heavy, and brutal.
- No refined magic language is introduced.
- Primary silhouette is large and readable.
- Micro wear is texture detail.
- LOD and collision plans are defined.
