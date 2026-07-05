# SM_GIA_BloodAxeCairnstone_A002 Phase 3B Generator And Audit Script Record

Status: `A002 generator and audit scripts created; Blender not run`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_1_SOURCE_EVIDENCE_LOCK.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2C_PRE_GEOMETRY_FORMULA_AUDIT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_3A_MODULAR_DCC_SOURCE_CANDIDATE_PLAN.md`

## Purpose

Create the A002-owned generator and audit scripts required by Phase 3A before running Blender.

This record does not generate geometry, renders, exports, Unreal output, UVs, texture nodes, or final assembly. It only records the scripts that will be used in the next controlled production step.

## Created Scripts

Generator:

- `Tools/DCC/build_bloodaxe_cairnstone_a002_modular_dcc_source_a01.py`

Audit:

- `Tools/DCC/audit_bloodaxe_cairnstone_a002_modular_dcc_source_a01.py`

## Generator Scope

The generator is limited to these planned DCC source candidates:

- `SM_GIA_BloodAxeCairnstone_A002_PrimaryMonolith.blend`
- `SM_GIA_BloodAxeCairnstone_A002_UpperSocketRing.blend`
- `SM_GIA_BloodAxeCairnstone_A002_SupportBase.blend`

Planned output roots remain:

- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_ModularDCCSource_A01/`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/ModularDCCSourceA01/`

## Encoded Formula Authority

The generator encodes these A002 source-owned values:

| Measurement | Value |
| --- | ---: |
| Overall height | `220.0 cm` |
| Primary footprint | `120.0 cm x 90.0 cm` |
| Support footprint | `140.0 cm x 110.0 cm` |
| Primary center | `[541, 1222]` |
| Upper socket ring center | `[528, 1223]` |
| Support base center | `[528, 1223]` |

Layered contacts remain per-view and non-averaged:

| View | Primary to ring top | Ring to support bottom |
| --- | ---: | ---: |
| front | `43.7811 cm` | `22.9851 cm` |
| back | `50.3268 cm` | `27.3203 cm` |
| left | `35.5280 cm` | `19.1304 cm` |
| right | `37.5610 cm` | `20.1220 cm` |

The generator maps continuous oval segments to the nearest cardinal source sector so that each mesh station uses an exact source-owned per-view contact value. It does not average front/back/left/right contacts.

## Component Separation Controls

- `primary_monolith`, `upper_socket_ring`, and `support_base` are generated as separate `.blend` files.
- Each component uses a component-local origin.
- Each component stores its A002 source center and authority metadata.
- Contact markers are generated as review markers, not final decorative geometry.
- The upper socket ring remains an independent interval shell.
- Hidden receiver surfaces remain open or marker-only until separately authorized.

## Blocked Outputs

The generator and audit scripts are not authorized to create:

- A001 or A02-derived generated source
- UV layers
- texture nodes
- texture maps
- FBX exports
- Unreal content
- merged final assembly
- source-image pixel edits
- visual-fit geometry
- cross-view averaged measurements
- single-zone void fills

## Audit Scope

The audit script is designed to check the generated Phase 3 source candidate after Blender is run.

It will verify:

- all three component `.blend` files exist
- component identities are preserved
- component-local pivots are preserved
- A002 source center metadata is present
- no UV layers exist
- no texture nodes exist
- no external image data blocks exist
- no blocked FBX or Unreal output exists
- proof renders exist for each component and required view

## Phase 3B Decision

Decision: `scripts_created`

Phase 3B is complete as a script-preparation step. Blender has not been run, no DCC source candidate has been generated, and no visual review output exists yet.

## Next Core-Valid Step

Begin A002 Phase 3C: Run the A002 Modular DCC Source Candidate Generator.

The next task is to create a manual checkpoint, run the A002 generator in Blender background, run the A002 audit, and then present the component proof renders for review if the audit passes.
