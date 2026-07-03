# SK_GIA_BloodAxeShaman_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeShaman_A01`
- Asset type: Skeletal Mesh character variant production package; future Blood Axe Giant shaman/cult-leader NPC only after later approval
- Parent route: future `KIT_GIA_BloodAxeWarband_A01`
- Source route references: `GiantBloodAxeMaleShaman.png` as the shaman/cult-leader candidate and `BloodAxeShamanHut.png` as environment context from the Giant Blood Axe slate
- Existing dependencies: `SK_GIA_Base_A01`, `KIT_GIA_BloodAxeArmory_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`, and the Blood Axe wearable gear package set
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, runtime, VFX graph, AI, combat, animation timing, cloth, physics, final visual approval, or first DCC target selection is included
- Source-storage guardrail: external concept images remain outside the repository. Do not copy, move, edit, embed, or commit external source concepts for this package.

`SK_GIA_BloodAxeShaman_A01` defines a hostile Blood Axe Giant shaman who reads as a ritual enforcer, warband omen-keeper, and brutal camp mystic without becoming the default Giant identity. The shaman should preserve the validated Giant body mass, then layer Blood Axe red-black raider material language, rough hide and fur, blackened reforged metal, dry bone and horn tokens, red mineral pigment, soot, and a few ritual stone/totem elements.

Magic is visual-readiness only in this package. Staff, hand, eye, totem, and ground locators may be planned, but no spell behavior, VFX graph, AI role, combat tuning, cast timing, projectile rule, aura, debuff, healing, summoning, or encounter logic is authorized here.

Blood Axe shaman language must stay separate from neutral/civilized Giant culture. Do not use blue-gray stoneworker pride, calm hearth identity, refined cave-town masonry symbols, peaceful highland nomad dress, or restrained civilized rune language as the default. Blood Axe ritual power should feel harsher: smoky, red-marked, bone-bound, iron-clamped, and threatening, but still readable and non-graphic.

## Gameplay Purpose

This package prepares a future Blood Axe Giant shaman/cult-leader character variant for warband hierarchy planning. The gameplay read is "dangerous ritual authority inside a hostile Blood Axe force," expressed through silhouette, equipment, material language, and socket/VFX-readiness locators only.

Expected future use cases:

- Elite Blood Axe shaman NPC silhouette within warbands, camps, stronghold approaches, or ritual-stone areas.
- Visual companion to Blood Axe chieftains, hunters, raiders, banner carriers, and armory gear.
- Source direction for future staff, hand-focus, chest-talisman, back-totem, and ground-totem locator reviews.
- Scale and clearance planning against the validated Giant male 470 cm and female 442 cm baselines.
- Material planning for restrained shamanic accents that do not overwrite the no-emissive default armory language.

Out of scope:

- No spell behavior, damage values, healing rules, buffs, debuffs, summons, projectile behavior, ground effects, faction aura, AI tactics, patrol logic, loot, quest, inventory, pickup, or encounter implementation.
- No VFX graph, Niagara system, animated material state, timing curve, Blueprint behavior, validator, or startup placement.
- No skeletal fitting, skinning, cloth simulation, physics setup, animation authoring, animation timing, or final visual approval.
- No source folders, DCC source, FBX export, Unreal Content asset, runtime source, copied external concept art, global index edit, or task-board update.

## Silhouette Notes

The shaman must read first as a Giant, then as Blood Axe, then as a ritual caster. Preserve a towering torso, broad shoulders, huge hands, long heavy arms, thick neck, sturdy legs, and the validated Giant scale before adding ritual equipment.

Primary silhouette goals:

- Male baseline silhouette at 470 cm, with future female fit review at 442 cm if a variant is approved.
- Massive Giant body mass with a slightly forward ritual stance and heavy staff support, not a thin wizard silhouette.
- One dominant shaman staff or totem-staff taller than the character shoulder line and readable at MMO camera distance.
- Broad asymmetrical shoulder wrap, fur/hide mantle, or partial raider chest armor that leaves Giant chest breadth visible.
- Heavy utility harness and ritual belts compatible in language with `SK_GIA_BloodAxeHarness_A01` and `SK_GIA_BloodAxeTrophyBelt_A01`, but simplified so the torso does not become cluttered.
- A small number of large bone, horn, tooth, stone, or broken-metal tokens, placed as clear ritual markers rather than dense charm curtains.
- Red mineral paint, red cloth wraps, and blackened metal blocks as Blood Axe identifiers.
- Optional helm, mask, or faceguard influence from `SM_GIA_BloodAxeTrophyHelm_A01`, but the eyes, brow, jaw, and thick neck must remain readable.
- Hands should remain visible enough to support future cast-hand locator review.

Staff and totem silhouette planning:

- `SM_GIA_BloodAxeShamanStaff_A01` candidate: long blackened-wood or dark-iron haft, heavy reforged metal head, rough stone or bone totem crown, two Giant hand grip zones, lower ground-contact foot, and one restrained focus core.
- `SM_GIA_BloodAxeShamanTotem_A01` candidate: optional back-carried or ground-planted ritual focus, built from dark granite, raw iron clamps, hide ties, red pigment channels, and sparse bone markers.
- Totem and staff should share motifs but remain separate enough that a future DCC lane can build one without committing to the other.

Avoid:

- Normal humanoid shaman proportions scaled up without Giant anatomy.
- Neutral/civilized Giant blue-gray stoneworker motifs as the default.
- Ogre shaman cairn language, Ogre Teknomancy parts, necromancer green-black glow, or polished druid elegance.
- Excessive skulls, teeth strings, tiny charms, gore ropes, wet blood, readable text, franchise-like symbols, or dense modeled micro-detail.
- Magic effects that hide the Giant silhouette or imply implemented spell behavior.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Feet at world origin and orientation should follow the future Giant base import convention.

Primary planning target:

- `A01` is planned against the male 470 cm Blood Axe shaman candidate first because the source route names a male shaman.
- A female 442 cm fit pass may be planned later, but this package does not approve a second mesh, shared deformation solution, or final wearable fit.
- Normal humanoid compatibility is not required.

Body and gear scale planning:

- Staff total height: 520-650 cm, with the highest crown or totem point clearly above shoulder level but not so tall that standard review framing becomes impractical.
- Staff haft diameter: 10-18 cm through grip zones, sized for Giant hands.
- Staff head or totem crown: 90-160 cm tall and 60-120 cm wide, with a bold readable top shape and no dense charm clutter.
- Ground-contact staff foot or spike: 25-60 cm, broad enough for a heavy prop read.
- Back totem height: 130-220 cm if carried; width 60-120 cm; must clear shoulders, hair, head turn, and `back_large_weapon` review.
- Chest talisman: 35-80 cm high, large enough to read against a Giant chest and small enough not to hide torso mass.
- Belt charms and trophy tokens: 30-85 cm, limited in count and placed away from pelvis, thigh, and knee clearance.
- Major straps: 12-28 cm wide, matching Giant-scale Blood Axe harness language.
- Ritual paint bands: broad body or gear markings, not tiny glyph strings.

Required future clearance checks before any implementation claim:

- Neck, jaw, hair, brow, and shoulder clearance for any helm/mask.
- Staff two-handed grip spacing using Giant hand sockets.
- Back-carry clearance for staff, totem, quiver, or large weapon conflicts.
- Belt, sidearm, charm, and tasset clearance during walk, turn, wide stance, and heavy upper-body poses.
- Staff ground-contact and lower-hand clearance without animation timing claims.
- VFX locator positions must remain outside body intersections and must not require a different Giant base scale.

## Materials and Color Palette

Primary Blood Axe shaman materials:

- Weathered Giant skin with soot, scars, ash, and broad red mineral ritual paint.
- Blackened iron, dark steel, and stolen/reforged metal using or matching `MI_GIA_BloodAxeReforgedMetal_A01`.
- Scorched leather, hide, dark fur, sinew cord, and rough rope.
- Dark granite, broken ritual stone, raw iron clamps, and ash-blackened channels for staff/totem pieces.
- Old dry bone, horn, tooth, cracked shell, or broken trophy tokens used sparingly and non-graphically.
- Torn deep red cloth, dirty red wraps, and chipped red war paint as Blood Axe identifiers.
- Soot, ash, mud, old smoke staining, rubbed metal edges, and broad hand-painted wear.

Suggested color ranges:

- Weathered Giant skin: muted stone-tan, gray-rose, and cold highland brown ranges, with soot and ash overlays.
- Blackened metal: `#151719` to `#2A2C2E`.
- Worn dark steel edges: `#555A5C` to `#787B78`.
- Scorched leather and hide: `#241611` to `#4A2E20`.
- Blood Axe red pigment and cloth: `#5F1513` to `#8B211B`.
- Old bone and horn: `#A69578` to `#D0B98C`.
- Dark ritual stone: `#1D1E20` to `#3F4142`.
- Soot and grime: `#0B0A09` to `#403025`.

Restrained magic material notes:

- Default state has no emissive dependency and no animated material state.
- Optional future approval-gated emissive may use dull ember orange, hot coal red-orange, or brief storm-white pinlines on staff cracks, totem channels, hand paint, eyes, or chest talisman.
- Emissive must remain small-area and low-bloom. It should clarify ritual focus points, not flood the body or replace the Blood Axe red-black material read.
- Do not use necromantic green-black, civilized Giant blue runes, large blue Aetherium glow, or broad purple arcane washes for this baseline.
- Suggested future scalar defaults if a material task is approved: `RitualGlowAmount=0.0`, `StaffCoreGlow=0.0`, `HandMarkGlow=0.0`, with any nonzero values requiring visual approval.

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_GIA_BloodAxeShaman_A01` for the world of Aerathea. The design should emphasize a 470 cm male Blood Axe Giant shaman with future 442 cm female scale reference, towering broad Giant anatomy, hostile Blood Axe raider-cult identity, a massive ritual staff or totem-staff, blackened reforged iron, scorched leather, dark hide and fur, dry bone and horn tokens, dark ritual stone, red mineral paint, torn deep red cloth, soot, ash, restrained ember or storm-white locator glow, and a gameplay role as a warband ritual authority without defining spell behavior. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents only as visual-readiness callouts, and MMO-friendly production design. Present it as a character production sheet with front, side, back, three-quarter view, staff callout, optional back-totem callout, socket/locator callouts, material swatches, and scale markers beside female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines on a clean background. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid dense trophy clutter, avoid final spell diagrams, avoid VFX graph language, avoid AI or combat tuning, avoid readable text, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, sculpt, retopo, UV, bake, FBX export, Unreal Content asset, skeletal fit, cloth setup, physics setup, VFX graph, runtime behavior, or final visual approval is created or approved by this package.

Future modeling should prioritize:

- Reuse the approved Giant base proportions and skeleton assumptions before adding shaman gear.
- Preserve the huge head, brow, neck, chest, hands, feet, and shoulder line of the Giant base.
- Build large outfit masses as modular, readable forms: hide mantle, fur blocks, chest straps, partial blackened armor, ritual belt, broad wrist wraps, and lower-leg wraps or greaves.
- Model the primary shaman staff as a large prop with a clean grip zone, bold crown silhouette, heavy ground-contact foot, and a few large totem elements.
- Model a back totem or chest talisman only if it remains readable and does not crowd the shoulder, spine, or back-carry zones.
- Use big dry trophies sparingly: one large horn, a few bone plates, one stone token cluster, or broken-metal talisman forms.
- Use large rings, clamps, straps, buckles, and iron collars as real geometry where they support attachment logic or silhouette.
- Keep ritual paint on the body and gear broad enough to read at MMO camera distance.
- Leave hands, staff grips, staff head, chest talisman, eyes, and ground-contact zones clean enough for future locator review.

Texture or normal-map:

- Tiny scratches, pitting, stitch rows, leather pores, fur texture, sinew fibers, fine bone cracks, stone grain, soot speckles, small paint chips, minor tally marks, and hairline surface damage.

Staff/totem modeling gates:

- Staff and totem should be buildable as separate future meshes if implementation later splits character, staff, and ground prop work.
- Staff grip geometry must not force crossed wrists or a different Giant hand scale.
- Totem crown and dangling elements must stay rigid and sparse by default.
- Avoid long cloth streamers, hanging chain curtains, or physics-dependent silhouettes in the first pass.
- Any moving cloth, swinging trophies, staff chain motion, or secondary physics requires a separate approval and validation pass.

Do not model:

- Spell projectiles, ground effect meshes, aura rings, interactable spell circles, floating UI symbols, dense particle cards, readable text, gore ropes, fresh remains, or many tiny charms.
- Civilized Giant stoneworker motifs, warm hearth markers, refined masonry symbols, or peaceful clan banners as default Blood Axe shaman language.

## Texture and Material Notes

Texture set targets for future approved build work:

- `T_GIA_BloodAxeShaman_A01_Body_BC`
- `T_GIA_BloodAxeShaman_A01_Body_N`
- `T_GIA_BloodAxeShaman_A01_Body_ORM`
- `T_GIA_BloodAxeShaman_A01_Gear_BC`
- `T_GIA_BloodAxeShaman_A01_Gear_N`
- `T_GIA_BloodAxeShaman_A01_Gear_ORM`
- `T_GIA_BloodAxeShamanStaff_A01_BC`
- `T_GIA_BloodAxeShamanStaff_A01_N`
- `T_GIA_BloodAxeShamanStaff_A01_ORM`
- Optional future approval-gated `T_GIA_BloodAxeShaman_A01_E`
- Optional future approval-gated `T_GIA_BloodAxeShamanStaff_A01_E`
- Optional future approval-gated `T_GIA_BloodAxeShamanTotem_A01_E`

Material slot target for character:

- Slot 0: `MI_GIA_BloodAxeShamanSkin_A01` for weathered Giant skin, scars, soot, and ritual paint.
- Slot 1: `MI_GIA_BloodAxeShamanHideFur_A01` for fur, hide, leather wraps, and rough cloth if combined.
- Slot 2: `MI_GIA_BloodAxeReforgedMetal_A01` for blackened iron, dark steel, clamps, rings, plates, and chipped red paint masks.
- Slot 3: `MI_GIA_BloodAxeBoneStone_A01` for dry bone, horn, teeth, dark ritual stone, and talisman pieces.
- Optional Slot 4: `MI_GIA_BloodAxeShamanRitualGlow_A01` only after visual/material approval.

Material slot target for staff/totem:

- Preferred: 2 material slots, one for dark haft/leather/cloth and one for metal/bone/stone.
- Maximum: 3 material slots if a future approved emissive material is separated.
- Do not create one-off slots for every charm, tooth, strap, paint mark, or stone chip.

Packed `ORM` plan:

- R: Ambient occlusion around straps, fur overlaps, staff collars, talisman seats, totem channels, bone sockets, and armor plates.
- G: High roughness for soot, skin paint, leather, fur, old bone, stone, and blackened metal; slightly lower on rubbed metal edges and hand-worn staff grips.
- B: Metallic only for iron, steel, rings, clamps, plates, staff head fittings, and reforged-metal pieces.

Readability requirements:

- Use broad body paint and material blocks instead of tiny glyphs.
- Keep soot and dark materials from flattening the whole shaman into one black mass.
- Keep red accents secondary to silhouette and role.
- Keep bone warm and matte so it supports the ritual read without overpowering the body.
- Any emissive map is absent by default and must be small, low-bloom, and approval-gated.

## Triangle Budget

`SK_GIA_BloodAxeShaman_A01` is a Giant character variant and should use the `SK_GIA_Base_A01` budget expectations as the scale reference.

Future LOD0 targets:

- Base Giant body contribution: 35k-55k tris, inherited from final approved Giant body work.
- Shaman outfit, straps, armor, fur, hair, talismans, and ritual gear: 22k-34k tris.
- Staff: 5k-9k tris.
- Optional back or ground totem: 4k-8k tris if approved as a separate mesh.
- Full common/elite shaman assembled target: 65k-85k tris excluding a separate ground prop.
- Hard cap for a named/boss shaman variant: 90k tris only after visual approval and with aggressive LODs.
- Material slots: target 4 slots for the character, 2 slots for staff/totem; 5 character slots only if the emissive material is separately approved.
- Texture resolution: 2K sets for standard enemy use; 4K only for a named hero or boss close-up variant after approval.

Budget distribution guidance:

- Body, head, hands, feet, and hair/fur masses: 45-55 percent of the assembled character.
- Hide/fur mantle, straps, belt, armor, and major wraps: 20-25 percent.
- Staff and totem gear: 10-15 percent.
- Bone, horn, ritual stone, rings, buckles, and talisman accents: 8-12 percent.
- Small silhouette chips, rigid cloth edges, and secondary forms: 5-8 percent.

Do not spend geometry on tiny rivets, many small charms, dense chain links, fine fur strands, tiny glyphs, stitch rows, pitting, hairline cracks, micro scratches, or particle-like magic cards.

## LOD Plan

All future character, staff, and totem meshes need LOD0-LOD3.

- LOD0: full Giant body silhouette, face planes, hands, feet, hair/fur clumps, major shaman wraps, armor masses, broad staff crown, chest talisman, back totem if present, sparse trophies, and locator-supporting focus points.
- LOD1: 60-70 percent of LOD0; reduce minor strap bevels, small bone chips, secondary talisman cuts, hair/fur subdivisions, small staff-crown notches, and underside gear details.
- LOD2: 35-45 percent of LOD0; simplify fingers, inner wraps, back-side harness detail, small trophy forms, stone/metal bevels, and staff head interior cuts while preserving the shaman read.
- LOD3: 15-25 percent of LOD0; preserve towering Giant height, head/shoulder line, huge hands, staff silhouette, red/black Blood Axe blocks, and one or two major ritual focus shapes.

Reduction order:

1. Tiny rivets, stitches, scratches, pitting, paint chips, and small glyph marks.
2. Small straps, knots, bindings, and minor cloth tears.
3. Small bone chips, little teeth, charm fragments, and tiny stone cracks.
4. Back-side harness and non-visible underwrap detail.
5. Secondary hair/fur cuts and non-silhouette clumps.
6. Staff crown interior cuts and small totem notches.
7. Minor armor bevels and support rings.

Never reduce the Giant height, shoulder width, hand size, staff outline, chest/totem focus read, or Blood Axe red-black identity before removing small detail.

## Collision Notes

No collision is authored or approved in this docs-only package.

Future collision planning:

- Character movement should inherit the Giant-tuned capsule policy from `SK_GIA_Base_A01`.
- Male baseline planning: roughly 470 cm height with 100-125 cm movement capsule radius, pending future implementation review.
- Female baseline planning: roughly 442 cm height with 95-115 cm movement capsule radius, pending future implementation review.
- Worn gear should normally rely on the owning Giant physics asset and movement capsule, not per-strap or per-trophy collision.
- Equipped staff collision should be disabled by default; future gameplay traces, if any, require a separate gameplay and animation task.
- Display staff or ground-totem variants may use one simple capsule, box, or low-count convex hull around the main volume.
- Cloth, fur, straps, charms, chains, bone tokens, and paint marks should not have individual collision.
- VFX locator names must not imply hit zones, weak points, damage types, aura volumes, or interactable areas.

Collision does not validate final wearable fit, physics bodies, staff traces, hit reactions, spell impact, or encounter behavior.

## Animation Notes

No animation, animation timing, skeletal fitting, retargeting, cloth simulation, physics setup, secondary motion, AI, combat tuning, or VFX timing is authored or approved here.

Future approval-gated animation needs may include:

- Giant base idle, heavy breathing, walk, run, turn in place, hit reaction, stagger, and death compatibility.
- Shaman idle with staff planted or carried.
- Two-handed staff hold, staff lift, staff ground-plant, and back-carry clearance poses.
- Cast-hand pose placeholders using `vfx_cast_hand_l` and `vfx_cast_hand_r` style locators only after socket approval.
- Chest-talisman, staff-tip, totem-core, and ground-contact locator checks in static review poses.
- Turn, wide stance, kneel or crouch review only if later approved for the Giant animation set.

No cast durations, cooldowns, damage windows, projectile spawn timing, area-control timing, summon timing, AI decision timing, cloth timing, chain physics, or footstep/VFX timing are part of this package.

Rigid gear is preferred for first planning. Any loose cloth strips, swinging trophies, staff chain motion, hair/fur physics, or dangling charm simulation requires separate approval and focused validation.

## Unreal Import Notes

This section is planning only. No Unreal Content, material instance, texture, skeletal mesh, static mesh, physics asset, animation Blueprint, Blueprint actor, Niagara system, validator, startup actor, or runtime source is created by this package.

Planned future Unreal folders:

- Character: `/Game/Aerathea/Characters/Giants/BloodAxe/Shaman/`
- Gear: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`
- Weapons/ritual props: `/Game/Aerathea/Weapons/Giants/BloodAxe/Shaman/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned Unreal assets:

- Primary skeletal mesh: `SK_GIA_BloodAxeShaman_A01`
- Optional male/female split after approval: `SK_GIA_BloodAxeShaman_Male_A01`, `SK_GIA_BloodAxeShaman_Female_A01`
- Staff static mesh candidate: `SM_GIA_BloodAxeShamanStaff_A01`
- Optional totem static mesh candidate: `SM_GIA_BloodAxeShamanTotem_A01`
- Future skeleton dependency: approved Giant base skeleton convention from `SK_GIA_Base_A01`
- Future animation Blueprint placeholder only after approval: `ABP_GIA_BloodAxeShaman_A01`

Import planning:

- Asset type: Skeletal Mesh for the character; Static Mesh for staff/totem unless a future task approves skeletal or cloth-ready variants.
- Pivot: character feet at world origin; staff pivot at primary grip center for equipped review; display staff pivot may be ground-contact center if split later.
- Scale: centimeter-authored, import at scale 1.0 after future DCC/export validation.
- Forward orientation: match the approved Giant base convention.
- LODs: LOD0-LOD3 required for character, staff, and totem.
- Collision: Giant capsule/physics asset for character; simple display collision only for non-equipped staff/totem variants.
- Material slot count: target 4 for character, 2 for staff/totem, optional emissive slot only after approval.
- Blueprint behavior: none.
- Niagara/VFX graph: none.

Inherited and candidate socket/locator planning:

- Inherited Giant sockets to respect: `hand_r_weapon`, `hand_l_offhand`, `hand_r_twohand_grip`, `hand_l_twohand_grip`, `back_large_weapon`, `back_shield`, `belt_tool_l`, `belt_tool_r`, `head_hair_ornament`, `chest_talisman`, `vfx_rune_hand_l`, `vfx_rune_hand_r`, `vfx_stomp_ground`.
- Blood Axe shaman candidate locators: `staff_grip_primary`, `staff_grip_offhand`, `staff_tip_focus`, `staff_totem_focus`, `staff_ground_contact`, `back_ritual_staff`, `back_ritual_totem`, `belt_ritual_charm_l`, `belt_ritual_charm_r`, `vfx_cast_hand_l`, `vfx_cast_hand_r`, `vfx_chest_talisman`, `vfx_totem_core`, `vfx_ground_totem`.
- Candidate locators are not implemented sockets and do not authorize spell spawning, trace behavior, aura volumes, AI hooks, or VFX graph work.

Planned texture list:

- `T_GIA_BloodAxeShaman_A01_Body_BC`
- `T_GIA_BloodAxeShaman_A01_Body_N`
- `T_GIA_BloodAxeShaman_A01_Body_ORM`
- `T_GIA_BloodAxeShaman_A01_Gear_BC`
- `T_GIA_BloodAxeShaman_A01_Gear_N`
- `T_GIA_BloodAxeShaman_A01_Gear_ORM`
- `T_GIA_BloodAxeShamanStaff_A01_BC`
- `T_GIA_BloodAxeShamanStaff_A01_N`
- `T_GIA_BloodAxeShamanStaff_A01_ORM`
- Optional approval-gated `E` maps for shaman, staff, or totem only after material/VFX approval.

## Folder and Naming Recommendation

Docs:

- Package folder: `docs/assets/characters/SK_GIA_BloodAxeShaman_A01/`
- Package file: `docs/assets/characters/SK_GIA_BloodAxeShaman_A01/PRODUCTION_PACKAGE.md`

Future naming candidates:

- Character: `SK_GIA_BloodAxeShaman_A01`
- Male split if approved: `SK_GIA_BloodAxeShaman_Male_A01`
- Female split if approved: `SK_GIA_BloodAxeShaman_Female_A01`
- Staff: `SM_GIA_BloodAxeShamanStaff_A01`
- Totem: `SM_GIA_BloodAxeShamanTotem_A01`
- Character materials: `MI_GIA_BloodAxeShamanSkin_A01`, `MI_GIA_BloodAxeShamanHideFur_A01`, `MI_GIA_BloodAxeBoneStone_A01`
- Shared metal dependency: `MI_GIA_BloodAxeReforgedMetal_A01`
- Optional approval-gated glow material: `MI_GIA_BloodAxeShamanRitualGlow_A01`
- Textures: `T_GIA_BloodAxeShaman_A01_*`, `T_GIA_BloodAxeShamanStaff_A01_*`, and optional `T_GIA_BloodAxeShamanTotem_A01_*`

Future DCC source/export paths are intentionally not selected in this docs-only package. Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, validators, startup-scene actors, external concept copies, global index entries, or task-board changes from this task.

## Quality Gate Checklist

- Package is docs-only and touches only `docs/assets/characters/SK_GIA_BloodAxeShaman_A01/PRODUCTION_PACKAGE.md`.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant stoneworker, cave-town, and highland nomad culture.
- Validated Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- `A01` plans against the male 470 cm Blood Axe shaman route while preserving future female 442 cm review as approval-gated.
- Giant body mass, shoulder width, hand scale, staff read, and ritual silhouette are protected before trophy or magic detail.
- Staff, totem, chest, hand, belt, and ground locator planning is included without authoring sockets, VFX graphs, spells, traces, AI, combat behavior, or animation timing.
- Magic material notes are restrained, optional, approval-gated, and default to no emissive.
- Materials use blackened/reforged metal, scorched leather, dark hide/fur, dry bone/horn, dark ritual stone, red pigment, soot, and ash consistently.
- Default design avoids necromancer green-black, civilized Giant blue runes, broad Aetherium glow, Ogre shaman identity, and polished druid language.
- Tiny scratches, stitch rows, small glyphs, dense charm detail, fur texture, pitting, and micro cracks are assigned to texture/normal detail instead of geometry.
- Triangle budgets, material slots, texture maps, LOD0-LOD3, collision planning, animation guardrails, Unreal folder planning, and naming recommendations are included.
- No DCC source, source folder, FBX export, Unreal Content, runtime source, validator, startup placement, cloth/physics setup, VFX graph, AI, combat tuning, final visual approval, first DCC target selection, external concept copying, global index edit, or task-board update is claimed.
