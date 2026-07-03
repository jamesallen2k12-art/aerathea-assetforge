# KIT_GIA_BloodAxeCamp_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeCamp_A01`
- Asset type: Production kit / multi-asset environment and settlement camp set
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Source references: `BloodAxeCamp.png`, `BloodAxecamp.png`, `Blood Axe Village.png`, `BloodAxeGate.png`, `BloodAxeForge.png`, `BloodAxeShelter.png`, `BloodAxeShamanHut.png`, and `BloodAxeStronghold.png` as catalogued by existing intake docs.
- Related kit dependency: `KIT_GIA_BloodAxeArmory_A01` for armory banners, scrap, reforging, bowyer, and weapon-dressing language.
- Status: docs-only kit production package ready for planning review.
- Source-storage guardrail: source concepts remain in the external concept folder only. Do not copy, move, edit, embed, or commit source images as part of this package.

`KIT_GIA_BloodAxeCamp_A01` defines a hostile Giant raider camp kit: rough highland shelters, defensive gates, watch points, forge and cooking zones, dressing racks, red warning banners, packed-earth paths, barricades, and camp clutter. The visual read should be brutal, temporary, territorial, and Giant-scaled, with oversized timber, hide, bone markers, blackened iron, stolen scrap, soot, ash, and torn red cloth. It must not become the default Giant culture; neutral and civilized Giants remain tied to hidden mountain settlements, master stonework, blue-gray masonry, terraces, waterworks, and warm hearth craft.

## Gameplay Purpose

This kit supports future Blood Axe camp layouts, hostile territory dressing, warband staging areas, gate approaches, camp navigation, and encounter-space composition at planning level only. It provides environment modules that can later frame Blood Axe Giant raiders, hunters, bowyers, sentries, chieftain approaches, and camp production zones without defining AI, encounter behavior, loot, resource loops, crafting, salvage, economy, or destructible behavior.

Expected planning uses:

- Camp perimeter and gate silhouettes for hostile territory recognition.
- Shelter, watch, forge, cooking, and dressing zones for environmental storytelling.
- Reusable camp dressing props that scale correctly around Giants.
- Visual continuity with `KIT_GIA_BloodAxeArmory_A01` while keeping camp modules separate from armory child packages.
- Composition references for later approval-gated DCC and Unreal work.

## Silhouette Notes

The kit should read from a distance as a brutal Giant camp, not a normal humanoid campsite scaled up. Use oversized, weighty forms:

- Tall raw-log gates with asymmetrical crossbeams, broad red banners, horn and bone markers, and crude blackened metal bindings.
- Hide-and-timber shelters with low, heavy rooflines, massive support ribs, tusk or horn silhouettes, and wide Giant-scale entrances.
- Watch points built from tree trunks, rough platforms, lashed railings, suspended trophies, and banner poles.
- Forge and cooking zones with heavy stone hearths, soot-blackened windbreaks, giant anvils, quench troughs, cooking spits, ash banks, and scrap-metal racks.
- Dressing zones with hide frames, drying racks, repair benches, trophy stands, tool hooks, and weapon staging rails.
- Paths made from trampled earth, log edges, cairn markers, broken shield plates, and red cloth warning strips.
- Barricades made from pointed logs, scrap shields, broken blades, chained plates, and rough stone weights.
- Camp clutter grouped into large readable shapes, not dense piles of tiny props.

Model the primary silhouettes, beams, walls, gates, platforms, hearth stones, roof ribs, large chains, broad banners, major trophies, and large scrap plates. Use textures and normal maps for small cuts, scratches, stitch lines, soot streaks, tiny rivets, rope fibers, wood grain, and dense grime.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock for all camp planning:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Suggested module scale targets:

- Main camp gate clear height: 650-850 cm; clear width: 550-750 cm.
- Secondary gate or side entry clear height: 540-700 cm; clear width: 400-550 cm.
- Shelter entrance clear height: 500-650 cm; interior standing clearance should support a 470 cm male Giant where the shelter is meant to be occupied.
- Shelter footprint: 900-1800 cm wide depending on longhouse, hut, or lean-to variant.
- Watch platform deck height: 450-800 cm; rail and step spacing must read as Giant-built.
- Main paths: 500-800 cm wide; side paths: 350-500 cm wide.
- Barricade height: 250-500 cm; main gate flanking stakes can exceed 650 cm.
- Forge/cooking/dressing work surfaces: 160-260 cm high, sized for Giant hands and tools.

Smallfolk should read as trespassers in an oversized enemy camp. Do not shrink Blood Axe props to normal humanoid scale unless a later loot/display task explicitly requests a separate scaled-down variant.

## Materials and Color Palette

Primary materials:

- Raw dark timber, split logs, charred stakes, and rough lashings.
- Hide, fur, scorched leather, rawhide roof panels, sinew ties, and heavy rope.
- Blackened iron, dark steel, broken shield plates, stolen scrap, large chains, and crude metal brackets.
- Rough field stone, ash-stained hearth blocks, packed earth, mud, slag, and charcoal.
- Bone, horn, tusks, skull-shaped trophies, and large teeth used sparingly as silhouette accents.
- Torn red cloth, red war paint, and weathered red banner panels as Blood Axe identifiers.
- Forge orange, coal red, and warm cooking-fire color only where fire or heated metal is present.

Avoid neutral/civilized Giant material language: carved blue-gray monumental stonework, warm orderly hearth halls, restrained blue runes, mountain-civic terraces, clean masonry, and refined stoneworker motifs. Emissive use is not a baseline camp requirement; optional emissive maps are limited to later-approved forge coals, lamps, or shamanic variants.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeCamp_A01` for the world of Aerathea. The design should emphasize a hostile Giant raider camp silhouette, massive raw-log gates, hide-and-timber shelters, elevated watch points, forge and cooking zones, hide-dressing racks, red warning banners, packed-earth paths, spike barricades, camp clutter, blackened iron, stolen scrap, scorched leather, bone markers, soot, ash, rough timber, hostile Blood Axe sub-faction identity, and a gameplay role as enemy-territory environment dressing and camp composition. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing forge/fire emissive accents only where justified, and MMO-friendly production design. Present it as a production camp kit board with a top-down layout, modular gate/shelter/watch/forge/cooking/dressing/barricade callouts, scale callouts against a 442 cm female Giant and 470 cm male Giant, and notes separating Blood Axe raider culture from neutral/civilized Giant culture. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe language the default Giant culture, avoid encounter behavior diagrams, avoid loot/crafting/resource UI, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

Concept source reference note: use the source filenames listed above as direction references through existing intake records only. This docs-only task does not inspect, copy, crop, move, embed, or approve external source concept art.

## Modeling Notes

This package is a planning document only. Future DCC work should treat the camp as modular child assets rather than one collapsed scene mesh.

Recommended module groups:

- Gates: main palisade gate, trophy entry, side gate, removable barricade insert, gate lintel, gate posts, chain loops, and banner sockets.
- Shelters: rawhide longhouse, lean-to, shaman hut shell, simple sleeping shelter, roof rib variants, entrance flaps, support posts, and ground tie-downs.
- Watch points: raised platform, stake tower, gate lookout deck, ladder or ramp module, rail pieces, signal banner pole, horn marker, and perch clutter.
- Forge zone: hearth body, stone windbreak, Giant anvil block, quench trough, slag tray, cooling rack, scrap rack, heated blank display, and ash piles.
- Cooking zone: stone fire pit, oversized spit, hanging frame, pot stand, fuel pile, butcher block, and non-graphic food prep props.
- Dressing zone: hide frame, drying rack, armor repair stand, weapon staging rail, trophy stand, tool hook board, and workbench.
- Paths and ground dressing: packed-earth path strips, trampled mud patches, log edging, stepping stones, warning cloth stakes, and approach cairns.
- Barricades: spike wall, log chevaux-de-frise, scrap shield wall, chained plate obstruction, rough stone weight, and broken-blade fence.
- Camp clutter: bedrolls, hide bundles, large crates, sacks, baskets, bone markers, rope coils, tool buckets, ash piles, firewood stacks, and discarded armory parts.

Use snap-friendly pivots and modular dimensions where possible. Keep repeated clutter pieces instanced or variant-friendly. Do not model every rope fiber, tiny stitch, tooth chip, ash fleck, or scratch; assign those to texture, normal, AO, or trim-sheet detail.

## Texture and Material Notes

Use Base Color, Normal, packed ORM, and optional Emissive only for later-approved fire, forge, lamp, or shamanic variants.

Shared material families:

- `MI_GIA_BloodAxeRoughTimber_A01`
- `MI_GIA_BloodAxeScorchedHide_A01`
- `MI_GIA_BloodAxeReforgedMetal_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeBoneTrophy_A01`
- `MI_GIA_BloodAxePackedEarth_A01`
- `MI_GIA_BloodAxeSootAsh_A01`
- `MI_GIA_BloodAxeForgeCoal_A01` only for approved forge or fire states

Texture naming examples:

- `T_GIA_BloodAxeCampGate_A01_BC`
- `T_GIA_BloodAxeCampGate_A01_N`
- `T_GIA_BloodAxeCampGate_A01_ORM`
- `T_GIA_BloodAxeShelter_A01_BC`
- `T_GIA_BloodAxeShelter_A01_N`
- `T_GIA_BloodAxeShelter_A01_ORM`
- `T_GIA_BloodAxeForgeZone_A01_E` only if a later fire/heat material state is approved

Large structures should target 2-4 material slots. Small props should target 1 material slot, or 2 where metal/hide separation materially improves reuse. Use trim sheets and tiling material sets for timber, hide, packed earth, and blackened metal so camp modules can share texture memory.

## Triangle Budget

Target ranges for future child packages:

- Main camp gate: 18k-35k tris LOD0, 3-4 material slots.
- Secondary gate or side entry: 10k-20k tris LOD0, 2-3 material slots.
- Shelter modules: 8k-22k tris LOD0 each, 2-4 material slots.
- Watch platforms or stake towers: 8k-18k tris LOD0 each, 2-3 material slots.
- Forge, cooking, or dressing zone cluster: 8k-24k tris LOD0 depending on child breadth, 2-4 material slots.
- Barricade modules: 2k-8k tris LOD0 each, 1-3 material slots.
- Path strips, ground patches, and cairn markers: 500-4k tris LOD0 each, 1-2 material slots.
- Banner poles and warning markers: 800-5k tris LOD0 each, 1-2 material slots.
- Camp clutter pieces: 300-4k tris LOD0 per prop; larger clutter clusters can reach 8k-14k tris if composed from reusable child meshes.
- Composed camp preview: keep modular preview scenes under 120k tris by instancing repeated shelters, stakes, banners, and clutter. Do not collapse the entire camp into one production mesh.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full primary silhouette, major beams, gate shape, shelter roof mass, platform rails, hearth stones, large trophies, banner cloth, barricade stakes, and camp clutter groups.
- LOD1: 60-70 percent of LOD0; reduce small chips, secondary rope wraps, small edge boards, dense scrap, tiny cloth tears, inner shelter supports, and minor prop backs.
- LOD2: 35-45 percent of LOD0; simplify rail geometry, trophy clusters, path stones, repeated stakes, hanging props, forge side dressing, and secondary collision-visible silhouettes.
- LOD3: 15-25 percent of LOD0; preserve the gate, shelter, watch, forge, path, barricade, and banner reads through large color and shape blocks.

Remove tiny lashings, small scratches, dense rope wraps, minor teeth, small straps, and backside camp dressing before reducing gate height, shelter roofline, watch platform outline, barricade spike read, or banner shape. Future far-view camp layouts may use HLODs or impostor cards, but that is outside this docs-only package.

## Collision Notes

Use simple, predictable collision:

- Gates and barricades: blocking simple boxes or low-count convex hulls; no per-spike collision.
- Shelter walls and roof forms: simplified boxes or hulls; entrances must preserve Giant clearance where enterable.
- Watch platforms: simple deck and railing collision if walkable in a future map; no ladder, climb, or AI behavior in this package.
- Forge, cooking, and dressing zones: simple hulls around hearths, racks, work surfaces, and large props; no heat damage, crafting, pickup, or interaction behavior.
- Paths and ground patches: no collision unless a raised edge or step is needed.
- Banners and hanging props: pole collision only, cloth bounds simplified or disabled.
- Small clutter: collision disabled by default unless the child prop is meant to block movement or cover.

Future navmesh or encounter validation must be handled by a separate implementation task. This package only states scale and collision intent.

## Animation Notes

Static mesh baseline for gates, shelters, platforms, forge props, cooking props, dressing racks, paths, barricades, banners, and clutter.

Approval-gated future options:

- Simple banner wind material or cloth simulation.
- Forge ember material state, cooking-fire material state, or smoke VFX.
- Gate open/close animation.
- Hanging prop sway.

None of those are authorized by this package. No animation timing, cloth simulation, VFX graph, Blueprint behavior, AI encounter behavior, loot behavior, resource behavior, or crafting behavior is defined here.

## Unreal Import Notes

Planned folders:

- Structures: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/`
- Props: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Props/`
- Ground: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Ground/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/`

Planned naming:

- `KIT_GIA_BloodAxeCamp_A01`
- `SM_GIA_BloodAxeCampGate_A01`
- `SM_GIA_BloodAxeTrophyGate_A01`
- `SM_GIA_BloodAxeShelter_A01`
- `SM_GIA_BloodAxeShamanHut_A01`
- `SM_GIA_BloodAxeWatchPlatform_A01`
- `SM_GIA_BloodAxeForgeZone_A01`
- `SM_GIA_BloodAxeCookingPit_A01`
- `SM_GIA_BloodAxeDressingRack_A01`
- `SM_GIA_BloodAxePackedEarthPath_A01`
- `SM_GIA_BloodAxeStakeBarricade_A01`
- `KIT_GIA_BloodAxeCampClutter_A01`

Pivot rules:

- Gates, barricades, watch platforms, forge zones, cooking pits, dressing zones, and clutter clusters: pivot at ground center.
- Modular wall, path, and barricade segments: pivot at snap edge or segment origin, with grid-friendly dimensions.
- Shelters: pivot at front-center ground or center ground depending on placement use; document which variant is chosen before DCC.
- Banners and warning poles: pivot at pole base.
- Hanging props: pivot at hang point if authored as separate child meshes.

Scale: centimeter-authored, Unreal import scale 1.0 after future DCC/export rules are approved. Validate all large clearances against 442 cm female and 470 cm male Giant baselines before any visual approval.

Sockets and markers, if later needed:

- `banner_socket`
- `hanging_trophy_socket`
- `torch_socket`
- `gate_chain_socket`
- `forge_tool_socket`
- `watch_signal_socket`

These are visual attachment markers only unless a future gameplay task explicitly approves interaction behavior.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/`
- Kit package: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md`
- Future child package docs can be split under `docs/assets/props/` for single static meshes or `docs/assets/kits/` for multi-prop zones.
- Recommended child prefixes: `SM_GIA_BloodAxe...` for static meshes, `KIT_GIA_BloodAxe...` for grouped camp mini-kits, `MI_GIA_BloodAxe...` for material instances, and `T_GIA_BloodAxe...` for textures.

Do not add SourceAssets, DCC files, FBX exports, Unreal Content assets, runtime source, validators, startup-scene actors, external concept copies, global index edits, or task-board edits from this task packet.

## Approval Gates and Stop Points

- Stop before final camp visual approval, hero camp composition approval, or first playable visual signoff.
- Stop before selecting any first DCC target from the camp children.
- Stop before creating source folders, Blender files, proof renders, FBX exports, Unreal imports, material graphs, Blueprints, validators, or startup placements.
- Stop before defining encounter behavior, patrol behavior, AI cover, damage volumes, gate interactions, loot, resource collection, crafting, salvage, cooking, vendor, economy, destructible, or pickup behavior.
- Stop before copying, embedding, moving, cropping, editing, or committing external source concepts.
- Stop if Blood Axe red-black raider language starts replacing neutral/civilized Giant culture.
- Stop if any child asset appears to require changing the validated Giant scale lock.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5".
- Camp gates, shelters, watch points, forge/cooking/dressing zones, banners, paths, barricades, and clutter are split for planning.
- Primary silhouettes are readable at MMO camera distance.
- Materials use raw timber, hide, blackened iron, stolen scrap, bone/horn markers, soot, ash, packed earth, and red cloth consistently.
- Tiny lashings, scratches, rope fibers, wood grain, stitch detail, ash flecks, and grime are assigned to textures or normals instead of geometry.
- Emissive use is absent by default and limited to later-approved fire, forge, lamp, or shamanic variants.
- Triangle budgets, material slot targets, texture maps, LODs, collision, pivots, scale, sockets, and Unreal path planning are included.
- Source concepts remain external and are not copied, moved, edited, embedded, or committed.
- Package makes no DCC, FBX, Unreal Content, runtime, validator, startup-scene, global-index, encounter, loot, resource, crafting, economy, or final visual approval claim.
