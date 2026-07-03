# SM_GIA_BloodAxeAshDrifts_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeAshDrifts_A01`
- Asset type: Static Mesh prop production package
- Task: `AET-MA-20260629-441`
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Clutter_AshPiles_FootprintDrifts`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready for planning review; no DCC source, FBX, Unreal Content asset, material graph, VFX, runtime source, validator, startup placement, final approval, terrain blending approval, collision proxy creation, or implementation target is created or approved here.

`SM_GIA_BloodAxeAshDrifts_A01` defines thin static ash deposits for hearth bases, threshold edges, path corners, and shelter-adjacent soot falloff in Blood Axe camps. These pieces should read as flat residue sheets and shallow wind-pushed dust banks, not as animated drifting ash.

The Blood Axe Tribe remains a hostile Giant sub-faction. This asset uses dirty red-black raider camp language and must not replace or contaminate neutral/civilized Giant culture such as hidden cave-town terraces, blue-gray civic masonry, warm communal hearths, restrained blue runes, peaceful highland stonework, and organized civic craft.

## Gameplay Purpose

The asset supports static environmental dressing where a full ash pile would be too tall. It gives artists a low-cost residue edge for hostile Blood Axe forge lanes and camp thresholds while staying non-interactive.

Allowed planning purpose:

- Thin static ash around hearth bases, forge work lanes, shelter thresholds, and path corners.
- Visual transition between larger ash piles and surrounding ground without approving landscape or terrain blending.
- Cheap flat residue shapes that support Giant scale and Blood Axe camp grime.

Out of scope:

- No ash drift VFX, wind motion, dust particles, smoke, heat shimmer, ember particles, heat damage, burn damage, gatherable ash, crafting input, resource node, loot, economy behavior, pickup prompt, interaction marker, terrain blending approval, landscape material work, decal approval, collision proxy creation, DCC source, Unreal implementation, final visual approval, or implementation target selection.

## Silhouette Notes

Primary silhouette: very low, elongated ash drifts with feathered-looking painted edges, shallow ridges, and irregular crescent footprints. The mesh should read as a thin residue layer from game camera distance, with only enough geometry to avoid a perfectly flat card.

Required reads:

- Thin footprint strips and shallow banks that stay below surrounding props.
- Dark soot concentration near the inner edge and pale ash fading outward.
- Wide Giant-scale footprints that imply large work lanes and rough camp sweeping.
- Several reusable shapes: crescent edge, threshold strip, corner patch, and scattered low bank.

Avoid animated ash trails, terrain-blend claims, decal-only planning, glowing hot ash, resource pickup shapes, tidy civic floor dressing, dense particle-like debris, or polished neutral/civilized Giant craft.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Suggested size variants:

- Threshold strip: 220-420 cm long, 50-110 cm deep, 2-12 cm high.
- Corner drift: 180-360 cm wide, 120-260 cm deep, 3-18 cm high.
- Long footprint drift: 420-800 cm long, 80-180 cm deep, 4-22 cm high.
- Patch set: 100-240 cm wide per patch, 60-160 cm deep, 2-12 cm high.

These pieces are floor residue for Giant-scale spaces. Any future review should compare them against both the female 442 cm and male 470 cm Giant baselines before DCC or Unreal work.

## Materials and Color Palette

Primary material language:

- Matte powder ash, soot falloff, pale gray dust, and crushed charcoal residue.
- Very broad value transitions that remain readable when viewed flat on the ground.
- No emissive glow, active heat, resource-node color, or magical dust language.

Suggested palette:

- Soot black: `#0B0A09` to `#201D19`
- Drift core gray: `#4A4741` to `#6C665E`
- Powder ash: `#898175` to `#B5AA98`
- Pale edge dust: `#C7BCA8` to `#D8CBB4`
- Charcoal fleck: `#151412` to `#2F2E2A`

Keep edge noise painterly and restrained. The visual should be broad, dirty, and static, not a high-frequency particle field.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeAshDrifts_A01` for the world of Aerathea. The design should emphasize thin static ash drifts, flat elongated footprint strips, shallow threshold residue, pale ash edges, dark soot falloff, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, hostile Blood Axe Giant sub-faction identity, matte ash gray and soot black color language, rough camp threshold mood, and a static environment-dressing role with no ash drift VFX, heat, damage, gatherable resource, terrain blending approval, collision proxy creation, interaction, or implementation behavior. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a clean production asset board with top-down footprint variants, very low side profiles, material swatches, LOD notes, and scale callouts. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral/civilized Giant cave-town motifs, avoid resource UI, avoid terrain blending diagrams, avoid smoke or particle VFX, avoid heat damage markings, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, implementation target, or final visual approval is created or approved here.

Future modeling guidance:

- Build four reusable low-profile variants: threshold strip, corner drift, long footprint drift, and scattered patch.
- Use very low geometry for the main surface undulation and irregular footprint edge.
- Keep the forms shallow enough to sit visually on ground planes without claiming terrain blending approval.
- Add only a few raised ridges where silhouette helps read from camera distance.
- Avoid vertical chunks except occasional broad low charcoal smudges.

Use texture and normal detail for powder falloff, fine ash dust, soot staining, small charcoal flecks, and subtle scrape marks. Do not model individual ash grains, dust trails, high-frequency debris, or many tiny pebbles.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, landscape material, terrain blend, decal setup, or Unreal import is authored by this package.

Material slot plan:

- Slot 0: planned ash drift and soot falloff material.

Texture naming examples:

- `T_GIA_BloodAxeAshDrifts_A01_BC`
- `T_GIA_BloodAxeAshDrifts_A01_N`
- `T_GIA_BloodAxeAshDrifts_A01_ORM`
- `MI_GIA_BloodAxeAshDrifts_A01`

Texture resolution target: 512 to 1K. Use broad hand-painted gradients and avoid 4K hero texture planning.

Packed `ORM` guidance:

- R: subtle occlusion in shallow ridges and darker drift cores.
- G: high roughness across all ash and soot.
- B: metallic black.

## Triangle Budget

Target LOD0 ranges:

- Small patch: 250-500 tris.
- Threshold strip: 350-800 tris.
- Corner drift: 500-1.1k tris.
- Long footprint drift: 700-1.8k tris.
- Combined reusable drift set target: 1.5k-3.5k tris if packaged as one mesh with variants.

Target material slots: 1.

Spend geometry only on broad footprint shape, shallow raised ridges, and non-rectangular edges. Do not spend geometry on dust, soot speckles, fine edge breakup, tiny charcoal flecks, or ground blending.

## LOD Plan

All important variants require LOD0-LOD3.

- LOD0: full footprint shapes, shallow surface ridges, broad soot-to-ash material zones, and irregular perimeter.
- LOD1: 60-70 percent of LOD0; reduce edge cuts, remove minor ridges, and simplify patch outlines.
- LOD2: 35-45 percent of LOD0; flatten most internal ridges, merge perimeter detail, and keep only the strongest silhouette corners.
- LOD3: 15-25 percent of LOD0; preserve broad flat drift footprint and dark-to-pale ash read.

Reduction order:

1. Soot speckles, ash flecks, and fine scrape marks.
2. Tiny edge cuts and small perimeter waves.
3. Minor internal ridges.
4. Secondary patch shapes.
5. Main footprint only after all small detail is removed.

Never reduce the flat elongated drift identity before removing small detail.

## Collision Notes

Collision guidance is display-only planning. This package does not create or approve collision proxies.

Recommended future collision:

- Collision disabled by default.
- No walkable collision requirement.
- No blocking collision unless a later implementation task explicitly requests a simple display-only hull for a composed review scene.

Do not add gatherable collision, resource triggers, interaction volumes, heat damage volumes, burn hazards, VFX collision, terrain-blend collision, decal collision, navmesh rules, cover volumes, physics simulation, or collision proxy assets from this package.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Fixed ash drift silhouettes.
- Painted ash, soot, and powder falloff as visual material language only.
- No runtime motion claim.

Not approved:

- Ash drift VFX, wind movement, dust particles, smoke, embers, sparks, heat shimmer, active flames, animated material states, emissive maps, bloom, audio cues, physics movement, interaction behavior, heat damage, burn damage, gatherable behavior, Blueprint state, or startup-scene behavior.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, import script, material instance, texture, Blueprint, Niagara system, validator, startup actor, runtime source, terrain blending approval, final approval, or implementation target is created or approved by this package.

Planned future asset type:

- Static Mesh prop.

Planned future folder:

- `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/Ash/`

Planned future import rules:

- Import at scale 1.0 from centimeter-authored source.
- Pivot at ground center of each drift footprint.
- Assign LOD0, LOD1, LOD2, and LOD3.
- Use 1 material slot.
- Sockets: none.
- Blueprint behavior: none.
- Animation list: none.
- Performance note: preserve broad flat footprints and remove fine ash/soot detail before changing the main drift shape.

## Folder and Naming Recommendation

Docs path:

- `docs/assets/props/SM_GIA_BloodAxeAshDrifts_A01/PRODUCTION_PACKAGE.md`

Future naming, pending separate approval:

- Static Mesh: `SM_GIA_BloodAxeAshDrifts_A01`
- Material Instance: `MI_GIA_BloodAxeAshDrifts_A01`
- Textures: `T_GIA_BloodAxeAshDrifts_A01_BC`, `T_GIA_BloodAxeAshDrifts_A01_N`, `T_GIA_BloodAxeAshDrifts_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concept folders, global indexes, task-board files, backlog files, bootstrap files, or any package outside this owned docs path from this task.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Validated Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5".
- Ash drifts are static residue only, not ash drift VFX, heat damage, burn damage, gatherable resource, terrain blending approval, collision proxy creation, DCC source, Unreal implementation, final approval, or implementation target.
- Primary silhouette is flat, low, elongated, readable, and MMO-safe.
- Materials use soot black, ash gray, powder pale edges, and matte charcoal flecks consistently.
- No emissive glow, active fire, smoke, particle VFX, resource-node color, UI marker, terrain blending claim, or neutral/civilized Giant civic language is included.
- Tiny ash flecks, soot speckles, fine scrape marks, and powder falloff are assigned to textures or normals instead of geometry.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision guidance, animation limits, Unreal import planning, folder/naming recommendation, and stop gates are included.
