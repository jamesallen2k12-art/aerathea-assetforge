# KIT_INF_BalgorothCult_A01 Visual Kit Breakdown

## Art Direction Summary

`KIT_INF_BalgorothCult_A01` is the production breakdown for Infernal cult symbols, ritual props, trial spaces, material states, and VFX language. The kit supports adult Infernals, Lesser Infernal lifecycle scenes, class VFX, cult dens, proving arenas, and Balgoroth worship sites.

Balgoroth worship should feel severe, predatory, hierarchical, and judgmental. It should communicate sacrifice, worthiness, culling temper, and chosen bloodline status without depending on gore.

## Gameplay Purpose

The kit provides modular pieces and shared materials for:

- Infernal proving arenas and bloodline trials.
- Lesser Infernal Spawn, 1st Kill, and Blooded training spaces.
- Elder and Ancient ritual authority scenes.
- Mage, rogue, hunter, and warrior class VFX callouts.
- Cult settlement interiors, dens, altar rooms, banners, trial floors, and encounter dressing.

## Source Concept Routing

The 2026-06-27 Infernal source addendum adds practical references for cult scene dressing, lit brand material states, gate defense silhouettes, and Lesser trial population. These files should inform kit children without overriding the approved symbol language.

| Source group | Routed use |
| --- | --- |
| `InfernalFemaleLit*.png`, `InfernalMaleLit.png`, `InfernalMaleSorcererLit.png` | `MI_INF_BrandGlowStates_A01`, restrained emissive masks, ritual-active body/material states |
| `Infernals Guarding a Gate*.png` | `SM_INF_HornWingArch_A01`, cult gate stance, guard spacing, and encounter threshold dressing |
| `InfernalClutch.png`, `Infernal Children.png` | Trial den layout, Spawn-scale props, low viewing angles, culling trial staging |
| `Infernals.png` | Group hierarchy, leader/readiness poses, cult settlement population density |

## Symbol Language

| Symbol | Shape rule | Use |
| --- | --- | --- |
| Horned crown | three to five horn points, center taller | Balgoroth authority, leaders, altars |
| Split wing | two severe wing blades divided by a central mark | transformation, chosen bloodline, wing rites |
| Hooked tail crescent | crescent ending in a claw/tail hook | hunt, pursuit, rogue/hunter marks |
| Claw slash | three black cuts or raised grooves | culling temper, trial success, arena scoring |
| Ember eye | angular eye with small ember core | invisible sight, judgment, watcher positions |
| Broken circle | incomplete ritual ring | rejected/unworthy sacrifice, witness punishment |

Symbols must be graphic and readable at MMO camera distance. Do not rely on readable text glyphs.

## Child Asset Breakdown

| Child asset | Type | Purpose | Status |
| --- | --- | --- | --- |
| `SM_INF_BalgorothSigil_A01` | Static Mesh | large wall/floor horned crown sigil | Package needed |
| `SM_INF_CullingTrialFloor_A01` | Static Mesh modular floor | circular proving floor with claw channels | DCC/Unreal first-pass visual review accepted; final art and VFX states pending |
| `SM_INF_HornWingArch_A01` | Static Mesh | tall arch scaled for 9' Infernals with folded wings | Production package and modeling handoff ready; DCC build not started |
| `SM_INF_WorthinessAltar_A01` | Static Mesh or Blueprint | altar/platform for sacrifice judgment states | Package needed |
| `SM_INF_AshBasin_A01` | Static Mesh/VFX hook | ash, ember, and regeneration ritual prop | Package needed |
| `SM_INF_WitnessChains_A01` | Static Mesh | non-blocking witness/restraint dressing | Package needed |
| `SM_INF_TrialBanner_A01` | Static Mesh/Skeletal optional | hanging black-red cult banner | Package needed |
| `SM_INF_BrandingStone_A01` | Static Mesh | body-brand source prop and VFX anchor | Package needed |
| `MI_INF_CultStone_Set_A01` | Material set | basalt, ash stone, scorched red stone | Package needed |
| `MI_INF_BrandGlowStates_A01` | Material set | inactive, smolder, active, rejected states | Production package ready |
| `VFX_INF_RegenerationBrand_A01` | VFX | restrained body/brand regen pulse | Package needed |
| `VFX_INF_WorthinessJudgment_A01` | VFX | altar active/rejected/accepted pulse | Production package ready |
| `BP_INF_RitualAltar_A01` | Blueprint Actor | altar state machine and VFX/audio hooks | Blocked until mesh/material set exists |

## Scale Notes

- Doorways and arches must clear a 274 cm adult plus horns and folded wings.
- Trial floors need space for tail sweeps, wing flares, and 5-stage Lesser lineup reviews.
- Spawn-scale props should sit low enough for 70-90 cm characters but not make rooms feel toy-sized.
- Elder and Ancient authority props should have raised platforms but avoid unreachable interaction points.

## Materials And Color Palette

| Material | Color | Use |
| --- | --- | --- |
| Basalt cult stone | black, blue-black, ash-gray edge wear | floors, walls, altar bases |
| Scorched red stone | dark red, burnt umber, warm cracks | trial channels, ritual insets |
| Blackened iron | charcoal metal, dark bronze wear | chains, braces, frames |
| Obsidian | near-black with sharp gray highlights | sigil insets, altar cores |
| Bone and horn | aged ivory, smoke-stained tan | ornaments, witness beads, rite markers |
| Ash cloth/leather | black, ash gray, blood-dark red | banners, wraps, portable cult items |
| Emissive brands | ember orange, deep red, restrained violet | active marks, altar cores, eye symbols |

## Concept Image Prompt

Create an original stylized fantasy MMORPG visual kit board for the Balgoroth cult of the Infernals in Aerathea. The design should emphasize horned crown symbols, split wing marks, hooked tail crescents, claw-slash scoring, ember eye judgment motifs, black basalt, ash-gray stone, scorched red stone, blackened iron, obsidian, bone ornaments, ash cloth banners, proving arenas, culling trial floors, worthiness altars, witness chains, branding stones, restrained ember and violet abyssal glow, and modular MMO-friendly construction. Present it as a clean production kit board with symbol callouts, material swatches, altar, arch, trial floor, banner, ash basin, VFX state callouts, and scale beside a 180 cm humanoid and 274 cm Infernal. Avoid copied franchise designs, gore, excessive particles, readable text, watermarks, and photoreal micro-detail.

## Modeling Notes

- Model real geometry for large symbols, arch silhouettes, altar masses, floor slabs, chains, basins, banner rods, and major stone breaks.
- Use texture/normal maps for fine cracks, ash smears, tiny brands, scratches, cloth weave, and heat stress lines.
- Build trial floors as snap-friendly modular wedges, center discs, edge rings, and channel inserts.
- Keep altar collision simple and interaction-facing.
- Chains are mostly non-blocking dressing unless a specific gameplay restraint needs collision.

## Texture And Material Notes

Shared texture/material targets:

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
- `T_INF_BrandGlow_A01_E`

Material states:

- Inactive: almost no emissive, readable stone/metal forms.
- Smoldering: low ember glow in channels and brands.
- Trial active: stronger but still localized red-orange channel glow.
- Accepted: warm focused ember at sigil core.
- Rejected: short violet-red pulse and broken-circle mark.

## Triangle Budget

- Small props: 500-4k tris.
- Banners/chains/basins: 1k-6k tris.
- Altar and arch pieces: 4k-12k tris.
- Trial floor module set: 8k-18k tris per assembled review cluster.
- Hero ritual room cluster: 18k-30k tris before dressing props.

## LOD Plan

- LOD0: full symbol silhouette, altar/arch form, major cracks, chains, banner shapes.
- LOD1: 55-60 percent; reduce small chain links, secondary bevels, tiny stone chips.
- LOD2: 25-35 percent; simplify symbol bevels, remove small ornaments, flatten minor breaks.
- LOD3: 10-15 percent; preserve horn/wing/claw symbol, altar mass, floor ring, and glow blocks.

## Collision Notes

- Trial floors use flat simple collision.
- Altars and arches use simple blocking volumes.
- Chains, banners, small ornaments, and ash props are non-blocking by default.
- Ensure winged/tail characters do not snag on low arches, raised trim, or channel geometry.

## Animation And VFX Notes

- Brand pulse should be low frequency and localized.
- Altar states: inactive, smolder, trial active, accepted, rejected.
- Ash basin VFX: restrained smoke/ember, no constant heavy particles.
- Witness-chain sway is optional and should not become a performance cost.
- VFX color must stay consistent with Infernal emissive rules: ember, deep red, and restrained violet.

## Unreal Import Notes

- Root folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/`
- Materials: `/Game/Aerathea/Materials/Infernals/`
- VFX: `/Game/Aerathea/VFX/Infernals/`
- Blueprints: `/Game/Aerathea/Blueprints/Infernals/`
- Pivots: floor modules at center-bottom, arches at ground center, altars at interaction-facing center, banners at hanging point if animated.
- Collision: simple collision authored or generated per child.
- First DCC candidate: `SM_INF_CullingTrialFloor_A01`, because it validates symbols, material channels, scale, collision, and future ritual props in one controlled module.

## Folder And Naming Recommendation

- Kit package: `docs/assets/kits/KIT_INF_BalgorothCult_A01/`
- Visual breakdown: `docs/assets/kits/KIT_INF_BalgorothCult_A01/VISUAL_KIT_BREAKDOWN.md`
- Source: `SourceAssets/Blender/Kits/Infernals/BalgorothCult/`
- Export: `SourceAssets/Exports/Kits/Infernals/BalgorothCult/`
- Unreal: `/Game/Aerathea/Props/Infernals/BalgorothCult/`

## Quality Gate Checklist

- Symbols are original to Aerathea and readable without text.
- Culling temper, worthiness judgment, and Balgoroth hierarchy are visible without gore.
- Props support Spawn through 9' adult Infernal scale.
- Materials use red, black, ash, obsidian, bone, and restrained ember/violet glow.
- LOD, collision, texture maps, Unreal paths, pivots, and performance budgets are defined.
- Child assets are split clearly enough for follow-up production packages.
