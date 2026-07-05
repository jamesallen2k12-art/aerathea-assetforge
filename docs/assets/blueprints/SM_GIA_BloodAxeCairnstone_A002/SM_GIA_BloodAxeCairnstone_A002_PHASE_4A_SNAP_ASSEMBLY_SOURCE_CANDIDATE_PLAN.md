# SM_GIA_BloodAxeCairnstone_A002 Phase 4A Snap Assembly Source Candidate Plan

Status: `snap assembly plan recorded; assembly not generated`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2C_PRE_GEOMETRY_FORMULA_AUDIT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_3C_MODULAR_DCC_SOURCE_OUTPUT_RECORD.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_3D_VISUAL_REVIEW_DECISION.md`

## Purpose

Define the exact Phase 4 snap assembly plan before running Blender or generating an assembled proof.

This plan does not generate assembly geometry, UVs, textures, FBX, Unreal output, or final runtime meshes.

## Authorized Phase 4 Goal

Create a snap assembly source candidate that proves the three approved A002 components reconnect by source-derived anchors and measured contacts.

Approved components:

- `primary_monolith`
- `upper_socket_ring`
- `support_base`

Planned assembly asset:

- `SM_GIA_BloodAxeCairnstone_A002_Assembled_Proof`

Planned assembly status:

- `A002 modular assembly source candidate`

## Required Pre-Assembly Gate

Assembly generation is blocked until A002 records a Phase 4B snap-anchor manifest.

The manifest must bind all assembly anchors to A002 formula authority, not to visual fitting.

Required component pairs:

- `primary_monolith` to `upper_socket_ring`
- `upper_socket_ring` to `support_base`

Required anchor families:

- center anchor for each component using the approved component center type
- front/back/left/right contact anchors for `primary_monolith` bottom to `upper_socket_ring` top
- front/back/left/right contact anchors for `upper_socket_ring` bottom to `support_base` top
- contact perimeter IDs for each participating interface
- orientation anchors confirming zero yaw, pitch, and roll
- source-owner labels for every anchor

## Approved Contact Stations

Primary-to-ring top contacts:

| Direction | Contact station |
| --- | ---: |
| front | `43.7811 cm` |
| back | `50.3268 cm` |
| left | `35.5280 cm` |
| right | `37.5610 cm` |

Ring-to-support bottom contacts:

| Direction | Contact station |
| --- | ---: |
| front | `22.9851 cm` |
| back | `27.3203 cm` |
| left | `19.1304 cm` |
| right | `20.1220 cm` |

These values must remain per-view. Cross-view averaging is blocked.

## Alignment Rules

Component origins:

- `primary_monolith`: component-local origin at its approved center authority
- `upper_socket_ring`: component-local origin at its approved center authority
- `support_base`: component-local origin at its approved center authority

Assembly transform policy:

- translation tolerance: `0`
- yaw tolerance: `0`
- pitch tolerance: `0`
- roll tolerance: `0`

Any disagreement between paired anchors must stop the assembly step before moving, rotating, stretching, or deforming geometry.

## Planned Output Locations

Planned DCC source folder:

- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_SnapAssemblySource_A01/`

Planned automation folder:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/SnapAssemblySourceA01/`

Planned source file:

- `SM_GIA_BloodAxeCairnstone_A002_Assembled_Proof.blend`

Planned manifests:

- `SM_GIA_BloodAxeCairnstone_A002_SnapAssemblySourceA01AnchorManifest.json`
- `SM_GIA_BloodAxeCairnstone_A002_SnapAssemblySourceA01Manifest.json`
- `SM_GIA_BloodAxeCairnstone_A002_SnapAssemblySourceA01Audit.json`

Planned proof board:

- `SM_GIA_BloodAxeCairnstone_A002_SnapAssemblySourceA01_ProofBoard.png`

## Proof Render Requirements

Assembly proof renders must show:

- front
- back
- left
- right
- top
- angle

Proof renders must include:

- separate component colors
- component identity labels
- socket/contact labels
- snap-anchor markers
- contact station markers

Proof renders must not include:

- source-matched textures
- UVs
- texture nodes
- FBX export
- Unreal output
- final runtime merge

These proof renders are technical audit outputs. They should not be treated as Flamestrike subjective visual approval gates unless the assembly reaches the concept-art-match stage or exposes a decision that cannot be resolved from approved authority.

## Audit Requirements

The Phase 4 audit must verify:

- all three source component `.blend` files are present
- the assembly imports or links only the three approved A002 component sources
- component identity metadata is preserved
- all required snap-anchor IDs exist
- required anchor pairs exist
- zero translation, yaw, pitch, and roll policy is respected or a stop-line mismatch is reported
- contact station values match the A002 formula records
- no manual visual fitting occurred
- no component was stretched, deformed, or rescaled to force a fit
- no UV layers exist
- no texture nodes exist
- no FBX export exists
- no Unreal output exists
- no final runtime merge occurred

## Blocked Methods

Phase 4 may not use:

- A001 generated output as source authority
- A02 generated output as source authority
- manual visual fitting
- copied or inherited contact loops
- cross-view averaged contact positions
- old `35 cm` support-height flattening
- hidden lifts or drops
- stretch strips
- cover planes
- runtime mesh merge
- UV or texture generation
- FBX or Unreal output

## Phase 4A Decision

Decision: `plan_complete`

Phase 4A is sufficient to proceed to a snap-anchor manifest, but no assembly source candidate has been generated.

## Next Core-Valid Step

Begin A002 Phase 4B: Snap Anchor Manifest.

The next task is to create the A002 snap-anchor manifest from approved formula records and component metadata before any assembly generation occurs.
