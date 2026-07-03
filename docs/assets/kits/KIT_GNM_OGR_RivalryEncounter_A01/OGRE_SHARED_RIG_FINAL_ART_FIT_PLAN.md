# Ogre Shared Rig Final-Art Fit Plan

## Purpose

This plan locks the final-art handoff for the Ogre base and first four class variants used by `KIT_GNM_OGR_RivalryEncounter_A01`. It exists so final sculpt, retopo, UV, texture, physics, and animation work can improve the art model without breaking the validated shared Ogre skeleton, startup scene, encounter coordinator, or class socket contracts.

## Approved Execution Status

- 2026-06-28: Flamestrike approved the production order to finish the Gnome/Ogre encounter final-art foundation first, then complete the Ogre shared rig/art-model fit before moving to Iona, Infernal, Giant, Portal, and Abyss lanes.
- 2026-06-28: `Tools/Unreal/validate_ogre_shared_skeletons.py` passed through `UnrealEditor-Cmd`; `SK_OGR_Base_Male_A01`, `SK_OGR_Teknomancer_A01`, `SK_OGR_Warrior_Rival_A01`, `SK_OGR_Shaman_A01`, and `SK_OGR_Necromancer_A01` are bound to `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton`.

## Shared Rig Invariants

- Skeleton path remains `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton` for the male final-art pass.
- Final art must not rename, remove, rescale, or rotate the shared root, pelvis, spine, neck, head, arm, hand, leg, foot, or IK/control bones.
- Preserve the Ogre male review baseline at about 330 cm and the female fit target at about 315 cm unless a later scale-chart approval changes it.
- Pivot remains ground center between feet. Import scale remains 1 Unreal unit = 1 cm, with no import-scale compensation.
- Base body silhouette remains broad and war-created: huge shoulders, barrel chest, thick neck, heavy forearms, slab hands, dense legs, oversized feet.
- Class gear is modular over the base body. Do not bake Teknomancer, Warrior, Shaman, or Necromancer costume shapes into the base body.
- Final mesh replacements must preserve current asset paths, actor assignment expectations, validation scripts, and socket names unless a migration note and validator update are committed in the same pass.

## Final-Art Fit Order

1. **Freeze the validated baseline.**
   - Keep the current first-pass Unreal assets as the reference slice.
   - Save baseline viewport captures for male base, Teknomancer, Warrior, Shaman, and Necromancer before replacement.
   - Re-run `Tools/Unreal/validate_ogre_shared_skeletons.py` before any final-art import.
2. **Finish `SK_OGR_Base_A01` male/female body art.**
   - Sculpt and retopo final male and female bodies from the approved Ogre scale/proportion anchors.
   - Preserve socket-bearing bones and broad mass from the validation mesh.
   - Author final body UVs and skin texture set before class outfit finalization.
3. **Skin and validate the male shared skeleton.**
   - Bind final male body to `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton`.
   - Tune weights for shoulders, elbows, wrists, fingers, pelvis, knees, ankles, jaw, and neck before class overlays.
   - Run the shared-skeleton validator and startup validation after the base body swap.
4. **Fit class overlays in encounter priority order.**
   - `SK_OGR_Teknomancer_A01`: first class fit because it anchors the Gnome Mek rivalry and crude Teknomancy silhouette.
   - `SK_OGR_Warrior_Rival_A01`: second class fit because it anchors melee pressure, shield-wall opposition, shield traces, and hammer impact VFX.
   - `SK_OGR_Shaman_A01`: third class fit because it expands Ogre caster language without Tek hardware.
   - `SK_OGR_Necromancer_A01`: fourth class fit because it locks grave-cairn language and separates green-black necromancy from shamanic glow.
5. **Fit female Ogre class variants after the male contract is stable.**
   - Female variants inherit the same class-kit logic but require proportion-aware armor, staff, shield, and reactor offsets.
   - Female class fit must preserve the approved female Ogre height band: 305-320 cm.
6. **Tune physics, collision, and LODs after topology is final.**
   - Replace generated physics placeholders with simplified bodies for torso, limbs, hands, feet, staff, shield, hammer, reactor, and large trophy clusters only where needed.
   - Keep minor straps, chains, charms, rivets, stitches, and micro-surface detail non-colliding.
   - Preserve LOD0-LOD3 and reduce small details before body mass or class-defining silhouettes.
7. **Run validation and visual review after each import.**
   - Re-run the smallest focused validator first, then startup validation.
   - Capture a clean review image after validators pass; marker views are only needed if orientation is uncertain.

## Required Socket Contract

Base Ogre sockets that must remain valid:

- `hand_l_weapon`
- `hand_r_weapon`
- `back_weapon`
- `spine_teknomancy_pack`
- `shoulder_l_large`
- `shoulder_r_large`
- `belt_front`
- `belt_back`
- `vfx_mouth`
- `vfx_eye_l`
- `vfx_eye_r`
- `vfx_chest_core`

Class-specific sockets that must remain valid where used:

- Teknomancer: `hand_l_offhand`, `hand_r_twohand_grip`, `hand_l_twohand_grip`, `vfx_hammer_core`, `vfx_bracer_l`, `vfx_bracer_r`, `vfx_stomp_ground`.
- Warrior: `back_large_weapon`, `back_shield`, `vfx_belt_forge`, `vfx_shield_core`, `vfx_hammer_core`, `vfx_stomp_ground`, `head_fx`.
- Shaman: `hand_r_staff`, `hand_l_cast`, `staff_head_fx`, `staff_ground_fx`, `staff_rune_wheel_fx`, `belt_charm_fx`, `vfx_cast_hand_l`, `vfx_cast_hand_r`, `vfx_chest_rune`, `vfx_totem_slam`, `vfx_storm_channel`.
- Necromancer: `hand_r_staff`, `hand_l_cast`, `staff_lantern_fx`, `staff_ground_fx`, `skull_belt_fx`, `back_trophy_fx`, `vfx_cast_hand_l`, `vfx_cast_hand_r`, `vfx_necro_orb`, `vfx_soul_drain`, `vfx_corpse_raise`.

## Art Model Requirements

- Model real geometry for body mass, face planes, hands, feet, major armor plates, large shoulder forms, staff heads, tower shield, hammer, reactor housings, tanks, large bone trophies, large cairn stones, and dominant cloth/fur silhouettes.
- Use textures, normal maps, AO, and packed ORM for small scars, pores, scratches, stitching, rivets, small runes, chain wear, cloth weave, hide grain, bone pores, and stone cracks.
- Keep emissive accents focused: Teknomancer forge/reactor glow, Warrior forge windows, Shaman ember/storm runes, Necromancer grave-green lantern/cast effects.
- Avoid dense dangling clutter that will skin poorly, disappear in LODs, or create noisy silhouettes.
- Preserve class separation from distance: Teknomancer = reactor/bracers/hammer, Warrior = tower shield/hammer, Shaman = rune staff/hide/fur/cairn charms, Necromancer = grave-lantern/skulls/tomb plates/green-black glow.

## Texture And Material Plan

- Base Ogre body target: 2K texture set for common use, 4K only for named hero or cinematic review.
- Class overlay target: 2K texture sets; shared tiling detail materials may supplement but do not replace authored BC/N/ORM/E maps.
- Required maps per final mesh or overlay:
  - Base Color / Albedo
  - Normal
  - Ambient Occlusion or packed ORM
  - Packed ORM: Occlusion, Roughness, Metallic
  - Emissive only for eyes, runes, reactors, forge windows, staff glow, and spell telegraphs
- Material slot budget:
  - Base body: 3 slots target.
  - Fully equipped class variant: 4-5 slots target.
  - Do not add material slots for tiny decoration.

## Triangle And LOD Targets

| Asset | LOD0 target | Material target | Notes |
| --- | ---: | ---: | --- |
| `SK_OGR_Base_A01` body per sex | 35k-55k tris | 3 | Hero variants can justify 4K textures, not extra micro-geometry |
| `SK_OGR_Teknomancer_A01` full equipped | 50k-70k tris | 4-5 | Reactor, bracers, hammer, and tanks get geometry priority |
| `SK_OGR_Warrior_Rival_A01` full equipped | 35k-55k common, 60k-70k elite | 4-5 | Shield slab and hammer silhouette outrank small spikes |
| `SK_OGR_Shaman_A01` full equipped | 50k-65k tris | 4-5 | Staff, rune wheel, fur mass, and large charms get priority |
| `SK_OGR_Necromancer_A01` full equipped | 50k-70k tris | 4-5 | Grave-lantern staff, skull belt, tomb plates, and trophy clusters get priority |

LOD reduction order:

1. Tiny rivets, stitches, scratches, and small rune cuts.
2. Small straps, small chain loops, and tiny dangling charms.
3. Secondary spikes, minor plate bevels, and small trophy detail.
4. Interior/backside costume detail.
5. Small pipes, small ornaments, and minor cloth tears.
6. Large class gear only after small detail has been removed.
7. Primary Ogre body mass and class-defining silhouette last.

## Collision And Physics Plan

- Gameplay movement uses the Ogre character capsule, not costume collision.
- Base physics bodies cover head, torso, pelvis, upper/lower arms, hands, upper/lower legs, and feet.
- Add simplified auxiliary bodies only for dominant gameplay shapes: tower shield, hammer, staff, back reactor, large tank, large trophy cluster.
- Weapon and spell mechanics should use sockets, traces, and Blueprint/gameplay volumes rather than detailed mesh collision.
- Disable collision on small straps, chains, minor charms, small spikes, cloth strips, fur trim, and tiny trophies.

## Validation Gates

Run after each final-art import or skeleton-affecting change:

1. `Tools/Unreal/validate_ogre_shared_skeletons.py`
2. `Tools/Unreal/validate_startup_scene.py`

Run when encounter actor assignments, VFX sockets, or phase views are touched:

1. `Tools/Unreal/validate_gnome_ogre_encounter_phase_sequence.py`
2. `Tools/Unreal/validate_gnome_ogre_gameplay_timing_traces.py`
3. `Tools/Unreal/validate_gnome_ogre_vfx_polish_targets.py`
4. `Tools/Unreal/capture_gnome_ogre_phase_reviews.sh`

## Final-Art Acceptance Checklist

- The base and all four class meshes remain bound to the validated shared male Ogre skeleton.
- Broad Ogre silhouette, height, socket placement, and ground pivot are preserved.
- Each class is readable at MMO camera distance without relying on tiny details.
- Skin weights support heavy shoulders, huge hands, weapon grips, stomp poses, staff casts, shield braces, and large gear silhouettes.
- Physics bodies are tuned and simplified after final topology, not left as generated placeholders.
- Texture sets include BC/N/ORM and focused emissive where needed.
- LOD0-LOD3 exist and preserve body mass and class-defining shapes.
- Startup validation, shared-skeleton validation, and relevant encounter validators pass after replacement.
