# SK_CRE_Gryphon_A01 Modeling Handoff

## Purpose

Create the DCC source, skeletal mesh, skeleton target, material plan, LODs, and Unreal import path for Aerathea's first large creature package.

## Source References

- Production package: `docs/assets/creatures/SK_CRE_Gryphon_A01/PRODUCTION_PACKAGE.md`
- Source concept folder: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/`
- Relevant source files: `Gryphon.png`, `Gryphon1.png`, `Gryphon2.png`, `Gryphon5.png`, `Gryphon6.png`, `Gryphon7.png`, `Gryphon8.png`, `Gryphon9.png`, `Gryphon10.png`

## Production Target

Large skeletal mesh creature with eagle head/wings/forelegs/talons and lion rear body/hind legs/tail. The first build target is a golden mountain gryphon suitable for creature pipeline validation and future mount planning.

## Modeling Constraints

- Author in centimeters.
- Pivot at ground center under body mass.
- Preserve eagle-front/lion-rear anatomy from all main camera angles.
- Model only large silhouette feathers; texture dense feather/fur detail.
- Keep base creature free of saddle, armor, or magical glow.
- Include wing topology suitable for folded, spread, flap, glide, and landing poses.

## Blender Setup

- Collection: `SK_CRE_Gryphon_A01`
- Mesh groups:
  - `Body_EagleFront`
  - `Body_LionRear`
  - `Head_Beak_Crest`
  - `Wings_Left_Right`
  - `Forelegs_Talons`
  - `Hindlegs_Paws`
  - `Tail_Tuft`
- Skeleton: `SKEL_CRE_Gryphon_A01`
- Add sockets as empties or document their intended bone attachment points.

## Modeling Sequence

1. Block body proportions at target scale.
2. Establish side silhouette: beak, chest, wings, lion haunches, tail.
3. Block wing spread and folded wing volumes before adding feather slabs.
4. Model head, beak, crest, neck ruff, talons, paws, and tail tuft.
5. Retopologize for shoulders, wing joints, elbows/wrists, hips, knees, ankles, neck, jaw, and tail.
6. Create major feather clumps as controlled geometry.
7. UV body/wing/keratin material sets.
8. Build LOD0-LOD3 with explicit wing silhouette preservation.
9. Create physics asset proxy bodies and export skeletal FBX.

## Triangle Budget

- LOD0: 35k-50k tris.
- LOD1: 22k-30k tris.
- LOD2: 10k-16k tris.
- LOD3: 3k-6k tris.

## Texture Deliverables

- `T_CRE_Gryphon_A01_Body_BC`
- `T_CRE_Gryphon_A01_Body_N`
- `T_CRE_Gryphon_A01_Body_ORM`
- `T_CRE_Gryphon_A01_Wings_BC`
- `T_CRE_Gryphon_A01_Wings_N`
- `T_CRE_Gryphon_A01_Wings_ORM`
- `T_CRE_Gryphon_A01_Eyes_BC`

## Collision Deliverables

- Creature movement capsule/body proxy.
- Physics asset bodies for head, neck, chest, pelvis, wings, legs, paws, talons, and tail.
- No per-feather collision.

## Export Targets

- Blender source: `SourceAssets/Blender/Creatures/Gryphon/SK_CRE_Gryphon_A01/SK_CRE_Gryphon_A01.blend`
- FBX export: `SourceAssets/Exports/Creatures/Gryphon/SK_CRE_Gryphon_A01/SK_CRE_Gryphon_A01.fbx`
- Unreal skeletal mesh: `/Game/Aerathea/Creatures/Gryphon/Base/SK_CRE_Gryphon_A01`
- Skeleton: `/Game/Aerathea/Creatures/Gryphon/Base/SKEL_CRE_Gryphon_A01`
- Physics asset: `/Game/Aerathea/Creatures/Gryphon/Base/PHYS_CRE_Gryphon_A01`

## Unreal Validation

- Imports at correct creature scale.
- Grounded idle pose fits startup review space.
- Wing spread view does not exceed intended review bounds.
- Material slots are 3 target, 4 maximum.
- LODs preserve the beak, wing outline, talons, haunches, and tail tuft.
- Physics asset does not include tiny feather bodies.

## Acceptance Checklist

- Eagle front, lion rear, clear talons and lion tail.
- Noble mountain guardian read.
- Buildable mid-poly creature topology.
- Large feathers modeled only where they affect silhouette.
- Full skeleton/physics/animation/socket plan ready for DCC and Unreal.
