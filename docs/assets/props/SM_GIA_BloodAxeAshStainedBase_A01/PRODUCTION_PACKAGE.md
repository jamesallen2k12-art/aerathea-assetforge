# SM_GIA_BloodAxeAshStainedBase_A01 Production Package

## 1. Art Direction Summary

- Task ID: `AET-MA-20260629-364`
- Asset name: `SM_GIA_BloodAxeAshStainedBase_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Child intake row: `BloodAxeStronghold.png#PathMarkers_AshBase_A01`
- Related packages: `SM_GIA_BloodAxeCairnPathMarker_A01`, `SM_GIA_BloodAxeClothStakeMarker_A01`, `SM_GIA_BloodAxeBoneHornPathMarker_A01`, `SM_GIA_BloodAxeHornForkMarker_A01`, `SM_GIA_BloodAxeCairnScrapCap_A01`, and `SM_GIA_BloodAxeLowRedRagMarker_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Role: low ash, soot, charcoal, and trampled mud base for grounding cairns and stakes
- Package status: docs-only production specification for one static ground-dressing prop

`SM_GIA_BloodAxeAshStainedBase_A01` is a shallow Blood Axe ground base that visually seats cairns, cloth stakes, horn markers, and rough path-warning props into hostile Giant camp terrain. It should read as low, matte, dirty residue: cold ash, soot, broken charcoal, packed earth, and trampled mud pressed down by Giant movement and crude camp activity.

Blood Axe visual language must stay separate from neutral/civilized Giant culture. This asset belongs to the hostile Blood Axe sub-faction only and must not become the default Giant ground language, cave-town paving, refined highland trail marker, civic stoneworker residue, warm hearth settlement dressing, blue-gray terrace material, or restrained blue-rune culture package.

This package is planning only. It does not authorize source creation, sculpting, retopology, UVs, baking, collision proxy authoring, proof renders, export files, engine content, material instance creation, texture asset creation, runtime source, Blueprint work, startup placement, final visual approval, implementation target selection, Hermes files, or Hermes configuration work.

## 2. Gameplay Purpose

The gameplay purpose is static visual grounding only. The base supports environmental readability by making Blood Axe path-marker props feel pressed into rough camp terrain, but it must remain subordinate to the cairn or stake it grounds.

Allowed purpose:

- Visually anchor a crude cairn, cloth stake, horn marker, shield scrap, or low red rag into ash-darkened camp ground.
- Break up broad packed-earth surfaces with matte soot, charcoal, trampled mud, and dirty ash variation.
- Reinforce hostile Giant scale through broad, heavy scuffing and compacted ground contact.
- Provide a shared visual base language for Blood Axe path-marker siblings without turning into a readable trail.
- Keep the marker family visually distinct from neutral/civilized Giant settlement culture.

Out of scope:

- No decal gameplay, trail tracking, footprints-as-tracking, waypoint behavior, breadcrumb behavior, objective pathing, nav/pathfinding behavior, route validation, gatherable ash, resource node, harvesting, pickup/loot behavior, crafting/economy behavior, salvage behavior, interaction prompt, damage field, hazard field, aura field, combat modifier, AI marker, patrol marker, spawn marker, encounter scripting, VFX, smoke, ash drift, audio cue, material-state behavior, startup placement, runtime behavior, final approval, or implementation target selection.

## 3. Silhouette Notes

Primary silhouette:

- Very low, irregular ash-and-mud base with broken edges and a compressed central contact area.
- Broad, lopsided footprint that can sit under or beside cairns and stakes without reading as a path stripe, arrow, ring, symbol, or UI mark.
- Slight raised mud lips, ash ridges, and charcoal clusters may shape the edge, but the asset should remain ground-hugging.
- The center should feel trampled and pressed flat by Giant-scale movement, dragged stones, and repeated camp use.
- Soot should darken contact points near the marker base, with ash feathering outward into packed earth.
- Charcoal pieces should be sparse and chunky enough to read as broad residue, not a dense debris pile.

Model as major forms in any later approved source task:

- Main irregular base footprint, broad mud lips, shallow ash ridges, larger charcoal fragments, embedded stone grit, and marker-contact depressions.

Keep as texture, normal, or baked detail in any later approved material task:

- Fine ash flecks, soot speckles, dust gradients, tiny grit, small mud cracks, charcoal pitting, minor scuffs, dried mud streaks, and small embedded pebbles.

Avoid:

- Clean circular pads, route lines, dotted trails, repeated footprints, readable symbols, arrows, bright color coding, active fire, smoke plumes, glowing embers, magic stains, polished civic stone, refined paving, blue rune residue, warm hearth cues, dense trophy clutter, or graphic gore.

## 4. Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant range: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft / 452-488 cm.
- Any later source task should author in centimeters with 1 engine unit = 1 cm.

Planning dimensions:

- Compact marker base: 180-320 cm long by 120-260 cm wide.
- Standard cairn or stake base: 320-560 cm long by 220-420 cm wide.
- Wide grounding base for a larger marker cluster: 560-780 cm long by 320-580 cm wide.
- Surface height: 0-8 cm for most ash, soot, and pressed mud.
- Raised mud lips or ash ridges: 8-24 cm high only where needed for silhouette and contact shadow.
- Larger charcoal or embedded stone pieces: 5-22 cm high and sparse.
- Marker-contact depression: broad and shallow; it should imply weight without becoming a socket, gameplay locator, or placement guarantee.

These values are visual planning dimensions only. They are not route widths, navigation values, traversal guarantees, collision claims, tracking radii, damage radii, gatherable-resource bounds, VFX bounds, camera requirements, terrain-integration proof, placement approval, or implementation approval.

## 5. Materials and Color Palette

Primary materials:

- Cold ash, soot, charcoal, trampled mud, packed earth, burned grass residue, rough stone dust, blackened grit, and sparse dirty oxide-red contamination.
- Optional low rope fiber or cloth residue may appear as ground-level contamination only if it stays visually secondary to ash and mud.
- No polished stone, refined civic material, readable carving, metal hardware focus, magic glow, or active fire material is part of the default asset.

Palette targets:

- Cold ash: `#5B5850`, `#716B61`, `#8B8376`
- Soot and charcoal: `#0D0E0E`, `#181A19`, `#272928`
- Trampled mud: `#211811`, `#35271C`, `#4C3929`
- Packed earth: `#3D2F24`, `#594534`, `#70573F`
- Rough grit and stone dust: `#302F2C`, `#4B4740`, `#676157`
- Burned grass residue: `#3F3D2B`, `#56543A`, `#746E50`
- Restrained Blood Axe contamination: `#4F1410`, `#681B16`, `#7D241D`

Material discipline:

- Keep the surface matte, dusty, rough, and cold.
- Use ash and soot value contrast to support readability instead of bright color coding.
- Oxide red must remain dirty, weak, and non-symbolic if used.
- No default emissive, heat pulse, smoke, ash drift, glow, animated material state, magic stain, signal color, UI highlight, or gameplay-readable material state is approved.
- Do not borrow neutral/civilized Giant blue-gray masonry, cave-town carving, terrace or waterwork motifs, warm hearth language, refined highland guide marks, civic stoneworker symbols, or restrained blue runes.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG static prop concept sheet of `SM_GIA_BloodAxeAshStainedBase_A01` for the world of Aerathea. The design should emphasize a very low irregular ash-stained ground base for Blood Axe Giant path markers, cold ash, soot, charcoal, trampled mud, packed earth, broad Giant-scale compression, broken feathered edges, shallow marker-contact depressions, sparse chunky charcoal fragments, hostile Blood Axe Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and the gameplay role of static non-interactive visual grounding for cairns and stakes. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a single prop production sheet with top-down outline views, low three-quarter view, side relief profile, material swatches, LOD/collision callouts, and scale references beside a female 442 cm Giant and a male 470 cm Giant from `SK_GIA_Base_A01` on a clean background. Avoid copying any existing franchise, avoid clean circles, avoid arrows, avoid route lines, avoid footprints or tracking marks, avoid decal gameplay, avoid trail tracking, avoid gatherable ash, avoid damage fields, avoid VFX, avoid material-state behavior, avoid active fire or smoke, avoid readable text or symbols, avoid DCC or engine approval claims, avoid startup placement, avoid final approval, avoid implementation target language, avoid Hermes work, avoid neutral/civilized Giant cave-town materials, and avoid excessive micro-detail that would not translate to a mid-poly static prop.

## 7. Modeling Notes

This is a docs-only modeling handoff. It creates no source mesh, sculpt, retopo, UVs, bake, proof render, LOD source, collision proxy, exported asset, engine content, material instance, texture asset, material graph, validator, runtime source, visual signoff, build-order decision, Hermes file, or implementation target.

Future source-planning priorities after separate approval:

- Build a shallow uneven ground mass, not a flat graphic symbol.
- Shape the footprint with three to seven broad broken lobes that can sit naturally beneath cairns or stakes.
- Keep the middle compressed and slightly darker to imply weight, soot, and trampling.
- Use broad mud lips and ash ridges only where they help the outline or contact shadow.
- Add a few larger charcoal pieces or embedded stone chips at the edges; avoid dense scatter.
- Keep optional dirty red residue as low contamination caught in ash or mud, not a painted marker.
- Maintain a ground-centered pivot concept so the future asset can be placed under marker props without scale reinterpretation.
- Author rotation and scale variation from the same base concept instead of multiplying unique micro-detail.

Suggested future mesh groups:

- `AshStainedBase_MainPad`
- `AshStainedBase_MudLips`
- `AshStainedBase_AshRidges`
- `AshStainedBase_CharcoalChunks`
- `AshStainedBase_ContactDepression`

Geometry treatment:

- Real geometry only for the broad footprint, shallow relief, major mud lips, major ash ridges, larger charcoal chunks, and readable embedded stones.
- Texture or normal detail for ash dust, soot speckles, fine grit, small cracks, dried mud streaks, charcoal pores, minor scuffs, and surface feathering.

Do not add sockets, attachment points, waypoint helpers, trail helpers, navigation helpers, VFX locators, audio locators, interaction affordances, pickup affordances, resource-node markers, damage volumes, aura volumes, objective volumes, gameplay collision, material-state hooks, or implementation-specific files.

## 8. Texture and Material Notes

Material target:

- 1 material slot for the default asset.
- 512-1K texture set for repeated ground dressing.
- 1K preferred if used under close-view cairns or stakes in a later approved art task.
- 2K is not required for this single low base unless a later lead-approved close-review use case changes scope.
- No emissive texture is part of the baseline.

Required map plan for a future approved texture task:

- `T_GIA_BloodAxeAshStainedBase_A01_BC`
- `T_GIA_BloodAxeAshStainedBase_A01_N`
- `T_GIA_BloodAxeAshStainedBase_A01_ORM`

No emissive texture is planned:

- Do not create `T_GIA_BloodAxeAshStainedBase_A01_E` for the default asset.
- Any active, glowing, ritual, signal, shamanic, magic, heat, smoke, ash-drift, or gameplay-readable variant must be split into a separately approved package.

Base Color plan:

- Hand-painted ash value shifts from light gray-beige to charcoal black.
- Mud should read warmer and darker than ash, with packed-earth transitions at the perimeter.
- Charcoal chunks should stay dark and matte without ember color.
- Optional dirty oxide-red contamination must be broad, faded, and non-symbolic.

Normal plan:

- Shallow ash ridges, broad mud ripples, compacted center depression, embedded stone edges, charcoal lump shape, and soft perimeter buildup.
- Keep surface noise controlled so the prop does not shimmer or clutter at MMO camera distance.

Packed ORM plan:

- R: Ambient occlusion in mud lips, charcoal contacts, embedded grit, and compressed marker-contact depressions.
- G: High roughness for ash, soot, charcoal, mud, packed earth, burned grass residue, and grit.
- B: Metallic should remain black.

Do not paint arrows, path stripes, repeated footprints, tracking marks, readable travel instructions, objective rings, UI-like symbols, readable text, glowing stains, damage-field borders, gatherable-resource highlights, or material-state indicators into textures.

## 9. Triangle Budget

Target as a small-to-medium low static ground prop:

- Compact LOD0: 150-600 tris, 1 material.
- Standard LOD0: 400-1,200 tris, 1 material.
- Wide LOD0: 900-2,200 tris, 1 material.
- LOD1: 50-65 percent of LOD0.
- LOD2: 25-40 percent of LOD0.
- LOD3: 10-20 percent of LOD0.
- Texture budget: 512-1K BC/N/ORM.

Budget priorities:

- Spend triangles on the non-circular footprint, shallow relief, broad mud lips, larger ash ridges, compressed center, major charcoal chunks, and readable perimeter.
- Do not spend triangles on ash grains, soot dots, tiny grit, fine cracks, small mud streaks, many tiny pebbles, grass fibers, charcoal pores, or hidden underside faces.
- If later combined with path-marker clusters, favor instancing, shared materials, and aggressive LOD reduction over unique high-density variants.

## 10. LOD Plan

All future important static mesh use requires LOD0, LOD1, LOD2, and LOD3 before shipping use.

- LOD0: full irregular ash/mud footprint, shallow center compression, major mud lips, ash ridges, sparse charcoal chunks, embedded stone/grit reads, and dirty perimeter transitions.
- LOD1: reduce minor perimeter cuts, simplify small ridge loops, remove tiny charcoal geometry, flatten subtle relief, and rely more on normal detail.
- LOD2: preserve the broad non-circular base shape, central dark contact read, and largest mud/ash value breaks while merging secondary ridges into the base.
- LOD3: preserve only the low irregular footprint and strongest broad value shape; remove all small chunks and most relief.

Reduction order:

1. Fine ash flecks, soot speckles, grit dots, charcoal pores, tiny cracks, and small mud streaks.
2. Minor edge wobble, small embedded pebbles, tiny charcoal pieces, and secondary residue tears.
3. Secondary ash ridges, small scuff geometry, underside cuts, and back-facing bevels.
4. Embedded stones or charcoal pieces that do not affect the main outline.
5. Mud lip density and broad mound subdivisions.
6. Main irregular footprint only after smaller details are already removed.

Never collapse the asset into a clean circle, ring, arrow, dotted route, repeated footprint chain, readable tracking mark, or gameplay-readable border.

## 11. Collision Notes

This package creates no collision asset, collision proxy, physics body, blocking setup, gameplay volume, navigation helper, validator, runtime setup, startup placement, or collision correctness claim.

Default future collision intent after separate approval:

- Collision disabled.
- Ash, soot, charcoal dust, mud, packed earth, burned grass residue, and small grit: no blocking.
- Larger charcoal chunks or embedded stones: no blocking by default because the asset is ground dressing.
- If a later placement owner requires contact handling, use only the parent cairn or stake collision; this base should remain visually supportive.

Explicitly out of scope:

- No waypoint collision, trail-marker collision, objective volume, nav/pathfinding helper, pickup collision, loot collision, gatherable-resource collision, interaction collision, destructible collision, physics collision, combat cover collision, AI marker collision, spawn logic volume, aura volume, damage volume, hazard field, VFX bounds, or startup placement collision.

This document does not verify traversal, navigation, terrain blending, camera clearance, runtime performance, or in-world placement.

## 12. Animation Notes

The asset is static.

Approved animation scope:

- None.

Not approved here:

- No skeletal setup, vertex animation, ash drift, smoke, fire, ember pulse, heat haze, dust plume, wind motion, physics movement, mud deformation, material animation, material-state behavior, VFX, audio cue, interaction state, pickup state, resource state, damage state, aura state, objective state, waypoint behavior, breadcrumb behavior, tracking behavior, route behavior, runtime behavior, startup placement, final approval, or implementation target selection.

Any active, glowing, moving, audio-linked, VFX-linked, interactive, damaging, aura-emitting, resource-readable, objective-readable, route-readable, tracking-readable, or gameplay-readable variant must be split into a separately named and separately approved package.

## 13. Unreal Import Notes

This required universal-format section records guardrails only. It does not perform or authorize engine work, import scripts, engine content, material instance creation, texture import, socket work, Blueprint work, validator work, runtime source work, review actor creation, startup placement, final visual approval, or implementation target selection.

Future import constraints if a separate implementation task is approved:

- Asset name: `SM_GIA_BloodAxeAshStainedBase_A01`
- Asset type: Static Mesh prop
- Authorized engine folder for this task: none; no game-content path is selected or created by this package.
- Pivot: ground center of the irregular footprint.
- Orientation: non-directional by default; strongest value gradient may face +X only if a later approved source task needs a primary read.
- Scale: centimeter-authored source, import scale 1.0, preserving the 442 cm female Giant and 470 cm male Giant baselines for review comparison.
- Collision type: disabled.
- LODs: LOD0-LOD3 required before any later shipping use.
- Material slot count: 1.
- Texture list: `T_GIA_BloodAxeAshStainedBase_A01_BC`, `T_GIA_BloodAxeAshStainedBase_A01_N`, `T_GIA_BloodAxeAshStainedBase_A01_ORM`.
- Emissive texture: none.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: keep the prop shallow, matte, low-cost, collisionless, texture-led, and reusable under sibling path-marker props.

Do not add decal gameplay, trail tracking, gatherable ash, damage fields, hazard fields, VFX/audio components, material-state behavior, navigation behavior, objective behavior, interaction prompts, pickup components, resource components, startup placement, source folders, export files, engine assets, implementation target choices, Hermes files, or Hermes configuration from this package.

## 14. Folder and Naming Recommendation

Allowed documentation path for this task:

- `docs/assets/props/SM_GIA_BloodAxeAshStainedBase_A01/PRODUCTION_PACKAGE.md`

Reserved asset naming after separate approval only:

- `SM_GIA_BloodAxeAshStainedBase_A01`
- `MI_GIA_BloodAxeAshStainedBase_A01`
- `T_GIA_BloodAxeAshStainedBase_A01_BC`
- `T_GIA_BloodAxeAshStainedBase_A01_N`
- `T_GIA_BloodAxeAshStainedBase_A01_ORM`

No source folder, export folder, game-content folder, material file, texture file, validator, global index edit, backlog edit, task-board edit, external concept copy, runtime file, startup file, Hermes file, or unrelated package file is created or authorized by this docs-only task.

## 15. Quality Gate Checklist

- Required 15 package headings are present in order.
- Package is docs-only and limited to `docs/assets/props/SM_GIA_BloodAxeAshStainedBase_A01/PRODUCTION_PACKAGE.md`.
- Asset remains a low static ash, soot, charcoal, trampled mud, packed earth, and burned-residue base for grounding cairns and stakes.
- Giant scale lock is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- Approved Giant ranges are explicit: females 14-15 ft and males 14 ft 10 in-16 ft.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Materials stay matte and restrained: cold ash, soot, charcoal, trampled mud, packed earth, grit, burned grass residue, and dirty oxide-red contamination.
- Silhouette remains low, irregular, broken-edged, non-circular, non-directional, and subordinate to the cairn or stake it grounds.
- No decal gameplay, trail tracking, footprints-as-tracking, waypoint behavior, objective pathing, route validation, nav/pathfinding behavior, gatherable ash, pickup/loot behavior, resource behavior, damage field, hazard field, aura field, VFX, smoke, ash drift, audio cue, material-state behavior, gameplay behavior, interaction behavior, collision claim, traversal proof, terrain integration claim, source asset creation, engine content, startup placement, runtime source, validator, final approval, implementation target, Hermes work, or build-order selection is defined.
- Default emissive, active fire, smoke, glowing embers, route lines, UI-like markers, readable text, polished civic Giant language, warm hearth identity, blue-gray cave-town masonry, refined highland guide marks, terrace/waterwork motifs, and restrained blue-rune language are absent.
- Fine ash flecks, soot speckles, grit, mud streaks, grass residue, charcoal pores, small cracks, tiny chips, and minor scuffs are assigned to textures or normals in future packages.
- LOD0-LOD3 planning, triangle budgets, collision limits, animation limits, guardrailed import notes, folder naming, and stop gates are included.
