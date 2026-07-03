# KIT_GIA_BloodAxeBowParts_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeBowParts_A01`
- Asset type: Production kit / Giant bow parts, bowyer rack, and repair accessory set
- Parent source: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#BowStaveParts_Set`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only kit production package ready
- Scope guardrail: this package creates no DCC source, FBX export, Unreal Content asset, runtime source, startup-scene placement, projectile stats, combat rules, animation timing, or copied concept art.

`KIT_GIA_BloodAxeBowParts_A01` defines a Giant-scale bowyer mini-kit for Blood Axe camps, armory racks, repair benches, and static workshop dressing. It covers spare bow strings, replacement limbs, longbow stave sections, arrow shafts, arrow heads, leather wraps, nock parts, repair clamps, rack variants, and bundled parts. The kit supports `SM_GIA_BloodAxeLongbow_A01` and future Blood Axe bow variants as visual dressing and construction support, not as gameplay ammunition or combat tuning.

Blood Axe identity must stay hostile, brutal, and raider-specific: dark highland wood, scorched leather, sinew, blackened iron, horn, bone, torn red cloth markers, soot, grime, and rough repair work. This visual language must remain separate from neutral/civilized Giant culture, which uses blue-gray stoneworker craft, warm hearth presentation, and restrained blue rune language in other packages.

## Gameplay Purpose

The kit provides static environment and equipment-support pieces for Blood Axe bowyer areas:

- Rack and workshop dressing for hostile Giant camps, bowyer corners, armory tents, forge-adjacent work areas, and loot silhouettes.
- Longbow support pieces that visually explain repair, restringing, stave replacement, and arrow-head preparation for Giant archers.
- Reusable child meshes for bow strings, limbs, shafts, heads, wraps, nock pieces, repair blocks, and bundles.
- Scale references for future Blood Axe longbow, shortbow, quiver, and bowyer tool packages.

This package does not define projectile stats, damage values, ammunition counts, arrow flight behavior, hit detection, combat traces, pickup logic, loot rules, inventory behavior, bow draw distances, release timing, reload timing, or animation montage timing. Any interactive or combat-facing behavior requires a separate gameplay or animation task.

## Silhouette Notes

Primary read: oversized Giant bow construction parts laid out for harsh Blood Axe repair work. Each child should look functional at Giant scale and readable at MMO camera distance, with a small number of bold details instead of dense clutter.

- Bow strings: thick sinew, cord, or braided hide loops, coiled or stretched on a simple rack. Read as heavy cord, not fine thread.
- Replacement limbs: tall curved stave sections with reinforced tips, broad repaired cracks, horn caps, and blackened iron splints.
- Arrow shafts: long straight shafts grouped in bundles, repair racks, or drying cradles; preserve length and direction as the first read.
- Arrow heads: broadhead, barbed, bodkin, and blunt training/repair variants, displayed in trays or nailed to rough boards.
- Wraps: scorched leather grip wraps, red cloth ties, sinew binding strips, and rawhide coils, grouped as useful workshop stock.
- Nock parts: oversized horn, bone, and blackened iron nock caps, string grooves, tip plates, and replacement anchor pieces.
- Racks: floor-standing or wall-leaning Giant workshop racks with stable feet, crossbars, clamps, and visible part silhouettes.
- Repair pieces: splints, clamps, patch plates, resin pots, wedge blocks, and crude alignment blocks that show bow maintenance without becoming a full tool kit.
- Bundle variants: tied limb bundles, string coils, shaft bundles, and mixed repair bundles that can populate shelves, carts, racks, and tables.

Model large forms as geometry: rack frames, stave limbs, horn caps, major string coils, arrow shafts, arrow heads, wrap rolls, clamps, splints, wedges, and broad red cloth ties. Use texture and normal detail for wood grain, small cracks, scratches, pitting, soot, stitch lines, minor fibers, tiny rivets, and small binding marks.

## Scale Notes

Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

- Author in centimeters. 1 Unreal unit = 1 cm.
- Fit all longbow support pieces to `SM_GIA_BloodAxeLongbow_A01` proportions and the validated `SK_GIA_Base_A01` scale lock.
- Normal humanoid compatibility is not required.
- Static rack and workshop pieces should read as Giant-built beside a 470 cm male Giant.
- Wearable or equipped behavior is not authored here; parts may inform future socket clearance but remain static display/support pieces in this package.

Suggested production scale targets:

- Spare bow string coil: 45-85 cm diameter, 8-16 cm cord thickness depending on coil state.
- Stretched bow string rack: 240-430 cm long depending on longbow or shortbow support.
- Replacement longbow limb: 180-260 cm long per half limb, 12-24 cm thick at major sections.
- Full spare stave or rough blank: 330-455 cm long, 18-34 cm thick before shaping.
- Arrow shaft stock: 180-260 cm long, 3-8 cm diameter, bundled in groups that imply volume without modeling every shaft uniquely.
- Arrow head pieces: 25-70 cm long depending on broadhead/barbed/bodkin/blunt type.
- Wrap coils and leather strips: 30-90 cm across for rolls, 8-18 cm wide for strips.
- Nock caps and tip parts: 25-55 cm long, sized to longbow tips and readable string grooves.
- Bowyer rack: 220-340 cm tall, 140-320 cm wide, with stable floor contact and broad crossbars.
- Repair clamps/splints: 35-110 cm long, oversized for Giant hands and longbow limbs.
- Bundle variants: 90-280 cm long depending on contents, with clear tied mass and one or two Blood Axe red markers.

## Materials and Color Palette

Primary material language:

- Dark highland hardwood and rough bow stave blanks in dark brown, gray-brown, soot-stained ochre, and rubbed raw-wood cuts.
- Sinew, braided hide cord, rawhide, heavy fiber, and waxed string material.
- Horn, bone, and antler caps for nocks, tips, wedges, and arrow-head displays.
- Blackened iron, dark steel, and reforged scrap plates for splints, clamp jaws, arrow heads, racks, and repair braces.
- Scorched leather, hide, fur scraps, grip wraps, and wide red cloth ties.
- Soot, ash, resin, oil stains, grime, broad hand-painted wear, and dull red Blood Axe paint.

Avoid neutral/civilized Giant visual language: no blue-gray civic stone motifs, warm hearth craft presentation, peaceful highland masonry symbols, restrained blue runes, or clean monumental workshop identity. Blood Axe bowyer work should look raider-made, field-repaired, and hostile without becoming visually unreadable or graphic.

Emissive is not part of the baseline. No glow maps are expected for this kit. Any shamanic, ritual, or storm-charged bow-part variant requires a separate approved package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeBowParts_A01` for the world of Aerathea. The design should emphasize Giant-scale Blood Axe bowyer parts, spare bow strings, replacement longbow limbs, stave blanks, arrow shafts, arrow heads, scorched leather grip wraps, nock caps, horn tips, repair splints, crude clamps, floor racks, wall racks, tied part bundles, dark highland wood, sinew, blackened iron, dark steel, bone, horn, torn red cloth markers, hostile raider workshop culture, static armory dressing, and longbow support. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a clean production asset board with child part callouts, rack and bundle variants, longbow scale reference, and scale callouts against female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5" Giants. Avoid copying any existing franchise, avoid projectile gameplay diagrams, avoid combat stats, avoid making Blood Axe language the default Giant culture, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only package. Future DCC work should build the mini-kit as reusable child meshes and bundle compositions, not one collapsed workshop object.

- Bow string set: model coiled strings, folded strings, and one stretched display string with large looped ends. Keep individual fibers in texture/normal detail.
- Replacement limbs: model upper and lower limb sections with broad curvature, repair scars, horn/iron tip pieces, and optional split-stave profiles.
- Stave blanks: model rough unstrung longbow blanks and shaped half-limbs that can lean against a rack or rest on a bench.
- Arrow shafts: model straight shafts, rough-cut shafts, drying shafts, and a few reusable shaft tips. Use grouped clusters for high counts.
- Arrow heads: model a small set of large silhouettes: broadhead, barbed, bodkin, blunt, and unfinished forged head. Avoid dozens of tiny head variants.
- Wraps: model leather rolls, red cloth strips, sinew coils, rawhide lashings, and grip wrap bundles as simple readable stock pieces.
- Rack variants: model a floor rack, wall rack, and low workbench cradle with broad crossbars, stable feet, and simple clamp points.
- Repair pieces: model blackened iron splints, horn nock caps, bone wedges, resin pot, clamp jaws, alignment blocks, and replacement string anchors.
- Nock parts: model top/bottom nock caps, grooved horn inserts, iron tip plates, and anchor hooks that align visually with `SM_GIA_BloodAxeLongbow_A01`.
- Bundle variants: model tied string coils, limb bundles, arrow shaft bundles, mixed repair bundles, and small crates/trays of nock or head pieces.

Use real geometry for silhouettes, contact points, large rings, clamp jaws, crossbars, stave curves, major arrow heads, horn caps, and broad wrap rolls. Use texture and normal maps for wood pores, small cracks, fine soot, string fibers, leather grain, tiny stitch marks, pitting, scratches, and minor hammered texture.

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

- `T_GIA_BloodAxeBowParts_A01_BC`
- `T_GIA_BloodAxeBowParts_A01_N`
- `T_GIA_BloodAxeBowParts_A01_ORM`
- `T_GIA_BloodAxeBowRack_A01_BC`
- `T_GIA_BloodAxeBowRack_A01_N`
- `T_GIA_BloodAxeBowRack_A01_ORM`
- `T_GIA_BloodAxeArrowParts_A01_BC`
- `T_GIA_BloodAxeArrowParts_A01_N`
- `T_GIA_BloodAxeArrowParts_A01_ORM`

Material slot targets:

- Small part meshes: 1 slot where practical.
- Racks and workbench cradles: 1-2 slots for wood/leather plus metal/bone accents.
- Arrow head boards or repair trays: 1-2 slots depending on backing material.
- Bundle variants: 1 material slot preferred through shared atlased materials.
- Do not create one material slot per string, shaft, wrap, nail, nock, or arrow head.

Packed ORM should emphasize high roughness on wood/leather/bone/string, restrained metallic on blackened iron, strong AO under wraps and rack contact points, and no glow.

## Triangle Budget

Target LOD0 ranges:

- `SM_GIA_BloodAxeBowStringCoil_A01`: 400-1.2k tris per coil or folded string.
- `SM_GIA_BloodAxeBowStringRack_A01`: 2k-5k tris.
- `SM_GIA_BloodAxeReplacementLimb_A01`: 1.5k-4k tris per limb section.
- `SM_GIA_BloodAxeStaveBlank_A01`: 1k-3k tris per blank.
- `SM_GIA_BloodAxeArrowShaftSet_A01`: 900-2.8k tris per grouped shaft set.
- `SM_GIA_BloodAxeArrowHeadTray_A01`: 1.5k-4.5k tris depending on head count.
- `SM_GIA_BloodAxeWrapBundle_A01`: 600-2k tris.
- `SM_GIA_BloodAxeBowNockParts_A01`: 900-3k tris per grouped display set.
- `SM_GIA_BloodAxeBowRepairPieces_A01`: 1.5k-5k tris per grouped repair set.
- `SM_GIA_BloodAxeBowPartsRack_A01`: 4k-9k tris depending on rack size and visible child pieces.
- `SM_GIA_BloodAxeBowPartsWallRack_A01`: 2.5k-7k tris depending on wall support and visible child pieces.
- `SM_GIA_BloodAxeBowWorkbenchCradle_A01`: 2k-6k tris depending on clamp and cradle complexity.
- `SM_GIA_BloodAxeLimbBundle_A01`: 1.2k-3.5k tris depending on visible limb count.
- `SM_GIA_BloodAxeArrowPartsBundle_A01`: 1.2k-3.5k tris depending on visible shaft/head/wrap count.
- `SM_GIA_BloodAxeBowPartsBundle_A01`: 1.2k-4k tris depending on contents.
- Composed workshop/rack preview grouping: target under 35k tris by reusing child meshes and avoiding individually unique high-count shafts or heads.

Budget priorities: spend geometry on rack footprint, stave curves, long shaft direction, large arrow-head silhouettes, nock grooves, clamp jaws, and bundle mass. Keep tiny scratches, fibers, pitting, stitch marks, and small carved marks in texture/normal detail.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full rack frames, stave/limb curves, string loops, arrow shaft direction, arrow-head silhouettes, nock grooves, clamp jaws, wrap rolls, red cloth markers, and major material breaks.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor rack braces, secondary string loops, extra shaft count, tiny cloth tears, small clamp details, and nock cap bevels.
- LOD2: 35-45 percent of LOD0; simplify rack interiors, merge small repair pieces, reduce arrow-head interior cuts, simplify wrap rolls, and reduce bundle contents to clear grouped masses.
- LOD3: 15-25 percent of LOD0; preserve rack footprint, stave/limb direction, shaft bundle direction, broad arrow-head shapes, red cloth accents, and Giant-scale mass.

Remove details in this order: tiny fibers, stitch marks, pitting, scratches, small knots, small nails, minor wedges, secondary bindings, duplicate shaft interiors, tiny nock bevels, then secondary rack braces. Never destroy the primary rack silhouette, longbow limb curve, shaft direction, or large head/nock profile first.

## Collision Notes

Collision remains simple and display-focused.

- Bow string coils, wrap bundles, nock parts, arrow heads, and repair trays: one simple box or capsule around the grouped prop if world placement requires collision.
- Replacement limbs and stave blanks: one narrow capsule or box along the length for display placement; no per-splinter collision.
- Arrow shaft sets and shaft bundles: one long box/capsule around the bundle; no per-shaft collision.
- Floor racks and wall racks: grouped boxes or low-count convex hulls for feet, uprights, crossbars, and large shelves; no per-part collision inside dense racks.
- Repair clamps and splints: collision disabled when used as small set dressing; grouped simple collision only for larger trays or bench pieces.
- Equipped or socketed future support parts: collision disabled unless a separate attachment task defines a specific preview volume.

No projectile collision, arrow impact collision, combat trace collision, damage volume, or interactive repair collision is defined by this docs-only package.

## Animation Notes

Static mesh baseline. No animation, draw timing, string deformation timing, reload timing, projectile launch behavior, repair interaction timing, cloth simulation, physics simulation, or runtime equip behavior is authored here.

Future animation or socket review, if assigned separately, should only use these parts for visual clearance:

- Longbow support parts align visually with `SM_GIA_BloodAxeLongbow_A01` nock and limb scale.
- String coils and stretched strings remain plausible for Giant hand scale.
- Racks and benches do not block Giant pathing if placed as static dressing.
- Part bundles can be lifted or carried only after a future gameplay/animation package defines attachment behavior.

## Unreal Import Notes

These are planned import notes only. This task does not create Unreal assets.

Planned asset types:

- Static Meshes: string coils, stretched string rack, replacement limbs, stave blanks, arrow shaft sets, arrow head trays, wrap bundles, nock part sets, repair piece sets, floor racks, wall racks, workbench cradles, and bundle variants.
- Material Instances: shared Blood Axe bow wood, string, scorched leather, blackened iron, bone/horn, red cloth, and soot/resin materials.

Planned folders:

- `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowRacks/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/ArrowParts/`
- `/Game/Aerathea/Weapons/Giants/BloodAxe/Support/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned naming:

- `SM_GIA_BloodAxeBowStringCoil_A01`
- `SM_GIA_BloodAxeBowStringRack_A01`
- `SM_GIA_BloodAxeReplacementLimb_A01`
- `SM_GIA_BloodAxeStaveBlank_A01`
- `SM_GIA_BloodAxeArrowShaftSet_A01`
- `SM_GIA_BloodAxeArrowHeadTray_A01`
- `SM_GIA_BloodAxeWrapBundle_A01`
- `SM_GIA_BloodAxeBowNockParts_A01`
- `SM_GIA_BloodAxeBowRepairPieces_A01`
- `SM_GIA_BloodAxeBowPartsRack_A01`
- `SM_GIA_BloodAxeBowPartsWallRack_A01`
- `SM_GIA_BloodAxeBowWorkbenchCradle_A01`
- `SM_GIA_BloodAxeLimbBundle_A01`
- `SM_GIA_BloodAxeArrowPartsBundle_A01`
- `SM_GIA_BloodAxeBowPartsBundle_A01`
- `MI_GIA_BloodAxeBowWood_A01`
- `MI_GIA_BloodAxeBowString_A01`

Pivot planning:

- String coils and wrap rolls: pivot at center of coil mass.
- Stretched string rack: pivot at ground center or rack center depending on floor/wall variant.
- Replacement limbs and stave blanks: pivot at part center for rack placement; optional lower-end pivot only for lean-against-wall variants.
- Arrow shaft sets: pivot at bundle center or lower tie point for rack insertion.
- Arrow head trays and repair trays: pivot at tray/backing center.
- Floor racks: pivot at ground center of footprint.
- Wall racks: pivot at back-plane center for wall snapping.
- Workbench cradles: pivot at ground or bench contact center.
- Nock and repair piece sets: pivot at grouped display center.

Scale: centimeter authored, future import scale 1.0, with visual validation against the approved Giant baselines and `SM_GIA_BloodAxeLongbow_A01` before any promotion.

Performance notes: reuse stave, shaft, head, wrap, and nock child meshes across racks and bundles; keep material slots low; limit visible shaft/head counts in dense clusters; avoid unique material instances for every part.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeBowParts_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeBowParts_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeBowParts_A01/CHILD_ASSET_INTAKE.md`

Future package names, if promoted by later tasks:

- `SM_GIA_BloodAxeBowStringCoil_A01`
- `SM_GIA_BloodAxeBowStringRack_A01`
- `SM_GIA_BloodAxeReplacementLimb_A01`
- `SM_GIA_BloodAxeStaveBlank_A01`
- `SM_GIA_BloodAxeArrowShaftSet_A01`
- `SM_GIA_BloodAxeArrowHeadTray_A01`
- `SM_GIA_BloodAxeWrapBundle_A01`
- `SM_GIA_BloodAxeBowNockParts_A01`
- `SM_GIA_BloodAxeBowRepairPieces_A01`
- `SM_GIA_BloodAxeBowPartsRack_A01`
- `SM_GIA_BloodAxeBowPartsWallRack_A01`
- `SM_GIA_BloodAxeBowWorkbenchCradle_A01`
- `SM_GIA_BloodAxeLimbBundle_A01`
- `SM_GIA_BloodAxeArrowPartsBundle_A01`
- `SM_GIA_BloodAxeBowPartsBundle_A01`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied source concepts, validators, task-board updates, backlog edits, bootstrap edits, or global index entries from this task packet.

## Approval Gates

- Stop before DCC source creation, FBX export, Unreal Content asset creation, material authoring, runtime source changes, startup-scene placement, validator creation, or source-concept copying.
- Stop before defining projectile stats, projectile behavior, combat rules, ammunition counts, arrow damage, hit logic, pickup behavior, loot behavior, inventory behavior, bow draw distance, release timing, reload timing, or animation montage timing.
- Stop if strings, limbs, arrow shafts, heads, wraps, racks, repair pieces, nock parts, and bundle variants collapse into one single mesh assumption.
- Stop if collision becomes dense per-shaft, per-head, per-string, or per-repair-piece complexity instead of simple display collision.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop if the validated Giant scale lock, `SK_GIA_Base_A01` assumptions, or `SM_GIA_BloodAxeLongbow_A01` support relationship changes without a new approval task.
- Stop if trophy, skull, red cloth, shaft count, or tiny repair detail becomes too dense for mid-poly MMO readability.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Static rack/workshop dressing and longbow support purpose is clear.
- Projectile stats, combat rules, projectile behavior, and animation timing are explicitly out of scope.
- Child coverage includes strings, limbs, arrow shafts, arrow heads, wraps, racks, repair pieces, nock parts, and bundle variants.
- Primary silhouettes read as Giant-scale bowyer parts at MMO camera distance.
- Materials use dark wood, sinew, rawhide, scorched leather, blackened iron, dark steel, bone/horn, red cloth, soot, resin, and grime consistently.
- Emissive is absent by default and approval-gated for any future ritual or shamanic variant.
- Tiny fibers, scratches, pitting, stitch marks, wood grain, small rivets, and minor binding detail are assigned to textures or normals instead of geometry.
- Texture maps, material slot targets, triangle budgets, LOD0-LOD3, collision planning, Unreal import planning, folder naming, approval gates, and docs-only guardrails are included.
- The package makes no DCC, FBX, Unreal Content, runtime source, global index, task board, external concept copy, or startup-scene work claim.
