# SM_GIA_BloodAxeCharcoalHeaps_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeCharcoalHeaps_A01`
- Asset type: Static Mesh production package, docs-only planning
- Task: `AET-MA-20260629-443`
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Clutter_CharcoalHeaps_CrushedFuel`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: production package documentation only; no DCC, FBX, Unreal Content asset, material graph, VFX, Blueprint, validator, startup placement, final approval, or implementation target is created or approved here

`SM_GIA_BloodAxeCharcoalHeaps_A01` is a set of broad, matte black charcoal residue heaps for Blood Axe Giant forge yards and hostile camp edges. The asset should read as crushed fuel remnants and dirty environmental dressing, not as a pickup, counted fuel stack, crafting ingredient, cooking station, inventory object, economy item, heat source, VFX emitter, or workstation.

The Blood Axe Tribe remains a hostile Giant sub-faction. This visual language must stay separate from neutral/civilized Giant culture: no blue-gray civic masonry, peaceful cave-town hearth identity, restrained blue runes, waterworks, terraces, or polished master-stoneworker craft.

## Gameplay Purpose

The asset supports static environmental storytelling around Blood Axe forge hearths, rough shelters, cooking-pit perimeters, and dirty work lanes. It gives level artists a readable black fuel-residue mass that reinforces the soot-heavy camp story without adding gameplay systems.

Allowed purpose:

- Static camp and forge dressing only.
- Visual evidence of burned fuel and crude Blood Axe labor.
- Ground-level breakup near ash piles, slag, firewood, quench props, and scorched debris.
- Giant-scale residue that remains readable from MMO camera distance.

Out of scope:

- Pickup, fuel-count, cooking, crafting, economy, inventory, workstation, resource, loot, salvage, vendor, interaction, UI prompt, heat, damage, VFX, audio, physics, destructible, DCC, Unreal implementation, final approval, or implementation-target behavior.

## Silhouette Notes

Primary read: low to mid-height crushed charcoal mounds with a few large, angular top chunks. The heap should be broad and dirty, with irregular but simple mound edges, dark center mass, and pale ash dust around contact points.

Required silhouette traits:

- Broad oval or crescent heap footprints.
- Several chunky, hand-readable charcoal pieces on top, each large enough to read at distance.
- Low collapsed slopes rather than tidy resource piles.
- Broken matte fragments, crushed black dust, and soft ash spill edges.
- No treasure-pile, ore-node, crystal, UI pickup, active coal, or glowing ember silhouette.

Model real geometry for the main mound, large top chunks, broad fracture planes, and a few chunky outline pieces. Use texture and normal detail for tiny pores, soot speckles, hairline cracks, fine ash grains, and small chips.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Suggested production dimensions:

- Small heap variant: 160-260 cm wide, 90-180 cm deep, 30-70 cm high.
- Medium heap variant: 260-380 cm wide, 140-250 cm deep, 55-105 cm high.
- Large heap variant: 380-500 cm wide, 220-320 cm deep, 80-140 cm high.
- Major top chunks: 25-85 cm across, kept broad and sparse.
- Pale ash spill edge: 20-70 cm beyond the dark core where needed.

The heaps should feel too large and dirty for normal humanoids to treat as convenient handheld supplies. Scale review in any future lane must compare against both the female 442 cm and male 470 cm Giant baselines before DCC or Unreal work.

## Materials and Color Palette

Primary material language:

- Matte black charcoal.
- Soft gray ash dust.
- Charred bark remnants.
- Dull fracture planes.
- Pale residue on ground contact edges.
- Very restrained Blood Axe red cloth flecks only if needed for faction read; avoid making red tags look like interaction markers.

Suggested palette:

- Charcoal black: `#080706` to `#1E1B18`
- Soft soot: `#24211E` to `#393631`
- Fracture gray: `#4A4942` to `#626057`
- Pale ash edge: `#8E887C` to `#B7AA98`
- Charred bark brown: `#24150F` to `#3A2419`
- Restrained Blood Axe red: `#5F1513` to `#812018`

No emissive color is planned. Avoid orange glow, heat language, bright resource colors, blue Aetherium, civilized Giant civic blues, polished metal shine, or high-frequency gray noise.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeCharcoalHeaps_A01` for the world of Aerathea. The design should emphasize broad crushed charcoal heaps, matte black fuel residue, sparse large angular chunks, soft pale ash edges, Giant scale beside female 442 cm / 14'6" and male 470 cm / 15'5" baselines, hostile Blood Axe camp identity, soot-black and ash-gray color language, separation from neutral/civilized Giant culture, and a static environment-dressing role only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a clean static prop concept sheet with three heap size variants, top-down footprints, material swatches, and LOD/collision callouts. Avoid copying any existing franchise, avoid active flames, glowing embers, heat shimmer, smoke, particles, pickup markers, fuel counters, cooking or crafting UI, workstation staging, inventory presentation, resource-node language, and excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, runtime behavior, final approval, or implementation target is created or approved here.

Future modeling guidance:

- Build three reusable heap sizes from broad mound forms.
- Add a sparse layer of large charcoal chunks on the top and front-facing edges.
- Keep the underside flat enough for predictable ground placement.
- Use asymmetric silhouettes so repeated placement does not form obvious identical piles.
- Keep top chunks broad, faceted, and readable rather than numerous and tiny.
- Add shallow ash lips as part of the static mesh only where they support placement readability.
- Avoid handle-like shapes, tidy counted stacks, bin labels, cooking props, recipe boards, forge controls, interaction rings, UI-friendly outlines, or heat-warning geometry.

Use real geometry for main mound profiles and large charcoal silhouette chunks. Use texture and normal maps for pores, soot dust, small cracks, bark grain remnants, and fine ash.

## Texture and Material Notes

Required future texture map set:

- Base Color / Albedo: `T_GIA_BloodAxeCharcoalHeaps_A01_BC`
- Normal: `T_GIA_BloodAxeCharcoalHeaps_A01_N`
- Packed Occlusion/Roughness/Metallic: `T_GIA_BloodAxeCharcoalHeaps_A01_ORM`

Material slot target:

- Slot 0: `MI_GIA_BloodAxeCharcoal_A01` or a shared future ash/slag/charcoal material instance.

Texture resolution target:

- 512 to 1K for small and medium heap variants.
- 1K for the large heap set.
- No 2K or 4K hero texture is planned unless a later approved review changes scope.

Packed `ORM` guidance:

- R: strong occlusion under top chunks, in mound creases, and at the dark heap core.
- G: very high roughness across charcoal, soot, and ash; no glossy fuel or wet coal read.
- B: metallic at 0.0 for the baseline asset.

No emissive map is planned. No material graph, shader, texture asset, or material instance is authored by this package.

## Triangle Budget

Target LOD0 budget:

- Small heap variant: 900-1,600 tris.
- Medium heap variant: 1,500-2,800 tris.
- Large heap variant: 2,500-4,000 tris.
- Combined size-variant set: keep under 8,500 tris if authored as one review mesh.

Material slots:

- 1 material slot target.
- 2 material slots maximum only if a later approved package requires separate ash decals or faction tags.

Spend geometry on the main heap shape, large readable top chunks, and broad footprint edges. Do not spend geometry on tiny pores, ash flecks, dust grains, small chips, dense gravel, individual splinters, or counted fuel pieces.

## LOD Plan

All important variants require LOD0-LOD3.

- LOD0: full mound profile, large top chunks, asymmetric footprint, broad ash lips, and readable fracture planes.
- LOD1: 60-70 percent of LOD0; reduce small bevels, secondary chips, minor ash-lip subdivisions, and non-silhouette chunk cuts.
- LOD2: 35-45 percent of LOD0; merge small chunk clusters, simplify mound slopes, remove interior cuts, and keep only major top pieces.
- LOD3: 15-25 percent of LOD0; preserve broad black heap mass, low silhouette, footprint, and pale ash edge read.

LOD reduction order:

1. Tiny pores, soot speckles, ash flecks, and fine cracks.
2. Small chips, secondary bevels, and minor fracture cuts.
3. Non-silhouette top chunks and internal mound subdivisions.
4. Back-side or underside detail.
5. Broad mound profile only after all small detail has been removed.

Never collapse the heap into a flat decal-like smear before the charcoal mass is unreadable.

## Collision Notes

Collision remains simple, static, and display-focused.

Recommended future collision:

- Collision disabled by default for purely visual floor dressing.
- If blocking is needed, use one shallow low-count convex hull or box around the broad mound footprint.
- Keep walkable collision disabled.
- Do not use per-chunk collision.

Do not add pickup collision, fuel-count collision, cooking interaction volumes, crafting triggers, inventory triggers, workstation volumes, heat damage volumes, VFX collision, resource harvest volumes, loot outlines, physics simulation, destructible fracture collision, cover volumes, nav rules, or encounter hazard volumes.

## Animation Notes

Baseline asset is static.

Approved for this package:

- Fixed charcoal heap silhouettes.
- Painted soot and ash variation only.
- No runtime motion claim.

Not included:

- Smoke, sparks, embers, active flame, heat shimmer, ash drift, dust puffs, animated material states, emissive pulsing, physics-simulated chunks, destructible collapse, audio, interaction, pickup, fuel-count, cooking, crafting, economy, inventory, workstation, or Blueprint state.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, import, material instance, texture asset, Blueprint, Niagara system, validator, startup actor, runtime source, final approval, or implementation target is created by this package.

Planned future asset type:

- Static Mesh: `SM_GIA_BloodAxeCharcoalHeaps_A01`

Import planning:

- Author in centimeters and import at scale 1.0.
- Pivot at ground center of the heap footprint.
- Forward axis should support easy rotation for repeated ground placement.
- Assign LOD0, LOD1, LOD2, and LOD3.
- Material slots: 1 target.
- Collision: disabled by default or one simple display hull if explicitly needed later.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance note: keep large charcoal chunks readable while reducing pore, dust, chip, and crack detail first.

Texture list:

- `T_GIA_BloodAxeCharcoalHeaps_A01_BC`
- `T_GIA_BloodAxeCharcoalHeaps_A01_N`
- `T_GIA_BloodAxeCharcoalHeaps_A01_ORM`

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeCharcoalHeaps_A01/PRODUCTION_PACKAGE.md`

Future planning folders, pending separate approval:

- Static Mesh: `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/ForgeClutter/`

Recommended names:

- Static Mesh: `SM_GIA_BloodAxeCharcoalHeaps_A01`
- Material Instance: `MI_GIA_BloodAxeCharcoal_A01`
- Base Color: `T_GIA_BloodAxeCharcoalHeaps_A01_BC`
- Normal: `T_GIA_BloodAxeCharcoalHeaps_A01_N`
- ORM: `T_GIA_BloodAxeCharcoalHeaps_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concepts, global indexes, task-board files, backlog files, bootstrap files, or sibling package files from this task.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Female Giant baseline 442 cm / 14'6" and male Giant baseline 470 cm / 15'5" are preserved.
- Asset is static charcoal fuel residue only.
- No pickup, fuel-count, cooking, crafting, economy, inventory, workstation, heat, VFX, DCC, Unreal implementation, final approval, or implementation target is claimed.
- Silhouette uses broad MMO-readable heaps and sparse large chunks.
- Materials use matte charcoal black, soot gray, pale ash edge, and no emissive glow.
- Tiny pores, soot speckles, ash flecks, hairline cracks, and small chips are texture or normal detail, not geometry.
- Triangle budget, LOD0-LOD3 plan, simple display collision guidance, texture map plan, and Unreal import planning are included.
- Folder and naming recommendations preserve `GIA` and `BloodAxe` naming.
- Package remains docs-only and does not modify external source concepts, global indexes, task board, DCC, Unreal, source, tools, validators, Hermes files, or unrelated packages.
