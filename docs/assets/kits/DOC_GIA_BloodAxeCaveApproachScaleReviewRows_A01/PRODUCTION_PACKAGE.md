# DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01`
- Asset type: Documentation-only scale review-row package
- Task: `AET-MA-20260629-226`
- Parent package: `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- Related packages: `KIT_GIA_BloodAxeCaveApproachStandingPair_A01` and `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only non-shipping planning; stop before DCC, FBX, Unreal actor work, startup placement, validator work, capture work, final visual approval, or implementation target selection.

`DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01` defines scale-review rows for Blood Axe cave approach markers. The rows compare low cairns, paired stones, remnant clusters, red cloth markers, and broken slab remnants against locked Giant baselines so future reviewers can judge readable size relationships before any source or engine work exists.

This document is not a shipping asset package. It is a planning package for visual scale discipline only. It does not select a first target, approve source creation, approve scene placement, or provide final visual signoff.

Blood Axe visual language remains a hostile Giant sub-faction identity. It must stay separate from neutral/civilized Giant culture, which remains tied to skilled highland stonework, hidden cave towns, terraces, waterworks, hearth warmth, monumental civic masonry, and restrained blue-gray stone language.

## Gameplay Purpose

The gameplay purpose is scale readability planning only. These review rows help compare marker families beside the locked Giant baselines without defining gameplay, route behavior, encounter behavior, or cave function.

Allowed planning uses:

- Compare cave approach marker sizes against female and male Giant baselines.
- Keep low cairns, paired stones, remnant clusters, red cloth markers, and slab remnants visually Giant-scaled.
- Prevent Blood Axe cave dressing from drifting into neutral/civilized Giant cave-town language.
- Provide a non-shipping reference for later package reviewers to discuss size, silhouette, and material restraint.
- Preserve the static cave-threshold readability established by `KIT_GIA_BloodAxeCaveApproachMarkers_A01`.

Out of scope:

- Cave gameplay, traversal proof, path-width rules, route validation, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, spawn logic, patrol logic, combat cover, damage/aura behavior, VFX/audio, source asset creation, DCC, FBX, Unreal actor work, startup placement, validator creation, capture automation, final visual approval, or implementation target selection.

## Silhouette Notes

Scale rows should use clean row compositions with the Giant baselines shown consistently beside each marker family. Each row should isolate one silhouette problem instead of mixing every marker type into a dense scene.

Row silhouette families:

- Low cairn row: squat, heavy stone piles built from a few large rocks. The row should show low, medium, and high cairn variants without turning them into gates or route markers.
- Paired stone row: asymmetric tall/short standing stones with broad fractured planes and a visual gap. The row should compare visual gaps without implying a doorway, nav gate, objective frame, or traversal lane.
- Remnant cluster row: low mixed groups of partial cairns, old ash bases, cave grit, rope residue, dull horn, dull bone, and broken stone. The row should read as static cave-edge memory rather than encounter setup.
- Red cloth marker row: broad oxide red strips, wraps, knots, and drapes scaled for Giant hands. The row should compare cloth size and mount height without reading as a quest marker, flag animation, or UI cue.
- Slab remnant row: broad broken threshold slabs, split slab pairs, ash-grounded slabs, painted slabs, and sparse chock stones. The row should read as damaged static threshold history rather than route blocking.

Avoid polished monuments, refined civic masonry, blue rune identity, warm neutral settlement cues, readable arrows, readable text, magic glyph panels, dense trophy clutter, graphic gore, and micro-detail that would not survive mid-poly MMO production.

## Scale Notes

Use the Giant scale lock from `SK_GIA_Base_A01`:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- These rows must not alter race scale, skeleton policy, collision capsules, sockets, proportions, or character baselines.

Non-shipping scale row register:

| Row ID | Marker family | Review variants | Scale beside Giant baselines | Planning notes |
| --- | --- | --- | --- | --- |
| `ScaleRow_LowCairns_A01` | Low cairns | 80 cm, 130 cm, and 180 cm tall cairns; 140-360 cm footprints | Show each cairn beside female 442 cm and male 470 cm baselines | Cairns should stay squat and readable as threshold dressing, not gates, blockers, objective markers, or civilized Giant wayfinding. |
| `ScaleRow_PairedStones_A01` | Paired standing stones | Tall/short pair, leaning pair, broken pair; 300-620 cm stone heights; 260 cm, 380 cm, and 560 cm visual gaps | Show the tallest and shortest stones against both Giant baselines | Gaps are visual rhythm only, not traversal clearance, path width, nav space, or cave approval. |
| `ScaleRow_RemnantClusters_A01` | Cave remnant clusters | 300 cm, 650 cm, and 1100 cm footprints with one to three major stone reads | Show footprint blocks and dominant height beats beside both Giant baselines | Clusters should feel old, abandoned, and static without becoming encounter markers, spawn markers, or route devices. |
| `ScaleRow_RedClothMarkers_A01` | Red cloth markers | 80 cm, 160 cm, and 240 cm strips; 20-70 cm widths; low stone wrap, standing-stone wrap, slab drape | Show cloth strips at Giant-readable scale beside both Giant baselines | Cloth is a restrained Blood Axe accent only, not a flag system, UI pointer, objective cue, or animated material state. |
| `ScaleRow_SlabRemnants_A01` | Broken slab remnants | 180-520 cm slab lengths; 35-110 cm thickness; 360-950 cm cluster footprints | Show slab thickness, length, and cluster footprint beside both Giant baselines | Slabs are static visual history only, not route blockers, climb assists, cave compatibility proof, or interaction props. |

All row dimensions are visual planning values only. They are not gameplay measurements, traversal proof, collision correctness claims, encounter spacing, trigger sizes, interaction ranges, camera approval metrics, terrain integration values, or final cave approval metrics.

## Materials and Color Palette

Shared Blood Axe cave approach materials:

- Rough highland stone, dark fractured cave-edge slabs, ash-stained field rock, weathered granite, and soot-blackened recesses.
- Packed earth, trampled mud, cold ash, charcoal dust, cave grit, dry stone dust, muted lichen, and eroded threshold dirt.
- Oxide red cloth, faded maroon wraps, chipped dirty red paint, soot-stained cloth edges, and old red warning swipes used sparingly.
- Rope, rawhide, sinew ties, worn leather, sparse blackened iron, old horn, and dull bone as secondary non-graphic warning accents.

Palette targets:

- Dominant: charcoal gray, dark stone gray, ash gray, cave black, mud brown, weathered slate, and cold granite.
- Faction accent: oxide red, faded maroon, dirty red-brown paint, and soot-stained red cloth.
- Secondary accent: rawhide tan, old horn tan, dull bone ivory, rubbed dark iron, muted lichen green, and dry grass residue.
- Emissive: absent. Glow, signal lights, ritual light, shamanic pulse, torch state, UI highlight, or animated material state is outside this package.

Exclude neutral/civilized Giant culture from the default read: no refined blue-gray civic masonry, terrace or waterwork motifs, warm hearth identity, peaceful highland wayfinding, polished stoneworker craft marks, carved civic ornament, or restrained blue rune language.

## Concept Image Prompt

Create an original stylized fantasy MMORPG documentation board of `DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01` for the world of Aerathea. The design should emphasize non-shipping scale review rows for Blood Axe cave approach markers, low cairns, paired standing stones, cave remnant clusters, red cloth threshold markers, broken slab remnants, rough highland stone, soot-blackened cave-edge slabs, cold ash, trampled mud, cave grit, restrained oxide red cloth, chipped dirty red paint, rope, rawhide, sparse old horn, dull bone, blackened iron, hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and scale comparison beside a female 442 cm Giant and a male 470 cm Giant from `SK_GIA_Base_A01`. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a clean docs-only scale board with row labels, height callouts, footprint callouts, material restraint notes, and stop gates. Avoid copying any existing franchise, avoid cave gameplay diagrams, avoid traversal proof, avoid collision correctness claims, avoid nav/pathfinding diagrams, avoid quest/UI markers, avoid encounter triggers, avoid objective markers, avoid interaction behavior, avoid readable route signage, avoid magic glow, avoid DCC claims, avoid FBX claims, avoid Unreal claims, avoid startup placement, avoid validator claims, avoid capture claims, avoid final approval language, avoid implementation target language, avoid neutral Giant cave-town architecture as Blood Axe default language, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly game assets.

## Modeling Notes

This package stops at documentation. It does not contain source geometry instructions beyond scale-row planning.

If a later approved lane needs a visual board, preserve these documentation rules:

- Use simple row layout, shared baselines, and clear centimeter labels.
- Keep each row readable from left to right: Giant baselines first, then low/small variant, median variant, and large variant.
- Keep marker families separate so cairns, paired stones, remnant clusters, red cloth, and slab remnants can be reviewed independently.
- Use few large forms for scale comparison instead of dense pebble fields, tiny crack carpets, rope-fiber geometry, cloth-fiber geometry, or trophy clutter.
- Treat red cloth and chipped red paint as restrained faction accents, not the main silhouette.
- Keep Blood Axe hostility in rough stone, soot, ash, mud, crude red accents, and sparse warning materials rather than neutral/civilized Giant craft language.

Stop before Blender files, mesh creation, sculpting, retopology, UVs, baking, proof renders, LOD source, collision proxy work, FBX export, Unreal actor work, validator work, runtime work, startup placement, final visual approval, or implementation target selection.

## Texture and Material Notes

This package creates no textures, materials, material instances, texture atlases, masks, or material graphs.

Texture planning discipline for later child packages:

- Use Base Color / Albedo, Normal, and packed Occlusion/Roughness/Metallic only if a separate asset package reaches source production.
- Keep Emissive out of the baseline cave approach scale rows.
- Use textures and normals for fine cracks, stone pitting, soot speckles, ash flecks, cloth weave, rope fibers, mud streaks, chipped paint, lichen specks, horn rings, bone pores, and small scratches.
- Do not assign unique materials per stone, cloth strip, rope tie, ash patch, horn piece, bone token, paint mark, crack, or lichen spot.
- Keep scale rows visually neutral enough to judge size, with material swatches acting as reminders rather than final color approval.

Suggested documentation-only swatch groups:

- `Stone_Soot_Ash`
- `Mud_CaveGrit_Lichen`
- `OxideRed_Cloth_Paint`
- `Rawhide_Rope_Leather`
- `BlackenedIron_Horn_DullBone`

## Triangle Budget

This docs-only package has no triangle budget because it creates no mesh.

Reference-only future planning targets from related packages:

- Low cairn reference: 800-3.5k tris for a single future static cairn.
- Paired standing-stone reference: 5k-13k tris for future pair variants depending on cloth and accent complexity.
- Remnant cluster reference: 5k-18k tris for a future mixed cave remnant cluster.
- Red cloth marker reference: 300-1.5k tris for a future static cloth marker if separately scoped.
- Broken slab remnant reference: 4k-12k tris for a future primary broken slab cluster.
- Non-shipping review row reference: 0 shipping tris. Any later board visualization remains separate planning scope.

Spend future geometry on primary stone mass, broad slab thickness, paired-stone height contrast, major cloth silhouettes, large knots, sparse chock stones, and ash/mud grounding forms. Do not spend geometry on tiny cracks, soot speckles, ash grains, cloth weave, rope fibers, paint chips, lichen, mud flecks, or small scratches.

## LOD Plan

This package creates no LODs. Scale rows are documentation only.

If later child packages use this document, preserve the established LOD discipline:

- LOD0 should preserve the full primary silhouette and readable Giant-scale relationship.
- LOD1 should reduce small bevels, secondary chips, cloth edge cuts, lashing subdivisions, minor base cuts, and hidden backside detail.
- LOD2 should simplify stones into larger planes, merge or remove smaller base pieces, flatten cloth folds, and keep only the strongest red faction beat.
- LOD3 should preserve the main cairn, paired-stone, remnant-cluster, cloth-marker, or slab-remnant read with minimal detail.

Reduction order:

1. Tiny cracks, soot speckles, ash flecks, lichen specks, paint chips, cloth weave, rope fibers, grit, pores, and minor scratches.
2. Small lashings, secondary cloth tears, small stone wedges, small horn chips, minor iron nicks, and tiny knots.
3. Back-facing pieces, hidden underside bevels, buried base cuts, and non-visible mud or ash undercuts.
4. Secondary marker tokens, duplicate foot stones, small cloth holes, minor slab scars, and optional review-row helper detail.
5. Stone bevel density, cloth fold geometry, ash/mud ridge geometry, and secondary base-plane subdivisions.
6. Only after small detail is removed, simplify the primary scale-read silhouette.

Never reduce the female 442 cm and male 470 cm Giant baseline read, Blood Axe red warning accent, static cave-threshold readability, or main marker-family silhouette before removing small detail.

## Collision Notes

This package creates no collision plan beyond a documentation stop gate. Review rows are non-shipping and have no collision.

Future static collision discipline from related packages:

- Low cairns: collision disabled by default, with only simple primitive blocking if a separate owner requires it.
- Paired standing stones: simple boxes or low-count convex hulls around major stone masses only if separately scoped.
- Remnant clusters: disabled by default or broad hulls around the largest static stones only if separately scoped.
- Red cloth markers: collision disabled for cloth, rope, small stakes, paint, and loose accents.
- Broken slab remnants: disabled by default for dressing use, with simple hulls around major slab bodies only if separately scoped.
- Scale rows: collision disabled.

No route blocker, traversal clearance, pathing validity, player navigation, combat cover, camera clearance, terrain integration, cave compatibility, collision correctness, or runtime performance validation is claimed here.

## Animation Notes

Baseline scale rows are static documentation.

Allowed at planning level:

- Static row labels, static scale bars, static Giant baselines, static marker silhouettes, static material swatches, and static stop-gate notes.
- Static variation notes for stone value, soot, ash, mud, cave grit, cloth age, red paint wear, lichen, horn, bone, and blackened iron.

Not approved here:

- Cloth simulation, wind sway, dangling physics, destructible collapse, moving slabs, puzzle state, gate opening, material pulse, particle effects, glow, torch state, smoke, audio cue, Blueprint state, interaction state, objective state, damage state, aura state, gameplay state change, startup placement, final visual approval, or implementation target selection.

Any moving, glowing, interactive, objective-readable, gameplay-readable, damaging, audio-driven, route-affecting, or shipping version must be split into a separately named package.

## Unreal Import Notes

Not applicable for this docs-only package. This section exists only to satisfy the universal package shape and to define the stop gate.

No Unreal actor work, game content folder, import script, material instance, texture asset, socket, Blueprint, runtime source, review actor, startup actor, source asset, FBX export, scene placement, collision setup, nav setup, trigger setup, objective setup, quest/UI setup, interaction setup, VFX/audio setup, validator work, capture work, final visual approval, or implementation target selection belongs to this package.

Potential future documentation identity only:

- Asset name: `DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01`
- Asset type: docs-only scale review-row package
- Game asset status: none
- Pivot guidance: none
- Orientation guidance: row reading direction only if a later documentation board needs it
- Scale guidance: use female 442 cm and male 470 cm Giant baselines without changing `SK_GIA_Base_A01`
- Collision: none
- LODs: none
- Material slots: none
- Texture list: none
- Sockets: none
- Animation list: none
- Blueprint behavior: none
- Performance notes: documentation only; preserve low material counts, disabled collision on detail, and aggressive LOD expectations in later child packages.

## Folder and Naming Recommendation

Docs:

- `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01/PRODUCTION_PACKAGE.md`

Review-row identifiers:

- `ScaleRow_LowCairns_A01`
- `ScaleRow_PairedStones_A01`
- `ScaleRow_RemnantClusters_A01`
- `ScaleRow_RedClothMarkers_A01`
- `ScaleRow_SlabRemnants_A01`

Related source-of-truth packages:

- `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- `KIT_GIA_BloodAxeCaveApproachStandingPair_A01`
- `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01`
- `SK_GIA_Base_A01` for Giant scale lock

Do not create source asset folders, DCC files, FBX exports, game content folders, material instances, texture assets, validators, global index edits, backlog edits, task-board edits, bootstrap edits, startup placement, external source concept copies, runtime files, VFX/audio assets, or unrelated package files from this task.

## Quality Gate Checklist

- Required universal package headings are present and adapted to docs-only scale-row planning.
- Package is limited to `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01/PRODUCTION_PACKAGE.md`.
- Scale rows are non-shipping and compare low cairns, paired stones, remnant clusters, red cloth markers, and slab remnants beside Giant baselines.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Approved Giant ranges are explicit: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Neutral/civilized Giant culture remains separate: hidden highland settlements, skilled stonework, cave-town terraces, waterworks, hearth warmth, monumental civic masonry, and restrained blue-gray stone language.
- Cave approach markers remain static threshold readability planning only.
- No cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI marker, encounter trigger, objective marker, readable signage, interaction behavior, VFX/audio, DCC, FBX, Unreal actor work, source asset creation, startup placement, validator work, capture work, final visual approval, or implementation target selection is defined.
- No mesh, texture, material instance, material graph, source folder, game asset, runtime source, Blueprint, socket, animation, VFX/audio asset, external source concept file, global index edit, backlog edit, task-board edit, or bootstrap edit is created.
- Materials use rough highland stone, soot, ash, trampled mud, cave grit, oxide red cloth, chipped red paint, rope, rawhide, sparse blackened iron, old horn, and dull bone without default emissive.
- Silhouette reads through row-separated marker families rather than UI signage, route devices, polished monuments, or gameplay markers.
- Fine cracks, soot speckles, ash flecks, stone pitting, cloth weave, rope fibers, paint chips, lichen, mud streaks, horn rings, bone pores, grit, and small scratches remain texture or normal detail in later packages.
- Triangle budget, LOD plan, collision limits, animation limits, folder naming, import stop gates, and quality gates are included without claiming shipping readiness.
