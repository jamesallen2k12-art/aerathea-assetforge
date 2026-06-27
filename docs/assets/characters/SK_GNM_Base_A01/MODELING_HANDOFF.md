# SK_GNM_Base_A01 Modeling Handoff

## Purpose

Create the first Aerathea gnome base body DCC source, skeleton target, and Unreal import path. This handoff converts the approved gnome anchor into a build-ready character target for scale validation, gear fitting, sockets, animation tests, and future player/NPC variants.

## Source References

- Production package: `docs/assets/characters/SK_GNM_Base_A01/PRODUCTION_PACKAGE.md`
- Source concepts:
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Male.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Female.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GnomeMale1.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnomish Sentinels.png`
- Related kit: `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md`
- Gear fit references: `docs/assets/characters/SK_GNM_ChestRig_MKG_A01/PRODUCTION_PACKAGE.md`, `docs/assets/kits/KIT_GNM_MekgineersKit_A01/PRODUCTION_PACKAGE.md`

## Production Target

Skeletal mesh base body for an adult Aerathea gnome: compact 3-4 ft proportions, large expressive head and ears, sturdy legs, oversized boots, broad gloves/hands, four fingers plus one thumb per hand, and clean attachment landmarks for Mekgineer gear.

The first body source should be a neutral production body, not a final armored hero. Starter clothing, armor, goggles, backpacks, and tools remain modular where possible.

## Modeling Constraints

- Target standing height: 110-120 cm, with 110 cm used for the startup scale marker.
- Author in centimeters, 1 Unreal unit = 1 cm.
- Feet at world origin, facing +X unless import tests establish a different project convention.
- Use adult proportions. Avoid childlike body language even when the head and eyes are stylized.
- Model clean primary forms for head, ears, torso, arms, hands, fingers, legs, boots, and simple starter clothing.
- Keep dense armor plates, tool belts, pouches, goggles, backpacks, and chest rigs modular rather than baked into the base body.
- Four fingers plus one thumb per hand. Do not use five-finger human hands.
- Preserve generous hand size for tools and weapons without making the character human-scale.

## Blender Setup

- Collection: `SK_GNM_Base_A01`
- Mesh objects:
  - `Body_Head`
  - `Body_Torso`
  - `Body_Arms`
  - `Body_Hands`
  - `Body_Legs`
  - `Starter_Boots`
  - `Starter_Gloves`
  - `Starter_Workwear`
- Skeleton object: `SKEL_GNM_Base_A01`
- Apply transforms before export.
- Use clean mirrored topology where possible, but keep asymmetry only in optional starter clothing or hair later.
- Leave enough topology around eyes, mouth, brows, and ears for future expression support.

## Modeling Sequence

1. Block the 110-120 cm body against the startup gnome scale marker.
2. Establish head, ear, torso, leg, boot, and hand proportions in low-poly blockout.
3. Create neutral adult body forms and simple starter workwear volumes.
4. Build hands with four fingers plus one thumb and clear knuckle/finger separation.
5. Add large ear silhouettes with readable inner-ear planes for normal-map detail.
6. Add starter boots and gloves as modular-feeling geometry that can be replaced later.
7. Create socket landmarks for goggles, weapon hands, backpack, belt tools, muzzle preview, and Aetherium core VFX.
8. Retopologize for animation-friendly shoulders, elbows, wrists, hips, knees, ankles, fingers, neck, jaw, and ears.
9. Create UVs and placeholder material assignments.
10. Build LOD0-LOD3 while preserving head, ears, boots, hands, and compact stance.
11. Export skeletal FBX and validate scale in Unreal beside `AET_BOOT_GnomeScale_110cm`.

## Triangle Budget

- Base body LOD0: 15k-25k tris.
- Starter workwear, boots, and gloves: 5k-12k tris if included in the first review mesh.
- First playable review target: under 35k tris total.
- LOD1: 60-70 percent of LOD0.
- LOD2: 35-45 percent of LOD0.
- LOD3: 15-25 percent of LOD0.

Reduce stitching, small clothing folds, boot cuts, minor glove seams, and inner clothing detail before reducing head, ear, hand, boot, or stance silhouette.

## Texture Deliverables

- `T_GNM_Base_A01_Body_BC`
- `T_GNM_Base_A01_Body_N`
- `T_GNM_Base_A01_Body_ORM`
- `T_GNM_Base_A01_Eyes_BC`
- `T_GNM_StarterOutfit_A01_BC`
- `T_GNM_StarterOutfit_A01_N`
- `T_GNM_StarterOutfit_A01_ORM`

Material slot target:

- Body/head/skin
- Eyes
- Starter outfit/boots/gloves

Use 2K texture sets by default. Reserve 4K only for a hero review variant.

## Collision Deliverables

- Movement collision: gnome-height capsule tuned to 110-120 cm body height.
- Physics asset: head, torso, upper/lower arms, hands, thighs, calves, feet, and optional ear bodies after skeleton approval.
- Equipped gear collision remains disabled by default and uses the character capsule/physics asset unless a specific gameplay system requires otherwise.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Gnomes/SK_GNM_Base_A01/SK_GNM_Base_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Gnomes/SK_GNM_Base_A01/SK_GNM_Base_A01.fbx`
- Unreal skeletal mesh: `/Game/Aerathea/Characters/Gnomes/Base/SK_GNM_Base_A01`
- Skeleton: `/Game/Aerathea/Characters/Gnomes/Base/SKEL_GNM_Base_A01`
- Physics asset: `/Game/Aerathea/Characters/Gnomes/Base/PHYS_GNM_Base_A01`
- Animation Blueprint placeholder: `/Game/Aerathea/Characters/Gnomes/Base/ABP_GNM_Base_A01`

## Unreal Validation

- Imports at 110-120 cm standing height.
- Feet sit at world origin with no scale correction needed.
- Skeleton supports idle, walk, run, jump, interact, one-handed attack, two-handed attack, pistol aim/fire placeholder, cast/channel placeholder, emote wave, and death.
- Required sockets exist:
  - `hand_r_weapon`
  - `hand_l_offhand`
  - `back_pack`
  - `head_goggles`
  - `belt_tool_l`
  - `belt_tool_r`
  - `muzzle_preview`
  - `vfx_aether_core`
- Body remains readable beside player and minotaur startup scale markers.
- Gear modules from `KIT_MKG_Armory_A01` have clear fit targets.

## Acceptance Checklist

- Compact adult gnome silhouette, not a short human and not childlike.
- Large head, large expressive ears, sturdy legs, oversized boots, and tool-ready hands.
- Four fingers plus one thumb per hand.
- Starter workwear/boots/gloves support the Mekgineer material language without baking armor into the base body.
- Skeleton, sockets, physics asset plan, material slots, texture maps, LODs, and Unreal paths are defined.
- Base body can support future male/female variants, starter outfits, goggles, backpacks, and armory modules.
- No copied franchise gnome design language.
