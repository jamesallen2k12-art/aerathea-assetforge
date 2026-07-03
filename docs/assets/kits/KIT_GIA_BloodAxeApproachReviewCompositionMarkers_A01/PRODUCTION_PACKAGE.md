## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01`
- Asset type: Production kit / docs-only non-shipping review composition marker plan
- Parent route: `KIT_GIA_BloodAxeStrongholdApproach_A01#Review_CompositionMarkers`
- Source route reference: `BloodAxeStronghold.png#Review_CompositionMarkers` as split by the existing stronghold approach child intake
- Related planning docs: `KIT_GIA_BloodAxeStrongholdApproach_A01`, `KIT_GIA_BloodAxeFormationDressing_A01`, `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeArmory_A01`, `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeTrophyGate_A01`, and `SM_GIA_BloodAxeWatchPlatform_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only package ready for planning review; no DCC, FBX, Unreal Content, Unreal actor, runtime source, validator, capture automation, startup scene, final visual signoff, nav/pathfinding, source concept movement, final stronghold approval, or first implementation target is created or claimed
- Source-storage guardrail: external source concepts remain outside the repository. Do not copy, move, edit, embed, crop, rename, inspect for final approval, or commit source concepts for this package.

`KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01` defines non-shipping planning aids for future review composition of the Blood Axe stronghold approach. The kit covers height rods, cliff silhouette blocks, palisade silhouette blocks, gate-frame thumbnails, ground ticks, scale rods, camera-composition notes, material discipline markers, and LOD/collision planning rows. These are review aids only; they are not final environment assets, gameplay markers, encounter diagrams, validator targets, capture tools, or review-scene actors.

Blood Axe visual language must remain separate from neutral/civilized Giant culture. Blood Axe is a hostile Giant sub-faction tied to rough cliffs, raw palisades, blackened iron, chained scrap, scorched hide, soot, ash, oxide red cloth, and sparse non-graphic warnings. Neutral/civilized Giant culture remains tied to hidden mountain settlements, master stonework, blue-gray masonry, terraces, waterworks, warm hearth light, restrained blue runes, and civic stoneworker identity.

## Gameplay Purpose

The gameplay purpose is planning support only. The kit helps future art direction and production review teams judge scale, framing, silhouette balance, and material discipline for the Blood Axe stronghold approach without creating any playable asset or implementation dependency.

Allowed planning uses:

- Show female and male Giant baselines beside approach cliff, palisade, and gate-framing silhouettes.
- Keep Blood Axe approach composition readable at MMO camera distance before any DCC or Unreal work begins.
- Clarify whether cliff mass, palisade height, gate-facing compression, red cloth rhythm, and ground scale markers support the hostile approach read.
- Provide notes for future A/B composition planning without making camera actors, capture automation, validators, startup-scene edits, or final approval images.
- Route future rows into package planning only if a lead task explicitly expands the docs-only scope.

Out of scope:

- Unreal actor creation, validator creation, capture automation, startup scene work, final visual signoff, nav/pathfinding, DCC, FBX, Unreal import, runtime source, external source concept movement, final stronghold approval, or first implementation target selection.
- Encounter routes, AI spaces, patrol logic, spawn logic, climb logic, path widths as gameplay values, destructible behavior, cover rules, gate behavior, objective markers, loot, crafting, economy, resource behavior, VFX, audio, or interaction behavior.
- Any claim that markers, rods, thumbnails, or ticks are shipping environment content.

## Silhouette Notes

The marker kit should read as a clean review overlay for a hostile Blood Axe approach, not as polished set dressing. Each marker must preserve the primary approach read: vertical cliff mass, rough palisade skyline, gate-facing compression, Giant scale rods, and ground ticks that make the ascent legible.

Planning marker silhouettes:

- Height rods: simple vertical rods or cards for the validated female 442 cm and male 470 cm Giant baselines, with clear top bars and base marks. They must stay visually separate from banners, spears, or shipped poles.
- Cliff silhouette blocks: broad matte proxy slabs that describe expected cliff wall height, overhang pressure, ledge steps, and framing mass without approving terrain sculpt or final cliff art.
- Palisade silhouette blocks: simplified post-line and spike-line proxy blocks that indicate Giant-scale raw-log walls, uneven crowns, diagonal brace mass, and gate-flank pressure without becoming final palisade meshes.
- Gate-frame thumbnails: small composition cards or frame outlines showing how the path, cliff, and palisade aim toward a future gate. They must not approve final gate design, open/close behavior, collision, or stronghold layout.
- Ground ticks: low-profile strips, stones, or flat marks for visual scale and spacing review only. They must not become nav markers, spawn spacing, patrol spacing, collision blockers, or gameplay measurement rules.
- Scale rods: neutral measuring rods for 1 m, 5 m, 10 m, and Giant shoulder/head references when useful. They support scale review only and do not change the Giant scale lock.
- Camera-composition notes: thumbnail frame guides, crop boxes, and line-of-sight notes for docs-only review sheets. They must not become camera actors, capture scripts, startup-scene edits, or validation targets.
- Material discipline markers: swatch cards or small marker tags showing approved Blood Axe material families and banned neutral/civilized Giant cues. They create no materials or textures.
- LOD/collision planning markers: simple labels or planning rows showing which future proxies would need LOD0-LOD3 and collision disabled/simple assumptions if later approved.

Avoid silhouettes that look like UI quest arrows, navigation arrows, tactical maps, spawn points, loot markers, readable combat labels, polished civilized Giant masonry, refined civic stonework, warm hearth props, blue-rune cultural markers, or final Blood Axe stronghold approval.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft and males 14'10"-16'0".
- Author any future source in centimeters. 1 Unreal unit = 1 cm.
- This package does not change Giant race scale, skeleton policy, socket contracts, capsule expectations, body proportions, camera rules, or base proportions.

Planning-only review marker scale targets:

- Female height rod: 442 cm tall, base at ground plane, top bar visible in review composition.
- Male height rod: 470 cm tall, base at ground plane, top bar visible in review composition.
- Optional range ghost rods: 427 cm and 457 cm for female range bounds; 452 cm and 488 cm for male range bounds. Use only in docs/review planning when the range needs checking.
- Cliff silhouette block planning: 1200-2600 cm tall and 900-2200 cm wide, matching the parent approach range without approving terrain or HLOD.
- Palisade silhouette block planning: 700-1100 cm tall to top spikes or cloth; 700-1400 cm wide per visual segment.
- Gate-frame thumbnail planning: use thumbnail frames that imply a gate-facing vertical read around Giant baselines, but do not define final gate clearance, collision, or layout.
- Ground tick planning: 100 cm, 250 cm, and 500 cm visual intervals may be shown for scale review only. They are not nav, spawn, patrol, combat, or collision values.
- Scale rod planning: 1 m, 5 m, 10 m, female baseline, and male baseline rods may be shown together when a future review sheet needs production scale comparison.

All dimensions are visual production planning values only. They are not traversal proofs, nav widths, pathfinding values, encounter lanes, spawn spacing, patrol spacing, camera blockers, collision guarantees, or final stronghold measurements.

## Materials and Color Palette

Review markers should be visually distinct from shipping Blood Axe set dressing while still supporting Blood Axe material discipline.

Marker material direction:

- Matte neutral gray, bone-white, charcoal, and muted oxide red bands for non-shipping rods, silhouette blocks, ground ticks, and frame thumbnails.
- Low contrast surface marks only. Do not add final hand-painted detail, finished grime, trophy ornament, weapon dressing, or polished faction art to marker proxies.
- Use a single review-marker material family if future markers are ever approved, with no emissive by default.

Blood Axe material discipline markers should document these approved families:

- Fractured highland rock, packed earth, mud, ash, soot, slag dust, and charcoal staining.
- Raw dark timber, split logs, charred stakes, rough braces, and buried post feet.
- Blackened iron, dark steel, crude reforged scrap, chain plates, clamp bands, and heavy rings.
- Scorched leather, rawhide lashings, sinew ties, rough rope, and hide wraps.
- Torn oxide red cloth, faded maroon banners, chipped red paint, and dirty red warning strips.
- Sparse aged bone, horn, tusk, old weapon fragments, and broken shield tokens used cleanly and non-graphically.

Banned default reads:

- Neutral/civilized Giant blue-gray civic masonry, refined carved stone, terrace/waterwork forms, warm hearth identity, restrained blue runes, peaceful highland clan markers, or master-stoneworker motifs.
- Ogre Teknomancy, dwarf smith elegance, normal humanoid fortification scale, readable tactical text, UI-like route markers, loot-rarity colors, or dense graphic trophy clutter.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01` for the world of Aerathea. The design should emphasize docs-only non-shipping review composition markers for a hostile Blood Axe Giant stronghold approach, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, approved Giant ranges of females 14-15 ft and males 14'10"-16'0", simple height rods, cliff silhouette blocks, palisade silhouette blocks, gate-frame thumbnails, ground ticks, scale rods, camera-composition note frames, material discipline markers, LOD and collision planning callouts, rough Blood Axe approach language, fractured rock, raw timber, blackened iron, chained scrap, scorched hide, soot, ash, oxide red cloth, and strict separation from neutral/civilized Giant stoneworker culture. Use hand-painted texture detail only on referenced material swatches, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a clean production planning board with rods, proxy blocks, thumbnail frames, ground tick strips, scale references, material swatches, and docs-only stop gates on a neutral background. Avoid copying any existing franchise, avoid source concept embedding, avoid final stronghold approval, avoid final visual signoff, avoid Unreal actor or validator implications, avoid capture automation, avoid startup-scene framing claims, avoid nav/pathfinding arrows, avoid encounter diagrams, avoid AI spaces, avoid gameplay labels, avoid UI quest markers, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, Blender file, terrain sculpt, mesh, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, Unreal actor, material instance, texture asset, Blueprint, validator, runtime source, capture automation, startup placement, final visual signoff, final stronghold approval, or first implementation target is created or authorized.

Future DCC work, if separately approved, should keep markers simple and modular:

- Height rods: straight rods, base plates, and top bars with clear female/male baseline heights. Use geometry only for large read shapes.
- Cliff silhouette blocks: broad blockout slabs with clean planes and large negative-space cuts. No final terrain detail.
- Palisade silhouette blocks: simplified post groups, spike crowns, and brace mass proxies. No per-log final modeling.
- Gate-frame thumbnails: flat cards or frame outlines that can be arranged in docs or review boards. No final gate mesh.
- Ground ticks: flat strips, shallow stones, or small cards that read from the review camera without changing terrain.
- Scale rods: reusable measuring rods with simple subdivision marks. Avoid tiny modeled numerals if a texture or document label can carry the information.
- Camera-composition frames: flat wire/frame cards or document thumbnails only if later approved for a review board.
- Material discipline markers: swatch cards or simple placards for planning references, not material-instance authoring.
- LOD/collision markers: docs-only rows or simple proxy cards that remind future implementers to use LOD0-LOD3 and disabled/simple collision where appropriate.

Use large readable shapes and clean pivots if any future marker assets are approved. Do not spend geometry on small scratches, tiny rivets, rope fibers, cloth weave, ash flecks, pitted metal, little chips, readable text, or detailed Blood Axe dressing on non-shipping markers.

## Texture and Material Notes

This package creates no textures or materials. Future marker assets, if approved by a separate implementation task, should use standard Aerathea texture outputs:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Emissive (`E`) is not used by default and should remain absent for review markers

Candidate future review-marker material family:

- `MI_GIA_BloodAxeApproachReviewMarker_A01`
- `T_GIA_BloodAxeApproachReviewMarker_A01_BC`
- `T_GIA_BloodAxeApproachReviewMarker_A01_N`
- `T_GIA_BloodAxeApproachReviewMarker_A01_ORM`

Material slot targets if future marker meshes are approved:

- Height rods: 1 material.
- Cliff silhouette blocks: 1 material.
- Palisade silhouette blocks: 1 material.
- Gate-frame thumbnails: 1 material.
- Ground ticks: 1 material.
- Scale rods: 1 material.
- Camera-composition frames: 1 material.
- Material discipline markers: 1 marker material plus docs-only swatch references; no material instance creation in this task.
- LOD/collision planning markers: 1 material if ever converted to proxy meshes.

Final Blood Axe material assets remain owned by their future environment, prop, or material packages. This package only records discipline and banned reads.

## Triangle Budget

This package creates no mesh. Future non-shipping marker modules, if separately approved, should stay extremely light:

- Height rod module: 100-600 tris each, 1 material.
- Cliff silhouette block: 100-1k tris each, 1 material.
- Palisade silhouette block: 200-1.5k tris each, 1 material.
- Gate-frame thumbnail/card: 100-800 tris each, 1 material.
- Ground tick strip: 20-200 tris each, 1 material.
- Scale rod module: 100-700 tris each, 1 material.
- Camera-composition frame/card: 100-600 tris each, 1 material.
- Material discipline marker card: 50-300 tris each, 1 material.
- LOD/collision planning card: 50-300 tris each, 1 material.
- Complete review composition marker kit: 2k-10k tris total if assembled as temporary review geometry.

Spend triangles only on readable proxy silhouettes, rod legibility, simple frame edges, and broad block masses. Do not model final cliff cracks, timber grain, per-spike palisade detail, cloth fray, chain links, tiny bolts, ash flecks, pitted metal, or dense Blood Axe dressing for this marker kit.

## LOD Plan

If any future marker meshes are approved, provide LOD0-LOD3 even though they are non-shipping review aids.

- LOD0: full marker read with height rods, scale rods, cliff/palisade proxy shapes, gate-frame cards, ground ticks, camera-composition frames, and material discipline cards.
- LOD1: 60-70 percent of LOD0; simplify bevels, frame edges, rod subdivisions, proxy-card backs, and small tick marks.
- LOD2: 35-45 percent of LOD0; merge small tick marks into larger strips, flatten card frames, reduce rod subdivisions, and simplify silhouette blocks into large planes.
- LOD3: 15-25 percent of LOD0; preserve female/male Giant height read, cliff mass reference, palisade height line, gate-frame relationship, and ground-scale rhythm.

LOD reduction order:

1. Tiny tick subdivisions, small bevels, minor backing geometry, card thickness, and decorative edges.
2. Secondary guide marks, nonessential frame borders, small ground ticks, and backside surfaces.
3. Minor silhouette block cuts, optional range ghost rods, and duplicate marker variants.
4. Only after secondary detail is removed, simplify the main 442 cm and 470 cm rods, cliff/palisade mass read, and gate-frame relationship.

Never destroy the validated Giant scale read, main approach composition, or Blood Axe/civilized Giant separation before removing small marker detail.

## Collision Notes

This package defines no gameplay collision and creates no collision proxies.

Future collision policy, if marker meshes are separately approved:

- Review markers: collision disabled by default.
- Height rods and scale rods: collision disabled; editor selection bounds only if needed.
- Cliff and palisade silhouette blocks: collision disabled for review proxies; do not use as terrain, wall, nav, or traversal collision.
- Gate-frame thumbnails and camera-composition frames: collision disabled.
- Ground ticks: collision disabled; do not affect navigation, pathfinding, spawn spacing, patrol spacing, or movement tests.
- Material discipline and LOD/collision planning cards: collision disabled.

Do not create nav blockers, nav links, smart links, climb volumes, camera blockers, spawn blockers, patrol blockers, encounter lanes, projectile blockers, damage volumes, cover volumes, objective zones, interaction triggers, loot pickup collision, destructible collision, physics bodies, custom UCX meshes, or validator checks from this package.

## Animation Notes

Baseline marker assets are static planning aids.

Allowed at planning level:

- Static height rods, scale rods, silhouette blocks, gate-frame thumbnails, ground ticks, camera-composition frames, material discipline cards, and LOD/collision planning cards.
- Static docs-only notes describing how future review compositions should be judged.

Not authorized:

- Animated markers, capture automation, camera animation, startup-scene camera work, validator-driven marker passes, material pulses, emissive highlights, VFX arrows, signal lights, gameplay state changes, interaction prompts, cloth simulation, physics motion, gate motion, destruction states, or audio cues.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, Unreal actor, material instance, texture, socket, collision proxy, Blueprint, validator, runtime source, capture automation, review-scene actor, startup actor, import script, source asset, or implementation file is created or authorized.

Potential future Unreal folders, approval-gated only:

- Review-only markers: `/Game/Aerathea/Review/Giants/BloodAxe/StrongholdApproach/CompositionMarkers/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/Review/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/Review/`

Candidate future asset names, not implementation targets:

- `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01`
- `SM_GIA_BloodAxeApproachHeightRod_A01`
- `SM_GIA_BloodAxeApproachCliffSilhouetteBlock_A01`
- `SM_GIA_BloodAxeApproachPalisadeSilhouetteBlock_A01`
- `SM_GIA_BloodAxeApproachGateFrameThumbnail_A01`
- `SM_GIA_BloodAxeApproachGroundTick_A01`
- `SM_GIA_BloodAxeApproachScaleRod_A01`
- `SM_GIA_BloodAxeApproachCameraFrame_A01`
- `SM_GIA_BloodAxeApproachMaterialMarker_A01`
- `SM_GIA_BloodAxeApproachLODMarker_A01`

Future import assumptions:

- Asset type: Static Mesh review proxy only if a later task explicitly approves implementation.
- Pivot: base center for rods, ground center for blocks/cards, lower-left or center for thumbnail cards depending on future DCC convention.
- Orientation: face +X for review-facing cards unless future DCC/export work confirms another project convention.
- Scale: centimeter-authored source; Unreal import scale 1.0 after DCC/export approval.
- Collision: disabled.
- LODs: LOD0-LOD3 required before any production import approval.
- Material slot count: 1 marker material for each proxy.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance note: markers remain review-only and non-shipping; remove or exclude them from packaged runtime content unless a future lead-approved task changes scope.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01/CHILD_ASSET_INTAKE.md`
- Parent package: `docs/assets/kits/KIT_GIA_BloodAxeStrongholdApproach_A01/`
- Related marker language: `docs/assets/kits/KIT_GIA_BloodAxeFormationDressing_A01/`

Recommended naming if future work is approved:

- `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01` for the grouped docs-only marker package.
- `SM_GIA_BloodAxeApproach<MarkerPurpose>_A01` for static review proxy modules.
- `DOC_GIA_BloodAxeApproach<PlanningPurpose>_A01` for docs-only notes, thumbnails, and planning rows.
- `MI_GIA_BloodAxeApproachReviewMarker_A01` for a future non-shipping review marker material.
- `T_GIA_BloodAxeApproachReviewMarker_A01_BC`, `T_GIA_BloodAxeApproachReviewMarker_A01_N`, and `T_GIA_BloodAxeApproachReviewMarker_A01_ORM` for future marker textures if separately approved.

Do not create or edit `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, external source concept folders, task board, global indexes, backlog, bootstrap, unrelated production packages, or first implementation target documents from this task.

## Quality Gate Checklist

- Package uses the universal 15 headings exactly and remains docs-only.
- Only the production package and child intake in `docs/assets/kits/KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01/` are changed by this task.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Package covers height rods, cliff silhouette blocks, palisade silhouette blocks, gate-frame thumbnails, ground ticks, scale rods, camera-composition notes, material discipline markers, and LOD/collision planning.
- Markers are non-shipping planning aids and do not become final environment art, gameplay markers, UI markers, nav/pathfinding markers, encounter markers, capture tools, validators, startup-scene actors, or review-scene actors.
- No Unreal actor creation, validator creation, capture automation, startup scene work, final visual signoff, nav/pathfinding, DCC, FBX, Unreal import, source concept movement, final stronghold approval, or first implementation target selection is claimed.
- Materials follow Blood Axe discipline: fractured rock, packed earth, raw timber, blackened iron, dark steel, chained scrap, scorched hide, soot, ash, oxide red cloth, and sparse non-graphic bone/horn warnings.
- Banned neutral/civilized Giant cues remain absent: blue-gray civic masonry, refined stonework, terraces, waterworks, warm hearth identity, restrained blue runes, and civic stoneworker motifs.
- Default emissive, gameplay VFX, animation, readable tactical labels, UI quest markers, loot-rarity colors, final gate approval, and final stronghold approval are absent and approval-gated.
- Triangle budgets, material slot targets, texture naming, LOD0-LOD3 planning, collision-disabled policy, animation limits, Unreal import planning, folder naming, and stop gates are included.
