# SM_GIA_BloodAxeRedClothThresholdMarker_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeRedClothThresholdMarker_A01`
- Asset type: Static Mesh prop production package, docs-only
- Task: `AET-MA-20260629-213`
- Parent package: `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- Source child row: `BloodAxeCaveApproachMarkers_A01#RedClothThresholdMarker_Tied_A01`
- Related material policy: `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: planning package only. No source asset, DCC work, FBX export, Unreal asset, material graph, texture asset, material instance, VFX, audio, runtime source, startup placement, cloth simulation, wind animation, first implementation target, cave signoff, or final visual signoff is created or claimed.

`SM_GIA_BloodAxeRedClothThresholdMarker_A01` defines a broad static oxide-red cloth threshold marker tied to a rough stone, short stake, or rope binding near a Blood Axe cave approach. It is a hostile Giant sub-faction accent only: a dirty red warning beat that helps future cave-edge dressing read as Blood Axe territory without becoming a flag, UI marker, quest pointer, objective marker, or animated signal.

The asset should feel crude, old, and practical: faded maroon cloth, soot, mud, rawhide, rope, and a simple support form. It must stay separate from neutral/civilized Giant culture, which remains tied to hidden highland settlements, skilled stonework, blue-gray civic masonry, terraces, waterworks, warm hearth light, restrained civic runes, and master stoneworker identity.

## Gameplay Purpose

The purpose is visual production planning only. The marker supports static threshold readability for Blood Axe cave approaches and abandoned shelter edges without defining route behavior, interaction, objectives, UI, VFX, audio, or final cave approval.

Allowed planning uses:

- Add a restrained oxide-red Blood Axe accent beside low threshold cairns, paired standing stones, remnant clusters, or cave-edge ash bases.
- Give future environment dressing a readable hostile threshold color beat at Giant scale.
- Show cloth tied by Giant hands through thick rope, rawhide, short stakes, or stone wrapping.
- Preserve separation between Blood Axe raider language and neutral/civilized Giant culture.
- Provide art, modeling, texture, LOD, collision, and import-planning guidance without creating implementation evidence.

Out of scope:

- Not approved here: flag animation, cloth simulation, wind animation, dangling physics, UI marker behavior, quest pointer behavior, objective marker behavior, VFX, audio, material graph authoring, material-state animation, interaction prompts, readable signage, cave gameplay, route validation, nav/pathfinding, encounter triggers, damage/aura behavior, DCC source, FBX export, Unreal Content, runtime source, startup placement, first implementation target selection, final cave signoff, or final visual signoff.

## Silhouette Notes

- Primary read: one broad torn cloth strip or wrap in faded oxide red, tied to a rough stone, short stake, or heavy rope binding.
- The cloth should read as a static threshold accent, not a waving banner, route arrow, map pin, quest icon, objective frame, or UI symbol.
- Default `A01` composition should use one main cloth shape with an obvious knot, wrap, or tied-over-stone anchor. Keep the form broad enough to read from MMO camera distance.
- Support options may include a squat stone nub, a short scorched stake, a buried wedge stone, or a rope loop around an existing marker composition. The support should stay secondary to the cloth.
- Cloth edges should have a few large tears, frayed corners, and heavy sag folds sculpted as fixed shapes if a later task approves source work.
- Rope and rawhide should be thick, sparse, and oversized for Giant hands. One or two big wraps are preferable to many thin bands.
- Soot, mud, and ash should ground the lower edge and tie point without turning the asset into a full ash base or route marker.
- Optional chipped dark paint or a broad hand-smeared slash may appear on the cloth, but it must avoid readable text, modern iconography, UI arrows, quest symbols, objective symbols, or magic glyph panels.
- Model only large visible forms if future source work is separately approved: main cloth shell, broad tears, top fold or knot, thick rope/rawhide wrap, short stake, large stone anchor, and major contact folds.
- Keep cloth weave, tiny fray threads, rope fibers, soot speckles, mud flecks, chipped paint edges, small holes, and scratches in future textures, normals, AO, or masks.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Future source, if separately approved, should be authored in centimeters with 1 Unreal unit = 1 cm.

Visual planning dimensions:

- Broad cloth length: 110-260 cm.
- Broad cloth width: 35-95 cm.
- Cloth thickness: 2-5 cm as a fixed shaped shell or thickened folded edge, not a simulated cloth surface.
- Short stake height: 70-180 cm if used as the support.
- Stone anchor height: 45-140 cm if used as the support.
- Rope or rawhide wrap diameter: 8-22 cm, scaled for Giant-tied material.
- Main knot or tied bundle: 22-55 cm across.
- Total footprint: 80-220 cm wide and 50-160 cm deep depending on stone, stake, or rope-binding variant.
- Placement height on a standing stone or cave marker, if referenced later: usually 150-340 cm above ground as a visual cloth tie, not a gameplay measurement.

The marker should feel oversized for normal humanoids and believable beside the 442 cm female and 470 cm male Giant baselines. It should remain smaller than a gate drape, banner pole, standing-stone pair, or full cave remnant cluster.

## Materials and Color Palette

Primary materials:

- Faded oxide-red cloth, dirty maroon canvas, sun-bleached red strips, and soot-darkened cloth edges.
- Rough highland stone, ash-stained field rock, cave-edge slab fragments, or a short scorched stake as the anchor.
- Thick rope, rawhide ties, sinew wraps, worn leather strips, and smoke-stained binding.
- Packed mud, cold ash, soot, charcoal dust, cave grit, and dried brown-gray stains.
- Sparse blackened iron pin, dull horn chip, or dull bone token only if needed as a secondary non-graphic warning beat.

Palette targets:

- Oxide red and faded maroon cloth: `#5A1412`, `#711B17`, `#84261E`, `#9C3A2D`
- Cloth shadow and soot: `#17191A`, `#242729`, `#3C3D3A`
- Mud and packed earth: `#2A2119`, `#403126`, `#5C4938`, `#75624E`
- Ash and cold dust: `#6F6D66`, `#8A867B`, `#ADA698`
- Rope, rawhide, and worn leather: `#5B442B`, `#745C3C`, `#9A7A4E`, `#B09361`
- Rough stone: `#242729`, `#3C3D3A`, `#5A5A53`, `#6F6D66`
- Optional blackened iron: `#101113`, `#222529`, `#3A3F41`

Material restraint:

- No default emissive is approved.
- No glow, ritual light, shamanic pulse, signal state, torch response, objective highlight, UI highlight, VFX state, or animated material state belongs to this baseline.
- The red cloth should be a controlled accent, not a full red environment wash.
- Avoid neutral/civilized Giant materials as the default read: no refined blue-gray civic masonry, terrace/waterwork symbols, warm hearth cloth, peaceful highland wayfinding, clean cave-town banners, civic mason marks, or restrained blue rune language.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeRedClothThresholdMarker_A01` for the world of Aerathea. The design should emphasize a broad static oxide-red cloth threshold marker tied to a rough stone, short scorched stake, or heavy rope binding, faded maroon fabric, soot-dark cloth edges, mud stains, cold ash, thick rawhide and rope wraps, a crude Giant-tied knot, hostile Blood Axe Giant sub-faction identity, strict separation from neutral/civilized Giant culture, grim cave-approach mood, and the gameplay role of static visual threshold dressing only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh prop concept sheet with front, side, back, and three-quarter views, stone/stake/rope-binding variant callouts, material swatches, LOD and collision planning notes, and scale markers beside a female 442 cm Giant and a male 470 cm Giant on a clean background. Avoid copying any existing franchise, avoid flag animation, avoid cloth simulation, avoid wind animation, avoid quest pointers, avoid objective markers, avoid UI marker shapes, avoid VFX or audio cues, avoid material graph diagrams, avoid DCC or Unreal implementation claims, avoid readable text, avoid neutral Giant cave-town symbols as Blood Axe default language, avoid magic glow, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly game asset.

## Modeling Notes

This is a docs-only modeling plan. No source folder, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal asset, material instance, texture asset, material graph, validator, runtime source, Blueprint, socket, animation, startup placement, implementation target, cave signoff, or final visual signoff is created or authorized.

Future modeling priorities, if separately approved:

- Build the marker as a single static prop composition with one broad red cloth read and one simple attachment method.
- Provide three compatible silhouette options for later art review: cloth tied around a rough low stone, cloth fixed to a short stake, or cloth wrapped through a heavy rope binding.
- Keep the default `A01` read simple: one main cloth shape, one knot or wrap, one anchor support, and optional low mud/ash contact.
- Shape major folds, sag, large tears, and thickened cloth edges as fixed geometry only if they affect distance readability.
- Make rope and rawhide wraps thick enough to read as Giant-scale ties; avoid many thin loops.
- Keep the stone or stake anchor chunky, irregular, and secondary. It should not become a standing-stone package, gate post, banner pole, or navigation marker.
- Back side should be simpler but readable, with believable tie pressure, cloth overlap, and soot/mud wear.
- Optional blackened iron pin, old horn chip, or dull bone token should remain sparse and removable from the design.
- Avoid modeled readable symbols, route arrows, tiny crack carpets, cloth fibers, rope fibers, individual stitch rows, many small holes, dense pebble scatter, graphic trophies, or hidden underside detail.

Use textures, normals, AO, roughness, or masks for:

- Cloth weave, fine fray, faded dye breakup, small punctures, soot speckles, ash flecks, mud droplets, rope fibers, rawhide pores, stone pitting, chipped paint edges, lichen flecks, small scratches, and minor dents.

## Texture and Material Notes

Target material strategy for future source work:

- Default material count: 1 shared prop material for cloth, rope/rawhide, stone/stake, soot, mud, and ash.
- Maximum material count: 2 if a later art pass requires a separate cloth material and a shared stone/rope/support material.
- Default texture resolution: 1K BC/N/ORM.
- 2K is acceptable only if a later task promotes the marker to close-view hero cave dressing.
- No default emissive map.

Required future texture names, planning only:

- `T_GIA_BloodAxeRedClothThresholdMarker_A01_BC`
- `T_GIA_BloodAxeRedClothThresholdMarker_A01_N`
- `T_GIA_BloodAxeRedClothThresholdMarker_A01_ORM`

Optional future texture name, approval-gated only:

- `T_GIA_BloodAxeRedClothThresholdMarker_A01_Mask` for controlled soot, mud, faded dye, edge wear, or cloth-age variation if a later material task approves it.

Texture guidance:

- Base Color should carry faded maroon/oxide red cloth, soot-dark lower edges, mud stains, ash dust, rawhide browns, rope tans, and rough stone or scorched stake values.
- Normal should carry cloth weave, shallow folds, rope fiber, rawhide pores, stone pitting, chipped paint edges, and small tear thickness.
- ORM should emphasize occlusion at knots, wrapped cloth overlaps, rope contacts, stone/stake contact, lower fold creases, and mud/ash buildup.
- Roughness should stay high across cloth, soot, mud, ash, rope, rawhide, stone, and scorched wood.
- Metallic should remain near zero except for a rare blackened iron pin or clamp if that optional accent is later retained.
- Do not assign unique materials to individual tears, knots, stains, rope loops, stone chips, ash flecks, paint marks, or support variants.

## Triangle Budget

- Target category: small to medium static prop.
- LOD0 target: 700-2.5k tris.
- LOD0 upper limit: 3.5k tris only if the marker includes a broad cloth shell, stone anchor, short stake option, and large rope knot.
- LOD1 target: 350-1.3k tris.
- LOD2 target: 150-550 tris.
- LOD3 target: 50-180 tris.
- Material budget: 1 material target, 2 maximum.
- Texture budget: 1K BC/N/ORM by default; 2K only for a separately approved close-view use.

Suggested LOD0 allocation:

- Main cloth shell, thickened edges, broad folds, and large torn silhouette: 45-60 percent.
- Knot, rope, rawhide, and wrapped binding: 18-28 percent.
- Stone anchor, short stake, or simple support form: 15-25 percent.
- Optional iron, horn, bone, or painted-shape accent: 0-7 percent.

Do not spend geometry on cloth weave, tiny fray fibers, rope fibers, stitch rows, small holes, soot speckles, ash flecks, mud droplets, small cracks, lichen, paint chips, or minor scratches.

## LOD Plan

All future important static meshes require LOD0, LOD1, LOD2, and LOD3 before any shipping use.

- LOD0: full broad cloth silhouette, large fixed folds, main torn edges, knot/wrap read, stone/stake/rope-binding support, soot/mud grounding, and optional sparse accent.
- LOD1: 55-70 percent of LOD0; reduce secondary folds, minor edge cuts, small knot bevels, backside overlap detail, and support bevels while preserving the cloth threshold read.
- LOD2: 30-45 percent of LOD0; flatten most folds, merge cloth planes, simplify the knot, reduce support geometry, and keep one strong oxide-red silhouette.
- LOD3: 12-25 percent of LOD0; preserve only the red cloth mass, rough attachment block, and broad anchor silhouette.

Reduction order:

1. Tiny fray cuts, stitch holes, cloth weave, soot speckles, ash flecks, mud droplets, paint chips, small scratches, lichen, and minor pitting.
2. Small cloth tears, minor fold loops, little rope cuts, small rawhide ends, tiny knots, and non-silhouette chips.
3. Back-facing overlap detail, hidden underside folds, small support bevels, and buried mud undercuts.
4. Optional iron pin, horn chip, dull bone token, or secondary painted smear.
5. Major knot subdivisions, cloth thickness subdivisions, and stone or stake bevel density.
6. Only after small detail is removed, simplify the primary red cloth outline and the main attachment read.

Never reduce Giant-scale readability, Blood Axe oxide-red warning read, or the static threshold-marker silhouette before removing small detail.

## Collision Notes

Collision is planning only. Do not create collision proxies, UCX meshes, Unreal collision settings, physics bodies, cloth collision, nav blockers, smart links, gameplay volumes, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, or runtime setup from this package.

Future static collision intent, if separately approved:

- Default: collision disabled.
- Cloth: no player collision, no camera collision, no cloth collision, and no per-tear collision.
- Rope, rawhide, knots, small stakes, iron pins, horn chips, bone tokens, mud, ash, soot, paint, and surface wear: no individual collision.
- Optional: one simple non-blocking selection hull around the full prop only if later editor workflow needs it.
- Optional: one very simple static hull for a stone anchor only if a later environment owner explicitly requires basic blocking on the support stone.

This package makes no claim of collision correctness, cave compatibility, terrain integration, route clearance, player movement validity, camera clearance, objective-zone behavior, interaction behavior, or runtime performance validation.

## Animation Notes

- Baseline asset is static.
- Cloth, rope, rawhide, knots, short stakes, stone anchors, and optional accents should be fixed in a readable pose if later approved.
- Static material variation for faded dye, soot, mud, ash, and edge wear may be planned only as non-runtime surface variation.
- No cloth simulation, wind animation, vertex sway, banner waving, rope physics, hanging prop sway, physics bodies, destructible tear behavior, burn state, material pulse, glow, particle effect, VFX, audio, Blueprint state, interaction state, quest state, objective state, UI state, damage state, aura state, or gameplay state change.
- Any moving, simulated, glowing, audio-linked, interactive, objective-readable, UI-readable, or gameplay-readable variant must be split into a separately named and approved package.

## Unreal Import Notes

This section is future guardrail planning only. No Unreal asset, game folder, import script, material instance, texture asset, socket, Blueprint, validator, runtime source, review actor, startup actor, source asset, DCC work, FBX export, cave placement, collision setup, nav setup, trigger setup, objective setup, quest/UI setup, interaction setup, material graph work, VFX, audio, or first implementation target is created or authorized.

Potential future identity after separate approval:

- Asset name: `SM_GIA_BloodAxeRedClothThresholdMarker_A01`
- Asset type: Static Mesh
- Potential future folder: `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/`
- Naming convention: `SM_GIA_BloodAxeRedClothThresholdMarker_A01`, `MI_GIA_BloodAxeRedClothThresholdMarker_A01`, `T_GIA_BloodAxeRedClothThresholdMarker_A01_BC`, `T_GIA_BloodAxeRedClothThresholdMarker_A01_N`, `T_GIA_BloodAxeRedClothThresholdMarker_A01_ORM`
- Pivot: ground center of the full marker footprint for standalone stone or stake variants; attachment center only if a later composition package explicitly owns the parent support.
- Orientation: strongest cloth read faces +X unless a later DCC/export task confirms a different project convention.
- Scale: centimeter-authored source at scale 1.0 only in a later approved implementation lane, matching the female 442 cm and male 470 cm Giant baselines without changing the Giant scale lock.
- Collision type: disabled by default; optional simple support-stone hull only if separately approved.
- LOD plan: LOD0-LOD3 required before any shipping use.
- Material slot count: 1 target, 2 maximum.
- Texture list: `T_GIA_BloodAxeRedClothThresholdMarker_A01_BC`, `T_GIA_BloodAxeRedClothThresholdMarker_A01_N`, and `T_GIA_BloodAxeRedClothThresholdMarker_A01_ORM`.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: low triangle count, one broad red read, shared Blood Axe material language, no default emissive, disabled collision on cloth/detail, and aggressive LOD reduction.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeRedClothThresholdMarker_A01/PRODUCTION_PACKAGE.md`

Future asset naming references, for planning only:

- Static mesh: `SM_GIA_BloodAxeRedClothThresholdMarker_A01`
- Material instance: `MI_GIA_BloodAxeRedClothThresholdMarker_A01`
- Base color: `T_GIA_BloodAxeRedClothThresholdMarker_A01_BC`
- Normal: `T_GIA_BloodAxeRedClothThresholdMarker_A01_N`
- ORM: `T_GIA_BloodAxeRedClothThresholdMarker_A01_ORM`

Related planning references:

- Parent kit: `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachMarkers_A01/`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachMarkers_A01/CHILD_ASSET_INTAKE.md`
- Material discipline: `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01/`

Do not create or edit source asset folders, DCC files, FBX exports, Unreal game content folders, material graphs, material instances, texture assets, validators, global indexes, backlog docs, task-board docs, bootstrap docs, startup placement, external source concept files, runtime source files, VFX assets, audio assets, or unrelated package files from this task.

## Quality Gate Checklist

- Required universal package headings are present in the requested order.
- Package is docs-only and limited to `docs/assets/props/SM_GIA_BloodAxeRedClothThresholdMarker_A01/PRODUCTION_PACKAGE.md`.
- Asset remains a broad static oxide-red cloth threshold marker tied to stone, short stake, or rope binding.
- Giant scale lock is explicit: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved ranges are females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Material restraint is explicit: faded maroon/oxide red, soot, mud, rawhide/rope, rough stone or scorched stake support, and no default emissive.
- Primary read is static cloth threshold dressing only, without flag animation, cloth simulation, wind animation, quest pointers, objective markers, UI markers, VFX/audio, material graph authoring, DCC, FBX, Unreal work, startup placement, or final visual signoff.
- No source asset, mesh, material instance, texture asset, validator, runtime source, Blueprint, implementation target, or final approval is created or claimed.
- No excessive micro-detail, readable text, UI arrows, magic glyphs, neutral Giant civic markers, dense trophy clutter, graphic gore, or glow is required for the asset read.
- Texture plan includes BC, N, and ORM maps with no default emissive map.
- Triangle budgets, material limits, LOD0-LOD3 plan, collision planning limits, animation limits, Unreal import planning, folder naming, and stop gates are included.
- Fine cloth weave, fray, rope fibers, rawhide pores, soot speckles, ash flecks, mud droplets, chipped paint, stone pitting, lichen, and small scratches are assigned to textures or normals in future work.
- Future collision remains disabled by default and non-gameplay; no route, movement, cave compatibility, interaction, objective, damage, aura, nav, quest, UI, VFX, audio, cloth simulation, or wind animation behavior is defined.
