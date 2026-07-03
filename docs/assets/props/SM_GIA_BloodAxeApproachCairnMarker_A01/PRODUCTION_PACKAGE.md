## Art Direction Summary

`SM_GIA_BloodAxeApproachCairnMarker_A01` is a crude Blood Axe approach cairn used as hostile Giant sub-faction dressing along the stronghold route. It should read as an improvised route-edge warning beat: heavy ash-stained stones stacked by force, oxide red cloth strips tied between upper stones, and blackened dirt packed into the base.

The Blood Axe Tribe language is hostile raider language only and must stay separate from neutral/civilized Giant culture. This asset must not use civilized Giant cave-town cues, blue-gray civic masonry, terraces, waterworks, warm hearth symbolism, restrained blue runes, refined stoneworker craft, or neutral highland settlement identity. It should feel rough, threatening, and practical without graphic gore or excessive trophy clutter.

## Gameplay Purpose

This is a visual approach-rhythm prop only. It helps the player read that the route is entering Blood Axe-controlled ground by repeating crude cairns, torn cloth, ash, and route-edge massing at MMO camera distance.

It does not define readable text, waypoint logic, trail-marker gameplay, objective logic, quest/UI symbols, interaction behavior, loot, pickup behavior, damage behavior, aura behavior, nav/pathfinding, patrol routing, encounter scripting, source concept embedding, DCC work, FBX export, Unreal Content import, startup placement, final visual approval, final stronghold approval, or first implementation target selection.

## Silhouette Notes

- Primary read: squat, uneven stacked-stone wedge with a heavier Giant-scale base and a broken peak leaning slightly toward the route.
- Secondary read: two or three tied cloth strips caught between upper stones, hanging low enough to break the rock mass but not becoming banner gameplay language.
- Tertiary read: loose foot stones, ash smears, soot-darkened chips, and compact dirt packed around the bottom.
- Keep stones large and readable. Avoid pebble noise, tiny stacked fragments, repeated skull motifs, carved warning glyphs, arrows, symbols, or UI-like marks.
- The cairn should look built quickly by very large hands: asymmetrical, blunt, compressed, and weighty rather than balanced, sacred, or civic.
- Preserve a clear silhouette from front, three-quarter, and side views so it works when placed along cliff shelf edges or beside rough palisade returns.

## Scale Notes

Use the validated Giant scale lock from `SK_GIA_Base_A01`: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", with approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

Target asset scale:

- Approximate height: 180-260 cm, depending on placement variant.
- Approximate base width: 160-240 cm.
- Approximate depth: 100-180 cm.
- Cloth-strip drop: 60-120 cm, scaled as Giant-tied material rather than small-folk ribbons.

The cairn should be large enough to read as a Blood Axe route-edge marker beside a 470 cm male Giant, but small enough to remain a repeated approach prop instead of a monument, gate, shrine, objective marker, or review scale rod.

## Materials and Color Palette

- Ash-stained mountain stone: dark gray, charcoal, soot black, muted warm gray chips, and dirty tan exposed breaks.
- Packed earth and ash: desaturated brown, charcoal dust, blackened foot smears, and dull gray ash deposits.
- Oxide red cloth: torn, sun-faded, soot-smudged red strips with frayed ends, used sparingly as the Blood Axe route rhythm.
- Optional binding: rough hide cord or dark fiber lashings, kept thick and readable.
- No emissive material, no active flame, no magic glow, no readable ink, no bright UI color, and no polished neutral Giant stoneworker finish.
- Non-graphic discipline: avoid blood pools, fresh gore, body parts, explicit trophy content, or repeated small horror ornaments. Threat should come from scale, ash, rough stone, and hostile red cloth.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeApproachCairnMarker_A01` for the world of Aerathea. The design should emphasize a squat uneven Giant-scale cairn silhouette, crude stacked ash-stained mountain stones, tied oxide red cloth strips, soot-black packed earth, hostile Blood Axe raider identity, grim route-edge warning mood, and visual approach-rhythm role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive accents, and MMO-friendly production design. Present it as a static mesh concept sheet with front, side, and three-quarter views on a clean neutral background plus a small scale inset against the validated Giant baselines of female 442 cm / 14'6" and male 470 cm / 15'5". Avoid copying any existing franchise, avoid readable text, avoid waypoint icons, avoid objective symbols, avoid graphic gore, avoid source concept embedding, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

- Build as a static mesh composed of 6-10 large stone forms, not many tiny pebbles.
- Model the main stones as chunky low-to-mid-poly forms with beveled, chipped silhouettes and uneven contact points.
- Model cloth strips as simple thick planes or thin folded ribbons with enough geometry to hold ragged hanging shapes. Keep cloth fixed; no cloth simulation requirement.
- Model only major tears and folds in the cloth. Handle weave, soot, fray, and small holes through texture and normal detail.
- Add a small packed-earth base or embedded foot stones only if needed to ground the silhouette. Do not create terrain blending, walkable shelf geometry, or route collision.
- Do not include carved words, directional arrows, quest marks, readable glyphs, UI-like icons, or numbered markers.
- Keep the asset modular enough to rotate and reuse along cliff shelves without looking like a precise waypoint chain.

## Texture and Material Notes

- Recommended material slots: 1 shared atlas for stone, ash, packed earth, cloth, and optional bindings.
- Texture set: 1K for standard use; 2K only if later promoted to close-up hero dressing.
- Required maps: `Base Color`, `Normal`, and packed `ORM`.
- Ambient occlusion should strengthen stone contact shadows, lower base dirt, cloth overlap, and ash deposits.
- Roughness should remain high across stone, ash, and cloth. Metallic should remain black/unused.
- No emissive map is required. Do not add glowing runes, lamps, fire channels, magical trail marks, or UI-like highlight masks.
- Color variation should come from large hand-painted stone planes, soot gradients, and oxide red cloth rhythm rather than many tiny decals.

## Triangle Budget

- Target category: small-to-medium static prop.
- LOD0: 1.5k-3.5k tris.
- LOD1: 800-1.8k tris.
- LOD2: 300-700 tris.
- LOD3: 80-200 tris or simplified impostor-quality silhouette if used only at distance.
- Material budget: 1 material slot.
- Texture budget: 1K BC/N/ORM set by default.

## LOD Plan

- LOD0: full stone stack silhouette, major chipped edges, cloth strips with readable bends, and grounded ash base.
- LOD1: reduce stone edge loops, simplify cloth cuts, remove small foot stones, and bake minor chips into normal detail.
- LOD2: merge small stone forms into broader blocks, reduce cloth to one or two simplified hanging shapes, and remove minor underside detail.
- LOD3: preserve only the cairn wedge, top lean, and oxide red cloth color beat. Do not destroy the primary stacked-stone silhouette first.
- Reduction order: tiny chips, cloth fray cuts, foot stones, underside contact shapes, small binding details, secondary stone edge cuts.

## Collision Notes

- Future collision recommendation: simple collision only, using one low convex hull around the cairn mass plus optional simple cloth-exclusion if cloth hangs outside the hull.
- Collision should support basic blocking only if a future placement owner requests it. It must not claim nav/pathfinding behavior, route blocking correctness, traversal validation, cover behavior, damage volume, pickup behavior, objective behavior, or interaction behavior.
- No collision proxy is created by this package.
- Keep player and camera readability in mind, but do not define final collision correctness or startup-scene placement.

## Animation Notes

- Static mesh only.
- No skeletal rig, cloth simulation, wind animation, physics sway, destruction, collapse, interaction state, material pulse, VFX, audio, or gameplay state change.
- Cloth strips should be modeled in a fixed readable pose suitable for multiple rotations along the approach.

## Unreal Import Notes

- Asset name: `SM_GIA_BloodAxeApproachCairnMarker_A01`.
- Asset type: Static Mesh planning package.
- Recommended future folder path: `Content/Aerathea/Props/Giants/BloodAxe/StrongholdApproach/CairnMarkers/`.
- Pivot: ground center at the base footprint, with forward axis facing the strongest readable presentation side.
- Scale: authored in centimeters; match the target scale notes and validated Giant baselines without changing `SK_GIA_Base_A01`.
- Collision type: future simple collision only if requested by an implementation task.
- LODs: LOD0-LOD3 required for future implementation.
- Material slots: 1.
- Texture list: `T_GIA_BloodAxeApproachCairnMarker_A01_BC`, `T_GIA_BloodAxeApproachCairnMarker_A01_N`, `T_GIA_BloodAxeApproachCairnMarker_A01_ORM`.
- Material instance recommendation: `MI_GIA_BloodAxeApproachCairnMarker_A01`.
- Sockets: none.
- This package does not create Unreal assets, import scripts, material instances, validators, Blueprint behavior, source assets, startup placement, final visual approval, or first implementation selection.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeApproachCairnMarker_A01/PRODUCTION_PACKAGE.md`

Future source and game asset names, for planning only:

- Static mesh: `SM_GIA_BloodAxeApproachCairnMarker_A01`
- Material instance: `MI_GIA_BloodAxeApproachCairnMarker_A01`
- Base color: `T_GIA_BloodAxeApproachCairnMarker_A01_BC`
- Normal: `T_GIA_BloodAxeApproachCairnMarker_A01_N`
- ORM: `T_GIA_BloodAxeApproachCairnMarker_A01_ORM`

No source folder, DCC file, FBX, Unreal Content path, external source concept copy, task-board change, global index update, backlog update, bootstrap update, approval queue update, or runtime source file is created by this docs-only task.

## Quality Gate Checklist

- Universal 15-section production package is present with unnumbered headings.
- Asset remains docs-only and modifies no files outside this package path.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Blood Axe is defined as a hostile Giant sub-faction only and does not overwrite neutral/civilized Giant culture.
- Visual focus stays on crude cairns, tied cloth strips, ash-stained stones, route-edge warning beats, scale readability, and non-graphic material discipline.
- No readable text, waypoint logic, trail-marker gameplay, objective logic, quest/UI symbol, source concept embedding, source concept movement, DCC source, FBX export, Unreal Content import, startup placement, final visual approval, final stronghold approval, or first implementation target selection is claimed.
- No nav/pathfinding, traversal proof, encounter scripting, patrol route, AI space, damage/aura behavior, pickup, loot, crafting, economy, resource, destructible, VFX, audio, or interaction behavior is defined.
- Materials are MMO-safe: one atlas, high roughness, no metallic use, no emissive, no magic glow, no polished civic Giant finish.
- LOD0-LOD3, triangle budgets, texture maps, collision notes, animation notes, folder naming, and Unreal import planning notes are included without performing implementation work.
- Silhouette remains readable from MMO camera distance and does not depend on excessive micro-detail, graphic content, or UI-like color/signage.
