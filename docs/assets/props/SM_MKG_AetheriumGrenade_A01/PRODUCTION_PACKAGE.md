# SM_MKG_AetheriumGrenade_A01 Production Package

## Art Direction Summary

- Asset name: `SM_MKG_AetheriumGrenade_A01`
- Asset type: Static Mesh throwable / inventory prop
- Source: `Gnome Armory.png#Grenades_AetheriumGrenade`
- Faction: Gnome / Mekgineer
- Status: Production package ready

Small round throwable with brass ribs, dark-iron casing, a protected blue Aetherium core window, and an oversized pull mechanism designed for gnome hands. It should read as volatile but engineered, with the glow contained.

## Gameplay Purpose

Supports future throwable item tests, inventory icons, loot/vendor display, workshop dressing, and VFX socket planning.

## Silhouette Notes

Use a squat oval/round body with large metal ribs and a visible pull ring or cap. The core window should be central and protected. Avoid overly smooth sci-fi grenade shapes.

## Scale Notes

- Target diameter: 18-24 cm.
- Pivot: center of mass.
- Socket candidates: `VFX_Core`, `PullRing`.

## Materials And Color Palette

Dark iron casing, brass/copper ribs, leather or rubberized grip band, blue Aetherium crystal/glass core. Add dark soot and edge wear through textures.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a gnome Mekgineer Aetherium grenade for the world of Aerathea. The design should emphasize a small round throwable silhouette, brass ribs, dark iron casing, a protected blue Aetherium core window, oversized gnome-friendly pull mechanism, and volatile engineered mood. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a small prop turnaround and inventory-icon source on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model the main shell, large ribs, cap, pull ring, and core frame as geometry. Texture small screws, scorch marks, stamped safety runes, micro dents, and seams.

## Texture And Material Notes

- `T_MKG_AetheriumGrenade_A01_BC`
- `T_MKG_AetheriumGrenade_A01_N`
- `T_MKG_AetheriumGrenade_A01_ORM`
- `T_MKG_AetheriumGrenade_A01_E`

Use one material slot where possible; emissive channel only for the core window.

## Triangle Budget

LOD0 target: 1k-2.5k tris.

## LOD Plan

- LOD0: full ribbed body, pull ring, cap, core window.
- LOD1: reduce rib bevels and pull ring detail.
- LOD2: merge cap/ring detail into simplified forms.
- LOD3: round silhouette with core color mark.

## Collision Notes

Equipped/held collision disabled. World pickup uses simple sphere or capsule collision. Projectile collision is gameplay-owned by future throwable Blueprint, not by the static mesh.

## Animation Notes

Static mesh baseline. Future throw, arm, detonate, and VFX are handled by character/Blueprint systems.

## Unreal Import Notes

- Folder: `/Game/Aerathea/Props/Mekgineer/Armory/`
- Mesh: `SM_MKG_AetheriumGrenade_A01`
- Material instance: `MI_MKG_AetheriumGrenade_A01`
- Pivot: center of mass
- Sockets: `VFX_Core`, `PullRing`
- Collision: simple pickup sphere if world-placed

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_MKG_AetheriumGrenade_A01/`
- Source: `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01/`
- Export: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_AetheriumGrenade_A01/`

## Quality Gate Checklist

- Original gnome/Mekgineer throwable silhouette.
- Aetherium core is protected and restrained.
- Projectile behavior is not baked into the mesh.
- Inventory-icon readability considered.
- LOD0-LOD3, collision, sockets, texture maps, and Unreal path defined.
