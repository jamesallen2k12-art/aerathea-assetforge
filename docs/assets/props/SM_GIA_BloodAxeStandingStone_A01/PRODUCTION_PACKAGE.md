# SM_GIA_BloodAxeStandingStone_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeStandingStone_A01`
- Asset type: Static Mesh prop production package, docs-only
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Dependency reference: validated `SK_GIA_Base_A01` scale lock
- Status: planning package only

`SM_GIA_BloodAxeStandingStone_A01` is a single rough Blood Axe standing stone used as non-graphic territory and memory dressing for hostile Giant camp, highland trail, or abandoned nomad-site scenes. It should read as one heavy fractured slab forced upright by Giant hands, with blunt broken planes, a grounded stone base, sparse dark lashings, and restrained oxide red cloth or old trophy hints as texture detail or removable accents.

Blood Axe identity must remain separate from neutral/civilized Giant culture. The asset should feel harsh, improvised, and threatening, but it must not become a refined cave-town monument, civic wayfinding sign, magical gameplay device, readable rune object, altar, quest marker, or interactive prop.

## Gameplay Purpose

The standing stone is static visual dressing only. It helps mark Blood Axe-claimed ground, abandoned camp edges, approach beats, and rough highland memory sites without defining mechanics.

Allowed planning uses:

- Provide a tall, readable hostile marker silhouette sized for Giant spaces.
- Add rough Blood Axe territory language beside camp routes, gates, shelters, cairns, or stronghold approach pieces.
- Support future kit composition for standing-stone rows or loose marker clusters without selecting an implementation target here.
- Reinforce that Blood Axe is a hostile Giant sub-faction, not the default Giant culture.

Out of scope:

- Readable rune text, ritual VFX, objective marker design, damage/aura behavior, interaction behavior, quest marker behavior, nav/pathfinding behavior, pickup or loot behavior, destructible behavior, DCC source work, FBX export, Unreal Content creation, source export work, game asset creation, startup placement, and first implementation target selection.

## Silhouette Notes

- Primary read: one tall fractured stone slab with a heavy uneven crown, broad chipped sides, and a slight forward or side lean.
- Secondary read: two or three large base chock stones pressed into mud and ash, not a finished plinth.
- Tertiary read: sparse hide lashings, one optional faded oxide red cloth wrap, and old non-graphic trophy hints handled as texture marks or removable accent pieces.
- Keep the slab silhouette simple and memorable from front, side, and three-quarter views. The top should not form a clean obelisk, arrow, UI pointer, readable letter, or sacred icon.
- Model the large slab planes and major chips as real geometry. Keep fine cracks, soot, scratch noise, cloth weave, lashing fibers, and small surface pitting in textures and normal detail.
- Avoid excessive scratches, rivets, micro-detail, dense carved marks, skull piles, fresh gore, glowing channels, floating symbols, or polished blue-gray civic masonry.

## Scale Notes

Use the validated Giant scale lock from `SK_GIA_Base_A01`: female 442 cm and male 470 cm baselines. The broader Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.

Target asset dimensions:

- Overall height: 420-620 cm.
- Main slab width: 150-260 cm at the broadest point.
- Main slab depth: 70-160 cm.
- Base footprint: 220-420 cm wide and 160-320 cm deep, including chock stones and embedded earth.
- Cloth or lashing band height: roughly 180-360 cm above ground, scaled as Giant-tied material.

The standing stone should feel oversized for normal humanoids and readable beside a 470 cm male Giant, but it should remain smaller and less formal than major gates, monuments, shaman huts, or cave-town civic stonework.

## Materials and Color Palette

Primary materials:

- Fractured highland stone with dark gray, charcoal, muted slate, dirty tan chips, and soot-black recesses.
- Packed mud, ash, and embedded base stones around the bottom edge.
- Sparse hide or rope lashings, darkened by weather and smoke.
- Optional oxide red cloth strip or faded paint smear for Blood Axe identity.
- Optional old horn, dull bone, or broken shield hint as a small removable accent, never as graphic trophy clutter.

Palette targets:

- Stone and soot: `#17191A`, `#2B2E2F`, `#4E504C`, `#68645A`
- Fresh fractured chips: `#7A7266`, `#91846D`
- Mud and packed earth: `#2D2118`, `#463325`, `#5E4A36`
- Oxide red cloth or paint: `#5F1513`, `#7A1D18`, `#8B2A21`
- Hide, rope, and old leather: `#5B442B`, `#7A6040`, `#A88958`
- Old bone or horn hints: `#85775E`, `#A8946D`, `#C7B98F`

No default emissive is allowed. No polished neutral/civilized Giant culture materials should appear: no refined terrace stone, civic mason marks, blue rune inlays, waterwork motifs, warm hearth symbolism, or peaceful highland wayfinding finish.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeStandingStone_A01` for the world of Aerathea. The design should emphasize a tall rough fractured standing-stone slab, Giant-scale height, heavy base chock stones, dark highland stone, soot, ash, packed mud, sparse hide lashings, restrained oxide red cloth, optional non-graphic trophy hints as texture or removable accents, Blood Axe hostile Giant sub-faction identity, clear separation from neutral/civilized Giant culture, grim highland camp-marker mood, and static visual territory-dressing role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a static mesh concept sheet with front, side, back, and three-quarter views, material swatches, scale markers beside female 442 cm and male 470 cm Giant baselines, and LOD/collision callouts on a clean background. Avoid copying any existing franchise, avoid readable rune text, avoid ritual VFX, avoid objective markers, avoid quest marker language, avoid interaction behavior, avoid damage or aura affordances, avoid nav/pathfinding diagrams, avoid graphic gore, avoid magical gameplay-device design, and avoid excessive scratches, rivets, or micro-detail that would not translate to a mid-poly game asset.

## Modeling Notes

This package defines a future static mesh only and creates no DCC source, FBX export, Unreal Content, game asset, material instance, validator, runtime code, or placement.

Future modeling priorities:

- Build the main slab as one dominant fractured stone mass with a readable lean and thick, weighty proportions.
- Use 3-6 large chock stones and embedded base forms to make the stone feel physically wedged into the ground.
- Add only major chips, bevels, missing corners, and broad fracture cuts as geometry.
- Keep lashings thick and sparse. Two or three broad bands are enough; avoid many thin cords.
- Model optional cloth as fixed static geometry with one broad wrap or hanging strip.
- Keep trophy hints removable and minimal: a single old horn chip, dull bone token, or broken shield scrap at most.
- Use asymmetry, weight, and rough stone planes for Blood Axe identity instead of dense symbols or graphic decoration.
- Do not model small cracks, fine scratches, cloth fibers, rope fibers, dirt speckles, tiny chips, or surface stains as geometry.

## Texture and Material Notes

Target material strategy:

- Default material count: 1 shared prop material for stone, mud, ash, cloth, lashings, and optional accent.
- Maximum material count: 2 if a later art pass needs separate stone and cloth/hide/horn reuse.
- Default texture resolution: 1K BC/N/ORM.
- 2K is acceptable only if this prop becomes close-view hero dressing in a later task.

Required future texture names:

- `T_GIA_BloodAxeStandingStone_A01_BC`
- `T_GIA_BloodAxeStandingStone_A01_N`
- `T_GIA_BloodAxeStandingStone_A01_ORM`

Texture guidance:

- Base Color should carry broad stone plane variation, soot gradients, faded red cloth or paint, mud at the base, and old weathered accent tones.
- Normal should carry fine cracks, stone pitting, cloth weave, rope fiber, minor chips, and surface roughness.
- ORM should use ambient occlusion around slab-base contact, chock stones, lashings, cloth overlaps, and underside creases.
- Roughness should stay high across stone, mud, ash, cloth, hide, and old bone. Metallic should remain unused unless an optional broken shield scrap is added.
- No emissive texture is needed for the default asset.

## Triangle Budget

- Target category: large static prop.
- LOD0: 3k-7k tris.
- LOD1: 1.5k-3.5k tris.
- LOD2: 600-1.4k tris.
- LOD3: 150-450 tris.
- Material budget: 1 material target, 2 maximum.
- Texture budget: 1K BC/N/ORM by default, 2K only for later close-view use.

Spend geometry on the slab outline, top break, leaning profile, base chock stones, and broad cloth/lashing silhouette. Do not spend geometry on tiny crack carpets, dense scratches, rivets, fine fray, small ash flecks, repeated bone tokens, or hidden underside detail.

## LOD Plan

- LOD0: full slab silhouette, major fractured planes, base chock stones, broad lashings, optional cloth, and readable grounded base.
- LOD1: reduce secondary bevels, simplify small chips, merge minor base pieces, and lower lashing/cloth cuts while preserving the standing-stone height read.
- LOD2: simplify the slab into fewer broad planes, reduce base stones to major masses, keep only the strongest cloth or red-paint beat, and remove most backside detail.
- LOD3: preserve the tall leaning slab, heavy base footprint, and one Blood Axe color/material accent. Remove nearly all small cuts and accent geometry.

Reduction order:

1. Tiny chips, surface scratches, dirt flecks, cloth holes, and paint chips.
2. Minor lashing cuts, small knots, and secondary cloth tears.
3. Small chock stones, underside base detail, and back-facing accent pieces.
4. Secondary fracture cuts and non-silhouette bevels.
5. Optional trophy accent geometry.

Never reduce the primary tall slab silhouette, Giant-scale height read, rough fractured crown, or Blood Axe red/black identity before removing small detail.

## Collision Notes

Future collision should be simple and non-gameplay-focused:

- Default: one low-count convex hull or simple box group around the stone slab and base.
- Optional: separate simple base hull if placement needs cleaner player or camera contact.
- No per-chip, per-lashing, per-cloth, per-accent, or per-crack collision.
- No gameplay volumes, marker volumes, damage volumes, aura volumes, pickup collision, interaction collision, route proofing, or pathing claims.

This package creates no collision asset and does not validate placement behavior.

## Animation Notes

- Static mesh only.
- No skeletal setup, cloth simulation, wind motion, physics sway, destruction, collapse, material pulse, VFX, audio, Blueprint state, interaction state, or gameplay state change.
- Cloth and lashings should be modeled in fixed readable poses that work from multiple viewing angles.

## Unreal Import Notes

This section is future planning only. No game asset, material instance, texture asset, script, validator, Blueprint, runtime file, or placement is created or authorized by this package.

- Asset name: `SM_GIA_BloodAxeStandingStone_A01`
- Asset type: Static Mesh
- Planned future folder: `/Game/Aerathea/Props/Giants/BloodAxe/StandingStones/`
- Naming convention: `SM_GIA_BloodAxeStandingStone_A01`, `MI_GIA_BloodAxeStandingStone_A01`, `T_GIA_BloodAxeStandingStone_A01_BC`, `T_GIA_BloodAxeStandingStone_A01_N`, `T_GIA_BloodAxeStandingStone_A01_ORM`
- Pivot: ground center at the base footprint.
- Orientation: strongest front-facing slab read points along +X unless a later implementation task sets a different convention.
- Scale: centimeter-authored source, imported at scale 1.0, matching the female 442 cm and male 470 cm Giant baselines without changing the Giant scale lock.
- Collision type: simple collision only if later requested.
- LOD plan: LOD0-LOD3 required before any shipping use.
- Material slot count: 1 target, 2 maximum.
- Texture list: `T_GIA_BloodAxeStandingStone_A01_BC`, `T_GIA_BloodAxeStandingStone_A01_N`, `T_GIA_BloodAxeStandingStone_A01_ORM`.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: use a low material count, aggressive LOD reduction, broad baked texture detail, and instancing for repeated standing-stone rows or clusters.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeStandingStone_A01/PRODUCTION_PACKAGE.md`

Future asset naming references, for planning only:

- Static mesh: `SM_GIA_BloodAxeStandingStone_A01`
- Material instance: `MI_GIA_BloodAxeStandingStone_A01`
- Base color: `T_GIA_BloodAxeStandingStone_A01_BC`
- Normal: `T_GIA_BloodAxeStandingStone_A01_N`
- ORM: `T_GIA_BloodAxeStandingStone_A01_ORM`

No source folder, DCC file, FBX export, Unreal Content folder, source concept copy, task-board edit, index edit, backlog edit, approval-queue edit, runtime source file, placement, or target selection is created by this docs-only task.

## Quality Gate Checklist

- Top-level package headings match the required universal format.
- Asset remains a docs-only static mesh production package.
- Giant scale lock is explicit with female 442 cm and male 470 cm baselines from `SK_GIA_Base_A01`.
- Blood Axe is described as a hostile Giant sub-faction and does not overwrite neutral/civilized Giant culture.
- Standing stones remain rough non-graphic marker stones, not magical gameplay devices.
- Primary read is a large fractured stone slab with readable silhouette, base chock stones, sparse lashings, and restrained Blood Axe color.
- Sparse trophy hints remain texture detail or removable accents, never dense gore or graphic trophy clutter.
- No readable rune text, ritual VFX, objective marker, damage/aura, interaction behavior, quest marker, nav/pathfinding, destructible behavior, pickup/loot behavior, gameplay volumes, DCC source work, FBX export, Unreal Content creation, startup placement, or first implementation target selection are defined.
- No excessive scratches, rivets, dense cracks, tiny chips, or micro-detail are required for the asset read.
- Texture plan includes BC, N, and ORM maps with no default emissive map.
- Triangle budgets, LOD0-LOD3, collision notes, animation notes, and future import planning are present without performing implementation work.
