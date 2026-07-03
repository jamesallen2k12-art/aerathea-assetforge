# KIT_GIA_BloodAxeStrongholdApproach_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeStrongholdApproach_A01`
- Asset type: Production kit / docs-only environment approach planning package
- Task: `AET-MA-20260629-114`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Gate_StrongholdApproach`
- Source route reference: `BloodAxeStronghold.png#Gate_StrongholdApproach` as listed by the existing Blood Axe camp intake docs
- Related planning docs: `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeWarband_A01`, `KIT_GIA_BloodAxeFormationDressing_A01`, `KIT_GIA_BloodAxeArmory_A01`, `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeTrophyGate_A01`, and `SM_GIA_BloodAxeWatchPlatform_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready for planning review; no DCC, FBX, Unreal Content, source asset, runtime source, validator, startup placement, implementation target, final visual approval, or final stronghold approval is created or claimed
- Source-storage guardrail: external source concept images remain outside the repository. Do not copy, move, edit, embed, crop, rename, inspect for final approval, or commit external source concepts for this package.

`KIT_GIA_BloodAxeStrongholdApproach_A01` defines the hostile approach outside a Blood Axe Giant stronghold: steep cliff wall segments, rough palisade wall runs, switchback path sections, warning markers, overlook silhouettes, chained plate and barricade accents, and visual gate relationship planning. The package stops at the approach zone. It does not approve the final stronghold, interior, courtyard, boss space, encounter route, gate behavior, nav path, or any playable implementation.

Blood Axe visual language must remain a raider sub-faction read. Use red warning cloth, blackened iron, rough timber, scorched hide, soot, ash, chained scrap, and sparse non-graphic trophy markers. Do not let this package redefine neutral or civilized Giant culture, which remains tied to hidden highland settlements, master stonework, blue-gray masonry, terraces, waterworks, warm hearth light, restrained blue runes, and civic stoneworker identity.

## Gameplay Purpose

The gameplay purpose is visual and production planning only. This kit gives future Blood Axe exterior layouts a readable hostile approach before the viewer reaches any gate, wall, or stronghold structure. It supports environment composition, scale planning, and child package routing without defining gameplay behavior.

Allowed planning uses:

- Establish the visual build-up to a Blood Axe stronghold gate without approving the stronghold itself.
- Define modular cliff, palisade, switchback path, warning marker, overlook, barricade, and review-marker lanes.
- Keep Giant scale, material discipline, LOD, collision, and Unreal import assumptions aligned with existing Blood Axe camp and formation docs.
- Clarify how the approach should frame existing or future gate assets such as `SM_GIA_BloodAxeCampGate_A01` and `SM_GIA_BloodAxeTrophyGate_A01`.
- Provide non-shipping review composition markers for later A/B planning if a future task approves them.

Out of scope:

- Final stronghold approval, final visual approval, first playable approval, source concept approval, DCC target selection, source folders, Blender files, proof renders, FBX exports, Unreal imports, material graphs, validators, startup placement, runtime source, Blueprints, nav/pathfinding, encounter scripting, AI patrols, spawn logic, combat rules, loot, crafting, economy, resource behavior, destructible behavior, gate interaction, objective logic, VFX, audio, or implementation claims.

## Silhouette Notes

The approach should read as a hostile vertical threshold carved into Blood Axe territory, not as a full fortress package. The main read is the compression between rough cliff mass, oversized palisade silhouettes, switchback path ledges, warning markers, and a distant gate relationship.

Primary silhouette goals:

- Cliff wall segments: tall broken rock slabs, harsh vertical faces, stepped ledges, overhang shadows, and large angular cuts. Keep the cliff readable as a terrain-adjacent modular wall, not a sculpted final landscape.
- Rough palisade walls: Giant-scale raw logs, uneven spike crowns, heavy diagonal braces, broad blackened iron bands, chained scrap plates, and torn red cloth breaks.
- Switchback path sections: wide trampled shelves, hairpin turns, mud-packed ramps or stepped plateaus, log edging, stone chocks, and visual drop-offs that imply a difficult ascent without defining navigation.
- Warning markers: tall stakes, red cloth strips, bone/horn markers, broken shield tokens, blade fragments, and cairn-like piles used sparingly and non-graphically.
- Overlook silhouettes: crude ledge posts, watch-platform outlines, banner poles, rail fragments, or shadowed timber shapes above the route. These are visual intimidation forms, not AI sightline or encounter markers.
- Chained plate and barricade accents: heavy scrap plates, blade-fence inserts, chain runs, log chokers, rough stone weights, and red-marked obstructions that frame the approach without creating destructible behavior.
- Gate relationship: the approach should funnel the viewer toward a hostile gate silhouette or gate placeholder relationship, while leaving the actual gate package and final stronghold approval separate.

Model the large cliff faces, palisade posts, path edges, major ledges, broad chains, large plates, banner cloth, big stakes, and primary barricade shapes as geometry if later approved. Push tiny cracks, scratches, wood grain, rope fibers, nail heads, stitch rows, soot speckles, ash flecks, cloth weave, small chips, and dense grime into textures, normals, AO, or trim sheets.

Avoid refined Giant stonework, clean masonry, carved civic symbols, warm hearth cues, blue rune culture, readable tactical labels, UI markers, dense skull curtains, graphic gore, or a one-color red/black wall of noise.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- This package does not change Giant race scale, skeleton policy, socket contracts, capsule expectations, or base proportions.

Planning-only approach scale targets:

- Cliff wall segment height: 1200-2600 cm for modular vertical faces; taller backdrops require separate terrain or HLOD planning.
- Cliff wall segment width: 900-2200 cm; use snap-friendly lengths where possible.
- Switchback main path visual width: 650-950 cm; narrow tension points can visually compress to 500-650 cm but must not be interpreted as nav/pathfinding values.
- Switchback shelf depth at turns: 1000-1800 cm so a 470 cm male Giant reads believably scaled near the route.
- Approach palisade height: 700-1100 cm to top spikes or warning cloth; gate-adjacent wall peaks may exceed this only if a later gate package approves the relationship.
- Palisade wall segment width: 700-1400 cm; depth 120-320 cm depending on log bundles, braces, and chained scrap.
- Warning markers: 300-850 cm tall, with the tallest banner or horn markers still secondary to gate and cliff silhouettes.
- Overlook silhouettes: 700-1300 cm above local ledge height, depending on pole, rail, or platform outline.
- Chained plate or barricade accents: 180-520 cm high, sized as Giant-built obstructions or visual edge controls.
- Gate relationship: maintain visual clearance and scale compatibility with existing Giant gate guidance, including clear passage planning around a 470 cm male Giant, but do not approve a final gate or stronghold layout here.

All dimensions are visual production planning values. They are not nav widths, encounter lanes, patrol paths, spawn spacing, climb rules, traversal proofs, or collision guarantees.

## Materials and Color Palette

Use Blood Axe material discipline:

- Rough highland stone, fractured dark cliff faces, mud, trampled earth, ash, soot, slag dust, and charcoal staining.
- Raw dark timber, split logs, charred stakes, heavy beams, rough braces, and buried post feet.
- Blackened iron, dark steel, crude reforged scrap plates, chained plates, clamp bands, heavy rings, and blade-fence accents.
- Scorched leather, rawhide lashings, sinew ties, rough rope, and hide wraps.
- Torn oxide-red cloth, dull red war paint, faded maroon banners, and dirty red warning strips as Blood Axe identifiers.
- Sparse aged bone, horn, tusk, broken shield plates, old weapon fragments, and carved warning tokens used cleanly and non-graphically.

Palette targets:

- Dominant: dark rock gray, charcoal black, mud brown, weathered timber brown, and soot-dark iron.
- Faction accent: oxide red, faded maroon, and chipped red paint in controlled beats.
- Secondary accent: bone ivory, rubbed steel edges, and ash gray in small amounts.
- Emissive: absent by default. Any torch, signal fire, forge heat, ritual glow, shamanic glow, or warning-light variant requires separate approval.

Avoid neutral/civilized Giant language: blue-gray civic masonry, refined carved stone, warm orderly hearth identity, terrace/waterwork forms, restrained blue runes, and peaceful highland clan markers. Avoid Ogre Teknomancy, dwarf smith elegance, normal humanoid fortification scale, readable text, UI-like route markers, or loot-rarity color coding.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeStrongholdApproach_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant stronghold approach, steep modular cliff wall segments, rough palisade wall runs, switchback path sections, vertical intimidation silhouettes, warning stakes, torn red cloth markers, sparse non-graphic bone and horn signs, crude overlook silhouettes, chained plate and blade-fence barricade accents, a distant gate relationship without final stronghold approval, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, blackened iron, dark steel, scorched leather, rough timber, soot, ash, packed earth, fractured rock, and strict separation from neutral/civilized Giant stoneworker culture. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a production approach kit board with top-down route composition, modular cliff/palisade/path/marker/barricade callouts, gate relationship thumbnails, scale bars, material swatches, LOD and collision planning notes, and docs-only stop gates on a clean background. Avoid copying any existing franchise, avoid graphic gore, avoid final stronghold approval claims, avoid encounter diagrams, avoid nav/pathfinding arrows, avoid patrol or spawn markers, avoid destructible behavior, avoid loot/crafting/economy/resource callouts, avoid source concept embedding, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, terrain sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material graph, Blueprint, validator, runtime source, startup placement, final visual approval, or implementation target is created or authorized.

Future DCC work, if separately approved, should split the approach into reusable child modules:

- Cliff wall segments: modular vertical rock faces, ledge caps, overhang blocks, cliff-base rubble shelves, and occluder-friendly back faces.
- Approach palisades: straight wall segment, angled wall segment, corner return, gate-flank return, broken top variant, and chained-scrap variant.
- Switchback paths: straight shelf, hairpin turn, ramp-like visual slope, stepped shelf, log-edged strip, stone-chocked edge, and packed-earth blend patch.
- Warning markers: red cloth stakes, horn markers, broken shield posts, blade fragments, cairn stacks, and non-graphic trophy tokens.
- Overlook silhouettes: non-walkable ledge outline, crude rail shape, post cluster, banner pole, watch-platform silhouette, and shadow-card marker if later approved for review only.
- Chained plate and barricade accents: heavy chained plate run, blade-fence insert, log barricade, scrap shield wall, rough stone anchor, and chain loop modules.
- Gate relationship markers: non-shipping framing blocks or thumbnail layouts that show how the approach visually leads to a gate without approving the gate or stronghold.
- Review composition markers: height rods, camera frame markers, cliff/palisade/gate silhouette markers, and scale ticks for planning review only.

Use snap-friendly pivots and repeatable dimensions for wall, cliff, and path segments. Do not collapse the whole approach into one scene mesh. Keep repeated posts, chains, plates, markers, and cloth strips instanced or variant-friendly. Large forms should carry the read; small surface damage belongs in textures, normals, AO, masks, or shared trim sheets.

## Texture and Material Notes

Use standard Aerathea map outputs if future assets are approved:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Optional Emissive (`E`) only for a separately approved torch, signal fire, forge heat, ritual, or shamanic variant

Suggested shared material families:

- `MI_GIA_BloodAxeCliffRock_A01`
- `MI_GIA_BloodAxePackedEarth_A01`
- `MI_GIA_BloodAxeRoughTimber_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeReforgedMetal_A01`
- `MI_GIA_BloodAxeScorchedHide_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeBoneTrophy_A01`
- `MI_GIA_BloodAxeSootAsh_A01`
- `MI_GIA_BloodAxeReviewMarker_A01` only for non-shipping visual review markers, if later approved

Texture naming examples:

- `T_GIA_BloodAxeApproachCliffWall_A01_BC`
- `T_GIA_BloodAxeApproachCliffWall_A01_N`
- `T_GIA_BloodAxeApproachCliffWall_A01_ORM`
- `T_GIA_BloodAxeApproachPalisade_A01_BC`
- `T_GIA_BloodAxeApproachPalisade_A01_N`
- `T_GIA_BloodAxeApproachPalisade_A01_ORM`
- `T_GIA_BloodAxeSwitchbackPath_A01_BC`
- `T_GIA_BloodAxeSwitchbackPath_A01_N`
- `T_GIA_BloodAxeSwitchbackPath_A01_ORM`
- `T_GIA_BloodAxeChainedPlateBarricade_A01_E` only if a separate emissive or heated state is approved; baseline chained plate has no emissive

Material slot targets:

- Cliff wall segments: 1-2 slots, preferably rock plus earth/ash blend.
- Palisade wall segments: 3 target, 4 maximum for timber, metal, cloth, and optional bone/hide accents.
- Switchback path sections: 1-2 slots for packed earth, rock, and edge dressing.
- Warning markers: 1-3 slots depending on cloth, timber, metal, or bone split.
- Overlook silhouettes: 2-4 slots if promoted beyond review markers.
- Chained plate/barricade accents: 2-3 slots for metal, timber, and cloth/hide.
- Review markers: 1 material, visually distinct from final art and never used as shipping set dressing without reapproval.

## Triangle Budget

This package creates no mesh. Future child modules, if approved, should use these LOD0 planning targets:

- Cliff wall segment: 8k-22k tris each, 1-2 material slots.
- Cliff ledge cap, rubble shelf, or overhang block: 3k-12k tris each, 1-2 material slots.
- Approach palisade wall segment: 8k-18k tris each, 2-4 material slots.
- Gate-flank palisade return or heavy corner segment: 12k-26k tris each, 3-4 material slots.
- Switchback straight path section: 2k-8k tris each, 1-2 material slots.
- Switchback hairpin or shelf-turn section: 5k-14k tris each, 1-3 material slots.
- Warning marker module: 800-5k tris each, 1-3 material slots.
- Overlook silhouette module: 5k-18k tris each when static dressing; 500-3k tris when a review marker only.
- Chained plate or blade-fence barricade accent: 3k-10k tris each, 2-3 material slots.
- Review composition marker kit: 2k-10k tris total, 1 material, non-shipping only.
- Composed approach preview: prefer instancing and keep unique static approach dressing under 140k tris before any future character or gate instances. Do not create one unique high-poly approach mesh.

Spend triangles on the readable cliff planes, palisade spike line, gate-framing mass, path ledges, major chains, large plates, and red cloth silhouettes. Do not spend geometry on tiny cracks, nail heads, rope fibers, cloth fray, ash flecks, pitted metal, many small stones, dense splinters, or per-link chain curtains unless the chain is a major silhouette element.

## LOD Plan

All approved future static meshes need LOD0-LOD3.

- LOD0: full approach read, including cliff wall shapes, ledge caps, palisade post mass, spike crowns, path shelf edges, large braces, red cloth markers, major chained plates, warning stakes, overlook silhouettes, and gate relationship markers where approved.
- LOD1: 60-70 percent of LOD0; reduce secondary rock cuts, small brace bevels, minor cloth tears, small chain subdivisions, edge chips, path rubble, and backside details.
- LOD2: 35-45 percent of LOD0; simplify cliff faces into larger planes, merge palisade post clusters, flatten small path edging, reduce chained plate undercuts, and remove non-silhouette marker detail.
- LOD3: 15-25 percent of LOD0; preserve the vertical cliff read, rough palisade outline, switchback route silhouette, red warning beats, large barricade shapes, and distant gate-framing composition.

LOD reduction order:

1. Tiny scratches, stitch rows, nail heads, rope fibers, soot speckles, ash flecks, pitting, small cracks, and cloth weave.
2. Small straps, minor knots, little chips, small stones, fine plank splits, and minor cloth holes.
3. Secondary trophy tokens, small chain segments, blade nicks, and backside marker detail.
4. Hidden cliff backs, underside ledges, non-visible braces, and camera-hidden path clutter.
5. Palisade post bevels, rock-plane subdivisions, cloth fold geometry, and metal plate undercuts.
6. Only after secondary detail is removed, simplify the main cliff mass, palisade height line, switchback shelf read, gate-framing silhouette, and large red cloth markers.

Never destroy the primary vertical approach silhouette, Giant-scale relationship, gate-facing composition, or Blood Axe red warning read before removing small detail.

## Collision Notes

Collision is planning only. Do not create collision proxies, custom UCX meshes, physics bodies, Unreal collision channels, nav links, nav blockers, smart links, traversal proofs, validation scripts, or runtime setup from this package.

Future static collision intent:

- Cliff wall segments: simple boxes or low-count convex hulls around large blocking faces only. No per-crack, per-stone, or per-rubble collision.
- Switchback path sections: simple surface collision only if a future implementation task promotes them to walkable environment pieces. This package does not approve nav/pathfinding, traversal, slope values, step heights, or route validation.
- Palisade walls: simple boxes or convex hulls around post clusters and heavy braces. No per-spike or per-lashing collision.
- Warning markers: collision disabled by default; simple pole bounds only if a large marker enters traversal space in a later implementation.
- Overlook silhouettes: collision disabled for review markers; simple static hulls only if later promoted to environment dressing. No climb, lookout, or AI sightline behavior.
- Chained plate/barricade accents: simplified hulls around major blocking plates or log masses only. No destructible collision, damage zones, cover rules, weak points, or per-chain collision.
- Cloth, small trophy markers, rope, lashings, ash piles, and small scrap: collision disabled by default.

No pathfinding, navmesh, patrol routes, spawn blockers, encounter lanes, cover volumes, climb volumes, camera blockers, projectile blockers, damage volumes, objective zones, interaction triggers, loot pickup collision, destructible setup, or gameplay collision is defined here.

## Animation Notes

Baseline future assets are static.

Allowed at planning level:

- Static cliff wall, palisade, path, marker, overlook, barricade, and review-marker modules.
- Optional static material variation for mud, soot, red paint wear, rock value, and timber age if a later material task approves it.

Approval-gated future options:

- Banner or cloth wind material.
- Hanging marker sway.
- Torch, signal fire, smoke, forge heat, ritual, or shamanic VFX.
- Gate motion, chain hoists, collapses, falling debris, breakable palisade states, destructible barricades, or damage-state variants.

None of those options are authorized by this package. Do not define animation timing, cloth simulation, physics setup, Blueprint behavior, interaction prompts, destructible behavior, VFX graphs, audio cues, encounter states, or gameplay state changes here.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, material instance, texture, socket, collision proxy, Blueprint, validator, runtime source, review-scene actor, startup actor, import script, source asset, or implementation file is created or authorized.

Potential future Unreal folders:

- Cliffs: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/StrongholdApproach/Cliffs/`
- Palisades: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/StrongholdApproach/Palisades/`
- Paths: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/StrongholdApproach/Paths/`
- Markers: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/StrongholdApproach/Markers/`
- Barricades: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/StrongholdApproach/Barricades/`
- Review-only markers: `/Game/Aerathea/Review/Giants/BloodAxe/StrongholdApproach/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/StrongholdApproach/`

Candidate future asset names, approval-gated only:

- `KIT_GIA_BloodAxeStrongholdApproach_A01`
- `SM_GIA_BloodAxeApproachCliffWall_A01`
- `SM_GIA_BloodAxeApproachCliffLedgeCap_A01`
- `SM_GIA_BloodAxeApproachPalisadeWall_A01`
- `SM_GIA_BloodAxeApproachGateFlank_A01`
- `SM_GIA_BloodAxeSwitchbackPath_A01`
- `SM_GIA_BloodAxeSwitchbackTurn_A01`
- `KIT_GIA_BloodAxeApproachWarningMarkers_A01`
- `SM_GIA_BloodAxeOverlookSilhouette_A01`
- `SM_GIA_BloodAxeChainedPlateBarricade_A01`
- `SM_GIA_BloodAxeBladeFenceAccent_A01`
- `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01`

Import assumptions for future work:

- Asset type: Static Mesh modules and docs-only review markers unless a later task explicitly promotes a different asset type.
- Pivot: ground center for cliff, overlook, and barricade clusters; snap edge for modular wall/path segments; pole base for warning markers; base center for height rods or review markers.
- Orientation: face +X for authored review markers unless a later DCC/export task confirms a different project convention.
- Scale: centimeter-authored source; Unreal import scale 1.0 after DCC/export approval.
- Collision: disabled for review markers; simple static hulls only for environment modules after implementation approval.
- LODs: LOD0-LOD3 required before production import approval.
- Material slot count: 1-2 for cliff/path modules, 2-4 for palisade/overlook/barricade modules, 1 for review markers.
- Sockets: none defined by this package.
- Animation list: none.
- Blueprint behavior: none.
- Performance note: use modular instancing, shared materials, trim sheets, HLOD planning, or impostor planning only after a future implementation task approves the approach composition.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeStrongholdApproach_A01/`
- Kit package: `docs/assets/kits/KIT_GIA_BloodAxeStrongholdApproach_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeStrongholdApproach_A01/CHILD_ASSET_INTAKE.md`
- Parent kit: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/`
- Related kits: `docs/assets/kits/KIT_GIA_BloodAxeFormationDressing_A01/`, `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/`, and `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/`

Recommended future child naming:

- `KIT_GIA_BloodAxeApproach<PlanningLane>_A01` for grouped docs-only split packages.
- `SM_GIA_BloodAxeApproach<AssetPurpose>_A01` for static mesh modules.
- `SM_GIA_BloodAxeSwitchback<PathPurpose>_A01` for route-shelf modules.
- `SM_GIA_BloodAxe<BarrierPurpose>_A01` for barricade and chained plate modules.
- `MI_GIA_BloodAxe<MaterialPurpose>_A01` for shared material instances.
- `T_GIA_BloodAxe<AssetName>_BC`, `T_GIA_BloodAxe<AssetName>_N`, and `T_GIA_BloodAxe<AssetName>_ORM` for future texture assets.
- `T_GIA_BloodAxe<AssetName>_E` only when a separate material/VFX approval allows emissive.

Do not create or edit `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, external concept folders, global indexes, task boards, backlog docs, bootstrap docs, unrelated production packages, or other asset docs from this task.

## Approval and Stop Gates

- Stop before final Blood Axe stronghold approval, final approach visual approval, hero screenshot approval, or first playable visual approval.
- Stop before selecting a first DCC, Unreal, source asset, or implementation target from this package.
- Stop before creating DCC source folders, Blender files, terrain sculpts, meshes, proof renders, UVs, bakes, collision proxies, LOD sources, FBX exports, Unreal Content assets, material instances, texture assets, import scripts, validators, runtime source, Blueprints, sockets, animation assets, review-scene actors, or startup placements.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before defining nav/pathfinding, traversal proofs, path widths as gameplay rules, climb logic, gate interaction, destructible behavior, damage volumes, cover rules, AI groups, patrol routes, perception, spawn logic, encounter design, combat stats, objective logic, loot, inventory, rewards, crafting, economy, resource behavior, pickup behavior, salvage behavior, VFX behavior, audio cues, or interaction behavior.
- Stop before claiming collision correctness, camera-capture approval, marker validation, HLOD implementation, terrain integration, gate compatibility, final silhouette approval, or runtime performance validation.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any planning row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, bootstrap, or unrelated package file.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Scope is stronghold approach planning only, not final stronghold approval.
- Package covers cliff wall segments, rough palisade walls, switchback path sections, hostile vertical silhouettes, approach markers, gate relationship, material discipline, LOD planning, collision planning, Unreal import notes, folder/naming recommendations, quality gates, and explicit stop gates.
- Child intake rows cover cliff wall segments, approach palisades, switchback path sections, warning markers, overlook silhouettes, chained plate/barricade accents, and review composition markers.
- Primary silhouettes are readable at MMO camera distance: vertical cliffs, rough palisades, switchback shelves, red warning beats, chained plate barriers, overlook shapes, and gate-facing compression.
- Materials use fractured rock, packed earth, rough timber, blackened iron, dark steel, scorched hide, oxide red cloth, soot, ash, and sparse non-graphic bone/horn markers consistently.
- Default emissive, ritual glow, forge heat, signal fire, shamanic glow, animated material states, gameplay VFX, UI-like markers, readable tactical text, and loot-rarity colors are absent and approval-gated.
- Tiny cracks, scratches, stitches, rivets, rope fibers, pitting, cloth weave, fray, soot speckles, ash flecks, paint chips, wood grain, and minor stone chips are assigned to textures or normals.
- Triangle budgets, texture maps, material slot targets, LOD0-LOD3 plan, collision planning, animation limits, Unreal import planning, folder naming, approval gates, and stop gates are included.
- No nav/pathfinding, encounter scripting, AI behavior, patrol logic, spawn logic, destructible behavior, gameplay/loot/economy/crafting/resource behavior, startup placement, source asset creation, implementation claim, final visual approval, final stronghold approval, or source concept movement is claimed.
