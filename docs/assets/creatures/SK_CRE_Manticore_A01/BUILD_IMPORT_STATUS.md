# SK_CRE_Manticore_A01 Build And Import Status

## Current Status

- Production scope: base Aerathea Manticore creature package.
- Build/import status: first-pass DCC review source generated and imported to Unreal.
- Source mesh status: Blender source and FBX export exist.
- Unreal state: skeletal mesh imported, generated skeleton created, material instances assigned, LOD0-LOD3 generated, sockets added, physics asset assigned, animation Blueprint placeholder created, startup review actor placed, validation passing.
- Dependency unlocked: `SK_CRE_Manticore_Interrupt_A01` now imports against the base Manticore skeleton.

## Source And Export Paths

- Blender source: `SourceAssets/Blender/Creatures/Manticores/SK_CRE_Manticore_A01/SK_CRE_Manticore_A01.blend`
- FBX export: `SourceAssets/Exports/Creatures/Manticores/SK_CRE_Manticore_A01/SK_CRE_Manticore_A01.fbx`
- DCC review render: `Saved/Automation/GnomeOgreRemainingReview/SK_CRE_Manticore_A01_DCCReview.png`
- DCC build script: `Tools/DCC/build_gnome_ogre_remaining_assets.py`
- Unreal import script: `Tools/Unreal/import_gnome_ogre_remaining_assets.py`

## Unreal Assets

- `/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01`
- `/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01_Skeleton`
- `/Game/Aerathea/Creatures/Manticores/Base/PHYS_CRE_Manticore_A01`
- `/Game/Aerathea/Creatures/Manticores/Base/ABP_CRE_Manticore_A01`
- Startup actor: `AET_PROD_CRE_Manticore_A01`
- Material instances:
  - `/Game/Aerathea/Materials/Instances/MI_CRE_Manticore_A01_Manticore_Body`
  - `/Game/Aerathea/Materials/Instances/MI_CRE_Manticore_A01_Manticore_Mane`
  - `/Game/Aerathea/Materials/Instances/MI_CRE_Manticore_A01_Manticore_Wing`
  - `/Game/Aerathea/Materials/Instances/MI_CRE_Manticore_A01_Manticore_TailClaw`
  - `/Game/Aerathea/Materials/Instances/MI_CRE_Manticore_A01_Manticore_Venom`

## Validation

- `Tools/Unreal/validate_startup_scene.py` now checks the base mesh, physics asset, generated skeleton binding, LOD count, sockets, bounds, runtime visibility, and startup actor.
- Latest validation result: passing with `121` expected assets, `46` expected actor labels, and `25` ground tiles.

## Documentation

- Production package: `docs/assets/creatures/SK_CRE_Manticore_A01/PRODUCTION_PACKAGE.md`
- Modeling handoff: `docs/assets/creatures/SK_CRE_Manticore_A01/MODELING_HANDOFF.md`
- Source intake: `docs/assets/creatures/SK_CRE_Manticore_A01/SOURCE_CONCEPT_INTAKE.md`
- Related encounter variant: `docs/assets/creatures/SK_CRE_Manticore_Interrupt_A01/PRODUCTION_PACKAGE.md`

## Remaining To Finalize

1. Review the first-pass scale and silhouette against Ogres, heavy Mek, Gryphon, and the encounter staging.
2. Replace blockout creature geometry with approved final sculpt/retopo.
3. Author final UVs, hand-painted body/wing/tail texture sets, packed ORM, and optional venom emissive map.
4. Tune physics bodies for torso, head, legs, wing roots, tail chain, and stinger.
5. Build the full animation set for prowl, leap, wing buffet, tail sweep, tail sting, bite/claw, hit reactions, death, and interrupt-specific timing.
