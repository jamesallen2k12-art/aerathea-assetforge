# SK_OGR_Warrior_Rival_A01 Production Package

## Art Direction Summary

`SK_OGR_Warrior_Rival_A01` is the first Ogre melee pressure unit for `KIT_GNM_OGR_RivalryEncounter_A01`. It uses the approved Ogre male scale and body mass, then adds brutal front-line gear: spiked blackened-iron shoulders, heavy bracers, strapped plate skirt, a huge tower shield, and a chained crusher hammer with restrained forge-orange glow windows.

The Warrior should feel less technical than `SK_OGR_Teknomancer_A01`: simpler, meaner, and more direct. Any magic-tech details are crude forge reinforcements, not gnomish precision.

Shared final-art fit source: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/OGRE_SHARED_RIG_FINAL_ART_FIT_PLAN.md`. This class remains bound to `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton` and should be the second class overlay fit after Teknomancer.

## Gameplay Purpose

- Provides the first Ogre melee rival for Gnome Heavy Mek and shield-wall encounter tests.
- Supports warrior waves, shield-bearer elites, gate defenders, and siege push units.
- Establishes shield/hammer sockets for later combat animation, impact VFX, shield slam logic, and encounter Blueprint assembly.
- Gives designers a non-Teknomancer Ogre comparison in the startup scene.

## Silhouette Notes

- Preserve the Ogre male base: broad chest, huge arms, thick neck, large hands, heavy forward stance.
- Add a dominant left-side tower shield that reads at MMO camera distance.
- Add a right-hand chained crusher hammer with a blocky head and forge glow windows.
- Use large shoulder plates, bracers, knee guards, belt disk, and hanging plate skirt.
- Use spikes sparingly as large silhouette points; do not model hundreds of tiny rivets or chains.

## Scale Notes

- Body target: male Ogre, 330 cm baseline.
- Shield target: 230-260 cm tall, wide enough to cover most of the Ogre side profile.
- Hammer target: 190-230 cm overall handle/head read.
- Pivot: ground center between feet inherited from the Ogre base skeleton.
- Startup actor should stage near the Ogre Teknomancer and Gnome Heavy Mek without blocking the shield-wall read.

## Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Ogre skin | umber, ash-brown, ochre | exposed body, face, hands |
| Warpaint | dark red-brown | chest marks, arm marks, intimidation pattern |
| Blackened iron | dark steel, soot-black iron | shield frame, bracers, shoulder plates, hammer head |
| Leather/fur | scorched brown, dirty red cloth | straps, skirt, wraps, belt hangers |
| Bone/trophies | aged ivory | skull charms, teeth, shield trophies |
| Forge glow | restrained orange | shield windows, hammer core, belt disk |

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_OGR_Warrior_Rival_A01`, an Ogre warrior rival for the world of Aerathea. The design should emphasize a massive broad 10-11 ft Ogre male body, spiked blackened-iron shoulder armor, huge bracers, rough leather straps, red-brown warpaint, a strapped plate skirt, a massive tower shield with crude forge-orange glow windows, a chained crusher hammer, bone trophies, dirty battlefield confidence, and a brutal melee role against Gnome Heavy Meks. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a character production sheet with front, side, back, three-quarter, weapon callouts, socket callouts, shield callout, material swatches, and scale beside a Gnome Heavy Mek. Avoid copied franchise designs, excessive micro-rivets, unreadable chain noise, photoreal clutter, text, and watermarks.

## Modeling Notes

- Build the first pass as gear over the existing Ogre male base source pattern.
- Model real geometry for the tower shield, hammer, shoulder plates, bracers, knee guards, belt disk, plate skirt, large spikes, and big trophies.
- Texture or normal-map tiny rivets, scratches, cloth weave, small chain links, small runes, and fine surface dents.
- Shield and hammer should be removable modules in the final rig pass.
- First DCC pass validates silhouette, sockets, scale, and startup placement only.

## Texture And Material Notes

- `T_OGR_Warrior_Rival_A01_BC`
- `T_OGR_Warrior_Rival_A01_N`
- `T_OGR_Warrior_Rival_A01_ORM`
- `T_OGR_Warrior_Rival_A01_E`
- Use packed ORM: Occlusion, Roughness, Metallic.
- Emissive map only for forge windows, hammer core, belt disk, and optional eye/impact VFX points.

## Triangle Budget

- Review blockout LOD0 target: under 35k tris.
- Final common warrior target: 35k-55k tris including gear.
- Elite shield-bearer or named champion may reach 60k-70k only if justified.
- Material slot target: 4-5 total.

## LOD Plan

- LOD0: full Ogre body, tower shield, hammer, shoulders, bracers, belt, skirt plates, major spikes, sockets.
- LOD1: 55-60 percent; reduce bevels, secondary straps, small trophies, and shield frame cuts.
- LOD2: 25-35 percent; merge skirt plates, simplify spikes, remove minor hangers and small chain hints.
- LOD3: 10-15 percent; preserve Ogre body mass, shield slab, hammer block, shoulder width, and forge glow read.

## Collision Notes

- Use Ogre character capsule for movement.
- Physics asset can be generated for first-pass review; final pass needs tuned simplified bodies for shield, hammer, torso, arms, and legs.
- Weapon and shield impact logic should use sockets/traces rather than detailed mesh collision.
- Disable collision on minor trophy and skirt detail.

## Animation Notes

Initial animation targets:

- Heavy idle.
- Shield brace.
- Shield slam.
- One-handed hammer swing.
- Two-handed overhead smash.
- Forward charge.
- Stagger into shield.
- Stomp.
- Taunt/roar.
- Hit reaction.
- Death/fall.

Required sockets:

- `hand_r_weapon`
- `hand_l_offhand`
- `hand_r_twohand_grip`
- `hand_l_twohand_grip`
- `back_large_weapon`
- `back_shield`
- `belt_front`
- `vfx_belt_forge`
- `vfx_shield_core`
- `vfx_hammer_core`
- `vfx_stomp_ground`
- `head_fx`

## Unreal Import Notes

- Asset type: Skeletal Mesh class variant.
- Primary mesh: `SK_OGR_Warrior_Rival_A01`.
- Skeleton: `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton`.
- Physics asset: `PHYS_OGR_Warrior_Rival_A01`.
- Animation Blueprint placeholder: `ABP_OGR_Warrior_Rival_A01`.
- Unreal path: `/Game/Aerathea/Characters/Ogres/Warrior/`.
- Startup actor: `AET_PROD_OgreWarrior_Rival_A01`.
- Scale: centimeters, imported with the same Ogre review import scale as `SK_OGR_Teknomancer_A01`.

## Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_OGR_Warrior_Rival_A01/`
- Source: `SourceAssets/Blender/Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01/`
- Export: `SourceAssets/Exports/Characters/Ogres/Warrior/SK_OGR_Warrior_Rival_A01/`
- Unreal: `/Game/Aerathea/Characters/Ogres/Warrior/`
- DCC script: `Tools/DCC/build_ogre_warrior.py`
- Unreal import script: `Tools/Unreal/import_ogre_warrior.py`

## Quality Gate Checklist

- Reads as a broad 10-11 ft Ogre, not a tall human.
- Final art follows the Ogre shared rig fit plan and remains bound to the validated male Ogre skeleton.
- Warrior silhouette is distinct from Teknomancer: shield and hammer, not reactor cannon.
- Tower shield and hammer read at gameplay distance.
- Glow is sparing and forge-like.
- Major forms are real geometry; small detail belongs to texture/normal maps.
- Triangle budget, texture maps, sockets, LODs, collision, animation targets, and Unreal paths are defined.
