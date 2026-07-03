# SM_GIA_BloodAxeCharcoalBins_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeCharcoalBins_A01`
- Asset type: Static Mesh production package, docs-only planning
- Task: `AET-MA-20260629-443`
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Clutter_CharcoalHeaps_ShallowBins`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: production package documentation only; no DCC, FBX, Unreal Content asset, material graph, VFX, Blueprint, validator, startup placement, final approval, or implementation target is created or approved here

`SM_GIA_BloodAxeCharcoalBins_A01` defines shallow crude charcoal trays and half-bin dressing for Blood Axe Giant camp and forge spaces. The bins are dirty static residue holders, not functional storage, pickup containers, fuel-count systems, cooking props, crafting stations, inventory interfaces, economy objects, heat sources, VFX assets, or workstations.

The Blood Axe Tribe remains a hostile Giant sub-faction. These bins should feel raider-built and temporary, with rough charred timber, black dust, and crude iron, while staying separate from neutral/civilized Giant cave-town craft, polished stonework, blue-gray masonry, peaceful hearth language, restrained blue runes, terraces, and waterworks.

## Gameplay Purpose

The asset supports static forge-yard and camp dressing where loose charcoal needs a stronger container silhouette than an open heap. It helps communicate that Blood Axe camps consume heavy fuel and leave disorderly residue without introducing resource behavior.

Allowed purpose:

- Non-interactive charcoal and black dust dressing.
- Shallow tray or half-bin forms for camp edges and forge-side clutter.
- Visual bridge between loose charcoal heaps, firewood stacks, ash piles, and cooled slag.
- Giant-scale environmental story object sized for broad readability.

Out of scope:

- Pickup, fuel-count, cooking, crafting, economy, inventory, workstation, resource, loot, salvage, vendor, storage gameplay, interaction, UI prompt, heat, damage, VFX, audio, physics, destructible, DCC, Unreal implementation, final approval, or implementation-target behavior.

## Silhouette Notes

Primary read: a shallow, crude, Giant-scale tray or half-bin holding matte black charcoal and black dust. The profile should be squat and broad, with rough plank or hammered metal edges and a low mound of broken charcoal inside.

Required silhouette traits:

- Wide low rectangular, oval, or rough trapezoid footprint.
- Crude lip or tray wall that reads as Blood Axe field construction.
- Charcoal fill sitting below or slightly above the rim, never as a tidy counted stockpile.
- Chunky large pieces near the rim for readability.
- Optional tipped or split half-bin variant for abandoned dressing.
- No workstation read, inventory chest read, loot container read, cooking station read, or glowing hot coal read.

Model real geometry for tray walls, heavy rim pieces, broad charcoal fill, large visible chunks, and damaged plank or metal lip silhouettes. Use texture and normal detail for fine soot, wood grain, small nail marks, metal pitting, tiny cracks, and charcoal pores.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Suggested production dimensions:

- Small shallow bin: 180-280 cm wide, 100-180 cm deep, 45-80 cm high.
- Medium shallow bin: 280-420 cm wide, 150-250 cm deep, 65-110 cm high.
- Large shallow bin: 420-560 cm wide, 220-330 cm deep, 90-140 cm high.
- Rim thickness: 12-35 cm, exaggerated enough to read at Giant scale.
- Charcoal fill mound: 20-75 cm above the tray floor, kept low enough to stay residue-like.
- Large visible chunks: 25-90 cm across.

The bins should read as equipment-sized dressing for female 442 cm and male 470 cm Giants, not convenient normal-humanoid containers. Future scale review must compare against both Giant baselines before DCC or Unreal work.

## Materials and Color Palette

Primary material language:

- Matte black charcoal and dust.
- Charred rough timber or dark battered metal tray sides.
- Dull blackened iron bands or nail heads only as sparse support details.
- Pale ash accumulation along floor contacts and lower rim corners.
- Restrained Blood Axe red paint or cloth tag only if needed for faction read, never as an interaction marker.

Suggested palette:

- Charcoal black: `#080706` to `#1F1C18`
- Soot gray: `#2B2925` to `#514D45`
- Pale ash: `#8E877A` to `#B8AD9C`
- Charred timber: `#1D120D` to `#3E281B`
- Rough dark iron: `#151515` to `#33312C`
- Oxide brown: `#52301F` to `#704229`
- Restrained Blood Axe red: `#5A1412` to `#832018`

No emissive color is planned. Avoid orange heat, bright coals, magical glow, blue Aetherium, polished civilized craft, clean storage-chest colors, or vendor/resource readability.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeCharcoalBins_A01` for the world of Aerathea. The design should emphasize shallow crude Blood Axe Giant charcoal bins, rough tray or half-bin silhouettes, matte black charcoal fill, black dust, charred timber or battered dark iron rims, pale ash deposits, female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale callouts, hostile raider camp identity, separation from neutral/civilized Giant culture, and a static residue-dressing role only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a clean prop concept sheet with front, top, and three-quarter views, size variants, material swatches, and LOD/collision callouts. Avoid copying any existing franchise, avoid workstation controls, inventory chest language, pickup prompts, fuel counters, cooking or crafting UI, resource-node framing, active heat, smoke, sparks, VFX, and excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, runtime behavior, final approval, or implementation target is created or approved here.

Future modeling guidance:

- Build two or three shallow container variants: intact tray, damaged tray, and tipped half-bin.
- Keep the tray silhouette broad and low so it reads as dressing, not as a crafting workstation.
- Use oversized planks, crude hammered plates, or dark iron straps with simple shapes.
- Keep the charcoal fill as a broad interior mass with sparse large chunks.
- Make damage chunky and readable, not splinter-heavy.
- Use a flat ground contact plane or stable rim supports for predictable placement.
- Avoid lids, hinges, handles, latch hardware, UI-facing front panels, readable labels, cooking hooks, recipe boards, forge controls, resource sacks, or pickup affordances.

Use real geometry for the tray, half-bin rim, broad fill, and major chunks. Use texture and normal maps for soot, charred wood grain, small nail heads, metal pitting, charcoal pores, and ash dust.

## Texture and Material Notes

Required future texture map set:

- Base Color / Albedo: `T_GIA_BloodAxeCharcoalBins_A01_BC`
- Normal: `T_GIA_BloodAxeCharcoalBins_A01_N`
- Packed Occlusion/Roughness/Metallic: `T_GIA_BloodAxeCharcoalBins_A01_ORM`

Material slot target:

- Slot 0: charcoal, ash, charred timber, and blackened tray surfaces atlased together where possible.
- Optional Slot 1: dark iron hardware only if metal coverage is too high for a clean single-slot atlas.

Texture resolution target:

- 1K for standard bin variants.
- 512 for small alternate fill or broken-rim pieces if split later.
- No 4K hero texture is planned.

Packed `ORM` guidance:

- R: strong occlusion inside tray corners, below charcoal chunks, under rims, and around ground contacts.
- G: high roughness for charcoal, soot, ash, charred wood, and blackened iron.
- B: metallic only on dark iron bands, nail heads, or hammered metal tray pieces; charcoal, ash, and wood remain non-metallic.

No emissive map is planned. No material graph, shader, texture asset, or material instance is authored by this package.

## Triangle Budget

Target LOD0 budget:

- Small shallow bin: 1,200-2,200 tris.
- Medium shallow bin: 2,000-3,800 tris.
- Large or tipped half-bin: 3,200-5,000 tris.
- Combined variant review mesh: keep under 10,000 tris if variants are temporarily composed for review by a later approved task.

Material slots:

- 1 material slot target.
- 2 material slots maximum for optional metal hardware.

Spend geometry on tray proportions, heavy rims, damaged broad edges, large charcoal chunks, and the bin footprint. Do not spend geometry on tiny soot specks, dense pores, individual ash grains, small nail heads, fine wood fibers, or numerous small charcoal fragments.

## LOD Plan

All important variants require LOD0-LOD3.

- LOD0: full tray silhouette, rim damage, broad charcoal fill, large chunks, rough supports, and material zone separation.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor rim cuts, secondary chunks, underside supports, and small plank variation.
- LOD2: 35-45 percent of LOD0; simplify tray walls, merge charcoal fill pieces, remove non-silhouette damage, and reduce hardware.
- LOD3: 15-25 percent of LOD0; preserve shallow bin footprint, rim height, black fill mass, and crude Blood Axe dressing read.

LOD reduction order:

1. Soot speckles, pores, fine wood grain, tiny nail marks, and small cracks.
2. Minor rim chips, small hardware, tiny charcoal pieces, and secondary bevels.
3. Interior fill subdivisions and non-silhouette tray damage.
4. Underside supports and back-side detail.
5. Main tray walls and broad fill mass only after smaller details are removed.

Never remove the shallow-bin read before reducing interior charcoal detail.

## Collision Notes

Collision remains simple, static, and display-focused.

Recommended future collision:

- Collision disabled by default for non-blocking dressing.
- If display blocking is required, use one simplified box or convex hull around the full tray footprint.
- For larger bins, use two simple hulls at most: tray body and visible fill mass.
- Keep walkable collision disabled.
- Do not use per-charcoal, per-rim, or per-hardware collision.

Do not add pickup collision, fuel-count collision, cooking interaction volumes, crafting triggers, inventory volumes, workstation triggers, storage gameplay collision, heat damage volumes, VFX collision, resource harvest volumes, loot outlines, physics simulation, destructible fracture collision, cover volumes, nav rules, or encounter hazard volumes.

## Animation Notes

Baseline asset is static.

Approved for this package:

- Fixed shallow-bin and charcoal-fill silhouettes.
- Painted soot, ash, wood, and blackened metal variation only.
- No runtime motion claim.

Not included:

- Opening lids, moving tray parts, sliding charcoal, smoke, sparks, embers, active flame, heat shimmer, ash drift, animated material states, emissive pulsing, physics-simulated pieces, destructible collapse, audio, interaction, pickup, fuel-count, cooking, crafting, economy, inventory, workstation, storage gameplay, or Blueprint state.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, import, material instance, texture asset, Blueprint, Niagara system, validator, startup actor, runtime source, final approval, or implementation target is created by this package.

Planned future asset type:

- Static Mesh: `SM_GIA_BloodAxeCharcoalBins_A01`

Import planning:

- Author in centimeters and import at scale 1.0.
- Pivot at ground center of the bin footprint.
- Long axis aligned for grid-friendly placement.
- Assign LOD0, LOD1, LOD2, and LOD3.
- Material slots: 1 target, 2 maximum if hardware is separated.
- Collision: disabled by default or simple display hulls if explicitly needed later.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance note: preserve tray silhouette and black fill mass; remove pores, dust, rim chips, and back-side detail first.

Texture list:

- `T_GIA_BloodAxeCharcoalBins_A01_BC`
- `T_GIA_BloodAxeCharcoalBins_A01_N`
- `T_GIA_BloodAxeCharcoalBins_A01_ORM`

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeCharcoalBins_A01/PRODUCTION_PACKAGE.md`

Future planning folders, pending separate approval:

- Static Mesh: `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/ForgeClutter/`

Recommended names:

- Static Mesh: `SM_GIA_BloodAxeCharcoalBins_A01`
- Material Instance: `MI_GIA_BloodAxeCharcoalBins_A01`
- Base Color: `T_GIA_BloodAxeCharcoalBins_A01_BC`
- Normal: `T_GIA_BloodAxeCharcoalBins_A01_N`
- ORM: `T_GIA_BloodAxeCharcoalBins_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concepts, global indexes, task-board files, backlog files, bootstrap files, or sibling package files from this task.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Female Giant baseline 442 cm / 14'6" and male Giant baseline 470 cm / 15'5" are preserved.
- Asset is static charcoal and black dust dressing only.
- No pickup, fuel-count, cooking, crafting, economy, inventory, workstation, storage gameplay, heat, VFX, DCC, Unreal implementation, final approval, or implementation target is claimed.
- Silhouette uses broad shallow bins, crude heavy rims, and sparse large charcoal chunks.
- Materials use matte charcoal, soot, ash, charred timber, optional blackened iron, and no emissive glow.
- Tiny pores, soot speckles, ash flecks, fine cracks, small nails, and pitting are texture or normal detail, not geometry.
- Triangle budget, LOD0-LOD3 plan, simple display collision guidance, texture map plan, and Unreal import planning are included.
- Folder and naming recommendations preserve `GIA` and `BloodAxe` naming.
- Package remains docs-only and does not modify external source concepts, global indexes, task board, DCC, Unreal, source, tools, validators, Hermes files, or unrelated packages.
