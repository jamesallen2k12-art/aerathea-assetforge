# SM_GIA_BloodAxeCrusherHammer_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeCrusherHammer_A01`
- Asset type: Static Mesh / Giant two-handed blunt weapon production package
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source child ID: `BloodAxeArmory.png#Weapon_CrusherWarHammer`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Source-storage guardrail: the source concept remains in the external concept folder only; do not copy, move, edit, embed, or commit it for this package.

`SM_GIA_BloodAxeCrusherHammer_A01` is a massive Blood Axe raider hammer built around broad blunt impact mass, overhand readability, and brutal reforged-metal utility. It should contrast the Blood Axe double axe by reading as a crushing block weapon first: a slab-heavy head, long wrapped haft, large forged bands, and a weight-forward profile that clearly telegraphs overhead smashes at MMO camera distance.

This asset belongs only to the hostile Blood Axe Giant sub-faction. It must not replace or redefine neutral/civilized Giant culture, which remains tied to mountain stonework, cave towns, restrained blue-gray materials, and practical highland craft.

## Gameplay Purpose

The hammer supports Blood Axe Giant crusher units, heavy raiders, camp guards, elite brutes, and possible chieftain variants. Its main gameplay read is a slow, dangerous two-handed impact weapon used for overhand slams, ground-shock attacks, barricade smashing, intimidation poses, and heavy back-carry silhouettes.

Expected uses:

- Equipped two-handed weapon for hostile Giant melee combat packages.
- Display or pickup prop in Blood Axe armories, forge camps, weapon racks, and loot scenes.
- Readable encounter telegraph for overhead windup, high guard, downward smash, and recovery poses.
- Environmental storytelling prop that suggests stolen metal reforged into a crude but effective war tool.

This package does not define final damage values, combat trace timing, animation assets, Blueprint behavior, DCC geometry, FBX export, Unreal Content assets, or startup placement.

## Silhouette Notes

Primary read: a huge rectangular or slightly wedge-shaped hammer head mounted on a long Giant haft. The head should feel like a portable battering ram, with broad impact faces, thick side plates, and only a few giant-scale fasteners. The weapon should look top-heavy enough that a normal humanoid could not plausibly wield it.

Key silhouette requirements:

- Broad blunt head mass is the hero shape; avoid blade-forward or axe-like reads.
- Overhand readability must be strong from front, side, and three-quarter views.
- Long haft gives enough spacing for Giant two-handed grip and sweeping body mechanics.
- Head width should be visibly wider than the haft and grip wraps, with a clear impact face.
- Reinforcing bands should be large, simple, and readable, not dense strips of tiny metal.
- Red cloth or red paint should identify Blood Axe allegiance without overwhelming the blackened metal silhouette.
- Optional trophy language must be restrained: one large bone charm, tooth bundle, or skull fragment maximum unless a future hero variant is approved.

Avoid:

- Dense tiny rivets, nail forests, wire wraps, micro gears, or excessive chain clutter.
- Spiked mace language that turns the asset into a different weapon type.
- Graphic gore or fresh blood detail.
- Neutral/civilized Giant blue-gray stoneworker motifs unless explicitly used as a stolen defaced object in a later variant.

## Scale Notes

Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

Additional scale rules:

- Author in centimeters. 1 Unreal unit = 1 cm.
- Target total length: 320-380 cm.
- Target hammer head width: 105-145 cm across the broad impact face.
- Target hammer head height/depth: 65-95 cm, with enough volume to read as blunt impact mass.
- Target haft diameter: 16-24 cm at the main grip, tapering only where readability allows.
- Target two-handed grip span: 85-125 cm between primary and offhand grip centers.
- Back-carry version must clear the Giant shoulder, neck, and head silhouette without hiding the full body mass.
- Hand and socket fit must be validated against `SK_GIA_Base_A01`, not against normal humanoid scale.
- Normal humanoid compatibility is not required unless a future loot-display or trophy-scale task asks for a separate reduced variant.

Socket and grip dependencies inherited from the Giant base package:

- `hand_r_weapon`
- `hand_r_twohand_grip`
- `hand_l_twohand_grip`
- `back_large_weapon`
- `weapon_trace_start`
- `weapon_trace_end`

Suggested mesh marker names for a future DCC pass:

- `grip_primary`
- `grip_offhand`
- `impact_face_center`
- `hammer_head_top`
- `hammer_head_bottom`
- `back_carry_anchor`

## Materials And Color Palette

Primary materials:

- Blackened iron and dark steel for the hammer head, side plates, bands, and end cap.
- Reforged stolen metal with broad hammer marks, soot, heat discoloration, rough dents, and chipped edges.
- Scorched leather, hide, and wrapped cord for the Giant grip.
- Torn red cloth strips or dull red war paint as Blood Axe identifiers.
- Bone, horn, or tooth accents used sparingly as hostile trophy language.
- Ash, grime, oil-dark roughness, and baked dirt in recessed areas.

Palette:

- Charcoal black, dark iron gray, soot brown, dull steel highlights.
- Deep dried red for cloth and paint accents.
- Aged leather browns and desaturated hide tans.
- Muted bone ivory only for limited trophies.
- No default emissive treatment.

Keep Blood Axe material language separate from neutral/civilized Giant culture. This hammer should not use the civilized Giant stoneworker palette as its default identity.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeCrusherHammer_A01` for the world of Aerathea. The design should emphasize a Giant-scale block-headed crusher hammer, broad blunt impact mass, a long two-handed wrapped haft, overhand attack readability, blackened iron, dark steel, reforged stolen metal, scorched leather, dull red Blood Axe cloth and paint, restrained bone trophy accents, hostile Giant raider identity, and a gameplay role as a slow heavy impact weapon for Blood Axe crusher units. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a weapon concept sheet and turnaround on a clean background with scale callouts against the female Giant baseline 442 cm / 14'6" and male Giant baseline 470 cm / 15'5", grip markers, impact-face callouts, and back-carry notes. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe language the default Giant culture, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This package is a planning document only. Future DCC work should build the primary shapes first:

- Large hammer head block with broad impact faces and thick bevels.
- Reinforced side plates or cap plates that make the head feel reforged and brutal.
- Heavy central socket or collar where the head clamps around the haft.
- Long wooden or iron-cored haft scaled for Giant hands.
- Primary and offhand grip wraps with large, readable leather bands.
- Heavy pommel or butt cap for counterweight and back-carry readability.
- A small number of oversized bolts, pegs, clamps, or pins if needed for construction logic.
- Large chips, dents, asymmetrical hammered planes, and worn corners as sculpted silhouette accents.

Use texture and normal detail for:

- Fine scratches.
- Small pitting.
- Tiny rivets.
- Shallow edge nicks.
- Leather pores.
- Stitching.
- Grime streaks.
- Hammer marks that do not affect the silhouette.

The head should remain simpler and broader than a spiked mace. Any spikes should be absent or limited to blunt corner lugs that support the hammer shape rather than changing the weapon category. Keep the asset mid-poly and production-friendly; do not model every wrap thread, dent, nail, or scrap seam.

## Texture And Material Notes

Material slot target:

- Preferred: 1 material slot using a single weapon texture set.
- Maximum: 2 material slots if metal and haft/leather separation is required for reuse.
- Do not add one-off material slots for individual straps, trophies, red cloth, or grime.

Texture list:

- `T_GIA_BloodAxeCrusherHammer_A01_BC`
- `T_GIA_BloodAxeCrusherHammer_A01_N`
- `T_GIA_BloodAxeCrusherHammer_A01_ORM`
- `T_GIA_BloodAxeCrusherHammer_A01_E` only if a future approved ritual or forge-heat variant requires emissive.

Material instances:

- `MI_GIA_BloodAxeCrusherHammer_A01`
- May inherit from `MI_GIA_BloodAxeReforgedMetal_A01` or a future shared Blood Axe weapon master material.

Texture treatment:

- Paint broad value separation between impact faces, reinforcing bands, haft, wraps, and red accents.
- Bake ambient occlusion into recesses under bands, around socket collars, under grip wraps, and inside large chips.
- Use normal-map dents and pitting instead of dense modeled damage.
- Keep metal rough and dark, with limited bright edge highlights for readability.
- Keep red cloth/paint worn, torn, and matte rather than clean or decorative.
- Emissive is absent by default; this is a blunt raider weapon, not a magical artifact.

## Triangle Budget

Target budget:

- LOD0: 5k-9k tris.
- LOD0 hard cap: 10k tris.
- Material slots: 1 preferred, 2 maximum.
- Texture resolution: 1K standard, 2K for hero or boss-equipped variant only.

Suggested LOD0 allocation:

- Hammer head, impact faces, socket, and bevels: 2.5k-4.5k tris.
- Haft, grip wraps, and pommel: 1.5k-3k tris.
- Large clamps, pins, red cloth, and restrained trophy accent: 500-1.5k tris.

This is a large prop / hero weapon. Spend triangles on the head mass, readable bevels, grip fit, and silhouette breaks before spending them on small metal dressing.

## LOD Plan

All important equipped and display versions need LOD0-LOD3.

- LOD0: full block head, major bevels, reinforced plates, socket collar, haft, grip wraps, pommel, large chips, red cloth, and any restrained trophy accent.
- LOD1: 60-70 percent of LOD0; simplify minor chips, secondary bevel loops, small cloth tears, small pins, and underside detail.
- LOD2: 35-45 percent of LOD0; simplify grip-wrap segmentation, trophy accent geometry, rear-side plates, socket interior cuts, and small silhouette dents.
- LOD3: 15-25 percent of LOD0; preserve the block head, long haft, primary grip span, red color block, and top-heavy hammer read.

Reduction order:

1. Tiny rivets, scratches, small pins, and narrow bands.
2. Cloth tear subdivisions and minor leather wrap cuts.
3. Secondary chipped corners and small dents.
4. Back-side or underside plate breaks.
5. Trophy accent geometry.
6. Minor socket/collar bevels.
7. Haft subdivisions.

Never reduce the broad blunt head mass, overhand silhouette, impact face, or Giant grip spacing before secondary decoration.

## Collision Notes

Equipped collision should be disabled by default. Combat should rely on future trace sockets such as `weapon_trace_start`, `weapon_trace_end`, and an impact-center marker, but this package does not define final trace behavior.

Display and pickup collision:

- One simple box or convex hull around the hammer head.
- One capsule or box around the haft.
- Optional small box around the pommel if needed for floor placement.
- No per-bolt, per-chip, per-wrap, or per-trophy collision.
- Walkable collision should remain disabled unless a future environment-cover variant is approved.

If a world prop version is needed, create simple collision that supports rack placement, ground placement, and interaction targeting without simulating the weapon's exact silhouette.

## Animation Notes

Static mesh baseline. No animation assets are created or approved by this docs-only package.

Future animation alignment requirements:

- Two-handed idle with the head weight visibly carried low or over the shoulder.
- Overhand windup with clear upward lift and readable pause before impact.
- Downward smash with the impact face leading the motion.
- Ground-slam or barricade-smash variant, if approved by gameplay.
- Recovery animation that sells heavy mass and slow momentum.
- Back-carry attach pose that keeps the hammer clear of the Giant head, shoulders, and spine.

Grip markers must support both dominant-hand and offhand placement on `SK_GIA_Base_A01`. Animation timing, damage windows, camera shake, VFX, hit reactions, and gameplay effects require separate approval.

## Unreal Import Notes

Planned Unreal asset:

- Static Mesh: `SM_GIA_BloodAxeCrusherHammer_A01`
- Folder: `/Game/Aerathea/Weapons/Giants/BloodAxe/`
- Asset type: Static Mesh
- Collision type: simple custom collision for display/pickup variants; disabled collision for equipped combat variant
- Import scale: 1.0 after centimeter-authored DCC export in a future task
- Pivot: primary grip center aligned for `hand_r_weapon`; display-only variant may use a duplicate with a floor/rack placement pivot if approved
- Orientation: align the haft for Giant hand attachment and keep the broad impact face easy to inspect in a weapon preview
- LODs: LOD0, LOD1, LOD2, LOD3 required
- Material slots: 1 preferred, 2 maximum

Planned texture assets:

- `T_GIA_BloodAxeCrusherHammer_A01_BC`
- `T_GIA_BloodAxeCrusherHammer_A01_N`
- `T_GIA_BloodAxeCrusherHammer_A01_ORM`
- `T_GIA_BloodAxeCrusherHammer_A01_E` only for a future approved emissive variant

Planned material instance:

- `MI_GIA_BloodAxeCrusherHammer_A01`

Planned attachment and trace references:

- `hand_r_weapon`
- `hand_r_twohand_grip`
- `hand_l_twohand_grip`
- `back_large_weapon`
- `weapon_trace_start`
- `weapon_trace_end`
- `impact_face_center`

Do not create Unreal Content assets, Blueprints, combat traces, gameplay behavior, startup-scene actors, source assets, DCC files, or FBX exports from this task.

## Folder And Naming Recommendation

Docs path:

- `docs/assets/props/SM_GIA_BloodAxeCrusherHammer_A01/PRODUCTION_PACKAGE.md`

Planned Unreal path for a future implementation task:

- `/Game/Aerathea/Weapons/Giants/BloodAxe/SM_GIA_BloodAxeCrusherHammer_A01`

Recommended names:

- Static Mesh: `SM_GIA_BloodAxeCrusherHammer_A01`
- Material Instance: `MI_GIA_BloodAxeCrusherHammer_A01`
- Base Color: `T_GIA_BloodAxeCrusherHammer_A01_BC`
- Normal: `T_GIA_BloodAxeCrusherHammer_A01_N`
- Packed ORM: `T_GIA_BloodAxeCrusherHammer_A01_ORM`
- Optional Emissive: `T_GIA_BloodAxeCrusherHammer_A01_E`

Future DCC, export, Unreal, source asset, global index, and startup-scene paths require separate approval and are intentionally not created by this package.

## Approval Gates

- Stop before any DCC, Blender, FBX, Unreal Content, runtime source, source asset, global index, startup-scene, or external concept-folder work.
- Stop before copying, embedding, editing, moving, or committing the external `BloodAxeArmory.png` source concept.
- Stop if the hammer loses its broad blunt impact mass or starts reading as an axe, mace, spear, or magic staff.
- Stop if tiny metal clutter, dense rivets, chains, trophies, or scratches begin to overpower the primary silhouette.
- Stop if Blood Axe raider language starts replacing neutral/civilized Giant culture.
- Stop if the Giant scale lock or `SK_GIA_Base_A01` socket assumptions appear insufficient for two-handed grip, back carry, or overhand readability.
- Visual approval is required before final head proportions, trophy density, red accent placement, and material breakup are locked.
- Gameplay approval is required before combat trace timing, damage arcs, impact VFX, camera shake, knockback, destructible behavior, or loot rules are authored.

## Quality Gate Checklist

- Asset is original to Aerathea and belongs to the Blood Axe Tribe as a hostile Giant sub-faction.
- Blood Axe visual language remains separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- The hammer reads as a broad blunt impact weapon, not an axe or spiked mace.
- Overhand attack readability is supported by head mass, haft length, grip spacing, and impact-face orientation.
- Tiny metal clutter is reduced; small rivets, scratches, pitting, stitching, and grime are texture or normal-map details.
- Materials use blackened iron, dark steel, reforged metal, scorched leather, dull red cloth/paint, soot, and restrained bone accents.
- Emissive is absent by default and approval-gated for any future ritual or forge-heat variant.
- Triangle budget, material slot target, texture list, LOD plan, collision plan, sockets, animation notes, and Unreal import notes are included.
- Package makes no DCC, FBX, Unreal Content, source asset, global index, startup placement, or final visual approval claim.
- Source concept remains external and is not copied, moved, edited, embedded, or committed by this package.
