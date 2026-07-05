# SM_GIA_BloodAxeCairnstone_A002 Reset Resume State

Status: `safe to resume at Phase 5D`

Date: 2026-07-05

## Resume Instruction

On reset/resume, read this file first, then read the listed authority records before taking production action.

Do not rely on conversation memory.

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`

## Current A002 State

A002 is a clean restart after A001 drift quarantine.

Current completed stage:

- Phase 5C: texture/UV/material generator and audit script creation

Current status:

- Phase 5B ownership manifest is complete and valid JSON.
- Phase 5C generator/audit scripts are created and pass Python syntax validation.
- No Phase 5D Blender run has happened yet.
- No UV candidate `.blend` has been generated yet.
- No source-matched textures have been generated yet.
- No FBX export has been created.
- No Unreal import has been created.
- Flamestrike subjective visual review remains reserved for the later concept-art-match assembled asset stage.

## Latest Recovery Checkpoint

Manual checkpoint after Phase 5C validation:

- `Saved/ProjectRecovery/20260705-183056`

Checkpoint note:

- `A002 after Phase 5C script creation and validation`

## Required Read Before Continuing

Read in this order:

1. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
2. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_4E_SNAP_ASSEMBLY_SOURCE_OUTPUT_RECORD.md`
3. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_5A_TEXTURE_UV_MATERIAL_CANDIDATE_PLAN.md`
4. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_5B_UV_TEXTURE_OWNERSHIP_MANIFEST.md`
5. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_5C_GENERATOR_AND_AUDIT_SCRIPT_RECORD.md`

## Phase 5B Ownership Manifest

Ownership manifest:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/TextureUVMaterialA01/SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterialA01OwnershipManifest.json`

Status:

- `ownership_manifest_recorded_uv_texture_generation_not_authorized`

Important policy:

- visible source pixels must copy exactly from approved source regions
- inferred/contact/hidden areas must be tagged separately
- no A001/A02 generated texture or material authority
- no FBX export
- no Unreal output

## Phase 5C Scripts

Generator:

- `Tools/DCC/build_bloodaxe_cairnstone_a002_texture_uv_material_a01.py`

Audit:

- `Tools/DCC/audit_bloodaxe_cairnstone_a002_texture_uv_material_a01.py`

Validation already completed:

- `python3 -m py_compile Tools/DCC/build_bloodaxe_cairnstone_a002_texture_uv_material_a01.py Tools/DCC/audit_bloodaxe_cairnstone_a002_texture_uv_material_a01.py`
- `python3 -m json.tool Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/TextureUVMaterialA01/SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterialA01OwnershipManifest.json`
- `git diff --check` for Phase 5C/5B scoped files

## Next Core-Valid Step

Begin A002 Phase 5D: Run Texture UV Material Candidate Generator.

Required sequence:

1. Create a manual checkpoint.
2. Run:
   `blender --background --python Tools/DCC/build_bloodaxe_cairnstone_a002_texture_uv_material_a01.py`
3. Run:
   `blender --background --python Tools/DCC/audit_bloodaxe_cairnstone_a002_texture_uv_material_a01.py`
4. If audit passes, record Phase 5D output.
5. Do not open proof renders for Flamestrike unless a real decision is needed or the asset reaches concept-art-match subjective review stage.

## Hard Boundaries

Do not do any of the following before Phase 5D audit passes:

- FBX export
- Unreal import
- runtime mesh merge
- source-image pixel edits
- A001/A02 generated texture or material reuse as source authority
- manual painting over visible measured source pixels
- subjective visual approval request for technical proof renders

If the Phase 5D audit fails, stop, record the mismatch, identify the violated authority, and propose the smallest correction.
