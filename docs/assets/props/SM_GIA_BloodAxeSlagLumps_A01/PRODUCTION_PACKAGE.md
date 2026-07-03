# SM_GIA_BloodAxeSlagLumps_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeSlagLumps_A01`
- Asset type: Static Mesh prop production package
- Task: `AET-MA-20260629-442`
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Clutter_SlagLumps_CooledClumps`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready for planning review; no DCC source, FBX, Unreal Content asset, material graph, VFX, runtime source, validator, startup placement, final approval, ore/resource/salvage/economy behavior, heat damage, or implementation target is created or approved here.

`SM_GIA_BloodAxeSlagLumps_A01` defines cooled black-gray slag clumps and rough static spill clusters for Blood Axe forge yards. The asset should read as matte waste from brutal field forging: heavy, crusted, discarded, and inert.

The Blood Axe Tribe remains a hostile Giant sub-faction. This package must stay separate from neutral/civilized Giant culture such as hidden cave-town terraces, blue-gray civic masonry, warm communal hearth craft, restrained blue runes, peaceful highland stonework, and refined civic forge discipline.

## Gameplay Purpose

The asset supports non-interactive environmental storytelling near Blood Axe forge hearths, quench areas, and rough scrap lanes. It adds cooled residue and waste mass without creating a resource or economy object.

Allowed planning purpose:

- Static cooled slag clumps for forge-adjacent dressing.
- Matte waste clusters that imply repeated brutal forging without becoming sorted scrap or ore.
- Scale support around Giant-built workspaces while preserving sibling boundaries with forge hearth, anvil/quench, scrap sorting, cooking pit, path marker, barricade, and shelter packages.

Out of scope:

- No ore node, metal resource, salvage object, crafting input, economy item, loot, harvest behavior, pickup prompt, interaction marker, heat damage, burn damage, hot-surface gameplay, VFX, smoke, sparks, heat shimmer, emissive map, material graph authoring, DCC source, Unreal implementation, final visual approval, or implementation target selection.

## Silhouette Notes

Primary silhouette: irregular cooled slag clumps with chunky lumpy crowns, broad heavy bases, crusted broken edges, and a few larger readable pieces arranged as static clusters.

Required reads:

- Cooled, matte, black-gray waste mass rather than shiny ore.
- Giant-scale clumps with broad broken planes and heavy contact shadows.
- Sparse bubble pits and crust detail handled mostly by texture/normal maps.
- Cluster variations that can sit beside ash piles and spill strips without merging into them.

Avoid gemstone silhouettes, collectible ore chunks, shiny metal nuggets, organized sorted scrap piles, hot glowing edges, active forge VFX, tidy civic forge waste, resource-node outlines, or dense micro-pore geometry.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Suggested size variants:

- Small clump cluster: 120-220 cm wide, 60-140 cm deep, 20-55 cm high.
- Medium clump cluster: 220-340 cm wide, 120-220 cm deep, 35-85 cm high.
- Large clump cluster: 340-480 cm wide, 180-300 cm deep, 55-125 cm high.
- Individual large lumps: 35-140 cm across, with only a few pieces large enough to affect silhouette.

The asset should feel like heavy Giant-scale forge waste, not small humanoid ore pickups. Any future review should compare the clump set against both the female 442 cm and male 470 cm Giant baselines before DCC or Unreal work.

## Materials and Color Palette

Primary material language:

- Matte cooled slag, black crust, dull iron gray, oxidized brown fractures, and ash-dusted contact edges.
- High roughness and no default emissive glow.
- Rare dull metal sheen only as broad worn planes, not shiny harvestable ore.

Suggested palette:

- Slag black: `#111111` to `#272522`
- Cooled iron gray: `#2F3333` to `#545957`
- Oxidized brown: `#3F281D` to `#6D432B`
- Ash-dusted edge: `#746D61` to `#A69A86`
- Deep crevice: `#050505` to `#151412`

Avoid bright resource colors, golden ore reads, molten orange heat, magical blue runes, civilized forge polish, or high-frequency shiny pitting.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeSlagLumps_A01` for the world of Aerathea. The design should emphasize cooled black-gray slag clumps, chunky lumpy crowns, broad heavy bases, crusted broken edges, ash-dusted contact zones, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, hostile Blood Axe Giant sub-faction identity, matte cooled waste color language, brutal field-forge mood, and a static environment-dressing role with no ore, resource, salvage, economy, heat damage, VFX, material graph, interaction, or implementation behavior. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a clean production asset board with small, medium, and large cluster variants, top-down footprints, side silhouettes, material swatches, LOD notes, and scale callouts. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral/civilized Giant cave-town motifs, avoid resource UI or pickup outlines, avoid molten glow, avoid active forge VFX, avoid economy diagrams, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, implementation target, ore/resource behavior, salvage behavior, economy behavior, or final visual approval is created or approved here.

Future modeling guidance:

- Build three reusable cluster variants: small, medium, and large.
- Use real geometry for primary lumpy silhouettes, broad broken planes, heavy bases, and a few large separate chunks.
- Keep the underside contact simple and stable for static dressing.
- Shape clusters as discarded waste, not neatly sorted scrap or collectible ore.
- Use asymmetry and broad planes so the asset reads from MMO camera distance.

Use texture and normal detail for tiny bubble pits, cooled crust pores, hairline cracks, ash dust, oxide staining, and minor chips. Do not model dense pore fields, tiny pebbles, small spark marks, or high-frequency cracks.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, or Unreal import is authored by this package.

Material slot plan:

- Slot 0: planned cooled slag material for black crust, iron-gray planes, ash dust, and oxidized fracture tones.

Texture naming examples:

- `T_GIA_BloodAxeSlagLumps_A01_BC`
- `T_GIA_BloodAxeSlagLumps_A01_N`
- `T_GIA_BloodAxeSlagLumps_A01_ORM`
- `MI_GIA_BloodAxeSlagLumps_A01`

Texture resolution target: 512 to 1K for individual clusters; 2K only if later approved for a combined slag atlas. 4K is not planned.

Packed `ORM` guidance:

- R: strong occlusion under cluster bases, between large lumps, and inside broad cracks.
- G: high roughness for cooled crust and ash; slightly lower roughness only on rare broad worn metal-like planes.
- B: low metallic overall; use restrained metallic only for rare cooled metal inclusions if approved by later material work.

## Triangle Budget

Target LOD0 ranges:

- Small cluster: 700-1.3k tris.
- Medium cluster: 1.2k-2.4k tris.
- Large cluster: 2.2k-4k tris.
- Combined reusable cluster set target: 3k-6k tris if packaged as one mesh with variants.

Target material slots: 1.

Spend geometry on lumpy profile, broad broken planes, heavy base shapes, and a few large separate chunks. Do not spend geometry on tiny pores, micro cracks, small chips, ash speckles, or dense surface pits.

## LOD Plan

All important variants require LOD0-LOD3.

- LOD0: full lumpy silhouettes, large broken planes, visible cluster separation, ash-dusted base edges, and broad crust zones.
- LOD1: 60-70 percent of LOD0; reduce small bevels, secondary chips, minor cracks, and small separate chunks.
- LOD2: 35-45 percent of LOD0; merge minor chunks, simplify lump crowns, reduce undercut detail, and keep only major planes.
- LOD3: 15-25 percent of LOD0; preserve cooled slag cluster read, broad heavy base, and matte dark mass.

Reduction order:

1. Tiny pore detail, ash speckles, and hairline cracks.
2. Small chips and minor bevels.
3. Secondary separate chunks and underside detail.
4. Internal lump subdivisions.
5. Primary lumpy silhouette only after all small detail is removed.

Never reduce the cooled slag mass read before removing small detail.

## Collision Notes

Collision guidance is display-only planning. This package does not create or approve collision proxies.

Recommended future collision:

- One simple grouped hull or box around each cluster footprint if blocking is required.
- Collision disabled for small decorative clusters unless a later implementation task needs display collision.
- No per-lump collision.
- Walkable collision disabled by default.

Do not add resource triggers, salvage triggers, harvest volumes, pickup collision, interaction volumes, heat damage volumes, burn hazards, VFX collision, per-chip collision, navmesh rules, cover volumes, physics simulation, or collision proxy assets from this package.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Fixed cooled slag cluster silhouettes.
- Painted cooled crust, ash dust, and oxide variation as visual material language only.
- No runtime motion claim.

Not approved:

- Heat shimmer, sparks, smoke, embers, molten glow, animated material states, emissive maps, bloom, audio cues, physics movement, destructible chunks, ore/resource behavior, salvage behavior, economy behavior, interaction behavior, heat damage, burn damage, Blueprint state, VFX, or startup-scene behavior.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, import script, material instance, texture, Blueprint, Niagara system, validator, startup actor, runtime source, material graph, final approval, ore/resource system, salvage system, economy object, or implementation target is created or approved by this package.

Planned future asset type:

- Static Mesh prop.

Planned future folder:

- `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/Slag/`

Planned future import rules:

- Import at scale 1.0 from centimeter-authored source.
- Pivot at ground center of each cluster footprint.
- Assign LOD0, LOD1, LOD2, and LOD3.
- Use 1 material slot.
- Sockets: none.
- Blueprint behavior: none.
- Animation list: none.
- Performance note: preserve cooled slag cluster mass and remove pore/chip detail before primary silhouette simplification.

## Folder and Naming Recommendation

Docs path:

- `docs/assets/props/SM_GIA_BloodAxeSlagLumps_A01/PRODUCTION_PACKAGE.md`

Future naming, pending separate approval:

- Static Mesh: `SM_GIA_BloodAxeSlagLumps_A01`
- Material Instance: `MI_GIA_BloodAxeSlagLumps_A01`
- Textures: `T_GIA_BloodAxeSlagLumps_A01_BC`, `T_GIA_BloodAxeSlagLumps_A01_N`, `T_GIA_BloodAxeSlagLumps_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concept folders, global indexes, task-board files, backlog files, bootstrap files, or any package outside this owned docs path from this task.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Validated Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5".
- Slag lumps are cooled static residue only, not ore, resource, salvage, economy object, heat damage source, VFX asset, material graph task, DCC source, Unreal implementation, final approval, or implementation target.
- Primary silhouette is chunky, matte, cooled, readable, and MMO-safe.
- Materials use cooled slag black, dull iron gray, oxidized brown, ash-dusted edges, and high roughness consistently.
- No emissive glow, molten heat, sparks, smoke, resource-node color, UI marker, shiny ore read, or neutral/civilized Giant civic language is included.
- Tiny pores, ash speckles, hairline cracks, and small chips are assigned to textures or normals instead of geometry.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision guidance, animation limits, Unreal import planning, folder/naming recommendation, and stop gates are included.
