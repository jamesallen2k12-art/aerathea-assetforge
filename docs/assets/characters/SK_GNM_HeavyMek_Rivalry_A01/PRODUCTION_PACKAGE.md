# SK_GNM_HeavyMek_Rivalry_A01 Production Package

## Art Direction Summary

`SK_GNM_HeavyMek_Rivalry_A01` is the generic Gnome/Mekgineer heavy combat Mek for `KIT_GNM_OGR_RivalryEncounter_A01`. It is not the named Iona hero Mek. This asset establishes the reusable encounter-class silhouette: a tiny visible gnome pilot seated in an oversized dark-iron and brass frame with massive shoulders, heavy boots, a bright blue Aetherium chest reactor, a cannon/tool arm, a hammer or breaching arm, and blue shield-ready socket points.

The design language is precise and engineered, unlike Ogre Teknomancy. Forms should feel clever, compact, layered, and mechanically deliberate, with large readable plates and sparing blue glow rather than dense micro-rivets or noisy gears.

## Gameplay Purpose

- Provides the first full-body Gnome heavy Mek scale and silhouette target for Gnome-vs-Ogre encounter staging.
- Supports defensive line encounters, shield-wall reinforcement, cannon recoil tests, anti-Ogre pressure, and future Mek pilot animation planning.
- Bridges `BP_GNM_HeavyMekShieldwall_A01`, `SK_GNM_Base_A01`, and future named hero assets from `KIT_GNM_IonaSiegebreaker_A01`.
- Gives designers sockets for shield VFX, reactor VFX, cannon fire, stomp effects, pilot hatch interaction, and tool/weapon attachment.

## Silhouette Notes

- Overall read: 340-380 cm tall heavy Mek frame with a visible 100-115 cm gnome pilot.
- Primary shapes: huge rounded shoulder housings, deep chest core, high cockpit ring, thick mechanical arms, oversized armored boots, and compact back reactor stacks.
- Left arm should read as cannon or shield projector capable.
- Right arm should read as tool-hammer or breaching weapon capable.
- Pilot should remain visible enough to preserve gnome scale and identity.
- Avoid Ogre-like crude asymmetry. This is heavy, but still engineered and intentional.

## Scale Notes

- Gnome pilot: approximately 110 cm visible body reference.
- Heavy Mek frame: first-pass review target 360 cm to sit above Minotaurs but below Ogres and far below Giants.
- Pivot: ground center between the Mek feet.
- Cockpit socket should align near the visible pilot hatch.
- Shield sockets should align to forearm/shoulder emitter locations and later attach to `BP_GNM_HeavyMekShieldwall_A01`.

## Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Dark iron | charcoal, blue-gray blackened steel | main armor plates, joints, boots |
| Brass and copper | warm brass, dull copper, worn gold edges | trim, rings, piston housings, reactor cages |
| Aetherium | blue, cyan, blue-white | chest reactor, cannon muzzle, shield sockets, back core |
| Pilot materials | gnome skin, workwear blue, leather gloves, bright hair accent | visible pilot, goggles, harness |
| Blue heraldry panels | desaturated deep blue with brass trim | shoulder caps, chest banner, knee plates |

Glow must stay limited to core, cannon muzzle, reactor stack, shield sockets, and small sensor lenses.

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_GNM_HeavyMek_Rivalry_A01`, a generic Gnome/Mekgineer heavy combat Mek for the world of Aerathea. The design should emphasize a tiny visible gnome pilot seated inside a 360 cm oversized combat frame, huge rounded dark-iron shoulder armor, brass and copper engineered trim, a bright blue Aetherium chest reactor, heavy armored boots, a cannon or shield-projector left arm, a hammer/tool right arm, compact back reactor stacks, clean gnome engineering, and a defensive rivalry role against massive Ogre warriors. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing blue emissive accents, and MMO-friendly production design. Present it as a character sheet with front, side, back, three-quarter, pilot hatch callout, weapon socket callouts, scale beside a 110 cm gnome and 335 cm Ogre, material swatches, and animation state notes. Avoid copied franchise designs, excessive rivets, unreadable micro-gears, photoreal noise, text, and watermarks.

## Modeling Notes

- Build large body plates, boots, gauntlets, cockpit ring, reactor housing, cannon barrel, hammer head, shoulder shells, and back stacks as real geometry.
- Fake tiny rivets, panel scratches, gauge ticks, soot, and small wire detail in texture and normal maps.
- Keep the pilot visible as a simplified seated bust for the first pass; final pilot/vehicle separation can happen later.
- Use broad plate seams and clear silhouette breaks so the Mek reads at MMO camera distance.
- Leave enough space around shoulders and elbows for future animation deformation.
- First DCC pass validates scale, sockets, and review placement only.

## Texture And Material Notes

Texture targets:

- `T_GNM_HeavyMek_Rivalry_A01_BC`
- `T_GNM_HeavyMek_Rivalry_A01_N`
- `T_GNM_HeavyMek_Rivalry_A01_ORM`
- `T_GNM_HeavyMek_Rivalry_A01_E`
- `T_GNM_HeavyMekPilot_Rivalry_A01_BC`
- `T_GNM_HeavyMekPilot_Rivalry_A01_N`
- `T_GNM_HeavyMekPilot_Rivalry_A01_ORM`

Material targets:

- `MI_GNM_HeavyMek_Rivalry_A01_DarkIron`
- `MI_GNM_HeavyMek_Rivalry_A01_Brass`
- `MI_GNM_HeavyMek_Rivalry_A01_BluePanel`
- `MI_GNM_HeavyMek_Rivalry_A01_AetheriumGlow`
- `MI_GNM_HeavyMek_Rivalry_A01_PilotSkin`
- `MI_GNM_HeavyMek_Rivalry_A01_PilotWorkwear`
- `MI_GNM_HeavyMek_Rivalry_A01_Leather`

## Triangle Budget

- Review blockout LOD0 target: under 25k tris.
- Final common encounter variant LOD0: 28k-45k tris, 3-4 materials.
- Final hero/unique variant may reach 45k-70k tris only when justified.
- Use 2K texture sets for the common encounter variant. Reserve 4K for named hero variants.

## LOD Plan

- LOD0: full cockpit, pilot bust, shoulders, boots, reactor, cannon, hammer/tool arm, shield socket hardware.
- LOD1: 55-60 percent; reduce bevels, trim density, small pipes, secondary brackets.
- LOD2: 25-35 percent; merge plate groups, simplify hands, reduce pilot detail, remove small sockets that are not gameplay-critical.
- LOD3: 10-15 percent; preserve body mass, shoulder silhouette, blue core read, cannon arm, and heavy boots.

## Collision Notes

- Use a simple character/vehicle capsule for gameplay movement once movement rules are chosen.
- Review physics asset may use generated bodies for validation only.
- Weapon traces should use sockets rather than mesh collision.
- Foot and stomp sockets support ground VFX; foot collision should not drive gameplay damage directly.

## Animation Notes

Initial animation list:

- Idle reactor hum.
- Heavy walk.
- Turn in place.
- Brace shield.
- Cannon charge.
- Cannon fire and recoil.
- Hammer/tool swing.
- Stomp.
- Overheat vent.
- Shutdown kneel.
- Pilot hatch gesture.
- Hit reaction.
- Disabled/death state.

## Unreal Import Notes

- Asset type: Skeletal Mesh.
- Primary mesh: `SK_GNM_HeavyMek_Rivalry_A01`.
- Skeleton: `SK_GNM_HeavyMek_Rivalry_A01_Skeleton`.
- Physics asset: `PHYS_GNM_HeavyMek_Rivalry_A01`.
- Animation Blueprint placeholder: `ABP_GNM_HeavyMek_Rivalry_A01`.
- Unreal path: `/Game/Aerathea/Characters/Gnomes/Meks/`.
- Startup actor: `AET_PROD_GNM_HeavyMek_Rivalry_A01`.
- Required sockets: `vfx_reactor_core`, `vfx_shield_l`, `vfx_shield_r`, `weapon_cannon_muzzle`, `pilot_hatch`, `foot_l`, `foot_r`, `vfx_stomp_l`, `vfx_stomp_r`, `weapon_hammer_socket`, `vfx_chest_core`.

## Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_GNM_HeavyMek_Rivalry_A01/`
- Source: `SourceAssets/Blender/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01/`
- Export: `SourceAssets/Exports/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01/`
- Unreal: `/Game/Aerathea/Characters/Gnomes/Meks/`
- DCC script: `Tools/DCC/build_gnome_heavy_mek.py`
- Unreal import script: `Tools/Unreal/import_gnome_heavy_mek.py`

## Quality Gate Checklist

- Reads as Gnome/Mekgineer engineering, not Ogre Teknomancy.
- Visible pilot preserves gnome scale.
- Mek frame sits below Ogre height while still feeling massive beside the gnome.
- Silhouette is readable from gameplay camera distance.
- Blue Aetherium glow is sparing and functional.
- Major mechanical shapes are real geometry; micro-detail is reserved for textures.
- Triangle budget, texture maps, sockets, LODs, collision, animation targets, and Unreal paths are defined.
