## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeApproachLODAndCollision_A01`
- Asset type: Documentation-only production policy package for LOD and collision planning
- Task: `AET-MA-20260629-165`
- Parent kit: `KIT_GIA_BloodAxeStrongholdApproach_A01`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Gate_StrongholdApproach`
- Source child ID: `BloodAxeStronghold.png#LODCollisionPlanning`
- Related planning references: `KIT_GIA_BloodAxeStrongholdApproach_A01`, `KIT_GIA_BloodAxeApproachCliffWalls_A01`, `KIT_GIA_BloodAxeSwitchbackPathSections_A01`, `KIT_GIA_BloodAxeApproachWarningMarkers_A01`, `KIT_GIA_BloodAxeApproachOverlookSilhouettes_A01`, `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01`, and current Blood Axe approach static prop packages
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready for planning review; no collision proxy, nav blocker, gameplay volume, validator, implementation file, DCC source, FBX, Unreal Content asset, startup placement, external source concept movement, final visual approval, final stronghold approval, or first implementation target is created or claimed

`DOC_GIA_BloodAxeApproachLODAndCollision_A01` defines planning policy for future LOD and collision treatment across Blood Axe stronghold approach static modules and non-shipping review markers. It covers LOD0-LOD3 reduction order, disabled collision defaults, simple collision boundaries for separately approved future static modules, review-marker collision exclusions, and no-implementation stop gates.

Blood Axe remains a hostile Giant sub-faction, not the default for Giant culture. Blood Axe approach assets may use rough cliffs, raw palisades, blackened iron, dark steel, chained scrap, scorched hide, soot, ash, oxide red cloth, rough timber, packed earth, and sparse non-graphic warning trophies. Neutral/civilized Giant culture remains separate: hidden mountain settlements, master stonework, blue-gray masonry, terraces, waterworks, warm hearth light, restrained blue runes, and civic stoneworker identity are not the default language for this package.

## Gameplay Purpose

The gameplay purpose is production planning only. This package prevents future Blood Axe approach modules from drifting into expensive or gameplay-implying collision and LOD work before a lead-approved implementation task exists.

Allowed planning uses:

- Establish consistent LOD0-LOD3 expectations for future cliff walls, ledge caps, palisade walls, gate-flank returns, switchback path sections, warning markers, overlook silhouettes, chained-plate accents, blade-fence accents, review composition markers, and scale rods.
- Clarify which future asset families should default to disabled collision, which may later use simple collision, and which must never become nav, gameplay, or validator objects through this docs package.
- Keep the validated Giant scale read intact through LOD reduction so the approach still reads as built for Giants at MMO camera distance.
- Keep review markers non-shipping and non-colliding.
- Provide stop gates before collision proxies, nav blockers, gameplay volumes, DCC, Unreal, runtime source, validators, startup placement, final visual approval, final stronghold approval, or first implementation target selection.

Out of scope:

- Creating collision proxies, custom UCX meshes, physics bodies, nav blockers, nav links, smart links, gameplay volumes, damage volumes, cover volumes, interaction triggers, validators, Unreal assets, Blueprint actors, runtime source, DCC files, FBX exports, source asset folders, material instances, texture assets, startup-scene placement, final visual approval, final stronghold approval, or first implementation target selection.
- Defining traversal proofs, pathfinding correctness, climb logic, walkable slopes, encounter lanes, AI spaces, patrol routes, spawn logic, projectile behavior, damage values, cover rules, destructible behavior, gate interaction, objective logic, loot, pickup, salvage, crafting, economy, resource behavior, VFX, audio, or interaction behavior.

## Silhouette Notes

LOD and collision decisions must protect the primary Blood Axe approach silhouette before preserving small detail. The future approach should read as a hostile Giant-scaled ascent with vertical cliff mass, rough palisade skyline, switchback shelf rhythm, warning-marker beats, overlook silhouettes, chained scrap accents, and gate-facing compression.

Primary silhouette priorities to preserve through LODs:

- Cliff mass: tall fractured walls, overhang-shadow blocks, ledge-back faces, choke-wall pressure, rubble-foot bases, and dark recess reads.
- Palisade mass: Giant-scale raw-log wall runs, uneven spike crowns, heavy crossbeam lines, rough brace depth, blackened iron bands, chained scrap blocks, and controlled oxide-red cloth rhythm.
- Switchback mass: broad shelf strips, packed-earth route read, stone-chocked edges, hairpin turns, ledge lips, and grounded path rhythm.
- Warning markers: oversized stakes, horn markers, broken shield tokens, blade fragments, cairn markers, cloth-line beats, and rough warning posts as sparse non-graphic reads.
- Overlook silhouettes: shadowed ledge outlines, crude rail shapes, banner poles, post clusters, and silhouette-only watch cutouts.
- Review markers: female and male Giant height rods, ground ticks, cliff/palisade proxy blocks, gate-frame thumbnails, and material discipline cards as visibly non-shipping planning aids.

LOD reduction and collision simplification must not erase Giant scale first. Remove tiny surface detail, small hanging pieces, backside detail, and non-silhouette fragments before reducing main wall heights, cliff masses, switchback outlines, or the validated Giant scale references.

Avoid silhouette changes that create neutral/civilized Giant civic masonry, refined terrace reads, warm hearth settlement identity, restrained blue-rune culture, UI route arrows, gameplay symbols, cover-slot shapes, damage-volume silhouettes, trap teeth, nav lanes, or final gate approval.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author any future source in centimeters. 1 Unreal unit = 1 cm.
- This package does not change Giant race scale, skeleton policy, socket policy, capsule expectations, body proportions, camera rules, or base proportions.

LOD and collision planning scale guidance:

- Future LOD review should compare LOD0, LOD1, LOD2, and LOD3 against 442 cm female and 470 cm male Giant baselines before any production import signoff.
- LOD3 must still communicate whether a module belongs to a Giant approach rather than a human-scale camp.
- Collision planning for future static modules must stay broad and simple relative to Giant scale. Do not use per-detail collision for posts, spikes, chains, cloth, small rubble, small warning tokens, or surface ornament.
- Review scale rods, range ghost rods, ground ticks, thumbnail frames, and proxy silhouette blocks are visual planning aids only. They do not define path widths, nav widths, patrol spacing, spawn spacing, combat lanes, collision bounds, or traversal values.
- Optional future range references may use 427 cm and 457 cm for female bounds and 452 cm and 488 cm for male bounds in docs or review boards only. These do not change the validated baselines.

All dimensions in this package are production planning values, not gameplay metrics, navmesh values, movement tests, slope rules, collision guarantees, or final stronghold measurements.

## Materials and Color Palette

LOD and collision policy should reinforce the established Blood Axe material discipline without adding new material work.

Approved Blood Axe material families for future modules:

- Fractured highland rock, dark slate, packed earth, mud, ash, soot, slag dust, charcoal staining, and rubble bases.
- Raw dark timber, split logs, charred stakes, rough braces, heavy crossbeams, and buried post feet.
- Blackened iron, dark steel, crude reforged scrap, chain plates, clamp bands, ring plates, blade fragments, and broken shield tokens.
- Scorched leather, rawhide lashings, sinew ties, rough rope, hide wraps, and weathered bindings.
- Torn oxide red cloth, faded maroon warning strips, chipped red paint, dirty red wraps, and restrained Blood Axe marks.
- Sparse aged bone, horn, tusk, old weapon fragments, and non-graphic warning tokens only where they support the hostile read.

LOD material guidance:

- Preserve broad value separation between rock, timber, dark metal, earth, and red cloth through all LODs.
- Let textures, normals, AO, and masks carry wood grain, small cracks, soot speckles, ash flecks, metal pitting, cloth weave, rope fibers, small paint chips, and tiny scratches.
- Do not add material slots to solve LOD issues. Shared material families and broad masks should carry variation.
- No default emissive is approved. Any torch, ritual glow, forge heat, shamanic effect, alarm state, or magical marker requires a separate approval-gated package.

Banned default reads:

- Neutral/civilized Giant blue-gray civic masonry, refined carved stone, terrace/waterwork forms, warm hearth identity, restrained blue runes, peaceful highland clan markers, or master-stoneworker motifs.
- Ogre Teknomancy, dwarf smith elegance, normal humanoid fortification scale, readable tactical text, UI-like route markers, loot-rarity colors, weak-point colors, or dense graphic trophy clutter.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production planning board of `DOC_GIA_BloodAxeApproachLODAndCollision_A01` for the world of Aerathea. The design should emphasize docs-only LOD and collision planning for a hostile Blood Axe Giant stronghold approach, validated Giant scale with female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved Giant ranges of females 14-15 ft and males 14'10"-16'0", LOD0-LOD3 reduction rows for cliff walls, palisade walls, switchback path sections, warning markers, overlook silhouettes, chained-plate accents, blade-fence accents, review composition markers, non-shipping height rods, disabled collision defaults, future simple collision notes, review-marker collision exclusions, no-implementation stop gates, rough Blood Axe approach silhouettes, fractured rock, raw timber, blackened iron, chained scrap, scorched hide, soot, ash, oxide red cloth, and strict separation from neutral/civilized Giant stoneworker culture. Use hand-painted texture detail only in material swatches, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a clean documentation board with LOD rows, collision-policy callouts, scale references, material swatches, and red stop-gate notes on a neutral background. Avoid copying any existing franchise, avoid source concept embedding, avoid creating collision proxies, avoid navmesh diagrams, avoid gameplay volume diagrams, avoid validator diagrams, avoid Unreal implementation screenshots, avoid DCC source claims, avoid final visual approval, avoid final stronghold approval, avoid first implementation target selection, avoid readable tactical UI, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

Concept source note: this package references `BloodAxeStronghold.png#LODCollisionPlanning` only through existing intake documentation. It does not inspect, move, copy, crop, edit, embed, rename, commit, approve, or present external source concept art.

## Modeling Notes

This is a docs-only modeling policy. No DCC source, source folder, Blender file, terrain sculpt, mesh, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material graph, Blueprint, validator, runtime source, startup actor, first implementation target, final visual approval, or final stronghold approval is created or authorized.

Future modeling teams, if separately approved, should use this LOD/collision policy when building child modules:

- Build the large readable silhouette first: cliff planes, wall post rows, switchback shelf outlines, warning-marker profiles, overlook rail silhouettes, chained plate masses, and broad route-framing shapes.
- Model real geometry only for primary forms, major supports, large metal scraps, broad chains where they affect silhouette, major cloth strips, large stones, heavy braces, and main marker rods.
- Use texture, normal maps, AO, trim sheets, or masks for tiny rivets, small scratches, wood grain, stone cracks, cloth weave, rope fibers, small runes, soot speckles, ash flecks, paint chips, metal pitting, and micro debris.
- Keep future LOD source organized by removable detail tiers so LOD1, LOD2, and LOD3 can remove detail in the required order.
- Keep review markers visually simple and separate from final art. Height rods, scale rods, proxy blocks, ground ticks, and planning cards should never look like shipping Blood Axe props.
- Do not model collision affordances into the art such as nav arrows, cover slots, trap teeth, damage plates, destructible seams, interactable handles, objective markers, pickup highlights, loot symbols, or pathfinding indicators.

Recommended future LOD source group order:

1. Primary silhouette and scale-critical forms.
2. Secondary construction forms and large faction accents.
3. Large material-break forms and readable grounding details.
4. Small hanging pieces, optional accents, and backside-only detail.
5. Texture-only and normal-only surface detail.

Only a later task may convert these notes into meshes, LOD sources, proxy geometry, Unreal assets, or validators.

## Texture and Material Notes

This package creates no textures, material instances, material functions, shader graphs, or Unreal assets.

Future approved modules should use standard Aerathea outputs:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Emissive (`E`) only for a separately approved torch, ritual, forge, shamanic, alarm, or magic variant

LOD texture guidance:

- Maintain material readability at distance by preserving large value groups and faction-color rhythm rather than relying on tiny detail.
- Keep Blood Axe red cloth or paint sparse and broad enough to survive LOD reduction without turning into noisy red speckling.
- Bake strong AO under major overlaps, post bases, rock shelves, chained plates, brace intersections, and large cloth folds.
- Use roughness variation to separate raw timber, blackened metal, mud, soot, hide, cloth, and rock without adding material slots.
- Metallic should remain limited to iron, steel, chain, clamp, ring, plate, broken shield, blade fragment, and reforged hardware zones.
- Review markers should use matte neutral review materials if ever approved, with no emissive by default.

Do not author unique textures or materials for each LOD level unless a separate optimization task approves it. Do not create material graphs, textures, masks, emissive maps, VFX materials, review-marker materials, or runtime material states from this docs-only package.

## Triangle Budget

This package creates no mesh. Future Blood Axe approach modules, if separately approved, should use LOD0 budgets already appropriate to their asset class and then apply the reduction bands below.

Recommended LOD0 planning targets for common approach families:

- Cliff wall modules: 5k-24k tris each depending on wall type, with composed unique cliff-wall dressing kept under 90k tris before gates, palisades, paths, markers, characters, or stronghold assets are added.
- Ledge cap and rubble modules: 2k-9k tris each.
- Palisade wall and gate-flank modules: 8k-18k tris each for standard or heavy gate-facing pieces; 4k-8k tris for short filler segments.
- Switchback path straight or turn modules: 4k-14k tris each depending on shelf width, edge treatment, and large stone forms.
- Warning marker kit modules: 50-2k tris per marker, with mixed clusters kept light enough for repeated route dressing.
- Overlook silhouette kit modules: 300-6k tris per silhouette module, preserving only the ledge, rail, post, banner, or cutout read.
- Chained-plate and blade-fence accent modules: 1k-8k tris depending on scrap mass and silhouette value.
- Review composition markers and scale rods: 20-1.5k tris per marker, collision disabled, non-shipping, and extremely light.

LOD reduction bands for future static modules:

- LOD0: full approved silhouette and material-break geometry.
- LOD1: 60-70 percent of LOD0.
- LOD2: 35-45 percent of LOD0.
- LOD3: 15-25 percent of LOD0.

Budget priorities:

- Spend triangles on primary cliff mass, Giant-scale palisade height, switchback shelf outline, large braces, major scrap silhouettes, broad chains, large red cloth shapes, major warning-marker profiles, and review height rods.
- Do not spend triangles on tiny cracks, fine bark cuts, soot speckles, ash flecks, individual rope fibers, cloth weave, tiny rivets, small nail heads, non-silhouette chain links, dense small trophies, readable text, or tiny surface chips.

## LOD Plan

All important future Blood Axe approach static modules require LOD0, LOD1, LOD2, and LOD3 before production import signoff. This package does not create LOD meshes, source files, validation files, or Unreal imports.

Baseline LOD expectations:

- LOD0: full approved module silhouette with primary forms, large construction forms, material-break geometry, large Blood Axe faction accents, scale-critical mass, and readable grounding forms.
- LOD1: 60-70 percent of LOD0. Reduce small bevels, tiny chips, minor cloth cuts, secondary lashing turns, non-silhouette chain subdivisions, small ground clutter, thin backside details, and optional accent undercuts.
- LOD2: 35-45 percent of LOD0. Merge smaller rock planes, simplify individual post cuts, flatten small bands and rope wraps, reduce brace subdivisions, simplify cloth shapes, remove most optional accent detail, and keep only major silhouette breaks.
- LOD3: 15-25 percent of LOD0. Preserve the main Giant-scale read: vertical cliff mass, palisade height line, switchback footprint, gate-facing compression, warning-marker rhythm, overlook outline, chained scrap block read, broad red Blood Axe accent, and validated height-rod references where review markers are used.

Required LOD reduction order:

1. Tiny bolts, rivets, nail heads, stitches, rope fibers, cloth weave, soot speckles, ash flecks, tiny scratches, small paint chips, fine wood grain cuts, tiny stone cracks, and metal pitting.
2. Small straps, small lashings, loose hanging pieces, small cloth holes, tiny frayed edges, little splinters, small mud clumps, minor pebbles, and non-silhouette chain links.
3. Small spikes, secondary warning points, minor horn/bone undercuts, small blade teeth, duplicate stake tips, and optional marker fragments.
4. Secondary decorative cuts, extra rock-plane subdivisions, small plate undercuts, small shield chips, secondary red marks, and nonessential frame borders.
5. Interior, underside, backside, and hidden detail not visible from intended approach compositions.
6. Small pipes, ornaments, redundant scrap plates, optional duplicate chains, and decorative edge cuts.
7. Minor animation-ready parts, material-state holders, optional cloth-sway pieces, or future variant hooks if a later task ever approves them.

Never reduce the primary Giant-scale silhouette first. Main cliff height, palisade skyline, switchback path outline, gate-facing composition, main warning-marker rhythm, overlook silhouette, large chained scrap mass, and Blood Axe red/black material identity must survive until all secondary detail has already been removed.

## Collision Notes

This package defines policy only. It does not create collision proxies, UCX meshes, physics bodies, Unreal collision channels, nav blockers, nav links, smart links, gameplay volumes, damage volumes, cover volumes, interaction triggers, validators, startup placement, or collision correctness claims.

Default future collision policy:

- Review composition markers, scale rods, height rods, ground ticks, camera-composition frames, thumbnail cards, material discipline cards, LOD/collision planning cards, and proxy silhouette blocks: collision disabled.
- Warning markers, cloth-line markers, small cairns, loose blade accents, horn tokens, bone tokens, small scrap tokens, red cloth strips, lashings, rope, hanging chains, and non-structural dressing: collision disabled by default.
- Cliff wall modules, palisade wall modules, gate-flank returns, large switchback edge modules, large barricade accents, and major chained-plate masses: simple collision may be considered only by a later approved implementation task when the asset is intended to block movement visually and physically.
- Switchback path visual modules: collision policy remains unset by this docs package. A later terrain, traversal, or Unreal task must define any walkable surface, slope, step, nav, or movement behavior.
- Dark recess inserts and overlook silhouettes: collision disabled by default unless a later implementation task promotes them to broad static blockers.

Future simple collision guidance, if separately approved:

- Use one to three broad boxes or low-count convex hulls for large wall or palisade masses.
- Use broad hulls around major cliff blocking planes only; no per-crack, per-rubble, per-overhang, per-ledger, or underside micro-collision.
- Use disabled collision or one broad hull for large rubble-foot strips depending on later placement needs.
- Use a small number of hulls for large chained-plate or barricade masses only if they are intended to physically block players in a later task.
- Do not use per-post collision, per-spike collision, per-chain collision, per-plate collision, per-stake collision, complex-as-simple collision, physics-simulated loose scrap, or projectile-blocking gameplay claims by default.

Review-marker collision exclusions:

- Review markers are non-shipping planning aids and must not affect navigation, pathfinding, movement, spawn spacing, patrol spacing, encounter layout, camera blockers, projectile blockers, damage zones, cover logic, objective zones, interaction prompts, loot pickup, or validation results.
- Marker bounds may exist only as editor selection bounds if a future non-shipping marker task explicitly approves marker assets. They are not gameplay collision.
- A/B/C/D/E marker passes, scale rods, and orientation markers must be collision disabled and excluded from shipping content unless a future lead-approved task changes scope.

Stop before claiming collision correctness, navmesh compatibility, terrain integration, walkable route approval, gate compatibility, camera capture approval, marker validation, runtime performance validation, or final silhouette approval.

## Animation Notes

Baseline policy is static. LOD and collision planning does not authorize animation, material-state animation, physics, VFX, audio, Blueprint behavior, runtime behavior, or startup-scene behavior.

Allowed at planning level:

- Static notes for LOD0-LOD3 reduction order.
- Static notes for disabled collision and future simple collision boundaries.
- Static review-marker exclusions and no-implementation stop gates.
- Static discussion of future modules that may remain non-animated by default.

Not authorized:

- Animated markers, cloth simulation, chain sway, falling logs, collapsing rocks, destructible breaks, trap movement, gate movement, camera animation, capture automation, material pulses, emissive highlights, VFX arrows, smoke, fire, signal lights, audio cues, Blueprint timelines, gameplay notifies, physics fragments, interaction prompts, damage reactions, repair states, loot behavior, resource behavior, crafting behavior, economy behavior, combat behavior, nav behavior, encounter behavior, objective logic, or startup-scene behavior.

Any moving, glowing, destructible, interactive, or gameplay-readable version must be split into a separately named and approval-gated package.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, source asset, source folder, material instance, texture, socket, collision proxy, Blueprint, validator, runtime source, review actor, startup actor, import script, FBX, DCC file, or implementation file is created or authorized.

Documentation package identity:

- Asset name: `DOC_GIA_BloodAxeApproachLODAndCollision_A01`
- Asset type: Documentation / production policy, not a shipping Unreal asset
- Docs folder: `docs/assets/kits/DOC_GIA_BloodAxeApproachLODAndCollision_A01/`
- Production package: `docs/assets/kits/DOC_GIA_BloodAxeApproachLODAndCollision_A01/PRODUCTION_PACKAGE.md`
- Parent kit: `docs/assets/kits/KIT_GIA_BloodAxeStrongholdApproach_A01/`
- Scale: centimeters for all future authored sources; Unreal import scale 1.0 after a separate DCC/export approval
- Pivot: defined per future asset package only; this docs package defines no mesh pivot
- Collision type: disabled by default for review markers; broad simple collision only for separately approved future blocking static modules; no collision proxy is created here
- LODs: LOD0-LOD3 required for important future static modules before import signoff
- Material slot count: preserve each future package's slot target; do not add slots for LOD work
- Sockets: none from this package
- Animation list: none
- Blueprint behavior: none
- Performance note: preserve primary Blood Axe Giant-scale silhouette while removing small detail first; keep review markers non-shipping and collision disabled

Potential future Unreal folders, approval-gated only:

- Environment approach modules: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/StrongholdApproach/`
- Review-only markers: `/Game/Aerathea/Review/Giants/BloodAxe/StrongholdApproach/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/StrongholdApproach/`

No folder above is created or approved for implementation by this docs-only package. A future implementation task must define exact import paths, pivots, LOD files, collision setup, material assignments, Nanite/HLOD policy, startup placement, and validation scope.

## Folder and Naming Recommendation

Documentation file created by this task:

- `docs/assets/kits/DOC_GIA_BloodAxeApproachLODAndCollision_A01/PRODUCTION_PACKAGE.md`

Naming discipline:

- Use `DOC_GIA_BloodAxeApproachLODAndCollision_A01` for this planning-policy package.
- Use `GIA` for Giant race assets and `BloodAxe` for the hostile Giant sub-faction so the work stays separate from neutral/civilized Giant culture.
- Use `DOC_GIA_BloodAxeApproach<PlanningPurpose>_A01` for docs-only planning rows.
- Use `KIT_GIA_BloodAxeApproach<KitPurpose>_A01` for future grouped Blood Axe approach kits.
- Use `SM_GIA_BloodAxeApproach<AssetPurpose>_A01` for future static mesh modules only after a separate implementation task approves mesh work.
- Use `MI_GIA_BloodAxe<MaterialPurpose>_A01` and `T_GIA_BloodAxe<AssetPurpose>_A01_BC`, `T_GIA_BloodAxe<AssetPurpose>_A01_N`, and `T_GIA_BloodAxe<AssetPurpose>_A01_ORM` only after a separate material or implementation task approves asset creation.

Do not add or edit `Content/Aerathea/`, `SourceAssets/`, `Tools/DCC/`, `Tools/Unreal/`, runtime source, external source concept folders, task board, global indexes, backlog, bootstrap, unrelated production packages, source concept manifests, approval queues, validators, startup-scene files, collision proxy files, gameplay system files, or first implementation target documents from this task.

## Quality Gate Checklist

- [x] Package uses the universal 15 headings exactly and unnumbered.
- [x] Package remains docs-only production planning and creates no DCC, FBX, Unreal Content, runtime source, validator, startup placement, collision proxy, nav blocker, gameplay volume, external source concept movement, final visual approval, final stronghold approval, or first implementation target.
- [x] Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- [x] Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- [x] Neutral/civilized Giant cues remain excluded as defaults: blue-gray civic masonry, refined stonework, terraces, waterworks, warm hearth identity, restrained blue runes, and civic stoneworker motifs.
- [x] LOD0, LOD1, LOD2, and LOD3 expectations are included.
- [x] LOD reduction order removes tiny detail, small hanging pieces, small spikes, secondary cuts, hidden/backside detail, small ornaments, and minor animation-ready parts before reducing primary silhouette.
- [x] Triangle budget guidance covers common future Blood Axe approach module families and review markers without creating meshes.
- [x] Texture and material notes include BC, N, ORM, and approval-gated E only, with no material or texture creation.
- [x] Collision notes define disabled defaults, future simple collision policy, review-marker collision exclusions, and no collision-correctness claim.
- [x] Review markers are non-shipping and collision disabled by default, including scale rods, height rods, ground ticks, thumbnail cards, composition frames, material cards, LOD/collision cards, and A/B/C/D/E marker passes.
- [x] Nav blockers, nav links, smart links, gameplay volumes, damage volumes, cover volumes, interaction triggers, projectile-blocking claims, complex-as-simple collision, per-detail collision, and validator checks are explicitly out of scope.
- [x] Unreal import notes are future planning only and include asset name, asset type, folder path, naming convention, pivot policy, scale, collision type, LOD plan, material slot policy, texture list, sockets, animation list, Blueprint behavior, and performance notes.
- [x] Source concepts remain external and are not copied, moved, cropped, edited, embedded, renamed, inspected for final approval, committed, approved, or presented by this package.
- [x] No first DCC, Unreal, source asset, gameplay, final visual, final stronghold, or implementation target is selected.
