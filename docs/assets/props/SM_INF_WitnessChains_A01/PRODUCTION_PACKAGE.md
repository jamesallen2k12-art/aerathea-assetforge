# SM_INF_WitnessChains_A01 Production Package

## Art Direction Summary

`SM_INF_WitnessChains_A01` is a Balgoroth cult static dressing set for worthiness chambers, Lesser trial dens, gate approaches, branding-stone alcoves, and altar walls. The chains should feel oppressive and ritualized, but they are not a gameplay restraint system in this package.

The design uses chunky blackened iron links, basalt wall/floor anchors, claw-shaped hooks, sparse bone/horn witness markers, ash wear, and small restrained ember channels. The chains must stay readable and performant: large forms carry the silhouette, while small scratches, soot, and link wear stay in textures and normal maps.

## Gameplay Purpose

- Adds non-blocking witness/restraint dressing to Balgoroth trial spaces.
- Provides snap-ready wall, floor, hanging, and broken-chain variants for ritual-room composition.
- Supports visual storytelling around worthiness judgment, culling temper, and witness punishment without adding gore.
- Provides optional future sockets for light ember pulses or chain-sway hooks, but no runtime behavior is implemented here.

## Silhouette Notes

- Primary read: thick chain lengths with oversized oval/knife-edged links and heavy anchor plates.
- Variants:
  - wall hanging chain pair
  - floor anchor chain coil
  - suspended witness chain loop
  - broken-chain fragment
  - anchor plate with claw hook
- Chain links should be few, large, and readable. Avoid hundreds of tiny modeled links.
- Anchors should use horned crown, claw slash, or broken-circle motifs only as broad relief forms.

## Scale Notes

- Wall chain pair: 180-320 cm hanging length.
- Floor anchor/coil: 80-160 cm footprint.
- Suspended loop: 100-220 cm drop.
- Broken fragments: 40-120 cm length.
- Link thickness should read beside a 180 cm humanoid and 274 cm Infernal without becoming fine jewelry.

## Materials and Color Palette

- Chain metal: blackened iron using `MI_INF_CultStone_BlackIron_A01`, dark bronze edge wear, no bright steel.
- Anchor stone: black basalt using `MI_INF_CultStone_Basalt_A01`.
- Scorched grooves: muted red-brown using `MI_INF_CultStone_ScorchedRed_A01`.
- Bone/horn markers: smoke-stained ivory, used sparingly.
- Emissive accents: tiny ember/deep-red pips in anchor grooves only, no glowing chain ropes.

## Concept Image Prompt

Create an original stylized fantasy MMORPG static mesh concept sheet of `SM_INF_WitnessChains_A01`, a Balgoroth cult witness-chain dressing set for the Infernals of Aerathea. The design should emphasize chunky blackened iron chain links, heavy basalt wall and floor anchors, claw-shaped hooks, broken-chain fragments, sparse smoke-stained bone markers, ash wear, broad horned crown and broken-circle relief motifs, restrained ember channel accents, and readable non-blocking ritual-room dressing for worthiness chambers, branding-stone alcoves, gate approaches, and Lesser trial dens. Use hand-painted texture detail, readable broad shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly mid-poly production geometry. Present it as a static mesh production sheet with wall hanging, floor anchor, suspended loop, broken fragment, and anchor plate variants, plus collision notes, socket callouts, material swatches, and scale beside a 180 cm humanoid and 274 cm Infernal. Apply A03-style cleanup if using Infernal source references: preserve large chains, stone anchors, skull/bone menace if used, claw grooves, brands, and villain threat while reducing tiny rivets, random speckle artifacts, malformed micro-spikes, broken micro-chains, dense hanging clutter, and photoreal noise. Avoid copied franchise symbols, gore, readable text, watermarks, tiny chain-link fields, and physics-heavy cloth/rope simulation.

## Modeling Notes

- Model large chain links, anchor plates, claw hooks, broken end caps, and major wall/floor brackets as real geometry.
- Use texture/normal maps for soot, scratches, pitted iron, ash, small dents, and link wear.
- Use modular link chunks rather than simulating every link independently.
- Make chain variants static by default. If a later task needs sway, author a separate skeletal/physics variant after approval.
- Avoid thin dangling micro-chains, dense rings, gore hooks, or restraint mechanisms that imply gameplay behavior.

## Texture and Material Notes

Texture targets:

- `T_INF_WitnessChains_A01_BC`
- `T_INF_WitnessChains_A01_N`
- `T_INF_WitnessChains_A01_ORM`
- `T_INF_WitnessChains_A01_E`

Recommended material slots:

1. `MI_INF_CultStone_BlackIron_A01`
2. `MI_INF_CultStone_Basalt_A01`
3. `MI_INF_CultStone_ScorchedRed_A01`
4. `MI_INF_CultStone_BoneHorn_A01`
5. `MI_INF_WitnessChains_A01_Emissive`

Material rules:

- Most variants should use 2-3 material slots.
- Use emissive only on anchor grooves or broken-circle relief pips.
- Chain wear should be value/roughness driven, not bright metallic shine.

## Triangle Budget

- Wall hanging pair LOD0: 2k-5k tris.
- Floor anchor/coil LOD0: 1.5k-4k tris.
- Suspended loop LOD0: 1.5k-4k tris.
- Broken fragment LOD0: 500-1.5k tris.
- Anchor plate LOD0: 700-2k tris.
- Hero assembled set: 6k-10k tris maximum, only when replacing other dressing.

## LOD Plan

- LOD0: full chain silhouettes, anchor relief, hooks, broken ends, major bevels.
- LOD1: 55-60 percent; reduce link bevels, small dents, secondary hook loops.
- LOD2: 25-35 percent; merge link clusters, flatten minor relief, preserve chain path and anchor silhouette.
- LOD3: 10-15 percent; preserve chain mass, anchor plates, and major dark metal/stone blocks only.

## Collision Notes

- Non-blocking by default for dressing.
- If a variant must block movement, use simple capsules/boxes around large chain masses and anchor plates only.
- Do not create complex per-link collision.
- Keep collision away from hanging decorative ends to avoid snagging wings, tails, or player capsules.
- No gameplay restraint collision is implied by this package.

## Animation Notes

- Static mesh by default.
- Optional future sockets:
  - `vfx_anchor_ember`
  - `vfx_chain_snap`
  - `snap_wall_anchor`
  - `snap_floor_anchor`
- Chain sway, physics constraints, break events, and gameplay restraint behavior are approval-gated future tasks.
- No skeletal mesh or simulated chain behavior is authored in this package.

## Unreal Import Notes

- Asset type: Static Mesh set.
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/WitnessChains/`
- Naming convention:
  - `SM_INF_WitnessChains_WallPair_A01`
  - `SM_INF_WitnessChains_FloorAnchor_A01`
  - `SM_INF_WitnessChains_SuspendedLoop_A01`
  - `SM_INF_WitnessChains_BrokenFragment_A01`
  - `SM_INF_WitnessChains_AnchorPlate_A01`
  - `MI_INF_WitnessChains_A01_Emissive`
  - `T_INF_WitnessChains_A01_BC`
  - `T_INF_WitnessChains_A01_N`
  - `T_INF_WitnessChains_A01_ORM`
  - `T_INF_WitnessChains_A01_E`
- Pivot:
  - wall variants at top/back anchor center
  - floor variants at bottom center
  - broken fragments at center bottom
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Collision: none or simple non-complex collision only.
- LODs: LOD0-LOD3 required for placed variants.

## Folder and Naming Recommendation

- Package folder: `docs/assets/props/SM_INF_WitnessChains_A01/`
- Related kit: `docs/assets/kits/KIT_INF_BalgorothCult_A01/`
- Related material package: `docs/assets/materials/MI_INF_CultStone_Set_A01/`
- Related symbol package: `docs/assets/props/SM_INF_BalgorothSigil_A01/`
- Source folder: `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/`
- Export folder: `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/`
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/WitnessChains/`

## Quality Gate Checklist

- Chains read as Balgoroth cult witness/restraint dressing, not generic dungeon chains.
- Link count is sparse and chunky enough for MMO camera readability.
- Material language follows `MI_INF_CultStone_Set_A01`.
- Large links, anchors, hooks, and broken ends are geometry; soot, pitting, scratches, and small wear stay in maps.
- No complex per-link collision, physics simulation, gameplay restraint behavior, gore, readable text, or copied symbols are claimed.
- Triangle budget, material slots, texture targets, LOD0-LOD3, collision, pivots, sockets, and Unreal paths are defined.
