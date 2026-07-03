# SM_GIA_BloodAxeShelter_Longhouse_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeShelter_Longhouse_A01`
- Asset type: Static Mesh production package / Giant-scale hostile camp longhouse shelter
- Task: `AET-MA-20260629-115`
- Parent kit: `KIT_GIA_BloodAxeCamp_A01`
- Related shelter kit: `KIT_GIA_BloodAxeCampShelters_A01`
- Source child ID: `BloodAxeCamp.png#Shelter_RawhideLonghouse`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only static visual production package ready for planning review
- Source-storage guardrail: source concepts remain external through existing intake records. Do not copy, move, crop, edit, embed, inspect for final approval, or commit source images from this package.

`SM_GIA_BloodAxeShelter_Longhouse_A01` defines a large occupied Blood Axe Giant raider shelter: a crude longhouse-shaped camp structure with a heavy hide roof, oversized timber ribs, wide Giant entrance clearance, soot-darkened panels, mud-packed ground contact, red warning cloth, blackened hardware, and hard-used shelter clutter. It should read as a hostile war-camp living structure from MMO camera distance, not as neutral or civilized Giant cave-town architecture.

This package is static visual production planning only. It does not authorize DCC source creation, FBX export, Unreal Content creation, material graph authoring, modular snapping implementation, collision proxy creation, cloth or physics setup, shelter interaction, destructible behavior, startup placement, first build target selection, final visual approval, or source concept movement.

## Gameplay Purpose

The longhouse supports future Blood Axe camp readability and environmental storytelling. Its gameplay-facing purpose is visual only: players should understand that hostile Giant raiders occupy the camp through the oversized shelter footprint, Giant-scale entrance, sleeping/living-zone implications, soot, dirt, crude repairs, and Blood Axe red identifiers.

Expected static uses:

- Primary occupied shelter silhouette for Blood Axe camp living zones.
- Large structure near camp paths, sentry points, cooking pits, forge yards, and raider staging areas.
- Scale reference for Giant-sized shelter entrances, roof height, bedding volume, support ribs, and interior implied clearance.
- Visual continuity with `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeCampShelters_A01`, `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeWatchPlatform_A01`, and Blood Axe armory material language.

Out of scope: player shelter interaction, entering/resting logic, storage, loot, search behavior, crafting, resource collection, camp alarms, destructible tents, fire spread, cloth simulation, physics, gameplay cover tagging, navmesh policy, AI patrols, encounter scripting, VFX, audio, startup placement, final camp composition approval, or first DCC target selection.

## Silhouette Notes

Primary silhouette: a long, low, brutal shelter with a broad hide roof stretched over exposed timber ribs, heavy end frames, a wide front entrance, dark interior mouth, and rough defensive dressing. It should feel built by raiders with huge logs, stitched hides, scavenged metal, and brute-force repairs rather than by master Giant stoneworkers.

Key visual reads:

- Longhouse footprint with a stretched oval, wedge, or shallow barrel profile rather than a small tent shape.
- Dominant roof mass made from broad rough hide panels, fur-edged patches, soot stains, and static torn flaps.
- Exposed timber ribs or A-frame bents spaced along the length, large enough to read from distance.
- Massive front entrance with clear Giant-scale passage, dark inner silhouette, thick side posts, and lifted hide flaps.
- Rear end cap or closed back frame with visible lashings, patched hide, and soot-darkened wear.
- Ground-contact base with packed mud, log skids, large stakes, rough stone weights, and dirt buildup.
- Sparse Blood Axe identifiers: torn red warning cloth, oxide-red slash marks, blackened iron clamps, and one to three non-graphic horn, bone, or broken-armor markers.
- Shelter-adjacent static dressing such as bundled hides, bedding rolls, leaning barricade boards, or tool hooks kept secondary to the main shelter shape.

Model the roof mass, timber ribs, main entrance frame, thick stakes, large lashings, major cloth tears, broad red cloth pieces, blackened metal clamps, and large ground-contact forms as real geometry. Use textures and normal maps for hide grain, cloth weave, stitching, small scratches, soot streaks, mud spatters, wood grain, fine cracks, rope fibers, tiny nail heads, and edge wear.

Avoid neutral/civilized Giant cave-town language: no blue-gray monumental masonry, refined terraces, carved civic stone, orderly hearth-hall warmth, restrained blue runes, clean highland clan banners, or master-stoneworker pride. Also avoid dense trophy clutter, graphic gore, hundreds of modeled stitches, and noisy small props that harm the main longhouse read.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant range: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Recommended production dimensions:

- Overall length: 1800-2600 cm.
- Overall width: 900-1400 cm.
- Overall roof height: 620-850 cm at ridge or highest rib.
- Interior standing clearance near centerline: 540-680 cm, planned against the 470 cm male Giant baseline plus helmet, shoulder, and carried-gear allowance.
- Main entrance clear height: 560-700 cm under lifted hide, lintel, or entrance rib.
- Main entrance clear width: 420-620 cm between inner posts or flap edges.
- Secondary service opening, if included visually: 360-480 cm high and 260-420 cm wide, not guaranteed playable.
- Timber rib diameter: 35-75 cm for visible roof ribs, with 80-120 cm anchor posts permitted.
- Ridge pole or top spine: 50-100 cm thick.
- Roof hide panel thickness read: 8-20 cm at silhouette folds, with actual cloth thickness stylized but not overbuilt.
- Ground stakes and tie-downs: 80-220 cm exposed height.
- Red cloth markers: 120-320 cm long, broad enough to read at camp distance.
- Recommended clear work/circulation apron around entrance: 250-400 cm, with nearby main camp paths preserving the 500-800 cm path width from `KIT_GIA_BloodAxeCamp_A01`.

The entrance should be checked against the 470 cm male Giant baseline first. Smallfolk should feel like trespassers entering an enemy Giant shelter. Do not shrink the longhouse toward normal humanoid scale and do not adjust the validated Giant scale lock to fit a later layout.

## Materials and Color Palette

Primary Blood Axe materials:

- Rough rawhide, patched leather, scorched hide panels, fur-edged seams, sinew cord, thick rope, and static torn flaps.
- Dark timber, split logs, charred pole ribs, bark remnants, rough skids, and uneven ground stakes.
- Blackened iron, dark steel, reforged scrap plates, crude clamp bands, large rings, and heavy tie hardware.
- Torn red war cloth, oxide-red painted slashes, faded maroon repair patches, and dirty warning strips.
- Packed mud, dried dirt, soot, ash, grease, charcoal staining, and rain-darkened grime.
- Sparse bone, horn, broken shield, or large tooth markers used as secondary silhouette accents only.

Palette targets:

- Dominant: soot brown, dark umber hide, charcoal black, gray-brown timber, mud brown, and dirty leather tan.
- Faction accent: deep oxide red, rubbed maroon, and dark red cloth patches.
- Metal accent: dull gunmetal, blackened iron, worn steel edge highlights.
- Bone accent: muted ivory and gray bone in small amounts.
- Emissive: none for the baseline longhouse.

Avoid one-note red presentation. Blood Axe identity should come from crude hostile construction, red accents, soot, dirt, and blackened hardware together, not from painting the whole shelter red. Any ritual, shamanic, firelit, lamp, or emissive shelter variant requires a separate approval-gated package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeShelter_Longhouse_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant raider longhouse shelter, a long low occupied shelter silhouette, a heavy rawhide roof stretched over huge timber ribs, a wide Giant-scale entrance with dark interior mouth, soot-dark hide panels, mud-packed base, rough log skids, blackened iron clamps, thick lashings, torn red warning cloth, sparse non-graphic horn or bone territory markers, bundled hides and static shelter dressing, hostile Blood Axe sub-faction identity, and the gameplay role of static enemy-camp living-zone environment dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh production sheet with front, side, rear, top footprint, and three-quarter views, scale bars beside a 442 cm female Giant and a 470 cm male Giant, entrance clearance callouts, material swatches, LOD planning notes, simple collision intent callouts, and a clear note separating Blood Axe raider culture from neutral/civilized Giant cave-town culture. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe language the default Giant culture, avoid shelter interaction diagrams, avoid destructible or cloth-simulation claims, avoid modular snapping implementation claims, avoid final visual approval claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeCamp.png#Shelter_RawhideLonghouse` only through existing intake documentation. It does not inspect, move, copy, crop, embed, or approve external source concept art.

## Modeling Notes

This package is a planning document only. Future DCC work requires a separate approved task before any source folders, Blender files, proof renders, collision proxies, LOD sources, variant exports, or FBX files are created.

Future modeling should prioritize these readable forms:

- Long continuous shelter body with a clear front entrance, rear closure, roof ridge, and broad ground footprint.
- Large roof hide sheets shaped as static geometry with bold folds, overlaps, and a few readable tears.
- Exposed timber rib sequence along the shelter length, including heavy front and rear frames.
- Ridge pole, side rails, anchor posts, ground stakes, tie-down logs, and log skids that show Giant-scale construction.
- Lifted front flap or hide curtain as a fixed static shape, not simulated cloth.
- Thick lashings, large rope wraps, and crude blackened iron clamps where they affect silhouette or structural read.
- Broad red warning cloth patches, tied strips, or painted slashes positioned for long-distance Blood Axe recognition.
- Mud-packed base, soot-dark entry edges, ash staining near vents or smoke holes, and dirt buildup at contact points.
- Optional simple smoke-hole flap or roof vent shape, static and non-emissive.
- Sparse non-graphic horn, bone, or broken armor markers kept secondary and readable.
- Minimal shelter-adjacent dressing such as two or three hide rolls, a bedding bundle, or a leaning board cluster if it helps occupancy read without becoming a separate clutter kit.

Use textures, normals, and AO for:

- Fine hide grain, leather pores, cloth weave, stitching, small fray, tiny cuts, soot gradients, rain streaks, mud splatter, wood grain, bark roughness, small scratches, metal pitting, red paint flakes, and small nail heads.

Simplification rules:

- Keep the longhouse body as the primary read; do not collapse the shelter into a full camp scene.
- Keep roof ribs chunky and few enough to read clearly from the game camera.
- Keep red cloth accents large and directional instead of many tiny strips.
- Keep trophies sparse and non-graphic.
- Do not model every stitch, rope strand, hide pore, scratch, splinter, ash fleck, or mud clump.
- Do not define snap modules, snap sockets, grid dimensions, DCC variant manifests, collision proxies, cloth simulation meshes, or interactive flap separation in this package.

## Texture and Material Notes

Target material slot count:

- Preferred: 3 material slots.
- Maximum: 4 material slots if a later hero-route longhouse needs separate metal or bone treatment.

Recommended material slots:

- Slot 0: `MI_GIA_BloodAxeHideLeather_A01` or `MI_GIA_BloodAxeScorchedHide_A01` for roof hide, patched leather, fur edges, and static flaps.
- Slot 1: `MI_GIA_BloodAxeRoughTimber_A01` or `MI_GIA_BloodAxeScorchedWood_A01` for ribs, posts, skids, stakes, and braces.
- Slot 2: `MI_GIA_BloodAxeRedCloth_A01` for warning cloth, repair patches, and painted identity accents.
- Optional Slot 3: `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeBlackenedIron_A01`, or `MI_GIA_BloodAxeBoneTrophy_A01` only if separation materially improves reuse or readability.

Required future texture maps:

- `T_GIA_BloodAxeShelter_Longhouse_A01_BC`
- `T_GIA_BloodAxeShelter_Longhouse_A01_N`
- `T_GIA_BloodAxeShelter_Longhouse_A01_ORM`

Optional future texture maps only after separate approval:

- `T_GIA_BloodAxeShelter_Longhouse_A01_E` for a ritual, shamanic, lamp, firelit, or magical variant. The baseline longhouse has no emissive.
- `T_GIA_BloodAxeShelter_Longhouse_A01_Mask` if future material variation needs controlled mud, soot, red paint, edge wear, or hide color blending.

Texture set targets:

- Standard longhouse: 2K texture set with shared trim or tiling support.
- Hero camp-route longhouse: 2K with additional masks; 4K only with explicit hero approval.
- Far dressing variant: 1K with simplified roof, rib, and red cloth reads.

Packed ORM guidance:

- R: Ambient occlusion under hide overlaps, rib contact points, entrance flaps, lashings, ground stakes, skids, and mud buildup.
- G: Roughness high for hide, cloth, timber, soot, mud, and bone; medium-high varied roughness for blackened iron.
- B: Metallic only on iron, steel, chain, clamp, ring, and reforged scrap zones.

No material graph, animated cloth shader, wind deformation, emissive timing, smoke VFX, fire VFX, or runtime material-state authoring is included in this package.

## Triangle Budget

`SM_GIA_BloodAxeShelter_Longhouse_A01` is a large occupied camp shelter and should fit between large prop and small/medium building ranges while staying static and repeatable.

Targets:

- LOD0 target: 18k-28k tris.
- LOD0 hard cap: 32k tris.
- Material slots: 3 target, 4 maximum.
- Texture set: 2K standard; 4K only with explicit hero approval.

Suggested LOD0 allocation:

- Main shelter body, roof hide sheets, entrance flaps, and rear closure: 35-45 percent.
- Timber ribs, ridge pole, anchor posts, skids, stakes, and braces: 30-35 percent.
- Large lashings, blackened clamps, red cloth patches, and major repair forms: 10-15 percent.
- Ground-contact mud forms, sparse trophies, static shelter dressing, and silhouette accents: 8-12 percent.
- Minor bevels, asymmetry, and edge breakup: remaining budget only after the primary form reads clearly.

Variant guidance:

- Simpler repeated camp longhouse: 14k-20k tris.
- Default occupied longhouse: 18k-28k tris.
- Hero-route longhouse with stronger entrance dressing: 26k-32k tris, approval-gated.
- Far camp shell: keep under 12k tris and rely on shared materials, baked detail, and LODs.

Spend geometry on the roofline, entrance clearance read, rib rhythm, major support posts, broad flap shapes, and silhouette-level wear. Do not spend geometry on dense stitching, small fray fibers, per-rope strands, tiny scratches, many small hanging strips, dense trophy piles, or individual dirt clods.

## LOD Plan

All future approved mesh work should include LOD0-LOD3.

- LOD0: 18k-28k tris target, 32k hard cap. Full longhouse silhouette, roof hide sheets, timber ribs, entrance frame, static flaps, skids, stakes, large lashings, blackened hardware, red cloth, ground-contact wear, and sparse markers.
- LOD1: 60-70 percent of LOD0. Reduce minor hide folds, small cloth tears, secondary lashings, small rib bevels, underside cuts, ground clutter, and back-facing dressing.
- LOD2: 35-45 percent of LOD0. Preserve long roofline, entrance mouth, rib rhythm, red cloth blocks, major support frame, and mud base while flattening small folds, clamps, and secondary stakes.
- LOD3: 15-25 percent of LOD0. Preserve the long occupied shelter mass, dark entrance, Giant-scale proportions, red/black Blood Axe read, and primary roof profile. Remove most small hardware, lashings, trophies, inner detail, and ground dressing.

Reduction order:

1. Tiny stitches, fray cuts, nail heads, small scratches, soot speckles, mud flecks, and metal pitting.
2. Minor cloth holes, small roof-edge tears, small red strips, and tiny hide patches.
3. Secondary lashings, small straps, small clamps, and non-structural rope wraps.
4. Backside dressing, underside details, hidden interior geometry, and small shelter clutter.
5. Secondary rib bevels, minor stake subdivisions, trophy undercuts, and ground debris.
6. Only then reduce the main roofline, entrance frame, primary timber ribs, ridge pole, support posts, and broad Blood Axe red-cloth read.

Never reduce the primary longhouse silhouette, Giant entrance clearance, dark shelter-mouth read, roof rib rhythm, or Blood Axe red identity before removing small detail.

## Collision Notes

Collision is planning only. Do not create collision proxies, UCX meshes, physics bodies, cloth collision, nav policy, destructible chunks, interaction volumes, gameplay cover tags, or validation scripts from this task.

Future static collision intent:

- Main shelter body: simple boxes or low-count convex hulls around blocked side walls and rear closure.
- Roof: simplified hulls only where player traversal or camera collision requires it; no per-hide-fold collision.
- Entrance frame: simple side-post blockers and optional lintel/upper frame hull while preserving planned Giant visual clearance.
- Static entrance flap: collision disabled by default unless a later traversal task approves a blocker.
- Timber ribs, stakes, skids, and braces: fold into simplified hulls where they affect movement; no per-rib collision unless a major exposed rib blocks traversal.
- Ground-contact mud, ash, and dirt blend: no collision unless raised enough to affect movement.
- Red cloth, ropes, lashings, small trophies, rings, chains, and minor hardware: no collision.
- Shelter-adjacent dressing: disabled by default for small props; one simple box or hull for large blocking bundles only.

Future implementation must decide whether the longhouse is pure backdrop, a static blocker with visible entrance, or an enterable shell. This package does not define navmesh behavior, AI routes, patrol points, interior gameplay, cover tags, door/flap states, interaction traces, destruction, damage, fire spread, or traversal policy.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh visual planning.
- Fixed roof hide, fixed entrance flap, fixed ribs, fixed lashings, fixed red cloth, and fixed shelter dressing.
- Optional future material variation for soot, dirt, red paint, hide color, or timber age documented as approval-gated only.

Approval-gated future work:

- Cloth simulation, wind animation, vertex sway, rope physics, hanging prop sway, moving flaps, opening/closing entrance covers, collapse states, destructible shelter pieces, fire spread, smoke, ember glow, VFX, audio, or runtime material-state animation.
- Shelter interaction, rest logic, storage, loot/search behavior, quest objective logic, camp alarm logic, AI occupation behavior, encounter behavior, gameplay cover, nav blocking, or interior traversal.

Any moving, interactive, destructible, VFX-driven, or enterable gameplay version should be split into a separately named package or implementation task so `SM_GIA_BloodAxeShelter_Longhouse_A01` remains a lightweight static camp shelter plan.

## Unreal Import Notes

No Unreal import is authorized by this docs-only package. The following notes are future planning only.

Planned future import target:

- Folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/Shelters/`
- Mesh: `SM_GIA_BloodAxeShelter_Longhouse_A01`
- Asset type: Static Mesh
- Pivot: ground-contact center of the longhouse footprint, with +Z up.
- Orientation: primary entrance/read faces +X unless a future project import convention overrides it.
- Scale: centimeter-authored source, import at scale 1.0 after future DCC/export approval.
- Bounds: include roof ridge, static flaps, red cloth, side stakes, and sparse silhouette markers.
- Collision: simple custom collision or generated primitive collision as described above after approval.
- LODs: import LOD0-LOD3 if and when mesh work is approved.
- Material slot count: 3 target, 4 maximum.
- Blueprint behavior: none.
- Runtime interaction: none.
- Startup placement: none.

Default material family references:

- `MI_GIA_BloodAxeHideLeather_A01`
- `MI_GIA_BloodAxeScorchedHide_A01`
- `MI_GIA_BloodAxeRoughTimber_A01`
- `MI_GIA_BloodAxeScorchedWood_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeReforgedMetal_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`

Texture list:

- `T_GIA_BloodAxeShelter_Longhouse_A01_BC`
- `T_GIA_BloodAxeShelter_Longhouse_A01_N`
- `T_GIA_BloodAxeShelter_Longhouse_A01_ORM`

Optional future textures:

- `T_GIA_BloodAxeShelter_Longhouse_A01_E` only for a separately approved emissive/firelit/ritual variant.
- `T_GIA_BloodAxeShelter_Longhouse_A01_Mask` only if a later material variation pass is approved.

Potential visual-only locator names, if a later task approves attachment planning:

- `entrance_marker_visual`
- `roof_smokehole_visual`
- `hide_bundle_visual_l`
- `hide_bundle_visual_r`
- `red_cloth_marker_visual`

These names are planning notes only. Do not author sockets, snap points, Blueprint behavior, VFX hooks, gameplay interactions, material graphs, validators, or startup-scene placement from this package.

## Folder and Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeShelter_Longhouse_A01/PRODUCTION_PACKAGE.md`

Related planning docs:

- `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeCampShelters_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeCampShelters_A01/CHILD_ASSET_INTAKE.md`

Planned future source/export paths, pending separate approval:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeShelter_Longhouse_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeShelter_Longhouse_A01.fbx`
- Unreal: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/Shelters/`

Naming:

- Static mesh: `SM_GIA_BloodAxeShelter_Longhouse_A01`
- Optional cold/unoccupied visual variant, if later approved: `SM_GIA_BloodAxeShelter_Longhouse_Empty_A01`
- Optional hero-route visual variant, if later approved: `SM_GIA_BloodAxeShelter_Longhouse_Hero_A01`
- Related but separate child candidates: `SM_GIA_BloodAxeShelter_LeanTo_A01`, `SM_GIA_BloodAxeShamanHut_A01`, `KIT_GIA_BloodAxeShelterClutter_A01`
- Material instance: `MI_GIA_BloodAxeShelter_Longhouse_A01`
- Required textures: `T_GIA_BloodAxeShelter_Longhouse_A01_BC`, `T_GIA_BloodAxeShelter_Longhouse_A01_N`, `T_GIA_BloodAxeShelter_Longhouse_A01_ORM`
- Optional future emissive texture: `T_GIA_BloodAxeShelter_Longhouse_A01_E`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, tools, validators, material graphs, startup-scene actors, copied source concepts, global index entries, task-board edits, production backlog edits, modular snapping data, collision proxy files, cloth setup, physics setup, destructible setup, shelter interaction setup, first build target selection, or final visual approval from this task.

## Approval Gates and Stop Points

- Stop before any DCC source, Blender file, proof render, FBX export, Unreal Content asset, runtime source, Blueprint, tool, validator, material graph, VFX asset, audio asset, or startup-scene placement work.
- Stop before creating source folders, source meshes, LOD sources, variant export manifests, collision proxy meshes, UCX files, physics bodies, cloth assets, snap sockets, snap grids, snap validators, or placement validators.
- Stop before copying, moving, cropping, editing, embedding, inspecting for final approval, or committing external source concept images.
- Stop before selecting this longhouse as a first DCC build target.
- Stop before claiming final visual approval, final camp composition approval, first playable approval, implementation readiness, or Unreal readiness.
- Stop before defining shelter interaction, rest/sleep behavior, storage, loot, search behavior, crafting, resource gathering, salvage, economy, vendor behavior, pickup behavior, quest objective behavior, camp alarm behavior, AI occupation, encounter logic, cover rules, navmesh policy, or gameplay collision channels.
- Stop before defining moving flaps, cloth simulation, wind animation, vertex sway, rope physics, destructible shelter states, collapse states, fire spread, smoke, embers, firelight, animated emissive, particle systems, audio cues, or material-state timing.
- Stop if Blood Axe red-black raider language starts replacing neutral/civilized Giant stoneworker, cave-town, highland nomad, or warm hearth language.
- Stop if the shelter starts reading as neutral Giant domestic architecture, polished highland craft, a refined lodge, or a normal humanoid tent scaled up.
- Stop if future scale checks conflict with the validated Giant scale lock: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Stop if material count exceeds 4 slots or LOD0 exceeds 32k tris without explicit hero-longhouse approval.

## Quality Gate Checklist

- Asset is a hostile Blood Axe Giant sub-faction shelter, not neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Primary silhouette reads at MMO distance as a long occupied Blood Axe shelter with broad hide roof, timber ribs, dark Giant entrance, heavy stakes, ground mud, blackened hardware, and restrained red cloth.
- Scale planning includes overall footprint, roof height, interior standing clearance, main entrance clearance, rib thickness, stake scale, and entrance apron planning against the 470 cm male Giant baseline.
- Materials use rough hide, patched leather, scorched timber, blackened iron, reforged scrap, red cloth, soot, ash, mud, grime, and sparse non-graphic bone/horn markers consistently.
- Emissive, firelight, smoke, ritual glow, shamanic states, magical shelter variants, VFX, audio, and material animation are absent by default and approval-gated.
- Tiny stitches, fray, scratches, soot speckles, hide grain, wood grain, rope fibers, metal pitting, mud flecks, and small nail heads are assigned to textures or normals instead of geometry.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision planning, animation limits, Unreal import planning, folder naming, approval gates, and explicit stop points are included.
- Collision remains simple planning only and contains no interaction, cloth, physics, destructible, cover, navmesh, AI, damage, fire, pickup, loot, rest, storage, or gameplay volumes.
- Package remains static visual planning only and makes no DCC, FBX, Unreal Content, SourceAssets, collision proxy, runtime, validator, startup placement, modular snapping, cloth/physics setup, destructible behavior, shelter interaction, first build target, final visual approval, global index edit, task-board edit, production backlog edit, or source concept movement claim.
