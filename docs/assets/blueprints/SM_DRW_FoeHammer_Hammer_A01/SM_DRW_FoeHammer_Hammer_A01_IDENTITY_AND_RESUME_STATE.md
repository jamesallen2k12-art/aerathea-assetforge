# SM_DRW_FoeHammer_Hammer_A01 Identity And Resume State

- Date established: `2026-07-24`
- Asset name: `Foe Hammer`
- Asset ID: `SM_DRW_FoeHammer_Hammer_A01`
- Asset type: `Dwarven great hammer weapon/prop`
- Identity record status: `authoritative`
- Geometry status: `DCC source candidate`
- DCC game-ready status: `false`
- Fully game-ready status: `false`
- Step 13 authority: `false`
- Unreal authority: `false`

## Establishing Decision

Flamestrike selected Candidate B, the
`metal_center_piece_side` Step 12 source candidate, as **Foe Hammer** and
required a new Foe Hammer record.

Foe Hammer and Siege Breaker have an identical shared asset identity except
for their doubled head-side treatment:

- `SM_DRW_SiegeBreaker_Hammer_A01` is double rune sided.
- `SM_DRW_FoeHammer_Hammer_A01` is double metal-center-piece sided.

No additional identity, lore, faction, culture, scale-family, gameplay-class,
world-role, material-language, or performance distinction is approved by this
record.

The governing approval record is:

`docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/STEP_12_DUAL_ASSET_SELECTION_APPROVAL_RECORD.md`

## Selected Source Lineage

- Source run:
  `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Source candidate key: `metal_center_piece_side`
- Source artifact status: `DCC source candidate`
- Current Blender source:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_Step12_SourceGeometry_A01/run_a/metal_center_piece_side/SM_DRW_SiegeBreaker_Hammer_A01_metal_center_piece_side_DCCSourceCandidate.blend`
- Blender SHA-256:
  `d98fe28d1409954069fbe77cca2fe7ae1b49c1d63bbff00096ff1986af2ef8de`
- Canonical geometry:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_Step12_SourceGeometry_A01/run_a/metal_center_piece_side/canonical_geometry.json.gz`
- Canonical geometry SHA-256:
  `47422ab9775847e0f66cc1db6ae587eadec46bca7dc54027f69c7fe4a3a98175`
- Build manifest SHA-256:
  `9a5fe4b034bd1b5af512e6cd8a404a3cf30970c88b2809f39a9d4e961d6fd982`
- Independent saved-file audit SHA-256:
  `f29de64688e7be8af42d320a6c2c77c5858f59c5fed64cb92f4dccc1496dbd50`
- Independent saved-file audit: `105/105 PASS`
- Exact dimensions, width × depth × height:
  `50719500/517681 × 11815/274 × 170/1 cm`
- Decimal dimensions:
  `97.974428267601 × 43.120437956204 × 170 cm`
- Observed triangles, not gated at this high-poly stage: `2,316,748`

The source still carries the Siege Breaker path and internal asset identity.
That is valid lineage evidence, not a standalone Foe Hammer production file.
No source copy, rename, internal data-block rename, relink, or resave has been
authorized or performed.

## Shared Identity Authority

The approved Siege Breaker identity is inherited as the shared identity
baseline. The only Foe Hammer-specific visual identity decision is the
double metal-center-piece head treatment.

The selected Foe Hammer source was completed from the approved
`metal_center_piece_side` half by the same governed Step 12 construction
family used for the Siege Breaker twin. The opposite head side therefore
repeats the metal-center-piece treatment rather than the rune-side treatment.

This record does not promote the DCC candidate itself to visual canon and does
not alter `docs/assets/VISUAL_CANON_REGISTRY.md`.

## Evidence Constraint

Shared identity is authoritative; exact mesh parity is not yet proven.

The selected Foe Hammer candidate is
`43.120437956204 cm` deep. The selected Siege Breaker candidate is
`34.434306569343 cm` deep. Their observed topology counts also differ.

These measurements must remain visible. They may not be normalized, averaged,
or described as exact geometric equality without a separately approved rule
and audit. A later decision must establish whether the difference is accepted
as part of the head-side treatment or must be reconciled before advancement.

## Current Artifact Vocabulary

- Foe Hammer identity and Candidate B assignment: `authoritative`.
- Candidate B Blender source: `DCC source candidate`.
- Candidate B validation and review renders: `proof only`.
- Standalone Foe Hammer Blender source: `does not exist`.
- Foe Hammer UVs, textures, materials, LODs, collision, and exports:
  `do not exist under the Foe Hammer identity`.
- Unreal asset: `does not exist`.
- DCC game-ready candidate: `false`.
- Fully game-ready: `false`.

## Resume Instruction

On resume, verify:

1. this record;
2. the governing dual-asset selection approval record;
3. the hash-locked Candidate B source and canonical geometry;
4. the latest recovery journal/checkpoint; and
5. git status.

Report that Foe Hammer is a selected `DCC source candidate`, shares Siege
Breaker's identity except for the double metal-center-piece treatment, still
uses the pre-fork Siege Breaker source path, and cannot advance without a new
contract.

## Next Approval Gate

No production action is currently active.

A separate visible contract must decide whether to preserve Candidate B
exactly in a hash-verified Foe Hammer identity fork or first perform an
evidence-only geometric-parity reconciliation. Step 13, source modification,
asset copying/renaming, export, and Unreal remain locked.
