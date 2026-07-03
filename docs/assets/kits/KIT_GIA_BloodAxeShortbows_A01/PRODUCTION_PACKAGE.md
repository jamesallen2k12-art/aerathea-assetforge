# KIT_GIA_BloodAxeShortbows_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeShortbows_A01`
- Asset type: Production kit / Giant shortbow variants and support pieces
- Parent source: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#Bow_Shortbow_Set`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Related packages: `SM_GIA_BloodAxeLongbow_A01`, `KIT_GIA_BloodAxeQuivers_A01`, `KIT_GIA_BloodAxeBowParts_A01`
- Status: docs-only kit production package ready
- Scope guardrail: this package creates no DCC source, FBX export, Unreal Content asset, Unreal import, runtime source, startup-scene placement, projectile behavior, projectile collision, animation timing, combat stats, copied source concept, or final visual approval.

`KIT_GIA_BloodAxeShortbows_A01` defines four Giant-scaled Blood Axe shortbow variants plus reusable string, nock, grip, repair, and support pieces. These are hunter, scout, camp-rack, and repaired-spare bows for hostile Blood Axe Giant camps and archer silhouettes. They must read as shorter and more field-practical than `SM_GIA_BloodAxeLongbow_A01`, while still being too large for normal humanoids.

Blood Axe remains a hostile Giant sub-faction only. This kit must not overwrite neutral/civilized Giant culture, which is tied to mountain stonework, hidden cave towns, warm hearths, restrained rune or storm accents, and blue-gray masonry language in separate packages.

## Gameplay Purpose

The kit supports future Blood Axe Giant hunters, scouts, sentries, camp guards, bowyer areas, and armory dressing:

- Hunter shortbow for readable Giant field-hunter silhouettes and camp patrol dressing.
- Scout compact bow for smaller, tighter Blood Axe archer profiles without normal-humanoid scaling.
- Camp rack bow for static armory racks, shelter interiors, repair benches, and bowyer corners.
- Repaired spare bow for rough workshop storytelling, broken-and-fixed bow silhouettes, and supply piles.
- String, nock, grip wrap, repair splint, and support rack pieces that help future DCC workers build reusable bow variants without unique one-off clutter.

This package does not define projectile stats, damage values, range, attack speed, ammunition counts, projectile behavior, arrow flight, hit logic, combat traces, pickup logic, loot behavior, inventory behavior, final draw distance, release timing, reload timing, animation montage timing, or encounter balance. Any combat-facing or interactive behavior requires a separate gameplay or animation task.

## Silhouette Notes

Primary read: brutal Giant shortbows with shorter crescent arcs, thick dark stave limbs, heavy grip wraps, oversized nocks, sinew strings, blackened iron or horn reinforcement, and limited Blood Axe red cloth markers. The bows should feel compact only relative to Giant longbows, not compact relative to normal humanoid weapons.

Variant silhouettes:

- Hunter shortbow: broad practical crescent, reinforced tips, sturdy grip, one red cloth marker, and restrained bone/horn accent.
- Scout compact bow: tighter C-shaped arc, slightly shorter limb length, cleaner profile for back or side carry, and fewer hanging pieces.
- Camp rack bow: less ornate static prop variant with clear rack-facing silhouette, widened lower limb foot, and no implied equipped behavior.
- Repaired spare bow: visibly patched with large splints, rawhide lashings, replaced nock cap, and uneven but readable stave curve.
- String and nock support pieces: thick coiled sinew strings, stretched shortbow string references, oversized horn/bone/iron nock caps, grip wrap bundles, splints, and simple rack supports.

Model large forms as geometry: bow arcs, stave thickness, grip blocks, horn or iron nocks, string anchor grooves, major repair splints, broad grip wraps, rack supports, and large red cloth ties. Use textures and normal maps for wood grain, fibers, scratches, stitch lines, soot, pitting, tiny rivets, small cracks, and minor lashing detail.

## Scale Notes

Giant scale lock exactly:

- Female Giants: 14-15 ft / 427-457 cm.
- Male Giants: 14'10"-16'0" / 452-488 cm.
- Validated baseline references inherited from `SK_GIA_Base_A01`: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5".
- Author in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Suggested production scale targets:

- Hunter shortbow: 300-335 cm unstrung height, 11-19 cm primary stave thickness, 34-48 cm grip height.
- Scout compact bow: 240-290 cm unstrung height, 10-17 cm primary stave thickness, 30-44 cm grip height.
- Camp rack bow: 265-325 cm unstrung height, slightly flatter rack-facing presentation, stable display contact points.
- Repaired spare bow: 250-315 cm unstrung height, larger splints and patch plates that do not exceed the primary bow silhouette.
- Shortbow string coil: 36-70 cm diameter, 6-13 cm cord thickness depending on coil state.
- Stretched shortbow string support: 220-330 cm long, sized to shortbow rather than longbow staves.
- Nock/tip parts: 18-38 cm long, with readable string grooves and oversized Giant repair handling.
- Grip wraps and rawhide strips: 20-75 cm roll diameter, 8-16 cm strip width.
- Repair splints/support blocks: 28-90 cm long.
- Shortbow support rack: 180-285 cm tall, 120-260 cm wide, with broad feet and simple crossbars.

Attachment planning is documentation-only. Candidate future sockets or locators include `socket_bow_grip`, `socket_arrow_rest`, `socket_arrow_nock`, `socket_string_top`, `socket_string_bottom`, `socket_string_pull_ref`, `socket_back_carry_attach`, `socket_shortbow_rack_contact`, `bow_grip_l`, `bow_string_pull_r`, `arrow_nock`, `back_large_weapon`, and `back_quiver`. Final socket ownership remains with `SK_GIA_Base_A01` or a future Blood Axe archer package.

## Materials and Color Palette

Primary material language:

- Dark highland hardwood, smoke-dark stave blanks, rubbed raw-wood cuts, and hand-painted grain.
- Sinew, braided hide cord, rawhide, and waxed string material.
- Horn, bone, and antler caps for nocks, tips, wedges, and repair pieces.
- Blackened iron and dark steel for reinforcement plates, splints, nock plates, rack hardware, and repair braces.
- Scorched leather, hide, rough fur scraps, heavy grip wraps, and broad rawhide lashings.
- Torn red cloth, dull red paint, and dirty red binding as Blood Axe identifiers.
- Soot, ash, resin, oil stains, dried mud, grime, and broad hand-painted wear.

Avoid neutral/civilized Giant visual language: no blue-gray civic stone motifs, warm hearth craft presentation, peaceful highland masonry symbols, restrained blue runes, or clean monumental workshop identity. Emissive is not part of the baseline. Any shamanic, ritual, storm, or forge-glow shortbow variant requires a separate approved package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeShortbows_A01` for the world of Aerathea. The design should emphasize Giant-scaled Blood Axe shortbows for hostile Giant hunters, scouts, camp racks, and repaired spare bow dressing, with compact-but-massive bow arcs, thick dark hardwood staves, horn and blackened iron nocks, scorched leather grips, sinew strings, rawhide repair lashings, large repair splints, shortbow string coils, nock support pieces, simple rack supports, dull red cloth markers, soot, grime, brutal raider bowyer craft, and a gameplay role as static equipment and future archer visual support. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a clean production asset board with four shortbow variant callouts, support-piece callouts, scale notes against female Giant baseline 442 cm / 14'6" and male Giant baseline 470 cm / 15'5", pivot and socket notes, material swatches, LOD/collision notes, and a clear docs-only guardrail. Avoid copying any existing franchise, avoid projectile gameplay diagrams, avoid combat stats, avoid animation timing diagrams, avoid final visual approval framing, avoid making Blood Axe language the default Giant culture, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only package. Future DCC work should build the mini-kit as separate reusable bow variants and support meshes, not one collapsed armory object.

- Hunter shortbow: model a sturdy Giant-scale shortbow with thick limbs, large grip wrap, horn or iron nocks, simple string, and one controlled Blood Axe red marker.
- Scout compact bow: model a tighter shortbow profile with fewer trophies, cleaner back-carry silhouette, and reduced hanging details for small-profile Giant scouts.
- Camp rack bow: model a static display bow with durable tips, broad rack contact areas, and minimal detail density for repeated camp placement.
- Repaired spare bow: model oversized splints, replacement nock cap, rawhide wraps, patch plates, and an uneven curve while keeping the main bow arc readable.
- String pieces: model coiled spare strings, folded strings, and a stretched shortbow string support; keep fibers in texture/normal detail.
- Nock and tip pieces: model horn caps, bone inserts, blackened iron plates, string grooves, and anchor hooks that are visibly shortbow-proportioned.
- Grip and wrap pieces: model large leather rolls, rawhide strips, red cloth ties, and grip-wrap bundles as reusable support props.
- Repair pieces: model splints, wedge blocks, patch plates, clamp blocks, resin pot, and simple alignment supports without becoming a full bowyer-tools kit.
- Rack/support pieces: model a floor rack and low support cradle with broad feet, crossbars, and controlled child density.

Use real geometry for bow curves, contact points, grip mass, major nocks, string silhouette, large repair splints, rack frames, and broad wraps. Use texture and normal maps for wood pores, small cracks, string fibers, leather grain, soot streaks, stitch marks, pitting, scratches, minor chips, and tiny hammered texture.

## Texture and Material Notes

Required map set for future texture work:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No emissive map is planned for the baseline kit.

Shared material targets:

- `MI_GIA_BloodAxeBowWood_A01`
- `MI_GIA_BloodAxeBowString_A01`
- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeBoneHorn_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeSootResin_A01`

Texture naming examples:

- `T_GIA_BloodAxeHunterShortbow_A01_BC`
- `T_GIA_BloodAxeHunterShortbow_A01_N`
- `T_GIA_BloodAxeHunterShortbow_A01_ORM`
- `T_GIA_BloodAxeScoutShortbow_A01_BC`
- `T_GIA_BloodAxeScoutShortbow_A01_N`
- `T_GIA_BloodAxeScoutShortbow_A01_ORM`
- `T_GIA_BloodAxeShortbowSupport_A01_BC`
- `T_GIA_BloodAxeShortbowSupport_A01_N`
- `T_GIA_BloodAxeShortbowSupport_A01_ORM`

Material slot targets:

- Shortbow variants: 1 slot preferred, 2 slots maximum if string/leather separation is required.
- String coils, grip wraps, nock parts, and repair bundles: 1 slot preferred through shared atlased materials.
- Shortbow rack/support pieces: 1-2 slots for wood/leather plus metal/bone accents.
- Do not create one material slot per string, nock cap, strap, splint, cloth tie, or repair patch.

Packed ORM should emphasize high roughness on wood, leather, bone, horn, sinew, and cloth; restrained metallic response on blackened iron; and strong AO under wraps, splints, nocks, and rack contact points. Keep red faction marks in base color with no glow.

## Triangle Budget

Target LOD0 ranges:

- `SM_GIA_BloodAxeHunterShortbow_A01`: 3.5k-6.5k tris.
- `SM_GIA_BloodAxeScoutShortbow_A01`: 2.8k-5.5k tris.
- `SM_GIA_BloodAxeCampRackShortbow_A01`: 2.5k-5k tris.
- `SM_GIA_BloodAxeRepairedShortbow_A01`: 3.5k-7k tris.
- `SM_GIA_BloodAxeShortbowStringCoil_A01`: 350-1.1k tris per coil or folded string.
- `SM_GIA_BloodAxeShortbowStringRack_A01`: 1.8k-4.5k tris.
- `SM_GIA_BloodAxeShortbowNockParts_A01`: 800-2.8k tris per grouped display set.
- `SM_GIA_BloodAxeShortbowGripWrapBundle_A01`: 600-2k tris.
- `SM_GIA_BloodAxeShortbowRepairPieces_A01`: 1.2k-4.5k tris per grouped repair set.
- `SM_GIA_BloodAxeShortbowRackSupport_A01`: 3k-7k tris depending on rack size and visible child pieces.
- Composed shortbow/rack preview grouping: target under 28k tris by reusing bow, string, nock, wrap, and support meshes.

Budget priorities: spend geometry on the bow arc, stave thickness, grip, nocks, string line, major repair splints, rack footprint, and readable Blood Axe red markers. Do not spend geometry on tiny rivets, fine string fibers, scratch patterns, dense lashing wraps, or repeated small trophies.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full bow arcs, stave thickness, grip wrap forms, nocks, string line, major reinforcement plates, repair splints, red cloth markers, rack frames, and support-piece silhouettes.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor wrap cuts, tiny cloth tears, secondary string loops, small nock bevels, minor rack braces, and small chips.
- LOD2: 35-45 percent of LOD0; simplify nock caps, merge small repair pieces, reduce wrap-roll detail, flatten secondary reinforcement, simplify rack interiors, and reduce support-piece contents to grouped masses.
- LOD3: 15-25 percent of LOD0; preserve the shortbow arc, grip mass, string line, nock endpoints, rack footprint, red faction color blocks, and Giant-scale mass.

Remove details in this order: tiny fibers, stitch marks, pitting, scratches, small knots, tiny rivets, small nails, minor wedges, secondary bindings, tiny nock bevels, secondary repair patch bevels, then secondary rack braces. Never destroy the primary shortbow arc, grip, nocks, or string line before removing small detail.

## Collision Notes

Collision remains simple and display-focused.

- Equipped shortbow variants: collision disabled by default when attached to a character.
- World-display shortbows: one long capsule or narrow box following the bow height; optional small box around the grip for pickup focus only if a future pickup package approves it.
- String coils, grip wraps, nock parts, and repair bundles: one simple box or capsule around the grouped prop if world placement requires collision.
- String rack and shortbow support rack: grouped boxes or low-count convex hulls for feet, uprights, crossbars, and large shelves; no per-part collision inside dense racks.
- Repaired spare bow: no per-splint, per-string, or per-lashing collision.
- Back-carry preview: non-blocking attachment bounds only if future animation review requests them.

No projectile collision, arrow impact collision, combat trace collision, damage volume, runtime ammunition logic, inventory pickup collision, or interactive repair collision is defined by this docs-only package.

## Animation Notes

Static mesh baseline. No animation, final draw length, string deformation timing, reload timing, projectile launch behavior, bow draw timing, release timing, repair interaction timing, cloth simulation, physics simulation, runtime equip behavior, or animation montage timing is authored here.

Future animation or socket review, if assigned separately, should only validate visual clearance:

- Shortbow grip aligns to Giant hand sockets without shrinking the bow to normal humanoid scale.
- Nock and arrow-rest areas remain broad enough for Giant arrows from `KIT_GIA_BloodAxeQuivers_A01`.
- Back or side carry does not clip Giant shoulders, spine, arm swing, trophy armor, or quiver space.
- Rack and support props remain static camp dressing and do not block Giant pathing unless a future environment task defines collision roles.

## Unreal Import Notes

These are planned import notes only. This task does not create Unreal assets, run Unreal import, edit Content assets, add startup actors, add validators, or modify runtime source.

Planned asset types:

- Static Meshes: four shortbow variants, string coils, stretched shortbow string rack, nock part sets, grip wrap bundles, repair piece sets, and rack/support pieces.
- Material Instances: shared Blood Axe bow wood, string, scorched leather, blackened iron, bone/horn, red cloth, and soot/resin materials.

Planned folders:

- `/Game/Aerathea/Weapons/Giants/BloodAxe/Shortbows/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/Shortbows/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned naming:

- `SM_GIA_BloodAxeHunterShortbow_A01`
- `SM_GIA_BloodAxeScoutShortbow_A01`
- `SM_GIA_BloodAxeCampRackShortbow_A01`
- `SM_GIA_BloodAxeRepairedShortbow_A01`
- `SM_GIA_BloodAxeShortbowStringCoil_A01`
- `SM_GIA_BloodAxeShortbowStringRack_A01`
- `SM_GIA_BloodAxeShortbowNockParts_A01`
- `SM_GIA_BloodAxeShortbowGripWrapBundle_A01`
- `SM_GIA_BloodAxeShortbowRepairPieces_A01`
- `SM_GIA_BloodAxeShortbowRackSupport_A01`
- `MI_GIA_BloodAxeBowWood_A01`
- `MI_GIA_BloodAxeBowString_A01`

Pivot planning:

- Equipped shortbow variants: pivot at center of main grip.
- Camp rack bow: pivot at grip center for reuse; optional display duplicate may use ground or rack-contact pivot only if a future DCC task approves it.
- String coils and grip wrap rolls: pivot at center of coil mass.
- Stretched shortbow string rack: pivot at ground center or rack center depending on floor/wall variant.
- Nock part sets and repair trays: pivot at grouped display center.
- Shortbow support rack: pivot at ground center of footprint.
- Repaired spare bow: pivot at grip center unless promoted to a display-only lean variant.

Scale: centimeter authored, future import scale 1.0, with visual validation against the approved Giant baselines, `SM_GIA_BloodAxeLongbow_A01`, and `KIT_GIA_BloodAxeQuivers_A01` before any promotion.

Performance notes: reuse string, nock, wrap, repair, and support meshes across the four shortbow variants; keep material slots low; limit visible trophies and repair patches; avoid unique material instances for each support piece.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeShortbows_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeShortbows_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeShortbows_A01/CHILD_ASSET_INTAKE.md`

Future package names, if promoted by later tasks:

- `SM_GIA_BloodAxeHunterShortbow_A01`
- `SM_GIA_BloodAxeScoutShortbow_A01`
- `SM_GIA_BloodAxeCampRackShortbow_A01`
- `SM_GIA_BloodAxeRepairedShortbow_A01`
- `SM_GIA_BloodAxeShortbowStringCoil_A01`
- `SM_GIA_BloodAxeShortbowStringRack_A01`
- `SM_GIA_BloodAxeShortbowNockParts_A01`
- `SM_GIA_BloodAxeShortbowGripWrapBundle_A01`
- `SM_GIA_BloodAxeShortbowRepairPieces_A01`
- `SM_GIA_BloodAxeShortbowRackSupport_A01`

Do not add SourceAssets, Blender files, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied source concepts, validators, task-board updates, backlog edits, bootstrap edits, final visual approval captures, or global index entries from this task packet.

## Approval Gates

- Stop before DCC source creation, Blender source creation, FBX export, Unreal Content asset creation, Unreal import, material authoring, runtime source changes, startup-scene placement, validator creation, final visual approval, or source-concept copying.
- Stop before defining projectile behavior, projectile collision, combat rules, combat stats, ammunition counts, arrow damage, hit logic, pickup behavior, loot behavior, inventory behavior, bow draw distance, release timing, reload timing, repair interaction timing, or animation montage timing.
- Stop if the four shortbow variants, strings, nocks, wraps, repair pieces, and rack supports collapse into one single mesh assumption.
- Stop if collision becomes dense per-string, per-nock, per-splint, per-lashing, or per-small-repair-piece collision.
- Stop if shortbows appear sized for normal humanoids instead of the Giant scale lock.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop if the validated Giant scale lock, `SK_GIA_Base_A01` attachment assumptions, `SM_GIA_BloodAxeLongbow_A01` support relationship, or `KIT_GIA_BloodAxeQuivers_A01` dependency changes without a new approval task.
- Stop if skulls, trophies, red cloth, repair patches, string coils, or tiny texture detail become too dense for mid-poly MMO readability.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female Giants 14-15 ft / 427-457 cm; male Giants 14'10"-16'0" / 452-488 cm; baseline references female 442 cm / 14'6" and male 470 cm / 15'5".
- Shortbows are Giant-scaled and readable, not normal humanoid bows.
- Four shortbow variants are covered: hunter shortbow, scout compact bow, camp rack bow, and repaired spare bow.
- Child support coverage includes strings, stretched string support, nock parts, grip wraps, repair pieces, and rack/support pieces.
- Projectile behavior, projectile collision, combat stats, combat rules, and animation timing are explicitly out of scope.
- Primary silhouettes read at MMO camera distance and preserve bow arcs, grips, nocks, strings, rack footprint, and Giant-scale mass.
- Materials use dark highland wood, sinew, rawhide, scorched leather, blackened iron, dark steel, bone/horn, red cloth, soot, resin, and grime consistently.
- Emissive is absent by default and approval-gated for any future ritual, shamanic, storm, or forge-heat variant.
- Tiny fibers, scratches, pitting, stitch marks, wood grain, small rivets, and minor binding detail are assigned to textures or normals instead of geometry.
- Texture maps, material slot targets, triangle budgets, LOD0-LOD3, collision planning, pivot planning, socket planning, Unreal import planning, folder naming, approval gates, child package recommendations, and docs-only guardrails are included.
- The package makes no DCC, FBX, Unreal Content, Unreal import, runtime source, global index, task board, external concept copy, startup-scene placement, projectile behavior, animation timing, combat stats, or final visual approval claim.
