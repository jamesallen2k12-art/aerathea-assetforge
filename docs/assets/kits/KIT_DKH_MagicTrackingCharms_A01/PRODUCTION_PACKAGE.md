# KIT_DKH_MagicTrackingCharms_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_DKH_MagicTrackingCharms_A01`
- Asset type: Prop/accessory mini-kit
- Source: `Drakhar Arms Relics and Field Gear.png#Charms_MagicTracking`
- Parent kit: `KIT_DKH_FieldGear_A01`
- Status: Production package ready; DCC build not started

Original Drakhar charm set used to sense and collect magic, with bone, teeth, cords, ember stones, sealed relic fragments, and Volcreon-linked arcane motifs.

## Gameplay Purpose

Accessory props for Drakhar magic-sensing identity, belts, packs, staffs, weapons, NPCs, and relic-tracking gameplay hooks.

## Silhouette Notes

Readable charm clusters with large tokens and stones. Avoid dense strings of tiny unreadable trinkets.

## Scale Notes

Individual charms 8-25 cm; clusters 20-45 cm. Fit A04 Drakhar gear: females 3'6"-4'2", males 4'0"-4'6".

## Materials And Color Palette

Bone, teeth, leather cord, sun-baked stone, ember crystal, relic metal, low orange-blue arcane glow.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_DKH_MagicTrackingCharms_A01` for the world of Aerathea. The design should emphasize readable magic-tracking charm clusters, bone tokens, teeth, leather cords, sun-baked stones, ember crystals, sealed relic fragments, corrected A04 Drakhar scale, bearded-dragon desert-lizard identity, Volcreon-linked magic obsession, and relic-tracking gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a charm catalog with belt, weapon, pack, and hand-held attachment callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model large tokens, stones, cords, rings, and relic fragments. Fake tiny glyphs, scratches, cord fiber, and bone pores in textures.

## Texture And Material Notes

- `T_DKH_MagicTrackingCharms_A01_BC`
- `T_DKH_MagicTrackingCharms_A01_N`
- `T_DKH_MagicTrackingCharms_A01_ORM`
- `T_DKH_MagicTrackingCharms_A01_E` for ember/arcane stones only

## Triangle Budget

LOD0 500-1.5k tris per charm, 2k-4k per cluster.

## LOD Plan

LOD0 full cluster; LOD1 removes minor cords; LOD2 merges small tokens; LOD3 preserves primary charm silhouette and glow point.

## Collision Notes

No blocking collision while attached. Optional small overlap for pickup or magic-sense interactables.

## Animation Notes

Static baseline. Limited sway can be added only if attached to character gear with budget available.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Props/Drakhar/KIT_DKH_MagicTrackingCharms_A01`
- Pivot: attachment cord or cluster center.
- Scale: centimeters.
- Sockets: `socket_charm_attach`; optional `socket_magic_sense_vfx`.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_DKH_MagicTrackingCharms_A01/`
- Source: `SourceAssets/Blender/Kits/Drakhar/FieldGear/KIT_DKH_MagicTrackingCharms_A01/`
- Export: `SourceAssets/Exports/Kits/Drakhar/FieldGear/KIT_DKH_MagicTrackingCharms_A01/`
- Unreal: `/Game/Aerathea/Props/Drakhar/`

## Quality Gate Checklist

- Drakhar magic obsession is clear.
- Volcreon influence is implied through relic motifs, not copied franchise language.
- Correct scale is used.
- Glow is restrained.
- Attachment, collision, and LOD plans are defined.
