# SM_GIA_BloodAxeBrokenShieldPathMarker_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeBrokenShieldPathMarker_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Child intake row: `BloodAxeCamp.png#PathMarkers_BrokenShieldMarker_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Visual brief: large broken shield fragment, dull scrap plate, rope-tied stake, and red paint smear as a sparse hostile warning
- Package status: documentation-only production package

`SM_GIA_BloodAxeBrokenShieldPathMarker_A01` is a crude Blood Axe path warning made from a large broken shield fragment lashed to a scorched stake, with a dull scrap plate and broad oxide red paint smear. It should read from MMO camera distance as hostile Giant camp route dressing: heavy, improvised, field-made, and deliberately threatening without becoming a usable shield, loot object, destructible barricade, inventory prop, or combat cover asset.

The Blood Axe identity must stay separate from neutral/civilized Giant culture. This marker belongs only to the hostile Blood Axe raider sub-faction and must not become a civic Giant road sign, cave-town wayfinding marker, refined highland guidepost, stoneworker craft object, warm hearth settlement detail, or restrained blue-rune cultural prop.

This package does not authorize external source concept handling, DCC work, Unreal work, startup placement, final visual approval, implementation target selection, Hermes work, usable shield behavior, pickup behavior, loot behavior, destructible behavior, inventory behavior, or combat cover definition.

## 2. Gameplay Purpose

The asset is static visual warning dressing for Blood Axe camp paths, approach bends, rough perimeter routes, and hostile trail edges. Its role is to add Giant-scale faction readability and sparse path rhythm without defining any gameplay system.

Allowed purpose:

- Signal a Blood Axe-controlled route or threshold through environmental storytelling only.
- Add one low-to-mid-height shield-scrap warning accent among cairns, cloth stakes, horn/bone markers, ash bases, and banner-line dressing.
- Break up rough ground planes with a crude Giant-made silhouette that reads as hostile warning from a gameplay camera.
- Reinforce Blood Axe raider presence through broken shield mass, blackened scrap, rope lashing, soot, mud, and broad red paint.

Out of scope:

- No usable shield behavior, pickup behavior, loot behavior, destructible behavior, inventory behavior, combat cover definition, waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding helper, interaction prompt, resource node, salvage rule, crafting/economy behavior, AI patrol marker, spawn marker, encounter scripting, faction buff, morale behavior, UI marker, VFX pulse, audio cue, startup placement, runtime behavior, DCC work, Unreal work, final approval, implementation target, or Hermes work.

## 3. Silhouette Notes

Primary read:

- Large broken shield fragment mounted or lashed to a short scorched timber stake.
- Dull scrap plate crossing or capping part of the broken shield face, angled enough to catch silhouette without reading as a functional repair.
- Thick rope or rawhide lashing tying the shield fragment and plate to the stake.
- Broad oxide red paint smear across the shield or plate, non-symbolic and not readable as text or UI.
- Asymmetrical, snapped, battered outline with missing corners, a fractured rim, and one dominant jagged side.
- Low ash, mud, or one grounding stone at the base only if needed to seat the prop visually.

Shape hierarchy:

- First read: broken shield fragment silhouette.
- Second read: rope-tied stake support.
- Third read: dull scrap plate and broad red paint smear.
- Fourth read: soot, mud, scratches, dents, frayed rope, and chipped edges.

Model as real geometry in a later separately approved source task:

- Main shield fragment, thick rim segments, major broken edge, stake shaft, dull scrap plate, primary rope lashings, large fastening bands, broad base mound, and any large grounding stones.

Keep in textures or normal maps:

- Fine wood grain, shield dents, paint chips, metal pitting, tiny scratches, soot speckles, ash flecks, rope fibers, leather grain, small splinters, mud streaks, and minor edge chips.

Avoid:

- Complete shield silhouette, intact handle presentation, polished shield face, heroic crest, readable symbols, UI arrow shapes, glowing runes, blue rune language, refined civic carving, neutral Giant wayfinding motifs, graphic gore, dense trophy clutter, many tiny plates, usable item framing, loot sparkle language, destructible fracture stages, or waist-high cover readability.

## 4. Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Author any future source in centimeters. 1 Unreal unit equals 1 cm.

Target prop dimensions:

- Overall visible height: 120-240 cm.
- Preferred A01 nominal height: 170-210 cm, roughly knee-to-low-waist warning height against the Giant baselines.
- Ground footprint: 90-220 cm wide by 70-180 cm deep.
- Shield fragment: 90-180 cm wide, 80-165 cm tall, with an uneven broken edge and thick rim mass.
- Shield thickness and rim depth: 6-18 cm at the most readable edge.
- Stake height above ground: 130-230 cm, with 10-24 cm rough diameter.
- Dull scrap plate: 50-120 cm wide, 5-14 cm thick at bent or raised edges.
- Rope or rawhide lashing: 5-12 cm apparent diameter, using a few large turns instead of dense cord detail.
- Optional ash/mud grounding spread: up to 260 cm footprint, shallow and visually subordinate.

The marker should feel built and placed by hostile Giants, not scaled up from human camp dressing. It should remain smaller and lower than Blood Axe banner-line assets, watch posts, gate markers, ritual stones, and defensive barricades.

## 5. Materials and Color Palette

Primary materials:

- Broken shield wood, split planks, battered thick rim, dull scrap plate, blackened iron, and dark steel.
- Scorched timber stake, hacked wood end, soot-dark burn marks, and exposed dark brown cuts.
- Heavy rope, rawhide, dirty leather ties, or sinew lashing.
- Oxide red paint smear, faded red hand-applied streaks, dull maroon weathering, and soot-dark paint edges.
- Ash, charcoal, trampled mud, burned grass, and rough field stone at the base if needed.

Palette targets:

- Blood Axe dull red paint: `#5F1513` to `#8B211B`
- Dark dried red shadow, without gore read: `#3A0E0C` to `#551410`
- Blackened iron and charcoal: `#111214` to `#2A2C2E`
- Dull scrap edge and worn metal: `#4B4A45` to `#777167`
- Scorched timber and shield wood: `#22170F` to `#5A351E`
- Rope, rawhide, and dirty leather: `#6C5434` to `#A88958`
- Rough ash, mud, and stone: `#2E2C28` to `#6C6254`

Material separation rules:

- Use Blood Axe red sparingly but clearly as the focal warning mark.
- Keep metal dull, blackened, and rough. No polished trim or heroic shield finish.
- Keep rope and hide matte and practical, with large readable turns.
- No default emissive, blue runes, hearth glow, polished civic metal, refined stone carving, or neutral/civilized Giant material language.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeBrokenShieldPathMarker_A01` for the world of Aerathea. The design should emphasize a large broken shield fragment, dull blackened scrap plate, rope-tied scorched timber stake, broad oxide red paint smear, ash and mud at the base, hostile Blood Axe Giant sub-faction identity, clear separation from neutral/civilized Giant culture, sparse warning-marker placement, and the gameplay role of static non-interactive route dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a single prop concept sheet with front, side, and three-quarter views, material swatches, LOD/collision notes, and scale callouts beside a 442 cm female Giant and a 470 cm male Giant on a clean background. Avoid copying any existing franchise, avoid making the shield usable, avoid pickup or loot presentation, avoid destructible state diagrams, avoid inventory framing, avoid combat cover readability, avoid neutral Giant cave-town architecture, avoid blue runes, avoid readable text, avoid UI arrows, avoid gore, avoid DCC/Unreal/startup/final approval/implementation target/Hermes implications, and avoid excessive micro-detail that would not translate to a mid-poly asset.

## 7. Modeling Notes

This section is a future modeling handoff only. No source mesh, sculpt, retopo, UV, bake, proof render, FBX export, collision proxy, tool file, validator, runtime file, Unreal Content, startup placement, final approval asset, implementation target, or Hermes file is created or authorized by this package.

Model as real geometry if a separate approved build lane exists later:

- One dominant broken shield fragment with a thick, readable rim and irregular missing edges.
- A rough scorched stake behind or through the fragment, visibly carrying the weight.
- One dull scrap plate strapped across the shield face or upper edge, with broad bends and battered corners.
- Three to six large rope/rawhide turns that clearly bind shield, plate, and stake together.
- Large split surfaces, chunky bevels, and broad dents that support hand-painted texture reads.
- Optional low ash/mud base mound or one grounding stone, kept secondary to the shield warning shape.

Construction notes:

- Use an asymmetrical composition so the prop reads improvised and hostile.
- Keep the shield fragment broken enough that it cannot read as a functional shield or salvageable player item.
- Avoid a centered grip, intact boss, inventory-facing silhouette, clean straps, or heroic crest.
- Do not make the shield face wide and smooth enough to imply reliable combat cover.
- Put the pivot at ground center under the stake/base footprint if a later source task is approved.
- Keep underside and back detail simple; the prop is primarily read from path-level and three-quarter views.

Keep in texture or normal maps:

- Small chips, hairline cracks, shield grain, soot speckles, ash flecks, tiny dents, scratch lines, metal pitting, paint chips, rope fibers, leather pores, mud streaks, and minor splinters.

## 8. Texture and Material Notes

Target material strategy:

- 1 material slot preferred for the shipping prop.
- 2 material slots allowed only if shield/wood/rope and metal/paint need separation for reuse or close review.
- No emissive material slot for the default asset.
- No unique material per rope turn, plate chip, paint streak, shield splinter, ash patch, or mud stain.

Texture set target:

- 1K texture set for normal Blood Axe camp dressing use.
- 2K only if this exact prop is promoted for close review in a separate approved task.
- Required maps: Base Color, Normal, packed ORM.
- Emissive map is not approved for this default warning marker.

Suggested future texture names:

- `T_GIA_BloodAxeBrokenShieldPathMarker_A01_BC`
- `T_GIA_BloodAxeBrokenShieldPathMarker_A01_N`
- `T_GIA_BloodAxeBrokenShieldPathMarker_A01_ORM`

Suggested future material instance:

- `MI_GIA_BloodAxeBrokenShieldPathMarker_A01`

Packed `ORM` plan:

- R: Ambient occlusion under rope wraps, between shield and stake, around scrap plate overlaps, inside broken rim recesses, and at ash/mud contact.
- G: High roughness for wood, rope, rawhide, leather, paint, soot, ash, and mud; medium-high varied roughness for blackened metal and dull scrap edges.
- B: Metallic only on the dull scrap plate, blackened iron rim fragments, clamps, or exposed metal edges.

Base Color guidance:

- The red smear must look like crude oxide paint, not glowing magic, UI paint, or gore.
- Paint should be broad and sparse, with weathered edges and no readable symbol.
- Shield wood, stake, and rope should carry most of the surface area so the red accent remains a warning beat rather than a full red object.

## 9. Triangle Budget

Target future LOD0 budget:

- Preferred: 1,800-3,800 tris.
- Hard cap: 4,000 tris.
- Material slots: 1 preferred, 2 maximum.
- Texture size: 1K default, 2K only by later close-review approval.

Geometry spend:

- Spend triangles on the broken shield silhouette, thick rim, stake profile, major rope lashings, dull scrap plate bend, broad shield cracks, and base grounding.
- Preserve the warning profile from MMO camera distance with a clear shield-fragment/stake read.

Do not spend triangles on:

- Tiny splinters, dense paint chips, many small scratches, individual rope fibers, small nail heads, tiny dents, soot flecks, ash clumps, mud grains, fine wood grain, or many layered scrap shards.

The prop should stay cheap enough for sparse repeated camp dressing and must not use barricade, cover, or hero-shield budgets.

## 10. LOD Plan

All future important versions require LOD0-LOD3.

- LOD0: Full broken shield fragment, thick rim segments, visible stake, dull scrap plate, major rope lashings, broad red paint smear, large broken edges, and optional base ash/mud shape.
- LOD1: 60-70 percent of LOD0; simplify shield bevels, reduce scrap plate bends, merge minor rope turns, flatten underside cuts, and remove small base chips.
- LOD2: 35-45 percent of LOD0; preserve shield-fragment/stake silhouette, red paint read, and scrap-plate accent while baking most dents, cracks, and lashing detail into textures.
- LOD3: 15-25 percent of LOD0; preserve only the broad broken shield mass, stake silhouette, and a simplified scrap/paint read; remove back-side detail, small lashings, base chips, and secondary plates.

Reduction order:

1. Tiny paint chips, soot speckles, ash flecks, scratches, nail heads, small dents, and fine wood grain.
2. Minor rope fibers, secondary lashing ridges, leather pores, and small knot tails.
3. Small shield splinters, tiny plate chips, and secondary broken-edge cuts.
4. Back-facing shield detail, underside cuts, and non-visible stake cuts.
5. Secondary scrap plate bends and minor base ash geometry.

Never reduce the broken shield fragment silhouette, rope-tied stake read, dull scrap plate accent, or Blood Axe red/black hostile identity before removing micro-detail.

## 11. Collision Notes

Default collision should be disabled or very simple depending on a later placement need.

- Preferred default: no collision for visual dressing where player contact is not required.
- If contact is later required: one simple box or low-count convex hull around the stake/base mass and one simplified hull around the largest shield fragment.
- Keep any collision shallow and conservative so the prop does not become combat cover.
- No per-board, per-rim, per-rope, per-plate, per-chip, per-splinter, per-ash, or per-mud collision.
- No cloth, physics, destructible, pickup, loot, resource, waypoint, objective, nav helper, interaction, aura, trigger, damage, inventory, shield-use, or combat cover collision.
- If placed near paths in a later task, collision must not imply a nav blocker or defensive barricade unless a separate gameplay task explicitly authorizes that behavior.

## 12. Animation Notes

Baseline asset is fully static.

Allowed planning:

- Static mesh prop only.
- Fixed shield fragment, stake, rope, scrap plate, paint, and base shape.
- Optional static material wear variation only in a later approved material task.

Not approved:

- Skeletal animation, vertex wind, cloth simulation, dangling rope physics, shield swing, collapse, breakage, destructible state, pickup animation, inventory presentation, combat cover state, runtime material state, emissive pulse, VFX pulse, audio cue, interaction animation, waypoint behavior, trail-marker behavior, objective logic, AI logic, spawn timing, startup placement, Unreal work, DCC work, implementation target, final approval, or Hermes-driven behavior.

Any moving, glowing, interactive, destructible, pickup, loot, inventory, combat-cover, or gameplay-readable version must be split into a separately named package and separately approved task.

## 13. Unreal Import Notes

This section records reference-only constraints for a possible future separate import task. This package performs and authorizes no Unreal work, no Content asset creation, no material instance creation, no texture import, no Blueprint, no socket authoring, no validator, no runtime source, no startup placement, no final visual approval, no implementation target, and no Hermes work.

Reference metadata only if a separate approved task opens later:

- Asset name: `SM_GIA_BloodAxeBrokenShieldPathMarker_A01`
- Asset type: Static Mesh prop
- Reference Content folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/PathMarkers/`
- Reference material folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Naming convention: `SM_` for mesh, `MI_` for material instance, `T_` for textures.
- Pivot location: ground/base center below the stake and shield footprint.
- Orientation: primary shield-fragment read faces +X unless a later approved source/export task confirms a different project convention.
- Scale: centimeter-authored source, import scale 1.0.
- Collision type: disabled by default or simple primitive collision only; no complex collision required by default.
- LODs: LOD0, LOD1, LOD2, and LOD3 required before any shipping use.
- Material slot count: 1 preferred, 2 maximum.
- Texture list: `T_GIA_BloodAxeBrokenShieldPathMarker_A01_BC`, `T_GIA_BloodAxeBrokenShieldPathMarker_A01_N`, `T_GIA_BloodAxeBrokenShieldPathMarker_A01_ORM`.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: use low material count, disabled or simple collision, no dynamic lights, no emissive, no physics, no destructible setup, no cover setup, and aggressive LOD reduction of small detail.

## 14. Folder and Naming Recommendation

Docs path created by this task:

- `docs/assets/props/SM_GIA_BloodAxeBrokenShieldPathMarker_A01/PRODUCTION_PACKAGE.md`

Reserved future names only if a separate approved task authorizes asset creation:

- Static mesh: `SM_GIA_BloodAxeBrokenShieldPathMarker_A01`
- Material instance: `MI_GIA_BloodAxeBrokenShieldPathMarker_A01`
- Base Color: `T_GIA_BloodAxeBrokenShieldPathMarker_A01_BC`
- Normal: `T_GIA_BloodAxeBrokenShieldPathMarker_A01_N`
- Packed ORM: `T_GIA_BloodAxeBrokenShieldPathMarker_A01_ORM`

Do not add or edit from this task:

- `Content/Aerathea/`
- `SourceAssets/`
- `Tools/DCC/`
- `Tools/Unreal/`
- Runtime source
- External source concepts
- Global indexes
- Hermes files or configuration
- Startup scenes, validators, source folders, export folders, implementation handoffs, build status files, or final approval records

## 15. Quality Gate Checklist

- Package is docs-only and changes only the requested production package file.
- Asset is original to Aerathea and belongs to the Blood Axe hostile Giant sub-faction only.
- Blood Axe path-marker language stays separate from neutral/civilized Giant culture, cave-town masonry, refined highland wayfinding, warm hearth settlement cues, and restrained blue-rune language.
- Visual brief is present: large broken shield fragment, dull scrap plate, rope-tied stake, and red paint smear as a sparse hostile warning.
- Validated Giant scale is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- Silhouette is readable from MMO camera distance as a broken shield warning marker, not a complete shield, loot pickup, inventory item, destructible object, combat cover asset, or barricade.
- Materials use broken shield wood, dull scrap plate, blackened iron, scorched timber, rope/rawhide, oxide red paint, soot, ash, mud, and rough field stone consistently.
- No usable shield behavior, pickup behavior, loot behavior, destructible behavior, inventory behavior, combat cover definition, waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, interaction behavior, resource behavior, crafting/economy behavior, VFX/audio, runtime behavior, or startup placement is defined.
- No DCC source, FBX export, Unreal Content, runtime source, validator file, final visual approval, first implementation target, source concept movement, global index edit, or Hermes work is authorized.
- Triangle budget, texture map plan, LOD0-LOD3 plan, collision limits, animation limits, reference-only Unreal notes, and naming recommendations are included.
- Tiny splinters, scratches, paint chips, soot speckles, ash flecks, metal pitting, rope fibers, wood grain, mud streaks, and small dents are assigned to textures or normal maps.
- Default emissive, ritual glow, shamanic glow, signal glow, magic marker states, animated material states, UI-like marker language, readable text, polished shield presentation, and neutral/civilized Giant material language are absent.
