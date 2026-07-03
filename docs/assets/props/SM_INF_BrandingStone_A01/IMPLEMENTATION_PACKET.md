# SM_INF_BrandingStone_A01 Implementation Packet

## Task Scope

- Task: `AET-MA-20260628-030`
- Build scope: docs-only implementation packet.
- Result target: prepare `SM_INF_BrandingStone_A01` for a future DCC and Unreal build lane using validated CultStone material and BalgorothSigil outputs.
- Not included: Blender source creation, FBX export, Unreal import, runtime interaction behavior, startup scene placement, final shader polish, final authored textures, final VFX graph art, or gameplay regeneration tuning.

This packet promotes the production package into an implementation-ready task contract. It does not approve or start asset construction.

## Dependency Evidence

| Dependency | Evidence | Status |
| --- | --- | --- |
| `MI_INF_CultStone_Set_A01` | `docs/assets/materials/MI_INF_CultStone_Set_A01/BUILD_IMPORT_STATUS.md` | First-pass Unreal material set implemented and focused validation passed. Final textures and final shader polish remain open. |
| `SM_INF_BalgorothSigil_A01` | `docs/assets/props/SM_INF_BalgorothSigil_A01/BUILD_IMPORT_STATUS.md` | First-pass Blender source, FBX export, Unreal static mesh import, material assignment, LODs, and sockets validated. Final sculpt, UVs, textures, and tuned collision remain open. |
| `SM_INF_BrandingStone_A01` package | `docs/assets/props/SM_INF_BrandingStone_A01/PRODUCTION_PACKAGE.md` | Production package ready. |
| `VFX_INF_RegenerationBrand_A01` | `docs/assets/vfx/VFX_INF_RegenerationBrand_A01/PRODUCTION_PACKAGE.md` | Future VFX consumer only. Do not author Niagara work in the BrandingStone build lane. |

## Selected Variant

- Variant: `A01` upright angled basalt branding monolith.
- Review size: 190 cm high x 95 cm wide x 75 cm deep.
- Primary read: horned crown cap, split-wing silhouette, large Balgoroth sigil inset, wide hand/forearm presentation groove, claw-score channels, restrained brand-core glow.
- Gameplay role: static ritual prop and future socket/mask anchor for body-brand, regeneration, and worthiness staging.
- Safety/readability rule: read as a severe ritual stone, not a torture machine, gore prop, portal, forge, or generic tombstone.

## DCC Build Contract

Future DCC lane may create:

- `Tools/DCC/build_infernal_branding_stone.py`
- `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_BrandingStone_A01/SM_INF_BrandingStone_A01.blend`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_BrandingStone_A01/SM_INF_BrandingStone_A01.fbx`
- `Saved/Automation/InfernalBrandingStoneReview/SM_INF_BrandingStone_A01_DCCReview.png`

Required DCC features:

- Center-bottom pivot at base footprint.
- Centimeter scale, 1 Unreal unit = 1 cm.
- LOD0 blockout silhouette near 190h x 95w x 75d cm.
- Large monolith mass, horned crown cap, split-wing cap silhouette, sigil inset, presentation groove, broad claw channels, base stones, and black-iron brace as real geometry.
- Fine cracks, ash wear, small scratches, tiny chips, and heat stress reserved for maps or material parameters.
- Chunky readable forms only; no dense rivets, tiny rune clusters, broken micro-chains, mechanical needles, torture blades, or gore.

## Unreal Import Contract

Future Unreal lane may create:

- `Tools/Unreal/import_infernal_branding_stone.py`
- `Tools/Unreal/validate_infernal_branding_stone.py`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/BrandingStone/SM_INF_BrandingStone_A01`

Import requirements:

- Asset type: Static Mesh.
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/BrandingStone/`
- Static mesh name: `SM_INF_BrandingStone_A01`
- Pivot: center bottom of base footprint.
- Scale: centimeters.
- Collision: simple authored collision or generated convex collision, preferably 2-3 hulls covering body and base without trapping player capsules, wings, or tails.
- LODs: LOD0-LOD3 required.
- Startup scene: out of scope unless a later placement task explicitly assigns it.

## Material Slot Plan

Target 4-5 material lanes:

1. `MI_INF_CultStone_Basalt_A01`
2. `MI_INF_CultStone_ScorchedRed_A01`
3. `MI_INF_CultStone_ObsidianInset_A01` or sigil-specific obsidian instance if later approved
4. `MI_INF_CultStone_BlackIron_A01`
5. `MI_INF_CultStone_EmissiveChannel_A01` or future `MI_INF_BrandingStone_A01_Emissive`

Do not create a duplicate stone material identity. Final authored textures remain future work:

- `T_INF_BrandingStone_A01_BC`
- `T_INF_BrandingStone_A01_N`
- `T_INF_BrandingStone_A01_ORM`
- `T_INF_BrandingStone_A01_E`

## Socket Contract

Required sockets:

- `vfx_brand_core`
- `vfx_brand_transfer`
- `vfx_rejected_snap`
- `interact_brand_side`
- `snap_floor_center`

Socket intent:

- `vfx_brand_core`: localized ember/sigil response in the brand groove.
- `vfx_brand_transfer`: future `VFX_INF_RegenerationBrand_A01` transfer origin.
- `vfx_rejected_snap`: brief violet-red rejection event, not constant aura.
- `interact_brand_side`: future interaction trace side; no runtime behavior in the mesh lane.
- `snap_floor_center`: placement helper only.

## Validation Plan

Future build lane must run:

- `python -m py_compile Tools/DCC/build_infernal_branding_stone.py`
- Blender background generation for the DCC source/export/proof render.
- `python -m py_compile Tools/Unreal/import_infernal_branding_stone.py Tools/Unreal/validate_infernal_branding_stone.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/import_infernal_branding_stone.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_infernal_branding_stone.py`
- `git diff --check`

Focused validator should check:

- Static mesh path and name.
- Bounds close to 190h x 95w x 75d cm, allowing first-pass silhouette tolerance.
- LOD0-LOD3 presence.
- 4-5 material slots using approved CultStone lanes.
- Required socket names.
- Collision exists and stays simple.
- Startup scene is unchanged unless a placement task explicitly owns it.

## Stop Conditions

Stop and return to lead/user approval before:

- Starting DCC source creation from this packet.
- Exporting FBX.
- Importing Unreal Content.
- Creating `Tools/DCC/build_infernal_branding_stone.py` or Unreal import/validator scripts.
- Adding runtime interaction, regeneration values, damage/healing behavior, backend authority, or quest state.
- Creating final BrandGlow shader/textures or `VFX_INF_RegenerationBrand_A01` Niagara systems.
- Placing the asset into the startup scene or review map.
- Changing the Balgoroth symbol language beyond the validated sigil direction.

## Acceptance Checklist

- Packet uses validated CultStone and BalgorothSigil outputs as dependencies.
- BrandingStone remains package-ready and implementation-ready, not implemented.
- DCC, export, Unreal, runtime, VFX, and startup paths are named but untouched.
- Scale, pivot, material slots, sockets, collision, LODs, validators, and stop conditions are explicit.
- The next production step is an approval-gated build promotion task.
