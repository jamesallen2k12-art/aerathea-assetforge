# DOC_GIA_BloodAxeAshSlagFirewoodLODAndCollision_A01 Production Package

## 1. Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeAshSlagFirewoodLODAndCollision_A01`
- Asset type: Documentation-only LOD and collision policy package; non-shipping
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake rows: ash piles, slag lumps, charcoal heaps, firewood stacks, scorched debris, review composition rows, and optional forge clutter cluster from `BloodAxeForge.png#Clutter_AshSlagFirewood`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: policy-only review planning document; not a mesh, not a collision proxy, not an Unreal actor, not shipped content

This package defines docs-only LOD0-LOD3 and simple display collision policy for future ash piles, slag lumps, charcoal heaps, firewood stacks, scorched debris rows, review composition rows, and the optional forge clutter cluster. It protects silhouette readability and prevents overbuilt collision without creating UCX files, proxies, validators, nav blockers, gameplay volumes, or implementation targets.

Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture. LOD and collision policy must preserve hostile forge-residue readability without turning ash, slag, charcoal, firewood, or debris into refined Giant civic objects, resource systems, heat hazards, or gameplay volumes.

Guardrails: docs-only, policy-only, non-shipping, no-DCC, no-FBX, no-Unreal, no-startup, no-shipped-marker, no-scale-lock-change, no-nav, no-nav-blocker, no-encounter, no-workstation, no-loot, no-resource, no-material-instance, no-texture-asset, no-material-graph, no-VFX/audio, no-collision-proxy, no-UCX, no-gameplay-volume, no-validator, no-capture, no-final-approval, no-implementation-target.

## 2. Gameplay Purpose

This is a non-shipping LOD/collision policy document. It helps later packages avoid silhouette-damaging LOD reductions, per-detail physics, overbuilt collision, nav/pathing overclaims, heat or damage overclaims, and gameplay-volume drift.

It does not create gameplay, runtime behavior, nav/pathfinding, nav blockers, encounters, workstations, loot, resources, economy systems, pickups, interactions, heat damage, burn damage, damage volumes, startup placement, captures, validators, meshes, collision proxies, UCX files, material instances, texture assets, material graphs, VFX/audio, shipped markers, or final approval.

## 3. Silhouette Notes

LOD policy should preserve the broad category reads before retaining small detail:

- Ash: low bank footprint, dark center mass, pale edge silhouette, and broad mound rhythm.
- Slag: lumpy cooled clumps, spill strip footprint, chunky profile, and rough crusted mass.
- Charcoal: broad heap mass, a few large top chunks, matte black read, and crushed fuel rhythm.
- Firewood: Giant-scale log thickness, crib-stack rhythm, split trunk planes, tied bundle mass, and charred end caps.
- Scorched debris: long burned beams, snapped stakes, broken plank silhouettes, ash-stained stones, rare bent plate fragments, and sparse red cloth tags.
- Review rows: row spacing, category separation, and non-shipping label readability if a later task visualizes rows.
- Forge clutter cluster: broad composed footprint and negative space around represented child categories without merging sibling package silhouettes.

Collision policy should outline simple display hulls only. It must not imply pickup volumes, harvest volumes, workstation use, hot-surface behavior, heat damage, burn damage, nav blockers, cover, traps, destructible chunks, physics simulation, or encounter logic.

## 4. Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

LOD/collision policy should ensure simplified forms remain readable beside the 442 cm and 470 cm baselines. Collision simplification must not become a gameplay scale claim, nav/pathfinding rule, traversal proof, cover rule, heat hazard, or shipped marker approval.

This package does not change scale lock, create collision proxies, create UCX files, approve shipped markers, or select implementation targets.

## 5. Materials and Color Palette

Policy rows should use the same review language as the parent kit: soot black, ash gray, pale ash edge, cooled slag black, oxidized slag brown, charcoal fracture gray, charred bark, split raw wood, rare blackened stolen metal scraps, and restrained oxide red cloth tags.

Material color should support LOD readability by keeping broad ash/soot, slag, charcoal, wood, metal, and red cloth blocks recognizable at distance. This package does not create material instances, texture assets, material graphs, shaders, emissive maps, or VFX materials.

Reject neutral/civilized Giant blue-gray civic masonry, warm peaceful hearth symbolism, restrained blue runes, polished stoneworker craft, resource-node shine, active orange fire, glowing coals, and material changes that imply gameplay states.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `DOC_GIA_BloodAxeAshSlagFirewoodLODAndCollision_A01` for the world of Aerathea. The design should emphasize docs-only non-shipping LOD0 through LOD3 and simple display collision policy rows for hostile Blood Axe Giant ash piles, cooled slag lumps, charcoal heaps, Giant-scale firewood stacks, scorched debris, review composition rows, and an optional forge clutter cluster, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", preserved silhouettes, ordered detail reduction, simplified display hull callouts, no UCX creation, no collision proxies, no validators, no nav blockers, no gameplay volumes, no heat damage, no resource pickups, Blood Axe hostile sub-faction identity, soot black, ash gray, cooled slag, charred bark, split raw wood, rare blackened metal, restrained oxide red cloth, and policy-only review use. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean docs-only review board with LOD rows and collision diagrams clearly labeled as non-shipping policy only. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral/civilized Giant cave-town motifs, avoid final visual approval claims, avoid startup placement framing, avoid collision-correct gameplay claims, avoid nav/pathfinding diagrams, avoid crafting or economy markers, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## 7. Modeling Notes

No modeling is authorized. This document defines LOD/collision policy only and does not create DCC source, meshes, proxies, proof renders, FBX, collision, UCX, LOD source, Unreal Content, startup scenes, validators, captures, material instances, texture assets, material graphs, VFX/audio, shipped markers, or implementation targets.

Future asset packages should use this policy to keep LOD reductions ordered and collision simple, but they must author their own budgets and proxy details under separate approved implementation tasks. Review rows remain documentation aids, not startup placement or final approval scenes.

## 8. Texture and Material Notes

No texture or material assets are authorized. LOD policy should remove tiny texture-level detail before reducing primary silhouettes. Collision policy should not depend on material states or painted warnings.

This package does not create Base Color, Normal, ORM, emissive maps, material instances, texture assets, shaders, material graphs, VFX materials, or Unreal material assignments.

## 9. Triangle Budget

No shipping triangle budget applies because this is a non-shipping documentation row package and not a mesh.

Policy targets for represented future assets:

- Preserve silhouette first, then remove minor bevels, small chips, tiny ash flecks, soot speckles, bark hairlines, slag pores, small charcoal fragments, tiny nails, cloth edge nicks, underside details, and duplicate loose fragments.
- Keep LOD percentages aligned with the parent kit unless a future approved child package gives stricter budgets.
- Do not authorize geometry, LOD source, collision source, implementation targets, or shipped review rows from this document.

## 10. LOD Plan

Docs-only LOD policy rows should require:

- LOD0: complete child silhouettes, ash mound profiles, large slag lumps, charcoal top chunks, log stack forms, scorched debris beams, rare metal scraps, red cloth tags, row spacing, and broad material zones.
- LOD1: 60-70 percent of LOD0; reduce small bevels, secondary charcoal chunks, minor log-end cuts, small slag chips, cloth edge nicks, duplicate loose fragments, and backside detail.
- LOD2: 35-45 percent of LOD0; simplify mound interiors, reduce slag chunk count, merge charcoal clusters, simplify log stack overlaps, reduce debris row interiors, remove underside detail, and preserve category reads.
- LOD3: 15-25 percent of LOD0; preserve ash/slag/charcoal/wood/debris category reads, broad footprint, log-stack rhythm, dark residue mass, review-row spacing if visualized, and restrained red Blood Axe accents.

Reduction order:

1. Tiny ash flecks, soot speckles, bark hairlines, fine slag pores, tiny chips, small cracks, and minor texture-driven forms.
2. Small nails, minor ties, cloth edge nicks, fine charcoal pieces, small splinters, and non-silhouette pores.
3. Secondary slag chips, duplicate log cuts, non-silhouette debris pieces, and inner mound subdivisions.
4. Back-side or underside debris, concealed log overlaps, and non-visible ash-bank detail.
5. Secondary bevels and minor metal-scrap cuts.
6. Only after secondary details are reduced, simplify the main ash mound, slag lump, charcoal heap, firewood stack, scorched debris, review-row, or forge cluster footprint.

No LOD meshes, LOD source files, validators, captures, Unreal assets, DCC work, or final approval are created by this package.

## 11. Collision Notes

Docs-only collision policy rows should require simple display collision only if a future implementation task explicitly approves it:

- Ash piles: no collision by default, or one shallow low-count hull around the broad mound if display blocking is separately required.
- Ash drifts: collision disabled by default.
- Slag lumps and spill strips: grouped simple hulls or boxes around cluster footprints; no per-lump collision.
- Charcoal heaps and bins: one low hull or box around the heap or bin; no per-chunk collision.
- Firewood stacks and tied bundles: one to three simplified boxes or convex hulls around the stack mass; no per-log collision.
- Scorched debris and edge scatter rows: grouped hulls around the broad row footprint; no per-splinter, per-nail, per-cloth, or per-metal-scrap collision.
- Review composition rows: collision disabled by default unless a later approved review implementation task explicitly needs display collision.
- Forge clutter cluster: broad grouped display hulls only if separately approved; no merged gameplay blocker.
- Walkable collision disabled by default for all represented pieces.

Reject pickup collision, gatherable collision, harvest volumes, resource triggers, loot outlines, crafting interaction volumes, economy triggers, heat damage volumes, burn hazard volumes, damage volumes, VFX collision, destructible fracture collision, physics-simulated logs, per-log collision, per-lump collision, per-charcoal collision, navmesh rules, nav blockers, cover volumes, encounter hazard volumes, gameplay volumes, collision proxies, UCX files, validators, and startup placement collision.

## 12. Animation Notes

No animation is authored. LOD/collision rows are static policy references only and do not define physics, falling logs, rolling charcoal, shifting ash, destructible burning debris, wind movement, smoke, embers, sparks, active flames, heat shimmer, ash drift, VFX/audio, material-state timing, NPC routines, interaction prompts, resource behavior, or startup behavior.

## 13. Unreal Import Notes

No Unreal import is authorized. This is not a Static Mesh, Blueprint Actor, Material Instance, texture asset, material graph, Niagara system, validator, capture setup, collision proxy asset, UCX file, startup actor, shipped LOD board, shipped collision board, or shipped review asset.

Future implementation must create its own LOD and collision assets under a separate approved task. This package only records policy and does not select a first DCC target, implementation order, final visual approval, shipped marker approval, or implementation target.

## 14. Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/DOC_GIA_BloodAxeAshSlagFirewoodLODAndCollision_A01/`
- Production package: `docs/assets/kits/DOC_GIA_BloodAxeAshSlagFirewoodLODAndCollision_A01/PRODUCTION_PACKAGE.md`
- Review document code: `DOC_GIA_BloodAxeAshSlagFirewoodLODAndCollision_A01`
- Related parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, Hermes files or configuration, global indexes, task board updates, material instances, texture assets, material graphs, VFX/audio, collision proxy files, UCX files, nav blockers, gameplay volumes, startup scene files, shipped markers, or shipping assets from this package.

## 15. Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Is clearly docs-only, non-shipping, and policy-only.
- Remains no-DCC/no-FBX/no-Unreal/no-startup/no-nav/no-nav-blocker/no-encounter/no-workstation/no-loot/no-resource/no-material-instance/no-texture-asset/no-material-graph/no-VFX/audio/no-collision-proxy/no-UCX/no-gameplay-volume/no-validator/no-capture/no-final-approval/no-implementation-target.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Defines docs-only LOD0-LOD3 policy for ash, slag, charcoal, firewood, scorched debris, review rows, and forge clutter cluster.
- Defines simple display collision policy without creating UCX files, collision proxies, validators, nav blockers, gameplay volumes, Unreal actors, or shipped assets.
- Rejects per-log, per-lump, per-charcoal, per-splinter, pickup, resource, heat, damage, nav, cover, and encounter collision overclaims.
- Does not claim meshes, textures, material instances, captures, runtime behavior, final approval, shipped marker approval, or first DCC target selection.
