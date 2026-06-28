# KIT_INF_BalgorothCult_A01 Production Package

## Art Direction Summary

`KIT_INF_BalgorothCult_A01` defines the cult symbol, ritual-site, material, and VFX language for Infernals. Balgoroth worship should feel severe, predatory, hierarchical, and sacrificial without relying on gore. The visual language supports Infernal body brands, cult dens, ritual arenas, sacrifice platforms, bloodline trials, Lesser Infernal training spaces, and mage/rogue/hunter class details.

The child asset split and first DCC target are tracked in `VISUAL_KIT_BREAKDOWN.md`. `SM_INF_CullingTrialFloor_A01` is the first accepted child package because it validates symbols, material states, collision, scale, and VFX channels before altar or Blueprint work. `SM_INF_HornWingArch_A01` is the next documented child package and covers guarded Infernal cult thresholds from the gate imagery.

## Gameplay Purpose

The kit supports Infernal settlements, encounter spaces, class VFX, faction props, quest locations, and readable cult identity. It gives artists and designers a shared visual source before individual ritual props, buildings, or VFX are built.

## Silhouette Notes

- Symbol language: horned crown, split wing, hooked tail crescent, claw slash, and ember eye motif.
- Ritual-site language: circular trial floors, claw-marked stones, wing-shaped arches, horned altars, dark chains, ash basins.
- Trial spaces should feel like arenas and proving grounds, not temples of passive worship.
- Sacrifice platforms should imply worthiness judgment; weak/unworthy victims may be left alive in the lore, so visual storytelling can show empty chains, broken circles, and witness positions.

## Scale Notes

- Props must support Spawn through Ancient Infernal scale.
- Doorways/arches should account for tall adult Infernals up to 274 cm plus horns and folded wings. `SM_INF_HornWingArch_A01` uses a minimum 360 cm by 260 cm clear opening for the first production target.
- Arena and trial sites should leave room for wing flares, tail sweeps, and claw combat.

## Materials And Color Palette

- Stone: black basalt, ash-gray stone, scorched red stone.
- Metal: blackened iron, dark bronze, obsidian insets.
- Organic: bone beads, horn fragments, old leather, ash cloth.
- Glow: ember red, deep orange, restrained violet abyssal marks.
- Surface detail: claw grooves, heat-cracked stone, worn ritual paths, ash staining, Balgoroth brands.

## Concept Image Prompt

Create an original stylized fantasy MMORPG cult material and ritual-site concept board for the Infernals of Aerathea. The design should emphasize Balgoroth worship, horned crown symbols, split wing and claw motifs, ash-black stone, scorched red stone, blackened iron, obsidian, bone ornaments, restrained ember and violet abyssal glow, proving arenas, culling temper trial spaces, sacrifice-worthiness platforms, and Infernal bloodline hierarchy. Use hand-painted texture detail, readable MMO silhouettes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and production-friendly modular forms. Present it as a kit board with symbols, altar, trial floor, banners, chains, brand marks, material swatches, VFX callouts, and scale beside 180 cm humanoid and tall Infernal. Avoid copied franchise designs, gore, excessive particles, readable text, and photoreal micro-detail.

## Modeling Notes

- Build modular ritual props after race body approval.
- Model real geometry for altars, arches, chains, basins, large symbols, standing stones, and trial-floor slabs.
- Use textures/normals for tiny brands, scratches, scorch marks, stone cracks, and fine cloth weave.
- Keep symbols readable at MMO distance; avoid text glyph dependency.
- Design with snap-friendly modules for arena floors and cult interiors.

## Texture And Material Notes

- Shared material set:
  - `T_INF_CultStone_A01_BC/N/ORM/E`
  - `T_INF_BlackIron_A01_BC/N/ORM`
  - `T_INF_ObsidianBone_A01_BC/N/ORM`
  - `T_INF_BrandGlow_A01_E`
- Emissive only for brands, eye motifs, altar cores, and active ritual channels.
- Material instances should support inactive, smoldering, and active states.

## Triangle Budget

- Small cult prop: 500-4k tris.
- Large ritual prop: 4k-10k tris.
- Modular altar/arena piece: 8k-18k tris depending scale.
- Interior ritual kit module: 12k-25k tris per assembled hero cluster.

## LOD Plan

- LOD0: full silhouette, symbol geometry, large chains, altar forms.
- LOD1: 60 percent; reduce small chains, minor stone cuts, secondary trims.
- LOD2: 30 percent; simplify symbol bevels, remove small ornaments.
- LOD3: 10-15 percent; preserve altar, horn/wing/claw symbol read, and glow color blocks.

## Collision Notes

- Use simple collision for altars, stones, walls, and platforms.
- Chains and small props should be non-blocking unless used for gameplay.
- Trial floors should use flat collision and avoid snagging tail/wing characters.

## Animation Notes

- Optional: low-frequency brand pulse, altar glow state, ash basin smoke, chain sway.
- Avoid constant heavy particle systems.
- VFX should support inactive, trial active, sacrifice accepted, and unworthy rejected states.

## Unreal Import Notes

- Asset type: Static Mesh kit, Material Instances, optional Blueprint Actors, optional VFX.
- Suggested root: `/Game/Aerathea/Props/Infernals/BalgorothCult/`.
- Materials: `/Game/Aerathea/Materials/Infernals/`.
- VFX: `/Game/Aerathea/VFX/Infernals/`.
- Naming examples:
  - `SM_INF_BalgorothAltar_A01`
  - `SM_INF_CullingTrialFloor_A01`
  - `SM_INF_HornWingArch_A01`
  - `MI_INF_CultStone_Smolder_A01`
  - `BP_INF_RitualAltar_A01`

## Folder And Naming Recommendation

- Package folder: `docs/assets/kits/KIT_INF_BalgorothCult_A01/`.
- Visual kit breakdown: `docs/assets/kits/KIT_INF_BalgorothCult_A01/VISUAL_KIT_BREAKDOWN.md`.
- First child package: `docs/assets/props/SM_INF_CullingTrialFloor_A01/PRODUCTION_PACKAGE.md`.
- Gate/threshold child package: `docs/assets/props/SM_INF_HornWingArch_A01/PRODUCTION_PACKAGE.md`.
- Source: `SourceAssets/Blender/Kits/Infernals/BalgorothCult/`.
- Export: `SourceAssets/Exports/Kits/Infernals/BalgorothCult/`.
- Unreal: `/Game/Aerathea/Props/Infernals/BalgorothCult/`.

## Quality Gate Checklist

- Balgoroth symbols are original to Aerathea and readable.
- Cult language supports culling temper, worthiness judgment, and natural-weapon doctrine.
- Ritual props do not depend on gore to communicate threat.
- Materials match Infernal red/black/ash/obsidian/ember language.
- Glow is sparing and tied to brands, eyes, altars, or ritual channels.
- LOD, collision, texture maps, and Unreal naming are specified.
