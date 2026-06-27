# SK_GNM_ClimbingHarness_MKG_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GNM_ClimbingHarness_MKG_A01`
- Asset type: Skeletal/attachable equipment
- Source: `Gnome Armory.png#Utility_ClimbingHarness`
- Parent kit: `KIT_MKG_Armory_A01`
- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Armory.png`
- Faction/theme: Gnome / Mekgineer
- Status: Production package and handoff ready; DCC build not started; final fit blocked on `SK_GNM_Base_A01` source mesh and skeleton approval

Create an original Aerathea gnome/Mekgineer child asset from the armory catalog. This package keeps the compact, rugged, Aetherium-powered language established by `KIT_MKG_Armory_A01` and the first five completed child props.

## Gameplay Purpose

Supports strapped traversal gear for gnome scout and engineer loadouts. It can also serve future loot, crafting, vendor preview, armory display, equipment socket, and startup-scene review workflows where appropriate.

## Silhouette Notes

Primary read: wide waist harness, thigh loops, large belt buckle, hook ring, and sturdy leather straps. Preserve the large readable forms first; any tiny screws, rivets, wire runs, gauge ticks, and surface scratches must be texture or normal-map detail.

## Scale Notes

fits `SK_GNM_Base_A01`; cloth/strap deformation tied to body approval. Author in centimeters. Keep handles, grips, buttons, and attachment zones usable by compact 3-4 ft gnomes rather than human-scale proportions.

## Materials And Color Palette

Brass, copper, dark iron, dark brown leather, desaturated workwear cloth where needed, and one restrained blue Aetherium accent. Use hand-painted edge highlights, baked-AO-style socket depth, and normal-map detail for tiny screws, scratches, stitching, and micro gears.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_GNM_ClimbingHarness_MKG_A01`, a skeletal/attachable equipment for the world of Aerathea. The design should emphasize wide waist harness, thigh loops, large belt buckle, hook ring, and sturdy leather straps, compact gnome-scale ergonomics, brass and dark-iron engineering, dark leather utility details, restrained blue Aetherium accents, curious Mekgineer culture, and strapped traversal gear for gnome scout and engineer loadouts. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, three-quarter view, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Block against `SK_GNM_Base_A01` once the body source mesh exists. Model primary armor plates, harness straps, boots, gloves, hardpoints, and core housings as real geometry. Texture tiny rivets, stitching, scratches, and fine seams.

## Texture And Material Notes

- `T_GNM_ClimbingHarness_MKG_A01_BC`
- `T_GNM_ClimbingHarness_MKG_A01_N`
- `T_GNM_ClimbingHarness_MKG_A01_ORM`
- `T_GNM_ClimbingHarness_MKG_A01_E` only for the explicit blue Aetherium lens/core/window
- Prefer one material slot; use two only when a backpack, rifle, shield, or configuration needs a shared core material split.

## Triangle Budget

LOD0 2.5k-5k tris, shared leather/metal material.

## LOD Plan

LOD0 full silhouette; LOD1 removes small bevels and secondary bands; LOD2 simplifies side panels, sockets, and minor straps; LOD3 preserves only primary silhouette, grips/attachment volumes, and major blue core/lens read.

## Collision Notes

Equipped attachment collision disabled by default. Use gnome capsule/physics asset for character movement and add per-module physics bodies only after the gnome base skeleton is approved.

## Animation Notes

Driven by the future gnome skeleton and attachment rules. Do not author independent animation until `SK_GNM_Base_A01` proportions, sockets, and skeleton are approved.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Characters/Gnomes/Gear/SK_GNM_ClimbingHarness_MKG_A01`
- Pivot: use the scale notes above; equipped items pivot at grip/attachment point, world props at bottom center unless otherwise stated.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Collision: simple pickup/display bounds only unless gameplay later requires a dedicated Blueprint.
- Material slot count: follow the texture/material notes above.
- Sockets: add `socket_muzzle`, `socket_beam`, `socket_flame`, `socket_cable`, `back_pack`, or module attachment sockets only when named in scale notes or gameplay purpose.

## Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_GNM_ClimbingHarness_MKG_A01/`
- Source: `SourceAssets/Blender/Characters/Gnomes/Gear/SK_GNM_ClimbingHarness_MKG_A01/`
- Export: `SourceAssets/Exports/Characters/Gnomes/Gear/SK_GNM_ClimbingHarness_MKG_A01/`
- Unreal: `/Game/Aerathea/Characters/Gnomes/Gear/SK_GNM_ClimbingHarness_MKG_A01`

## Quality Gate Checklist

- Original to Aerathea and aligned with the approved gnome/Mekgineer anchor.
- Compact gnome scale and ergonomics are preserved.
- Primary silhouette reads from MMO camera distance.
- Brass, copper, dark iron, leather, and blue Aetherium language is consistent.
- Glow is sparing and justified by a core, lens, muzzle, reactor, or Aetherium shard.
- Tiny rivets, scratches, stitching, and micro gears are texture/normal detail.
- Triangle budget, texture maps, LODs, collision, and Unreal path are defined.
- DCC source waits for approval when body fit, skeleton, or gameplay rules are unresolved.
