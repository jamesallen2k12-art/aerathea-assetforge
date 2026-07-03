# SM_INF_WitnessChains_A01 Implementation Packet

## Task Scope

- Task: `AET-MA-20260629-043`
- Build scope: docs-only implementation packet.
- Result target: prepare `SM_INF_WitnessChains_A01` for a future modular DCC and Unreal build lane using the existing production package and Balgoroth cult readiness matrix.
- Not included: Blender source creation, FBX export, Unreal import, skeletal mesh setup, physics simulation, chain break behavior, gameplay restraint behavior, gore escalation, startup scene placement, final visual approval, final authored textures, or final shader polish.

This packet converts the production package into an implementation-ready task contract. It does not approve or start asset construction.

## Dependency Evidence

| Dependency | Evidence | Status |
| --- | --- | --- |
| `SM_INF_WitnessChains_A01` package | `docs/assets/props/SM_INF_WitnessChains_A01/PRODUCTION_PACKAGE.md` | Production package ready. |
| `KIT_INF_BalgorothCult_A01` readiness | `docs/assets/kits/KIT_INF_BalgorothCult_A01/IMPLEMENTATION_READINESS_MATRIX.md` | WitnessChains is recommended after AshBasin and must preserve sparse chunky chain geometry, shared materials, non-complex collision, and explicit physics/restraint stop gates. |
| `MI_INF_CultStone_Set_A01` | `docs/assets/materials/MI_INF_CultStone_Set_A01/BUILD_IMPORT_STATUS.md` | First-pass Unreal material set implemented and focused validation passed. Final textures and final shader polish remain open. |
| `SM_INF_BalgorothSigil_A01` | `docs/assets/props/SM_INF_BalgorothSigil_A01/BUILD_IMPORT_STATUS.md` | Validated symbol language dependency for broad anchor relief only. Do not copy or redesign the symbol in this packet. |

## Selected Variants And Modular Lengths

The future build lane should treat `A01` as a static mesh dressing set:

| Variant | Target Unreal mesh | Target scale or range | Primary placement |
| --- | --- | --- | --- |
| Wall hanging chain pair | `SM_INF_WitnessChains_WallPair_A01` | 180-320 cm hanging length | Worthiness walls, altar backs, gate approaches |
| Floor anchor chain coil | `SM_INF_WitnessChains_FloorAnchor_A01` | 80-160 cm footprint | Den floors, alcove bases, trial perimeter dressing |
| Suspended witness loop | `SM_INF_WitnessChains_SuspendedLoop_A01` | 100-220 cm drop | Ceiling hooks, tall arch interiors, high wall anchors |
| Broken chain fragment | `SM_INF_WitnessChains_BrokenFragment_A01` | 40-120 cm length | Floor scatter, wall-side fragments, aftermath dressing |
| Anchor plate with claw hook | `SM_INF_WitnessChains_AnchorPlate_A01` | 70-200 cm plate scale depending on wall/floor use | Reusable anchor module for wall, floor, and hanging variants |

Authoring presets may use short, medium, and long chain lengths inside the same source collection. If a future build lane exports those sizes separately, append `_Short`, `_Medium`, or `_Long` before `_A01` while preserving the base family name.

Readability target: oppressive ritualized chain dressing with chunky blackened iron links, basalt anchors, claw hooks, sparse bone/horn markers, ash wear, and small restrained ember channels. It must not read as generic dungeon chains, fine jewelry, gore equipment, active restraint gameplay, or physics-heavy rope simulation.

## DCC Build Contract

Future DCC lane may create:

- `Tools/DCC/build_infernal_witness_chains.py`
- `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/SM_INF_WitnessChains_A01.blend`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/SM_INF_WitnessChains_WallPair_A01.fbx`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/SM_INF_WitnessChains_FloorAnchor_A01.fbx`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/SM_INF_WitnessChains_SuspendedLoop_A01.fbx`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/SM_INF_WitnessChains_BrokenFragment_A01.fbx`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_WitnessChains_A01/SM_INF_WitnessChains_AnchorPlate_A01.fbx`
- `Saved/Automation/InfernalWitnessChainsReview/SM_INF_WitnessChains_A01_DCCReview.png`

Required DCC features:

- Wall variants pivot at top/back anchor center.
- Floor variants pivot at bottom center.
- Broken fragments pivot at center bottom.
- Centimeter scale, 1 Unreal unit = 1 cm.
- Real geometry for large chain links, anchor plates, claw hooks, broken end caps, wall brackets, floor brackets, and broad anchor relief.
- Modular link chunks with few large readable links; do not simulate or model hundreds of independent small links.
- Texture or material detail for soot, scratches, pitted iron, ash, small dents, and link wear.
- Sparse bone/horn witness markers only where they reinforce silhouette and do not become clutter.
- No thin dangling micro-chains, dense rings, gore hooks, readable text, chain physics rigs, or restraint mechanisms that imply gameplay behavior.

## Unreal Import Contract

Future Unreal lane may create:

- `Tools/Unreal/import_infernal_witness_chains.py`
- `Tools/Unreal/validate_infernal_witness_chains.py`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/WitnessChains/SM_INF_WitnessChains_WallPair_A01`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/WitnessChains/SM_INF_WitnessChains_FloorAnchor_A01`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/WitnessChains/SM_INF_WitnessChains_SuspendedLoop_A01`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/WitnessChains/SM_INF_WitnessChains_BrokenFragment_A01`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/WitnessChains/SM_INF_WitnessChains_AnchorPlate_A01`

Import requirements:

- Asset type: Static Mesh set.
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/WitnessChains/`
- Scale: centimeters.
- Collision: none or simple non-complex collision only.
- Default collision policy: non-blocking dressing.
- LODs: LOD0-LOD3 required for every imported mesh variant.
- Startup scene: out of scope unless a later placement task explicitly assigns it.
- Physics assets, skeletal meshes, constraints, breakable chains, and gameplay restraint logic are out of scope.

## Material Slot Plan

Preferred material lanes:

1. `MI_INF_CultStone_BlackIron_A01`
2. `MI_INF_CultStone_Basalt_A01`
3. `MI_INF_CultStone_ScorchedRed_A01`
4. `MI_INF_CultStone_BoneHorn_A01`
5. `MI_INF_CultStone_EmissiveChannel_A01` or future `MI_INF_WitnessChains_A01_Emissive` if the build task owns the custom instance.

Rules:

- Most variants should use 2-3 material slots.
- Anchor-heavy hero assemblies may use 4-5 slots only when bone/horn markers or ember pips need separate control.
- Emissive is limited to anchor grooves or broken-circle relief pips. Chains must not become glowing ropes.
- Chain wear should be value and roughness driven, not bright steel shine.
- Final authored textures remain future work:
  - `T_INF_WitnessChains_A01_BC`
  - `T_INF_WitnessChains_A01_N`
  - `T_INF_WitnessChains_A01_ORM`
  - `T_INF_WitnessChains_A01_E`

## Socket And Hang-Point Contract

Required Unreal sockets:

- `vfx_anchor_ember`
- `vfx_chain_snap`
- `snap_wall_anchor`
- `snap_floor_anchor`

Socket intent:

- `vfx_anchor_ember`: restrained ember pulse at anchor grooves; no VFX authored in this packet.
- `vfx_chain_snap`: optional future break/snap event hook; no break behavior or physics in this packet.
- `snap_wall_anchor`: placement helper for wall and hanging variants.
- `snap_floor_anchor`: placement helper for floor and coil variants.

Recommended DCC locator names for layout review only:

- `hang_top_l`
- `hang_top_r`
- `hang_low_l`
- `hang_low_r`
- `chain_end_a`
- `chain_end_b`

The DCC locators are not gameplay sockets by default. A future import lane may promote them to Unreal sockets only if a placement or composition task needs them.

## LOD Reduction Order

- LOD0: full chain paths, anchor plates, large links, hooks, broken ends, broad bevels, and major relief.
- LOD1: 55-60 percent; reduce link bevels, small dents, secondary hook loops, and minor anchor chips.
- LOD2: 25-35 percent; merge link clusters, flatten minor relief, remove small bone/horn markers, and simplify broken end caps.
- LOD3: 10-15 percent; preserve chain mass, chain path, anchor plate blocks, and major dark metal/stone color blocks only.

Reduce details in this order:

1. Tiny scratches, soot marks, pitting, and small dents through material simplification.
2. Bone/horn witness markers and tiny ember pips.
3. Link bevel loops and secondary hook loops.
4. Minor anchor relief and small bracket chips.
5. Broken-end interior detail.
6. Link cluster count, while preserving the overall chain path.
7. Primary anchor silhouette and chain mass last.

## Collision Rules

- Non-blocking by default for all dressing variants.
- If future placement requires blocking, use simple capsules or boxes around large chain masses and anchor plates only.
- Do not create complex per-link collision.
- Keep collision away from hanging decorative ends to avoid snagging wings, tails, or player capsules.
- Do not imply gameplay restraint collision, breakable links, damage volumes, or interaction traces in the mesh lane.

## Validation Plan

Future build lane must run:

- `python -m py_compile Tools/DCC/build_infernal_witness_chains.py`
- Blender background generation for source, FBX exports, and DCC proof render.
- `python -m py_compile Tools/Unreal/import_infernal_witness_chains.py Tools/Unreal/validate_infernal_witness_chains.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/import_infernal_witness_chains.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_infernal_witness_chains.py`
- `git diff --check`

Focused validator should check:

- Static mesh paths and names for all selected variants.
- Bounds match the selected modular length ranges with first-pass tolerance.
- LOD0-LOD3 presence.
- Material slots stay within 2-3 for most variants and 5 maximum for approved hero assemblies.
- Approved CultStone material instances are assigned.
- Required socket names exist on relevant wall/floor/anchor variants.
- Collision is none or simple only; no complex per-link collision.
- No skeletal mesh, physics asset, constraint setup, breakable behavior, gameplay restraint behavior, gore escalation, startup placement, or final-art claims are introduced.

## Approval Gates And Stop Conditions

Stop and return to lead/user approval before:

- Starting Blender or DCC source creation from this packet.
- Exporting FBX files.
- Importing Unreal Content.
- Creating DCC, Unreal import, or Unreal validator scripts.
- Adding skeletal mesh variants, physics simulation, constraints, chain sway, chain breaking, or runtime interaction.
- Adding gameplay restraint behavior, damage volumes, quest hooks, backend logic, or animation timing.
- Placing any WitnessChains variant in a startup scene or review map.
- Creating final authored textures, final shader polish, or final material identities beyond approved CultStone reuse.
- Increasing gore, chain density, micro-link count, emissive intensity, or Balgoroth symbol complexity beyond the production package.

## Acceptance Checklist

- Packet uses the WitnessChains production package and Balgoroth cult readiness matrix as dependencies.
- `SM_INF_WitnessChains_A01` remains package-ready and implementation-ready, not implemented.
- Future DCC, export, Unreal, validator, texture, physics, and startup paths are named but untouched.
- Modular variants, lengths, pivots, material slots, sockets/hang points, collision, LODs, validators, and approval gates are explicit.
- Chain links stay chunky, sparse, readable, and geometry-efficient.
- The next production step is an approval-gated build promotion task.
