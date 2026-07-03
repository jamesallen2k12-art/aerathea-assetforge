# KIT_GIA_BloodAxeHunters_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeHunters_A01`
- Asset type: Production kit / Blood Axe Giant hunter role, wearable loadout, and camp dressing plan
- Source concept reference: `GiantBloodAxeHuntersMale.png` routing from the Giant/Blood Axe slate; source concept remains external and is not copied, moved, edited, embedded, or committed by this docs-only task.
- Parent visual language: `KIT_GIA_BloodAxeArmory_A01`
- Approved bow dependencies: `SM_GIA_BloodAxeLongbow_A01`, `SM_GIA_BloodAxeLongbow_A02`, `SM_GIA_BloodAxeLongbow_A03`, `KIT_GIA_BloodAxeShortbows_A01`
- Approved quiver dependency: `KIT_GIA_BloodAxeQuivers_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready; no first DCC target selected

`KIT_GIA_BloodAxeHunters_A01` defines the planning lane for Blood Axe Giant archer, scout, trapper, and tracker silhouettes. The kit should read as a hostile hunting party using Giant-scale bows, quivers, hide cloaks, trap bundles, trophy tags, rough camp racks, and brutal field gear. It must remain separate from neutral/civilized Giant culture and must not turn all Giants into Blood Axe raiders.

This package reuses approved bow and quiver planning instead of redefining weapon behavior. It does not create DCC source, SourceAssets folders, FBX exports, Unreal Content, runtime source, validators, startup placements, external concept copies, projectile behavior, ammo rules, AI, stealth, patrol logic, combat stats, animation timing, final visual approval, or first DCC target selection.

## Gameplay Purpose

The hunter kit supports future visual planning for Blood Axe Giant ranged NPC groups, hunting-party silhouettes, camp dressing, armory racks, and field-gear variants. It is a production bridge between the Blood Axe armory kit and future warband or camp packages.

Expected visual uses:

- Archer silhouette using approved Giant longbow and back/belt quiver planning.
- Scout silhouette using the approved shortbow kit and cleaner carry profile.
- Trapper silhouette using static trap bundles, rope, hooks, hide rolls, and rack dressing without trap behavior.
- Tracker silhouette using hide cloak, trophy tags, footprint-marker props, and field gear without stealth or patrol logic.
- Camp and rack variants that reuse approved shortbow, quiver, arrow bundle, trophy tag, and rack planning.

Out of scope: projectile behavior, ammunition rules, AI, stealth, patrol logic, trap triggering, combat stats, encounter tuning, animation timing, loot rules, inventory behavior, pickup behavior, crafting, economy, final visual approval, and DCC target selection.

## Silhouette Notes

Primary read: tall Blood Axe Giant hunters with massive but practical ranged gear. The silhouette should come from a Giant body mass, broad shoulders, bow arc, back quiver or hip quiver, hide cloak, hanging trophy tags, heavy boots, wrapped forearms, and rough camp-rack props. Keep the design readable at MMO camera distance and avoid dense skull clutter.

Role silhouette targets:

- Archer: longbow or cleaner common-archer longbow, tall back quiver, heavy bracer, red cloth marker, and sparse trophy tags.
- Scout: shorter bow profile, tighter side/back carry, lighter cloak edge, fewer hanging pieces, and clear movement silhouette without stealth mechanics.
- Trapper: rope coil, hook bundle, large static trap bundle, hide-wrapped gear, and waist/back loadout that reads as equipment, not gameplay logic.
- Tracker: hide cloak, bone/horn markers, rough field satchel, trophy tag strand, and grounded hunter profile.
- Hide-cloak: broad shoulder mantle, fur/hide break across the back, ragged lower edge, and large readable folds instead of dense hair strands.
- Camp/rack variants: large bow racks, quiver racks, arrow bundles, hide drying frames, trophy tag strings, and repair props scaled for 470 cm male Giant review.

Avoid neutral/civilized Giant stoneworker cues, blue-gray civic stone motifs, warm hearth presentation, restrained blue runes, clean masonry symbols, elegant Elven archer language, normal-humanoid bow proportions, graphic gore, and dense micro-detail.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Planning scale targets:

- Full hunter loadout on base Giant body: fit both female 442 cm and male 470 cm baselines without changing race scale.
- Longbows: inherit dimensions from `SM_GIA_BloodAxeLongbow_A01`, `A02`, and `A03`.
- Shortbows: inherit dimensions from `KIT_GIA_BloodAxeShortbows_A01`, including hunter, scout, camp-rack, and repaired-spare variants.
- Quiver loadout: inherit belt, back, rack, loose arrow, arrow bundle, strap, and trophy tag dimensions from `KIT_GIA_BloodAxeQuivers_A01`.
- Hide cloak: shoulder width must clear Giant neck, shoulders, quiver straps, and bow carry; lower edge should land between mid-thigh and calf depending on role.
- Trophy tags: 18-45 cm accents reused from quiver planning; use sparingly.
- Camp/rack props: scale as Giant-made field equipment beside a 470 cm male Giant, not as small-folk camp dressing.

Attachment planning references include `back_quiver`, `belt_quiver_l`, `belt_quiver_r`, `belt_tool_l`, `belt_tool_r`, `back_large_weapon`, `hand_l_offhand`, `bow_grip_l`, `bow_string_pull_r`, `arrow_nock`, and future hunter loadout sockets. Final socket ownership remains deferred to `SK_GIA_Base_A01` or a future Blood Axe archer/warband package.

## Materials and Color Palette

Primary materials:

- Scorched leather, rough hide, fur, sinew, rawhide, and heavy cord.
- Dark highland wood and soot-dark bow staves inherited from approved bow packages.
- Blackened iron, dark steel, crude buckles, hooks, rings, and heavy braces.
- Bone, horn, tooth, broken tokens, and trophy tags used sparingly.
- Torn dull red cloth, dirty red binding, and restrained red war-paint marks.
- Soot, ash, dried mud, grime, oil stains, and broad hand-painted wear.

Palette control:

- Base colors: charcoal, dark umber, gray-brown wood, scorched leather brown, dirty hide tan, soot black, and muted bone.
- Accent colors: dull Blood Axe red on cloth ties, tag strings, bow wraps, and warning marks.
- No baseline emissive. Any shamanic, ritual, storm, necromantic, or forge-heat glow requires a separate approved package.
- Do not use neutral/civilized Giant blue-gray stonework, warm hearth colors, or restrained blue rune motifs in this hostile hunter kit.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeHunters_A01` for the world of Aerathea. The design should emphasize hostile Blood Axe Giant hunter silhouettes, archer, scout, trapper, tracker, hide-cloak, quiver loadout, trophy tags, camp/rack variants, Giant-scale bows, back and belt quivers, rough hide cloaks, scorched leather, dark highland wood, blackened iron, bone and horn tags, dull red cloth markers, soot, grime, brutal field-camp craft, and visual support for ranged hunter roles. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a production asset board with four role silhouettes, hide-cloak callouts, quiver and bow reuse notes, trophy tag limits, camp/rack dressing callouts, material swatches, and scale callouts against female Giant baseline 442 cm / 14'6" and male Giant baseline 470 cm / 15'5" on a clean background. Avoid copying any existing franchise, avoid graphic gore, avoid projectile behavior diagrams, avoid ammo rules, avoid AI, avoid stealth UI, avoid patrol route diagrams, avoid combat stat callouts, avoid final visual approval framing, avoid making Blood Axe language the default Giant culture, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only planning package. Future DCC work should split the kit into reusable role loadouts and static camp dressing instead of one collapsed hunter mesh.

Model real geometry for:

- Large hide cloak forms, shoulder mantle, broad folds, ragged lower edge, and major fur/hide panels.
- Broad leather straps, large buckles, quiver straps, belt loops, rope coils, hook bundles, and trapper gear blocks.
- Bow and quiver meshes only through their approved child packages; do not remake those packages inside this hunter kit.
- Large trophy tags, tooth charms, bone plates, and red cloth ties as sparse reusable accents.
- Static camp/rack pieces: bow rack frames, quiver rack bodies, arrow bundle rests, hide drying frames, and field-gear pegs.

Use texture and normal maps for:

- Fur grain, hide pores, leather stitching, small scratches, soot streaks, mud smears, pitting, tiny rivets, cord fibers, frayed cloth, and minor tag cracks.

Role loadout notes:

- Archer should prioritize longbow/quiver silhouette and readable hand/back clearance.
- Scout should reuse approved shortbow planning and keep side/back carry uncluttered.
- Trapper should show rope, hooks, bundled static traps, and hide-wrapped field gear without trigger or gameplay behavior.
- Tracker should emphasize hide cloak, tag markers, field satchel, and readable terrain-worn material language without stealth or patrol logic.

## Texture and Material Notes

Required map set for future texture work:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No emissive map is planned for the baseline hunter kit.

Shared material targets:

- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeHideFur_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeBowWood_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeBoneTrophy_A01`
- `MI_GIA_BloodAxeSootMud_A01`

Texture naming examples:

- `T_GIA_BloodAxeHunterHideCloak_A01_BC`
- `T_GIA_BloodAxeHunterHideCloak_A01_N`
- `T_GIA_BloodAxeHunterHideCloak_A01_ORM`
- `T_GIA_BloodAxeHunterLoadout_A01_BC`
- `T_GIA_BloodAxeHunterLoadout_A01_N`
- `T_GIA_BloodAxeHunterLoadout_A01_ORM`
- `T_GIA_BloodAxeHunterCampRack_A01_BC`
- `T_GIA_BloodAxeHunterCampRack_A01_N`
- `T_GIA_BloodAxeHunterCampRack_A01_ORM`

Material slot targets:

- Wearable role loadouts: 2-3 slots across hide/fur/leather, metal, and trophy/cloth accents.
- Hide cloak: 1-2 slots, with fur/hide in texture detail rather than dense strand geometry.
- Trophy tag clusters and quiver loadout accents: reuse quiver material families; do not create one material slot per tag.
- Camp/rack variants: 1-2 slots for wood/hide plus metal/trophy accents.

## Triangle Budget

Target LOD0 ranges for future child assets:

- Full hunter loadout overlay, excluding base Giant body and approved bow/quiver meshes: 12k-25k tris per role.
- Archer/scout/trapper/tracker complete visual composition, including reused bow and quiver meshes: target 30k-55k tris depending on selected approved bow/quiver variants.
- `SK_GIA_BloodAxeHideCloak_A01`: 5k-12k tris.
- `KIT_GIA_BloodAxeHunterQuiverLoadout_A01`: 8k-18k tris when composed from approved quiver children.
- `KIT_GIA_BloodAxeHunterTrophyTags_A01`: 300-1.5k tris per tag cluster.
- `KIT_GIA_BloodAxeHunterCampRack_A01`: 10k-28k tris per composed static camp/rack grouping, using repeated child meshes.

Budget priorities: spend geometry on the base role silhouette, hide cloak mass, large straps, quiver/bow clearance, camp rack footprint, and a small number of major trophy tags. Do not spend geometry on tiny stitch rows, dense fur strands, small scratches, fine rope fibers, repeated skull clutter, or excessive arrow count.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full role silhouette, hide cloak panels, large straps, quiver and bow attachment clearances, major trophy tags, trapper gear blocks, tracker satchel, and camp/rack silhouettes.
- LOD1: 60-70 percent of LOD0; reduce small folds, strap bevels, tag bevels, cloth tears, rope coil subdivisions, rack brace bevels, and inner dressing density.
- LOD2: 35-45 percent of LOD0; simplify cloak underside, merge small straps, flatten secondary tags, reduce trapper bundle parts, simplify rack interiors, and reduce camp dressing child count.
- LOD3: 15-25 percent of LOD0; preserve Giant hunter mass, cloak outline, bow/quiver read, red faction accents, and camp/rack footprint.

Reduce details in this order: tiny stitches, pitting, scratches, fur strands, small cloth tears, minor rope fibers, tiny tags, secondary straps, small hooks, inner/back-side details, then secondary rack braces. Never destroy the primary Giant body read, bow/quiver silhouette, hide cloak outline, or camp/rack footprint first.

## Collision Notes

Collision remains simple and planning-only.

- Worn hunter loadouts: no independent blocking collision by default; future character physics asset and attachment review handle body interaction.
- Approved bows and quivers: inherit collision policy from `SM_GIA_BloodAxeLongbow_A01-A03`, `KIT_GIA_BloodAxeShortbows_A01`, and `KIT_GIA_BloodAxeQuivers_A01`.
- Hide cloak: attachment preview bounds only; no cloth physics or per-fold collision in this package.
- Trapper gear bundles: one simple box or capsule for display placement only; no trap trigger, damage, or interaction collision.
- Trophy tags: no standalone collision unless promoted to a large world prop.
- Camp/rack variants: grouped boxes or low-count convex hulls for feet, uprights, frames, and shelves; no per-arrow, per-tag, per-rope, or per-hook collision.

No projectile collision, ammo collision, combat trace collision, AI sensing collision, stealth volume, patrol volume, trap trigger, damage volume, pickup collision, or loot collision is defined by this docs-only package.

## Animation Notes

Static mesh and wearable planning baseline only. This package authors no animation, no animation timing, no bow draw timing, no reload timing, no projectile launch behavior, no AI locomotion, no stealth behavior, no patrol logic, no trap trigger timing, no cloth simulation, and no physics setup.

Future animation or fit review, if assigned separately, should only validate visual clearance:

- Longbow and shortbow carry clears shoulders, elbows, back quiver, hide cloak, and trophy armor.
- Back and belt quivers remain reachable and do not clip the Giant pelvis, thighs, spine, or shoulders.
- Hide cloak does not obscure the main Giant read or collapse the archer/scout silhouette.
- Trapper and tracker loadouts do not block expected Giant arm swing or leg motion.

## Unreal Import Notes

These are planned future import notes only. This task does not create Unreal assets, run Unreal import, create DCC files, export FBX, add runtime source, place startup actors, create validators, or select a first DCC target.

Planned asset types:

- Production kit: `KIT_GIA_BloodAxeHunters_A01`
- Future wearable Skeletal Mesh or modular clothing targets for hide cloak and role loadouts.
- Future Static Mesh targets for trophy tags, trapper bundles, tracker field props, and camp/rack variants.
- Material Instances reusing Blood Axe hide, leather, iron, bow wood, red cloth, bone trophy, soot, and mud families.

Planned folders:

- `/Game/Aerathea/Characters/Giants/BloodAxe/Hunters/`
- `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/Hunters/`
- `/Game/Aerathea/Props/Giants/BloodAxeCamp/Hunters/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/Quivers/`
- `/Game/Aerathea/Weapons/Giants/BloodAxe/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned naming:

- `KIT_GIA_BloodAxeHunterArcher_A01`
- `KIT_GIA_BloodAxeHunterScout_A01`
- `KIT_GIA_BloodAxeHunterTrapper_A01`
- `KIT_GIA_BloodAxeHunterTracker_A01`
- `SK_GIA_BloodAxeHideCloak_A01`
- `KIT_GIA_BloodAxeHunterQuiverLoadout_A01`
- `KIT_GIA_BloodAxeHunterTrophyTags_A01`
- `KIT_GIA_BloodAxeHunterCampRack_A01`

Pivot planning:

- Wearable loadouts and hide cloak: align to the Giant skeleton or body origin in a future fit lane.
- Trophy tags: pivot at lash point.
- Trapper gear bundles: pivot at carry or display center depending on future promotion.
- Camp/rack props: pivot at ground center of footprint.
- Bow and quiver pivots: inherit approved bow/quiver package planning.

Scale: centimeter authored, future import scale 1.0, with validation against female 442 cm and male 470 cm Giant baselines before any visual review.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeHunters_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeHunters_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeHunters_A01/CHILD_ASSET_INTAKE.md`
- Related existing packages: `KIT_GIA_BloodAxeArmory_A01`, `SM_GIA_BloodAxeLongbow_A01`, `SM_GIA_BloodAxeLongbow_A02`, `SM_GIA_BloodAxeLongbow_A03`, `KIT_GIA_BloodAxeShortbows_A01`, and `KIT_GIA_BloodAxeQuivers_A01`.

Do not add SourceAssets, Blender files, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied external concepts, validators, task-board updates, backlog edits, bootstrap edits, global index entries, final visual approval captures, or first DCC target selection from this task packet.

## Approval Gates

- Lead approval is required before selecting any first DCC target.
- DCC approval is required before creating source folders, Blender files, source meshes, LOD sources, proof renders, or FBX exports.
- Unreal approval is required before importing Static Meshes, Skeletal Meshes, materials, textures, Blueprints, validators, or startup actors.
- Gameplay approval is required before projectile behavior, ammo rules, combat stats, hit logic, trap triggering, stealth, patrol logic, loot, pickup, crafting, economy, or inventory behavior.
- Animation approval is required before bow draw timing, release timing, reload timing, locomotion variants, cloak simulation, physics, or animation montage timing.
- Visual approval is required before final hunter role silhouettes, hide-cloak shape, trophy density, camp dressing density, or hero variant language are locked.
- Culture approval is required if Blood Axe hostile raider language starts bleeding into neutral/civilized Giant packages.
- Source-storage approval is required before any external concept file enters the repository.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit and unchanged: female 442 cm / 14'6" and male 470 cm / 15'5".
- Archer, scout, trapper, tracker, hide-cloak, quiver loadout, trophy tags, and camp/rack variants are covered as planning-only rows in the child intake.
- Approved bow and quiver planning is reused rather than redefined.
- Character role silhouettes remain Giant-scaled and readable at MMO camera distance.
- Materials use scorched leather, rough hide, fur, dark wood, blackened iron, bone/horn, red cloth, soot, ash, mud, and grime consistently.
- Emissive is absent by default and approval-gated for any future ritual, shamanic, storm, necromantic, or forge-heat variant.
- Tiny stitches, scratches, pitting, fur strands, small rivets, rope fibers, and minor tag cracks are assigned to textures or normals instead of geometry.
- Triangle budgets, texture maps, material slot targets, LOD0-LOD3, collision planning, socket references, animation scope, Unreal import planning, folder naming, and approval gates are included.
- No projectile behavior, ammo rules, AI, stealth, patrol logic, combat stats, animation timing, final visual approval, or first DCC target selection is claimed.
- The package makes no DCC, SourceAssets, FBX, Unreal Content, runtime source, external concept copy, validator, startup-scene, global index, task board, or backlog edit claim.
