# SK_GIA_BloodAxeShieldCarrier_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_BloodAxeShieldCarrier_A01`
- Asset type: Skeletal Mesh character variant production package; future hostile Blood Axe Giant shield-carrier visual row only after later approval
- Parent route: `KIT_GIA_BloodAxeWarband_A01#ShieldCarriers`
- Source route references: `Bloodaxe Army.png`, `GiantBloodAxeMale4.png`, and `GiantBloodAxeMaleandFemale.png` from the Giant Blood Axe slate
- Existing dependencies: `SK_GIA_Base_A01`, `KIT_GIA_BloodAxeWarband_A01`, `KIT_GIA_BloodAxeArmory_A01`, `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeRaiderChest_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, `SK_GIA_BloodAxeGreaves_A01`, and `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, runtime source, source asset folder, validator, startup placement, final visual approval, final wearable fit, final animation timing, shield prop build, or first DCC target selection is included
- Source-storage guardrail: external source concept images remain outside the repository. Do not copy, move, edit, embed, or commit external source concepts for this package.

`SK_GIA_BloodAxeShieldCarrier_A01` defines a hostile Blood Axe Giant visual archetype built around a massive front-facing shield mass, heavy shoulders, thick forearms, broad feet, and a braced stance read. The shield and stance are visual planning only: they establish a silhouette for concept, production, and future fit review, not a shield behavior system.

This character must read as a Giant first, a Blood Axe raider second, and a shield carrier third. The Blood Axe material language is hostile sub-faction language: blackened iron, dark steel, scorched leather, rough hide, soot, ash, deep red cloth, dry trophy accents, and brutal camp-forged utility. It must not become neutral/civilized Giant culture. Civilized Giant stoneworker identity, blue-gray cave-town masonry, warm hearth language, restrained blue runes, and highland nomad neutrality belong to separate Giant packages.

The shield itself may become a separate future static mesh dependency if approved, with a candidate name such as `SM_GIA_BloodAxeRaidShield_A01`. This package does not create, finalize, or authorize that prop. It only describes the character silhouette, future attachment expectations, material language, and stop gates needed before any implementation lane begins.

## Gameplay Purpose

Gameplay purpose is visual role only. This package supports a readable Blood Axe warband roster row at MMO camera distance: a towering hostile Giant carrying a huge shield-shaped mass, framed by heavy Blood Axe armor and a grounded posture.

Allowed visual-production uses:

- Concept sheet planning for a broad shield-bearing Blood Axe Giant silhouette.
- Future character outfit planning against the validated Giant scale baselines.
- Future attachment review for a large shield prop, harness, chest armor, belt/tassets, greaves, and optional side gear.
- Non-final roster readability planning beside Blood Axe chieftain, shaman, hunter, raider, banner bearer, forge guard, trophy carrier, and camp sentry rows.
- Material coordination with the Blood Axe armory and wearable gear packages.

Out of scope:

- No shield blocking mechanics, shield behavior, stamina rules, guard meters, block arcs, impact reactions, bash rules, hit volumes, damage zones, weak points, combat traces, projectile rules, encounter role, AI class, combat stats, abilities, loot, patrol behavior, spawn logic, or objective behavior.
- No DCC source, Blender file, sculpt, retopo, UV, bake, FBX export, Unreal Content asset, Blueprint behavior, runtime source, validator, startup placement, or copied source concept art.
- No final wearable skeletal fit, skin weighting, physics asset tuning, cloth simulation, animation timing, montage timing, or final visual approval.

## Silhouette Notes

Primary silhouette: a towering Blood Axe Giant with a huge shield-forward read, broad shoulders rising behind the shield, heavy hands gripping or supporting the shield mass, thick forearms, wide hips, sturdy legs, and oversized feet planted in a visually braced posture. The body must not vanish behind the shield; the head, shoulder width, forearm size, feet, and red-black Blood Axe material blocks need to remain readable from front and three-quarter views.

Core silhouette goals:

- Preserve the Giant scale read: tall head height, heavy brow, thick neck, wide shoulders, long powerful arms, huge hands, broad torso, sturdy legs, and large feet.
- Use the shield as a dominant front-facing mass, but leave enough exposed anatomy and gear to identify the wearer as a Blood Axe Giant rather than a walking prop.
- Favor one large shield outline: brutal tower, slab, hide-and-metal wall, or irregular reinforced oval-rectangle. Avoid many small shield plates that break the read.
- Keep the shield top below or near the lower face line in neutral concept pose so the head and brow remain visible for character identity.
- Let the shoulder line read above or around the shield through asymmetrical spaulders, fur/hide pads, or heavy harness straps.
- Use wide forearms and thick hand positions to sell shield weight visually, without locking an animation or gameplay function.
- Use a few large edge breaks, repair plates, rim chunks, or warning cloth strips as Blood Axe identity. Avoid dense spikes, rivet fields, teeth curtains, and small dangling clutter.
- Keep the lower silhouette grounded with thick greaves, broad boots, and a wide stance read that remains visual planning only.

Potential shield visual directions for later approval:

- Reforged slab shield: dark steel plates, blackened iron rim, large central boss, crude repair bars, and deep red cloth tags.
- Hide-and-plank shield: dark timber or hide core, rawhide lashing, blackened edge plates, and sparse bone anchors.
- Stolen-plate shield: mismatched metal panels reforged into a Giant-scale wall, with one or two broken enemy-shield fragments as non-graphic trophies.

Avoid:

- Neutral/civilized Giant stoneworker motifs as the baseline.
- Normal humanoid tower-shield proportions scaled up without Giant hand, forearm, shoulder, and foot mass.
- Shield silhouettes that cover the entire character and hide race identity.
- Excessive skull repetition, graphic gore, wet blood, readable text, franchise-like symbols, dense chains, tiny rivets, or noisy micro-detail.
- Magic glow or aura effects as the baseline.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author all future measurements in centimeters. 1 Unreal unit = 1 cm.
- Feet at world origin and orientation should follow the future Giant base import convention.

Primary planning target:

- `A01` should be reviewed first against the male 470 cm baseline because the shield carrier read depends on maximum shoulder width, hand size, and shield mass.
- Female 442 cm fit review remains required if a female variant or shared wearable solution is later approved.
- Normal humanoid compatibility is not required.

Shield mass visual planning:

- Shield height candidate: roughly 260-340 cm, sized to read as Giant-scale without hiding the full head and shoulder identity.
- Shield width candidate: roughly 130-210 cm, wide enough for a heavy front read while preserving arm and side silhouette.
- Shield thickness candidate: roughly 18-45 cm at the rim and reinforcement zones, with the broad face kept readable rather than overbuilt.
- Back grip or forearm support zone: sized to Giant hands and forearms only after a future prop package and socket review.
- Shield lower edge: should visually clear the feet enough for stance readability in concept pose; no movement or gameplay clearance is finalized here.
- Shield weight, mass, and braced stance are visual planning language only, not simulation, mechanics, or collision behavior.

Future fit and clearance checks before any implementation claim:

- Neck, head, shoulder, elbow, wrist, hand, pelvis, thigh, knee, ankle, and foot clearance against the validated Giant body.
- Shield front view, three-quarter view, side view, and back carry view if a later task approves back carry.
- Compatibility with `SK_GIA_BloodAxeRaiderChest_A01`, `SK_GIA_BloodAxeHarness_A01`, `SK_GIA_BloodAxeTrophyBelt_A01`, and `SK_GIA_BloodAxeGreaves_A01`.
- Candidate use of inherited Giant sockets such as `hand_l_offhand` and `back_shield`; no new socket contract is authorized here.

## Materials and Color Palette

Primary Blood Axe shield-carrier materials:

- Weathered Giant skin with soot, scars, ash, and broad red war paint.
- Blackened iron, dark steel, and reforged stolen metal matching or consuming `MI_GIA_BloodAxeReforgedMetal_A01`.
- Scorched leather, dark hide, rough fur pads, rawhide wraps, sinew cord, and heavy harness straps.
- Dark timber, battered hide, or reforged plate surfaces for the future shield face.
- Deep oxide red cloth, dirty red war paint, and chipped red marks as Blood Axe identifiers.
- Old bone, horn, broken weapon fragments, shield fragments, and dry trophy tokens used sparingly and non-graphically.
- Soot, ash, mud, oil-dark grime, broad hammer marks, worn metal edges, and large hand-painted wear.

Suggested palette:

- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#555A5C` to `#787B78`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Scorched leather: `#241611` to `#4A2E20`
- Dark hide/fur: `#1D1511` to `#3B2A1E`
- Old bone/horn: `#A69578` to `#D0B98C`
- Dark timber or burned plank: `#1E1712` to `#3A2A1C`
- Soot and grime: `#0B0A09` to `#403025`

No default emissive is approved. Forge heat, ritual glow, shamanic markings, shield glow, faction aura, animated material states, or glowing eyes require a separate visual/material approval and must not be assumed for `A01`.

Avoid civilized Giant blue-gray stoneworker colors, hearth warmth, calm carved masonry marks, restrained blue rune language, or polished civic craft motifs as the baseline.

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_GIA_BloodAxeShieldCarrier_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant shield-carrier visual archetype, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, towering broad anatomy, huge hands, thick forearms, heavy shoulders visible behind a massive front-facing shield, a visually braced stance, blackened reforged iron, dark steel, scorched leather, rough hide, dark timber or battered shield plates, deep oxide red cloth markers, soot, ash, sparse non-graphic trophy accents, preserved Giant body mass, and a gameplay purpose as visual roster readability only with no shield mechanics. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a character production sheet with front, side, back, three-quarter views, shield front/back callouts, hand and forearm grip callouts, shoulder and foot visibility callouts, material swatches, LOD simplification notes, and scale markers beside female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines on a clean background. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid dense shield clutter, avoid final wearable-fit claims, avoid DCC or Unreal implementation claims, avoid shield blocking mechanics, avoid hit volume diagrams, avoid combat stats or abilities, avoid AI or encounter-role diagrams, avoid readable text, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, mesh, sculpt, retopo, UV, bake, FBX export, Unreal Content asset, skeletal fit, socket authoring, physics asset, cloth setup, animation timing, runtime behavior, or final visual approval is created or approved by this package.

Future character modeling should prioritize:

- Reuse the validated Giant base proportions and skeleton assumptions before adding Blood Axe gear.
- Preserve Giant head, brow, neck, chest, shoulders, forearms, huge hands, pelvis, sturdy legs, large feet, and grounded body mass.
- Build Blood Axe wearable language from large readable modules: raider chest, harness, shoulder armor, belt/tassets, greaves, boots, fur/hide pads, and broad red cloth marks.
- Keep the front view clear enough that the shield, head, shoulders, hands, feet, and Blood Axe color blocks all read at MMO camera distance.
- Use rigid, large-form trophy accents only where they support the silhouette; avoid graphic or dense trophy treatment.
- Prefer modular character gear and a separate future shield prop if implementation later proceeds.

Future shield modeling, if separately approved, should prioritize:

- One dominant shield slab or shield-wall face with a clear rim silhouette.
- Large rim plates, central boss or grip housing, major repair bands, broad straps, and arm brace forms as real geometry.
- A readable back side with Giant-scale forearm strap, hand grip, or support brace, without finalizing socket or animation behavior.
- Sparse large trophy, red cloth, or broken-plate accents that do not cover the main shield face.
- Display and carried variants split later if pivot, thickness, collision, or material needs diverge.

Texture or normal-map:

- Tiny rivets.
- Fine scratches.
- Dense pitting.
- Small hammer marks.
- Stitch rows.
- Leather pores.
- Hide grain.
- Wood grain.
- Small red paint chips.
- Soot speckles.
- Minor edge nicks.
- Bone or horn hairline cracks.

Model as real geometry:

- Primary Giant body forms.
- Major armor plates.
- Shield slab, rim, boss, large repair bands, main grip structure, major straps, oversized buckles, broad tassets, greaves, and large rings.

Do not model:

- Shield behavior diagrams, invisible mechanics, impact fields, block arcs, hit volumes, damage zones, stamina indicators, UI symbols, projectile effects, aura rings, VFX cards, dense chain curtains, gore ropes, fresh remains, tiny teeth strings, or readable text.

## Texture and Material Notes

Target texture families for a future approved build:

- `T_GIA_BloodAxeShieldCarrier_A01_Body_BC`
- `T_GIA_BloodAxeShieldCarrier_A01_Body_N`
- `T_GIA_BloodAxeShieldCarrier_A01_Body_ORM`
- `T_GIA_BloodAxeShieldCarrier_A01_Gear_BC`
- `T_GIA_BloodAxeShieldCarrier_A01_Gear_N`
- `T_GIA_BloodAxeShieldCarrier_A01_Gear_ORM`
- `T_GIA_BloodAxeShieldCarrier_A01_HairFur_BC`
- `T_GIA_BloodAxeShieldCarrier_A01_HairFur_N`
- `T_GIA_BloodAxeShieldCarrier_A01_HairFur_ORM`
- Candidate future shield textures only after a separate shield prop approval: `T_GIA_BloodAxeRaidShield_A01_BC`, `T_GIA_BloodAxeRaidShield_A01_N`, `T_GIA_BloodAxeRaidShield_A01_ORM`
- Optional future approval-gated emissive texture: `T_GIA_BloodAxeShieldCarrier_A01_E` or `T_GIA_BloodAxeRaidShield_A01_E`

Material slot target for the character:

- Slot 0: body/head/skin war paint.
- Slot 1: eyes, hair, and fur, or split eyes if the future base convention requires it.
- Slot 2: `MI_GIA_BloodAxeReforgedMetal_A01` or equivalent for blackened iron, dark steel, chipped red paint masks, and hammered plates.
- Slot 3: scorched leather, dark hide, red cloth, harness wraps, and rough fur pads.
- Slot 4: optional bone/horn/trophy material only if shared atlas readability cannot handle these accents.

Material slot target for a future shield prop:

- Preferred: 1-2 material slots for metal/hide/timber/red cloth.
- Maximum: 3 material slots only if a separately approved shield variant needs metal, organic face material, and trophy/cloth separation.
- Do not create one-off material slots for every strap, plate, trophy, nail, paint mark, or repair piece.

Packed `ORM` plan:

- R: Ambient occlusion around armor overlaps, shield rim seams, grip housing, strap compression, belt/tasset hinges, greave undercuts, hand-contact zones, and trophy anchors.
- G: High roughness for soot, leather, hide, old bone, timber, matte blackened metal, and weathered skin; slightly lower roughness on rubbed steel edges, shield rim wear, and hand-contact hardware.
- B: Metallic only for iron, steel, buckles, rings, chain links, shield plates, rim bands, and armor plates.

Readability requirements:

- Keep the shield face broad and value-separated so it does not become a flat black rectangle.
- Keep red accents sparse and large enough to identify Blood Axe allegiance without overpowering the Giant body.
- Use broad wear, soot, ash, and edge highlights at Giant scale.
- Avoid readable text, franchise-like symbols, loot-rarity colors, fresh blood shine, damage-state masks, weak-point marks, shield-health indicators, or material states that imply gameplay behavior.
- No baseline emissive, animated material state, heat glow, ritual glow, shield glow, pulsing eyes, or faction aura is approved.

## Triangle Budget

`SK_GIA_BloodAxeShieldCarrier_A01` is a repeated hostile Giant character variant with a large visual shield dependency, not a named boss or raid-scale hero.

Target budget for a future approved fully dressed character:

- Character LOD0 target excluding separate shield prop: 55k-72k tris for body, head, hair/fur, armor, harness, belt/tassets, greaves, broad red cloth markers, and controlled trophies.
- Character LOD0 hard cap excluding shield: 75k tris unless a later named hero variant receives separate approval.
- Future shield prop LOD0 target if approved separately: 8k-14k tris for one Giant-scale shield with slab, rim, grip, straps, repair plates, and broad accents.
- Future shield prop LOD0 hard cap: 16k tris only if visual approval requires stronger rim depth or major back-side construction.
- Assembled review target including character and shield: 65k-86k tris.
- Assembled review hard cap including character and shield: 90k tris without separate hero approval.
- Material slots: 4 target for character, 5 maximum if necessary; shield 1-2 target, 3 maximum after approval.
- Texture resolution: 2K standard for body, gear, and shield sets; 4K only for an approved named hero, boss close-up, or marketing render variant.

Budget distribution guidance for the character excluding shield:

- Body, head, hands, feet, and base anatomical forms: 45-55 percent.
- Armor plates, shoulder forms, belt, greaves, and boots: 22-30 percent.
- Harness straps, rings, buckles, red cloth, hair/fur clumps, and stance read: 12-18 percent.
- Sparse trophies and secondary accents: 5-8 percent.

Budget distribution guidance for a future shield:

- Shield slab, rim, and back plate mass: 45-55 percent.
- Grip housing, forearm brace, major straps, and large buckles: 18-25 percent.
- Repair plates, boss, edge breaks, and broad bevels: 15-22 percent.
- Sparse trophy and red cloth accents: 5-10 percent.

Do not spend geometry on tiny rivets, dense chain links, fine stitches, hair strands, micro scratches, repeated tooth strands, small gore detail, or hidden back-side clutter.

## LOD Plan

All future character and shield meshes require LOD0-LOD3.

- LOD0: full Giant body mass, face planes, hands, feet, hair/fur clumps, broad shield silhouette, shoulder armor, harness, belt/tassets, greaves, major straps, shield rim, shield boss/grip forms, red cloth markers, sparse large trophies, and primary Blood Axe color blocks.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small strap loops, hair/fur subdivisions, small buckle edges, secondary trophy cuts, shield repair-plate bevels, and underside armor details.
- LOD2: 35-45 percent of LOD0; simplify fingers, inner armor folds, back-side straps, tasset detail, trophy forms, fur clumps, shield grip interior, shield back-side detail, and secondary cloth folds while preserving the shield-carrier read.
- LOD3: 15-25 percent of LOD0; preserve height, head, shoulders, huge hands, foot stance, broad shield outline, shield rim block, red/black Blood Axe material blocks, and overall Giant scale.

LOD reduction order:

1. Tiny rivets, scratches, stitches, pitting, leather pores, wood grain cuts, and small paint flakes.
2. Small strap loops, knots, buckle bevels, and minor chain segments.
3. Small trophy fragments, tiny bone chips, minor cloth tears, and small rim notches.
4. Under-armor and back-side shield detail.
5. Secondary hair/fur cuts and non-silhouette folds.
6. Minor armor plate bevels and shield repair-plate bevels.
7. Only after all secondary detail is reduced, simplify the head, shoulders, hands, feet, stance, shield outline, and major Blood Axe color blocks.

Never reduce the validated Giant scale read, shoulder line, heavy hands, head silhouette, broad foot stance, or shield outline before removing small detail.

## Collision Notes

No collision, physics asset, movement capsule edit, shield collision, shield behavior, hit volume, or gameplay trigger is authored or approved in this docs-only package.

Future collision planning:

- Character collision type: Giant-tuned movement capsule inherited from `SK_GIA_Base_A01` conventions.
- Male 470 cm planning capsule: roughly 470 cm height and 100-125 cm radius, pending future implementation validation.
- Female 442 cm planning capsule, if a variant is approved: roughly 442 cm height and 95-115 cm radius.
- Physics asset should use simplified bodies for pelvis, spine, chest, head, upper/lower arms, hands, grouped fingers, thighs, calves, feet, and only approved large hair/fur/gear bodies.
- Worn armor and gear should normally rely on the owning Giant physics asset and simple bounds, not per-strap or per-trophy collision.
- If a future shield prop is approved, equipped shield collision should remain disabled by default unless a separate gameplay task explicitly authorizes behavior. Display-only shield variants may use simple box or low-count convex bounds.

Do not add shield block volumes, damage zones, weak points, bash volumes, per-plate collision, per-strap collision, per-chain collision, per-cloth collision, per-trophy collision, projectile collision, nav blockers, spawn blockers, interaction triggers, pickup collision, loot collision, or encounter scripting from this package.

## Animation Notes

No animation, Animation Blueprint, montage, authored timing, cloth simulation, secondary motion, physics setup, shield behavior, or final pose set is created or approved here.

Future animation review may evaluate only approval-gated visual clearance, not gameplay behavior:

- Heavy idle readability with shield mass visible.
- Walk, jog, and turn-in-place clearance around shield, shoulders, hands, belt, knees, and feet.
- Front-facing braced concept pose as a visual stance only.
- Hand and forearm contact readability for a future shield prop.
- Back carry clearance only if a later shield prop task approves that visual state.
- Overlap review with chest armor, harness, trophy belt, greaves, optional side gear, and the future shield mesh.

No timing, attack, reaction, block, bash, stagger, AI state, encounter behavior, shield function, stamina rule, hit response, or ability animation is authorized by this package.

Rigid straps, rigid shield components, and sparse rigid trophies should be preferred for the first visual plan. Long cloth strips, swinging chains, dangling trophies, simulated straps, or secondary shield motion require separate approval and validation.

## Unreal Import Notes

This section is planning only. No Unreal Content, Skeletal Mesh, Static Mesh, material instance, texture, Blueprint, physics asset, validator, startup actor, or runtime file is created by this package.

Planned Unreal folders after later approval:

- Character: `/Game/Aerathea/Characters/Giants/BloodAxe/Warband/`
- Gear dependencies: `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/`
- Candidate future shield prop: `/Game/Aerathea/Shields/Giants/BloodAxe/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned asset naming:

- Character skeletal mesh: `SK_GIA_BloodAxeShieldCarrier_A01`
- Candidate future shield prop: `SM_GIA_BloodAxeRaidShield_A01` or another lead-approved Blood Axe Giant shield name
- Physics asset, if later approved: `PHYS_GIA_BloodAxeShieldCarrier_A01`
- Animation Blueprint, if later approved: `ABP_GIA_BloodAxeShieldCarrier_A01`
- Material instance examples: `MI_GIA_BloodAxeShieldCarrier_Body_A01`, `MI_GIA_BloodAxeShieldCarrier_Gear_A01`, `MI_GIA_BloodAxeRaidShield_A01`

Expected import assumptions for future work:

- Asset type: Skeletal Mesh character, with any shield authored as a separate Static Mesh dependency unless a later implementation task approves a different split.
- Pivot: character feet at world origin. Future shield prop pivot should be at the back grip or forearm support center unless display-only needs require a separate variant.
- Scale: centimeter authored, Unreal import scale 1.0 after DCC/export rules are established by a future task.
- Collision: inherit Giant capsule and simplified physics asset conventions; no shield behavior collision from this package.
- LODs: LOD0-LOD3 required for both character and shield prop if implemented.
- Material slots: character 4 target, 5 maximum; shield 1-2 target, 3 maximum only after approval.
- Texture list: `BC`, `N`, packed `ORM`; no `E` unless a separate visual/material task approves emissive.
- Sockets: candidate use of inherited `hand_l_offhand` and `back_shield` only after fit review; no new socket contract is authorized by this package.
- Animation list: none authored here. Future clearance poses require animation approval and do not define combat behavior.
- Blueprint behavior: none.
- AI/combat behavior: none.
- Startup placement: none.
- Performance note: repeated warband use should prefer shared materials, separate reusable shield props, aggressive LODs, and no per-piece collision.

## Folder and Naming Recommendation

- Docs: `docs/assets/characters/SK_GIA_BloodAxeShieldCarrier_A01/`
- Package: `docs/assets/characters/SK_GIA_BloodAxeShieldCarrier_A01/PRODUCTION_PACKAGE.md`
- Related parent kit: `docs/assets/kits/KIT_GIA_BloodAxeWarband_A01/`
- Related armory kit: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/`
- Related gear package docs: `docs/assets/characters/SK_GIA_BloodAxeHarness_A01/`, `docs/assets/characters/SK_GIA_BloodAxeRaiderChest_A01/`, `docs/assets/characters/SK_GIA_BloodAxeTrophyBelt_A01/`, `docs/assets/characters/SK_GIA_BloodAxeGreaves_A01/`

Do not create or modify `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, FBX exports, Blender files, global indexes, task boards, backlog files, bootstrap files, validators, startup-scene actors, external source concept folders, or source concept images from this package.

## Approval and Stop Gates

- Lead approval is required before selecting `SK_GIA_BloodAxeShieldCarrier_A01` as a DCC, Unreal, runtime, visual review, or first build target.
- Visual approval is required before locking the final shield-carrier silhouette, shield shape, stance read, trophy density, red cloth placement, or material distribution.
- Culture approval is required if Blood Axe shield-carrier language starts replacing neutral/civilized Giant culture.
- DCC approval is required before creating source folders, Blender files, proof renders, mesh sources, LOD sources, collision proxies, UVs, bakes, or FBX exports.
- Unreal approval is required before importing Skeletal Meshes, Static Meshes, materials, textures, physics assets, Blueprints, validators, or startup actors.
- Shield prop approval is required before creating, naming, modeling, exporting, importing, or attaching any Blood Axe Giant shield mesh.
- Wearable-fit approval is required before claiming the shield, harness, chest armor, belt, greaves, or any gear fits either Giant baseline.
- Animation approval is required before authoring poses, montages, locomotion variants, shield-carry motion, braced-pose timing, cloth, chain motion, physics, or deformation tests.
- Gameplay approval is required before defining shield blocking mechanics, shield behavior, stamina rules, combat stats, abilities, hit volumes, weak points, damage zones, encounter role, AI, patrols, spawns, loot, objectives, or interaction rules.
- Source-storage approval is required before any external source concept file is copied, moved, edited, embedded, or committed.
- Stop immediately if a future task would require edits outside its owned scope, source-art movement, final visual approval, DCC/FBX/Unreal creation, runtime changes, or gameplay system definition without explicit authorization.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved female range 14-15 ft / 427-457 cm, and approved male range 14'10"-16'0" / 452-488 cm.
- Gameplay purpose is visual role only and does not define shield mechanics, hit volumes, stamina, encounter role, AI, combat stats, abilities, or loot.
- Shield mass and braced stance are visual planning only.
- No DCC, FBX, Unreal Content, SourceAssets, runtime source, validators, startup placement, global index, task-board, backlog, bootstrap, source concept movement, or final visual approval is claimed.
- Silhouette preserves the Giant body read: head, shoulder width, huge hands, sturdy legs, large feet, and massive scale remain visible around the shield.
- Materials use blackened iron, dark steel, scorched leather, rough hide, soot, ash, deep red cloth, and sparse dry trophies consistently.
- Neutral/civilized Giant stoneworker motifs, warm hearth identity, blue-gray civic masonry, and restrained blue rune language are excluded from the baseline.
- Tiny rivets, scratches, stitching, pitting, wood grain, leather pores, small paint chips, and minor shield wear are assigned to textures or normals.
- Emissive use is absent by default and approval-gated for any future variant.
- Triangle budgets, texture maps, material slot targets, LODs, collision limits, animation limits, Unreal path planning, folder/naming recommendations, approval gates, and source-storage guardrails are included.
- Package is useful for production planning without overclaiming implementation readiness.
