# SM_GIA_BloodAxeSlagSpillStrips_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeSlagSpillStrips_A01`
- Asset type: Static Mesh prop production package
- Task: `AET-MA-20260629-442`
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Clutter_SlagLumps_SpillStrips`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready for planning review; no DCC source, FBX, Unreal Content asset, material graph, VFX, runtime source, validator, startup placement, final approval, ore/resource/salvage/economy behavior, heat damage, or implementation target is created or approved here.

`SM_GIA_BloodAxeSlagSpillStrips_A01` defines low elongated cooled slag spill strips for the edges near Blood Axe forge hearths, anvil/quench props, and rough work lanes. The asset should read as inert, cooled, matte residue that settled into crusted strips, not as hot molten flow.

The Blood Axe Tribe remains a hostile Giant sub-faction. This package uses dirty raider forge waste language and must remain separate from neutral/civilized Giant culture such as hidden cave-town terraces, blue-gray civic masonry, warm communal hearths, restrained blue runes, peaceful highland stonework, and refined civic forge discipline.

## Gameplay Purpose

The asset supports non-interactive environmental storytelling along Blood Axe forge boundaries. It gives artists low strip-shaped slag residue that can break up ground lines without implying heat, ore, salvage, or economy systems.

Allowed planning purpose:

- Static cooled strip residue beside forge hearth, anvil/quench, scrap lanes, and ash banks.
- Elongated footprints that guide the eye through rough Giant-scale work lanes without becoming path markers.
- Visual contrast against ash drifts and slag clump clusters while preserving sibling package boundaries.

Out of scope:

- No ore node, metal resource, salvage object, crafting input, economy item, loot, harvest behavior, pickup prompt, interaction marker, heat damage, burn damage, hot-surface gameplay, VFX, smoke, sparks, heat shimmer, emissive map, material graph authoring, DCC source, Unreal implementation, final visual approval, or implementation target selection.

## Silhouette Notes

Primary silhouette: low elongated cooled slag strips with irregular crusted edges, shallow raised ridges, broken matte clumps along the line, and heavy contact shadows under larger lumps.

Required reads:

- Long static spill-strip footprints that are clearly cooled and matte.
- Uneven widths and broken ends, like rough field-forge waste hardened in place.
- A few chunky raised islands for readability, with most micro crust detail handled in texture.
- Strong separation from active molten flow, ore veins, resource trails, and path marker props.

Avoid glowing lava-like ribbons, shiny ore veins, collectible salvage trails, sorted scrap rows, active forge VFX, tidy civic forge channels, resource-node outlines, or dense micro-crust geometry.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Suggested size variants:

- Short strip: 180-320 cm long, 35-90 cm wide, 8-28 cm high.
- Medium strip: 320-560 cm long, 50-130 cm wide, 12-45 cm high.
- Long strip: 560-850 cm long, 70-170 cm wide, 18-70 cm high.
- Raised islands: 35-120 cm across, used sparingly along the strip.

The asset should feel like hardened Giant-scale forge residue, not humanoid ore or salvage pickups. Any future review should compare the strip set against both the female 442 cm and male 470 cm Giant baselines before DCC or Unreal work.

## Materials and Color Palette

Primary material language:

- Matte cooled slag, dark crust, dull iron gray, oxidized brown cracks, and ash-dusted edges.
- High roughness with no active heat, no molten glow, and no emissive map for baseline `A01`.
- Broader value shapes than `SM_GIA_BloodAxeAshDrifts_A01`, with chunkier dark masses.

Suggested palette:

- Slag black: `#10100F` to `#272522`
- Cooled crust gray: `#2E3030` to `#545957`
- Oxide brown crack: `#3F281D` to `#6D432B`
- Ash-dusted edge: `#746D61` to `#A69A86`
- Deep strip crease: `#050505` to `#151412`

Avoid molten orange, bright resource colors, gold ore reads, magical blue runes, polished civic forge channels, or shiny wet material language.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeSlagSpillStrips_A01` for the world of Aerathea. The design should emphasize low elongated cooled slag spill strips, irregular crusted edges, shallow raised ridges, matte broken clumps, ash-dusted contact zones, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, hostile Blood Axe Giant sub-faction identity, dark cooled waste color language, brutal field-forge mood, and a static environment-dressing role with no ore, resource, salvage, economy, heat damage, VFX, material graph, interaction, or implementation behavior. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a clean production asset board with short, medium, and long strip variants, top-down footprints, low side profiles, material swatches, LOD notes, and scale callouts. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral/civilized Giant cave-town motifs, avoid resource UI or pickup outlines, avoid molten flow language, avoid active forge VFX, avoid economy diagrams, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, implementation target, ore/resource behavior, salvage behavior, economy behavior, or final visual approval is created or approved here.

Future modeling guidance:

- Build three strip variants: short, medium, and long.
- Use real geometry for the main strip footprint, broad crusted ridges, large raised islands, and broken strip ends.
- Keep most height low so the asset reads as ground residue, not a wall or barricade.
- Break the silhouette with wide irregular edges rather than tiny sawtooth detail.
- Keep the form separate from `SM_GIA_BloodAxeAnvilQuench_A01`; do not include quench trough, tray, rack, tools, or workstation hardware.

Use texture and normal detail for tiny crust pores, hairline cracks, cooled bubbles, ash dust, oxide staining, and small chips. Do not model dense pore fields, micro flakes, hot cracks, or many tiny fragments.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, hot-state material, or Unreal import is authored by this package.

Material slot plan:

- Slot 0: planned cooled slag strip material for dark crust, dull gray planes, ash dust, and oxidized crack tones.

Texture naming examples:

- `T_GIA_BloodAxeSlagSpillStrips_A01_BC`
- `T_GIA_BloodAxeSlagSpillStrips_A01_N`
- `T_GIA_BloodAxeSlagSpillStrips_A01_ORM`
- `MI_GIA_BloodAxeSlagSpillStrips_A01`

Texture resolution target: 512 to 1K for individual strips; 2K only if later approved for a combined slag atlas. 4K is not planned.

Packed `ORM` guidance:

- R: strong occlusion under raised islands, broad crust ridges, and broken strip edges.
- G: high roughness for cooled crust and ash; slightly lower roughness only on rare broad worn metal-like planes.
- B: low metallic overall; use restrained metallic only for rare cooled metal inclusions if approved by later material work.

## Triangle Budget

Target LOD0 ranges:

- Short strip: 500-1k tris.
- Medium strip: 900-1.8k tris.
- Long strip: 1.4k-3k tris.
- Combined reusable strip set target: 2.5k-5k tris if packaged as one mesh with variants.

Target material slots: 1.

Spend geometry on long footprint shape, broad crusted ridges, raised islands, and broken ends. Do not spend geometry on tiny pores, micro flakes, ash speckles, hairline cracks, or dense edge chips.

## LOD Plan

All important variants require LOD0-LOD3.

- LOD0: full strip footprints, irregular edges, raised islands, broad crust ridges, and ash-dusted contact zones.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor edge cuts, secondary islands, and non-silhouette cracks.
- LOD2: 35-45 percent of LOD0; merge minor raised islands, simplify strip ends, reduce internal ridges, and keep only major value zones.
- LOD3: 15-25 percent of LOD0; preserve elongated cooled spill-strip read, broad dark mass, and broken-end rhythm.

Reduction order:

1. Tiny pores, ash speckles, and hairline cracks.
2. Small edge chips and minor bevels.
3. Secondary raised islands and underside detail.
4. Internal ridge subdivisions.
5. Primary elongated footprint only after all small detail is removed.

Never reduce the long static strip identity before removing small detail.

## Collision Notes

Collision guidance is display-only planning. This package does not create or approve collision proxies.

Recommended future collision:

- Collision disabled by default for low decorative strips.
- Optional one simple low hull or box along a long strip footprint only if a later implementation task requires display blocking.
- No per-island or per-fragment collision.
- Walkable collision disabled by default.

Do not add resource triggers, salvage triggers, harvest volumes, pickup collision, interaction volumes, heat damage volumes, burn hazards, VFX collision, path-marker logic, navmesh rules, cover volumes, physics simulation, or collision proxy assets from this package.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Fixed cooled slag strip silhouettes.
- Painted cooled crust, ash dust, and oxide variation as visual material language only.
- No runtime motion claim.

Not approved:

- Heat shimmer, sparks, smoke, embers, molten flow, animated material states, emissive maps, bloom, audio cues, physics movement, destructible chunks, ore/resource behavior, salvage behavior, economy behavior, interaction behavior, heat damage, burn damage, Blueprint state, VFX, or startup-scene behavior.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, import script, material instance, texture, Blueprint, Niagara system, validator, startup actor, runtime source, material graph, final approval, ore/resource system, salvage system, economy object, or implementation target is created or approved by this package.

Planned future asset type:

- Static Mesh prop.

Planned future folder:

- `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/Slag/`

Planned future import rules:

- Import at scale 1.0 from centimeter-authored source.
- Pivot at ground center of each strip footprint, with the long axis aligned for grid placement.
- Assign LOD0, LOD1, LOD2, and LOD3.
- Use 1 material slot.
- Sockets: none.
- Blueprint behavior: none.
- Animation list: none.
- Performance note: preserve elongated cooled strip read and remove pore/chip detail before primary footprint simplification.

## Folder and Naming Recommendation

Docs path:

- `docs/assets/props/SM_GIA_BloodAxeSlagSpillStrips_A01/PRODUCTION_PACKAGE.md`

Future naming, pending separate approval:

- Static Mesh: `SM_GIA_BloodAxeSlagSpillStrips_A01`
- Material Instance: `MI_GIA_BloodAxeSlagSpillStrips_A01`
- Textures: `T_GIA_BloodAxeSlagSpillStrips_A01_BC`, `T_GIA_BloodAxeSlagSpillStrips_A01_N`, `T_GIA_BloodAxeSlagSpillStrips_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concept folders, global indexes, task-board files, backlog files, bootstrap files, or any package outside this owned docs path from this task.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Validated Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5".
- Slag spill strips are cooled static residue only, not ore, resource, salvage, economy object, heat damage source, VFX asset, material graph task, DCC source, Unreal implementation, final approval, or implementation target.
- Primary silhouette is elongated, matte, cooled, readable, and MMO-safe.
- Materials use cooled slag black, dull iron gray, oxidized brown cracks, ash-dusted edges, and high roughness consistently.
- No emissive glow, molten heat, sparks, smoke, resource-node color, UI marker, shiny ore read, path-marker behavior, or neutral/civilized Giant civic language is included.
- Tiny pores, ash speckles, hairline cracks, and small chips are assigned to textures or normals instead of geometry.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision guidance, animation limits, Unreal import planning, folder/naming recommendation, and stop gates are included.
