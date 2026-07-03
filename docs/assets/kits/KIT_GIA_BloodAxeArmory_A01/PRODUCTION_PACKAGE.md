# KIT_GIA_BloodAxeArmory_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeArmory_A01`
- Asset type: Production kit / multi-asset armory set
- Source concept: `BloodAxeArmory.png`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Priority children: `SM_GIA_BloodAxeDoubleAxe_A01`, `SM_GIA_BloodAxeCrusherHammer_A01`, `KIT_GIA_BloodAxeQuivers_A01`, `SM_GIA_BloodAxeLongbow_A01`, `SK_GIA_BloodAxeRaiderChest_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`
- Status: docs-only kit production package ready
- Source-storage guardrail: keep the source concept in `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/`; do not copy, move, edit, embed, or commit it as part of this package.

Blood Axe armory language for hostile Giant raiders: huge stolen-metal weapons, brutal reforged plates, bowyer craft adapted to Giant reach, trophy armor, red cloth warnings, soot-dark iron, rough leather, chains, skull trophies, and forge-camp utility. This kit must stay separate from neutral/civilized Giant stoneworker culture. It represents a feared raider sub-faction, not the default identity of Giants in Aerathea.

## Gameplay Purpose

Supports Blood Axe Giant raiders, chieftains, hunters, bowyers, camp guards, loot silhouettes, armory dressing, future warband packages, and forge/camp environment adjuncts. The kit establishes attachment rules for Giant-scale melee weapons, bows, quivers, trophy armor, banners, and reforged-metal material variants.

Expected use cases:

- Equipped Giant weapons for melee and bow combat packages.
- Wearable armor modules for Blood Axe raider and chieftain variants.
- Camp and armory set dressing: racks, scrap piles, forge stock, banners, quivers, bow parts, and bowyer tools.
- Loot/display variants that can be shown in a Giant camp without implying normal humanoid scale.

## Silhouette Notes

Blood Axe silhouettes should be large, top-heavy, jagged, and hostile, but still readable at MMO camera distance. The primary read comes from broad axe blades, slab cleaver mass, hammer block shape, hooked spear heads, oversized bow arcs, huge quiver cylinders, trophy helm outline, shoulder plates, tassets, greaves, and red banner shapes.

Keep the visual noise under control:

- Model the main weapon heads, armor plates, quiver bodies, bow staves, thick chains, large trophies, broad leather straps, and major spikes.
- Paint or normal-map small scratches, tiny rivets, dense chain clutter, pitting, grime, stitching, nicks, and metal hammer marks.
- Reduce skull/trophy repetition so each item reads as Blood Axe without becoming unreadable.
- Keep red cloth and paint as hostile sub-faction accents, not a full one-color palette.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Feet, hand, back, belt, head, torso, pelvis, thigh, and foot clearances must be checked against the Giant base before any future DCC work.

Suggested scale ranges:

- Double axe: 360-430 cm total length; head width 150-210 cm.
- Cleaver: 220-280 cm total length; blade length 110-160 cm.
- Crusher hammer: 300-380 cm total length; head width 90-140 cm.
- Hook spear: 420-560 cm total length.
- Giant knife: 130-180 cm total length.
- Longbow: 360-460 cm unstrung height; draw length must be checked against shoulder, elbow, and hand sockets.
- Shortbow variants: 240-330 cm.
- Quivers: 120-180 cm tall, sized for Giant arrows.
- Trophy helm and face guard: sized for Giant head/neck, with visibility and jaw motion preserved.
- Chest/spaulder module: sized for Giant torso and shoulder width without hiding the base race mass.
- Greaves/sabatons: sized around Giant calf, ankle, and foot proportions.

Socket planning should align with the Giant base package:

- `hand_r_weapon`
- `hand_l_offhand`
- `hand_r_twohand_grip`
- `hand_l_twohand_grip`
- `back_large_weapon`
- `back_shield`
- `belt_tool_l`
- `belt_tool_r`
- `head_hair_ornament`
- `chest_talisman`
- Future Blood Axe additions: `back_quiver`, `bow_grip_l`, `bow_string_pull_r`, `arrow_nock`, `belt_trophy`, `banner_carry`, `weapon_trace_start`, `weapon_trace_end`

## Materials And Color Palette

Primary materials:

- Blackened iron and dark steel.
- Reforged scrap plates with broad hammer marks.
- Scorched leather, hide, fur, sinew, and wrapped cord.
- Bone, horn, skull trophies, and large teeth or claws used sparingly.
- Torn red cloth, red war paint, and dried grime as Blood Axe identifiers.
- Forge soot, ash, charcoal, dull warm ember reflections, and oil-dark metal.

Avoid civilized Giant blue-gray stoneworker language in this kit. Neutral Giant materials such as carved blue-gray stone, warm hearth light, and restrained blue runes belong to other Giant packages unless a specific Blood Axe stolen-object variant is approved later.

Emissive use is normally not needed. If a future shamanic Blood Axe variant needs storm or ritual glow, it must be approved as a separate variant and remain restrained.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeArmory_A01` for the world of Aerathea. The design should emphasize hostile Giant raider silhouettes, enormous reforged axes, cleavers, war hammers, hook spears, giant bows, quivers, bowyer tools, trophy armor, red warning cloth, blackened iron, dark steel, scorched leather, bone trophies, soot, rough camp-forge materials, Blood Axe sub-faction identity, and gameplay roles for Giant raiders, hunters, chieftains, and bowyers. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a production armory catalog and child-asset board with scale callouts against a 442 cm female Giant and a 470 cm male Giant, plus socket notes for hands, back, belt, head, torso, and quiver attachments. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe language the default Giant culture, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This package is a planning document only. Future DCC work should model the big readable forms first:

- Double axe: broad blade slabs, central head block, thick socket ring, wrapped haft, end cap, large chips, and primary straps.
- Cleaver: slab blade, heavy spine, reinforced grip, broad chipped edge, and weighted pommel.
- Crusher hammer: block head, side plates, reinforced haft, major studs, and silhouette bevels.
- Hook spear: long shaft, hook blade, spear tip, grip wraps, and large binding rings.
- Knife: oversized sidearm blade, heavy handle, belt loop, and sheath option.
- Bows: stave curves, horn or metal caps, large grip wraps, string anchors, and draw readability.
- Quivers: cylinder or hide shell, top rim, arrow clusters, belt/back straps, major trophy tags, and display versions.
- Bowyer tools and parts: simple strong tool silhouettes, not dense workshop clutter.
- Trophy armor: torso plates, spaulders, helm/face guard, belts, tassets, greaves, sabatons, large chains, and large trophies.
- Banners and scrap piles: banner pole, cloth mass, scrap silhouettes, shield/plate chunks, ingots, and forge stock.

Texture or normal-map fine scratches, small rivets, dense metal pitting, tiny chain links, leather pores, soot streaks, stitch lines, and minor chips. The sheet has many tiny details; production versions must simplify them into a smaller number of bold, readable accents.

## Texture And Material Notes

Use `BC`, `N`, packed `ORM`, and optional `E` only for approved shamanic or forge-heat variants.

Shared material families:

- `MI_GIA_BloodAxeReforgedMetal_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeBoneTrophy_A01`
- `MI_GIA_BloodAxeSootAsh_A01`

Texture naming examples:

- `T_GIA_BloodAxeDoubleAxe_A01_BC`
- `T_GIA_BloodAxeDoubleAxe_A01_N`
- `T_GIA_BloodAxeDoubleAxe_A01_ORM`
- `T_GIA_BloodAxeRaiderChest_A01_BC`
- `T_GIA_BloodAxeRaiderChest_A01_N`
- `T_GIA_BloodAxeRaiderChest_A01_ORM`
- `T_GIA_BloodAxeForgeHeat_A01_E` only if a future forge-heat material state is approved

Weapons should usually use 1 material slot. Hero weapons may use 2 slots for metal/handle separation. Armor modules should target 2-3 material slots across metal, leather/cloth, and bone/trophy parts. Avoid one-off material slots for every strap or trophy.

## Triangle Budget

Target ranges for future child packages:

- Giant knives and small bowyer tools: 800-3k tris.
- Cleavers, hook spear heads, and simple bows: 2k-6k tris.
- Double axe and crusher hammer: 5k-10k tris.
- Hero longbow with trophies: 4k-8k tris.
- Quiver with arrows: 3k-8k tris depending on arrow count and display state.
- Trophy helm: 3k-7k tris.
- Chest/spaulder, belt/tasset, and greave modules: 5k-12k tris per major wearable module.
- Scrap pile or armory dressing cluster: 8k-18k tris, with modular subpieces preferred.
- Full kit display layout: keep under 55k tris for a composed preview scene by using repeated child meshes and simplified far props.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full primary silhouette, large blades/plates, grip wraps, big chains, major trophies, major chips, straps, bow curves, quiver shapes, and banner cloth.
- LOD1: 60-70 percent of LOD0; reduce minor chips, small straps, small chain segments, dense arrow tips, secondary cloth tears, and inner armor details.
- LOD2: 35-45 percent of LOD0; simplify trophy clusters, quiver interiors, blade bevels, back-side armor, tiny bindings, and tool handles.
- LOD3: 15-25 percent of LOD0; preserve axe/hammer/bow/armor/banner silhouette and major Blood Axe color blocks.

Remove tiny rivets, scratches, chain clutter, minor straps, and back-side dressing before reducing the big weapon heads, bow arcs, trophy helm shape, shoulder line, or banner outline.

## Collision Notes

Equipped weapons should have collision disabled by default and rely on combat traces from sockets such as `weapon_trace_start` and `weapon_trace_end`. World pickup or display variants use simple capsules, boxes, or low-count convex hulls.

Suggested collision:

- Double axe, cleaver, hammer, hook spear, and knife: simple capsule/box collision for pickup/display; trace sockets for combat.
- Bows: simple narrow box or capsule; no string collision.
- Quivers and arrows: one capsule or box around the quiver body; individual arrow collision disabled unless used as a projectile mesh.
- Trophy armor modules: attachment preview bounds only; character physics asset handles worn-body collision unless a boss mechanic requires a separate hit shape.
- Banner: simple pole capsule and cloth bounds; no per-strip collision.
- Scrap pile/display cluster: simplified convex hulls or grouped boxes, with walkable collision disabled unless promoted to environment cover.

## Animation Notes

Static mesh baseline for weapons, armor modules, quivers, banners, bowyer tools, and display props. Combat animation belongs to future Giant character and Blood Axe warband packages.

Future animation and attachment requirements:

- Two-handed axe and hammer grip alignment for idle, walk, run, windup, swing, impact, and back carry.
- Cleaver and knife one-handed grip alignment for belt carry and quick draw.
- Hook spear two-handed grip and reach-attack trace points.
- Bow grip, nock, draw, release, quiver reach, and arrow projectile socket rules.
- Trophy armor must clear shoulders, elbows, pelvis, thighs, knees, and ankles during the Giant base locomotion set.
- Banner may support later idle cloth simulation or a simple wind material state, but that is outside this docs-only package.

## Unreal Import Notes

Planned folders:

- Weapons: `/Game/Aerathea/Weapons/Giants/BloodAxe/`
- Gear: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`
- Props: `/Game/Aerathea/Props/Giants/BloodAxeArmory/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned naming:

- `SM_GIA_BloodAxeDoubleAxe_A01`
- `SM_GIA_BloodAxeCleaver_A01`
- `SM_GIA_BloodAxeCrusherHammer_A01`
- `SM_GIA_BloodAxeHookSpear_A01`
- `SM_GIA_BloodAxeSkinningKnife_A01`
- `SM_GIA_BloodAxeLongbow_A01`
- `KIT_GIA_BloodAxeQuivers_A01`
- `SK_GIA_BloodAxeRaiderChest_A01`
- `SK_GIA_BloodAxeTrophyHelm_A01`
- `MI_GIA_BloodAxeReforgedMetal_A01`

Pivot rules:

- Melee weapons: pivot at primary grip center unless a display-only variant needs floor placement.
- Two-handed weapons: include offhand grip marker and trace start/end markers.
- Bows: pivot at bow grip; include nock/draw reference markers.
- Quivers: pivot at back or belt attachment point depending on variant.
- Armor modules: pivot to the matching Giant skeleton attachment or body origin for skeletal clothing modules.
- Banners: pivot at pole base for world placement; separate carried banner variant if needed.
- Scrap piles: pivot at ground center.

Scale: centimeter authored; future Unreal import should use scale 1.0 after DCC/export rules are defined in a future task. Validate against the Giant base baselines before any visual approval.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/CHILD_ASSET_INTAKE.md`
- Kit package: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- Future child packages: `docs/assets/props/SM_GIA_BloodAxeDoubleAxe_A01/`, `docs/assets/props/SM_GIA_BloodAxeCrusherHammer_A01/`, `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/`, `docs/assets/characters/SK_GIA_BloodAxeRaiderChest_A01/`, `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, or global index entries from this task packet.

## Approval Gates

- DCC build promotion is required before any mesh source, FBX export, material asset, Unreal Content asset, or startup placement work.
- Visual approval is required before final Blood Axe hero silhouette, trophy density, gore limit, or chieftain variant language is locked.
- Giant scale/socket approval remains inherited from `SK_GIA_Base_A01`; stop if a child asset appears to require a different base scale or socket contract.
- Source-storage approval is required before any source concept image is copied into the repository.
- Gameplay approval is required before combat traces, damage arcs, bow projectile behavior, loot rules, or interactive forge behavior are authored.
- Culture approval is required if Blood Axe material language starts bleeding into neutral/civilized Giant cave-town or nomad packages.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", with approved Giant ranges documented.
- Child asset IDs cover axes, cleaver, hammer, spear, knife, bows, quivers, bow parts, bowyer tools, trophy armor, banner, reforged material language, and forge/camp references.
- Weapons and armor are buildable as mid-poly MMO assets with readable primary silhouettes.
- Materials use blackened iron, dark steel, scorched leather, hide/fur, bone trophies, red cloth, soot, and rough reforged-metal surfaces consistently.
- Tiny rivets, scratches, chain clutter, pitting, stitching, and dense trophy detail are assigned to textures or normals instead of geometry.
- Emissive use is absent by default and approval-gated for shamanic or forge-heat variants.
- Triangle budgets, texture maps, material slot targets, LODs, collision, sockets, animation notes, and Unreal path planning are included.
- Source concept remains external and is not copied, moved, edited, embedded, or committed by this package.
- Package makes no DCC, FBX, Unreal Content, runtime, source asset, global index, or startup-scene work claim.
