# SM_GIA_BloodAxeAshPiles_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeAshPiles_A01`
- Asset type: Static Mesh prop production package
- Task: `AET-MA-20260629-441`
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Clutter_AshPiles_LowBanks`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready for planning review; no DCC source, FBX, Unreal Content asset, material graph, VFX, runtime source, validator, startup placement, final approval, terrain blending approval, collision proxy creation, or implementation target is created or approved here.

`SM_GIA_BloodAxeAshPiles_A01` defines low shoveled ash banks and broad camp residue mounds for Blood Axe forge yards, cooking-pit edges, and shelter-adjacent waste zones. The read should be heavy, dirty, and raider-built: black soot cores, pale gray ash edges, rough shovel cuts, and flattened Giant-scale footprints.

The Blood Axe Tribe remains a hostile Giant sub-faction. This package must stay separate from neutral/civilized Giant culture such as hidden cave-town terraces, blue-gray civic masonry, warm communal hearth craft, restrained blue runes, peaceful highland stonework, and organized civic forge language.

## Gameplay Purpose

The asset supports non-interactive environmental storytelling. It gives level artists static ash residue for hostile Blood Axe camps without implying a resource, hazard, VFX, or interaction system.

Allowed planning purpose:

- Static forge and cooking-pit dressing.
- Low camp-edge residue that reinforces Blood Axe soot, waste, and rough field-camp maintenance.
- Scale support around Giant-built hearths and work lanes without merging into hearth, anvil, quench, cooking, path-marker, barricade, or shelter packages.

Out of scope:

- No ash drift VFX, smoke, dust movement, heat shimmer, ember particles, heat damage, burn damage, damage volume, gatherable ash, crafting input, resource node, loot, economy behavior, pickup prompt, interaction marker, terrain blending approval, collision proxy creation, DCC source, Unreal implementation, final visual approval, or implementation target selection.

## Silhouette Notes

Primary silhouette: low, broad ash piles with soft mounded tops, irregular shoveled ridges, darker soot basins, and pale ash lips. The form should stay squat and cheap, never tall enough to compete with forge hearths, Giant logs, slag clumps, or camp barricades.

Required reads:

- Wide flattened footprints that feel shoveled by large Blood Axe hands and tools.
- Soft ash edges with a few broad scallops, not thousands of individual particles.
- Dark interior soot massing that reads from MMO distance.
- Sparse large embedded charcoal fragments or blackened stone only when they help scale.

Avoid treasure-pile silhouettes, glowing coals, active fire language, tidy civic ash bins, circular interactable-resource shapes, readable UI marker shapes, dense pebble noise, or polished neutral/civilized Giant craft.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Suggested size variants:

- Small pile: 180-260 cm wide, 90-160 cm deep, 15-35 cm high.
- Medium pile: 280-420 cm wide, 150-260 cm deep, 25-60 cm high.
- Large pile: 430-600 cm wide, 240-380 cm deep, 40-90 cm high.

The asset should feel too wide and heavy for normal humanoids to treat as casual handheld clutter. Any future review should compare the pile set against both the female 442 cm and male 470 cm Giant baselines before DCC or Unreal work.

## Materials and Color Palette

Primary material language:

- Matte ash, soot black, pale gray forge residue, and crushed charcoal.
- Rare blackened stone or charcoal fragments only as static visual accents.
- No emissive glow, active orange heat, magical fuel, or resource-node color language.

Suggested palette:

- Soot black: `#0B0A09` to `#24201C`
- Dark ash core: `#34312C` to `#5F5B52`
- Ash gray: `#6D685F` to `#9A9386`
- Pale ash edge: `#B5AA98` to `#D0C3AA`
- Charcoal accent: `#151412` to `#30302C`

Keep contrast broad and hand-painted. Do not rely on high-frequency gray noise, excessive speckling, bright fire colors, blue civic rune language, or polished stoneworker material cues.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeAshPiles_A01` for the world of Aerathea. The design should emphasize low broad shoveled ash piles, dark soot cores, pale gray ash lips, sparse large charcoal fragments, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, hostile Blood Axe Giant sub-faction identity, soot black and ash gray color language, rough field-camp waste mood, and a static environment-dressing role with no resource, heat, interaction, terrain blending, or VFX gameplay. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a clean production asset board with three size variants, top-down footprints, side silhouettes, material swatches, LOD notes, and scale callouts. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral/civilized Giant cave-town motifs, avoid gatherable resource UI, avoid ash drift VFX, avoid heat damage diagrams, avoid active flames or smoke, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, implementation target, or final visual approval is created or approved here.

Future modeling guidance:

- Build three reusable pile variants: small, medium, and large.
- Use real geometry for the main mound forms, broad ridges, flattened underside contact, and a few large embedded chunks.
- Keep pile heights low and edges soft, with enough asymmetry to avoid a procedural blob read.
- Shape the base as an irregular static footprint for set dressing, not as terrain blending approval.
- Keep underside and back-side detail minimal.

Use texture and normal detail for ash dust, fine soot, small cracks, powdery falloff, tiny charcoal pores, and subtle shovel streaks. Do not model individual ash grains, dense small pebbles, micro charcoal fragments, or fine dust trails.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, terrain blend, decal setup, or Unreal import is authored by this package.

Material slot plan:

- Slot 0: planned ash/soot/charcoal material.

Texture naming examples:

- `T_GIA_BloodAxeAshPiles_A01_BC`
- `T_GIA_BloodAxeAshPiles_A01_N`
- `T_GIA_BloodAxeAshPiles_A01_ORM`
- `MI_GIA_BloodAxeAshPiles_A01`

Texture resolution target: 512 to 1K. A 2K set is only reasonable if a later review combines all pile variants into one reusable atlas; 4K is not planned.

Packed `ORM` guidance:

- R: strong contact occlusion under mound edges, embedded chunks, and dark soot interiors.
- G: high roughness across ash, soot, and charcoal; no wet or shiny read.
- B: metallic stays black unless rare metal fragments are approved by a separate package.

## Triangle Budget

Target LOD0 ranges:

- Small pile: 500-900 tris.
- Medium pile: 900-1.6k tris.
- Large pile: 1.4k-2.8k tris.
- Combined reusable pile set target: 2k-4k tris if packaged as one mesh with variants.

Target material slots: 1.

Spend geometry on the readable mound profile, broad shovel ridges, and large embedded chunks. Do not spend geometry on ash grains, soot speckles, small chips, fine cracks, or dense debris.

## LOD Plan

All important variants require LOD0-LOD3.

- LOD0: full mound silhouette, broad ridges, embedded chunks, dark soot core zones, and pale ash edge forms.
- LOD1: 60-70 percent of LOD0; reduce secondary ridges, small bevels, minor embedded chunks, and non-silhouette edge waves.
- LOD2: 35-45 percent of LOD0; merge mound interiors, simplify base outline, remove most embedded chunks, and keep only major light/dark material regions.
- LOD3: 15-25 percent of LOD0; preserve the low ash-pile footprint, squat height, soot-core read, and pale-edge read.

Reduction order:

1. Tiny ash flecks, soot speckles, and small cracks.
2. Minor embedded chunks and small edge scallops.
3. Secondary ridges and inner mound subdivisions.
4. Back-side and underside detail.
5. Main mound footprint only after all small detail is removed.

Never reduce the low broad silhouette before removing small detail.

## Collision Notes

Collision guidance is display-only planning. This package does not create or approve collision proxies.

Recommended future collision:

- Collision disabled by default for small and medium ash piles.
- Optional one shallow low-count hull or simple box around the large pile footprint only if a later implementation task requires blocking.
- Walkable collision disabled by default.

Do not add gatherable collision, resource triggers, interaction volumes, heat damage volumes, burn hazards, VFX collision, terrain-blend collision, per-chunk collision, navmesh rules, cover volumes, physics simulation, or collision proxy assets from this package.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Fixed ash mound silhouettes.
- Painted soot, ash, and charcoal variation as visual material language only.
- No runtime motion claim.

Not approved:

- Ash drift VFX, smoke, dust puffs, embers, sparks, heat shimmer, active flames, animated material states, emissive maps, bloom, audio cues, physics movement, interaction behavior, heat damage, burn damage, gatherable behavior, Blueprint state, or startup-scene behavior.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, import script, material instance, texture, Blueprint, Niagara system, validator, startup actor, runtime source, final approval, or implementation target is created or approved by this package.

Planned future asset type:

- Static Mesh prop.

Planned future folder:

- `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/Ash/`

Planned future import rules:

- Import at scale 1.0 from centimeter-authored source.
- Pivot at ground center of the full pile footprint.
- Assign LOD0, LOD1, LOD2, and LOD3.
- Use 1 material slot.
- Sockets: none.
- Blueprint behavior: none.
- Animation list: none.
- Performance note: preserve the low ash footprint and remove fine ash/soot detail before primary silhouette simplification.

## Folder and Naming Recommendation

Docs path:

- `docs/assets/props/SM_GIA_BloodAxeAshPiles_A01/PRODUCTION_PACKAGE.md`

Future naming, pending separate approval:

- Static Mesh: `SM_GIA_BloodAxeAshPiles_A01`
- Material Instance: `MI_GIA_BloodAxeAshPiles_A01`
- Textures: `T_GIA_BloodAxeAshPiles_A01_BC`, `T_GIA_BloodAxeAshPiles_A01_N`, `T_GIA_BloodAxeAshPiles_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concept folders, global indexes, task-board files, backlog files, bootstrap files, or any package outside this owned docs path from this task.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Validated Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5".
- Ash piles are static residue only, not ash drift VFX, heat damage, burn damage, gatherable resource, terrain blending approval, collision proxy creation, DCC source, Unreal implementation, final approval, or implementation target.
- Primary silhouette is low, broad, readable, and MMO-safe.
- Materials use soot black, ash gray, pale ash edge, and matte charcoal accents consistently.
- No emissive glow, active fire, smoke, particle VFX, resource-node color, UI marker, or neutral/civilized Giant civic language is included.
- Tiny ash flecks, soot speckles, fine cracks, and charcoal pores are assigned to textures or normals instead of geometry.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision guidance, animation limits, Unreal import planning, folder/naming recommendation, and stop gates are included.
