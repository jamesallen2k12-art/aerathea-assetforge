# SM_GIA_BloodAxeDrapedThresholdCloth_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeDrapedThresholdCloth_A01`
- Asset type: Static Mesh prop production package, docs-only
- Task: `AET-MA-20260629-222`
- Parent package: `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- Source child row: `BloodAxeCaveApproachMarkers_A01#RedClothThresholdMarker_Draped_A01`
- Related material policy: `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: planning package only. No source asset, DCC work, FBX export, Unreal asset, material graph, texture asset, material instance, VFX, audio, runtime source, startup placement, cloth simulation, interaction behavior, readable signage, objective cue, material pulse, first implementation target, final cave approval, or final visual approval belongs to this scope.

`SM_GIA_BloodAxeDrapedThresholdCloth_A01` defines a static draped cloth band laid over a low rough stone or slab near a Blood Axe cave approach. The cloth is faded oxide red with soot wear, broad fixed folds, dirty edge darkening, and a heavy settled feel. It is threshold dressing only: a crude hostile Giant sub-faction warning accent, not a flag, route marker, sign, interactable object, objective cue, or animated material state.

The asset should feel old, grounded, and practical. Its read comes from a low stone/slab mass with one broad red cloth band sagging over the front edge. It must stay separate from neutral/civilized Giant culture, which remains tied to skilled highland stonework, hidden cave towns, blue-gray civic masonry, terraces, waterworks, warm hearth identity, restrained civic runes, and master stoneworker craft.

## Gameplay Purpose

The purpose is visual production planning only. The draped cloth helps future cave-edge dressing read as Blood Axe territory through a restrained red threshold beat, while staying static and non-gameplay.

Allowed planning uses:

- Add a low, broad oxide-red threshold accent to cave approach marker compositions.
- Support static threshold readability beside low cairns, collapsed slabs, cave ash bases, and remnant clusters.
- Show Blood Axe raider presence through soot-worn cloth and crude stone use without making the cloth a sign, UI cue, objective cue, or route marker.
- Preserve Giant-scale readability with oversized fixed folds and cloth width suited to 442 cm and 470 cm Giant baselines.
- Provide art, modeling, texture, LOD, collision, and import-planning guardrails without selecting a production target.

Out of scope:

- Cloth simulation, wind animation, dangling physics, flag behavior, interaction behavior, readable signage, objective cue behavior, material pulse, glow state, quest/UI marker behavior, route validation, cave gameplay, nav/pathfinding, encounter trigger behavior, damage/aura behavior, DCC work, FBX export, Unreal Content, runtime source, startup placement, first implementation target selection, final cave approval, final visual approval, VFX, or audio.

## Silhouette Notes

- Primary read: one broad faded oxide-red cloth band draped over a low rough stone, broken slab, or squat stone lip.
- The cloth must rest in a fixed sculpted pose with broad folds, a heavy front sag, and a few large worn tears or uneven edges.
- The support stone/slab should be low, crude, and secondary to the draped red band, but still visible enough to ground the cloth.
- Default `A01` composition should avoid tall posts, banner poles, gate frames, standing-stone pairs, or signboard silhouettes.
- The front edge should read as a draped threshold lip rather than a hanging banner. Keep the lower cloth edge close to the stone/slab and ground plane.
- Use one to three large fold channels, not many thin ripples. The form should read from an MMO camera without cloth simulation.
- Optional anchors may include a heavy rope pinch, rawhide weight, soot-darkened stone notch, or small wedged rock. These must stay subordinate and sparse.
- Torn corners may be large and blunt, but avoid rag fields, dense fray strands, readable symbols, UI arrows, objective icons, or magic glyph panels.
- Future geometry, if separately scoped, should model the main cloth shell, thickened folded edge, broad sag folds, stone/slab support, one large contact crease, and optional rope/rawhide weight.
- Fine cloth weave, soot speckles, ash flecks, mud droplets, small holes, edge fray, rope fibers, chipped stone pitting, lichen, and scratches belong in future textures, normals, AO, roughness, or masks.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Future source, if separately scoped, should be authored in centimeters with 1 Unreal unit = 1 cm.

Visual planning dimensions:

- Low stone/slab support height: 35-95 cm.
- Low stone/slab support width: 120-320 cm.
- Low stone/slab support depth: 70-180 cm.
- Draped cloth band width across support: 95-260 cm.
- Visible cloth drop over front edge: 45-140 cm.
- Cloth thickness: 2-6 cm as a fixed shell or thickened folded edge, not simulated cloth.
- Broad fold depth: 8-24 cm where it affects silhouette.
- Optional rope/rawhide weight diameter: 8-20 cm.
- Total footprint: 140-360 cm wide and 90-220 cm deep depending on slab shape and cloth spread.

The draped cloth should feel large for normal humanoids but low and modest beside Blood Axe Giant-scale cairns and standing stones. It should remain smaller than a banner, gate cloth, cave curtain, standing-stone pair, or cave remnant cluster.

These values are visual planning values only. They are not traversal measurements, collision proof, cave compatibility proof, interaction ranges, objective ranges, nav/pathfinding values, or camera approval metrics.

## Materials and Color Palette

Primary materials:

- Faded oxide-red cloth, dirty maroon canvas, sun-bleached red fabric, soot-darkened lower edges, and ash-dusted folds.
- Rough highland stone, low broken slab, ash-stained field rock, dark cave-edge stone, chipped granite, and soot-streaked stone contact.
- Packed mud, cold ash, charcoal dust, cave grit, dried gray-brown stains, and trampled threshold dirt.
- Optional thick rope, rawhide tie, worn leather strip, or small wedged stone used only as a static weight or contact accent.
- Sparse blackened iron pin, old horn chip, or dull bone token only if a later art pass needs one non-graphic secondary warning beat.

Palette targets:

- Oxide red and faded maroon cloth: `#551311`, `#6B1A16`, `#81251D`, `#98372B`
- Cloth soot and dark wear: `#151718`, `#222527`, `#343635`
- Rough stone: `#242729`, `#3C3D3A`, `#5A5A53`, `#6F6D66`
- Ash and cold dust: `#67645E`, `#827B70`, `#A49B8E`, `#C0B5A3`
- Mud and cave grit: `#241D17`, `#382C22`, `#554332`, `#6F5B45`
- Rope, rawhide, and worn leather: `#4E3925`, `#684F33`, `#8E7048`, `#AF915F`
- Optional blackened iron: `#0F1011`, `#202326`, `#383D3E`

Material restraint:

- No default emissive map.
- No glow, ritual light, shamanic pulse, signal state, torch response, objective highlight, UI highlight, VFX state, audio response, or animated material state.
- Oxide red should remain a controlled Blood Axe accent, not a full red environment wash.
- Soot and ash should age the cloth and stone without making the silhouette muddy or unreadable.
- Avoid neutral/civilized Giant defaults: no refined blue-gray civic masonry, terrace or waterwork language, warm hearth banners, peaceful highland wayfinding, civic mason marks, or restrained blue-rune identity.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeDrapedThresholdCloth_A01` for the world of Aerathea. The design should emphasize a static draped oxide-red cloth band over a low rough stone or broken slab, faded maroon fabric, soot-worn lower edges, broad fixed folds, cold ash, cave grit, packed mud, rough highland stone, optional thick rope or rawhide weight, hostile Blood Axe Giant sub-faction identity, strict separation from neutral/civilized Giant culture, grim cave-approach mood, and the gameplay role of static visual threshold dressing only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh prop concept sheet with front, side, back, and three-quarter views, material swatches, fold callouts, LOD and collision planning notes, and scale markers beside a female 442 cm Giant and a male 470 cm Giant on a clean background. Avoid copying any existing franchise, avoid cloth simulation, avoid wind animation, avoid flag behavior, avoid interaction behavior, avoid readable signage, avoid objective cues, avoid material pulses, avoid quest or UI marker shapes, avoid VFX or audio cues, avoid DCC or Unreal implementation claims, avoid startup placement claims, avoid final visual approval language, avoid selecting a first implementation target, avoid neutral Giant cave-town symbols as Blood Axe default language, avoid magic glow, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly game asset.

## Modeling Notes

This is a docs-only modeling plan. It creates no source folder, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal asset, material instance, texture asset, material graph, validator, runtime source, Blueprint, socket, animation, startup placement, implementation target, cave signoff, or visual signoff.

Future modeling priorities, if separately scoped:

- Build the prop as one static low stone/slab support with one broad draped cloth band.
- Shape the cloth in a fixed pose with broad fold channels, a thickened front edge, one heavy sag, and large blunt tears where they affect silhouette.
- Keep the stone/slab low and chunky with broad chipped planes, simple bevels, and a clear base contact shadow.
- Make the cloth wrap or rest over the stone, not hang freely as a curtain or banner.
- Use optional rope/rawhide or a small wedge stone only as a static weight or contact detail. One large accent is preferable to many small ties.
- Keep the back side simpler but believable, with cloth overlap and stone contact rather than hidden elaborate detail.
- Avoid tall posts, readable sign boards, route arrows, UI icon silhouettes, objective frames, dense fray strands, individual stitch rows, tiny crack carpets, pebble scatter, graphic trophies, or hidden underside detail.

Use textures, normals, AO, roughness, or masks for:

- Cloth weave, edge fray, faded dye breakup, soot speckles, ash flecks, mud droplets, shallow stone pitting, chipped paint edges, lichen flecks, rope fibers, rawhide pores, tiny holes, minor scratches, and small contact stains.

## Texture and Material Notes

Target material strategy for future source work:

- Default material count: 1 shared prop material for cloth, stone/slab, soot, ash, mud, cave grit, and optional rope/rawhide.
- Maximum material count: 2 if a later art pass requires separate cloth and stone/support material families.
- Default texture resolution: 1K BC/N/ORM.
- 2K only if a later close-view cave dressing lane scopes it.
- No default emissive map.

Required future texture names, planning only:

- `T_GIA_BloodAxeDrapedThresholdCloth_A01_BC`
- `T_GIA_BloodAxeDrapedThresholdCloth_A01_N`
- `T_GIA_BloodAxeDrapedThresholdCloth_A01_ORM`

Optional future texture name, separate-scope only:

- `T_GIA_BloodAxeDrapedThresholdCloth_A01_Mask` for controlled soot, ash, mud, faded dye, and edge-wear variation.

Texture guidance:

- Base Color should carry faded maroon/oxide red cloth, soot-dark lower edges, ash dust, mud stains, rough stone values, cave grit, and optional rawhide or rope browns.
- Normal should carry broad fold definition, cloth weave, thickened edge cues, stone pitting, rope fiber direction, rawhide pores, chipped stone edges, and small tear thickness.
- ORM should emphasize occlusion at cloth folds, stone contact, lower drape overlaps, soot pockets, mud buildup, and rope/rawhide contact if present.
- Roughness should stay high across cloth, soot, ash, mud, cave grit, rope, rawhide, and rough stone.
- Metallic should remain near zero except for an optional blackened iron pin if a later art pass keeps it.
- Do not assign unique materials to folds, tears, stains, soot patches, ash flecks, rope loops, stone chips, lichen, mud droplets, or paint marks.

## Triangle Budget

- Target category: small to medium static prop.
- LOD0 target: 900-3k tris.
- LOD0 upper limit: 4k tris only if the slab, cloth shell, broad fixed folds, and one static weight accent all need stronger silhouette support.
- LOD1 target: 450-1.6k tris.
- LOD2 target: 180-700 tris.
- LOD3 target: 70-240 tris.
- Material budget: 1 material target, 2 maximum.
- Texture budget: 1K BC/N/ORM by default; 2K only for separately scoped close-view use.

Suggested LOD0 allocation:

- Main cloth shell, thickened front edge, broad fixed folds, and large torn silhouette: 50-65 percent.
- Low stone/slab support, broad chipped planes, and contact bevels: 25-38 percent.
- Optional rope/rawhide weight, wedge stone, or sparse hard accent: 0-12 percent.

Do not spend geometry on cloth weave, dense fray, tiny holes, soot speckles, ash flecks, mud droplets, individual fibers, small cracks, lichen specks, chipped paint flecks, or minor scratches.

## LOD Plan

All future important static meshes require LOD0, LOD1, LOD2, and LOD3 before any shipping use.

- LOD0: full broad cloth band, fixed fold channels, thickened front edge, low stone/slab support, large torn corners, soot/mud grounding, and optional static weight accent.
- LOD1: 55-70 percent of LOD0; reduce secondary fold cuts, minor edge waviness, small stone bevels, backside overlap detail, and optional accent bevels while preserving the draped red threshold read.
- LOD2: 30-45 percent of LOD0; flatten most folds, merge cloth planes, simplify support stone geometry, remove non-silhouette tears, and keep one strong oxide-red draped mass over a low slab.
- LOD3: 12-25 percent of LOD0; preserve only the broad red cloth band, low dark support mass, and primary front drape silhouette.

Reduction order:

1. Cloth weave, soot speckles, ash flecks, mud droplets, lichen, small scratches, tiny holes, small paint chips, and fine fray.
2. Small cloth tears, minor fold loops, tiny rawhide ends, rope cuts, little stone chips, and non-silhouette notches.
3. Back-facing overlap detail, hidden underside folds, buried support bevels, and minor contact undercuts.
4. Optional blackened iron pin, old horn chip, dull bone token, small wedge stone, or secondary paint smear.
5. Cloth thickness subdivisions, major fold subdivisions, and stone/slab bevel density.
6. Only after small detail is gone, simplify the primary draped cloth outline and low support mass.

Never reduce Giant-scale readability, Blood Axe oxide-red warning read, fixed draped-cloth silhouette, or static threshold readability before removing small detail.

## Collision Notes

Collision is planning only. This package creates no collision proxies, UCX meshes, Unreal collision settings, physics bodies, cloth collision, nav blockers, smart links, gameplay volumes, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, or runtime setup.

Future static collision intent, if separately scoped:

- Default: collision disabled.
- Cloth: no player collision, no camera collision, no cloth collision, and no per-fold or per-tear collision.
- Soot, ash, mud, cave grit, cloth wear, rope fibers, rawhide, small wedge stones, iron pins, horn chips, dull bone tokens, lichen, and surface wear: no individual collision.
- Optional: one very simple static hull for the low stone/slab only if a later environment owner requires basic blocking on that support.
- Optional: one simple non-blocking selection hull around the full prop only if a later editor workflow requires it.

This package makes no claim of collision correctness, cave compatibility, terrain integration, route clearance, player movement validity, camera clearance, objective-zone behavior, interaction behavior, or runtime performance validation.

## Animation Notes

- Baseline asset is static.
- The cloth band, broad folds, stone/slab support, soot wear, mud stains, and optional rope/rawhide weight should be fixed in one readable pose if later source work is separately scoped.
- Static material variation for faded dye, soot, ash, mud, cave grit, and edge wear may be planned only as non-runtime surface variation.
- No cloth simulation, wind animation, vertex sway, banner waving, rope physics, hanging prop sway, physics bodies, destructible tear behavior, burn state, material pulse, glow, particle effect, VFX, audio, Blueprint state, interaction state, quest state, objective state, UI state, damage state, aura state, or gameplay state change.
- Any moving, simulated, glowing, audio-linked, interactive, objective-readable, UI-readable, or gameplay-readable variant needs a separately named package and explicit scope.

## Unreal Import Notes

This section is future guardrail planning only. No Unreal asset, game folder, import script, material instance, texture asset, socket, Blueprint, validator, runtime source, review actor, startup actor, source asset, DCC work, FBX export, cave placement, collision setup, nav setup, trigger setup, objective setup, quest/UI setup, interaction setup, material graph work, VFX, audio, or first implementation target belongs to this package.

Potential future identity after separate scope:

- Asset name: `SM_GIA_BloodAxeDrapedThresholdCloth_A01`
- Asset type: Static Mesh
- Potential future folder: `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/`
- Naming convention: `SM_GIA_BloodAxeDrapedThresholdCloth_A01`, `MI_GIA_BloodAxeDrapedThresholdCloth_A01`, `T_GIA_BloodAxeDrapedThresholdCloth_A01_BC`, `T_GIA_BloodAxeDrapedThresholdCloth_A01_N`, `T_GIA_BloodAxeDrapedThresholdCloth_A01_ORM`
- Pivot: ground center of the low stone/slab footprint for standalone placement.
- Orientation: strongest draped-cloth read faces +X unless a later export task confirms a different project convention.
- Scale: centimeter-authored source at scale 1.0 in a later scoped production lane, matching the female 442 cm and male 470 cm Giant baselines without changing the Giant scale lock.
- Collision type: disabled by default; optional simple low stone/slab hull only under separate scope.
- LOD plan: LOD0-LOD3 required before any shipping use.
- Material slot count: 1 target, 2 maximum.
- Texture list: `T_GIA_BloodAxeDrapedThresholdCloth_A01_BC`, `T_GIA_BloodAxeDrapedThresholdCloth_A01_N`, and `T_GIA_BloodAxeDrapedThresholdCloth_A01_ORM`.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: low triangle count, one broad red draped read, shared Blood Axe cave-approach material language, no default emissive, disabled collision on cloth/detail, and aggressive LOD reduction.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeDrapedThresholdCloth_A01/PRODUCTION_PACKAGE.md`

Future asset naming references, for planning only:

- Static mesh: `SM_GIA_BloodAxeDrapedThresholdCloth_A01`
- Material instance: `MI_GIA_BloodAxeDrapedThresholdCloth_A01`
- Base color: `T_GIA_BloodAxeDrapedThresholdCloth_A01_BC`
- Normal: `T_GIA_BloodAxeDrapedThresholdCloth_A01_N`
- ORM: `T_GIA_BloodAxeDrapedThresholdCloth_A01_ORM`

Related planning references:

- Parent kit: `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachMarkers_A01/`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachMarkers_A01/CHILD_ASSET_INTAKE.md`
- Material discipline: `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01/`
- Sibling cloth marker reference: `docs/assets/props/SM_GIA_BloodAxeRedClothThresholdMarker_A01/`

Do not create or edit source asset folders, DCC files, FBX exports, Unreal game content folders, material graphs, material instances, texture assets, validators, global indexes, backlog docs, task-board docs, bootstrap docs, startup placement, external source concept files, runtime source files, VFX assets, audio assets, or unrelated package files from this task.

## Quality Gate Checklist

- Required universal package headings are present in the requested order.
- Package is docs-only and limited to `docs/assets/props/SM_GIA_BloodAxeDrapedThresholdCloth_A01/PRODUCTION_PACKAGE.md`.
- Asset remains a static draped cloth band over a low stone or slab.
- Cloth read is faded oxide red with soot wear, broad fixed folds, a low settled silhouette, and no simulated cloth requirement.
- Giant scale lock is explicit: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved ranges are females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Material restraint is explicit: faded maroon/oxide red cloth, soot, ash, mud, cave grit, rough stone/slab support, optional rope/rawhide, and no default emissive.
- Primary read is static threshold dressing only, without cloth simulation, wind animation, flag behavior, interaction behavior, readable signage, objective cue, material pulse, quest/UI marker behavior, VFX/audio, DCC work, FBX export, Unreal work, startup placement, or final visual approval.
- No source asset, mesh, material instance, texture asset, validator, runtime source, Blueprint, implementation target, or final approval is claimed.
- No excessive micro-detail, readable text, UI arrows, magic glyphs, neutral Giant civic markers, dense trophy clutter, graphic gore, or glow is required for the asset read.
- Texture plan includes BC, N, and ORM maps with no default emissive map.
- Triangle budgets, material limits, LOD0-LOD3 plan, collision planning limits, animation limits, import planning, folder naming, and stop gates are included.
- Fine cloth weave, fray, rope fibers, rawhide pores, soot speckles, ash flecks, mud droplets, chipped paint, stone pitting, lichen, and small scratches are assigned to textures or normals in future work.
- Future collision remains disabled by default and non-gameplay; no route, movement, cave compatibility, interaction, objective, damage, aura, nav, quest, UI, VFX, audio, cloth simulation, wind animation, material pulse, or readable signage behavior is defined.
