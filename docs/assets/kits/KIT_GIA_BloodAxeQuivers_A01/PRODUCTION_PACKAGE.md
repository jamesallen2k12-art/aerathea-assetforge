# KIT_GIA_BloodAxeQuivers_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeQuivers_A01`
- Asset type: Production kit / Giant quiver, arrow, strap, and display accessory set
- Parent source: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#QuiverArrow_Set`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only kit production package ready
- Scope guardrail: this package creates no DCC source, FBX export, Unreal Content asset, runtime source, startup-scene placement, projectile behavior, or copied concept art.

`KIT_GIA_BloodAxeQuivers_A01` defines the Giant-scale quiver and arrow mini-kit for Blood Axe raiders, hunters, camp guards, and armory dressing. The visual language is brutal, improvised, and hostile: oversized hide quivers, blackened iron rims, rough wood arrow shafts, barbed arrow heads, scorched leather straps, red cloth warnings, bone tags, and trophy lashings. Blood Axe must remain a hostile Giant sub-faction and must not replace neutral/civilized Giant culture.

## Gameplay Purpose

The kit supports visual equipment and set dressing for Blood Axe Giant archers and bowyer areas:

- Belt quivers for hip or side carry on Giant raider variants.
- Back quivers for large archer silhouettes and long-distance readability.
- Rack quivers for camp, forge, bowyer, and armory dressing.
- Loose arrows, bundled arrows, and display arrow heads for tables, racks, loot piles, and environmental storytelling.
- Strap variants and trophy tags for controlled reuse across quivers without creating a different mesh for every dressing detail.

This package does not define combat rules, ammunition counts, projectile behavior, bow animation timing, pickup logic, loot behavior, or inventory implementation. Arrows are specified here as equipped/display geometry and scale references only.

## Silhouette Notes

Primary read should be Giant-scale utility with Blood Axe menace. Each quiver must look large enough for a Giant hand and shoulder width, with chunky rims, thick side seams, wide straps, and visible arrow silhouettes at MMO camera distance.

- Belt quiver: shorter, angled, heavy hide tube or split leather shell with a thick upper rim, broad belt loops, side straps, and a few visible arrow ends.
- Back quiver: tall vertical or slightly tapered silhouette with a broad top mouth, reinforced bottom cup, oversized cross straps, and clear back-carry read.
- Rack quiver: stationary camp object with a heavier base, wood or iron frame, open arrow cluster, and Blood Axe red cloth tied near the top or side.
- Loose arrows: long thick shafts with readable fletching blocks and large broadhead, barbed, bodkin, or blunt head variants.
- Arrow bundle: tied cluster that reads as a single prop at distance, not a dense forest of separate shafts.
- Display arrow heads: oversized heads arranged on hide, wood, or iron display backing for bowyer/armory dressing.
- Strap variants: broad scorched leather, hide, cord, and chain-assisted straps that attach cleanly to belt/back versions.
- Trophy tags: bone, tooth, broken token, and red cloth tag details used sparingly to avoid visual clutter.

Model the top rim, shell mass, major straps, large arrow heads, big fletching blocks, rack frame, and major trophy tags as geometry. Use textures and normals for stitching, small cuts, nicks, soot, pitting, small rivets, leather grain, and minor binding detail.

## Scale Notes

Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

- Author in centimeters. 1 Unreal unit = 1 cm.
- Fit all carry variants to `SK_GIA_Base_A01` proportions before any future build promotion.
- Normal humanoid compatibility is not required for this kit.
- Belt and back variants must clear Giant pelvis, thighs, spine, shoulders, elbows, and hand reach.
- Rack variants must read as Giant-made armory props beside a 470 cm male Giant and should not collapse into small-folk prop scale.

Suggested production scale targets:

- Belt quiver: 95-130 cm tall, 24-38 cm wide, 20-34 cm deep; angled for hip carry without clipping the thigh.
- Back quiver: 145-185 cm tall, 32-48 cm wide, 28-42 cm deep; top rim must sit clear of shoulder silhouette and back weapon space.
- Rack quiver: 175-230 cm tall, 60-110 cm wide including frame or stand, with ground contact and a stable base.
- Loose arrows: 180-260 cm long depending on longbow/shortbow pairing; shaft diameter should feel Giant-scale without becoming log-like.
- Arrow heads: 28-65 cm long; broadhead and barbed variants should be readable at distance.
- Arrow bundle: 4-10 visible shafts per bundle; more arrows should be implied through texture and grouped silhouettes.
- Strap variants: 8-18 cm wide leather/hide straps; large buckles and rings should be readable but not excessive.
- Trophy tags: 18-45 cm long; use as accents, not a repeated covering layer.

Attachment planning references are documentation-only. Candidate future sockets include `back_quiver`, `belt_quiver_l`, `belt_quiver_r`, `belt_tool_l`, `belt_tool_r`, and `back_large_weapon`, with final socket ownership inherited from `SK_GIA_Base_A01` or a future Blood Axe archer package.

## Materials And Color Palette

Primary material language:

- Scorched dark leather, rough hide, sinew, cord wraps, and worn fur edges.
- Blackened iron and dark steel rims, rings, buckles, arrow heads, and rack hardware.
- Rough wood or split stave shafts in dark brown, gray-brown, and soot-stained ochre.
- Bone, horn, tooth, and broken trophy tags used sparingly.
- Torn red cloth, dull red paint, and dirty red binding as Blood Axe identifiers.
- Soot, ash, dried mud, grime, oil stains, and broad hand-painted wear.

Avoid neutral/civilized Giant stoneworker language here. Blue-gray carved stone, warm hearth presentation, and restrained blue runes belong to neutral Giant packages unless a future stolen-object variant is separately approved.

Emissive is not part of the baseline. No glow maps are expected for this kit.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeQuivers_A01` for the world of Aerathea. The design should emphasize Giant-scale belt quivers, back quivers, rack quivers, loose arrows, arrow bundles, display arrow heads, strap variants, trophy tags, scorched leather, blackened iron, dark steel, rough wood shafts, bone tags, red cloth warnings, hostile Blood Axe raider culture, and bowyer/armory gameplay dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a clean production asset board with front/side/back callouts, belt/back/rack attachment variants, arrow head closeups, scale callouts against a female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5" Giant, and notes separating Blood Axe hostile sub-faction identity from neutral/civilized Giant culture. Avoid copying any existing franchise, avoid graphic gore, avoid projectile gameplay diagrams, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only package. Future modeling work should build the mini-kit as reusable child meshes rather than one collapsed object.

- Belt quiver: model the shell, top rim, bottom cap, main belt loop, wide securing strap, large buckle/ring, and a small visible arrow cluster. Keep the open mouth readable.
- Back quiver: model a taller shell, reinforced rim, bottom cup, cross-back strap attachments, and optional side trophy tie points. Keep the profile thin enough to clear back weapon sockets.
- Rack quiver: model a stationary frame or floor tube with a stable base, heavy supports, and a moderate arrow cluster. Avoid overfilling it with individually unique arrows.
- Loose arrows: create a small reusable set of shaft/head/fletching silhouettes. Use shared proportions so arrows can populate belts, backs, racks, and bundles.
- Arrow bundle: model a grouped silhouette with several true shafts and texture-implied interior shafts. Use cord ties and one or two large red cloth strips.
- Display arrow heads: model a limited set of large heads on a hide/wood/iron presentation backing for bowyer tables or wall dressing.
- Strap variants: build reusable broad straps, buckle/ring pieces, and optional hide cord ties that can be placed on multiple quivers.
- Trophy tags: model only the largest bone/tooth/token shapes; paint the smaller scratches, cracks, tally marks, and binding fibers.

Use real geometry for quiver volumes, rims, rack frames, major straps, buckles, rings, large arrow heads, fletching blocks, and main trophy tags. Use texture and normal detail for leather pores, stitching, small nicks, soot streaks, pitting, scratches, minor rivets, and tiny binding fibers.

## Texture And Material Notes

Required map set for future texture work:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No emissive map is planned for the baseline kit.

Shared material targets:

- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeArrowWood_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeBoneTrophy_A01`

Texture naming examples:

- `T_GIA_BloodAxeBeltQuiver_A01_BC`
- `T_GIA_BloodAxeBeltQuiver_A01_N`
- `T_GIA_BloodAxeBeltQuiver_A01_ORM`
- `T_GIA_BloodAxeBackQuiver_A01_BC`
- `T_GIA_BloodAxeBackQuiver_A01_N`
- `T_GIA_BloodAxeBackQuiver_A01_ORM`
- `T_GIA_BloodAxeArrowSet_A01_BC`
- `T_GIA_BloodAxeArrowSet_A01_N`
- `T_GIA_BloodAxeArrowSet_A01_ORM`

Material slot targets:

- Belt/back quivers: 1-2 slots, combining leather/hide with metal/bone/cloth when possible.
- Rack quiver: 1-2 slots for wood/leather and metal/trophy accents.
- Loose arrows and arrow bundles: 1 material slot where practical.
- Display arrow heads: 1-2 slots depending on backing material.
- Strap and trophy variant kits: share existing materials; do not create unique slots per tag or buckle.

## Triangle Budget

Target LOD0 ranges:

- `SM_GIA_BloodAxeBeltQuiver_A01`: 2k-5k tris.
- `SM_GIA_BloodAxeBackQuiver_A01`: 3k-6.5k tris.
- `SM_GIA_BloodAxeRackQuiver_A01`: 4k-9k tris depending on rack frame and visible arrow count.
- `SM_GIA_BloodAxeArrow_A01`: 250-650 tris per loose/display arrow.
- `SM_GIA_BloodAxeArrowBundle_A01`: 900-2.5k tris.
- `KIT_GIA_BloodAxeArrowHeads_A01`: 1.5k-4k tris for the display board or grouped set.
- `KIT_GIA_BloodAxeQuiverStraps_A01`: 300-1.2k tris per strap variant.
- `KIT_GIA_BloodAxeTrophyTags_A01`: 300-1.5k tris per tag cluster.
- Composed quiver/rack preview grouping: target under 28k tris by reusing arrow, strap, and tag meshes.

These are planning budgets only. Any future build should preserve primary silhouette before adding more trophies or arrow count.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full shell/rim/rack/strap/arrow-head silhouettes, visible arrow clusters, large buckles, big tags, and broad hand-painted material breaks.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small strap cuts, secondary tags, repeated fletching subdivisions, and inner arrow cluster density.
- LOD2: 35-45 percent of LOD0; simplify quiver interiors, rack cross braces, buckle bevels, trophy tag shapes, and arrow head profile cuts.
- LOD3: 15-25 percent of LOD0; preserve belt/back/rack identity, top rim, main arrow direction, red cloth accent, and overall Giant-scale mass.

Remove tiny stitches, rivets, scratches, pitting, small bindings, and duplicate tag shapes before reducing the quiver body, top mouth, back-carry outline, rack footprint, or arrow head silhouettes.

## Collision Notes

Collision remains simple and display-focused.

- Equipped belt/back quivers: collision disabled by default when attached to a character; character physics and animation clearance handle body interaction.
- World-display belt/back quivers: one simplified capsule or box around the main shell.
- Rack quiver: grouped boxes or low-count convex hulls for the base/frame; no per-arrow collision.
- Loose arrows: one simple capsule or box only for static display placement if needed.
- Arrow bundles: one capsule or box around the bundle mass.
- Display arrow heads: one simple box around the board or head cluster.
- Strap variants and trophy tags: no standalone collision unless promoted to a large world prop in a future package.

No projectile collision, projectile behavior, damage tracing, or runtime ammunition logic is defined by this docs-only package.

## Animation Notes

Static mesh baseline. No animations, bow draw timing, reload timing, projectile launch behavior, cloth simulation, or runtime equip behavior are authored here.

Future animation review, if assigned separately, should only validate attachment clearance:

- Belt quivers clear Giant pelvis, thighs, belt armor, and hand reach during locomotion.
- Back quivers clear shoulders, spine, back weapons, and arm swing arcs.
- Straps do not obscure the main Giant torso read or cut through major Blood Axe armor modules.
- Rack and display props remain static camp dressing.

## Unreal Import Notes

These are planned import notes only. This task does not create Unreal assets.

Planned asset types:

- Static Meshes: belt quiver, back quiver, rack quiver, loose arrows, arrow bundle, display arrow head board, strap variants, trophy tag variants.
- Material Instances: shared Blood Axe leather, iron, wood, red cloth, and bone materials.

Planned folders:

- `/Game/Aerathea/Props/Giants/BloodAxeArmory/Quivers/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/Arrows/`
- `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/Quivers/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned naming:

- `SM_GIA_BloodAxeBeltQuiver_A01`
- `SM_GIA_BloodAxeBackQuiver_A01`
- `SM_GIA_BloodAxeRackQuiver_A01`
- `SM_GIA_BloodAxeArrow_A01`
- `SM_GIA_BloodAxeArrowBundle_A01`
- `SM_GIA_BloodAxeArrowHeadsDisplay_A01`
- `SM_GIA_BloodAxeQuiverStrap_A01`
- `SM_GIA_BloodAxeTrophyTag_A01`
- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeArrowWood_A01`

Pivot planning:

- Belt quiver: pivot at intended belt attachment point.
- Back quiver: pivot at intended upper-back attachment point.
- Rack quiver: pivot at ground center of rack footprint.
- Loose arrows: pivot at shaft midpoint for display placement.
- Arrow bundle: pivot at bundle center or lower tie point depending on display use.
- Display arrow heads: pivot at board/backing center.
- Strap variants: pivot at attach-center for reuse on quivers.
- Trophy tags: pivot at lash point.

Scale: centimeter authored, future import scale 1.0, with visual validation against the approved Giant baselines before any promotion.

Performance notes: keep material slots low, reuse arrow and strap meshes, keep cluster counts modest, and avoid unique material instances for every trophy tag or arrow head.

## Folder And Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/CHILD_ASSET_INTAKE.md`

Future package names, if promoted by later tasks:

- `SM_GIA_BloodAxeBeltQuiver_A01`
- `SM_GIA_BloodAxeBackQuiver_A01`
- `SM_GIA_BloodAxeRackQuiver_A01`
- `SM_GIA_BloodAxeArrow_A01`
- `SM_GIA_BloodAxeArrowBundle_A01`
- `KIT_GIA_BloodAxeArrowHeads_A01`
- `KIT_GIA_BloodAxeQuiverStraps_A01`
- `KIT_GIA_BloodAxeTrophyTags_A01`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied source concepts, or global index entries from this task packet.

## Approval Gates

- Stop before DCC source creation, FBX export, Unreal Content asset creation, runtime source changes, startup-scene placement, or source-concept copying.
- Stop if belt quiver, back quiver, rack quiver, loose arrows, arrow bundle, display arrow heads, strap variants, and trophy tags collapse into one single mesh assumption.
- Stop if arrow collision becomes per-arrow/per-head complexity instead of simple display collision.
- Stop before defining projectile behavior, combat rules, ammunition rules, bow animation timing, inventory behavior, or loot behavior.
- Stop if Blood Axe visual language starts replacing neutral/civilized Giant culture.
- Stop if the validated Giant scale lock or `SK_GIA_Base_A01` attachment assumptions are changed without a new approval task.
- Stop if trophy tags, skull/bone language, red cloth, or arrow count become too dense for mid-poly MMO readability.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Belt quiver, back quiver, rack quiver, loose arrows, arrow bundle, display arrow heads, strap variants, and trophy tags are all separated in the kit plan.
- The kit is docs-only and makes no DCC, FBX, Unreal Content, runtime source, startup-scene, copied concept, or projectile behavior claim.
- Silhouettes are readable at MMO camera distance and scaled for Giant hands, backs, belts, and camp props.
- Materials use scorched leather, hide, blackened iron, dark steel, rough wood, bone/horn tags, red cloth, soot, ash, and grime consistently.
- Emissive is absent from the baseline.
- Tiny stitches, scratches, pitting, leather grain, minor rivets, and small binding fibers are assigned to texture/normal detail instead of geometry.
- Triangle budgets, texture maps, material slot targets, LOD0-LOD3, collision, attachment planning, animation scope, Unreal import planning, folder recommendations, and approval gates are included.
- Arrow collision remains simple and display-focused.
