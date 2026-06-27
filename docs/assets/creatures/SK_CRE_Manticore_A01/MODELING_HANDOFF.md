# SK_CRE_Manticore_A01 Modeling Handoff

## Purpose

Create the DCC source, skeletal mesh, shared skeleton target, proportion sheet, material plan, LODs, sockets, physics notes, and Unreal import path for Aerathea's base Manticore creature.

This is the parent package for `SK_CRE_Manticore_Interrupt_A01`. The interrupt variant must reuse this base creature anatomy and skeleton unless an approved production reason requires a separate branch.

## Source References

- Production package: `docs/assets/creatures/SK_CRE_Manticore_A01/PRODUCTION_PACKAGE.md`
- Source intake: `docs/assets/creatures/SK_CRE_Manticore_A01/SOURCE_CONCEPT_INTAKE.md`
- Source concept folder: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/`
- Primary source files: `Manticore.png`, `Manticore1.png`, `Manticore3.png`, `Manticore4.png`, `Manticore8.png`
- Secondary posture/reference files: `Manticore5.png`, `Manticore6.png`, `Manticore9.png`
- Variant-only or rejected-for-base cues: `Manticore2.png`, `Manticore7.png`, `Manticore10.png`
- Encounter variant reference: `GnomevsOgreandManticore8.png`

## Production Target

Large skeletal mesh creature with a lion body, dark mane, leathery bat/draconic wings, and a high segmented scorpion tail. The first build target is a wild ruin/desert predator with no saddle, faction armor, machinery, or heavy ornamental dressing.

## Modeling Constraints

- Author in centimeters.
- Pivot at ground center under body mass.
- Target shoulder height: 230-260 cm.
- Target head height: 300-340 cm in neutral alert pose.
- Target body length: 520-650 cm nose to rump.
- Target spread wingspan: 900-1100 cm.
- Target tail arc height: 480-600 cm.
- Keep wing and tail silhouettes readable from a third-person gameplay camera.
- Use broad mane clumps and texture detail; do not model hair strand clutter.
- Use leathery membrane panels; do not use feather slabs on the base creature.
- Keep the base free of armor, harnesses, saddles, faction symbols, and Teknomancy hardware.

## Blender Setup

- Collection: `SK_CRE_Manticore_A01`
- Armature: `SKEL_CRE_Manticore_A01`
- Mesh groups:
  - `Body_Lion`
  - `Head_Mane`
  - `Legs_Paws_Claws`
  - `Wings_Left_Right`
  - `Tail_Scorpion`
  - `Stinger`
  - `Teeth_Claws_Keratin`
  - Optional `Venom_Telegraph`
- Unit scale: centimeters.
- Apply transforms before export.
- Add sockets as empties or document intended bone attachments if sockets are finalized in Unreal.

## Skeleton And Proportion Plan

Core hierarchy:

- `root`
- `pelvis`
- `spine_01`
- `spine_02`
- `spine_03`
- `chest`
- `neck_01`
- `neck_02`
- `head`
- `jaw`
- `ear_l`, `ear_r`
- `mane_01` through `mane_04` optional broad-clump controls
- `clavicle_fl`, `upperarm_fl`, `lowerarm_fl`, `paw_fl`, `claw_fl_01` through `claw_fl_04`
- `clavicle_fr`, `upperarm_fr`, `lowerarm_fr`, `paw_fr`, `claw_fr_01` through `claw_fr_04`
- `thigh_bl`, `calf_bl`, `hock_bl`, `paw_bl`, `claw_bl_01` through `claw_bl_04`
- `thigh_br`, `calf_br`, `hock_br`, `paw_br`, `claw_br_01` through `claw_br_04`
- `wing_l_root`, `wing_l_upper`, `wing_l_lower`, `wing_l_hand`, `wing_l_finger_01` through `wing_l_finger_04`, `wing_l_tip`
- `wing_r_root`, `wing_r_upper`, `wing_r_lower`, `wing_r_hand`, `wing_r_finger_01` through `wing_r_finger_04`, `wing_r_tip`
- `tail_01` through `tail_08`
- `tail_stinger_base`
- `tail_stinger_tip`

Keep tail bones numerous enough for idle curl, sweep, and straight thrust. Keep wing fingers long enough to preserve membrane deformation without forcing dense geometry.

## Modeling Sequence

1. Block the lion body as a low, powerful feline mass at target scale.
2. Lock side silhouette with shoulders, mane, haunches, tail arc, and folded wings.
3. Block the wing spread and folded-wing poses before detail modeling.
4. Build the tail chain and stinger early so the threat silhouette is validated with the body.
5. Model head planes, muzzle, ears, jaw, teeth, paws, and claws.
6. Add broad mane clumps and chest/shoulder fur forms.
7. Add wing arms, fingers, and membrane panels with clean deformation loops.
8. Add tail segment armor plates over the deforming chain.
9. Retopologize for shoulders, hips, wing roots, elbows, paws, neck, jaw, tail base, and tail segments.
10. UV body, wings, and tail/claws as separate material families.
11. Create LOD0-LOD3 with explicit preservation of wing outline, tail arc, and stinger.
12. Export skeletal FBX and prepare physics proxy plan.

## Triangle Budget

- LOD0: 35k-50k tris.
- LOD1: 22k-30k tris.
- LOD2: 10k-16k tris.
- LOD3: 3k-6k tris.

## Texture Deliverables

- `T_CRE_Manticore_A01_Body_BC`
- `T_CRE_Manticore_A01_Body_N`
- `T_CRE_Manticore_A01_Body_ORM`
- `T_CRE_Manticore_A01_Wings_BC`
- `T_CRE_Manticore_A01_Wings_N`
- `T_CRE_Manticore_A01_Wings_ORM`
- `T_CRE_Manticore_A01_TailClaws_BC`
- `T_CRE_Manticore_A01_TailClaws_N`
- `T_CRE_Manticore_A01_TailClaws_ORM`
- Optional `T_CRE_Manticore_A01_Venom_E`

## Collision Deliverables

- Movement capsule or body collision proxy around the torso footprint.
- Physics bodies for pelvis, chest, neck, head, jaw, shoulders, forelegs, paws, hips, hind legs, wing roots, wing arms, tail chain, and stinger.
- Socket or trace markers for bite, claws, wing buffet, tail sweep, tail sting, venom, and landing dust.
- No per-membrane, per-mane, or per-tail-plate collision.

## Socket Deliverables

- `socket_head_fx`
- `socket_mouth_fx`
- `socket_bite_trace`
- `socket_claw_l`
- `socket_claw_r`
- `socket_foot_l`
- `socket_foot_r`
- `socket_wing_l_root`
- `socket_wing_r_root`
- `socket_wing_l_tip`
- `socket_wing_r_tip`
- `socket_tail_base`
- `socket_tail_mid`
- `socket_tail_stinger`
- `socket_vfx_venom_drip`
- `socket_vfx_landing_dust`
- `socket_back_variant`

## Export Targets

- Blender source: `SourceAssets/Blender/Creatures/Manticores/SK_CRE_Manticore_A01/SK_CRE_Manticore_A01.blend`
- FBX export: `SourceAssets/Exports/Creatures/Manticores/SK_CRE_Manticore_A01/SK_CRE_Manticore_A01.fbx`
- Unreal skeletal mesh: `/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01`
- Skeleton: `/Game/Aerathea/Creatures/Manticores/Base/SKEL_CRE_Manticore_A01`
- Physics asset: `/Game/Aerathea/Creatures/Manticores/Base/PHYS_CRE_Manticore_A01`
- Animation Blueprint: `/Game/Aerathea/Creatures/Manticores/Base/ABP_CRE_Manticore_A01`

## Unreal Validation

- Imports at intended creature scale.
- Pivot sits at ground center under body mass.
- LODs preserve lion body, wing outline, high tail arc, and stinger.
- Material slot count is 3 target and 4 maximum.
- Physics bodies cover gameplay-relevant masses without per-detail collision.
- Wing folded and wing spread poses fit review framing.
- `SK_CRE_Manticore_Interrupt_A01` can reference the skeleton and socket plan without anatomy changes.

## Acceptance Checklist

- Lion body, leathery wings, and scorpion tail read from side, front, and gameplay camera angles.
- Tail stinger remains visible and usable as a combat telegraph.
- Wing membranes are bat/draconic, not feathered.
- Body proportions are threatening beside Ogres while remaining below boss-dragon scale.
- Mid-poly topology supports folded wings, wing buffet, leap, tail sweep, tail sting, and prowl locomotion.
- Texture, LOD, socket, collision, and Unreal import deliverables are documented.
