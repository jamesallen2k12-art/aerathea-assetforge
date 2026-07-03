# SM_GIA_BloodAxeDryChannelBrokenGapAshFill_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeDryChannelBrokenGapAshFill_A01`
- Asset type: Docs-only static mesh prop planning package
- Task: `AET-MA-20260629-263`
- Parent kit: `KIT_GIA_BloodAxeDryChannelStoneSet_A01`
- Parent intake row: `BloodAxeDryChannelStoneSet_A01#AshFill_BrokenGap_A01`
- Policy references: `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01`, `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`, `DOC_GIA_BloodAxeDryChannelStoneReviewRows_A01`, and sibling package `SM_GIA_BloodAxeDryChannelAshFill_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package; no source asset, DCC work, FBX, Unreal Content, runtime work, validator, material instance, texture asset, material graph, gameplay volume, damage path, readable rune, particle VFX, startup placement, implementation claim, implementation target, or final visual signoff is created or authorized
- Required exclusions: no gameplay volume, no damage path, no readable rune, no particle VFX, no DCC, no Unreal Content, no startup placement, no implementation claim

`SM_GIA_BloodAxeDryChannelBrokenGapAshFill_A01` is a low, static, matte dry ash and soot fill for broken gaps between Blood Axe dry-channel stone pieces. It should look like cold camp residue, wind-settled ash, dark soot, and gritty dirt trapped between fractured Giant-scale slabs. It is not liquid, not a hazard, not a gameplay volume, not an aura surface, not a particle effect, and not a readable rune.

Blood Axe identity remains a hostile Giant sub-faction treatment and must stay separate from neutral/civilized Giant culture. This package may support abandoned Blood Axe camp memory, hostile threshold dressing, and broken ritual-stone residue, but it must not become the default material language for Giants as a people. Exclude refined cave-town masonry, blue-gray civic stonework, terrace or waterwork channel language, warm hearth settlement identity, peaceful highland guide markers, civic mason symbols, restrained blue rune culture, and hidden-settlement polish.

## Gameplay Purpose

The gameplay purpose is visual planning only. The broken-gap ash fill is non-gameplay static dressing for dry inactive channel layouts.

Allowed planning uses:

- Fill irregular cracks and missing spans between dry channel stones with a matte ash and soot value.
- Reinforce broken continuity so adjacent slabs read as interrupted remnants, not an active route.
- Add cold ash, soot, grit, and trampled dirt where fractured channel pieces no longer meet cleanly.
- Provide a low-cost visual insert that can be reused beside broken sections, capped ends, shallow turns, and offset slabs.
- Keep the residue readable at MMO camera distance without drawing attention as an interactable object.

Out of scope:

- Gameplay volume, damage path, damage volume, aura behavior, ritual activation, offering mechanics, puzzle states, objective markers, quest/UI markers, waypoint behavior, interaction prompts, pickups, loot, harvesting, crafting, economy, AI behavior, encounter design, navigation/pathfinding, traversal proof, cover, destructibility, physics simulation, collision, particles, liquid surfaces, wet flow, material-state animation, material graph authoring, VFX/audio, DCC work, FBX, Unreal Content, runtime work, validators, startup placement, source concept movement, implementation target selection, implementation claim, final Blood Axe ritual approval, final Giant culture approval, or final visual signoff.

## Silhouette Notes

The silhouette should stay quiet and recessed. It supports broken channel stones by occupying negative space, not by becoming a dominant prop.

Primary silhouette goals:

- Low settled residue mass that sits between broken stone ends and fractured trough lips.
- Irregular footprint shaped by missing slab corners, snapped trough edges, and uneven stone spacing.
- Feathered ash margins that visually tuck under adjacent stone lips.
- Slight dark soot pockets in the lowest gaps, with pale ash gathered on shallow banks.
- Broad top-read value shape visible from above and from a three-quarter MMO camera.

Model as future geometry only where the fill needs shallow profile: one low surface, a few broad banks, soft broken edges, and small height variation where ash piles against stone. Keep ash dust, soot flecks, gritty powder, tiny charcoal chips, hairline cracks, powder ripples, mud stains, fine stone grit, and oxide red dusting in future texture, normal, AO, roughness, or mask detail.

Avoid readable symbols, carved text, rune marks, direction arrows, trail markers, puddle rims, wet highlights, liquid pools, aura rings, damage-field reads, smoke columns, particle emitters, magical residue, dense debris carpets, graphic remains, refined civic Giant finish, blue rune language, and high-frequency micro-detail.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.

Author any future source in centimeters. 1 Unreal unit = 1 cm.

Target planning scale:

- Small broken-gap fill: 90-180 cm long, 45-110 cm wide, 2-10 cm raised surface variation.
- Standard broken-gap fill: 160-340 cm long, 80-180 cm wide, 4-16 cm raised surface variation.
- Large offset-slab gap fill: 280-480 cm long, 120-240 cm wide, 6-24 cm raised surface variation.
- Edge feathering: keep most borders thin enough to sit visually under broken channel lips or against slab seams.
- Vertical read: keep residue below the stone lips so the ash never becomes a wall, cover shape, step, or traversal cue.

These values are art scale planning only. They are not navigation widths, traversal data, hazard radii, aura radii, damage radii, interaction ranges, objective spaces, liquid volumes, collision guarantees, route markers, pathfinding data, or final placement values.

## Materials and Color Palette

Primary materials:

- Cold settled ash, pale gray powder, charcoal dust, soot-dark recesses, dry cave grit, and old camp residue.
- Trampled mud and packed earth as subtle edge contamination where ash meets broken stones.
- Tiny stone grit, chipped mineral specks, and charcoal flecks as future texture detail only.
- Optional dull oxide red dusting as a restrained Blood Axe material echo, never as readable paint, blood, rune language, objective color, or gameplay marker.

Palette targets:

- Charcoal and soot: `#17191A`, `#242729`, `#3C3D3A`, `#5A5A53`
- Cold ash and dust: `#6F6D66`, `#8A867B`, `#ADA698`, `#C6BDAA`
- Packed earth contamination: `#2A2119`, `#403126`, `#5C4938`, `#75624E`
- Chipped stone grit: `#5A5A53`, `#6F6D66`, `#8A867B`, `#ADA698`
- Restrained oxide red dusting: `#5A1412`, `#711B17`, `#84261E`

Material behavior:

- Matte, dry, high roughness, non-metallic, and non-emissive.
- No wet specular sheen, no clearcoat, no transparency, no animated masks, no glow, no bloom cue, no liquid surface, and no gameplay-readable highlight.
- The residue should remain quieter than the surrounding rough highland stone, blackened iron, rawhide, rope, horn, bone, or oxide red Blood Axe accents.

Excluded neutral/civilized Giant materials:

- Blue-gray civic masonry, refined cave-town stonework, polished terrace or waterwork channel finish, warm hearth light, peaceful highland guide markers, civic mason symbols, restrained blue rune accents, and orderly hidden-settlement polish.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeDryChannelBrokenGapAshFill_A01` for the world of Aerathea. The design should emphasize a low matte dry ash and soot fill for broken gaps between dry channel stone pieces, irregular feathered residue edges, cold ash, charcoal dust, soot-dark recesses, dry cave grit, trampled mud edge contamination, non-liquid surface language, no glow, no particles, no aura, no hazard read, no gameplay volume, no damage path, no readable rune, Blood Axe hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, grim abandoned-camp memory, and the role of static non-interactive broken-channel dressing only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, non-emissive material behavior, and MMO-friendly production design. Present it as a static prop production sheet with top view, three-quarter view, broken-gap fit callout, material swatches, LOD notes, no-collision label, and scale markers beside the validated female 442 cm and male 470 cm Giant baselines on a clean background. Avoid copying any existing franchise, avoid liquid flow, avoid wet shine, avoid smoke, avoid particles, avoid aura materials, avoid damage areas, avoid material graph diagrams, avoid VFX/audio cues, avoid readable rune text, avoid interaction prompts, avoid DCC or FBX claims, avoid Unreal Content claims, avoid startup placement, avoid implementation claims, avoid final visual signoff, avoid neutral/civilized Giant civic materials, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. It does not create or authorize source folders, DCC source, mesh creation, sculpting, retopo, UVs, bakes, proof renders, LOD source, collision proxies, FBX, Unreal Content, material instances, texture assets, material graphs, validators, runtime source, Blueprints, sockets, animation assets, startup placement, source concept movement, final visual signoff, implementation target selection, or implementation claims.

Future source, if separately approved by a later task, should keep the broken-gap fill simple:

- Build one shallow irregular surface shaped for gaps between broken dry-channel stones.
- Keep the footprint smaller than the visible gap so the surrounding fractured stone remains dominant.
- Use a few broad ash banks and soot pockets, not dense sculpted ash grains.
- Make the underside flat or nearly flat for easy placement between low channel modules.
- Use variant shapes through footprint, edge feathering, and broad material masks rather than dense unique geometry.
- Avoid overhangs, deep cavities, undercuts, loose pebble carpets, modeled ash particles, complex debris piles, or gore-coded debris.

Future pivot policy:

- Base center of the broken-gap fill footprint.
- Primary long axis aligned with +X for offset-slab and straight broken-section use unless a later export convention sets another direction.
- Keep the local origin stable so gap-fill variants can be swapped in dry-channel layouts without changing stone assets.

## Texture and Material Notes

This package creates no textures, material instances, parent materials, material functions, shader graphs, trim sheets, masks, VFX materials, or Unreal Content.

Standard future texture outputs if a later approved package creates assets:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- No baseline emissive texture

Suggested future texture names for planning reference only:

- `T_GIA_BloodAxeDryChannelBrokenGapAshFill_A01_BC`
- `T_GIA_BloodAxeDryChannelBrokenGapAshFill_A01_N`
- `T_GIA_BloodAxeDryChannelBrokenGapAshFill_A01_ORM`

Texture direction:

- Base color should carry broad ash value shifts, soot-dark pockets, slightly warmer mud-contaminated edges, and restrained gritty breakup.
- Normal detail should stay subtle: fine powder ripples, shallow settled cracks, small grit impressions, and low residue ridges.
- AO should ground the fill against broken stone ends and trough lips without making it look wet.
- ORM should keep roughness high, metallic at zero, and occlusion broad enough to read in an irregular gap.

Material slot target:

- 1 material target.
- Do not create unique material slots for soot flecks, ash grains, grit, mud specks, red dusting, chips, edge stains, or channel contact marks.
- Do not add emissive, translucent, masked particle, liquid, aura, damage, decal-only, readable rune, or animated material behavior.

## Triangle Budget

This package creates no mesh. Future LOD0 planning target:

- Broken-gap ash fill static insert: 200-1,000 tris, 1 material target, 512-1K texture set.
- Small broken-gap variants: 150-400 tris.
- Standard broken-gap variants: 300-750 tris.
- Large offset-slab gap variants: 600-1,200 tris only when broad footprint variation requires it.

Spend triangles on the low residue footprint, broad ash banks, feathered perimeter forms, shallow soot pockets, and readable broken-gap fit. Do not spend triangles on ash grains, soot flecks, powder particles, tiny stones, fine cracks, mud droplets, red dust specks, hidden underside cuts, or debris better handled in future texture and normal detail.

## LOD Plan

All important future static variants need LOD0, LOD1, LOD2, and LOD3 before any separately approved production import lane uses them.

- LOD0: full shallow broken-gap footprint, broad ash banks, dark soot pockets, feathered edges, subtle fit against fractured stone, and broad material value grouping.
- LOD1: 55-70 percent of LOD0; reduce minor ridge loops, secondary edge waviness, tiny silhouette bites, small surface dimples, and underside detail.
- LOD2: 30-45 percent of LOD0; keep the main matte ash footprint, one or two broad raised forms, and the major soot/ash value separation.
- LOD3: 10-25 percent of LOD0; preserve only the low dry residue mass, broken-gap relationship, and broad pale/dark value read.

Reduction order:

1. Remove geometry assumptions for ash grains, soot speckles, powder flecks, tiny chips, small grit, and hairline cracks.
2. Reduce minor edge waviness, shallow non-silhouette ridges, and small surface dimples.
3. Remove hidden underside detail and any undercut that does not affect the top read.
4. Simplify secondary banks and merge small surface planes.
5. Preserve the primary low footprint and dry/no-flow broken-gap read until the final LOD.

Never let LOD reduction create a puddle, ripple, aura ring, hazard field, quest marker, readable rune, route marker, active flow read, or neutral/civilized Giant material read.

## Collision Notes

Collision is not part of this asset package. The broken-gap ash fill should remain collision disabled in future planning and should not block players, cameras, traces, projectiles, navigation, pathfinding, or gameplay systems.

Do not define:

- UCX proxies, complex collision, simple primitives, physics bodies, nav blockers, smart links, trigger volumes, gameplay volumes, damage volumes, aura volumes, objective volumes, interaction volumes, pickup collision, cover behavior, traversal proof, path widths, encounter lanes, or collision correctness.
- Collision for ash surface undulations, edge feathering, soot, grit, mud, chips, red dusting, channel contact marks, or broken-gap footprint.

If a future channel-stone implementation needs contact, the surrounding stone module must own that policy under a separate task. This broken-gap ash-fill package remains visual residue only.

## Animation Notes

Baseline asset is static.

Allowed planning language:

- Static matte ash and soot fill.
- Static grit, mud-edge contamination, roughness variation, and cold residue value breakup.
- Static placement between dry broken channel stones or offset slab gaps.

Not approved:

- Skeletal animation, vertex animation, physics movement, settling simulation, wind response, cloth simulation, liquid movement, material pulses, animated masks, emissive states, ritual activation, smoke, ash particles, particle VFX, gameplay state changes, damage behavior, aura behavior, quest/objective states, waypoint behavior, interaction behavior, pickup behavior, destructible behavior, startup placement, or material-state behavior.

Any moving, glowing, interactive, damaging, aura-emitting, quest-readable, waypoint-readable, liquid, audio, VFX, or gameplay-active variant must be split into a separately named and approved package.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, import script, material instance, texture asset, socket, collision proxy, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX, source asset movement, material graph, VFX/audio, final visual signoff, implementation target, implementation claim, or implementation file is created or authorized.

Potential future Unreal identity after a separately scoped and approved lane:

- Asset name: `SM_GIA_BloodAxeDryChannelBrokenGapAshFill_A01`
- Asset family: Static mesh visual dressing for Blood Axe dry channel broken gaps
- Candidate folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/RitualStones/Channels/`
- Pivot: base center of the broken-gap fill footprint.
- Orientation: longest axis faces +X unless a later export convention sets another direction.
- Scale: centimeter-authored source, import scale 1.0, preserving female 442 cm and male 470 cm Giant baselines.
- Collision type: disabled.
- LOD plan: LOD0-LOD3 required for any important future static variant.
- Material slots: 1 target.
- Texture list, planning only: `T_GIA_BloodAxeDryChannelBrokenGapAshFill_A01_BC`, `T_GIA_BloodAxeDryChannelBrokenGapAshFill_A01_N`, `T_GIA_BloodAxeDryChannelBrokenGapAshFill_A01_ORM`; no baseline emissive texture.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: use as static visual residue only, keep triangles low, share material vocabulary with the dry channel kit, keep collision disabled, and avoid runtime behavior.

These notes do not select an implementation target and do not authorize source, export, engine, runtime, material, VFX, audio, validator, gameplay, collision, or startup-scene work.

## Folder and Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeDryChannelBrokenGapAshFill_A01/PRODUCTION_PACKAGE.md`

Future planning names only:

- Static mesh: `SM_GIA_BloodAxeDryChannelBrokenGapAshFill_A01`
- Texture base color: `T_GIA_BloodAxeDryChannelBrokenGapAshFill_A01_BC`
- Texture normal: `T_GIA_BloodAxeDryChannelBrokenGapAshFill_A01_N`
- Texture packed ORM: `T_GIA_BloodAxeDryChannelBrokenGapAshFill_A01_ORM`
- Parent kit: `KIT_GIA_BloodAxeDryChannelStoneSet_A01`
- Parent intake row: `BloodAxeDryChannelStoneSet_A01#AshFill_BrokenGap_A01`
- Material policy reference: `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01`
- LOD/collision policy reference: `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`
- Review-row reference: `DOC_GIA_BloodAxeDryChannelStoneReviewRows_A01`

Do not create or edit `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, external concept folders, global indexes, task boards, backlog docs, bootstrap docs, child intake docs, unrelated production packages, validators, startup placement files, source folders, DCC files, FBX files, Unreal files, images, material graphs, VFX/audio assets, gameplay system files, or any file outside this package path from this task.

## Quality Gate Checklist

- Package uses the 15-section Aerathea universal production package format.
- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, material graph, VFX/audio asset, global index, task board, backlog, bootstrap, child intake doc, image, or unrelated package file.
- Asset identity is `SM_GIA_BloodAxeDryChannelBrokenGapAshFill_A01` under `KIT_GIA_BloodAxeDryChannelStoneSet_A01`.
- Giant scale lock is explicit: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Broken-gap ash fill remains static, matte, dry, shallow, non-emissive, non-liquid, non-interactive, and non-gameplay.
- Gameplay volumes, damage paths, readable runes, particle VFX, liquid surfaces, aura materials, material graph authoring, collision, VFX/audio, interaction behavior, startup placement, implementation claims, and implementation target selection are excluded.
- No ritual gameplay, offering mechanics, activation states, puzzle states, quest/UI markers, objective markers, waypoint behavior, navigation/pathfinding, traversal proof, encounter behavior, AI behavior, pickup/loot behavior, resource/crafting/economy behavior, destructible behavior, physics behavior, or material-state behavior is defined.
- Materials follow cold ash, soot, charcoal dust, cave grit, subtle mud contamination, chipped stone grit, and restrained oxide red dusting only.
- Default emissive, ritual glow, signal glow, shamanic glow, wet material, active flame, animated material state, UI-like marker, readable text, and neutral/civilized Giant material defaults are absent.
- Fine ash grains, soot flecks, powder, small grit, hairline cracks, mud specks, and surface dust are assigned to future texture or normal detail, not dense geometry.
- Triangle budgets, LOD0-LOD3 policy, no-collision limits, animation limits, Unreal import planning, folder naming, material slot target, and texture-map planning are included without implementation claims.
