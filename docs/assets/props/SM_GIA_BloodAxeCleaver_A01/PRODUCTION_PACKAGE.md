# SM_GIA_BloodAxeCleaver_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeCleaver_A01`
- Asset type: Static Mesh weapon prop production package
- Source kit: `KIT_GIA_BloodAxeArmory_A01`
- Source concept reference: `BloodAxeArmory.png#Weapon_GiantCleaver`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Source-storage guardrail: keep `BloodAxeArmory.png` in the external source concept folder only. Do not copy, move, edit, embed, or commit the source image for this package.

`SM_GIA_BloodAxeCleaver_A01` is a brutal Giant sidearm/offhand slab weapon for Blood Axe raiders. It should read as a huge hacked-down cleaver made from stolen and reforged metal, not a normal humanoid sword. The visual identity is hostile, practical, and intimidating: broad blade mass, blackened iron, chipped red war paint, rough Giant-scale grip wrapping, soot, dents, and a few large trophy or binding accents. Blood Axe visual language must remain a hostile Giant sub-faction treatment and must not replace neutral/civilized Giant stoneworker culture.

This package is a planning document only. It does not create DCC source, FBX exports, Unreal Content assets, runtime source, startup-scene placement, final visual approval, or combat behavior.

## Gameplay Purpose

The cleaver supports Blood Axe Giant raider identity as a close-range sidearm, offhand weapon, camp armory display prop, and loot silhouette reference. Its purpose is to make a Blood Axe Giant feel equipped with rough field-forged war gear that is oversized even by normal MMORPG weapon standards because it is fitted to Giant hands.

Expected use cases:

- Equipped sidearm/offhand planning for future Blood Axe Giant raider variants.
- Camp armory rack, forge stock, or ground-display prop planning.
- Loot-display silhouette that remains Giant-scaled unless a future task approves a separate small-folk trophy variant.
- Material and scale reference for future Blood Axe weapon-family consistency.

This document does not define attack arcs, damage values, combo timing, hit reactions, loot rules, interactable pickup behavior, or runtime Blueprint behavior.

## Silhouette Notes

The primary silhouette is a thick slab cleaver: short for a Giant weapon, enormous beside normal humanoids, and visibly heavier than a sword. The blade should feel like a chopped section of reforged plate with a brutal cutting edge rather than an elegant forged sword profile.

Required silhouette reads:

- Broad rectangular or slightly forward-heavy blade mass with an uneven chopped edge.
- Heavy spine and thick blade bevels that imply weight.
- Short, oversized Giant grip suitable for one-handed or offhand use.
- Large socket collar, binding band, or clamp where blade meets handle.
- Weighted pommel or end cap that balances the slab blade.
- One or two large chips or notches that affect the outline, not dozens of tiny cuts.
- Optional torn red wrap, hide strip, or single trophy token, kept secondary to the blade mass.

Avoid:

- Long sword proportions, thin fantasy saber language, or normal humanoid hand scale.
- Dense toothy serrations, tiny rivet fields, gore decoration, or unreadable edge clutter.
- Neutral Giant blue-gray stoneworker motifs, hearth accents, or civilized masonry identity.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock. Giant scale lock: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

Author in centimeters. 1 Unreal unit = 1 cm.

Target physical planning dimensions:

- Total length: 230-270 cm.
- Blade length: 130-165 cm.
- Blade height at deepest point: 60-90 cm.
- Blade thickness at spine: 10-18 cm before bevel taper.
- Handle length: 85-115 cm, including pommel and collar.
- Grip diameter: 13-18 cm, tuned for Giant hand mass.
- Display clearance: should fit on a Giant weapon rack or ground display without implying a normal humanoid sword scale.

Attachment planning should align to existing Giant socket assumptions from `SK_GIA_Base_A01` and the Blood Axe armory kit:

- Primary equipped alignment: `hand_r_weapon`.
- Offhand alignment: `hand_l_offhand`.
- Carry/display alignment: `back_large_weapon` or a future Blood Axe belt/back carry marker if approved.
- Future trace references, if ever needed, must be approved separately and should not be authored by this docs-only package.

Normal humanoid compatibility is not required. If displayed beside a normal humanoid, it should read closer to a massive slab weapon or short barricade-sized blade, not a usable one-handed sword.

## Materials And Color Palette

Primary material language:

- Blackened iron and dark steel for the slab blade.
- Reforged scrap-metal planes with broad hammer marks and uneven plate tone.
- Chipped deep red war paint as the Blood Axe identifier.
- Scorched leather, rawhide, dark cord, or sinew for the Giant grip.
- Soot, ash, oil-dark grime, and worn steel edge highlights.
- Bone, horn, or tooth accents only as one restrained secondary token, not a clutter field.

Recommended palette:

- Blackened metal: `#151719` to `#2A2C2E`.
- Worn steel edge: `#555A5C` to `#787B78`.
- Deep red war paint: `#5F1513` to `#8B211B`.
- Soot and char: `#0B0A09` to `#24201C`.
- Dark leather wrap: `#2A1A12` to `#4A2F21`.
- Aged bone accent: `#8A7B61` to `#B5A37B`.

Do not use default emissive. Forge heat, shamanic glow, or animated material states require a separate approved variant and are not part of `SM_GIA_BloodAxeCleaver_A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeCleaver_A01` for the world of Aerathea. The design should emphasize a Giant sidearm/offhand slab weapon silhouette, a broad hacked reforged-metal cleaver blade, blackened iron, dark steel, chipped deep red Blood Axe war paint, scorched leather Giant grip wrapping, soot, grime, broad hammer marks, hostile Blood Axe raider sub-faction identity, separation from neutral/civilized Giant stoneworker culture, and a gameplay role as an oversized Giant sidearm rather than a normal humanoid sword. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive accents, and MMO-friendly production design. Present it as a clean weapon production sheet with front, side, back, grip close-up, material callouts, silhouette callouts, and scale callouts against the 442 cm female Giant and 470 cm male Giant baselines. Avoid copying any existing franchise, avoid graphic gore, avoid readable text, avoid dense tiny rivets or nicks, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This task does not create geometry. Future DCC work should model the large readable forms first:

- Slab blade body with thick spine, broad bevels, and visibly weighted mass.
- Major asymmetry in the blade outline, with a few large chips or breaks that affect the silhouette.
- Reinforced collar or socket block where blade meets handle.
- Oversized grip core sized for Giant fingers and palm width.
- Large leather or hide wrap bands with simple overlaps.
- Heavy pommel or counterweight that reads from MMO camera distance.
- Optional large clamp plate, ring, or single trophy tie that does not hide the cleaver read.

Texture or normal-map the fine detail:

- Fine scratches.
- Small hammer marks.
- Dense pitting.
- Tiny rivets.
- Minor edge nicks.
- Leather pores.
- Stitching and cord fibers.
- Soot speckles and grime streaks.

Keep the cleaver buildable as a mid-poly prop. Do not model a forest of tiny serrations, bolts, hanging strips, or trophy fragments. The blade mass, collar, grip, and pommel carry the design.

## Texture And Material Notes

Texture set target:

- `T_GIA_BloodAxeCleaver_A01_BC`
- `T_GIA_BloodAxeCleaver_A01_N`
- `T_GIA_BloodAxeCleaver_A01_ORM`
- No `E` texture by default

Material slot target:

- Preferred: 1 material slot using shared masks for metal, red paint, leather wrap, soot, and edge wear.
- Acceptable hero/display variant: 2 material slots, `MI_GIA_BloodAxeReforgedMetal_A01` for blade/collar and a leather/bone material for handle accents.

Material dependencies:

- Primary shared material language should follow `MI_GIA_BloodAxeReforgedMetal_A01`.
- Red paint must remain a restrained Blood Axe accent and should not cover most of the visible blade.
- Use broad value changes and large paint chips instead of high-frequency noise.
- ORM plan: R = ambient occlusion, G = roughness, B = metallic.
- `BC` uses sRGB; `N` and `ORM` use sRGB disabled in future import.

Recommended texture resolution:

- 2K for the primary production cleaver.
- 1K acceptable for distant rack/display variants.
- 4K only if a future named boss or hero close-up approval requires it.

## Triangle Budget

Target budget for future mesh work:

- LOD0: 3k-6k tris.
- Material slots: 1 preferred, 2 maximum for hero/display separation.
- Texture set: 1K-2K standard, 4K only with future hero approval.

Budget allocation:

- Blade body, bevels, and spine: 45-55 percent.
- Collar, clamp, and structural bands: 15-20 percent.
- Grip, wrap forms, and pommel: 20-25 percent.
- Optional trophy or cloth accent: 5 percent maximum.

Do not spend triangles on tiny scratches, small rivets, fine stitching, dense serrations, or repeated edge damage.

## LOD Plan

Create LOD0, LOD1, LOD2, and LOD3 for any future mesh.

- LOD0: full slab blade profile, thick spine, large bevels, major chips, collar, grip wrap, pommel, broad red paint masks, and major material separation.
- LOD1: 60-70 percent of LOD0; reduce small bevel segments, minor collar cuts, secondary wrap overlaps, tiny chips, and small accent pieces.
- LOD2: 35-45 percent of LOD0; simplify blade bevels, merge grip wrap forms, reduce pommel/collar loops, and remove optional trophy or cloth accents if they create noise.
- LOD3: 15-25 percent of LOD0; preserve the slab cleaver outline, handle block, Blood Axe red/black material read, and Giant-scale mass.

Reduction order:

1. Tiny nicks, small rivets, and stitch forms.
2. Minor wrap overlaps and small hanging strips.
3. Secondary bevel cuts and small clamp details.
4. Optional trophy token or small cloth pieces.
5. Back-side details.
6. Collar subdivisions.
7. Blade outline only after all secondary detail is reduced.

Never reduce the slab blade silhouette, Giant grip scale, or primary Blood Axe color blocks before removing small detail.

## Collision Notes

This package plans collision only; it does not create collision assets or gameplay hit behavior.

Future collision guidance:

- Equipped variant: collision disabled by default; character and future approved gameplay systems handle interaction separately.
- Display or pickup prop variant: one simple oriented box or low-count convex hull around the blade and handle.
- Rack variant: collision can be disabled if the rack or display actor owns collision.
- No per-chip, per-wrap, per-rivet, or per-trophy collision.
- No combat trace sockets, hitboxes, damage arcs, or weak-point zones are authored by this package.

If a future task approves combat traces, use separate marker planning and validate against Giant hand sockets, but keep that outside this docs-only package.

## Animation Notes

Static mesh baseline. `SM_GIA_BloodAxeCleaver_A01` has no authored animation, no cloth simulation, no material animation, no Blueprint behavior, and no combat timing in this package.

Future animation-adjacent requirements, if separately approved:

- Hand alignment checks for `hand_r_weapon` and `hand_l_offhand`.
- Carry alignment checks for back or side display without clipping Giant torso, hip, arm, or thigh volume.
- Optional sheath/rack placement review as a separate prop or encounter dressing task.

## Unreal Import Notes

Planned Unreal asset:

- Asset name: `SM_GIA_BloodAxeCleaver_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Weapons/Giants/BloodAxe/`
- Scale: centimeter-authored, future import at scale 1.0 after DCC/export rules are approved.
- Pivot: primary Giant grip center for equipped planning; a separate display-only variant may use a ground or rack pivot if approved later.
- Orientation: blade forward/up according to the project weapon convention established during future DCC handoff.
- Collision: simple display collision only if needed; equipped collision disabled by default.
- LODs: import LOD0-LOD3 when mesh work is promoted.
- Material slots: 1 preferred, 2 maximum.
- Texture list: `T_GIA_BloodAxeCleaver_A01_BC`, `T_GIA_BloodAxeCleaver_A01_N`, `T_GIA_BloodAxeCleaver_A01_ORM`.
- Socket references: align to existing Giant `hand_r_weapon`, `hand_l_offhand`, and possible `back_large_weapon` carry planning; do not create or change sockets in this task.
- Performance notes: preserve readable slab silhouette at distance, keep red paint and metal value blocks broad, and avoid material-slot sprawl.

No Unreal Content assets, import scripts, validators, startup-scene actors, runtime classes, Blueprint Actors, or material graph changes are included in this package.

## Folder And Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeCleaver_A01/PRODUCTION_PACKAGE.md`

Planned Unreal path if promoted later:

- `/Game/Aerathea/Weapons/Giants/BloodAxe/SM_GIA_BloodAxeCleaver_A01`

Planned texture names if promoted later:

- `T_GIA_BloodAxeCleaver_A01_BC`
- `T_GIA_BloodAxeCleaver_A01_N`
- `T_GIA_BloodAxeCleaver_A01_ORM`

Planned material references:

- `MI_GIA_BloodAxeReforgedMetal_A01`
- Optional future handle/leather material only if material-slot approval allows a second slot

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, global index entries, or copied concept files from this task packet.

## Approval Gates

- Package approval is required before DCC source, FBX export, texture authoring, Unreal import, or startup placement work begins.
- Visual approval is required before locking final blade profile, chip count, trophy accent, red paint coverage, or hero/display variants.
- Giant scale approval remains inherited from `SK_GIA_Base_A01`; stop if the cleaver begins reading as a normal humanoid sword or if it no longer fits Giant hand/offhand assumptions.
- Culture approval is required if Blood Axe red-black raider language starts replacing neutral/civilized Giant stoneworker culture.
- Source-storage approval is required before copying, embedding, or committing `BloodAxeArmory.png` or any external source concept.
- Gameplay approval is required before defining combat traces, hitboxes, damage arcs, attack timing, loot behavior, pickup interaction, or Blueprint logic.
- Material approval is required before adding emissive, forge heat, shamanic glow, animated material states, or additional material slots.

## Quality Gate Checklist

- Package includes all universal Aerathea production sections plus approval gates.
- `SM_GIA_BloodAxeCleaver_A01` reads as a Giant sidearm/offhand slab weapon, not a normal humanoid sword.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Source concept remains external and is not copied, moved, edited, embedded, or committed.
- Silhouette is broad, brutal, readable, and mid-poly buildable.
- Materials align with blackened iron, dark steel, chipped red paint, scorched leather, soot, ash, and restrained bone/horn accents.
- Emissive use is absent by default and approval-gated for future variants.
- Tiny rivets, scratches, dense pitting, stitching, and minor nicks are assigned to textures or normal maps instead of geometry.
- Texture maps include `BC`, `N`, and packed `ORM`; no default `E` map is planned.
- Triangle budget, material slot target, LOD0-LOD3 plan, collision guidance, socket references, and Unreal import planning are documented.
- Package makes no DCC, FBX, Unreal Content, runtime source, source asset, startup-scene, combat behavior, global index, or source-concept-copying claim.
