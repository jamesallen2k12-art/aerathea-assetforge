# SK_CRE_Manticore_A01 Build And Import Status

## Current Status

- Production scope: base Aerathea Manticore creature package.
- Current state: production package, source concept intake, modeling handoff, skeleton/proportion plan, material plan, LOD plan, collision plan, sockets, and Unreal import notes are ready.
- DCC state: not started.
- Unreal state: not imported.
- Dependency unlocked: `SK_CRE_Manticore_Interrupt_A01` can now reference a base body/skeleton/proportion package, but should still wait for approval before DCC build.

## Planned Source And Export Paths

- Blender source: `SourceAssets/Blender/Creatures/Manticores/SK_CRE_Manticore_A01/SK_CRE_Manticore_A01.blend`
- FBX export: `SourceAssets/Exports/Creatures/Manticores/SK_CRE_Manticore_A01/SK_CRE_Manticore_A01.fbx`
- DCC review render: `Saved/Automation/ManticoreBaseReview/SK_CRE_Manticore_A01_DCCReview.png`

## Planned Unreal Assets

- `/Game/Aerathea/Creatures/Manticores/Base/SK_CRE_Manticore_A01`
- `/Game/Aerathea/Creatures/Manticores/Base/SKEL_CRE_Manticore_A01`
- `/Game/Aerathea/Creatures/Manticores/Base/PHYS_CRE_Manticore_A01`
- `/Game/Aerathea/Creatures/Manticores/Base/ABP_CRE_Manticore_A01`
- `/Game/Aerathea/Materials/Instances/MI_CRE_Manticore_A01_Body`
- `/Game/Aerathea/Materials/Instances/MI_CRE_Manticore_A01_Wings`
- `/Game/Aerathea/Materials/Instances/MI_CRE_Manticore_A01_TailClaws`
- Optional `/Game/Aerathea/Materials/Instances/MI_CRE_Manticore_A01_Venom`

## Review Requirements Before DCC Build

- Confirm the base direction: tawny/dark ruin predator, not white feathered/frost variant.
- Confirm the scale band: 230-260 cm shoulder height and 900-1100 cm spread wingspan.
- Confirm the shared skeleton supports the interrupt variant, future variants, and base combat animations.
- Confirm no faction armor, saddles, or Teknomancy devices appear on the base wild creature.

## Blocking Items

- Visual approval of this base package is needed before DCC modeling starts.
- Final sculpt, retopo, skin weighting, UVs, authored textures, physics asset tuning, and animation production are not started.

## Documentation

- Production package: `docs/assets/creatures/SK_CRE_Manticore_A01/PRODUCTION_PACKAGE.md`
- Modeling handoff: `docs/assets/creatures/SK_CRE_Manticore_A01/MODELING_HANDOFF.md`
- Source intake: `docs/assets/creatures/SK_CRE_Manticore_A01/SOURCE_CONCEPT_INTAKE.md`
- Related encounter variant: `docs/assets/creatures/SK_CRE_Manticore_Interrupt_A01/PRODUCTION_PACKAGE.md`

## Next Steps

1. Review and approve the base `SK_CRE_Manticore_A01` direction, skeleton, and proportions.
2. Build the first-pass DCC source for `SK_CRE_Manticore_A01`.
3. Export FBX and import to `/Game/Aerathea/Creatures/Manticores/Base/`.
4. Add material instances, generated LOD0-LOD3, physics asset, sockets, and ABP placeholder.
5. Validate scale and silhouette against Ogre, Heavy Mek, and Gryphon references before building the interrupt variant.
