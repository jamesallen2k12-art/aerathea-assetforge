# KIT_MKG_Armory_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_MKG_Armory_A01`
- Asset type: Production Kit / Multi-Asset Gear Set
- World: Aerathea
- Faction anchor: Gnome / Mekgineer
- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Armory.png`
- Current status: Kit package ready, child asset intake complete, all catalog child production packages and handoffs documented; first ten child DCC meshes imported or fit-previewed

`Gnome Armory.png` is a catalog sheet, not a single prop. This kit defines the production direction for compact gnome-scale weapons, Mek-linked devices, tools, armor modules, grenades, backpacks, power modules, and Aetherium core variants.

The visual language is compact, rugged, brass-and-dark-iron engineering with leather grips, blue Aetherium power elements, and practical field-worn silhouettes. Designs should look built small but engineered big, matching the approved gnome anchor and existing `SM_MKG_WorkshopPropCrate_A01` material language.

## Gameplay Purpose

This kit supports:

- Gnome/Mekgineer character equipment.
- Workshop dressing and armory displays.
- Future loot, vendor, crafting, and class identity assets.
- Weapon and gear socket planning for gnome characters and Mek suits.
- Reusable material language for brass, copper, dark iron, leather, and Aetherium cores.

Primary production goal: use the completed armory breakdown to build individual weapons, gear pieces, armor modules, packs, and material variants in controlled DCC priority order.

## Silhouette Notes

All child assets should preserve:

- Compact gnome-scale proportions.
- Large readable handles, barrels, plates, cores, and profile breaks.
- Chunky silhouettes that read at MMO camera distance.
- Blue Aetherium cores as focal points, not full-surface glow.
- Brass/copper/dark-iron shape contrast.

Avoid:

- Tiny exposed gears as modeled geometry unless they change silhouette.
- Thin wires, loose chains, or dense rivet fields.
- Overly modern firearm shapes.
- Oversized human-scale proportions that ignore gnome ergonomics.

## Scale Notes

- Gnome reference height: about 91-122 cm.
- Human comparison from source concept: about 183 cm.
- Gear should feel intentionally compact and serviceable by small hands.
- Pistols, tools, packs, and grenades should be readable in first-person/item preview and at third-person camera distance.

Recommended approximate child scales:

- One-handed weapons/tools: 35-65 cm.
- Pistols: 30-45 cm.
- Compact rifles: 80-115 cm.
- Grenades: 18-28 cm.
- Backpacks/power modules: 45-70 cm tall.
- Armor modules: scaled for gnome body variants, not human body proportions.

## Materials And Color Palette

Primary materials:

- Brass: worn warm gold.
- Copper: muted orange-brown metal.
- Dark iron: charcoal metal with blue-gray worn edges.
- Leather: dark brown straps, grips, harnesses.
- Aetherium: saturated blue crystal/glass/core elements.
- Cloth padding: desaturated workwear fabric.

Texture style:

- Hand-painted edge highlights.
- Baked-AO-style depth in sockets, rivet lines, and panel seams.
- Normal-map detail for small screws, fine gears, scratches, stitching, and stamped marks.
- Emissive only for powered Aetherium cores, lenses, reactors, and active weapons.

## Concept Reference

- Source file: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Armory.png`
- Child intake: `docs/assets/kits/KIT_MKG_Armory_A01/CHILD_ASSET_INTAKE.md`
- Storage note: source PNG remains in the desktop Asset Concepts folder until project asset-storage policy changes.

## Modeling Notes

Use the documented child packages before DCC modeling. For each child asset, decide whether the build pass is:

- Static mesh.
- Skeletal mesh.
- Modular attachment.
- Blueprint actor.
- Material variant.
- UI inventory icon source.

Model real geometry for:

- Main silhouettes.
- Large barrels, blades, grips, plates, shields, packs, cores, and housings.
- Functional hinges or folding parts when they affect gameplay/readability.
- Large sockets, nozzles, and power housings.

Fake with textures/normal maps:

- Tiny rivets.
- Micro gears.
- Fine scratches.
- Etched measuring marks.
- Leather stitching.
- Small screws.
- Panel seam grime.

## Texture And Material Notes

Kit material families:

- `MI_MKG_Armory_BrassDarkIron_A01`
- `MI_MKG_Armory_LeatherWorkwear_A01`
- `MI_MKG_Armory_AetheriumCore_A01`

Child textures should follow:

- `T_MKG_<ChildAsset>_BC`
- `T_MKG_<ChildAsset>_N`
- `T_MKG_<ChildAsset>_ORM`
- `T_MKG_<ChildAsset>_E` only for powered Aetherium elements.

Use shared trim/material atlases where practical for low-risk small gear. Use unique texture sets for hero items, weapons with readable painted markings, and major backpacks/reactors.

## Triangle Budget

Recommended child budgets:

- Small one-handed weapon/tool: LOD0 800-2.5k tris, 1 material.
- Pistol/grenade: LOD0 1k-3k tris, 1 material.
- Compact rifle: LOD0 2.5k-6k tris, 1-2 materials.
- Shield/backpack/reactor: LOD0 3k-8k tris, 1-2 materials.
- Armor module: LOD0 2k-6k tris per module, shared material preferred.
- Full armor configuration preview: LOD0 15k-25k tris if treated as character gear over gnome body.

## LOD Plan

Create LOD0-LOD3 for important child meshes.

Reduce details in this order:

1. Tiny rivets, screws, and etched marks.
2. Small wires, small vents, and micro gears.
3. Secondary bevel loops.
4. Minor side panels.
5. Interior or underside details.
6. Small animated pieces.

Preserve primary silhouette, hand grips, large cores, barrels, blades, and armor module profiles.

## Collision Notes

Default collision by child type:

- Weapons/tools/grenades: no runtime blocking collision unless world-placed; simple pickup bounds if interactive.
- Display props: simple box/capsule collision.
- Shields/backpacks: character attachment collision disabled by default; use physics asset only if needed.
- Blueprint devices/reactors: simple interaction bounds.

Do not use complex-as-simple collision for runtime gear displays.

## Animation Notes

Baseline static meshes need no animation.

Potential animated or socketed items:

- Folding shield: fold/unfold states.
- Linked tool rig: socketed tool attachments.
- Aetherium reactor/power modules: core idle pulse material state.
- Grenades: throw/use animations handled by character systems later.
- Armor configurations: skeletal/attachment rules after gnome rig direction is approved.

## Unreal Import Notes

Recommended content roots:

- `/Game/Aerathea/Props/Mekgineer/Armory/`
- `/Game/Aerathea/Weapons/Mekgineer/`
- `/Game/Aerathea/Characters/Gnomes/Gear/`
- `/Game/Aerathea/Materials/Props/Mekgineer/Armory/`
- `/Game/Aerathea/Textures/Props/Mekgineer/Armory/`
- `/Game/Aerathea/Blueprints/Props/Mekgineer/Armory/`

Kit-level package name:

- `KIT_MKG_Armory_A01`

Child asset names should use `SM_MKG_`, `SK_GNM_`, `BP_MKG_`, `MI_MKG_`, and `T_MKG_` prefixes as appropriate.

## Folder And Naming Recommendation

Documentation:

- `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_MKG_Armory_A01/CHILD_ASSET_INTAKE.md`

Future source files:

- `SourceAssets/Blender/Kits/Mekgineer/Armory/`
- `SourceAssets/Exports/Kits/Mekgineer/Armory/`

Do not commit large source meshes until the source-asset policy is approved.

## Quality Gate Checklist

- Child assets split from the source collage.
- Gnome scale and ergonomics preserved.
- Brass/copper/dark iron/leather/Aetherium language is consistent.
- Aetherium glow used sparingly.
- Each child item has a production package and proposed asset name before modeling.
- Triangle budget chosen by child type.
- Texture map plan uses BC, N, ORM, and optional E.
- LOD0-LOD3 expected for important meshes.
- Collision and socket behavior defined per child asset.
- Original Aerathea identity preserved.
- No copied franchise weapons, names, or gear designs.
