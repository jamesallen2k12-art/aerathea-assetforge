# SM_GIA_BloodAxePaintedThresholdStone_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxePaintedThresholdStone_A01`
- Asset type: Static Mesh prop production package, docs-only
- Task: `AET-MA-20260629-223`
- Parent package: `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- Source child row: `BloodAxeCaveApproachMarkers_A01#RedClothThresholdMarker_PaintOnly_A01`
- Related package: `SM_GIA_BloodAxeRedClothThresholdMarker_A01`
- Related material policy: `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: planning package only. No source asset, DCC work, FBX export, game-engine asset, texture asset, material instance, material graph, VFX, audio, runtime source, startup placement, first implementation target, cave signoff, final Blood Axe signoff, or final visual signoff is created or claimed.

`SM_GIA_BloodAxePaintedThresholdStone_A01` defines a rough static threshold stone with chipped dirty red paint used instead of cloth. It is the paint-only companion to the red cloth marker: a colder, heavier, texture-led warning beat for Blood Axe cave approaches where more fabric would create too much red density.

The primary read is a chunky highland stone with old soot, ash, mud, and non-readable dirty red paint wear. The paint must never become readable text, a UI arrow, a quest symbol, a magic glyph, a route mark, or an objective cue. Blood Axe raider language stays hostile and crude, while neutral/civilized Giant culture remains separate with skilled stonework, blue-gray civic masonry, terraces, waterworks, warm hearth language, and restrained civic rune identity.

## Gameplay Purpose

The purpose is visual production planning only. The marker supports static threshold readability near Blood Axe cave approaches, abandoned shelter edges, low cairns, broken slabs, and paired standing stones without defining route behavior, interaction, objective logic, UI, VFX, audio, or final cave approval.

Allowed planning uses:

- Provide a paint-only Blood Axe threshold accent where a cloth strip would be too loud, too clean, or too repeated.
- Add a hostile Giant sub-faction warning beat through rough stone, dirty red pigment, soot, ash, and mud.
- Reinforce cave-edge dressing while staying static, non-interactive, and non-gameplay.
- Preserve separation between Blood Axe raider language and neutral/civilized Giant culture.
- Give later art, modeling, texture, LOD, collision, and import-planning owners enough constraints without creating implementation evidence.

Out of scope:

- Not approved here: readable text, UI arrows, quest symbols, objective symbols, magic glyphs, route labels, sign behavior, interaction prompts, encounter triggers, nav/pathfinding, traversal proof, collision correctness, cave gameplay, material graph authoring, emissive maps, VFX, audio, DCC source, FBX export, game-engine content, runtime source, startup placement, first implementation target selection, final cave approval, or final visual approval.

## Silhouette Notes

- Primary silhouette: one squat-to-mid-height rough threshold stone with an uneven broken crest, broad chipped planes, and a heavy base that feels sized for Giant territory.
- The default `A01` read should be a single freestanding stone, not a paired gate, standing-stone frame, banner pole, cloth marker, route sign, map pin, or objective frame.
- The stone may lean slightly or have a broken shoulder, but it must remain stable and static rather than suggesting collapse, destruction, puzzle interaction, or physics behavior.
- Paint is a surface read only: broad irregular dirty red smears, chipped bands, hand-dragged blocks, and worn patches that break across stone chips.
- Paint shapes must be non-linguistic and non-directional. Avoid straight arrowheads, readable letters, route chevrons, quest icons, magic glyph panels, clan text, or UI-like symbol clusters.
- The bottom should carry soot, cold ash, cave grit, and mud staining, with broad contact shadows that make the stone feel settled into a cave approach.
- No cloth strips, draped fabric, knots, tassels, wind flags, or banner silhouettes belong to this paint-only variant.
- Future geometry, if separately approved, should model the main stone mass, large broken planes, major chips, ground-contact bevels, and any large fracture that affects silhouette.
- Keep stone pitting, tiny cracks, soot speckles, ash flecks, mud droplets, lichen flecks, paint chips, worn pigment edges, and small scratches in future texture, normal, AO, roughness, or mask work.
- Avoid neutral/civilized Giant cues: no refined civic carving, terrace or waterwork motifs, warm settlement marks, blue-gray mason symbols, restrained blue rune inlays, or peaceful wayfinding language.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Future source, if separately approved, should be authored in centimeters with 1 Unreal unit = 1 cm.

Visual planning dimensions:

- Stone height: 130-300 cm.
- Stone width: 90-230 cm.
- Stone depth: 55-150 cm.
- Ground footprint: 110-280 cm wide and 80-190 cm deep.
- Painted dirty red zone: 45-170 cm across, kept broken and irregular rather than icon-like.
- Major chipped planes: 25-90 cm across so the form reads beside Giant baselines.
- Soot, ash, and mud base spread: 40-160 cm around the contact edge as visual grounding only.

The marker should feel oversized for normal humanoids and believable beside female 442 cm and male 470 cm Giants. It should remain smaller than a paired standing-stone kit, cave gate, threshold arch, or cave remnant cluster. These dimensions are visual planning values only, not path widths, encounter spacing, nav values, trigger sizes, interaction ranges, camera approval, collision correctness, or terrain-fit proof.

## Materials and Color Palette

Primary materials:

- Rough highland stone, weathered granite, dark slate, cave-edge field rock, and ash-stained slab surfaces.
- Chipped dirty red paint, oxide pigment, faded maroon hand-smears, soot-darkened red patches, and worn pigment caught on stone edges.
- Cold ash, charcoal dust, soot, cave grit, trampled mud, mineral dust, and dark ground-contact staining.
- Sparse muted lichen, rubbed edge wear, and small mineral streaks as texture-level breakup only.

Palette targets are planning values, not final color approval:

- Deep stone and soot: `#151718`, `#222527`, `#343635`, `#4E4D47`
- Weathered stone and ash: `#67645E`, `#827B70`, `#A49B8E`, `#C0B5A3`
- Cave grit and trampled mud: `#241D17`, `#382C22`, `#554332`, `#6F5B45`
- Chipped dirty red paint: `#551311`, `#6B1A16`, `#81251D`, `#98372B`
- Muted lichen and mineral hints: `#4B5641`, `#657057`, `#8A867B`

Material restraint:

- Stone, soot, ash, grit, and mud should carry roughly 85-95 percent of the visual read.
- Dirty red paint should stay around 5-10 percent of the composition as a Blood Axe warning accent.
- No cloth material is part of this variant.
- No emissive map is part of this package. No glow, ritual light, shamanic pulse, torch response, route highlight, objective highlight, or animated material state belongs to the baseline.
- Avoid neutral/civilized Giant materials as the default read: no refined blue-gray civic masonry, terrace or waterwork symbols, warm hearth stone, peaceful highland guide marks, civic mason marks, or restrained blue rune language.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxePaintedThresholdStone_A01` for the world of Aerathea. The design should emphasize a rough static Giant-scale threshold stone, chunky chipped highland rock, dirty red chipped paint used instead of cloth, soot-blackened recesses, cold ash, cave grit, trampled mud, non-readable irregular pigment wear, hostile Blood Axe Giant sub-faction identity, strict separation from neutral/civilized Giant culture, grim cave-approach mood, and the gameplay role of static visual threshold dressing only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh prop concept sheet with front, side, back, and three-quarter views, paint-wear callouts, material swatches, LOD and collision planning notes, and scale markers beside a female 442 cm Giant and a male 470 cm Giant on a clean background. Avoid copying any existing franchise, avoid readable text, avoid UI arrows, avoid quest symbols, avoid objective symbols, avoid magic glyphs, avoid route signs, avoid cloth strips, avoid flag animation, avoid VFX or audio cues, avoid material graph diagrams, avoid DCC or FBX claims, avoid game-engine implementation claims, avoid startup placement, avoid final visual approval language, avoid neutral Giant cave-town symbols as Blood Axe default language, avoid magic glow, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly game asset.

## Modeling Notes

This is a docs-only modeling plan. No source folder, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, game-engine asset, material instance, texture asset, material graph, validator, runtime source, Blueprint, socket, animation, startup placement, implementation target, cave signoff, or final visual signoff is created or authorized.

Future modeling priorities, if separately approved:

- Build the marker as one static stone prop with a single dominant threshold read.
- Use broad asymmetrical rock planes, a chipped top edge, a heavy grounded base, and a few large fracture cuts that affect silhouette.
- Keep the paint flat to the stone surface. Do not model paint as raised glyphs, carved channels, sign plates, decals with gameplay meaning, or separate symbol meshes.
- Shape large chips, broken shoulders, contact bevels, and ground-settle planes in geometry only where they improve MMO camera readability.
- Keep the backside simpler but believable, with fewer chips and less paint so the front read remains clear.
- Use broad soot and ash contact zones as surface material planning unless a later ground-dressing package owns a base mesh.
- Avoid cloth strips, rope knots, banners, signposts, arrows, readable carved marks, dense crack networks, tiny pebble fields, graphic trophies, or hidden underside detail.

Use future textures, normals, AO, roughness, or masks for:

- Stone pitting, fine cracks, chipped paint edges, worn pigment grain, soot speckles, ash flecks, mud droplets, mineral streaks, muted lichen, small scratches, and minor dents.

## Texture and Material Notes

Target material strategy for future source work:

- Default material count: 1 shared stone-and-paint material.
- Maximum material count: 1 for this `A01` variant unless a later approved package adds a separate base composition.
- Default texture resolution: 1K BC/N/ORM.
- 2K is acceptable only if a later task promotes the marker to close-view hero cave dressing.
- No emissive map.

Required future texture names, planning only:

- `T_GIA_BloodAxePaintedThresholdStone_A01_BC`
- `T_GIA_BloodAxePaintedThresholdStone_A01_N`
- `T_GIA_BloodAxePaintedThresholdStone_A01_ORM`

Texture guidance:

- Base Color should carry dark stone value groups, dirty red paint breakup, soot darkening, ash dust, trampled mud stains, lichen hints, and worn mineral streaks.
- Normal should carry broad chipped stone planes, shallow pitting, cracked stone edges, worn paint breakup, and small surface dents.
- ORM should emphasize occlusion in fractures, base contact, chipped edges, soot-darkened recesses, ash deposits, and mud undercuts.
- Roughness should stay high across stone, soot, ash, mud, and old pigment. Dirty red paint should be matte, dry, and chipped.
- Metallic should remain zero.
- Any mask labels for paint wear, soot, ash, mud, or lichen are planning vocabulary only and do not authorize texture asset creation or material graph authoring.
- Do not assign unique materials to individual paint chips, cracks, soot patches, ash deposits, mud flecks, lichen specks, stone planes, or worn edges.

## Triangle Budget

- Target category: small to medium static prop.
- LOD0 target: 1.2k-4k tris.
- LOD0 upper limit: 5.5k tris only if the stone uses a larger broken base and several silhouette-driving chipped planes.
- LOD1 target: 600-2.2k tris.
- LOD2 target: 250-900 tris.
- LOD3 target: 80-300 tris.
- Material budget: 1 material.
- Texture budget: 1K BC/N/ORM by default; 2K only for separately approved close-view use.

Suggested LOD0 allocation:

- Main stone mass, broad planes, chipped crest, and major silhouette breaks: 70-82 percent.
- Ground-contact bevels, large fractures, and base-settle forms: 12-22 percent.
- Optional low base lip or embedded foot shape: 0-8 percent.

Do not spend geometry on painted shapes, paint chips, stone pores, tiny cracks, soot speckles, ash flecks, mud droplets, lichen, mineral streaks, or small scratches.

## LOD Plan

All future important static meshes require LOD0, LOD1, LOD2, and LOD3 before any shipping use.

- LOD0: full stone silhouette, broken crest, major chipped planes, large base contact, dirty red paint read through texture, soot/ash/mud grounding, and front/back readability.
- LOD1: 55-70 percent of LOD0; reduce secondary chips, small bevels, backside cuts, base undercuts, and non-silhouette fracture subdivisions while preserving the painted threshold read.
- LOD2: 30-45 percent of LOD0; merge stone planes, flatten small chips, simplify the broken crest, reduce base geometry, and keep the broad stone mass plus dirty red paint zone readable.
- LOD3: 12-25 percent of LOD0; preserve only the main stone block, asymmetrical top, grounded base, and broad paint/value read.

Reduction order:

1. Stone pores, fine cracks, paint chips, soot speckles, ash flecks, mud droplets, lichen, mineral streaks, and small scratches.
2. Tiny chipped cuts, minor bevels, shallow non-silhouette cracks, and little base nicks.
3. Back-facing fractures, underside cuts, buried contact undercuts, and hidden base detail.
4. Secondary rock-plane subdivisions and minor crest breaks.
5. Large bevel density and base-settle geometry.
6. Only after small detail is removed, simplify the primary stone silhouette and broad painted threshold read.

Never reduce Giant-scale readability, the Blood Axe dirty red warning accent, or the static threshold-stone silhouette before removing small detail.

## Collision Notes

Collision is planning only. Do not create collision proxies, UCX meshes, game-engine collision settings, physics bodies, nav blockers, smart links, gameplay volumes, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, or runtime setup from this package.

Future static collision intent, if separately approved:

- Default: collision disabled for review or decorative placement.
- Optional: one simple low-count convex hull around the main stone body only if a later environment owner explicitly requires basic blocking.
- No collision for paint, soot, ash, mud, lichen, cracks, chips, mineral streaks, or surface wear.
- No pathfinding helper, route blocker, cave compatibility proof, terrain integration proof, objective zone, interaction volume, or encounter trigger.

This package makes no claim of collision correctness, cave compatibility, terrain fit, route clearance, player movement validity, camera clearance, objective-zone behavior, interaction behavior, or runtime performance validation.

## Animation Notes

- Baseline asset is static.
- Stone, paint, soot, ash, mud, lichen, chips, and worn pigment should be fixed surface reads if later approved.
- Static material variation for paint wear, soot, ash, mud, stone value, and lichen may be planned only as non-runtime surface variation.
- No cloth simulation, wind animation, vertex sway, physics bodies, destructible breakage, collapse state, material pulse, glow, particle effect, VFX, audio, Blueprint state, interaction state, quest state, objective state, UI state, damage state, aura state, or gameplay state change.
- Any moving, glowing, audio-linked, interactive, objective-readable, UI-readable, or gameplay-readable variant must be split into a separately named later-scope package.

## Unreal Import Notes

This section is future guardrail planning only. No game-engine asset, game folder, import script, material instance, texture asset, socket, Blueprint, validator, runtime source, review actor, startup actor, source asset, DCC work, FBX export, cave placement, collision setup, nav setup, trigger setup, objective setup, quest/UI setup, interaction setup, material graph work, VFX, audio, or first implementation target is created or authorized.

Potential future identity after separate approval:

- Asset name: `SM_GIA_BloodAxePaintedThresholdStone_A01`
- Asset type: Static Mesh
- Potential future folder: candidate only, not selected by this docs-only package.
- Naming convention: `SM_GIA_BloodAxePaintedThresholdStone_A01`, `MI_GIA_BloodAxePaintedThresholdStone_A01`, `T_GIA_BloodAxePaintedThresholdStone_A01_BC`, `T_GIA_BloodAxePaintedThresholdStone_A01_N`, `T_GIA_BloodAxePaintedThresholdStone_A01_ORM`
- Pivot: ground center of the stone footprint if a later source task approves authoring.
- Orientation: strongest painted stone face should face +X unless a later export task confirms a different project convention.
- Scale: centimeter-authored source at scale 1.0 only in a later approved implementation lane, matching the female 442 cm and male 470 cm Giant baselines without changing the Giant scale lock.
- Collision type: disabled by default; optional single simple hull around the stone body only if separately approved.
- LOD plan: LOD0-LOD3 required before any shipping use.
- Material slot count: 1.
- Texture list: `T_GIA_BloodAxePaintedThresholdStone_A01_BC`, `T_GIA_BloodAxePaintedThresholdStone_A01_N`, and `T_GIA_BloodAxePaintedThresholdStone_A01_ORM`.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: one material, texture-led paint, no cloth geometry, no default emissive, simple optional collision only, and aggressive LOD reduction that preserves the main threshold silhouette.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxePaintedThresholdStone_A01/PRODUCTION_PACKAGE.md`

Future asset naming references, for planning only:

- Static mesh: `SM_GIA_BloodAxePaintedThresholdStone_A01`
- Material instance: `MI_GIA_BloodAxePaintedThresholdStone_A01`
- Base color: `T_GIA_BloodAxePaintedThresholdStone_A01_BC`
- Normal: `T_GIA_BloodAxePaintedThresholdStone_A01_N`
- ORM: `T_GIA_BloodAxePaintedThresholdStone_A01_ORM`

Related planning references:

- Parent kit: `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachMarkers_A01/`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachMarkers_A01/CHILD_ASSET_INTAKE.md`
- Material discipline: `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01/`
- Cloth companion package: `docs/assets/props/SM_GIA_BloodAxeRedClothThresholdMarker_A01/`

Do not create or edit source asset folders, DCC files, FBX exports, game content folders, material graphs, material instances, texture assets, validators, global indexes, backlog docs, task-board docs, bootstrap docs, startup placement, external source concept files, runtime source files, VFX assets, audio assets, or unrelated package files from this task.

## Quality Gate Checklist

- Required universal package headings are present in the requested order.
- Package is docs-only and limited to `docs/assets/props/SM_GIA_BloodAxePaintedThresholdStone_A01/PRODUCTION_PACKAGE.md`.
- Asset remains a static stone threshold marker using chipped dirty red paint instead of cloth.
- Giant scale lock is explicit: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved ranges are females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Material restraint is explicit: rough highland stone, soot, ash, cave grit, trampled mud, chipped dirty red paint, muted lichen, and no cloth material.
- No readable text, UI arrow, quest symbol, objective symbol, magic glyph, route label, sign behavior, material pulse, VFX/audio, DCC, FBX, game-engine work, startup placement, or final visual signoff is created or claimed.
- No emissive map, glow, ritual light, shamanic pulse, torch response, route highlight, objective highlight, or animated material state is part of the baseline.
- No source asset, mesh, material instance, texture asset, validator, runtime source, Blueprint, implementation target, cave approval, or final approval is created or claimed.
- No excessive micro-detail, neutral Giant civic markers, dense trophy clutter, graphic gore, cloth strips, banners, or gameplay-readable symbols are required for the asset read.
- Texture plan includes BC, N, and ORM maps only.
- Triangle budgets, material limits, LOD0-LOD3 plan, collision planning limits, animation limits, import-planning guardrails, folder naming, and stop gates are included.
- Fine stone pitting, tiny cracks, soot speckles, ash flecks, mud droplets, chipped paint, lichen, mineral streaks, and small scratches are assigned to textures or normals in future work.
- Future collision remains disabled by default and non-gameplay; no route, movement, cave compatibility, interaction, objective, damage, aura, nav, quest, UI, VFX, audio, material graph, or startup behavior is defined.
- Stop if any later request needs readable text, a UI arrow, quest symbol, magic glyph, emissive map, material graph authoring, DCC, FBX, game-engine work, startup placement, final cave approval, final visual approval, or first implementation target selection.
