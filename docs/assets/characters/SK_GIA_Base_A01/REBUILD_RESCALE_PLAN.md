# SK_GIA_Base_A01 Rebuild/Rescale Plan

## Purpose

This plan records the approved Giant base rebuild/rescale pass for `SK_GIA_Base_A01`. The earlier staged DCC/Unreal import was superseded by the A04 baseline and has been replaced by a regenerated first-pass scale review import. The current import locks the A04 body/scale baseline for downstream planning, but it is not final sculpted or hand-painted production art.

## Approved Execution Status

- 2026-06-28: Flamestrike approved rebuilding/rescaling `SK_GIA_Base_A01` to the current A04 Giant baselines.
- Approved female baseline: 442 cm / about 14'6".
- Approved male baseline: 470 cm / about 15'5".
- 2026-06-28: `Tools/DCC/build_giant_base.py` regenerated the Blender review source, male FBX, female FBX, and DCC review image to the approved baselines.
- 2026-06-28: `Tools/Unreal/import_giant_base.py` reimported the male/female skeletal meshes, sockets, physics assets, LOD0-LOD3, animation Blueprint placeholders, and startup actors.
- 2026-06-28: `Tools/Unreal/validate_giant_base_scale.py` passed with male visible bounds height 464.26 cm for the 470 cm baseline and female visible bounds height 429.35 cm for the 442 cm baseline.
- 2026-06-28: `Tools/Unreal/validate_startup_scene.py` passed after the import.
- Blood Axe armory, Giant cave-town modules, Giant doors/stairs, named Giant NPCs, and Giant weapon sockets remain downstream of this validated base scale.

## Scope

This pass updates the first-pass review body scale and import targets. It does not mark the Giant body as final sculpted or hand-painted production art.

Included:

- Update DCC review/export generation to 442 cm female and 470 cm male baselines.
- Regenerate Blender review source and male/female FBX exports.
- Reimport `SK_GIA_Base_Male_A01` and `SK_GIA_Base_Female_A01` into Unreal.
- Preserve current Unreal asset names, folder paths, socket names, physics asset names, animation Blueprint placeholders, and startup actor labels.
- Validate startup scene and review scale/camera framing after import.

Excluded:

- Blood Axe armor, trophies, red banners, raider markings, or hostile tribe body variants.
- Final sculpt/retopo/UV/texture polish.
- Giant cave-town, armory, warband, or named NPC production packages.

## DCC Targets

- Blender source: `SourceAssets/Blender/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_A01.blend`
- Male FBX export: `SourceAssets/Exports/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_Male_A01.fbx`
- Female FBX export: `SourceAssets/Exports/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_Female_A01.fbx`
- DCC script: `Tools/DCC/build_giant_base.py`
- Approved script constants:
  - `GIANT_MALE_BASELINE_CM = 470.0`
  - `GIANT_FEMALE_BASELINE_CM = 442.0`

## Unreal Targets

- Import script: `Tools/Unreal/import_giant_base.py`
- Male skeletal mesh: `/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01`
- Female skeletal mesh: `/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01`
- Male skeleton: `/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Male_A01_Skeleton`
- Female skeleton: `/Game/Aerathea/Characters/Giants/Base/SK_GIA_Base_Female_A01_Skeleton`
- Male physics asset: `/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Male_A01`
- Female physics asset: `/Game/Aerathea/Characters/Giants/Base/PHYS_GIA_Base_Female_A01`
- Startup actors:
  - `AET_PROD_GiantMaleBase_A01`
  - `AET_PROD_GiantFemaleBase_A01`

## Validation Gates

Run after DCC generation and Unreal import:

1. `Tools/Unreal/validate_giant_base_scale.py` - passed on 2026-06-28.
2. `Tools/Unreal/validate_startup_scene.py` - passed on 2026-06-28.
3. Focused startup or Giant review capture before visual approval.
4. Compare against 180 cm humanoid, 110 cm gnome, 270 cm minotaur, and future Giant door/stair markers.

Acceptance checks:

- Female Giant reads at the approved 442 cm baseline.
- Male Giant reads at the approved 470 cm baseline.
- Feet remain grounded and pivots remain at world origin.
- Required Giant sockets still exist.
- Startup scene validation passes.
- Neutral/civilized Giant identity remains separate from Blood Axe visual language.
