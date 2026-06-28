# Gnome And Gryphon Follow-Up Readiness

## Purpose

This handoff keeps the `SK_GNM_Base_A01` and `SK_CRE_Gryphon_A01` follow-up work bounded. Both assets already exist as validated first-pass review imports; this document defines what can be checked now and what must wait for approved final sculpt, skin weighting, physics, and animation direction.

Focused validator:

`Tools/Unreal/validate_gnome_gryphon_followup_readiness.py`

## Current Readiness

| Asset | Current First-Pass State | Ready To Validate Now | Blocked Until Final Art |
| --- | --- | --- | --- |
| `SK_GNM_Base_A01` | Imported skeletal mesh, generated skeleton, review sockets, generated physics asset, ABP placeholder, ToolPack `back_pack` fit preview, LOD0-LOD3, startup validation passing | Skeleton assignment, physics asset assignment, required sockets, material slots, ABP placeholder, startup presence | Final sculpt/retopo, clean skin weights, final sockets, UVs, BC/N/ORM texture sets, tuned physics bodies, real locomotion/attachment animation Blueprint |
| `SK_CRE_Gryphon_A01` | Imported skeletal mesh, generated skeleton, review sockets, generated physics asset, ABP placeholder, wing-spread animation blockout, LOD0-LOD3, startup validation passing | Skeleton assignment, physics asset assignment, required sockets, material slots, ABP placeholder, wing-spread animation asset, startup presence | Final golden gryphon sculpt/retopo, wing/neck/jaw/tail skin weights, final sockets, UVs, BC/N/ORM texture sets, tuned physics bodies, full locomotion/flight/attack/death animation set |

## Gnome Follow-Up Notes

- Preserve the compact adult 110-120 cm gnome height range and four-fingers-plus-thumb hand rule.
- Keep the first-pass `back_pack`, `head_goggles`, belt, weapon, muzzle, and Aetherium sockets until final gear fit is approved.
- Do not tune final physics bodies against the current blockout; use the current physics asset only for validation and coarse attachment testing.
- Real follow-up animation work should start only after the final sculpt and clean skin weights exist.
- The first practical tests after final art should be locomotion, backpack fit, one-handed tool use, two-handed weapon grip, pistol aim/fire, and interact/crafting poses.

## Gryphon Follow-Up Notes

- Preserve eagle-front/lion-rear readability, wing outline, talons, haunches, and tail tuft before polishing detail.
- Keep mount and saddle sockets planned but inactive until mount gameplay rules are approved.
- Do not add per-feather collision or tune final wing physics against the blockout.
- Real follow-up animation work should start only after final wing topology and skin weighting are stable.
- The first practical tests after final art should be grounded idle, walk/trot, wing spread, takeoff, glide, landing, talon swipe, bite/peck, pounce, hit reactions, and death.

## Required Validation

Run the focused validator before broad startup validation when changing either asset:

1. `Tools/Unreal/validate_gnome_gryphon_followup_readiness.py`
2. `Tools/Unreal/validate_startup_scene.py`

The focused validator confirms expected skeleton binding, physics asset assignment, material slots, required sockets, ABP placeholders, and the gryphon wing-spread animation asset.

## Quality Gate

- The first-pass assets remain usable for scale, socket, LOD, and attachment planning.
- Final physics, animation, and socket authoring are not treated as complete until final geometry and skin weighting are approved.
- Gnome gear and gryphon mount hooks stay socket-driven rather than collision-heavy.
- Startup validation remains the broad gate after any focused readiness changes.
