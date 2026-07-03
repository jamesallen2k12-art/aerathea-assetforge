# SM_GIA_BloodAxeScorchedDebris_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeScorchedDebris_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Clutter_ScorchedDebris_BurntBeams`
- Task: `AET-MA-20260629-445`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: package-ready planning document; no DCC, Unreal Content, startup placement, final visual approval, or implementation target is authorized

`SM_GIA_BloodAxeScorchedDebris_A01` defines a non-graphic row of burned beams, snapped stakes, broken planks, ash-stained stones, and rare bent metal scraps for hostile Blood Axe camp-edge dressing. The asset should read as inert battlefield and forge-yard residue, not as a destructible barricade, cover object, loot pile, resource node, heat hazard, or nav/collision behavior asset.

Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture. Use crude raider-camp language: scorched timber, black ash, matte soot, dull stone, blackened stolen metal, scorched hide ties, and restrained oxide red cloth. Do not use neutral Giant cave-town masonry, refined blue-gray stoneworker craft, peaceful highland markers, warm civic hearth identity, or restrained blue rune culture as the baseline.

## Gameplay Purpose

The purpose is static environmental storytelling for burned Blood Axe camp edges, forge perimeters, and ruined work lanes. It visually supports the history of a harsh hostile Giant encampment without adding gameplay affordances.

Allowed planning use:

- Dress the edge of Blood Axe forge, shelter, or work-lane spaces with non-interactive burned debris.
- Break up broad ash and packed-earth surfaces with a few large, readable charred forms.
- Reinforce Blood Axe hostility through crude scorch marks and restrained red identifiers.
- Stay separate from path markers, barricades, forge hearths, anvil/quench stations, scrap sorting, and cooking pit ownership.

Out of scope: destructible behavior, cover rules, loot behavior, resource behavior, salvage behavior, heat or damage behavior, nav behavior, collision gameplay behavior, interaction prompts, pickup affordances, crafting/economy systems, VFX, audio, DCC source, FBX export, Unreal Content, runtime source, validators, startup placement, final approval, or implementation target selection.

## Silhouette Notes

The primary read is a low-to-medium debris strip made from a few large burned beams, snapped stakes, collapsed plank sections, ash-stained stones, and rare bent plate scraps. The silhouette should be broken and irregular, but not dense enough to become a wall, barricade, obstacle, or cover affordance.

Key silhouette targets:

- Broad charred beams with blunt broken ends.
- Two or three snapped upright stakes at most, kept sparse.
- Low collapsed planks and log ends crossing at shallow angles.
- Ash-stained stones and dull metal scraps used as secondary accents.
- Restrained red cloth tags or scorched hide ties, never a route marker or UI signal.

Model real geometry for large beams, broken plank slabs, major stake silhouettes, large stone chunks, bent plate scraps, and cloth tags. Use texture and normal detail for soot speckles, wood grain, hairline scorch marks, small cracks, tiny nails, pitting, and ash dust.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Planning dimensions:

- Standard debris row: 350-900 cm long, 110-280 cm deep, 45-180 cm high.
- Compact variant: 220-420 cm long, 80-180 cm deep, 30-110 cm high.
- Large burned beams: 220-680 cm long, 35-90 cm thick.
- Snapped stakes: 120-260 cm tall, used sparingly.
- Stone chunks: 60-180 cm across, kept secondary to charred timber.

These dimensions are visual planning values only. They are not cover extents, traversal blockers, nav requirements, collision correctness claims, damage radii, or placement approvals.

## Materials and Color Palette

Primary materials:

- Charred timber, scorched bark, split raw wood, matte ash, soot, dull camp stone, blackened iron scraps, scorched hide ties, and restrained Blood Axe red cloth.
- No default emissive, active flame, glowing coal, molten metal, smoke, heat shimmer, or magic accent.

Palette targets:

- Soot black: `#0B0A09`, `#171412`, `#24201C`
- Charred bark: `#1D130F`, `#2C1C16`, `#3C261B`
- Split raw wood: `#6A4930`, `#815735`, `#A36C3A`
- Ash gray: `#5F5B52`, `#80796C`, `#9A9386`
- Burned stone: `#2E2D2A`, `#47443E`, `#615A50`
- Blackened metal: `#141414`, `#252525`, `#3A352F`
- Blood Axe red accent: `#5F1513`, `#7A1C17`, `#8B211B`

Keep roughness high and values matte. Avoid shiny ore reads, treasure metal, bright red flags, neutral/civilized Giant blue-gray stone, warm civic hearth color, and polished craft finishes.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeScorchedDebris_A01` for the world of Aerathea. The design should emphasize hostile Blood Axe Giant camp-edge dressing, burned beams, snapped stakes, collapsed planks, ash-stained stones, rare bent blackened metal scraps, restrained oxide red cloth tags, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", crude raider-camp culture, and a static non-interactive environmental storytelling role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh prop production sheet with front, side, top footprint, scale callouts, material swatches, LOD notes, and simple display collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid destructible behavior reads, avoid cover affordances, avoid loot/resource cues, avoid heat or damage hazard language, avoid nav or collision gameplay reads, avoid DCC or Unreal approval claims, avoid startup placement, avoid final visual approval, and avoid excessive micro-detail.

## Modeling Notes

This is a docs-only modeling plan. It creates no DCC source, mesh, sculpt, retopo, UVs, bake, collision proxy, FBX, Unreal Content, material instance, Blueprint, validator, startup actor, source concept movement, final visual approval, or implementation target.

Future modeling priorities after separate approval:

- Build the prop as a few large readable debris forms with strong negative space.
- Keep the row low enough to read as dressing rather than a barricade or cover object.
- Use varied beam lengths and broken-end angles while preserving a clean footprint.
- Keep metal scraps rare and clearly secondary to the burned timber read.
- Use red cloth tags as subtle Blood Axe identifiers only, not path markers.
- Avoid dense tiny splinters, gore, readable signage, route arrows, UI-like shapes, interaction rings, or pickup handles.

Suggested future mesh groups:

- `ScorchedDebris_CharredBeams`
- `ScorchedDebris_BrokenPlanks`
- `ScorchedDebris_SparseStakes`
- `ScorchedDebris_AshStoneAccents`
- `ScorchedDebris_OptionalMetalCloth`

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

Future texture names if separately approved:

- `T_GIA_BloodAxeScorchedDebris_A01_BC`
- `T_GIA_BloodAxeScorchedDebris_A01_N`
- `T_GIA_BloodAxeScorchedDebris_A01_ORM`

Material slot plan:

- Slot 0: scorched wood, ash, soot, and burned plank surfaces.
- Slot 1: dull stone, rare blackened metal, and restrained red cloth if these cannot be cleanly atlased into Slot 0.
- No emissive map is planned for baseline `A01`.

Target texture resolution: 1K by default, 2K maximum if the row needs broad unique beam and ash variation. Use textures and normals for soot, bark grain, tiny cracks, nail marks, pitting, ash flecks, and small scorch marks rather than modeled micro-detail.

## Triangle Budget

Target LOD0: 2k-8k tris.

Suggested breakdown:

- Compact row: 2k-4k tris.
- Standard row: 4k-6k tris.
- Dense but still readable row: 6k-8k tris.

Target material slots: 1-2. Spend geometry on the large beam silhouettes, snapped stake profiles, broad plank breaks, stone massing, and rare bent metal scraps. Do not spend geometry on tiny splinters, ash grains, soot flecks, nail heads, wood pores, hairline cracks, or dense pebble scatter.

## LOD Plan

All future static mesh implementation requires LOD0, LOD1, LOD2, and LOD3 before shipping use.

- LOD0: full burned beam row, snapped stakes, broad planks, stone accents, rare metal scraps, cloth tags, and ash-dark footprint.
- LOD1: 60-70 percent of LOD0; reduce bevels, minor plank chips, secondary stake cuts, metal edge subdivisions, and backside detail.
- LOD2: 35-45 percent of LOD0; merge small planks, simplify stakes, reduce stone chunks, flatten underside detail, and remove non-silhouette scraps.
- LOD3: 15-25 percent of LOD0; preserve the broad scorched debris footprint, beam rhythm, a few vertical breaks, and restrained Blood Axe accent only.

Reduction order:

1. Soot speckles, ash flecks, bark hairlines, tiny chips, nail marks, and fine pitting.
2. Small splinters, cloth edge nicks, minor metal tabs, and non-silhouette plank cuts.
3. Secondary stones, backside beams, underside faces, and hidden overlaps.
4. Stake subdivisions, plank bevels, and beam-end notches.
5. Main beam lengths, broken row footprint, and Giant-scale silhouette only after all smaller detail is removed.

## Collision Notes

This package creates no collision asset, collision proxy, Unreal collision setting, nav blocker, cover volume, damage volume, trigger volume, destructible fracture setup, validator, or collision correctness claim.

Future display collision guidance after separate approval:

- Collision disabled by default for purely decorative camp-edge placement.
- Optional simple display collision may use one to three low-count boxes or convex hulls around the broad debris mass if a later review task needs editor selection/display bounds.
- No per-plank, per-splinter, per-stake, per-stone, per-nail, per-cloth, or per-metal-scrap collision.
- No nav/pathfinding rules, cover rules, damage triggers, pickup volumes, loot outlines, resource triggers, heat hazard volumes, destructible collision, or gameplay collision behavior.

## Animation Notes

Baseline asset is static.

Not included: destruction, physics-simulated collapse, loose plank motion, cloth simulation, wind motion, smoke, sparks, flame, embers, heat shimmer, material pulse, glow state, audio, interaction state, pickup state, resource state, loot state, cover state, nav state, encounter behavior, startup behavior, DCC work, Unreal work, final approval, or implementation target.

Any moving, burning, smoking, damaging, destructible, interactive, pickup-readable, or gameplay-readable variant must be split into a separately approved package.

## Unreal Import Notes

This section is planning only because the universal package format requires import notes. No Unreal Content asset, import script, material instance, texture asset, Blueprint, validator, startup actor, runtime source, DCC file, FBX export, final visual approval, or implementation target is created or authorized.

Potential future import identity after separate approval:

- Asset name: `SM_GIA_BloodAxeScorchedDebris_A01`
- Asset type: Static Mesh prop
- Candidate future folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/`
- Pivot: ground center of the broad debris footprint.
- Scale: centimeter-authored source, import scale 1.0.
- Collision: disabled by default; simple display hulls only if separately approved.
- LODs: LOD0-LOD3 required.
- Material slots: 1-2 target.
- Texture list: BC, N, ORM only by default.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.

No destructible actor, cover system, resource node, loot component, heat damage, nav behavior, interaction prompt, VFX component, material graph, startup placement, or final signoff is authorized.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeScorchedDebris_A01/PRODUCTION_PACKAGE.md`

Potential future naming after separate approval:

- Mesh: `SM_GIA_BloodAxeScorchedDebris_A01`
- Textures: `T_GIA_BloodAxeScorchedDebris_A01_BC`, `T_GIA_BloodAxeScorchedDebris_A01_N`, `T_GIA_BloodAxeScorchedDebris_A01_ORM`
- Material instance: `MI_GIA_BloodAxeScorchedDebris_A01`

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, global index edits, task board edits, material graphs, VFX, startup scene files, or sibling package changes from this package.

## Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Defines static camp-edge dressing only, not a destructible object, cover object, loot pile, resource node, heat hazard, damage volume, path marker, barricade, or nav/collision behavior asset.
- Keeps forge hearth, anvil/quench, scrap sorting, cooking pit, path marker, barricade, and shelter ownership separate.
- Uses mid-poly MMO budgets, LOD0-LOD3, texture map planning, simple display collision guidance, and Unreal planning notes without implementation claims.
- Assigns tiny soot, ash, bark, pitting, nails, scratches, and cracks to textures or normals rather than geometry.
- Makes no DCC, FBX, Unreal Content, runtime source, material graph, VFX, validator, startup placement, final approval, first DCC target, source concept movement, global index edit, or task board edit claim.
