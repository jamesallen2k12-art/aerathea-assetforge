# SM_DWR_OathkeeperHammer_A01 Production Package

## Art Direction Summary

- Asset name: `SM_DWR_OathkeeperHammer_A01`
- Asset type: Static Mesh one-handed hammer
- Source: `Dwarven Armory.png#Hammer_Oathkeeper`
- Parent kit: `KIT_DWR_Armory_A01`
- Status: Production package ready; DCC build not started

Original Aerathea Dwarven guardian hammer with a compact square head, dense mountain-forged mass, blue rune inlay, worn steel, aged brass bands, and leather grip.

## Gameplay Purpose

One-handed warrior/runesmith weapon for starter combat, armory display, vendor preview, and socket testing against future Dwarven body packages.

## Silhouette Notes

Keep a broad rectangular hammer head, short heavy haft, visible rune face, and capped pommel. Avoid thin heroic-fantasy exaggeration; this should read as dense and practical.

## Scale Notes

55-75 cm long. Author in centimeters. Grip sized for broad Dwarven hands.

## Materials And Color Palette

Dark steel, slate stone inset, aged brass bands, dark leather grip, and sparing blue runic Aetherium glow.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_DWR_OathkeeperHammer_A01` for the world of Aerathea. The design should emphasize a compact square hammer silhouette, mountain-forged steel and stone, aged brass bands, dark leather grip, blue runic Aetherium inlay, solemn Dwarven guardian identity, and one-handed tank/runesmith gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, three-quarter view, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model the hammer head, haft, grip caps, major bevels, brass bands, and rune recesses as geometry. Fake tiny hammer marks, scratches, rune chipping, and leather grain in textures.

## Texture And Material Notes

- `T_DWR_OathkeeperHammer_A01_BC`
- `T_DWR_OathkeeperHammer_A01_N`
- `T_DWR_OathkeeperHammer_A01_ORM`
- `T_DWR_OathkeeperHammer_A01_E` for rune glow only

## Triangle Budget

LOD0 2k-4k tris, 1 material slot.

## LOD Plan

LOD0 full silhouette; LOD1 removes small bevels; LOD2 simplifies rune recesses and bands; LOD3 preserves hammer head, haft, and glow read.

## Collision Notes

Equipped collision disabled. World pickup/display uses simple box/capsule bounds.

## Animation Notes

Static mesh. Swing, impact, block, and sheathe motion belongs to character animation and item Blueprint systems later.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/Dwarven/SM_DWR_OathkeeperHammer_A01`
- Pivot: grip center at main hand hold.
- Scale: 1 Unreal unit = 1 cm.
- Sockets: add `socket_rune_glow` only if VFX is authored.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_DWR_OathkeeperHammer_A01/`
- Source: `SourceAssets/Blender/Kits/Dwarven/Armory/SM_DWR_OathkeeperHammer_A01/`
- Export: `SourceAssets/Exports/Kits/Dwarven/Armory/SM_DWR_OathkeeperHammer_A01/`
- Unreal: `/Game/Aerathea/Weapons/Dwarven/SM_DWR_OathkeeperHammer_A01`

## Quality Gate Checklist

- Original to Aerathea and aligned with the Dwarven anchor.
- Dense square hammer silhouette reads at MMO camera distance.
- Glow is limited to runic inlay.
- Tiny metal wear and leather grain are texture/normal detail.
- Triangle budget, texture maps, LODs, collision, and Unreal path are defined.
