# SM_GIA_BloodAxeDryChannelCornerAshResidue_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeDryChannelCornerAshResidue_A01`
- Asset type: Static Mesh docs-only prop production package
- Task: `AET-MA-20260629-268`
- Parent kit: `KIT_GIA_BloodAxeDryChannelStoneSet_A01`
- Parent intake row: `BloodAxeDryChannelStoneSet_A01#AshFill_CornerResidue_A01`
- Reference packages: `SM_GIA_BloodAxeDryChannelAshFill_A01` and `SM_GIA_BloodAxeDryChannelCornerTurn_A01`
- Policy references: `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01` and `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package; no source asset, DCC work, FBX, Unreal Content asset, runtime work, validator, material instance, texture asset, material graph, VFX/audio, interaction behavior, startup placement, first implementation target, final visual approval, or final Blood Axe ritual approval is created or claimed

`SM_GIA_BloodAxeDryChannelCornerAshResidue_A01` is a shallow matte ash-residue insert for static Blood Axe dry-channel corner pieces. It adds cold ash, soot, grit, and old camp residue to inside-corner trough pockets, broken outer-corner lips, and corner slab contact zones without creating a liquid surface, a directional flow read, a spline marker, an aura line, a gameplay conduit, a damage area, or an active ritual cue.

Blood Axe is a hostile Giant sub-faction. This ash-residue language must stay separate from neutral/civilized Giant culture, which remains tied to hidden highland settlements, master stonework, blue-gray civic masonry, terraces, bridges, waterworks, warm hearth light, restrained blue runes, and orderly stoneworker identity. Blood Axe ash residue may support abandoned camp memory and hostile threshold dressing, but it must not redefine Giants as a people.

## Gameplay Purpose

The gameplay purpose is visual planning only. The residue supports static dry-channel corner modules by making the corner feel abandoned, cold, and inactive.

Allowed planning uses:

- Add a matte, dry ash patch to static L-shaped, shallow-bend, or broken-corner dry channel pieces.
- Reinforce the no-flow read by collecting ash in corner recesses and broken lip pockets.
- Break up dark trough interiors with pale cold ash, soot, charcoal dust, grit, and subtle mud contamination.
- Provide a low-cost reusable visual insert for corner layouts without drawing attention as an interactable object.
- Keep Blood Axe dry-channel dressing consistent with the ash-fill and corner-turn packages.

Out of scope:

- Flow direction, liquid flow, wet material read, directional conduit language, spline marker behavior, aura line, route marker, pathfinding guide, quest route, damage path, gameplay conduit, ritual activation, offering mechanic, puzzle state, readable rune text, objective marker, waypoint behavior, interaction prompt, pickup, loot, harvesting, crafting, economy, AI behavior, encounter design, navigation/pathfinding, traversal proof, cover, destructibility, physics simulation, collision, particles, smoke, material-state animation, material graph authoring, VFX/audio, DCC work, FBX, Unreal asset work, runtime work, validators, startup placement, source concept movement, first implementation target selection, final Giant culture approval, final Blood Axe ritual approval, or final visual approval.

## Silhouette Notes

The silhouette should stay quiet and low. The residue is a support shape for corner stones, not the main prop identity.

Primary silhouette goals:

- Low matte ash residue settled into an inside corner pocket, broken trough bend, or chipped outer-corner recess.
- Irregular, non-directional footprint with no arrow shape, stream shape, trail shape, or readable route.
- Soft slumped banks, shallow wind-scattered edges, and broad pale/dark value grouping visible from above.
- Slight raised ridges only where they imply old settled ash, never movement, ripple, liquid pooling, or aura energy.
- Edge feathering that visually meets the surrounding stone lips without covering the Giant-scale slab silhouette.

Model as future geometry only where a visible shallow surface profile is needed: broad ash footprint, soft banks, low undulations, and a few chipped grit lumps at the perimeter. Keep ash dust, soot flecks, charcoal specks, powder grains, tiny stone chips, fine cracks, mud specks, red dust, and corner contact stains in future texture, normal, AO, roughness, or mask detail.

Avoid vertical plumes, splash forms, flowing curves, swirl shapes, directional streaks, rune-like marks, UI arrow language, route symbols, aura rings, liquid pools, wet highlights, hazard-field silhouettes, dense rubble carpets, graphic remains, polished civic Giant carving, blue rune language, and high-frequency micro-detail.

## Scale Notes

Giant scale lock: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.

Author any future source in centimeters. 1 Unreal unit = 1 cm.

Target planning scale:

- Small corner pocket residue: 70-130 cm across the inside corner, 3-10 cm raised surface variation.
- Standard corner residue: 120-240 cm across the inside bend, 4-16 cm raised surface variation.
- Broken outer-corner residue: 80-180 cm along the chipped lip, 3-12 cm raised surface variation.
- Perimeter feathering: most edges should remain low enough to tuck visually under or against surrounding stone lips.

These values are art scale planning only. They are not navigation widths, traversal data, hazard radii, aura radii, damage radii, route markers, liquid volumes, interaction ranges, objective spaces, collision guarantees, or implementation measurements.

The residue should feel made by Giant-scale camp use and old ritual cleanup, but it must remain visually subordinate to the corner stone mass.

## Materials and Color Palette

Primary materials:

- Cold matte ash, pale gray powder, charcoal dust, soot-dark corner recesses, cave grit, and old camp residue.
- Trampled mud and packed earth only as subtle edge contamination where the ash meets stone or ground.
- Tiny stone grit, chipped mineral specks, and charcoal fragments only as future texture detail.
- Optional restrained oxide red dusting as a Blood Axe echo, never as blood, paint symbols, rune text, route markings, UI language, or gameplay markers.

Palette targets:

- Charcoal and soot: `#17191A`, `#242729`, `#3C3D3A`, `#5A5A53`
- Cold ash and dust: `#6F6D66`, `#8A867B`, `#ADA698`, `#C6BDAA`
- Packed earth contamination: `#2A2119`, `#403126`, `#5C4938`, `#75624E`
- Chipped stone grit: `#5A5A53`, `#6F6D66`, `#8A867B`, `#ADA698`
- Restrained oxide red dusting: `#5A1412`, `#711B17`, `#84261E`

Material behavior:

- Matte, dry, high roughness, non-metallic, non-emissive.
- No wet specular sheen, clearcoat, translucency, animated mask, glow, bloom cue, liquid surface, smoke, particle read, or gameplay-readable highlight.
- The material should stay quieter than stone slabs, iron clamps, cloth knots, horn, bone, and banner accents.

Excluded neutral/civilized Giant materials:

- Blue-gray civic masonry, refined cave-town stonework, terrace or waterwork channel finish, polished bridge stone, warm hearth light, peaceful highland guide markers, civic mason symbols, restrained blue rune accents, and orderly hidden-settlement polish.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeDryChannelCornerAshResidue_A01` for the world of Aerathea. The design should emphasize a shallow matte dry ash-residue insert for static dry-channel corner pieces, cold ash, soot, charcoal dust, cave grit, trampled mud edge contamination, irregular non-directional corner residue, no flow direction, no liquid surface, no spline marker, no aura line, no glow, no particles, Blood Axe hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, grim abandoned-camp memory, and the gameplay role of static non-interactive corner dressing only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, non-emissive material behavior, and MMO-friendly production design. Present it as a static prop production sheet with top view, three-quarter view, corner-fit callout, material swatches, LOD notes, no-collision label, and scale markers beside female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines on a clean background. Avoid copying any existing franchise, avoid directional flow read, avoid wet shine, avoid smoke, avoid particles, avoid aura materials, avoid damage areas, avoid material graph diagrams, avoid VFX/audio cues, avoid readable rune text, avoid interaction prompts, avoid DCC or FBX claims, avoid Unreal implementation claims, avoid startup placement, avoid final visual approval, avoid neutral/civilized Giant civic materials, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. It does not create or authorize source folders, DCC source, mesh creation, sculpting, retopo, UVs, bakes, proof renders, LOD source, collision proxies, FBX, Unreal assets, material instances, texture assets, material graphs, validators, runtime source, Blueprints, sockets, animation assets, startup placement, source concept movement, final visual approval, or first implementation target selection.

Future source, if separately approved, should keep the residue simple:

- Build one shallow irregular surface shaped for static corner recesses and broken corner lips.
- Keep the footprint smaller than the surrounding trough or corner pocket so the stone module remains dominant.
- Use broad soft banks and a few low undulations instead of dense sculpted ash grains.
- Make the underside flat or nearly flat for simple placement against a corner trough floor.
- Use corner-fit variants through footprint shape and broad value masks rather than unique dense geometry.
- Avoid overhangs, deep cavities, undercuts, loose pebble carpets, modeled ash particles, arrow-like streaks, directional trails, or complex debris piles.

Future pivot policy:

- Base center of the residue footprint.
- Primary orientation neutral; do not encode a flow direction into the mesh shape.
- Keep the local origin stable so variants can be placed inside corner modules without changing the owning stone asset.

## Texture and Material Notes

This package creates no textures, material instances, parent materials, material functions, shader graphs, trim sheets, masks, VFX materials, or Unreal assets.

Standard future texture outputs if a later approved package creates assets:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- No baseline emissive texture

Suggested future texture names for planning reference only:

- `T_GIA_BloodAxeDryChannelCornerAshResidue_A01_BC`
- `T_GIA_BloodAxeDryChannelCornerAshResidue_A01_N`
- `T_GIA_BloodAxeDryChannelCornerAshResidue_A01_ORM`

Texture direction:

- Base color should carry broad ash value shifts, soot-dark corner pockets, cold powder, and warmer mud-contaminated edges.
- Normal detail should stay subtle: powder settling, small grit impressions, shallow cracks, and low residue ridges.
- AO should ground the residue against corner lips, broken trough edges, and stone contact zones without making it look wet.
- ORM should keep roughness high, metallic at zero, and occlusion broad enough to read inside dark stone corners.

Material slot target:

- 1 material target.
- Do not create unique material slots for soot flecks, ash grains, grit, mud specks, red dusting, chips, contact stains, or corner-edge powder.
- Do not add emissive, translucent, masked particle, liquid, aura, damage, decal-only, or animated material behavior.

## Triangle Budget

This package creates no mesh. Future LOD0 planning target:

- Corner ash residue static insert: 150-800 tris, 1 material target, 512-1K texture set.
- Small corner pocket residue variants: 100-350 tris.
- Standard corner residue variants: 250-650 tris.
- Broken outer-corner residue variants: 250-800 tris only when broad footprint variation requires it.

Spend triangles on the low ash footprint, soft perimeter banks, a few broad undulations, and a readable corner-fit silhouette. Do not spend triangles on ash grains, soot flecks, powder particles, tiny stones, fine cracks, mud droplets, red dust specks, hidden underside cuts, or residue detail that should be handled through future texture and normal detail.

## LOD Plan

All important future static variants need LOD0, LOD1, LOD2, and LOD3 before any separately approved production import lane uses them.

- LOD0: full irregular corner footprint, broad ash banks, low settled ridges, feathered perimeter, corner-fit shape, and broad ash/soot value grouping.
- LOD1: 55-70 percent of LOD0; reduce minor ridge loops, secondary edge variation, tiny silhouette bites, small grit lumps, and underside detail.
- LOD2: 30-45 percent of LOD0; keep the main matte ash footprint, one or two broad raised forms, and the major soot/ash value separation.
- LOD3: 10-25 percent of LOD0; preserve only the low dry ash mass, corner-pocket relationship, and broad pale/dark no-flow read.

Reduction order:

1. Remove geometry assumptions for ash grains, soot speckles, powder flecks, tiny chips, small grit, hairline cracks, and red dust.
2. Reduce minor edge waviness, shallow non-silhouette ridges, and small surface dimples.
3. Remove hidden underside detail and any undercut that does not affect the top read.
4. Simplify secondary banks and merge small surface planes.
5. Preserve the primary low footprint, corner-fit identity, and dry/no-flow read until the final LOD.

Never let LOD reduction create a puddle, ripple, flow direction, aura ring, hazard field, quest marker, readable rune, active channel cue, or route marker.

## Collision Notes

Collision is not part of this asset package. The corner ash residue should remain collision disabled in future planning and should not block players, cameras, traces, projectiles, navigation, pathfinding, or gameplay systems.

Do not define:

- UCX proxies, complex collision, simple primitives, physics bodies, nav blockers, smart links, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, pickup collision, cover behavior, traversal proof, path widths, route gates, encounter lanes, or collision correctness.
- Collision for ash surface undulations, edge feathering, soot, grit, mud, chips, red dusting, corner contact stains, or powder detail.

If a future corner-stone implementation needs contact, the surrounding stone module must own that policy under a separate task. This residue package remains visual dressing only.

## Animation Notes

Baseline asset is static.

Allowed planning language:

- Static matte ash residue.
- Static soot, grit, mud-edge contamination, powder settling, and roughness variation.
- Static placement inside dry channel corner pockets, shallow bends, or broken corner recesses.

Not approved:

- Skeletal animation, vertex animation, physics movement, settling simulation, wind response, cloth simulation, liquid movement, material pulses, animated masks, emissive states, ritual activation, smoke, ash particles, VFX/audio, gameplay state changes, damage behavior, aura behavior, quest/objective states, waypoint behavior, interaction behavior, pickup behavior, destructible behavior, or startup placement.

Any moving, glowing, interactive, damaging, aura-emitting, quest-readable, waypoint-readable, liquid, audio, VFX, or gameplay-active variant must be split into a separately named and approved package.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, import script, material instance, texture asset, socket, collision proxy, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX, source asset movement, material graph, VFX/audio, final visual approval, or implementation file is created or authorized.

Potential future Unreal identity after a separately scoped and approved lane:

- Asset name: `SM_GIA_BloodAxeDryChannelCornerAshResidue_A01`
- Asset type: Static Mesh visual dressing for Blood Axe dry channel corner modules
- Candidate folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/RitualStones/Channels/`
- Pivot: base center of the residue footprint.
- Orientation: neutral footprint orientation; do not encode flow direction.
- Scale: centimeter-authored source, import scale 1.0, preserving female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines.
- Collision type: disabled.
- LOD plan: LOD0-LOD3 required for any important future static variant.
- Material slots: 1 target.
- Texture list, planning only: `T_GIA_BloodAxeDryChannelCornerAshResidue_A01_BC`, `T_GIA_BloodAxeDryChannelCornerAshResidue_A01_N`, `T_GIA_BloodAxeDryChannelCornerAshResidue_A01_ORM`; no baseline emissive texture.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: use as static visual residue only, keep triangles low, share material vocabulary with the dry channel kit, keep collision disabled, and avoid runtime behavior.

These notes do not select a source asset target, DCC target, FBX target, Unreal target, runtime target, gameplay target, review-scene target, startup placement target, or implementation target.

## Folder and Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeDryChannelCornerAshResidue_A01/PRODUCTION_PACKAGE.md`

Future planning names only:

- Static mesh: `SM_GIA_BloodAxeDryChannelCornerAshResidue_A01`
- Texture base color: `T_GIA_BloodAxeDryChannelCornerAshResidue_A01_BC`
- Texture normal: `T_GIA_BloodAxeDryChannelCornerAshResidue_A01_N`
- Texture packed ORM: `T_GIA_BloodAxeDryChannelCornerAshResidue_A01_ORM`
- Parent kit: `KIT_GIA_BloodAxeDryChannelStoneSet_A01`
- Sibling reference: `SM_GIA_BloodAxeDryChannelAshFill_A01`
- Sibling reference: `SM_GIA_BloodAxeDryChannelCornerTurn_A01`
- Material policy reference: `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01`
- LOD/collision policy reference: `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`

Do not create or edit `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, external concept folders, global indexes, task boards, backlog docs, bootstrap docs, unrelated production packages, validators, startup placement files, source folders, DCC files, FBX files, Unreal files, images, material graphs, VFX/audio assets, or any file outside this package path from this task.

## Quality Gate Checklist

- Package uses the 15-section Aerathea universal production package format.
- Package is docs-only and changes no DCC, FBX, Unreal assets, runtime source, startup scene, external concept, validator, material instance, texture asset, material graph, VFX/audio asset, global index, task board, backlog, bootstrap, image, or unrelated package file.
- Asset identity is `SM_GIA_BloodAxeDryChannelCornerAshResidue_A01` under `KIT_GIA_BloodAxeDryChannelStoneSet_A01`.
- Giant scale lock is explicit: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline.
- Approved Giant ranges are explicit: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Corner ash residue remains static, matte, dry, shallow, non-emissive, non-liquid, non-directional, non-interactive, and non-gameplay.
- Flow direction, spline marker behavior, aura line, particles, liquid surfaces, damage areas, material graph authoring, collision, VFX/audio, interaction behavior, first implementation target selection, and final visual approval are excluded.
- No ritual gameplay, offering mechanics, activation states, puzzle states, quest/UI markers, objective markers, waypoint behavior, navigation/pathfinding, traversal proof, encounter behavior, AI behavior, pickup/loot behavior, resource/crafting/economy behavior, destructible behavior, physics behavior, or material-state behavior is defined.
- Materials follow cold ash, soot, charcoal dust, cave grit, subtle mud contamination, chipped stone grit, and restrained oxide red dusting only.
- Default emissive, ritual glow, signal glow, shamanic glow, wet material, active flame, animated material state, UI-like marker, readable text, and neutral/civilized Giant material defaults are absent.
- Fine ash grains, soot flecks, powder, small grit, hairline cracks, mud specks, red dust, and surface dust are assigned to future texture or normal detail, not dense geometry.
- Triangle budgets, LOD0-LOD3 policy, no-collision limits, animation limits, Unreal import planning, folder naming, material slot target, and texture-map planning are included without implementation claims.
