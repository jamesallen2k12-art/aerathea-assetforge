# SM_GIA_BloodAxeLongbow_A03 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeLongbow_A03`
- Asset type: Static Mesh weapon / Giant longbow
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source intake child ID: `BloodAxeArmory.png#Bow_Longbow_03`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Variant role: heavier battle-scarred longbow variant with red wrap and stronger silhouette breaks
- Status: docs-only production package ready; DCC build not started
- Source-storage guardrail: the source concept remains external and must not be copied, moved, edited, embedded, or committed for this task.

`SM_GIA_BloodAxeLongbow_A03` is the heavier battle-scarred Blood Axe Giant longbow variant. It should read as an older, brutally maintained war bow: thicker asymmetric stave, patched limb repairs, larger nocks, reinforced grip, red wrap, blackened iron bands, and a controlled number of visible damage marks. It remains a visual and production variant only. Do not imply higher damage, longer range, rarity, elite status, or any combat advantage over other Blood Axe longbows.

Variant distinction:

- `SM_GIA_BloodAxeLongbow_A01`: largest baseline longbow silhouette with a deep crescent arc, sparse trophy binding, and balanced giant-scale raider read.
- `SM_GIA_BloodAxeLongbow_A02`: cleaner wrapped-stave variant for common Blood Axe archers, per the armory intake note. It should read less repaired, less scarred, and more uniform than A03.
- `SM_GIA_BloodAxeLongbow_A03`: heavier battle-scarred variant with thicker asymmetric limbs, brutal repaired metal bands, heavier nocks, red wrap, and readable damage language that is visible but not dense.

Blood Axe visual language must stay separate from neutral/civilized Giant culture. This package describes hostile Giant raider equipment only; it must not redefine all Giants as Blood Axe raiders.

## Gameplay Purpose

This asset supports future Blood Axe Giant archer silhouettes, camp sentries, raider armory racks, bowyer repair scenes, loot-display props, and scale validation for Giant bow handling. It is useful as a visual alternative to A01 and the cleaner A02 variant, giving Blood Axe camps a repaired battlefield equipment read without creating new gameplay rules.

Expected use cases:

- Equipped two-handed ranged weapon mesh for Blood Axe Giant NPC visuals.
- Armory, rack, wall-leaning, or ground display prop in Blood Axe camps.
- Bowyer repair reference that pairs with `KIT_GIA_BloodAxeBowParts_A01`.
- Scale and attachment planning reference for `KIT_GIA_BloodAxeQuivers_A01` arrows and back quiver clearance.
- Variant dressing for hostile Blood Axe spaces where repeated A01 bows would look too uniform.

Do not define projectile behavior, damage values, range, charge behavior, hit logic, ammunition rules, arrow flight, draw timing, release timing, reload timing, inventory behavior, or loot rarity in this package.

## Silhouette Notes

Primary silhouette: a massive Giant-scale longbow with a heavy crescent profile, thicker uneven stave limbs, an offset repaired limb section, oversized center grip, broad horn or iron nocks, a visible string line, and a few large repair bands that break the outline. The bow should look patched after many raids, but still functional and readable from MMO camera distance.

Required A03 visual cues:

- Thicker asymmetric stave compared with A01 and the cleaner A02 wrapped-stave variant.
- One limb should carry a larger repaired splint or blackened iron band stack, creating a deliberate silhouette break.
- Nocks should be heavier than A01: broader horn/iron caps, deeper grooves, and more blocky end shapes.
- Damage marks should be visible at the silhouette and material level, but not dense: a handful of large chips, cracks, flattened cuts, and scorch scars.
- Red wrap should be bolder than A01, concentrated near the grip and one repaired limb, not spread across the full bow.
- Trophy language must stay sparse. Use one bone tag, broken tooth, or cloth charm cluster at most, and keep it away from the grip and nock readability.

Avoid elegant Elven bow language, clean neutral Giant craft, blue runes, civic stoneworker motifs, dense skull rows, tiny thorn fields, and fine damage noise that would disappear in-game.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: female Giants 14-15 ft / 427-457 cm; male Giants 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Target proportions for DCC planning:

- Resting bow height: 420-465 cm from lower nock to upper nock.
- Primary limb thickness: 16-28 cm through the heavier stave sections, with uneven hand-shaped transitions.
- Repaired splint/band zone: 55-95 cm long, with broad metal banding and one main patch area.
- Grip height: 48-62 cm, sized for a Giant hand and thick wrap.
- Grip depth/diameter: 18-28 cm depending on wrap and palm-stop mass.
- Nock/tip assemblies: 36-55 cm long per end, with clear string grooves and wider silhouette than A01.
- Resting string offset: enough to read from front and side without defining final draw mechanics.
- Back-carry envelope: must clear Giant head, shoulders, trophy armor, `back_quiver`, and `back_large_weapon` space.

The bow must be checked against the Giant base before any future build promotion. Attachment and draw references should assume a 470 cm male Giant for maximum practical clearance, then confirm the female baseline remains usable without changing the race scale lock.

## Materials and Color Palette

Primary materials:

- Dark highland hardwood or laminated stave, stained with soot and hand-painted grain.
- Blackened iron and dark steel repair bands with hammered broad wear.
- Scorched leather grip wrap, rawhide bindings, sinew lashings, and heavy cord.
- Horn, bone, or crude iron nock caps.
- Dull red cloth wrap and red war-paint streaks as Blood Axe identifiers.
- Small bone/tooth trophy tag used sparingly.
- Soot, ash, grime, rubbed edges, flattened chips, scorch scars, and broad repaired cracks.

Color language:

- Base: dark brown, charcoal, blackened iron, gray-brown wood, dirty leather, and soot-black recesses.
- Accent: dull Blood Axe red concentrated at grip wraps, one limb repair, or a single hanging strip.
- Wear: exposed pale wood cuts, rubbed metal edges, dark grime, and muted bone/horn.
- Emissive: none for this baseline package.

Avoid neutral/civilized Giant blue-gray stoneworker motifs, warm hearth symbolism, restrained blue rune language, carved civic stone, or peaceful highland craft markers. Those belong to non-Blood Axe Giant packages unless a later stolen-object variant is approved.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeLongbow_A03` for the world of Aerathea. The design should emphasize a massive Giant-scale heavier battle-scarred longbow, thick asymmetric dark hardwood stave, brutal repaired blackened-iron bands, oversized horn or iron nocks, heavy scorched-leather grip, dull red Blood Axe wrap, sparse bone or tooth tag, visible but not dense chips and scorch scars, hostile Blood Axe Giant raider identity, grim bowyer repair culture, and visual use as a ranged weapon and camp armory prop. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, strung/resting callouts, grip detail, nock detail, repaired limb detail, damage-density examples, back-carry clearance sketch, quiver dependency note, and scale callouts against female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5" Giants on a clean background. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid readable text, avoid combat stat callouts, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This package is documentation only. Future DCC work should model the big readable forms first and keep small damage in texture/normal detail.

Model real geometry for:

- Continuous curved bow stave with heavier asymmetric limb thickness than A01.
- One major repaired limb zone with broad blackened-iron bands and a large splint plate.
- Oversized center grip with raised palm stop, scorched leather wrap, and clear Giant hand fit.
- Heavier upper and lower nock assemblies with horn/iron caps, blocky end forms, and visible string grooves.
- Rest-position string as a clean thin element or separable string subpiece if a later rigged variant needs it.
- Major reinforcement plates near the grip and tips.
- A small number of large chips or broken silhouette cuts that read from distance.
- One optional sparse trophy tag or red cloth strip placed away from the nock and grip function.
- Back-carry loop or strap anchor markers as broad fittings, not tiny rings.

Use texture and normal maps for:

- Wood grain, fine cracks, small scratches, pitting, soot streaks, leather grain, sinew fibers, small stitch marks, rubbed edges, and minor metal hammer marks.
- Repeated small scars, tiny rivets, dense lashings, knot clusters, fine string fibers, and small trophy marks.

DCC planning notes:

- Keep the bow functional despite the scarred read. The stave may be asymmetric, but the nock-to-nock arc and grip alignment must still make sense.
- Place repair bands where they enhance silhouette without blocking the string line or arrow rest.
- A03 should not become a collapsed pile of repairs. Use one hero repair zone and two or three secondary scars at most.
- The grip, arrow rest, string anchors, and back-carry references must remain clearer than the damage detail.

## Texture and Material Notes

Texture set target: 2K for the baseline weapon. Use 4K only if a future named boss or hero variant approves it.

Required texture names:

- `T_GIA_BloodAxeLongbow_A03_BC`
- `T_GIA_BloodAxeLongbow_A03_N`
- `T_GIA_BloodAxeLongbow_A03_ORM`

Optional texture name:

- `T_GIA_BloodAxeLongbow_A03_E` only for a separately approved ritual or shamanic variant, not for this baseline.

Material instance:

- `MI_GIA_BloodAxeLongbow_A03`

Material slot target:

- 1 material slot preferred for the full bow.
- 2 material slots maximum if a future DCC pass needs separated string/leather from stave/metal.
- Do not add separate material slots for each repair band, cloth strip, tooth tag, crack, scratch, or wrapping layer.

Packed ORM guidance:

- Strong AO under repair bands, wraps, splints, nock caps, and grip overhangs.
- High roughness on wood, leather, horn, bone, soot, and cloth.
- Controlled metallic response on blackened iron and rubbed band edges.
- No glow for baseline Blood Axe longbow A03.

Damage texture guidance:

- Use a few bold scars and large hand-painted crack shapes.
- Keep fine scratches, pitting, and edge chips broad enough to support the hand-painted MMO style.
- Avoid dense all-over damage noise that would make A03 read muddy beside A01 and A02.

## Triangle Budget

- LOD0 target: 6k-9k tris.
- LOD0 hard cap: 10k tris if heavier nocks, repair bands, and grip mass require extra silhouette support.
- Material slots: 1 target, 2 maximum.
- Texture set: 2K baseline.

Budget priorities:

- Spend geometry on the bow arc, asymmetric stave thickness, grip, heavy nocks, string line, major repair bands, and one sparse trophy or red cloth accent.
- Use texture and normal detail for dense cracks, scratches, pitting, lashings, fibers, tiny rivets, and small scorch marks.
- A03 can be heavier than A01 in silhouette, but it should still remain within a large-prop MMO-safe budget.

## LOD Plan

All important production variants need LOD0-LOD3.

- LOD0: full heavy bow arc, asymmetric stave thickness, oversized grip, heavy nocks, string line, main repaired limb zone, broad metal bands, red wrap, visible major chips, and optional sparse trophy tag.
- LOD1: 60-70 percent of LOD0; simplify wrap bevels, reduce band bevels, merge small chips, reduce trophy/tag shape, simplify secondary scars, and reduce nock cap bevel detail.
- LOD2: 35-45 percent of LOD0; flatten secondary repair cuts, merge small bands into broader shapes, simplify string support, reduce nock caps, and preserve the main repaired-limb silhouette break.
- LOD3: 15-25 percent of LOD0; preserve the longbow arc, grip mass, string line, larger nock endpoints, one repaired limb mass, and red faction color block.

Reduce details in this order: fine scratches and pitting, tiny stitch marks, secondary wrap cuts, small cloth tears, minor chips, small strap loops, trophy bevels, back-side details, secondary band bevels, then large repair plate simplification. Never reduce the main bow arc, grip, heavy nocks, string line, or primary repaired-limb silhouette before removing small detail.

## Collision Notes

Equipped baseline collision should be disabled. Combat traces, projectile collision, hit detection, arrow collision, and damage volumes are future gameplay-system work and are not defined here.

Display or pickup variants may use simple collision only:

- One long capsule or narrow box following the main bow height.
- One small box around the grip if pickup focus is later required.
- Optional simple convex hull around the major repaired-limb mass for display placement.
- No per-string collision.
- No individual repair-band collision.
- No individual trophy, cloth-strip, crack, chip, or nock-groove collision.
- No arrow or projectile collision in this package.

Back-carry collision should rely on character attachment bounds or a simple non-blocking preview volume only. The bow must not create blocking collision that catches on Giant armor, quivers, camp props, or nearby weapons.

## Animation Notes

Static mesh baseline. Do not author animation timing, final draw length, release timing, reload timing, projectile spawn behavior, combat montage rules, cloth simulation, physics simulation, or runtime equip behavior in this package.

Future animation and socket review notes:

- Bow grip: align central grip to Giant hand sockets, defaulting to a left-hand bow grip review unless gameplay later requests mirrored use.
- Nock: reserve a clear arrow rest and nock reference near the grip and string line for future Giant arrow alignment.
- Draw: include a documentation point for `socket_string_pull_ref`, but leave draw distance and timing to a future Giant bow animation package.
- String anchors: top and bottom nock/string anchors must remain visually clear for a future string deformation or swapped string mesh plan.
- Back carry: support attachment to `back_large_weapon` or a future bow-specific back socket without clipping shoulders, trophy armor, hair, or quiver.
- Quiver dependency: `KIT_GIA_BloodAxeQuivers_A01` defines final arrow scale, `back_quiver` clearance, arrow reach, and draw-from-quiver dependencies before final animation approval.

## Unreal Import Notes

Planned future asset only; this package does not create Unreal Content, DCC files, FBX exports, startup actors, runtime source, validators, or final visual approval.

- Planned Unreal path: `/Game/Aerathea/Weapons/Giants/BloodAxe/SM_GIA_BloodAxeLongbow_A03`
- Planned asset type: Static Mesh
- Import scale: 1.0 after future DCC/export approval, authored in centimeters
- Pivot: center of the main bow grip
- Forward/orientation: align to the project weapon convention during future DCC handoff; document any deviation before import
- Collision: disabled for equipped use; simple display collision only if a pickup/display variant is approved
- Material slots: 1 target, 2 maximum
- LODs: LOD0, LOD1, LOD2, LOD3 required
- Performance note: preserve the bow arc, heavy nocks, and repaired-limb silhouette at distance; move small wear into textures

Recommended mesh sockets/locators for future import:

- `socket_bow_grip`
- `socket_arrow_rest`
- `socket_arrow_nock`
- `socket_string_top`
- `socket_string_bottom`
- `socket_string_pull_ref`
- `socket_back_carry_attach`
- `socket_quiver_alignment_ref`
- `socket_repair_band_ref`

Expected character-side socket dependencies:

- `hand_l_offhand` or future `bow_grip_l`
- `bow_string_pull_r`
- `arrow_nock`
- `back_large_weapon`
- `back_quiver`

These are planning names only. Final socket naming, projectile spawn rules, animation timing, import settings, and visual approval require future assigned tasks.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeLongbow_A03/`
- Production package: `docs/assets/props/SM_GIA_BloodAxeLongbow_A03/PRODUCTION_PACKAGE.md`
- Planned Unreal folder after approval: `/Game/Aerathea/Weapons/Giants/BloodAxe/`
- Planned mesh name: `SM_GIA_BloodAxeLongbow_A03`
- Planned material instance: `MI_GIA_BloodAxeLongbow_A03`
- Planned textures: `T_GIA_BloodAxeLongbow_A03_BC`, `T_GIA_BloodAxeLongbow_A03_N`, `T_GIA_BloodAxeLongbow_A03_ORM`

DCC source folders, FBX export folders, Unreal Content assets, runtime source, startup-scene placement, external concept storage, validators, task-board updates, backlog edits, bootstrap edits, and global index edits are intentionally out of scope for this docs-only task.

## Docs-Only Guardrails

This package is documentation only. It explicitly does not authorize or perform:

- No DCC or Blender source creation.
- No FBX export.
- No Unreal import or Unreal Content asset creation.
- No projectile behavior.
- No animation timing.
- No combat stats, damage values, range values, rarity, loot rules, or gameplay advantage claims.
- No source concept copying, moving, editing, embedding, or committing.
- No startup placement, review actor placement, startup scene edits, or visual approval capture.
- No final visual approval.
- No runtime source, validator, task-board, backlog, bootstrap, global index, or external source concept folder edits.

Promotion beyond this docs-only package requires a separate assigned DCC, Unreal, gameplay, animation, or visual review task.

## Approval Gates

- Stop before DCC mesh creation, Blender source creation, FBX export, Unreal Content import, runtime source changes, startup-scene placement, validator creation, or final visual approval.
- Stop before copying, moving, editing, embedding, or committing the external source concept.
- Stop if the bow appears sized for normal humanoids instead of the Giant scale lock.
- Stop if Blood Axe raider language begins to overwrite neutral/civilized Giant culture.
- Stop if A03 loses its distinct heavier battle-scarred identity and becomes either the A01 baseline longbow or the cleaner A02 wrapped-stave variant.
- Stop if skulls, trophies, gore, rivets, lashings, cracks, chips, scorch marks, or repair bands become dense enough to hurt mid-poly readability.
- Stop before defining final projectile gameplay, combat traces, hit behavior, arrow inventory rules, draw distance, draw timing, release timing, reload timing, damage values, range values, or animation montage timing.
- Stop before final bow approval if `KIT_GIA_BloodAxeQuivers_A01` has not resolved back quiver clearance, arrow scale, and draw-from-quiver dependency.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges female Giants 14-15 ft / 427-457 cm and male Giants 14'10"-16'0" / 452-488 cm.
- A03 is clearly distinct from `SM_GIA_BloodAxeLongbow_A01` and the cleaner `SM_GIA_BloodAxeLongbow_A02` intake variant.
- A03 reads as a heavier battle-scarred variant through thicker asymmetric stave, brutal repaired metal bands, heavier nocks, red wrap, and visible but not dense damage language.
- No stat, damage, range, rarity, loot, or combat advantage claim is made.
- Bow height, grip, nock, repaired limb, draw reference, string anchor, back carry, and quiver dependency notes are included.
- Final projectile gameplay and animation timing are not defined.
- Primary silhouette reads as a massive Giant longbow at MMO camera distance.
- Materials use dark hardwood, blackened iron, dark steel, horn/bone, scorched leather, rawhide, sinew, soot, grime, and dull red Blood Axe cloth/paint consistently.
- Emissive is absent by default and approval-gated for any future ritual or shamanic variant.
- Tiny rivets, scratches, string fibers, dense lashings, pitting, wood grain, stitch marks, and minor chips are assigned to textures or normals instead of geometry.
- Texture maps, material slot limits, triangle budgets, LOD0-LOD3, collision, socket planning, Unreal import planning, folder naming, approval gates, and docs-only guardrails are included.
- The package makes no DCC, FBX, Unreal Content, runtime source, global index, external concept copy, startup-scene placement, or final visual approval work claim.
