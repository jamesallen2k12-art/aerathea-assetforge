# KIT_ORC_ShamanicTalismans_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_ORC_ShamanicTalismans_A01`
- Asset type: Prop/accessory mini-kit
- Source: `Orc Arsenal.png#ShamanicTalismans`
- Parent kit: `KIT_ORC_Arsenal_A01`
- Status: Production package ready; DCC build not started

Original Orc talisman set with bone, leather, spirit stones, clan cords, feathers or fur tokens, and restrained blue-green spiritual glow.

## Gameplay Purpose

Accessory props for Orc shamans, warriors, camps, weapons, shields, and NPC dressing.

## Silhouette Notes

Readable charm clusters with large token shapes. Avoid many tiny dangling elements that would be noisy or expensive.

## Scale Notes

Individual charms 8-25 cm; clusters 20-45 cm. Fit belts, weapons, shields, and neck/chest attachments.

## Materials And Color Palette

Bone, leather cord, bronze rings, fur, muted clan cloth, spirit stone blue-green glow.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_ORC_ShamanicTalismans_A01` for the world of Aerathea. The design should emphasize readable bone and leather charm clusters, bronze rings, fur and clan cloth tokens, blue-green spirit stones, noble Orc spirituality, shamanic culture, and accessory gameplay roles for weapons, shields, belts, camps, and NPCs. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a talisman catalog with several cluster variants, attachment callouts, scale notes, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model only large tokens, cords, rings, and stones. Fake small carving, weave, tooth marks, and stitch detail in maps.

## Texture And Material Notes

- `T_ORC_ShamanicTalismans_A01_BC`
- `T_ORC_ShamanicTalismans_A01_N`
- `T_ORC_ShamanicTalismans_A01_ORM`
- `T_ORC_ShamanicTalismans_A01_E` for spirit stones only

## Triangle Budget

LOD0 500-1.5k tris per charm; 2k-4k per cluster.

## LOD Plan

LOD0 full cluster; LOD1 removes small cords; LOD2 merges tokens; LOD3 keeps primary charm mass.

## Collision Notes

No blocking collision when attached. Optional small pickup overlap for loose props.

## Animation Notes

Static baseline. Limited secondary motion only if later justified by character rig or Blueprint.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Props/Orc/KIT_ORC_ShamanicTalismans_A01`
- Pivot: attachment cord or cluster center depending on use.
- Scale: centimeters.
- Sockets: `socket_talisman_attach` on target assets when needed.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_ORC_ShamanicTalismans_A01/`
- Source: `SourceAssets/Blender/Kits/Orc/Arsenal/KIT_ORC_ShamanicTalismans_A01/`
- Export: `SourceAssets/Exports/Kits/Orc/Arsenal/KIT_ORC_ShamanicTalismans_A01/`
- Unreal: `/Game/Aerathea/Props/Orc/`

## Quality Gate Checklist

- Orc spirituality is respectful and original.
- Charm clusters remain readable.
- Glow is limited to spirit stones.
- Attachment pivots are clear.
- Triangle budgets stay MMO-safe.
