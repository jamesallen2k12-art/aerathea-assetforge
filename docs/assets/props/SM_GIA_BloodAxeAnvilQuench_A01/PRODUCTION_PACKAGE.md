# SM_GIA_BloodAxeAnvilQuench_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeAnvilQuench_A01`
- Asset type: Static Mesh production package / hostile Blood Axe Giant anvil and quench camp utility dressing
- Task: `AET-MA-20260629-122`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Zone_AnvilQuench`
- Source route reference: `BloodAxeForge.png#Zone_AnvilQuench`
- Related planning references: `SM_GIA_BloodAxeForgeHearth_A01`, `SK_GIA_BloodAxeForgeGuard_A01`, `KIT_GIA_BloodAxeReforging_A01`, `KIT_GIA_BloodAxeScrapPile_A01`, and `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, material graph, VFX, runtime source, validator, startup placement, first build target selection, final visual approval, heat gameplay, crafting/economy/resource behavior, workstation interaction, or source concept movement is included
- Source-storage guardrail: external source concept images remain outside the repository. Do not copy, move, edit, crop, embed, rename, or commit external source concepts for this package.

`SM_GIA_BloodAxeAnvilQuench_A01` defines a static forge-support prop for hostile Blood Axe Giant camps: a massive battered anvil block, heavy stone or metal quench trough, slag tray, and simple cooling rack grouped as static camp utility dressing. It supports the forge-yard read near `SM_GIA_BloodAxeForgeHearth_A01`, but it is not a functional crafting station.

The Blood Axe must remain a hostile Giant sub-faction, not neutral/civilized Giant culture. The asset should feel stolen, raider-built, soot-dark, temporary, and brutal. It must stay separate from neutral/civilized Giant culture, including mountain stoneworker civic craft, blue-gray cave-town masonry, warm communal hearth language, terraces, waterworks, and restrained blue rune identity.

All forge, quench, slag, cooling, and heat cues in this package are visual art-direction cues only. They do not define heat gameplay, crafting behavior, economy loops, resource extraction, workstation interaction, VFX, material graph behavior, damage volumes, or runtime systems.

## Gameplay Purpose

The gameplay purpose is limited to non-interactive environment dressing for hostile Blood Axe forge yards. The prop helps players understand where stolen metal is battered, cooled, and staged in the camp without creating any usable gameplay system.

Allowed visual planning purpose:

- Mark a Blood Axe forge-support zone beside future forge hearth, scrap sorting, weapon rack, and guard compositions.
- Provide Giant-scale static dressing that reads clearly at MMO camera distance.
- Reinforce hostile Blood Axe camp identity with soot, blackened metal, heavy stone, crude red warning cloth, slag, and stolen reforged hardware.
- Give future DCC and Unreal workers scale, material, LOD, collision, and import planning notes.

Out of scope:

- Functional crafting station behavior, repair loops, salvage loops, refining, recipes, upgrades, economy, resource nodes, harvestables, vendor data, inventory data, loot containers, pickup prompts, UI markers, interaction prompts, or workstation interaction.
- Heat gameplay, burn damage, steam damage, damage volumes, encounter hazards, destructible states, physics puzzles, quench effects, active smoke, sparks, heat shimmer, or authored VFX.
- Material graph authoring, emissive-state authoring, Blueprint behavior, runtime source, validators, startup placement, first build target selection, final visual approval, DCC source, FBX export, Unreal import, or source concept movement.

## Silhouette Notes

Primary read: a Giant-scale anvil/quench cluster with a brutal low anvil mass, adjacent heavy trough, slag tray, and rack silhouettes. The group should look like hostile Blood Axe camp utility, not a polished smithy workstation.

Required silhouette elements:

- Oversized blackened anvil block with a blunt horn or wedge face, broad battered top plane, and thick field-forged body.
- Heavy stone or dark metal base that raises the anvil to Giant working height.
- Wide quench trough beside or behind the anvil, built from cracked stone, stolen plate, blackened iron bands, or split timber lined with metal.
- Simple cooling rack made from thick iron bars or crude rests, sized for Giant weapon blanks and scrap slabs.
- Slag tray or shallow catch pan with cooled lumps and ash, kept as large readable forms.
- One or two oxide red cloth wraps, paint slashes, or warning tags as Blood Axe identifiers.
- Ground-contact ash, soot falloff, scuffed packed earth, and broad dark value zones tying the cluster to a forge-yard layout.

Model real geometry for the anvil mass, base plinth, trough walls, thick rack bars, major slag forms, broad brace plates, large bolts or clamps, and main red cloth/tag shapes. Use textures and normal maps for soot speckles, pitting, fine scratches, tiny chips, minor hammer marks, small rivets, water stains, and hairline cracks.

Avoid polished Dwarven smith craft, neutral/civilized Giant stoneworker motifs, clean civic masonry, warm peaceful hearth identity, blue rune accents, normal humanoid proportions, glowing crafting rings, recipe boards, progress meters, resource crystals, loot beams, excessive steam, dense sparks, many tiny tools, graphic gore, and unreadable micro-detail.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Recommended static prop scale:

- Overall composed footprint: 520-780 cm wide, 340-560 cm deep.
- Anvil block length: 260-420 cm.
- Anvil top working height: 150-230 cm, sized for Giant arms and heavy tools.
- Anvil base/plinth footprint: 220-360 cm wide, 180-300 cm deep.
- Quench trough length: 260-460 cm.
- Quench trough rim height: 110-180 cm, lower than the anvil top so the silhouette staggers clearly.
- Cooling rack height: 120-210 cm.
- Clear working lane around the prop: 500-700 cm where a future layout expects Giant passage.
- Red cloth/tags: 60-160 cm long so they read at Giant camp scale.

Future DCC validation must compare the anvil top height, quench trough rim, rack height, and work-lane clearance against both the 442 cm female and 470 cm male Giant baselines before any Unreal placement or visual approval. The prop should feel too large and hostile for normal humanoids to operate casually.

## Materials and Color Palette

Primary material language:

- Blackened iron, dark steel, stolen/reforged plate, and hammered metal surfaces using or matching `MI_GIA_BloodAxeReforgedMetal_A01`.
- Ash-stained field stone, cracked anvil base blocks, and soot-dark ground-contact stone.
- Scorched timber or hide only as support pads, wedges, tie points, or rough guards.
- Dark quench water or oil residue shown as a matte painted surface only, with no fluid simulation or VFX.
- Cooled slag, charcoal dust, scale flakes, matte ash, oil-dark grime, and rubbed steel edges.
- Deep oxide red cloth, chipped red paint, or crude warning tags as restrained Blood Axe identifiers.
- Painted warm orange or dull coal red only as reflected color on metal or slag unless a later material/VFX task approves active states.

Suggested palette:

- Soot black: `#0B0A09` to `#24201C`
- Ash gray: `#6A6458` to `#8A8275`
- Burned field stone: `#2B2B27` to `#575247`
- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#555A5C` to `#787B78`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Quench residue: `#101616` to `#25302D`
- Cooled slag: `#2E2D29` to `#5A554B`
- Painted forge reflection: `#8A3A19` to `#B45A24`, restrained and non-glowing by default

Avoid civilized Giant blue-gray masonry, polished stoneworker craft, restrained blue runes, warm communal hearth symbolism, shamanic storm language, clean Dwarven smith presentation, bright liquid glow, or default emissive material use. Any active heat, steam, glow, smoke, sparks, water animation, or material state requires separate approval.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeAnvilQuench_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant anvil and quench static camp utility dressing cluster, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, an oversized battered blackened anvil block, heavy cracked stone base, dark quench trough, crude cooling rack, slag tray, ash and soot buildup, stolen reforged metal bands, thick iron clamps, deep oxide red warning cloth, chipped red paint, Blood Axe hostile Giant sub-faction identity, and a non-interactive forge-yard dressing role rather than a functional crafting station. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, no VFX, and MMO-friendly mid-poly production design. Present it as a static prop production sheet with front, side, back, top-down footprint, scale callouts beside 442 cm female and 470 cm male Giants, material swatches, LOD/collision notes, and explicit labels that it is planning-only set dressing. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid neutral/civilized Giant cave-town motifs, avoid crafting/economy/resource UI, avoid interaction prompts, avoid heat gameplay diagrams, avoid active steam or sparks, avoid final visual approval framing, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, runtime behavior, or final visual approval is created or approved here.

Future modeling should prioritize large readable forms:

- Anvil block: build a heavy, blunt, asymmetrical mass with a broad top plane, battered edges, one wedge or horn read, and obvious Giant scale.
- Anvil base: use cracked field-stone blocks, a dark metal plinth, or a combined stone/metal base that feels improvised and raider-built.
- Quench trough: model thick walls, reinforced corners, an interior dark surface plane, and broad stained rim shapes. Do not model fluid motion.
- Cooling rack: use thick bars, heavy end supports, and a few large rest points sized for Giant weapon blanks and scrap slabs.
- Slag tray: include one shallow tray or ground pan with large cooled slag lumps and ash masses.
- Hardware: model wide brace plates, corner clamps, hammered bands, and a few oversized rivets only where they affect silhouette.
- Blood Axe identifiers: add one or two red cloth strips, red-painted slashes, or warning tags as bold shapes.
- Ground contact: include soot falloff, ash buildup, scuffed base shadow, and packed-earth contact planning so the prop can sit near forge-yard ground modules.
- Adjacency: leave visual room for `SM_GIA_BloodAxeForgeHearth_A01`, `KIT_GIA_BloodAxeForgeScrapSorting_A01`, `KIT_GIA_BloodAxeReforging_A01`, weapon dressing racks, and forge guard characters. Do not collapse those lanes into this mesh.

Use texture, normal maps, or material masks for:

- Fine pitting.
- Tiny rivets.
- Small scratches.
- Minor hammer marks.
- Soot speckles.
- Ash dust.
- Water stains.
- Oil streaks.
- Hairline stone cracks.
- Small red paint chips.
- Minor metal scale flakes.

Do not add gameplay affordance geometry such as glowing rings, button plates, recipe boards, progress meters, resource crystals, pickup handles, UI labels, loot beams, harvest outlines, workstation signs, destructible fracture chunks, hazard boundary markers, or interaction prompts.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, or Unreal import is authored by this package.

Material slot target:

- Slot 0: `MI_GIA_BloodAxeReforgedMetal_A01` or a consuming Blood Axe hardware instance for the anvil body, metal trough lining, rack bars, clamps, braces, and large hardware.
- Slot 1: planned soot/ash/stone material for the base plinth, slag tray support, ground-contact ash, and burned field stone.
- Slot 2: planned quench residue/scorched support material for dark trough interior, scorched timber pads, hide ties, red cloth, and warning tags.
- Optional future slot 3: approval-gated heated blank, active quench, steam, or forge-heat material state only if a later visual/material/VFX task promotes an active variant. Baseline `A01` does not author this slot.

Texture naming examples:

- `T_GIA_BloodAxeAnvilQuench_A01_BC`
- `T_GIA_BloodAxeAnvilQuench_A01_N`
- `T_GIA_BloodAxeAnvilQuench_A01_ORM`
- `T_GIA_BloodAxeAnvilQuench_Metal_A01_BC`
- `T_GIA_BloodAxeAnvilQuench_StoneAsh_A01_BC`
- `T_GIA_BloodAxeAnvilQuench_ResidueCloth_A01_BC`
- Future approval-gated only: `T_GIA_BloodAxeAnvilQuench_A01_E`

Texture resolution targets:

- Default camp prop: 2K texture set.
- Repeated background variant: 1K texture set.
- Close-up hero forge-yard variant: 2K, with 4K only if a later hero-review task explicitly approves it.

Packed `ORM` guidance:

- R: strong ambient occlusion under the anvil base, trough rim, rack supports, slag tray, metal bands, clamp overlaps, ash piles, and cloth ties.
- G: high roughness for soot, ash, quench residue, cooled slag, burned stone, scorched hide, and matte blackened metal; slightly lower roughness only on rubbed steel edges.
- B: metallic only for anvil metal, trough lining, iron bands, steel plates, rack bars, clamps, rivets, and stolen shield or scrap fragments.

Keep grime and soot broad so the prop reads as a large Blood Axe camp utility object. Do not fill the asset with high-frequency speckles, tiny tool clutter, or red paint overuse.

## Triangle Budget

Default static prop target:

- LOD0: 8k-16k tris.
- LOD0 hard cap: 20k tris for a larger hero forge-yard variant with a broader rack, larger trough, and richer anvil silhouette.
- Material slots: 3 target, 4 maximum only for a separately approved active-heat or hero-review variant.
- Texture target: 2K default.

Variant guidance:

- Compact repeated anvil/quench dressing: 5k-9k tris, 2-3 material slots.
- Standard anvil/quench cluster: 8k-16k tris, 3 material slots.
- Hero forge-yard cluster with expanded base, larger trough, rack, and slag tray: 14k-20k tris, 3-4 material slots by approval.

Spend geometry on the anvil mass, base silhouette, trough wall thickness, rack outline, major brace plates, large slag forms, and red faction shapes. Do not spend geometry on tiny scratches, dense pitting, individual soot dots, small rivet fields, fine cracks, many small tools, per-droplet water detail, steam shapes, or tiny slag chips.

## LOD Plan

All important anvil/quench variants require LOD0-LOD3.

- LOD0: full anvil mass, base plinth, trough walls, trough interior surface, cooling rack, slag tray, major hardware, large slag forms, red cloth/tag shapes, soot/ash zones, and ground-contact footprint.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor brace cuts, secondary slag forms, cloth edge cuts, small rivets, trough interior subdivisions, and non-silhouette base chips.
- LOD2: 35-45 percent of LOD0; simplify anvil bevels, base block separations, rack bars, trough back-side detail, slag tray cuts, red tag folds, and ash buildup while preserving the anvil/trough/rack read.
- LOD3: 15-25 percent of LOD0; preserve the large anvil block, lower trough block, rack line, dark metal/stone value zones, red Blood Axe accents, and broad composed footprint.

LOD reduction order:

1. Tiny scratches, ash flecks, soot speckles, water stains, pitting, small chips, and paint flakes.
2. Small rivets, minor metal band bevels, cloth edge nicks, and small slag chips.
3. Secondary slag lumps, small tied strips, trough interior breakup, and rack crossbar subdivisions.
4. Back-side trough detail and underside base overlaps.
5. Secondary stone bevels and non-silhouette brace cuts.
6. Only after secondary detail is reduced, simplify the anvil block, trough mass, cooling rack read, and main red/black faction silhouette.

Never reduce the Giant-scale footprint, anvil top read, quench trough mass, cooling rack silhouette, or dark Blood Axe forge-yard identity before removing small detail.

## Collision Notes

Collision remains simple, static, and display-focused.

Recommended future collision:

- Anvil and base: one low-count convex hull or grouped boxes around the main metal/stone footprint.
- Quench trough: simple box or convex hull around the outer trough; no detailed inner collision.
- Cooling rack: one simplified blocking hull or no collision if the rack is visually thin and not intended to block movement.
- Slag tray and large slag lumps: fold into nearby simple hulls or no collision.
- Cloth tags, ash piles, small clamps, minor protrusions, and red paint shapes: no individual collision.
- Trough interior surface: no fluid, water, or interaction collision.

Do not add heat damage volumes, burn hazards, steam damage, crafting interaction volumes, salvage triggers, resource harvesting volumes, pickup collision, loot outlines, recipe zones, economy/resource triggers, destructible fracture collision, physics-simulated tools, per-rivet collision, per-slag collision, per-chain collision, VFX collision, or encounter hazard volumes.

Walkable collision should be disabled by default on the anvil, trough, rack, and slag tray unless a later level-design task explicitly promotes a variant for traversal or cover.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh with fixed anvil, base, trough, cooling rack, slag tray, ash, soot, and red-cloth silhouettes.
- Painted non-emissive warm metal reflections or residue color as visual material language only.
- No runtime motion claim.

Approval-gated future work:

- Active steam, quench vapor, sparks, smoke, heated metal glow, or heat shimmer.
- Animated material states, emissive maps, pulsing heat, water movement, or bloom.
- Hammering loops, tool animation, rack movement, physics-simulated scrap, destructible states, hanging prop sway, or cloth motion.
- Any interaction, crafting, salvage, repair, heat gameplay, burn damage, encounter hazard, audio cue, Blueprint state, or workstation behavior.

Baseline `A01` stays inert set dressing.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, Niagara system, validator, startup actor, runtime source, or import script is created by this package.

Planned future Unreal asset:

- Asset name: `SM_GIA_BloodAxeAnvilQuench_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Props/Forge/`
- Planned material folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Planned texture folder: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/Forge/`
- Import scale: centimeter-authored source, import scale 1.0 after future DCC/export validation
- Pivot: ground-contact center of the composed anvil/quench footprint
- Orientation: primary open/work side faces +X unless a future project import convention overrides it
- Collision type: simple custom collision or generated primitive collision following the display-focused rules above
- LODs: LOD0, LOD1, LOD2, LOD3 required before production import approval
- Material slot count: 3 target, 4 maximum only for approved hero or active-state variant
- Blueprint behavior: none
- Animation list: none
- Sockets: none required for baseline static mesh
- Performance notes: preserve anvil block read, trough mass, cooling rack silhouette, dark metal/stone material blocks, and red Blood Axe accents; reduce soot noise, tiny chips, small rivets, slag chips, rack subdivisions, and back-side detail before primary silhouette.

Potential future sockets or markers, not authorized by this package:

- `anvil_work_top`
- `quench_surface`
- `quench_steam_origin`
- `cooling_rack_l`
- `cooling_rack_r`
- `slag_tray_origin`

These are planning notes only. Do not author sockets, VFX hooks, material states, Blueprint behavior, validator checks, or startup placement from this package.

Planned texture names:

- `T_GIA_BloodAxeAnvilQuench_A01_BC`
- `T_GIA_BloodAxeAnvilQuench_A01_N`
- `T_GIA_BloodAxeAnvilQuench_A01_ORM`
- Optional future approval-gated `T_GIA_BloodAxeAnvilQuench_A01_E`

Import guardrails:

- Do not import a Static Mesh, material, texture, Blueprint, Niagara system, validator, or startup actor from this docs-only package.
- Do not add crafting UI, resource behavior, economy data, salvage data, heat volumes, damage volumes, VFX graphs, material graphs, audio cues, loot tables, interaction prompts, workstation behavior, or encounter logic.
- Do not claim final visual approval, final source concept approval, first DCC target selection, or production import readiness.

## Folder and Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeAnvilQuench_A01/PRODUCTION_PACKAGE.md`

Planned future source/export paths, pending approval:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeAnvilQuench_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeAnvilQuench_A01.fbx`
- Unreal: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Props/Forge/`

Recommended future names:

- Static mesh: `SM_GIA_BloodAxeAnvilQuench_A01`
- Compact repeated variant: `SM_GIA_BloodAxeAnvilQuench_Compact_A01`
- Hero forge-yard variant, if approved: `SM_GIA_BloodAxeAnvilQuench_Hero_A01`
- Metal material instance: `MI_GIA_BloodAxeReforgedMetal_A01`
- Stone/ash material instance: `MI_GIA_BloodAxeAnvilQuench_StoneAsh_A01`
- Residue/cloth material instance: `MI_GIA_BloodAxeAnvilQuench_ResidueCloth_A01`
- Textures: `T_GIA_BloodAxeAnvilQuench_A01_BC`, `T_GIA_BloodAxeAnvilQuench_A01_N`, `T_GIA_BloodAxeAnvilQuench_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concept folders, global indexes, task-board files, backlog files, bootstrap files, or any package outside this owned docs path from this task.

## Approval Gates and Stop Points

- Stop before final Anvil/Quench visual approval, final silhouette lock, first playable visual signoff, or first DCC target selection.
- Stop before creating source folders, Blender files, sculpt files, retopo files, UVs, bakes, proof renders, LOD sources, collision proxies, FBX exports, Unreal imports, material graphs, textures, Blueprints, Niagara systems, validators, or startup placements.
- Stop before copying, moving, embedding, cropping, editing, renaming, or committing external source concepts.
- Stop before adding VFX, active steam, sparks, smoke, water motion, heated metal glow, heat shimmer, emissive maps, animated material states, bloom, audio cues, or material graph behavior.
- Stop before defining heat damage, burn damage, crafting, repair, salvage, refining, recipes, upgrade benches, economy, vendor, inventory, resource harvesting, loot, pickup, interaction prompts, UI markers, destructible behavior, physics puzzles, or encounter hazards.
- Stop before adding Blueprint behavior, runtime source, gameplay tags, data assets, resource tables, economy data, loot tables, validators, navmesh requirements, startup actors, or first build target selection.
- Stop before merging forge hearth, scrap sorting, bellows, weapon racks, process-line kits, forge tools, or forge-guard content into this anvil/quench mesh unless a later approved package explicitly expands scope.
- Stop if the asset requires changing the validated Giant scale lock or `SK_GIA_Base_A01` assumptions.
- Stop if Blood Axe red-black raider language starts replacing neutral/civilized Giant culture.
- Stop if anvil, quench, slag, or cooling language starts reading as implemented gameplay, active VFX, heat hazard, interactable crafting, or final visual approval instead of static visual production language.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Validated Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved range females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Package describes static camp utility dressing, not a functional crafting station, resource node, loot container, economy object, heat hazard, or interaction system.
- Anvil, quench trough, cooling rack, slag tray, soot, ash, residue, and painted warmth are visual-only art-direction cues; no VFX, material graph, emissive state, damage volume, active steam, sparks, smoke, or heat shimmer is authored.
- Primary silhouette reads at MMO distance: huge anvil block, heavy base, dark trough, simple rack, slag tray, broad hardware, and restrained red Blood Axe identifiers.
- Materials use blackened iron, dark steel, burned field stone, ash, soot, quench residue, cooled slag, scorched support materials, and oxide red warning accents consistently.
- No neutral/civilized Giant blue-gray civic stonework, warm peaceful hearth identity, restrained blue runes, polished masonry, waterworks, terraces, or cave-town craft language is used as baseline.
- Tiny scratches, soot speckles, pitting, hairline cracks, small chips, water stains, paint flakes, minor hammer marks, and small rivets are assigned to textures or normals instead of geometry.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision notes, animation limits, Unreal import planning, folder/naming recommendation, stop gates, and source-storage guardrails are included.
- Package makes no DCC, FBX, Unreal Content, runtime source, material graph, VFX, validator, startup placement, first build target selection, final visual approval, source concept movement, index edit, task-board edit, backlog edit, bootstrap edit, or unrelated package edit claim.
