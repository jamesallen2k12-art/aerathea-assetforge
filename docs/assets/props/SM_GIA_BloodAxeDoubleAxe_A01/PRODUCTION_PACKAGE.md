# SM_GIA_BloodAxeDoubleAxe_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeDoubleAxe_A01`
- Asset type: Static Mesh production package / Giant two-handed hero weapon
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source child ID: `BloodAxeArmory.png#Weapon_DoubleAxe`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Package status: docs-only production package

`SM_GIA_BloodAxeDoubleAxe_A01` is the primary hero two-handed Blood Axe weapon: a huge double-headed raider axe built from blackened stolen metal, rough reforged plates, heavy haft wrapping, red war paint, and controlled trophy accents. It should read instantly at MMO camera distance as the signature melee weapon of Blood Axe Giant raiders and chieftains.

The Blood Axe Tribe must remain a hostile Giant sub-faction separate from neutral/civilized Giant culture. This weapon uses brutal raider language, not the blue-gray stoneworker, cave-town, hearth, and restrained rune language reserved for neutral or civilized Giants.

This package is documentation only. It does not create, copy, move, embed, or commit source concepts, DCC files, FBX exports, Unreal Content assets, runtime source, startup-scene actors, or final visual approvals.

## Gameplay Purpose

The double axe establishes the high-value melee silhouette for Blood Axe Giant combatants. It supports future raider captain, chieftain, boss, elite guard, armory rack, and loot-display use without defining combat damage, trace timing, loot economy, or encounter behavior.

Expected gameplay roles:

- Primary equipped two-handed weapon for Blood Axe Giant elite variants.
- Hero prop for Blood Axe armory racks, forge-camp displays, and boss staging.
- Readable long-arc attack silhouette for future animation and combat packages.
- Back-carried weapon silhouette for patrols, camp guards, and encounter introductions.
- Optional non-combat display or pickup prop after later implementation approval.

The asset is not a default Giant weapon. Neutral/civilized Giant packages should continue to use mountain, stoneworker, tool, guardian, or shamanic visual language unless a separate stolen or captured variant is approved.

## Silhouette Notes

Primary read: a towering double axe with broad opposing blade masses, a thick central head block, heavy socket collars, a long wrapped haft, and a blunt or spiked end cap. The design should feel too massive for normal humanoids but practical for Giant hands.

Key silhouette requirements:

- Two broad axe blades form the main shape; the blade span must be readable before small chips or trophies.
- Head block should feel reforged and brutal, with large hammered plates rather than precise ornamental smithing.
- Haft must be thick enough for Giant grip and long enough for two-handed swing arcs.
- Grip zones should be visibly separated for dominant-hand and offhand placement.
- Large blade notches and chipped edges are acceptable, but the cutting profile must remain clear.
- Red cloth strips or paint marks should identify Blood Axe allegiance without covering the full shape.
- Bone or skull trophies may appear as one or two large accents only; avoid dense trophy clutter.

Model as real geometry:

- Blade slabs, central head mass, socket rings, reinforced bands, haft, major wraps, large chips, end cap, and one or two big trophy attachments.

Fake with texture, normals, or baked detail:

- Tiny scratches, hammered pitting, small rivets, leather pores, stitch lines, dried grime, minor blade nicks, small chips, and fine wrap fibers.

## Scale Notes

Giant scale lock: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

Scale rules:

- Author in centimeters. 1 Unreal unit = 1 cm.
- Primary fit target: male Giant baseline at 470 cm / 15'5".
- Secondary fit target: female Giant baseline at 442 cm / 14'6".
- Normal humanoid compatibility is not required unless a future loot-display task requests a scaled-down trophy variant.
- Grip spacing must align to `SK_GIA_Base_A01` two-handed sockets before any future implementation.

Suggested production dimensions:

- Total length: 390-430 cm.
- Blade span across widest opposing edges: 165-210 cm.
- Blade height per side: 115-155 cm.
- Central head block width along haft: 45-70 cm.
- Haft diameter: 10-16 cm through grip areas.
- Dominant-hand grip zone: 55-75 cm usable length.
- Offhand grip zone: 55-75 cm usable length.
- Clearance from lower grip to end cap: 70-110 cm for back carry and ground silhouette.

Scale validation targets for future work:

- Weapon must clear Giant shoulders, hips, knees, and back when carried on `back_large_weapon`.
- Two-handed grip must preserve readable Giant hand separation and not force crossed wrists.
- Blade span must not clip the ground during idle carry unless an intentional drag variant is separately approved.
- Armory display variant may use a separate floor/rack placement pivot, but the equipped mesh should stay grip-authored.

## Materials And Color Palette

Primary materials:

- Blackened iron and dark steel.
- Reforged stolen metal plates with broad hammer marks.
- Scorched leather and hide wraps.
- Dark wood or ironwood haft core, mostly hidden by wraps and bands.
- Torn red cloth, red war paint, and red-stained identification marks.
- Bone, horn, large teeth, or skull trophy accents used sparingly.
- Soot, ash, oil-dark grime, and worn bright metal only on major cutting edges.

Palette targets:

- Dominant: blackened iron, charcoal steel, dark brown leather, soot gray.
- Accent: desaturated Blood Axe red on paint, cloth, or blade marks.
- Secondary: bone off-white, dull brass/copper repair pins only if needed.
- Edge highlight: cold worn steel along the cutting edge and exposed chips.

Do not use civilized Giant blue-gray stoneworker material language, warm hearth identity, restrained blue rune accents, or neutral cave-town ornamentation. Emissive is not part of the baseline double axe. If a later ritual, shamanic, or boss variant needs glow, it requires a separate approval gate.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeDoubleAxe_A01` for the world of Aerathea. The design should emphasize a colossal double-headed two-handed axe silhouette, broad opposing blackened-iron blades, a heavy reforged central head block, thick wrapped haft, scorched leather, red Blood Axe paint and cloth accents, sparse bone trophy details, soot-dark raider material language, hostile Giant sub-faction identity, and the gameplay role of a primary hero melee weapon for Blood Axe Giant elites. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no baseline emissive effects, and MMO-friendly production design. Present it as a weapon concept sheet with front, side, back, grip close-up, blade material callouts, trace socket callouts, back-carry scale callout, and scale comparison against a 442 cm female Giant and a 470 cm male Giant on a clean background. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid readable text, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Future modeling should build the double axe as a single static mesh with clear equipped-weapon proportions first, then derive any display variant later only if approved.

Required modeled forms:

- Two large opposing blade slabs with thick bevels and readable cutting edges.
- Central reinforced head block tying both blades to the haft.
- Large socket collar and metal bands around the haft.
- Long haft with slightly uneven, hand-forged mass rather than a perfect cylinder.
- Two separated Giant grip zones with broad leather or hide wrapping.
- End cap, blunt pommel, or heavy spike that balances the silhouette.
- A few large blade chips or break points that do not destroy the main outline.
- One or two large trophy or cloth accents attached securely to the head or lower haft.

Simplification rules:

- Keep the head mass chunky and legible; avoid lace-like cutouts or fragile fantasy filigree.
- Use asymmetry in blade scars, paint, and repairs, but keep the double-axe read balanced.
- Make red cloth strips large and limited; do not add many thin dangling pieces.
- Avoid dense skull clusters, graphic gore, tiny chains, and excessive rivets.
- Do not model small hammered pits, scratches, fibers, stitch holes, or tiny metal flakes.

Production variants that may be requested later:

- Equipped grip-pivot variant.
- Armory rack display variant.
- Back-carry preview variant.
- Boss/chieftain material variant.

Those variants are not created by this docs-only package.

## Texture And Material Notes

Texture deliverables:

- `T_GIA_BloodAxeDoubleAxe_A01_BC`
- `T_GIA_BloodAxeDoubleAxe_A01_N`
- `T_GIA_BloodAxeDoubleAxe_A01_ORM`

Optional texture deliverables only after later approval:

- `T_GIA_BloodAxeDoubleAxe_A01_E` for an approved ritual, shamanic, or boss-state variant.
- `T_GIA_BloodAxeDoubleAxe_A01_Mask` if red paint, edge wear, or grime needs runtime tint control.

Material instance targets:

- `MI_GIA_BloodAxeDoubleAxe_A01`
- Optional shared-family references: `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeBlackenedIron_A01`, `MI_GIA_BloodAxeScorchedLeather_A01`, `MI_GIA_BloodAxeRedCloth_A01`, `MI_GIA_BloodAxeBoneTrophy_A01`

Material slot target:

- Preferred: 1 material slot using an atlas for metal, haft, leather, cloth, and trophy accents.
- Acceptable hero setup: 2 material slots maximum, with slot 0 for metal/head/blades and slot 1 for haft/leather/cloth/bone.
- Do not create separate material slots for every wrap, trophy, blade chip, paint mark, or grime layer.

Texture treatment:

- Base Color: blackened metal, dark leather, red paint/cloth, bone accents, soot, and exposed worn cutting edges.
- Normal: large hammer marks, blade bevel detail, leather wrap ridges, wood grain, shallow cracks, and major dents.
- ORM: strong roughness variation for soot, polished edge wear, dark oiled haft, and worn leather; metallic only for metal zones.
- Emissive: absent by default.

## Triangle Budget

`SM_GIA_BloodAxeDoubleAxe_A01` is a large hero weapon prop. It should be high enough quality for close camera inspection but still MMO-safe.

Targets:

- LOD0 target: 7k-9k tris.
- LOD0 hard cap: 10k tris.
- Material slots: 1 preferred, 2 maximum.
- Texture set: 2K target for hero/equipped use; 1K acceptable for lower-priority display variants.

Triangle allocation guidance:

- Blade/head assembly: 45-55 percent.
- Haft, collars, wraps, and end cap: 25-35 percent.
- Large chips, trophies, cloth, and asymmetry: 10-20 percent.
- Small bevel support and smoothing: remaining budget only after silhouette is locked.

Avoid spending triangles on tiny rivets, dense chain, thread, pitting, small scratches, or surface noise.

## LOD Plan

All important versions need LOD0-LOD3.

- LOD0: 7k-9k tris, hard cap 10k. Full silhouette, blade bevels, large chips, central head block, collars, grip wraps, end cap, and limited trophy/cloth accents.
- LOD1: 4k-5.5k tris. Reduce blade bevel loops, simplify collar bands, merge minor chip cuts, reduce cloth folds, and simplify trophy attachment geometry.
- LOD2: 2k-3k tris. Preserve the double-blade outline, head block, haft length, and red color blocks; flatten secondary chips, simplify wraps, and remove backside underside detail.
- LOD3: 900-1.5k tris. Preserve primary double-axe silhouette, broad blade span, haft length, and major Blood Axe color read; use simple geometry and baked texture detail.

LOD reduction order:

1. Tiny rivets, scratches, pitting, stitch detail, and small wrap ridges.
2. Minor blade nicks and secondary chipped cuts.
3. Small straps, cloth frays, and trophy attachment details.
4. Collar bevel loops and backside metal undercuts.
5. End cap bevels and grip subdivisions.
6. Only then reduce the broad blade outline, head block, and haft silhouette.

Never destroy the opposing blade read or Giant-scale length before removing small decoration.

## Collision Notes

Equipped weapon baseline:

- Collision disabled for equipped combat use.
- Future combat should use socket-driven traces rather than blade mesh collision.
- Planned trace sockets: `weapon_trace_start`, `weapon_trace_mid`, `weapon_trace_end`.
- Planned grip sockets/markers: `hand_r_weapon`, `hand_r_twohand_grip`, `hand_l_twohand_grip`.
- Planned carry socket alignment: `back_large_weapon`.

Display or pickup collision:

- Use simple box or capsule collision around the haft and head for non-combat display.
- Use 1-3 low-count convex hulls only if a rack or pickup pose needs more accurate bounds.
- Do not use per-blade complex collision for gameplay.
- Do not add collision to cloth strips, tiny trophies, or minor chips.

Collision approval guardrails:

- Any damage arcs, hit timing, stagger behavior, or boss-specific hit shapes require gameplay approval.
- Character collision remains controlled by the Giant character physics/capsule setup, not this prop.

## Animation Notes

Baseline asset is a static mesh. No animations are authored or claimed by this package.

Future animation compatibility targets:

- Two-handed idle hold.
- Two-handed walk/run carry.
- Back carry and unsheathe/sheath.
- Heavy windup.
- Horizontal cleave.
- Overhead chop.
- Diagonal swing.
- Ground impact.
- Hit reaction carry preservation.
- Death/drop placement.

Animation fit notes:

- Grip spacing must support the Giant base hand sockets without crossed wrists.
- Blade span must leave clear readable telegraph arcs for future attack animation.
- Back-carry orientation must avoid clipping the head, shoulder, hip, and ground at the approved Giant baselines.
- Cloth/trophy accents should be static by default; any secondary motion requires later implementation approval.

## Unreal Import Notes

These are future import planning notes only. This docs-only package does not create or import Unreal assets.

Planned Unreal asset:

- Static Mesh: `SM_GIA_BloodAxeDoubleAxe_A01`
- Planned folder: `/Game/Aerathea/Weapons/Giants/BloodAxe/`
- Planned material instance: `MI_GIA_BloodAxeDoubleAxe_A01`
- Planned material folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Planned texture folder: `/Game/Aerathea/Textures/Giants/BloodAxe/Weapons/DoubleAxe_A01/`

Import settings:

- Scale: authored in centimeters; Unreal import scale 1.0 after future DCC/export approval.
- Pivot: dominant-hand grip center for equipped version.
- Forward axis: align with the project weapon convention during future implementation review.
- Collision: no equipped combat collision; simple display collision only.
- LODs: import LOD0-LOD3.
- Nanite: off by default for equipped character weapon unless a later performance review approves a display-only Nanite variant.
- Material slots: 1 preferred, 2 maximum.

Socket and marker planning:

- `hand_r_weapon`
- `hand_r_twohand_grip`
- `hand_l_twohand_grip`
- `back_large_weapon`
- `weapon_trace_start`
- `weapon_trace_mid`
- `weapon_trace_end`

Blueprint behavior:

- None in this package.
- Future interactive pickup, equip, rack display, combat trace, VFX, sound, or loot behavior requires a separate gameplay or implementation task.

Performance notes:

- Preserve primary silhouette and reduce small surface decoration first.
- Keep material slots low for large warband encounters.
- Avoid baseline emissive, particle, or dynamic light dependencies.
- Validate at Giant scale and normal player camera distance before final visual approval.

## Folder And Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeDoubleAxe_A01/PRODUCTION_PACKAGE.md`

Planned future Unreal Content paths after approval:

- `/Game/Aerathea/Weapons/Giants/BloodAxe/SM_GIA_BloodAxeDoubleAxe_A01`
- `/Game/Aerathea/Materials/Giants/BloodAxe/MI_GIA_BloodAxeDoubleAxe_A01`
- `/Game/Aerathea/Textures/Giants/BloodAxe/Weapons/DoubleAxe_A01/T_GIA_BloodAxeDoubleAxe_A01_BC`
- `/Game/Aerathea/Textures/Giants/BloodAxe/Weapons/DoubleAxe_A01/T_GIA_BloodAxeDoubleAxe_A01_N`
- `/Game/Aerathea/Textures/Giants/BloodAxe/Weapons/DoubleAxe_A01/T_GIA_BloodAxeDoubleAxe_A01_ORM`

Naming:

- Static Mesh: `SM_GIA_BloodAxeDoubleAxe_A01`
- Material Instance: `MI_GIA_BloodAxeDoubleAxe_A01`
- Base Color: `T_GIA_BloodAxeDoubleAxe_A01_BC`
- Normal: `T_GIA_BloodAxeDoubleAxe_A01_N`
- Packed ORM: `T_GIA_BloodAxeDoubleAxe_A01_ORM`
- Optional approved emissive: `T_GIA_BloodAxeDoubleAxe_A01_E`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, external source concept copies, startup-scene placement, or global index entries from this task.

## Approval Gates

- Stop before DCC source creation, FBX export, Unreal Content import, runtime source, startup placement, or final visual approval.
- Stop before copying, moving, embedding, editing, or committing `BloodAxeArmory.png` or any external source concept.
- Stop if the Blood Axe look starts replacing neutral/civilized Giant culture instead of remaining a hostile sub-faction.
- Stop before adding graphic gore, dense skull clutter, excessive chains, tiny rivet fields, or unbuildable micro-detail.
- Stop if the weapon appears to require a different Giant scale lock or socket contract from `SK_GIA_Base_A01`.
- Visual approval is required before locking final blade shape, trophy density, paint placement, and chieftain/boss variants.
- Gameplay approval is required before combat traces, damage arcs, hit timing, equipping behavior, loot rules, or pickup interactions are authored.
- Implementation approval is required before any DCC, export, Unreal import, material asset, Blueprint, or validation script work.

## Quality Gate Checklist

- `SM_GIA_BloodAxeDoubleAxe_A01` is documented as the primary hero two-handed Blood Axe weapon.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- The package is docs-only and makes no DCC, FBX, Unreal Content, runtime source, startup placement, source concept copying, or final visual approval claim.
- Silhouette is readable at MMO camera distance: broad opposing blades, heavy head block, long haft, and Giant two-handed grip.
- Materials follow Blood Axe language: blackened iron, dark steel, reforged scrap, scorched leather, red paint/cloth, soot, grime, and sparse bone trophy accents.
- Civilized Giant stoneworker materials, blue-gray cave-town identity, warm hearth language, and restrained blue rune accents are excluded from the baseline.
- Emissive is absent by default and approval-gated for any later ritual, shamanic, or boss variant.
- Large forms are assigned to geometry; tiny scratches, rivets, pitting, stitch detail, and minor chips are assigned to textures or normals.
- Texture maps include `BC`, `N`, and packed `ORM`; optional `E` is approval-gated.
- Triangle budget, material slot target, LOD0-LOD3 plan, collision plan, sockets, animation compatibility, and future Unreal import planning are included.
- Collision stays simple, with equipped combat intended for socket traces rather than per-blade mesh collision.
- Approval gates protect culture separation, source-storage rules, gameplay scope, implementation scope, and performance readability.
