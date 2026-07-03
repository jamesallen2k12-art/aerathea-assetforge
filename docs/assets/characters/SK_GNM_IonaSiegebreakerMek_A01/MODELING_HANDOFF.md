# SK_GNM_IonaSiegebreakerMek_A01 Modeling Handoff

## Scope

Build Iona's approved first child asset: `SK_GNM_IonaSiegebreakerMek_A01`. This is the final-art DCC handoff plus a validated first-pass DCC/Unreal review foundation for a named Gnome hero heavy Mek. It should not be replaced by a generic `SK_GNM_HeavyMek_Rivalry_A01` duplicate, or a static mesh prop.

This first child package includes the Mek frame, cockpit/harness envelope, core, fists, boots, cannon mounts, vents, sockets, LOD plan, collision plan, and animation-ready skeleton. It does not include the final Iona pilot mesh, final detached arc cannon mesh, or assembled Blueprint actor.

Current implementation state: first-pass Blender source, FBX export, Unreal skeletal mesh import, generated LOD0-LOD3, sockets, physics asset, placeholder ABP, startup actor, focused validator, and startup validator are complete as of 2026-06-28. Final sculpt, retopo, authored UVs/textures, tuned physics bodies, and animation remain pending.

## Inputs

- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Iona.png`
- Related encounter reference: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Mek fighting Demon.png`
- Heavy Mek variant references:
  - `GnomeFemaleHeavyMek.png`
  - `GnomeFemaleHeavyMek0.png`
  - `GnomeFemaleHeavyMek8.png`
  - `GnomeFemaleHeavyMek10.png`
- Parent kit: `docs/assets/kits/KIT_GNM_IonaSiegebreaker_A01/PRODUCTION_PACKAGE.md`
- Production package: `docs/assets/characters/SK_GNM_IonaSiegebreakerMek_A01/PRODUCTION_PACKAGE.md`
- Related mechanical language:
  - `docs/assets/characters/SK_GNM_HeavyMek_Rivalry_A01/PRODUCTION_PACKAGE.md`
  - `docs/assets/blueprints/BP_GNM_HeavyMekShieldwall_A01/PRODUCTION_PACKAGE.md`
  - `docs/assets/kits/KIT_MKG_Armory_A01/PRODUCTION_PACKAGE.md`

## DCC Deliverables

- Blender source: `SourceAssets/Blender/Characters/Gnomes/Iona/SK_GNM_IonaSiegebreakerMek_A01/SK_GNM_IonaSiegebreakerMek_A01.blend`
- Export FBX: `SourceAssets/Exports/Characters/Gnomes/Iona/SK_GNM_IonaSiegebreakerMek_A01/SK_GNM_IonaSiegebreakerMek_A01.fbx`
- DCC proof render: `Saved/Automation/IonaSiegebreakerMekReview/SK_GNM_IonaSiegebreakerMek_A01_DCCReview.png`
- Skeletal mesh import target: `/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01`
- Physics asset: `/Game/Aerathea/Characters/Gnomes/Iona/Mek/PHYS_GNM_IonaSiegebreakerMek_A01`
- Animation Blueprint placeholder: `/Game/Aerathea/Characters/Gnomes/Iona/Mek/ABP_GNM_IonaSiegebreakerMek_A01`
- Materials: `/Game/Aerathea/Materials/Gnome/Iona/MI_GNM_IonaSiegebreakerMek_A01_*`
- Startup actor: `AET_PROD_GNM_IonaSiegebreakerMek_A01`

## Scale And Pivot

- Author at real Unreal centimeters.
- Target standing height: 420 cm.
- Acceptable first review range: 400-430 cm.
- Pilot envelope: 100-120 cm gnome in seated/standing harness.
- Pivot: ground center between feet.
- Neutral pose: stable heavy stance with both feet on ground and cockpit facing +X or the project-standard forward direction used by the import script.

## Skeleton And Rig Guidance

Use a dedicated Mek skeleton unless a later validation pass proves the rivalry Mek rig can safely be shared. The first production pass should prioritize clean Iona proportions and socket placement over forced reuse.

Required functional bone groups:

- `root`
- `pelvis` or `body_root`
- `torso`
- `cockpit`
- `core_chest`
- `upperarm_l`, `forearm_l`, `fist_l`
- `upperarm_r`, `forearm_r`, `fist_r`
- `thigh_l`, `shin_l`, `foot_l`
- `thigh_r`, `shin_r`, `foot_r`
- `cannon_mount_l`, `cannon_mount_r`
- `vent_l`, `vent_r`
- Optional helper bones for dominant pistons only where animation needs them.

Do not add bones for tiny bolts, micro-pistons, lamps, rivets, gauges, or decorative cables.

## Socket Contract

Required sockets:

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

Socket placement must support later `SK_GNM_IonaPilot_A01`, `SM_GNM_IonaArcCannon_A01`, and `BP_GNM_IonaSiegebreaker_A01` assembly without moving the main Mek mesh.

## Modeling Checklist

- Block the 420 cm silhouette first, then refine details.
- Keep the cockpit/harness visible and sized for a gnome pilot.
- Model real geometry for torso cage, cockpit guard, pilot harness mounts, main armor plates, fists, boots, piston silhouettes, cannon mount brackets, reactor core housing, vents, and large cables.
- Use normal/texture detail for tiny rivets, scratches, small bolts, gauge markings, leather grain, soot, oil streaks, and small seams.
- Keep silhouette forms large, chunky, and readable; avoid thin spider-like limbs or dense wire clutter.
- Leave enough clearance around shoulders and back for twin arc cannon assemblies.
- Preserve distinct Iona identity while sharing dark iron, brass, copper, leather, and blue Aetherium language with other Gnome Mekgineer assets.

## UV And Texture Checklist

- UVs must support readable hand-painted edge wear and grime.
- Keep cockpit/core/cannon mount areas easy to texture and inspect.
- Texture maps:
  - `T_GNM_IonaSiegebreakerMek_A01_BC`
  - `T_GNM_IonaSiegebreakerMek_A01_N`
  - `T_GNM_IonaSiegebreakerMek_A01_ORM`
  - `T_GNM_IonaSiegebreakerMek_A01_E`
- Packed ORM order: Occlusion, Roughness, Metallic.
- Emissive only for core, cannon charge sockets, vents, and status lamps.

## LOD Checklist

- LOD0: 45k-70k tris target.
- LOD1: 55-60% of LOD0; reduce bevels, small piston supports, secondary cables, and interior cockpit detail.
- LOD2: 25-35% of LOD0; merge armor panels, simplify fists/feet, reduce cable bundles, remove minor brackets.
- LOD3: 10-15% of LOD0; preserve cockpit/pilot read, torso, fists, boots, cannon mount silhouette, and blue core glow.

## Collision And Physics Checklist

- Create simplified bodies for torso, cockpit cage, fists, forearms, upper arms, thighs, shins, feet, cannon mounts, and core housing.
- Use sockets/traces for cannon fire, arc charge, vent effects, fist hits, and stomp effects.
- Do not create collision for tiny pistons, small cables, lamps, rivets, gauges, or decorative brackets.
- Confirm the movement capsule or vehicle collision envelope can fit startup review paths before gameplay tuning.

## Animation Readiness Checklist

The mesh and skeleton must support:

- Idle engine rumble.
- Heavy walk.
- Turn in place.
- Brace.
- Fist punch left/right.
- Stomp.
- Cannon aim and fire recoil.
- Overheat vent.
- Core charge loop.
- Hit reaction.
- Shutdown/kneel.
- Disabled/death state.

## Review And Validation

After import:

1. Validate mesh exists at `/Game/Aerathea/Characters/Gnomes/Iona/Mek/SK_GNM_IonaSiegebreakerMek_A01`.
2. Validate sockets listed in this handoff exist.
3. Validate material slot count stays at 4-5.
4. Validate LOD0-LOD3 exist.
5. Validate physics asset exists and uses simplified bodies.
6. Capture a clean startup or focused review image before presenting visual approval.

Do not present a visual approval if the camera shows underside/frustum/proxy geometry, the cockpit scale hides the gnome pilot envelope, or the Mek does not read as a Gnome/Mekgineer hero asset.

2026-06-28 validation results:

- `Tools/Unreal/validate_iona_siegebreaker_mek.py` passed: visible height `419.61 cm`, bounds radius `423.27 cm`, and `16` sockets present.
- `Tools/Unreal/validate_startup_scene.py` passed with `150 assets`, `49 expected actors`, and `25 ground tiles`.
