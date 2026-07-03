# SK_GNM_IonaSiegebreakerMek_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GNM_IonaSiegebreakerMek_A01`
- Asset type: Skeletal Mesh hero Mek / named Gnome Mekgineer vehicle-body
- Parent kit: `KIT_GNM_IonaSiegebreaker_A01`
- Source concept: `Iona.png`
- Related references: `Gnome Mek fighting Demon.png`, `GnomeFemaleHeavyMek.png`, `GnomeFemaleHeavyMek0.png`, `GnomeFemaleHeavyMek8.png`, `GnomeFemaleHeavyMek10.png`
- Approval status: first approved Iona child production lane, cleared by Flamestrike on 2026-06-28
- Current build status: first-pass DCC/Unreal review implementation complete and validated on 2026-06-28; final sculpt, UVs/textures, tuned physics, and animation remain pending

`SK_GNM_IonaSiegebreakerMek_A01` is Iona's named hero heavy Mek, not a generic workshop suit. It should feel like a gnome-built siege-defense machine: compact pilot presence, oversized armored limbs, dark iron and brass plates, visible cockpit/harness hardware, blue Aetherium power cores, twin arc-cannon mount points, heavy fists, smoke grime, and heroic battlefield urgency.

The design should share Mekgineer material language with `KIT_MKG_Armory_A01`, `SK_GNM_HeavyMek_Rivalry_A01`, and `BP_GNM_HeavyMekShieldwall_A01`, but it remains Iona's distinct hero Mek silhouette. Do not replace it with the generic rivalry Mek or a procedural placeholder.

## First-Pass Build Status

The approved first-pass review lane is complete. This pass establishes Iona's 420 cm Mek scale, cockpit/pilot envelope, twin arc-cannon socket contract, oversized fist/boot proportions, material families, generated LOD0-LOD3, simplified physics assignment, placeholder animation Blueprint, and startup-scene placement.

Generated and imported review files:

- Blender source: `SourceAssets/Blender/Characters/Gnomes/Iona/SK_GNM_IonaSiegebreakerMek_A01/SK_GNM_IonaSiegebreakerMek_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Gnomes/Iona/SK_GNM_IonaSiegebreakerMek_A01/SK_GNM_IonaSiegebreakerMek_A01.fbx`
- DCC proof render: `Saved/Automation/IonaSiegebreakerMekReview/SK_GNM_IonaSiegebreakerMek_A01_DCCReview.png`
- Unreal skeletal mesh: `/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01`
- Startup actor: `AET_PROD_GNM_IonaSiegebreakerMek_A01`

Validation is passing:

- Focused validator: visible height `419.61 cm`, bounds radius `423.27 cm`, `16` required sockets present.
- Startup validator: `150 assets`, `49 expected actors`, `25 ground tiles`.

This is not final art. Use it as the locked production foundation for the final art-model pass.

## Gameplay Purpose

- Establishes Iona's named hero Mek as the first child package from `KIT_GNM_IonaSiegebreaker_A01`.
- Locks the cockpit/harness envelope before `SK_GNM_IonaPilot_A01`.
- Locks cannon, core, fist, foot, vent, and pilot sockets before `SM_GNM_IonaArcCannon_A01` and `BP_GNM_IonaSiegebreaker_A01`.
- Supports siege-defense NPC staging, heavy Mek locomotion, Abyss invasion set pieces, and future hero encounter scripting.
- Provides a hero-scale Gnome Mek reference that can inform later Gnome heavy Mek variants without erasing Iona's identity.

## Silhouette Notes

- Primary read: compact gnome pilot carried in a massive but readable heavy Mek frame.
- Hero Mek should stand around 420 cm tall in the first production target, with an acceptable final range of 400-430 cm after cockpit and locomotion review.
- Maintain gnome engineering readability: squat power core, strong boots, oversized mechanical fists, shoulder/back cannon mount mass, protective cockpit cage, visible pilot harness, and sturdy piston-supported limbs.
- Avoid making the Mek look like an Ogre, Giant armor suit, or sleek elven construct. It should be clever, overbuilt, brass-and-iron, and mechanically expressive.
- Major arc-cannon mounts should read even before the separate cannon mesh is built.
- Pilot visibility matters. The cockpit should frame Iona rather than hide her.

## Scale Notes

- Author in centimeters at full production scale.
- Mek standing target: 420 cm.
- Acceptable height range after review: 400-430 cm.
- Pilot envelope: supports a 100-120 cm gnome pilot in harness.
- Fist width target: 70-95 cm.
- Boot/foot length target: 95-130 cm.
- Shoulder/back cannon socket separation should support twin cannons 160-240 cm long.
- Pivot: ground center between feet, aligned to the Mek's standing neutral pose.

## Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Dark iron and blackened steel | charcoal, soot black, dark gunmetal | Main frame, fists, boots, protective plates |
| Brass and copper | aged brass, oxidized copper, warm rivet/gasket tones | Trim, mechanical housings, piston rings, socket collars |
| Leather and rubberized wraps | dark brown, warm worn leather, black hose material | Pilot harness, cable guards, grip wraps, cockpit restraints |
| Glass and lenses | smoky glass, blue lens tint | Pilot canopy edges, gauges, sight lenses |
| Aetherium | clean blue, blue-white core light | Chest/core reactor, cannon charge sockets, vents, status lamps |
| Battle wear | soot, scratches, edge chips, oil grime | Hand-painted surface breakup and normal detail |

Emissive must remain focused on Aetherium cores, cannon charge points, vents, and small status lamps. Do not turn the whole frame into a glow silhouette.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production sheet of `SK_GNM_IonaSiegebreakerMek_A01`, Iona's named Gnome Mekgineer heavy siegebreaker Mek for the world of Aerathea. The design should emphasize a 420 cm hero combat Mek with oversized armored fists, heavy boots, dark iron and brass plating, copper trim, visible cockpit and pilot harness for a compact gnome, shoulder/back twin arc-cannon mount points, blue Aetherium power cores, smoke-grimed hand-painted surfaces, sturdy piston-supported limbs, and a siege-defense role against Abyss demon assaults. Use readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing blue emissive accents, and MMO-friendly production design. Present it as a production board with front, side, back, three-quarter view, cockpit/harness callout, socket callouts, material swatches, scale beside a 110 cm gnome and 180 cm humanoid, and an encounter inset against a large Abyss demon silhouette. Avoid copied franchise designs, photoreal over-detail, excessive micro-bolts, unreadable cables, text, watermarks, and procedural placeholder art.

## Modeling Notes

- Build as a skeletal mesh with mechanical limb articulation, not as a static prop.
- Model real geometry for torso cage, cockpit guard, pilot harness anchors, main frame, fists, boots, large armor plates, pistons, shoulder/back cannon mounts, reactor housing, vent stacks, and large cables.
- Use textures and normal maps for tiny rivets, scratches, seam lines, gauge markings, soot, oil, small bolt heads, cloth weave, and leather grain.
- Keep the pilot harness and cockpit open enough to receive `SK_GNM_IonaPilot_A01` later.
- Arc cannons can be represented by socket mounts in this first Mek package; final cannon assemblies belong to `SM_GNM_IonaArcCannon_A01`.
- Do not force skeleton reuse with `SK_GNM_HeavyMek_Rivalry_A01` unless a later validation pass confirms the proportions can share animation safely. Reuse socket vocabulary and material language first.

## Texture And Material Notes

Required texture families:

- `T_GNM_IonaSiegebreakerMek_A01_BC`
- `T_GNM_IonaSiegebreakerMek_A01_N`
- `T_GNM_IonaSiegebreakerMek_A01_ORM`
- `T_GNM_IonaSiegebreakerMek_A01_E`

Material slot target:

1. `MI_GNM_IonaSiegebreakerMek_A01_DarkIron`
2. `MI_GNM_IonaSiegebreakerMek_A01_BrassCopper`
3. `MI_GNM_IonaSiegebreakerMek_A01_LeatherCable`
4. `MI_GNM_IonaSiegebreakerMek_A01_AetheriumGlow`
5. Optional cockpit glass/lens material only if the cockpit needs separate translucency or masked treatment.

Use packed ORM: Occlusion, Roughness, Metallic. Use emissive only for Aetherium core, cannon sockets, vents, and small status lamps.

## Triangle Budget

- LOD0 target: 45k-70k tris.
- Hero review ceiling: 80k tris only if cockpit readability and cannon mount complexity require it.
- Material slot target: 4, maximum 5.
- Texture target: 2K for common gameplay, 4K hero set only if Iona becomes a cinematic or key story NPC.

## LOD Plan

- LOD0: full cockpit, harness anchors, fists, boots, main plates, piston silhouettes, cannon mounts, vents, core, socket helpers.
- LOD1: 55-60% triangle count; simplify bevels, small piston supports, secondary cables, interior cockpit detail, and minor plate cuts.
- LOD2: 25-35% triangle count; merge armor panels, simplify fists/feet, reduce cable bundles, remove small brackets and minor vent fins.
- LOD3: 10-15% triangle count; preserve cockpit/pilot read, torso mass, fists, boots, cannon mount silhouette, and blue core glow.
- Reduce tiny bolts, scratches, brackets, small lamps, and interior cockpit pieces before reducing major body mass or cannon/fist silhouettes.

## Collision Notes

- Use a custom Mek movement capsule or creature/vehicle movement collision profile after gameplay rules are selected.
- Use simplified convex bodies for torso, cockpit cage, fists, forearms, upper arms, thighs, shins, feet, back cannon mounts, and core housing.
- Disable collision on small pistons, minor cables, lamps, rivets, gauges, and decorative handles.
- Weapon fire and VFX use sockets and traces, not mesh collision.
- Footstep/stomp effects use foot sockets and gameplay trace volumes.

## Animation Notes

Initial animation set:

- Idle engine rumble.
- Heavy walk.
- Turn in place.
- Brace.
- Left fist punch.
- Right fist punch.
- Stomp.
- Cannon aim pose.
- Cannon fire recoil.
- Overheat vent.
- Core charge loop.
- Hit reaction.
- Shutdown/kneel.
- Disabled/death state.

Pilot-linked poses should preserve a visible cockpit/harness read but do not require the final pilot mesh before the Mek package is built.

## Unreal Import Notes

- Asset type: Skeletal Mesh.
- Primary mesh: `SK_GNM_IonaSiegebreakerMek_A01`.
- Skeleton: `SKEL_GNM_IonaSiegebreakerMek_A01`.
- Physics asset: `PHYS_GNM_IonaSiegebreakerMek_A01`.
- Animation Blueprint: `ABP_GNM_IonaSiegebreakerMek_A01`.
- Future assembled actor: `BP_GNM_IonaSiegebreaker_A01`.
- Unreal path: `/Game/Aerathea/Characters/Gnomes/Iona/Mek/`.
- Materials path: `/Game/Aerathea/Materials/Gnome/Iona/`.
- VFX path: `/Game/Aerathea/VFX/Gnome/AetheriumArc/`.
- Scale: centimeters, no import scaling.
- Pivot: ground center between feet.
- Required sockets:
  - `socket_pilot_harness`
  - `socket_cannon_l_mount`
  - `socket_cannon_r_mount`
  - `socket_cannon_l_muzzle`
  - `socket_cannon_r_muzzle`
  - `socket_core_chest`
  - `socket_core_back`
  - `socket_hand_l`
  - `socket_hand_r`
  - `socket_foot_l`
  - `socket_foot_r`
  - `socket_vent_l`
  - `socket_vent_r`
  - `socket_camera_focus`
  - `vfx_arc_l`
  - `vfx_arc_r`

## Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_GNM_IonaSiegebreakerMek_A01/`
- Source: `SourceAssets/Blender/Characters/Gnomes/Iona/SK_GNM_IonaSiegebreakerMek_A01/`
- Export: `SourceAssets/Exports/Characters/Gnomes/Iona/SK_GNM_IonaSiegebreakerMek_A01/`
- Unreal: `/Game/Aerathea/Characters/Gnomes/Iona/Mek/`
- Textures: `T_GNM_IonaSiegebreakerMek_A01_*`
- Materials: `MI_GNM_IonaSiegebreakerMek_A01_*`

Dependent follow-up packages:

- `SK_GNM_IonaPilot_A01`
- `SM_GNM_IonaArcCannon_A01`
- `BP_GNM_IonaSiegebreaker_A01`

## Quality Gate Checklist

- Mek reads as a Gnome/Mekgineer hero machine, not an Ogre suit or generic robot.
- Cockpit and harness preserve a visible 100-120 cm gnome pilot envelope.
- Scale supports the approved 420 cm hero Mek target without exceeding the intended 400-430 cm range.
- Fists, boots, cannon mounts, core, and cockpit silhouette read at MMO camera distance.
- Major forms are modeled; tiny bolts, scratches, gauge marks, and grime live in textures/normal maps.
- Materials match dark iron, brass/copper, leather/cable, glass/lens, and blue Aetherium language.
- LOD0-LOD3, collision plan, sockets, animation list, texture maps, and Unreal paths are defined.
- First-pass DCC/Unreal review implementation is validated; final sculpt, retopo, UVs, authored textures, tuned physics, and animation are still required before final art approval.
