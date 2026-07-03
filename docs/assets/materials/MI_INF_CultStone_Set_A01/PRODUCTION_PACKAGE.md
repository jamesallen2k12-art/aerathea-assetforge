# MI_INF_CultStone_Set_A01 Production Package

## Art Direction Summary

`MI_INF_CultStone_Set_A01` is the shared Balgoroth cult material set for Infernal ritual floors, horn-wing arches, worthiness altars, sigils, ash basins, witness chains, banners, branding stones, and Lesser trial dens.

The set locks the black basalt, ash-gray stone, scorched red stone, obsidian inset, blackened iron, bone/horn, ash cloth, and restrained ember-channel language so later cult props do not drift into unrelated stone, metal, or fire palettes.

## Gameplay Purpose

- Gives DCC and Unreal lanes one reusable material target for Balgoroth cult props.
- Supports inactive, smolder, trial-active, accepted, rejected, and cooldown readability without multiplying material slots.
- Provides texture and scalar rules for props that consume `VFX_INF_WorthinessJudgment_A01`, `MI_INF_BrandGlowStates_A01`, and future `VFX_INF_RegenerationBrand_A01`.

## Silhouette Notes

This is a material package, so silhouette comes from consuming meshes. The material must preserve large cult forms at MMO camera distance by emphasizing broad value separation:

- black basalt masses
- ash-gray chipped edges
- scorched red channel insets
- controlled ember seams
- restrained violet only on rejection/curse states

Do not use noisy micro-cracks, dense sparkle, or tiny rune fields that flatten the mesh read.

## Scale Notes

- Works on small props from 50 cm up to large 650 cm arch pieces.
- Texture scale should support 1 m, 2 m, and 4 m modular stone chunks without obvious repetition.
- Emissive channels should remain readable on Spawn-scale props but must not bloom over 9' adult Infernal silhouettes.

## Materials And Color Palette

Material instances:

- `MI_INF_CultStone_Basalt_A01`: blue-black basalt, ash-gray edge wear, low roughness variation.
- `MI_INF_CultStone_ScorchedRed_A01`: dark red-brown stone, heat stress, muted ember seams.
- `MI_INF_CultStone_ObsidianInset_A01`: near-black glossy insets with sharp gray highlights.
- `MI_INF_CultStone_BlackIron_A01`: blackened iron, dark bronze edge wear, no bright steel.
- `MI_INF_CultStone_BoneHorn_A01`: smoke-stained ivory, old horn, low saturation.
- `MI_INF_CultStone_AshCloth_A01`: black/ash cloth with blood-dark red trim.
- `MI_INF_CultStone_EmissiveChannel_A01`: ember-orange/deep-red channel glow with optional rejected violet pulse.

Texture targets:

- `T_INF_CultStone_A01_BC`
- `T_INF_CultStone_A01_N`
- `T_INF_CultStone_A01_ORM`
- `T_INF_CultStone_A01_E`
- `T_INF_BlackIron_A01_BC`
- `T_INF_BlackIron_A01_N`
- `T_INF_BlackIron_A01_ORM`
- `T_INF_ObsidianBone_A01_BC`
- `T_INF_ObsidianBone_A01_N`
- `T_INF_ObsidianBone_A01_ORM`
- `T_INF_AshCloth_A01_BC`
- `T_INF_AshCloth_A01_N`
- `T_INF_AshCloth_A01_ORM`
- `T_INF_BrandGlow_A01_E`

## Concept Image Prompt

Create an original stylized fantasy MMORPG material board for `MI_INF_CultStone_Set_A01` in the world of Aerathea. The design should emphasize Balgoroth cult black basalt, ash-gray chipped stone, scorched red ritual channels, obsidian insets, blackened iron braces, smoke-stained bone and horn, ash cloth, restrained ember-orange glow, deep red brand channels, and short violet rejection accents. Use hand-painted texture detail, readable broad shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a clean material swatch board with inactive, smolder, trial active, accepted, rejected, and cooldown examples on stone slabs, arch pieces, altar insets, chains, basins, and banners. Avoid copied franchise symbols, gore, excessive micro-cracks, readable text, watermarks, full-screen fire, and photoreal noise.

## Modeling Notes

- Consuming meshes should reserve separate material IDs only for major readable regions.
- Use geometry for large stone breaks, raised symbol plates, big iron braces, and major horn/bone pieces.
- Use normal maps for fine stone cracks, ash smears, scratches, cloth weave, small dents, and minor heat stress.
- Keep material slots low: most props should use 1-3 slots, hero ritual props 3-5 slots only when justified.

## Texture And Material Notes

Recommended parent material controls:

- `StateIndex`
- `GlowIntensity`
- `ChannelOpacity`
- `RejectedVioletMix`
- `AshWearAmount`
- `EdgeWearAmount`
- `HeatCrackAmount`
- `RoughnessBias`

State rules:

- Inactive: `GlowIntensity` near zero, surface forms still readable.
- Smolder: low ember channel only.
- Trial active: stronger red-orange channels, no broad bloom.
- Accepted: warm focused ember at core/sigil zones.
- Rejected: short violet-red pulse only, not a persistent aura.
- Cooldown: glow fades to ash and ember flecks.

Texture resolution:

- 1K for small props.
- 2K for shared hero prop atlases.
- 4K only for a hero environment cluster after visual approval.

## Triangle Budget

No triangle cost directly. This package controls material-slot and texture-cost budgets for consuming assets:

- Small prop: 1 material, 512-1K texture set.
- Large prop: 1-2 materials, 1K-2K texture set.
- Hero ritual prop or modular cluster: 3-5 materials, 2K shared atlas, 4K only if approved.

## LOD Plan

- LOD0: full material blend, edge wear, emissive channels, normal detail.
- LOD1: reduce emissive pulse frequency and fine normal intensity.
- LOD2: flatten small cracks and ash variation; preserve broad color blocks.
- LOD3: static color/emissive mask only; no animated scalar pulses except required gameplay state.

## Collision Notes

No collision. Consuming meshes own collision. Material glow must not imply gameplay collision unless the Blueprint or mesh package defines it.

## Animation Notes

- Scalar-only state animation is allowed for smolder, trial active, accepted, rejected, and cooldown.
- Avoid dynamic lights by default.
- No constantly scrolling noise unless a specific prop/VFX package requires it.

## Unreal Import Notes

- Asset type: Material Instances / texture set.
- Parent material path: `/Game/Aerathea/Materials/Infernals/`
- Material instance path: `/Game/Aerathea/Materials/Instances/`
- Texture path: `/Game/Aerathea/Textures/Infernals/BalgorothCult/`
- Naming convention:
  - `MI_INF_CultStone_Basalt_A01`
  - `MI_INF_CultStone_ScorchedRed_A01`
  - `MI_INF_CultStone_ObsidianInset_A01`
  - `MI_INF_CultStone_BlackIron_A01`
  - `MI_INF_CultStone_BoneHorn_A01`
  - `MI_INF_CultStone_AshCloth_A01`
  - `MI_INF_CultStone_EmissiveChannel_A01`

## Folder And Naming Recommendation

- Package folder: `docs/assets/materials/MI_INF_CultStone_Set_A01/`
- Related kit: `docs/assets/kits/KIT_INF_BalgorothCult_A01/`
- Related symbols: `docs/assets/props/SM_INF_BalgorothSigil_A01/`
- Unreal materials: `/Game/Aerathea/Materials/Infernals/`
- Unreal instances: `/Game/Aerathea/Materials/Instances/`

## Quality Gate Checklist

- Material language matches Infernal/Balgoroth red, black, ash, obsidian, bone, and ember rules.
- Glow is state-driven and restrained.
- Material slots stay MMO-safe.
- Texture targets include Base Color, Normal, ORM, and Emissive where needed.
- Tiny cracks, scratches, ash, and cloth weave stay in textures/normal maps.
- No gore, readable text, copied symbols, full-screen fire, or photoreal noise.
