# SM_GIA_BloodAxeSkinningKnife_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeSkinningKnife_A01`
- Asset type: Static Mesh prop / Giant sidearm with sheath planning
- Source kit: `KIT_GIA_BloodAxeArmory_A01`
- Source child ID: `BloodAxeArmory.png#Weapon_SkinningKnife`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Source-storage guardrail: keep `BloodAxeArmory.png` in the external source concept folder only. Do not copy, move, edit, embed, or commit the source image for this package.

`SM_GIA_BloodAxeSkinningKnife_A01` is a Giant-scale Blood Axe sidearm: a brutal utility knife for a raider, large enough to read as a short sword beside normal humanoids. The design should feel field-forged, heavy, and practical, with a broad blackened blade, oversized grip, thick guard or collar, rough leather wrap, red Blood Axe paint marks, and a heavy belt or thigh sheath. It belongs only to the Blood Axe Tribe and must not become the default visual language for neutral or civilized Giant culture.

The "skinning knife" name is an armory classification, not permission for graphic content or gameplay harvesting. The final asset should suggest hostile raider utility through scale, wear, and silhouette, while avoiding gore, explicit remains, trophy excess, or loot-system behavior.

## Gameplay Purpose

This prop supports Blood Axe Giant raiders as a sidearm, belt-carried utility blade, camp armory dressing item, weapon rack item, or non-interactive display prop. It establishes scale, sheath fit, material language, collision planning, and attachment expectations for later DCC and Unreal work without creating any runtime behavior in this package.

Expected production uses:

- Belt or thigh-mounted sidearm for Blood Axe Giant warriors, hunters, bowyers, and camp guards.
- Optional hand-held prop for animation posing or cinematic set dressing after separate animation approval.
- Armory rack, forge table, sheath, or display placement in Blood Axe camp environments.
- Scale reference for other Giant belt tools and sidearms.

Out of scope:

- Harvesting, skinning, loot, crafting, damage, finisher, or inventory mechanics.
- Graphic gore, fresh blood, explicit body-part trophies, or grisly dressing.
- Any DCC source, FBX export, Unreal Content asset, startup placement, or runtime source work.

## Silhouette Notes

The knife needs to read as a knife for a Giant rather than a normal humanoid sword. Preserve a compact sidearm profile relative to the 470 cm male Giant baseline:

- Broad single-edged or heavy leaf-like blade with a clipped, chipped, or hooked tip that remains readable at MMO camera distance.
- Thick spine and visible blade mass, but not a full cleaver silhouette.
- Oversized Giant grip with large hand clearance, palm stop, and rough wrap bands.
- Short guard, socket collar, or forged throat plate that separates blade from handle.
- Heavy pommel or ring cap sized for Giant hands and belt draw readability.
- Sheath silhouette should be nearly as important as the blade: thick leather or hide body, dark metal throat, reinforced chape, broad straps, and a large belt loop or thigh harness.

Model only the major form language. Fine chips, small scratches, pitting, stitching, tiny rivets, and minor hammer marks belong in texture and normal detail.

## Scale Notes

Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

Author in centimeters. 1 Unreal unit = 1 cm. The sidearm must be fitted to `SK_GIA_Base_A01` proportions before any future DCC work.

Suggested dimensions:

- Knife overall length: 145-175 cm.
- Blade length: 90-115 cm.
- Blade width at widest point: 18-28 cm.
- Blade thickness read: 3-6 cm at the spine, tapering at the edge.
- Handle length: 38-50 cm, with enough clearance for a Giant hand and wrap thickness.
- Sheath overall length: 105-135 cm visible body, with reinforced throat and chape.
- Sheathed carry width: target under 42 cm from belt or thigh to outer silhouette so it does not fight leg armor or bow quiver shapes.

Attachment planning:

- Primary carry: right hip or right outer thigh using existing Giant belt/tool attachment assumptions.
- Alternate carry: left hip for offhand or bowyer variants.
- Hand-held alignment: grip center should support a one-handed Giant hold.
- Sheath clearance: validate against pelvis, thigh, knee lift, walk cycle, sitting/crouch poses, and nearby quiver or trophy belt modules before implementation.

## Materials And Color Palette

Primary materials:

- Blackened iron and dark steel using the Blood Axe reforged-metal language.
- Scorched brown-black leather or hide for the grip and sheath body.
- Dark metal throat, chape, strap plates, and oversized buckle hardware.
- Deep oxide red paint, cloth tie, or carved mark as a restrained Blood Axe identifier.
- Soot, ash, dried mud, and dull edge wear on broad surfaces.
- Bone or horn may be used only as one large pommel insert or sheath toggle if it stays non-graphic and readable.

Recommended palette:

- Blackened metal: `#151719` to `#2A2C2E`
- Worn steel edge: `#555A5C` to `#787B78`
- Scorched leather: `#2A1710` to `#4A2B1A`
- Oxide red paint: `#5F1513` to `#8B211B`
- Ash and soot: `#0B0A09` to `#6A6458`
- Bone or horn accent, if used: `#8A7A5D` to `#B2A37C`

Avoid neutral/civilized Giant blue-gray stoneworker motifs, warm hearth craft language, refined carved masonry, or restrained blue rune accents unless a separate stolen-object variant is approved. No emissive is approved for the default knife.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeSkinningKnife_A01` for the world of Aerathea. The design should emphasize a Giant-scale sidearm that reads as a knife for a 442 cm female Giant and a 470 cm male Giant, a broad blackened iron blade, dark steel forged collar, scorched leather grip, heavy belt or thigh sheath, reinforced sheath throat and chape, restrained deep red Blood Axe markings, hostile Giant raider sub-faction identity, practical camp utility, and non-graphic armory display use. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean prop concept sheet with unsheathed view, sheathed view, side profile, grip callout, sheath strap callout, and scale markers beside the validated Giant baselines. Avoid copying any existing franchise, avoid graphic gore, avoid harvesting or loot-mechanic imagery, avoid making Blood Axe language the default Giant culture, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Future DCC work should build the knife as a practical Giant sidearm with optional separated sheath pieces:

- Model the blade as a broad forged form with a strong spine, simple bevels, a large edge plane, and a few major chips or dents only where they affect silhouette.
- Model the guard/collar as a chunky forged transition piece, not a delicate fantasy crossguard.
- Model the handle around Giant hand scale, with 3-5 large wrap bands or grip planes rather than many tiny spirals.
- Model the pommel as a heavy cap, ring, or blunt counterweight that supports belt draw readability.
- Model the sheath as a production-ready companion form: leather/hide shell, metal throat, metal chape, broad belt loop, optional thigh strap, and two or three large reinforcement bands.
- Keep the sheath and knife separable in planning so a future implementation can support sheathed display, unsheathed display, or hand-held prop variants without rebuilding the mesh language.
- Reserve minor scratches, leather grain, stitch rows, pitting, small red paint flakes, and tiny rivets for texture, normal, and ORM detail.

Do not model dense teeth, repeated skulls, graphic trophies, fine chain clutter, or high-frequency edge damage. The final read should come from blade mass, Giant grip scale, sheath bulk, and restrained Blood Axe markings.

## Texture And Material Notes

Target texture maps:

- `T_GIA_BloodAxeSkinningKnife_A01_BC`
- `T_GIA_BloodAxeSkinningKnife_A01_N`
- `T_GIA_BloodAxeSkinningKnife_A01_ORM`
- No default emissive map.

Material slot target:

- Preferred: 1 material slot using a compact atlas for blade, grip, sheath, straps, and hardware.
- Acceptable hero variant: 2 material slots, one for metal and one for leather/sheath, if material reuse or resolution requires it.

Suggested material instances:

- `MI_GIA_BloodAxeReforgedMetal_A01` for blade, collar, throat, chape, buckles, and strap plates.
- Future leather or hide material instance for grip wrap and sheath body.
- Future restrained red cloth/paint material mask for Blood Axe identity marks.

Texture treatment:

- Base Color: broad blackened metal planes, muted steel edge wear, scorched leather, dark straps, and restrained red paint.
- Normal: blade bevel support, large hammer marks, leather grain, broad stitch depressions, sheath seams, and controlled edge chips.
- ORM: strong cavity AO around collar, wrap overlaps, throat, chape, and strap plates; high roughness for soot and leather; metallic isolated to blade and hardware.

Avoid tiny readable text, symbol clutter, full-surface red paint, wet shine, gore coloring, or material masks that imply gameplay rarity, damage types, harvesting value, or loot state.

## Triangle Budget

Target a small-to-large Giant prop budget while preserving the blade and sheath silhouette:

- Knife only LOD0: 1.5k-2.8k tris.
- Sheath only LOD0: 1.0k-2.0k tris.
- Combined knife plus sheath display LOD0: 2.5k-4.5k tris.
- Material slots: 1 preferred, 2 maximum for an approved hero display variant.
- Texture resolution: 1K default, 2K only for hero close-up or armory catalog review.

Do not spend triangles on tiny rivets, individual stitch loops, dense scratches, or repeated micro chips. Spend them on blade bevels, grip volume, sheath bulk, reinforced throat/chape, and clean silhouette corners.

## LOD Plan

All important mesh variants need LOD0-LOD3.

- LOD0: full blade bevel, major chips, forged collar, full grip volume, pommel, sheath throat, sheath body, chape, broad straps, large buckles, and Blood Axe color blocks.
- LOD1: 60-70 percent of LOD0; reduce minor blade chips, secondary bevel loops, strap subdivisions, pommel bevels, and sheath seam geometry.
- LOD2: 35-45 percent of LOD0; simplify collar cuts, buckle shapes, sheath reinforcement bands, grip wrap divisions, and inner/backside detail.
- LOD3: 15-25 percent of LOD0; preserve knife length, blade width, grip mass, sheath outline, and red/black Blood Axe read.

Reduce tiny rivets, scratches, stitch detail, small strap ends, minor chape bevels, and backside sheath details before changing the blade mass, grip scale, or sheathed sidearm silhouette.

## Collision Notes

Collision is planning-only in this package.

- Equipped or hand-held variants: collision disabled by default; future combat packages may use trace sockets only after separate gameplay approval.
- Display or pickup-style prop variant: simple capsule or box around the sheathed knife, or two low-count convex hulls for blade and sheath if displayed separately.
- Sheath attachment: no per-strap collision; rely on character attachment clearance and simple preview bounds.
- Armory rack placement: use simple display collision that does not imply interactable loot behavior.

Suggested future trace marker names, if a combat task later approves them:

- `weapon_trace_start`
- `weapon_trace_end`

Do not add harvesting hit zones, weak points, loot collision, inventory pickup behavior, or per-edge damage volumes from this package.

## Animation Notes

Static mesh baseline. This package does not create animation, animation Blueprint logic, combat timing, draw behavior, sheath behavior, or gameplay interactions.

Future animation considerations, approval-gated:

- One-handed grip pose for Blood Axe Giants.
- Belt or thigh draw clearance with the sheath.
- Sheathed idle, walk, run, crouch, and turn-in-place clearance checks.
- Optional camp-worker or bowyer pose use as a held utility prop.

The knife should be planned so a future animator can see grip direction, draw direction, and sheath orientation without reinterpreting the asset.

## Unreal Import Notes

No Unreal Content asset is created by this docs-only package. These are planning notes for a future approved implementation task.

Planned Unreal folder:

- `/Game/Aerathea/Props/Giants/BloodAxeArmory/`

Planned asset names:

- `SM_GIA_BloodAxeSkinningKnife_A01`
- Optional future separated sheath mesh: `SM_GIA_BloodAxeSkinningKnifeSheath_A01`
- Optional future material instance names: `MI_GIA_BloodAxeSkinningKnife_A01`, `MI_GIA_BloodAxeSkinningKnifeSheath_A01`

Import planning:

- Asset type: Static Mesh.
- Pivot for unsheathed knife: primary grip center, aligned for Giant one-handed hold.
- Pivot for sheathed display: sheath belt loop or attachment point for carry variants; ground/display pivot can be a separate approved variant.
- Scale: authored in centimeters, import scale 1.0 after future DCC/export validation.
- Material slots: 1 preferred, 2 maximum.
- Collision: simple display hulls only unless a later gameplay task authorizes trace use.
- Sockets or markers to consider in a future implementation: `hand_r_weapon`, `belt_tool_r`, `belt_tool_l`, optional `belt_sidearm_r`, optional `thigh_sheath_r`, `weapon_trace_start`, `weapon_trace_end`.

Do not create startup actors, validators, Unreal assets, Blueprints, runtime source, loot behavior, or combat behavior as part of this package.

## Folder And Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeSkinningKnife_A01/`
- `docs/assets/props/SM_GIA_BloodAxeSkinningKnife_A01/PRODUCTION_PACKAGE.md`

Planned future source and content locations, not created by this task:

- Future source folder, if approved: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/SM_GIA_BloodAxeSkinningKnife_A01/`
- Future export folder, if approved: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/SM_GIA_BloodAxeSkinningKnife_A01/`
- Future Unreal folder, if approved: `/Game/Aerathea/Props/Giants/BloodAxeArmory/`

Naming examples:

- `SM_GIA_BloodAxeSkinningKnife_A01`
- `SM_GIA_BloodAxeSkinningKnifeSheath_A01`
- `T_GIA_BloodAxeSkinningKnife_A01_BC`
- `T_GIA_BloodAxeSkinningKnife_A01_N`
- `T_GIA_BloodAxeSkinningKnife_A01_ORM`
- `MI_GIA_BloodAxeSkinningKnife_A01`

Do not add global index entries, DCC files, FBX exports, Unreal Content assets, runtime source, external concept copies, or startup-scene references from this task packet.

## Approval Gates

- Stop before DCC source creation, FBX export, texture authoring, Unreal Content creation, Blueprint creation, runtime source changes, startup placement, or validator implementation.
- Stop before copying, moving, editing, embedding, or committing `BloodAxeArmory.png` or any external concept image.
- Stop if the Blood Axe red-black raider language starts replacing neutral/civilized Giant culture.
- Stop if the knife becomes a normal humanoid short sword instead of a Giant sidearm.
- Stop if sheath placement clips Giant pelvis, thigh, knee, quiver, trophy belt, or one-handed draw clearance assumptions.
- Stop before adding graphic gore, fresh blood, explicit remains, harvesting actions, loot behavior, crafting behavior, damage rules, or inventory claims.
- Stop before using emissive effects, shamanic glow, heat states, or animated material states without a separate visual approval.

## Quality Gate Checklist

- Asset remains original to Aerathea and tied to the Blood Axe hostile Giant sub-faction only.
- Blood Axe remains separate from neutral/civilized Giant stoneworker and highland culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Knife reads as a Giant sidearm and a short-sword-scale object beside normal humanoids.
- Sheath, belt loop, thigh strap, grip direction, and draw clearance are planned.
- No graphic gore, harvesting mechanic, loot behavior, crafting behavior, or inventory claim is included.
- Silhouette is readable through blade mass, grip scale, collar, pommel, sheath body, throat, chape, and broad Blood Axe markings.
- Materials use blackened iron, dark steel, scorched leather, soot, ash, dull edge wear, and restrained red paint.
- Tiny scratches, stitch rows, pitting, rivets, and leather grain are assigned to textures or normals, not dense geometry.
- Texture maps include Base Color, Normal, and packed ORM; no default emissive map is approved.
- Triangle budgets, LOD0-LOD3, material slot targets, collision planning, sockets/markers, animation notes, and Unreal planning notes are included.
- Package makes no DCC, FBX, Unreal Content, runtime source, source asset, global index, startup-scene, source-concept-copying, or final visual approval claim.
