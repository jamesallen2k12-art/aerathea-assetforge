# SK_OGR_Teknomancer_A01 Production Package

## Art Direction Summary

Ogre Teknomancers are battlefield inventors who make war machines through instinct, force, and dangerous magical engineering rather than gnomish precision. The approved direction is a heavily muscled Ogre body wearing asymmetrical blackened-iron armor, thick bracers, leather straps, bone and tooth trophies, rune-burned plates, and oversized reactor hardware. Their machinery should look overbuilt, chained together, hot from use, and one impact away from exploding, but still deliberate enough to be a playable MMO character variant.

Primary source references:

- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreMaleTek.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreMale1.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreTekvsGnomeMek.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreTekShop.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Ogres10.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Ogres11.png`

Shared final-art fit source: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/OGRE_SHARED_RIG_FINAL_ART_FIT_PLAN.md`. This class remains bound to `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton` and should be the first class overlay fit after the final Ogre base body.

## Gameplay Purpose

`SK_OGR_Teknomancer_A01` is the first Ogre class body package after `SK_OGR_Base_A01`. It supports player/NPC Teknomancer identity, elite enemy units, forge masters, siege engineers, and Gnome Mek rivalry encounters. Gameplay should read as brutal magic-tech pressure: cannon bracing, powered hammer strikes, overload casts, reactor venting, battlefield repairs, and anti-Mek disruption.

## Silhouette Notes

- Use the approved Ogre base proportions: females 10'0"-10'6", males 10'4"-11'0".
- Preserve the huge chest, heavy arms, slab hands, thick neck, and forward-driving stance from `SK_OGR_Base_A01`.
- Add one oversized shoulder/upper-arm armor mass and one exposed working arm for asymmetry.
- The waist or chest reactor must read clearly from MMO camera distance.
- Bracers should be blocky and huge, with major vents, pressure bands, and rune windows modeled in real geometry.
- The powered hammer or crusher tool should be the strongest prop silhouette, bigger than a normal humanoid torso.
- Avoid dense micro-bolts as geometry; use normal maps and painted detail for small rivets, scratches, tick marks, and wire tangles.

## Scale Notes

- Author in centimeters at full Ogre scale.
- Fit over `SK_OGR_Base_Male_A01` first, then produce female fit adjustments from the same modular armor kit.
- Core body height target: male 330 cm baseline, female 315 cm baseline.
- Reactor belt and bracers must clear the base body walk, heavy swing, and two-handed brace poses.
- Powered hammer length target: 190-240 cm; head mass can be 70-95 cm wide depending on gameplay read.

## Materials And Color Palette

- Skin: ash-brown, gray-umber, or ochre Ogre skin with scar and warpaint variation.
- Armor: blackened iron, dark steel, crude brass/copper, scorched leather, chain, and rough fur/hide.
- Teknomancy: forge-orange heat windows, rune-burned metal, heavy pressure cylinders, crude conduit hoses, and occasional blue-white electrical discharge when reacting against gnome Mek technology.
- Trophies: bone teeth, skull charms, chain links, broken tools, and stripped enemy machine parts.
- Keep emissive accents sparing: reactor windows, hammer core, bracer vents, rune cuts, and overload VFX sockets only.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_OGR_Teknomancer_A01`, an Ogre Teknomancer class character for the world of Aerathea. The design should emphasize a massive broad 10-11 ft Ogre silhouette, asymmetrical blackened-iron armor, huge bracers, a crude waist or chest reactor, chained pressure tanks, an oversized powered hammer, bone trophies, red-brown warpaint, forge-orange rune heat, jealous anti-gnome battlefield engineering, and a brutal role as a magic-tech siege fighter. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a character production sheet with front, side, back, three-quarter, weapon callouts, socket callouts, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

- Build this as modular class gear over `SK_OGR_Base_A01`; do not duplicate the base body.
- Model real geometry for bracers, major shoulder plates, belt reactor, hammer head, pressure tank housings, large chains, large vents, major skull trophies, and heavy straps.
- Texture or normal-map small rivets, fine chain scars, tiny runes, surface scratches, leather stitching, and minor wire wraps.
- Bracers and belt reactor should be removable modules for future Warrior/Shaman/Necromancer variants.
- Keep back-mounted hardware optional through `spine_teknomancy_pack` so the same skeleton can support less-equipped variants.
- Build first DCC pass as blockout fit over male Ogre; only move to sculpt/retopo after scale, sockets, and silhouette are approved.

## Texture And Material Notes

- `T_OGR_Teknomancer_A01_BC`
- `T_OGR_Teknomancer_A01_N`
- `T_OGR_Teknomancer_A01_ORM`
- `T_OGR_Teknomancer_A01_E`
- Base material slots: skin/body inherited from Ogre base; armor/metal; leather/cloth/fur; emissive Teknomancy core.
- Use packed ORM: Occlusion, Roughness, Metallic.
- Emissive map only for reactor windows, bracer vents, hammer core, rune cuts, and optional eye/vfx points.

## Triangle Budget

- Class gear over base body LOD0 target: 22k-35k tris.
- Full equipped character target with base body: 55k-70k tris for hero/NPC review; normal gameplay target should stay closer to 50k-60k.
- Material slot target: 4-5 total for fully equipped variant.

## LOD Plan

- LOD0: full body, major armor plates, bracers, reactor, hammer, sockets, and large chains.
- LOD1: 55-60% triangle count; simplify bevels, secondary straps, small vents, and chain loops.
- LOD2: 25-35% triangle count; remove minor hanging trophies, small wires, individual small rivet geometry, and secondary plates.
- LOD3: 10-15% triangle count; preserve Ogre body mass, hammer silhouette, reactor glow, and one dominant bracer/shoulder read.

## Collision Notes

- Use the Ogre character capsule from `SK_OGR_Base_A01` for movement.
- Equipped armor collision disabled by default.
- Hammer and back reactor get simplified convex collision only for weapon traces, pickup preview, or ragdoll hit reactions.
- Avoid per-chain and per-rivet collision.

## Animation Notes

- Required first-pass review poses: idle, hammer ready, two-handed overhead smash, cannon brace stance, bracer overload cast, repair/adjust reactor, heavy recoil, and stun/failure reaction.
- Needed sockets:
  - `hand_r_weapon`
  - `hand_l_offhand`
  - `hand_r_twohand_grip`
  - `hand_l_twohand_grip`
  - `spine_teknomancy_pack`
  - `vfx_chest_core`
  - `vfx_mouth`
  - `vfx_stomp_ground`
  - `vfx_hammer_core`
  - `vfx_bracer_l`
  - `vfx_bracer_r`

## Unreal Import Notes

- Asset type: Skeletal Mesh class outfit / gear configuration.
- Primary mesh: `SK_OGR_Teknomancer_A01`.
- Parent body: `SK_OGR_Base_A01`.
- Skeleton: use `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton`; current first-pass validation uses `Tools/Unreal/validate_ogre_shared_skeletons.py`, and class-specific auxiliary bones require a later shared-rig review.
- Physics asset: inherit base physics, add simplified auxiliary bodies for hammer/back reactor only when needed.
- Animation Blueprint: `ABP_OGR_Teknomancer_A01`, derived from future Ogre base locomotion.
- Unreal path: `/Game/Aerathea/Characters/Ogres/Teknomancer/`.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Pivot: inherited from base body at ground center between feet.
- Material slot count: 4-5.

## Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_OGR_Teknomancer_A01/`
- Source: `SourceAssets/Blender/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01/`
- Export: `SourceAssets/Exports/Characters/Ogres/Teknomancer/SK_OGR_Teknomancer_A01/`
- Unreal: `/Game/Aerathea/Characters/Ogres/Teknomancer/`
- Materials:
  - `MI_OGR_Teknomancer_A01_Armor`
  - `MI_OGR_Teknomancer_A01_Leather`
  - `MI_OGR_Teknomancer_A01_TekGlow`
  - `MI_OGR_Teknomancer_A01_Trophies`

## Quality Gate Checklist

- Reads as an Ogre, not a tall human or a gnome-style engineer.
- Final art follows the Ogre shared rig fit plan and remains bound to the validated male Ogre skeleton.
- Scale remains below Giants and above Minotaurs.
- Teknomancy reads crude, oversized, dangerous, and instinctive.
- Core silhouette is readable at MMO camera distance.
- Shared Ogre skeleton validation passes for the saved mesh, physics asset, and required class sockets.
- Glow is limited to reactor, hammer core, bracer vents, and rune cuts.
- Major hardware is real geometry; micro-detail is texture/normal detail.
- Base body, sockets, animation fit, collision, triangle budget, LODs, and Unreal paths are defined.
