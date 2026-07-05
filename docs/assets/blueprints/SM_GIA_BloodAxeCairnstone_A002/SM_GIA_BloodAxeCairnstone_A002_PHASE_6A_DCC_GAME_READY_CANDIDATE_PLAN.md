# SM_GIA_BloodAxeCairnstone_A002 Phase 6A DCC Game-Ready Candidate Plan

Status: `DCC game-ready candidate plan recorded; FBX LOD collision not generated`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/CONCEPT_ART_TO_GAME_READY_ASSET_PIPELINE.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_4E_SNAP_ASSEMBLY_SOURCE_OUTPUT_RECORD.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_5D_TEXTURE_UV_MATERIAL_CANDIDATE_OUTPUT_RECORD.md`

## Purpose

Define the Phase 6 DCC game-ready candidate plan before generating FBX exports, LODs, collision proxies, handoff manifests, final proof renders, or Unreal output.

This plan does not modify `.blend` files, export FBX, create LODs, create collision proxies, generate Unreal content, merge runtime meshes, or request subjective visual approval.

## Authorized Phase 6 Goal

Create a DCC game-ready candidate package that preserves A002 component lineage and prepares the asset for a later Unreal import candidate step.

The Phase 6 candidate must include:

- DCC source based on the passed Phase 5D texture/UV/material candidate.
- FBX exports.
- LOD0, LOD1, LOD2, and LOD3.
- Simple UCX collision proxy exports.
- Scale, pivot, orientation, and component lineage records.
- Texture/material package records.
- DCC handoff report and validation manifest.
- Final technical DCC proof renders.

The asset status may become `DCC game-ready candidate` only after a future Phase 6 generator and audit prove these outputs exist and pass.

## Approved Inputs

Phase 6 may use these A002 records and outputs:

- Phase 5D candidate `.blend`:
  `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterial_A01/SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterial_A01.blend`
- Phase 5D manifest:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/TextureUVMaterialA01/SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterialA01Manifest.json`
- Phase 5D audit:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/TextureUVMaterialA01/SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterialA01Audit.json`
- Phase 5D ownership manifest:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/TextureUVMaterialA01/SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterialA01OwnershipManifest.json`

Phase 6 must not use A001 or A02 generated meshes, textures, materials, exports, or Unreal assets as source authority.

## Component And Assembly Policy

Approved components remain:

- `primary_monolith`
- `upper_socket_ring`
- `support_base`

Phase 6 must preserve component identity, object names, UV ownership, material ownership, and source lineage.

Runtime mesh merge remains blocked in Phase 6A. The preferred DCC handoff path is:

- preserve separate source components in the DCC source
- export component FBXs and LODs where needed for lineage
- prepare an assembled handoff package that can be imported or assembled in Unreal without destroying source component records

If a later generator cannot create a usable assembled FBX without losing component lineage, it must block and report the conflict instead of merging destructively.

## Scale, Pivot, And Orientation Rules

Scale authority:

- Unreal scale: `1 Unreal unit = 1 cm`
- overall height: `220.0 cm`
- support/base width: `140.0 cm`
- support/base depth: `110.0 cm`
- primary width: `120.0 cm`
- primary depth: `90.0 cm`
- primary height: `185.0 cm`

Pivot and orientation:

- Up axis: `Z`
- Front direction: `-Y`
- Right direction: `+X`
- Support/base transform remains location `[0.0, 0.0, 0.0]`, rotation `[0.0, 0.0, 0.0]`, scale `[1.0, 1.0, 1.0]`
- Upper socket ring transform remains location `[0.0, 0.0, 0.0]`, rotation `[0.0, 0.0, 0.0]`, scale `[1.0, 1.0, 1.0]`
- Primary monolith transform remains location `[6.7158670425, 0.4247104228, 0.0]`, rotation `[0.0, 0.0, 0.0]`, scale `[1.0, 1.0, 1.0]`

No rescale, yaw, pitch, roll, lift, drop, or visual fitting is authorized.

## Planned Output Locations

Planned DCC game-ready source folder:

- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/`

Planned export folder:

- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/`

Planned automation folder:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/`

Planned DCC source file:

- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01.blend`

Planned manifests:

- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Manifest.json`
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Audit.json`
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Handoff.md`

## Planned FBX Package

Required future FBX outputs:

- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01.fbx`
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD0.fbx`
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD1.fbx`
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD2.fbx`
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD3.fbx`
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_UCX.fbx`

The future export must exclude non-shipping helpers, labels, camera objects, lights, and proof-only markers.

## LOD Plan

LOD0 must preserve the measured component silhouette and source-owned UV/material assignment.

Triangle-count audit rules:

- LOD0: report actual count; target at or below the large-prop budget unless source fidelity would be damaged
- LOD1: target `50-60%` of LOD0
- LOD2: target `25-35%` of LOD0
- LOD3: target `10-15%` of LOD0

Reduction order:

1. Proof-only marker/helper geometry.
2. Internal or nonvisible helper detail.
3. Small edge subdivisions that do not change silhouette.
4. Secondary socket/contact interior density.
5. Far-distance contour density.

Primary silhouette, contact seating, component identity, and UV ownership must not be destroyed to hit a triangle target.

If LOD generation changes visible silhouette, component contact, UV ownership, or material ownership beyond audit tolerance, Phase 6 must block.

## Collision Plan

Collision type:

- Simple UCX collision proxies only.
- No complex-as-simple collision.

Planned proxy strategy:

- One support/base proxy for the lower footprint.
- One upper socket ring proxy if needed for player/world blocking.
- One primary monolith proxy for the standing stone mass.

Collision objects must use Unreal UCX naming and must be excluded from render proof meshes:

- `UCX_SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_00`
- `UCX_SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_01`
- `UCX_SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_02`

Collision must preserve the broad cairn obstruction while avoiding tiny socket-detail collision and snag-prone concavity.

## Texture And Material Package Plan

Phase 5D confirmed these material slots:

- `M_A002_SourceTemplate_Closest`
- `M_A002_TaggedInferredHidden_Neutral`

Phase 6 must preserve the `A002_SourceOwnedUV` layer and must keep visible source pixels tied to the approved source template:

- `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`

Material package rules:

- Base Color authority remains the approved source template unless a later exact-copy texture manifest is created.
- Normal and ORM maps are optional for the first DCC game-ready candidate if the handoff explicitly records them as planned-but-not-authored.
- No emissive map is planned.
- Hidden or inferred surfaces must remain tagged separately and must not replace visible measured pixels.
- A001/A02 generated textures, atlases, material instances, or Unreal materials are blocked as source authority.

If Phase 6 creates new BC, N, ORM, or material-package files, the generator must also create an exact ownership manifest and audit. Visible BC regions must be exact-copy or the audit must fail.

## Proof Render Requirements

Future Phase 6 proof renders must include:

- front
- back
- left
- right
- top
- angle
- collision proxy proof
- LOD comparison proof

Proof outputs are technical audit artifacts. Do not open them for subjective visual approval unless the audit exposes a production decision that requires Flamestrike or the asset reaches the concept-art-match visual review gate.

## DCC Handoff Report Requirements

The future handoff report must include:

- asset name
- asset type
- folder paths
- source `.blend` path
- FBX paths
- texture/material paths or planned-map status
- LOD plan and actual LOD triangle counts
- collision plan and proxy names
- pivot
- scale
- orientation
- component lineage
- inferred-area notes
- proof render paths
- validation reports
- current approval status

## Audit Requirements

The future Phase 6 audit must verify:

- Phase 5D audit status is `pass`
- DCC game-ready `.blend` exists
- source components and object names are preserved
- `A002_SourceOwnedUV` exists on all shipping mesh components
- material slots match or are explicitly documented by the material package manifest
- FBX exports exist
- LOD0-LOD3 exports exist
- UCX export exists
- LOD triangle counts are reported
- non-shipping helpers are excluded from exports
- collision proxy names use UCX convention
- scale remains centimeters
- transforms match the Phase 4E snap assembly record unless a later approved rule changes them
- no source image pixels were edited
- no A001/A02 generated output was used as source authority
- no Unreal output exists
- no runtime mesh merge occurred unless separately authorized with lineage proof

## Blocked Methods

Phase 6A does not authorize:

- Blender generation or edits
- FBX export
- Unreal import
- runtime mesh merge
- source-image pixel edits
- A001 or A02 generated texture/material authority
- manual painting over visible measured source pixels
- unrecorded texture-map generation
- complex-as-simple collision
- visual fitting
- rescale, yaw, pitch, roll, lift, or drop to force contacts
- subjective visual approval request for technical proof renders

## Phase 6A Decision

Decision: `plan_complete`

Phase 6A is sufficient to proceed to DCC game-ready generator and audit script creation, but no FBX, LOD, collision, material-package file, Unreal output, or runtime merge has been generated.

## Next Core-Valid Step

Begin A002 Phase 6B: DCC Game-Ready Generator And Audit Script Creation.

The next task is to create the A002-owned DCC game-ready generator and audit scripts from this plan, without running Blender or generating FBX/LOD/collision outputs yet.
