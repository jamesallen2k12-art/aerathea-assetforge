# SM_GIA_BloodAxeBrokenChannelEnd_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeBrokenChannelEnd_A01`
- Asset type: Static Mesh docs-only prop production package
- Parent kit: `KIT_GIA_BloodAxeRitualStones_A01`
- Parent intake row: `BloodAxeRitualStones_A01#RitualChannelStone_BrokenEnd_A01`
- Related package: `SM_GIA_BloodAxeRitualChannelStone_A01`
- Faction/theme: Blood Axe Tribe as a hostile Giant sub-faction only
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Status: docs-only planning package; no source, mesh, texture, material, Unreal Content, validator, startup placement, final visual approval, or implementation target is created here

`SM_GIA_BloodAxeBrokenChannelEnd_A01` is a dry, inactive broken end-cap stone for Blood Axe ritual-channel arrangements. It should read as the severed terminal piece of a Giant-scale stone trough: a low heavy slab with a broad channel that stops at a shattered end, chipped lips, ash-packed recesses, soot-darkened cracks, and static blunt-force damage. The asset is visual dressing only, and the damage is baked into the static form rather than a destructible or gameplay state.

Blood Axe visual language must stay tied to a hostile Giant raider sub-faction and must remain separate from neutral/civilized Giant culture. Use crude hostile-camp residue, rough highland stone, soot, ash, mud, blackened iron, and restrained oxide red warning accents. Do not use refined cave-town masonry, blue-gray civic stonework, terrace or waterwork motifs, warm hearth identity, restrained blue runes, peaceful highland wayfinding, or polished Giant stoneworker craft language.

This package explicitly excludes liquid endpoints, damage paths, interaction behavior, collision proxies, VFX/audio, material graph authoring, DCC, FBX, Unreal Content, startup placement, validators, source concept movement, first implementation target selection, and final visual approval.

## Gameplay Purpose

This asset is static visual dressing for abandoned Blood Axe ritual-stone arrangements, moved-camp remnants, hostile cave approaches, and dry channel-stone clusters. It exists to show that a channel line is broken, old, and inactive without implying flow, magic, damage, or interactivity.

Allowed planning uses:

- Provide a reusable broken end-cap prop for dry ritual-channel layouts.
- Terminate a channel-stone arrangement visually without creating a liquid endpoint or gameplay endpoint.
- Add static damage silhouette variety beside `SM_GIA_BloodAxeRitualChannelStone_A01`.
- Support non-graphic Blood Axe environmental history through broad fractured stone, soot, ash, mud, and restrained red identity beats.
- Preserve Giant-scale readability for later scene dressing after separate approval.

Out of scope:

- Liquid endpoints, liquid flow, wet material cues, damage paths, damage volumes, aura lines, ritual conduits, VFX/audio, material graph authoring, interaction behavior, quest or UI markers, waypoint logic, navigation/pathfinding, readable rune text, destructible states, physics states, pickup/loot/resource/crafting/economy behavior, AI behavior, encounter scripting, collision proxies, DCC, FBX, Unreal Content, startup placement, validators, source concept movement, first implementation target selection, final Blood Axe ritual approval, final Giant culture approval, or final visual approval.

## Silhouette Notes

- Primary read: a low, heavy broken end-cap slab with one broad dry trough ending at a shattered stone face.
- The broken face should have a strong terminal silhouette: jagged large planes, missing corner mass, fractured trough lip, and a blunt vertical or slanted break that reads at MMO camera distance.
- The trough must stop dry and dead. It should not form a spout, drain, basin outlet, liquid nozzle, glowing channel, path arrow, or gameplay conduit.
- Shape language should feel Giant-made and crude: oversized slab thickness, broad carved channel lips, heavy chipped end mass, offset fractured seams, and compressed ground contact.
- Optional large accents may include one or two rough iron wedges or clamp plates near the main break, used as static structural damage reads rather than repair gameplay.
- Soot and ash should pool around the stopped trough, broken end, underside contact, and major cracks as broad value bands.
- Restrained oxide red may appear as a faded cloth scrap, old paint smear, or worn warning mark, but never as liquid, blood flow, active magic, or objective signage.

Model as future real geometry only when separately approved:

- Main slab body, broken terminal face, broad trough lips, major chipped planes, missing corner silhouette, large fracture seams, ash-packed base mass, and optional rough iron wedges.

Handle through future texture, normal, AO, roughness, or masks:

- Fine stone grain, small chips, hairline cracks, soot speckles, ash flecks, oxidation, old stain feathering, mud streaks, pitting, and worn red pigment.

Avoid tiny pebble noise, dense crack networks, readable symbols, carved text, UI-like arrows, liquid outlets, gore, skull piles, active glow, refined neutral Giant carving, or any silhouette that implies a working channel endpoint.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author any future source in centimeters. 1 Unreal unit = 1 cm.

Target asset scale:

- Low slab height: 45-105 cm.
- Single broken end-cap footprint: 220-460 cm long, 150-300 cm wide.
- Larger terminal module footprint: 360-620 cm long, 210-420 cm wide.
- Broad trough width: 45-100 cm, scaled for Giant-made tools and stone carving.
- Broken terminal face height variation: 25-90 cm above the surrounding trough floor.
- Optional ash/mud contact base: 10-30 cm visual buildup only, not a collision or gameplay value.

The broken end-cap should feel like a heavy terminal fragment that only Giants, large machinery, or siege-scale force could move. It must remain lower and smaller than standing-stone anchors, altar slabs, camp gates, or watch structures, and it must not define traversal, path width, interaction range, damage radius, aura radius, objective radius, or route validation.

## Materials and Color Palette

Primary materials:

- Dark highland stone, fractured slate, soot-stained granite, chipped pale stone faces, and eroded ash-gray trough interiors.
- Cold ash, packed mud, charcoal dust, dry grit, and trampled earth around base contact and broken recesses.
- Optional blackened iron wedges or clamp plates, matte and crude, used only as large static structural accents.
- Optional faded maroon cloth scrap, chipped oxide red paint, or dirty red warning smear used sparingly as Blood Axe identity.

Palette targets:

- Dark stone: `#191B1C`, `#2B2E30`, `#454744`, `#62615A`
- Exposed chipped stone: `#747066`, `#8A8272`, `#A39A86`
- Soot and charcoal: `#080808`, `#151515`, `#2A2825`
- Ash and dry dust: `#6F6B62`, `#8C877D`, `#A8A196`
- Packed earth and mud: `#2A1F18`, `#463426`, `#6C543A`
- Blackened iron: `#111214`, `#242729`, `#3F4443`
- Restrained Blood Axe red accent: `#5F1513`, `#7A1D18`, `#8B2A21`

No default emissive is approved. Do not add active flame, glowing grooves, ritual light, animated stains, wet shine, liquid material, magic pulse, signal glow, VFX state, audio cue, or gameplay-readable material state. Exclude neutral/civilized Giant materials as the default read: no refined blue-gray civic masonry, terrace/waterwork finish, warm hearth light, restrained blue rune inlays, civic mason symbols, or hidden-settlement polish.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeBrokenChannelEnd_A01` for the world of Aerathea. The design should emphasize a low broken Giant-scale stone end-cap slab, a broad dry carved trough that terminates at a shattered end, large static damage planes, chipped trough lips, ash-packed recesses, soot-darkened cracks, optional rough iron wedges, dark highland stone, restrained oxide red Blood Axe accents, hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, grim abandoned-site mood, and the gameplay role of static inactive visual dressing only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, no liquid endpoint, no damage path, and MMO-friendly production design. Present it as a static mesh production sheet with front, side, top, and three-quarter views, material swatches, LOD/collision notes, and scale markers beside the validated `SK_GIA_Base_A01` female 442 cm and male 470 cm Giant baselines on a clean background. Avoid copying any existing franchise, avoid readable symbols, avoid carved text, avoid active channels, avoid liquid, avoid gore, avoid VFX/audio, avoid material graph diagrams, avoid magic glow, avoid quest marker language, avoid nav/pathfinding language, avoid refined neutral Giant civic stonework, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. It does not create or authorize source folders, DCC source, Blender files, mesh creation, sculpting, retopo, UVs, bakes, FBX export, Unreal Content, material instances, material graphs, collision proxies, proof renders, validators, startup placement, runtime source, final visual approval, or first implementation target selection.

Future modeling should prioritize:

- A single readable broken terminal slab with one dominant broad trough that visibly stops at the damaged end.
- Large fracture planes and chunky chipped silhouettes rather than dense rubble or pebble fields.
- Broken trough lips as actual broad geometry, with worn dry interior edges and no spout, outlet, basin, or flow guide.
- A base-contact form that sits firmly in ash and mud without becoming terrain, nav proof, or collision proof.
- Optional iron wedges or clamp plates as one or two chunky pieces, not rivet fields, nails, complex repair rigs, or destructible hardware.
- Ground-centered pivot at the base footprint center for later placement flexibility.
- Strongest presentation side facing +X unless a future implementation task confirms another convention.

Suggested future mesh groups:

- `BrokenChannelEnd_MainSlab`
- `BrokenChannelEnd_TerminalFracture`
- `BrokenChannelEnd_TroughLips`
- `BrokenChannelEnd_BaseEmbed`
- `BrokenChannelEnd_IronWedges_Optional`

Do not add sockets, VFX locators, liquid paths, damage paths, physics pieces, destructible chunks, interaction handles, quest marker shapes, route arrows, readable glyphs, nav helpers, gameplay collision helpers, DCC deliverables, FBX deliverables, Unreal files, startup placement, validators, or first implementation targets.

## Texture and Material Notes

Target material strategy:

- Default target: 1 material slot using a compact Blood Axe stone/ash atlas.
- Optional 2-slot setup only if a later approved art pass needs separate `StoneAsh` and `BlackenedIron` materials.
- Avoid separate slots for the terminal break, trough, cracks, ash patches, stains, iron wedges, chipped planes, or red accents.

Required future texture names if this asset receives a unique texture set:

- `T_GIA_BloodAxeBrokenChannelEnd_A01_BC`
- `T_GIA_BloodAxeBrokenChannelEnd_A01_N`
- `T_GIA_BloodAxeBrokenChannelEnd_A01_ORM`

Optional only with separate approval:

- `T_GIA_BloodAxeBrokenChannelEnd_A01_E` is not part of the default asset and must not be authored for this inactive dry end-cap plan.

Texture set targets:

- 1K BC/N/ORM for standard use.
- 2K only if later promoted to close-up hero dressing after approval.
- 512 is acceptable for far-background variants if the broken terminal silhouette and dry trough read remain intact.

Packed `ORM` plan:

- R: Ambient occlusion around trough lips, terminal fracture planes, slab underside, optional iron wedges, and ash-packed base contact.
- G: High roughness for stone, soot, ash, dry earth, and old stains; medium-high roughness for blackened iron.
- B: Metallic only for optional blackened iron wedges or clamp plates.

Paint broad stone planes, soot bands, ash deposits, chipped terminal faces, and old staining at MMO-readable scale. Do not rely on micro-scratches, tiny chips, readable symbols, fine carved lines, wet/liquid material cues, magic glow, animated material states, or material graph behavior.

## Triangle Budget

Target category: large prop / reusable environment dressing.

- LOD0: 3k-7k tris, 1 material target, 2 material maximum.
- LOD1: 1.5k-3.8k tris.
- LOD2: 700-1.6k tris.
- LOD3: 200-600 tris.

Budget notes:

- Spend geometry on the main slab footprint, broken terminal face, broad trough lips, large chipped planes, missing corner silhouette, and optional large iron wedges.
- Use bevels on silhouette edges, terminal break planes, and trough lips only where they preserve readability.
- Push small cracks, soot flecks, ash dust, abrasion, pitting, chipped pigment, mud streaks, and minor stone grain into future textures and normal maps.
- If a future scene uses several broken end caps, prefer instancing, rotation, scale-safe variation, or simple authored variants rather than one heavy unique cluster mesh.

This package creates no mesh and selects no first DCC, Unreal, source asset, runtime, gameplay, or implementation target.

## LOD Plan

All important future static mesh variants require LOD0-LOD3.

- LOD0: Full slab silhouette, broad trough lips, broken terminal face, major chipped planes, optional rough iron wedges, ash-packed base, and readable baked detail.
- LOD1: 55-65 percent of LOD0; reduce underside cuts, simplify bevels, merge small fracture pieces, reduce secondary terminal chips, and remove minor trough edge cuts.
- LOD2: 30-40 percent of LOD0; preserve the main slab footprint, one dominant stopped trough, broken end massing, and optional iron accent read.
- LOD3: 10-18 percent of LOD0; preserve only the low slab silhouette, dry terminal channel line, broken end value read, and overall footprint.

Reduction order:

1. Tiny chips, soot flecks, ash flecks, minor scratches, iron pitting, chipped red pigment, lichen specks, and small stain feathering.
2. Small secondary cracks, narrow cuts, tiny rubble pieces, small underside forms, and minor mud clumps.
3. Minor trough-edge notches, small bevels, hidden backside details, and non-silhouette terminal nicks.
4. Optional secondary iron wedges, extra fracture seams, small red cloth scraps, and minor base stones.
5. Secondary trough complexity after the dominant dry stopped trough remains readable.

Never reduce the primary low slab mass, broken terminal read, broad dry trough, Giant-scale footprint, or Blood Axe material separation before removing small detail.

## Collision Notes

Default collision planning: disabled unless a later placement task requests simple blocking on the large static body.

If collision is approved later:

- Use one simple box or low convex hull for the main slab footprint.
- Use a second simple hull only for a high broken terminal face if needed.
- Keep trough interiors, terminal crack detail, ash deposits, small chips, stains, optional iron wedges, and base rubble out of collision.
- Keep collision non-interactive and non-gameplay.

Do not create collision proxies, UCX meshes, Unreal collision settings, physics bodies, complex-as-simple collision, nav blockers, nav links, liquid volumes, damage volumes, ritual volumes, aura volumes, objective volumes, interaction volumes, trigger volumes, destructible collision, per-crack collision, per-wedge collision, route validators, pathfinding helpers, or startup placement from this package.

This package makes no collision correctness claim and does not define path widths, traversal proof, route gates, encounter lanes, cover rules, damage paths, liquid endpoints, interaction behavior, quest logic, or gameplay affordances.

## Animation Notes

Static mesh only.

No skeletal rig, animation clips, liquid movement, cloth movement, physics movement, destruction, collapse, material pulse, VFX, audio, gameplay state change, interaction state, ritual state, damage state, endpoint state, or channel-flow state is planned or authorized.

The broken channel end should be modeled as permanently inactive: old, dry, eroded, non-graphic, and static. Any moving, glowing, audio-linked, destructible, interactive, damaging, aura-emitting, quest-readable, endpoint-readable, or gameplay-active variant requires a separately named and approved package.

## Unreal Import Notes

Future import planning only:

- Asset name: `SM_GIA_BloodAxeBrokenChannelEnd_A01`
- Asset type: Static Mesh
- Recommended future folder path: `/Game/Aerathea/Props/Giants/BloodAxe/RitualStones/`
- Pivot: ground center at the full slab footprint, with the strongest broken-terminal presentation side facing +X unless a future implementation task overrides it.
- Scale: authored in centimeters against `SK_GIA_Base_A01` female 442 cm and male 470 cm baselines.
- Collision type: no collision by default; future simple collision only if requested for a large static body.
- LODs: LOD0-LOD3 required for future implementation.
- Material slots: 1 target, 2 maximum.
- Texture list: `T_GIA_BloodAxeBrokenChannelEnd_A01_BC`, `T_GIA_BloodAxeBrokenChannelEnd_A01_N`, `T_GIA_BloodAxeBrokenChannelEnd_A01_ORM`.
- Material instance recommendation: `MI_GIA_BloodAxeBrokenChannelEnd_A01`.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: preserve broad slab, broken terminal, and dry trough silhouette first; remove micro-detail before silhouette detail in lower LODs.

This section does not authorize Unreal Content, import scripts, material instances, material graphs, texture assets, Blueprint actors, collision proxies, validators, review actors, startup placement, runtime source, source asset movement, final visual approval, or first implementation target selection.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeBrokenChannelEnd_A01/PRODUCTION_PACKAGE.md`

Future source and game asset names, for planning only:

- Static mesh: `SM_GIA_BloodAxeBrokenChannelEnd_A01`
- Material instance: `MI_GIA_BloodAxeBrokenChannelEnd_A01`
- Base color: `T_GIA_BloodAxeBrokenChannelEnd_A01_BC`
- Normal: `T_GIA_BloodAxeBrokenChannelEnd_A01_N`
- ORM: `T_GIA_BloodAxeBrokenChannelEnd_A01_ORM`

No source folder, DCC file, FBX, Unreal Content path, external source concept copy, source concept movement, task-board change, global index update, backlog update, bootstrap update, approval queue update, runtime source file, validator, collision proxy, startup placement, first implementation selection, or additional documentation file is created by this docs-only task.

## Quality Gate Checklist

- Required 15 top-level production package headings are present in the requested order.
- Asset remains docs-only and modifies no files outside `docs/assets/props/SM_GIA_BloodAxeBrokenChannelEnd_A01/PRODUCTION_PACKAGE.md`.
- Giant scale lock is explicit: `SK_GIA_Base_A01` female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline, with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe is defined as a hostile Giant sub-faction and does not overwrite neutral/civilized Giant culture.
- Broken channel end remains a static, dry, inactive, non-graphic end-cap stone for dry ritual-channel arrangements.
- Static visual damage is baked into the silhouette; no destructible state, physics state, damage state, endpoint state, liquid endpoint, or damage path is defined.
- Visual focus stays on broad stopped trough, broken terminal face, chipped slab mass, soot/ash staining, optional rough iron wedges, large readable forms, and no excessive micro-detail.
- No liquid endpoints, liquid flow, VFX/audio, material graph authoring, damage paths, damage volumes, ritual gameplay, interaction behavior, quest marker, navigation/pathfinding, collision proxies, DCC, FBX, Unreal Content, startup placement, validators, source concept movement, first implementation target selection, or final visual approval is claimed.
- No loot, pickup, crafting, economy, resource, aura, buff, debuff, AI, encounter scripting, waypoint logic, readable text, trail gameplay, audio cue, active material state, final Blood Axe ritual approval, or final Giant culture approval is defined.
- Materials are MMO-safe: 1 material target, 2 maximum, high roughness, no default emissive, no active liquid, no glow, and no refined neutral Giant civic finish.
- LOD0-LOD3, triangle budgets, texture maps, collision notes, animation notes, folder naming, future import planning notes, and stop gates are included without performing implementation work.
- Silhouette remains readable from MMO camera distance and does not depend on tiny cracks, graphic content, active effects, UI-like color, or signage.
