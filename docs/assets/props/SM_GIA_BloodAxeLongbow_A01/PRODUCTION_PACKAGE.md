# SM_GIA_BloodAxeLongbow_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeLongbow_A01`
- Asset type: Static Mesh weapon / Giant longbow
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source intake child ID: `BloodAxeArmory.png#Bow_Longbow_01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: Docs-only production package ready; DCC build not started
- Source-storage guardrail: the source concept remains external and must not be copied, moved, edited, embedded, or committed for this task.

`SM_GIA_BloodAxeLongbow_A01` is the largest Blood Axe Giant longbow silhouette from the armory intake: a brutal, heavy raider bow built from dark highland wood, horn, sinew, blackened iron reinforcement, scorched leather, red warning wraps, and a small number of oversized trophy bindings. It must read as hostile Blood Axe war gear for Giant raiders and hunters, not as neutral/civilized Giant stoneworker culture.

The design should feel crafted by a dangerous raider bowyer with practical Giant-scale reach: asymmetrical but functional, scarred but not cluttered, and readable at MMO camera distance. Keep skull/trophy language controlled so the bow remains buildable and does not become graphic or visually noisy.

## Gameplay Purpose

This asset supports future Blood Axe Giant archers, camp sentries, hunters, chieftain guards, armory racks, and loot-display silhouettes. It establishes Giant-scale bow proportions, grip placement, nock/string anchor references, back-carry clearance, and dependency rules for future quiver and arrow packages.

Expected use cases:

- Equipped two-handed ranged weapon for Blood Axe Giant NPCs.
- Armory, rack, or ground display prop in Blood Axe camps.
- Scale reference for future `KIT_GIA_BloodAxeQuivers_A01` arrows and quivers.
- Socket validation prop for Giant hand, back, draw, and nock alignment.

Do not define final projectile gameplay, damage, charge behavior, hit logic, arrow flight, or animation timing in this package.

## Silhouette Notes

Primary silhouette: a towering Giant longbow with a deep crescent arc, thick stave limbs, heavy wrapped center grip, reinforced horn or iron nocks, top and bottom string anchors, one readable trophy binding, and torn red cloth markers. The bow should look too large for normal humanoids and clearly fitted to a 470 cm male Giant hand span and shoulder line.

Readability rules:

- Preserve the bow's full arc, grip block, nock shapes, and string line as the first read.
- Use broad limb thickness and reinforced tips instead of dense spikes or tiny ornaments.
- Keep the trophy binding large and sparse: one skull or bone plate cluster is enough.
- Use red cloth wraps as faction markers, not as full-surface color coverage.
- Avoid elegant Elven crescent language and avoid neutral Giant carved-stone or blue rune identity.

## Scale Notes

Use the validated Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

Author in centimeters. 1 Unreal unit = 1 cm. Normal humanoid compatibility is not required.

Target proportions for DCC planning:

- Resting bow height: 410-455 cm from lower nock to upper nock.
- Stave thickness: 12-22 cm through the primary limbs, with thicker reinforced tips.
- Grip height: 42-55 cm, sized for a Giant hand and heavy leather wrap.
- Grip diameter/depth: 16-24 cm depending on hand fit and wrap thickness.
- Nock/tip assembly: 28-45 cm long per end, with clear string grooves.
- Resting string line offset: enough to read in silhouette without implying final draw mechanics.
- Full-draw reference envelope: validate against male Giant shoulder, elbow, wrist, and hand sockets, but leave final draw length and timing to future animation tasks.
- Back carry envelope: must clear Giant head, shoulder mass, trophy armor, and `back_quiver` placement when viewed from front, side, and rear.

Quiver dependency: future `KIT_GIA_BloodAxeQuivers_A01` must define final arrow count, arrow length, fletching size, quiver body, belt/back straps, and arrow projectile mesh. This longbow package only reserves the bow scale and socket references needed by that quiver package.

## Materials And Color Palette

Primary materials:

- Dark highland hardwood or laminated bow stave with hand-painted grain.
- Horn or bone caps at the nocks.
- Blackened iron and dark steel reinforcement plates near tips and grip.
- Scorched leather grip wrap, sinew binding, rawhide lashings, and heavy cord.
- Dark red cloth wraps and red war-paint marks for Blood Axe identity.
- Bone trophy binding used sparingly.
- Soot, ash, grime, rubbed edges, and broad hammered metal wear.

Avoid neutral/civilized Giant stoneworker language: no blue-gray civic stone motifs, warm hearth accents, restrained blue runes, monumental masonry ornament, or peaceful highland craft symbols. Those belong to non-Blood Axe Giant packages.

Emissive is not part of this baseline. If a future shamanic bow variant requires storm, ritual, or necromantic glow, it must be approved as a separate variant.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeLongbow_A01` for the world of Aerathea. The design should emphasize a massive Giant-scale longbow crescent, thick dark hardwood limbs, blackened iron reinforcements, horn nocks, heavy scorched-leather grip, sinew string anchors, sparse skull or bone trophy binding, torn red cloth markers, Blood Axe hostile Giant sub-faction identity, rough raider bowyer craft, grim camp-hunter mood, and future ranged weapon gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, strung/resting callouts, grip detail, nock detail, string anchor detail, back-carry clearance sketch, quiver dependency note, and scale callouts against female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5" Giants on a clean background. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid readable text, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model real geometry for the big production forms:

- Continuous curved bow stave with readable thickness and a slightly brutal, uneven hand-shaped profile.
- Oversized center grip block with leather wrap, raised palm stop, and enough depth for a Giant hand.
- Upper and lower nock assemblies with broad horn or iron caps and clear string grooves.
- Top and bottom string anchor hooks or grooves as simple, durable shapes.
- Rest-position string as a clean thin element, or a separable string subpiece if a future rigged/animated variant needs it.
- Main reinforcement plates at the grip and limb tips.
- One large trophy binding or bone plate cluster, placed so it does not obscure grip, nock, or string readability.
- Back-carry loop or strap anchor markers as large simple fittings, not tiny rings.

Use texture and normal maps for fine detail:

- Wood grain, small cracks, scratches, pitting, stitched wrap lines, sinew fibers, soot streaks, minor chips, and tiny metal hammer marks.
- Do not model dense rivet rows, tiny knot forests, hundreds of lashings, fine string fibers, or repeated small skulls.

Grip and draw fit notes:

- Pivot and grip center must align to the expected Giant bow hand, with the left-hand grip as the default review assumption.
- Nock and arrow-rest area must be broad enough for Giant arrows from the future quiver package.
- Draw reference markers should be documented for future animation, but no final draw distance, release timing, or projectile behavior is authored here.

## Texture And Material Notes

Texture set target: 2K for the baseline weapon. Use 4K only if a future named boss or hero variant approves it.

Required texture names:

- `T_GIA_BloodAxeLongbow_A01_BC`
- `T_GIA_BloodAxeLongbow_A01_N`
- `T_GIA_BloodAxeLongbow_A01_ORM`

Optional texture name:

- `T_GIA_BloodAxeLongbow_A01_E` only for a separately approved ritual or shamanic variant, not for this baseline.

Material instance:

- `MI_GIA_BloodAxeLongbow_A01`

Material slot target:

- 1 material slot preferred for the full bow.
- 2 material slots maximum if a future DCC pass needs separated string/leather from stave/metal.

Packed ORM should carry broad AO under wraps, high roughness on wood/leather/bone, lower roughness on rubbed metal edges, and restrained metallic response on blackened iron plates. Keep red faction marks in base color with no glow.

## Triangle Budget

- LOD0 target: 5k-8k tris.
- LOD0 hard cap: 9k tris if trophy binding, nocks, and grip require extra silhouette support.
- Material slots: 1 target, 2 maximum.
- Texture set: 2K baseline.

Budget priorities:

- Spend geometry on the bow arc, stave thickness, grip, nock forms, major reinforcement plates, and trophy binding.
- Do not spend geometry on tiny rivets, thread fibers, scratch patterns, dense binding wraps, or repeated small trophies.

## LOD Plan

All important production variants need LOD0-LOD3.

- LOD0: full bow arc, stave thickness, grip wrap forms, nocks, string, major reinforcement plates, red cloth markers, one trophy binding, and back-carry fittings.
- LOD1: 60-70 percent of LOD0; simplify wrap bevels, metal plate bevels, small cloth tears, minor chips, and trophy bevels.
- LOD2: 35-45 percent of LOD0; reduce nock caps, merge small fittings, flatten secondary reinforcement, simplify string support, and reduce trophy cluster shape.
- LOD3: 15-25 percent of LOD0; preserve the longbow arc, grip mass, string line, nock endpoints, and red faction color blocks.

Reduce details in this order: small scratches and rivets, secondary wrap cuts, tiny cloth tears, minor chips, small strap loops, trophy bevels, back-side details, then reinforcement plate bevels. Never reduce the main bow arc, grip, nocks, or string line before removing small detail.

## Collision Notes

Equipped baseline collision should be disabled. Combat traces, projectile collision, and hit detection are future gameplay-system work and are not defined here.

Display or pickup variants may use simple collision:

- One long capsule or narrow box following the main bow height.
- One small box around the grip if needed for pickup focus.
- No per-string collision.
- No individual trophy collision.
- No arrow or projectile collision in this package.

Back-carry collision should rely on character attachment bounds or a simple non-blocking preview volume only. The bow must not create blocking collision that catches on Giant armor, camp props, or quiver meshes.

## Animation Notes

Static mesh baseline. Do not author animation timing, final draw length, release timing, projectile spawn behavior, or combat montage rules in this package.

Future animation and socket notes:

- Bow grip: align the central grip to Giant hand sockets, defaulting to a left-hand bow grip review with future support for mirrored use if gameplay requests it.
- Nock: reserve a clear arrow nock/rest reference near the grip and string line for future Giant arrow alignment.
- Draw: include a draw reference marker or documentation point for the string pull hand, but leave draw distance and timing to the future Giant bow animation package.
- String anchor: top and bottom nock/string anchors must be clear enough for a future string deformation or swapped string mesh plan.
- Back carry: support attachment to `back_large_weapon` or a future bow-specific back socket without clipping Giant shoulders, hair, trophy armor, or quiver.
- Quiver dependency: future `KIT_GIA_BloodAxeQuivers_A01` must define `back_quiver`, arrow reach, arrow count, and draw-from-quiver clearance before final bow animation approval.

## Unreal Import Notes

Planned future asset only; this package does not create Unreal Content, DCC files, FBX exports, startup actors, runtime source, or validators.

- Planned Unreal path: `/Game/Aerathea/Weapons/Giants/BloodAxe/SM_GIA_BloodAxeLongbow_A01`
- Planned asset type: Static Mesh
- Import scale: 1.0 after future DCC/export approval, authored in centimeters
- Pivot: center of the main bow grip
- Forward/orientation: align to the project weapon convention during future DCC handoff; document any deviation before import
- Collision: disabled for equipped use; simple display collision only if a pickup/display variant is approved
- Material slots: 1 target, 2 maximum
- LODs: LOD0, LOD1, LOD2, LOD3 required
- Performance note: preserve the bow arc and nocks at distance; move small wear into textures

Recommended mesh sockets/locators for future import:

- `socket_bow_grip`
- `socket_arrow_rest`
- `socket_arrow_nock`
- `socket_string_top`
- `socket_string_bottom`
- `socket_string_pull_ref`
- `socket_back_carry_attach`
- `socket_quiver_alignment_ref`

Expected character-side socket dependencies:

- `hand_l_offhand` or future `bow_grip_l`
- `bow_string_pull_r`
- `arrow_nock`
- `back_large_weapon`
- `back_quiver`

These are planning names only. Final socket naming, projectile spawn rules, and animation timing require future gameplay/animation approval.

## Folder And Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeLongbow_A01/`
- Production package: `docs/assets/props/SM_GIA_BloodAxeLongbow_A01/PRODUCTION_PACKAGE.md`
- Planned Unreal folder after approval: `/Game/Aerathea/Weapons/Giants/BloodAxe/`
- Planned mesh name: `SM_GIA_BloodAxeLongbow_A01`
- Planned material instance: `MI_GIA_BloodAxeLongbow_A01`
- Planned textures: `T_GIA_BloodAxeLongbow_A01_BC`, `T_GIA_BloodAxeLongbow_A01_N`, `T_GIA_BloodAxeLongbow_A01_ORM`

DCC source folders, FBX export folders, Unreal Content assets, runtime source, startup-scene placement, external concept storage, and global index edits are intentionally out of scope for this docs-only task.

## Approval Gates

- Stop before DCC mesh creation, Blender source creation, FBX export, Unreal Content import, runtime source changes, startup-scene placement, or validator creation.
- Stop before copying, moving, editing, embedding, or committing the external source concept.
- Stop if the bow appears sized for normal humanoids instead of the Giant scale lock.
- Stop if Blood Axe raider language begins to overwrite neutral/civilized Giant culture.
- Stop if skulls, trophies, gore, rivets, lashings, or scratches become dense enough to hurt mid-poly readability.
- Stop before defining final projectile gameplay, combat traces, hit behavior, arrow inventory rules, draw distance, draw timing, release timing, or animation montage timing.
- Stop before final bow approval if `KIT_GIA_BloodAxeQuivers_A01` has not resolved back quiver clearance, arrow scale, and draw-from-quiver dependency.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Bow height, grip, nock, draw reference, string anchor, back carry, and quiver dependency notes are included.
- Final projectile gameplay and animation timing are not defined.
- Primary silhouette reads as a massive Giant longbow at MMO camera distance.
- Materials use dark hardwood, blackened iron, dark steel, horn/bone, scorched leather, sinew, soot, grime, and dark red Blood Axe cloth/paint consistently.
- Emissive is absent by default and approval-gated for any future ritual or shamanic variant.
- Tiny rivets, scratches, string fibers, dense lashings, pitting, wood grain, and minor chips are assigned to textures or normals instead of geometry.
- Texture maps, material slot limits, triangle budgets, LOD0-LOD3, collision, socket planning, Unreal import planning, folder naming, and approval gates are included.
- The package makes no DCC, FBX, Unreal Content, runtime source, global index, external concept copy, or startup-scene work claim.
