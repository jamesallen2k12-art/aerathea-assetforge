# SM_MKG_SparkPistol_A01 Production Package

## Art Direction Summary

- Asset name: `SM_MKG_SparkPistol_A01`
- Asset type: Static Mesh one-handed firearm / gear prop
- Source: `Gnome Armory.png#Pistols_SparkPistol`
- Faction: Gnome / Mekgineer
- Status: Production package ready

Short, heavy, gnome-scale spark pistol with a chunky barrel, dark-iron muzzle ring, brass chamber, leather grip, and one small blue Aetherium capacitor. It should feel like a compact field tool that throws a spark, not a modern handgun.

## Gameplay Purpose

Supports Mekgineer ranged weapon identity, display/rack props, loot previews, and future muzzle/socket tests.

## Silhouette Notes

Use a thick barrel, compact grip, large chamber, and clear muzzle opening. Avoid long sleek pistol profiles. The silhouette should read from the side at third-person MMO distance.

## Scale Notes

- Target length: 30-42 cm.
- Pivot: grip center for hand socketing.
- Sockets: `Muzzle`, `AetheriumCore`, optional `Grip`.

## Materials And Color Palette

Dark iron barrel and muzzle, brass/copper chamber, dark leather grip, blue Aetherium capacitor lens. Use soot-darkened muzzle texture and painted edge wear.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a compact gnome Mekgineer spark pistol for the world of Aerathea. The design should emphasize a short thick barrel, brass and dark iron chamber, leather grip, small blue Aetherium capacitor, clever field-engineering culture, and rugged reliable mood. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a side-view weapon sheet with muzzle and core callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model the barrel, chamber, grip, trigger guard, muzzle ring, and capacitor housing as real geometry. Texture small screws, soot, tiny gauge marks, grip stitching, and panel scratches.

## Texture And Material Notes

- `T_MKG_SparkPistol_A01_BC`
- `T_MKG_SparkPistol_A01_N`
- `T_MKG_SparkPistol_A01_ORM`
- `T_MKG_SparkPistol_A01_E`

Use one material slot for baseline; second slot only if shared Aetherium glass is needed.

## Triangle Budget

LOD0 target: 1.5k-3k tris.

## LOD Plan

- LOD0: full barrel, chamber, grip, trigger guard, sockets.
- LOD1: simplify bevels and trigger detail.
- LOD2: reduce chamber rings and capacitor frame.
- LOD3: side silhouette with simple barrel/grip/chamber.

## Collision Notes

No blocking collision while equipped. World pickup/display uses simple box collision.

## Animation Notes

Static mesh baseline. Future firing behavior uses muzzle socket and material flash/VFX, not modeled moving internals for first pass.

## Unreal Import Notes

- Folder: `/Game/Aerathea/Weapons/Mekgineer/`
- Mesh: `SM_MKG_SparkPistol_A01`
- Material instance: `MI_MKG_SparkPistol_A01`
- Pivot: grip center
- Sockets: `Muzzle`, `AetheriumCore`
- Collision: simple pickup bounds if world-placed

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_MKG_SparkPistol_A01/`
- Source: `SourceAssets/Blender/Kits/Mekgineer/Armory/SM_MKG_SparkPistol_A01/`
- Export: `SourceAssets/Exports/Kits/Mekgineer/Armory/SM_MKG_SparkPistol_A01/`

## Quality Gate Checklist

- Compact gnome-scale firearm silhouette.
- Not modern firearm shaped.
- Muzzle/core sockets planned.
- Glow used sparingly.
- LOD0-LOD3, collision, texture maps, and Unreal path defined.
