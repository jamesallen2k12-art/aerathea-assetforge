# SM_INF_AshBasin_A01 Implementation Packet

## Task Scope

- Task: `AET-MA-20260629-042`
- Build scope: docs-only implementation packet.
- Result target: prepare `SM_INF_AshBasin_A01` for a future DCC and Unreal build lane using the existing production package plus validated CultStone and BalgorothSigil dependencies.
- Not included: Blender source creation, FBX export, Unreal import, ember or smoke VFX authoring, Blueprint behavior, runtime state binding, startup scene placement, final visual approval, final authored textures, or final shader polish.

This packet converts the production package into an implementation-ready task contract. It does not approve or start asset construction.

## Dependency Evidence

| Dependency | Evidence | Status |
| --- | --- | --- |
| `SM_INF_AshBasin_A01` package | `docs/assets/props/SM_INF_AshBasin_A01/PRODUCTION_PACKAGE.md` | Production package ready. |
| `MI_INF_CultStone_Set_A01` | `docs/assets/materials/MI_INF_CultStone_Set_A01/BUILD_IMPORT_STATUS.md` | First-pass Unreal material set implemented and focused validation passed. Final textures and final shader polish remain open. |
| `SM_INF_BalgorothSigil_A01` | `docs/assets/props/SM_INF_BalgorothSigil_A01/BUILD_IMPORT_STATUS.md` | First-pass DCC source/export/proof and Unreal static mesh import validated. Final sculpt, UVs, textures, tuned collision, and startup placement remain open. |
| `KIT_INF_BalgorothCult_A01` readiness | `docs/assets/kits/KIT_INF_BalgorothCult_A01/IMPLEMENTATION_READINESS_MATRIX.md` | AshBasin is recommended after BrandingStone as a low-risk prop using shared CultStone and restrained ash/ember socket conventions. |

## Selected Variants

The future build lane should treat `A01` as a static mesh variant set:

| Variant | Target Unreal mesh | Target scale | Primary placement |
| --- | --- | --- | --- |
| Small floor basin | `SM_INF_AshBasin_Small_A01` | 65w x 42h x 65d cm | Den corners, Lesser staging, altar side dressing |
| Large altar-side basin | `SM_INF_AshBasin_Large_A01` | 130w x 75h x 130d cm | Worthiness altar sides, branding-stone staging, main ritual rooms |
| Wall-adjacent half-basin | `SM_INF_AshBasin_Wall_A01` | 100w x 55h x 55d cm, within the 80-120 cm package range | Walls, alcoves, tight trial-room edges |

Readability target: heavy ash-and-ember vessel with claw-cut rim, horned rim points, small Balgoroth sigil inset, blackened iron feet, ash fill, and restrained ember channels. It must not read as a generic brazier, campfire, portal, forge, gore bowl, or constant flame prop.

## DCC Build Contract

Future DCC lane may create:

- `Tools/DCC/build_infernal_ash_basin.py`
- `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_AshBasin_A01/SM_INF_AshBasin_A01.blend`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_AshBasin_A01/SM_INF_AshBasin_Small_A01.fbx`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_AshBasin_A01/SM_INF_AshBasin_Large_A01.fbx`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_AshBasin_A01/SM_INF_AshBasin_Wall_A01.fbx`
- `Saved/Automation/InfernalAshBasinReview/SM_INF_AshBasin_A01_DCCReview.png`

Required DCC features:

- Center-bottom pivot at each basin footprint.
- Centimeter scale, 1 Unreal unit = 1 cm.
- Shared proportion language across all variants so the small, large, and wall basins read as one family.
- Real geometry for basin body, wide claw-cut rim, horned rim points, thick feet, large stone chips, ash-fill surface, and broad Balgoroth sigil inset.
- Texture or material detail for soot, fine ash smears, tiny cracks, heat stress, subtle scratches, and small chips.
- Ash fill as a simple interior mesh or material surface, not loose particle fields or many small stones.
- No modeled flames, dense smoke, tiny dangling chains, needle spikes, gore pieces, readable text, or screen-filling glow forms.

## Unreal Import Contract

Future Unreal lane may create:

- `Tools/Unreal/import_infernal_ash_basin.py`
- `Tools/Unreal/validate_infernal_ash_basin.py`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/AshBasin/SM_INF_AshBasin_Small_A01`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/AshBasin/SM_INF_AshBasin_Large_A01`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/AshBasin/SM_INF_AshBasin_Wall_A01`

Import requirements:

- Asset type: Static Mesh set.
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/AshBasin/`
- Pivot: center bottom of each footprint.
- Scale: centimeters.
- Collision: simple convex hull, rounded hull, or low box set around the basin body only.
- Default collision policy: non-blocking dressing unless a later placement task explicitly needs an obstacle variant.
- LODs: LOD0-LOD3 required for every imported mesh variant.
- Startup scene: out of scope unless a later placement task explicitly assigns it.

## Material Slot Plan

Preferred material lanes:

1. `MI_INF_CultStone_Basalt_A01`
2. `MI_INF_CultStone_ScorchedRed_A01`
3. `MI_INF_CultStone_BlackIron_A01`
4. Future ash-fill lane, either a tuned CultStone instance or `MI_INF_AshBasin_A01_AshFill` if the build task owns material authoring.
5. `MI_INF_CultStone_EmissiveChannel_A01` or future `MI_INF_AshBasin_A01_Emissive` if the build task owns the custom instance.

Rules:

- Small and wall variants should target 3-4 material slots.
- Large hero placement may use 5 slots only if the ash fill and emissive channel need separate tuning.
- Do not create a duplicate stone material identity; start from the validated CultStone material set.
- Final authored textures remain future work:
  - `T_INF_AshBasin_A01_BC`
  - `T_INF_AshBasin_A01_N`
  - `T_INF_AshBasin_A01_ORM`
  - `T_INF_AshBasin_A01_E`

## Socket Contract

Required sockets for every variant unless the future build lane documents a variant-specific omission:

- `vfx_ash_lift`
- `vfx_ember_core`
- `vfx_rejected_puff`
- `snap_floor_center`

Socket intent:

- `vfx_ash_lift`: sparse upward ash or smoke hook above the ash surface; no VFX authored in this packet.
- `vfx_ember_core`: low ember response inside the basin, centered below the ash-fill surface.
- `vfx_rejected_puff`: brief rejection-state ash kick near the rim; not a constant aura.
- `snap_floor_center`: placement helper at the center-bottom pivot.

The sockets are implementation hooks only. They do not imply active Niagara systems, dynamic lights, gameplay collision, or runtime state binding.

## LOD And Collision Rules

- LOD0: full basin silhouette, horned rim points, claw grooves, feet, sigil inset, ash surface, and broad chips.
- LOD1: 55-60 percent; reduce rim bevel loops, small chips, foot bevels, and secondary ash-surface loops.
- LOD2: 25-35 percent; flatten minor grooves and ash surface detail while preserving basin mass, rim silhouette, and sigil read.
- LOD3: 10-15 percent; preserve primary basin mass, rim block, foot block, and one restrained ember color block.
- Collision must not include decorative horn points, ash surface ripples, or VFX sockets.
- Blocking variants, if ever approved, should keep collision below the rim and clear of wing, tail, and player capsule paths.

## Validation Plan

Future build lane must run:

- `python -m py_compile Tools/DCC/build_infernal_ash_basin.py`
- Blender background generation for source, FBX exports, and DCC proof render.
- `python -m py_compile Tools/Unreal/import_infernal_ash_basin.py Tools/Unreal/validate_infernal_ash_basin.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/import_infernal_ash_basin.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_infernal_ash_basin.py`
- `git diff --check`

Focused validator should check:

- Static mesh paths and names for all selected variants.
- Bounds near the selected target sizes, with first-pass silhouette tolerance.
- LOD0-LOD3 presence.
- Material slots stay within 3-4 for normal variants and 5 maximum for approved hero use.
- Approved CultStone material instances are assigned; custom ash/emissive instances are only accepted if authored by the build lane.
- Required socket names exist and are placed near ash/core/rejection/placement locations.
- Collision is none, simple, or convex only; no per-detail collision.
- No Niagara, Blueprint behavior, runtime interaction, dynamic lights, startup placement, or final-art claims are introduced.

## Approval Gates And Stop Conditions

Stop and return to lead/user approval before:

- Starting Blender or DCC source creation from this packet.
- Exporting FBX files.
- Importing Unreal Content.
- Creating DCC, Unreal import, or Unreal validator scripts.
- Authoring ember, ash, smoke, flame, rejection, or regeneration VFX.
- Adding Blueprint behavior, runtime state binding, gameplay collision, quest hooks, or backend logic.
- Placing any basin variant in a startup scene or review map.
- Creating final authored textures, final shader polish, or final material identities beyond approved CultStone reuse.
- Changing the Balgoroth symbol language or increasing gore, flame density, smoke density, or emissive intensity.

## Acceptance Checklist

- Packet uses the AshBasin production package and validated CultStone/BalgorothSigil outputs as dependencies.
- `SM_INF_AshBasin_A01` remains package-ready and implementation-ready, not implemented.
- Future DCC, export, Unreal, validator, texture, and startup paths are named but untouched.
- Selected variants, scale, pivot, material slots, sockets, collision, LODs, validators, and approval gates are explicit.
- Ash/ember treatment remains restrained and socket-driven.
- The next production step is an approval-gated build promotion task.
