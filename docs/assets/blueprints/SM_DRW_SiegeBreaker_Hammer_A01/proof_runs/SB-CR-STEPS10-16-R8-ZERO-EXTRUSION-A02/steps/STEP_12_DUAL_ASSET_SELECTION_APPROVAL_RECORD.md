# Step 12 Dual-Asset Selection Approval Record

- Date: `2026-07-24`
- Approving authority: `Flamestrike`
- Source asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Source run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Decision status:
  `authoritative for twin identity; geometry assignment superseded by Core recovery`
- Geometry status:
  `no valid DCC source candidate; former Step 12 geometry invalid / quarantined in place`
- Step 13 authority: `false`
- Unreal authority: `false`

## Approved Decision

Flamestrike selected both Step 12 candidates as two separate assets:

1. Candidate A, `rune_side`, is selected for
   `SM_DRW_SiegeBreaker_Hammer_A01` / **Siege Breaker**.
2. Candidate B, `metal_center_piece_side`, is selected for the new asset
   `SM_DRW_FoeHammer_Hammer_A01` / **Foe Hammer**.

The two assets have one shared identity. No separate faction, culture,
material language, scale family, gameplay class, or world-role identity is
introduced by this decision.

The only approved identity distinction is the completed head-side treatment:

- Siege Breaker is **double rune sided**.
- Foe Hammer is **double metal-center-piece sided**.

This selection supersedes only the earlier `candidate_selected: false` review
state. It does not rewrite the historical validation, review board, source
measurements, or saved candidate files.

## Hash-Locked Candidate Assignment

### Siege Breaker — Candidate A

- Candidate key: `rune_side`
- Artifact status: `DCC source candidate`
- Blender source:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_Step12_SourceGeometry_A01/run_a/rune_side/SM_DRW_SiegeBreaker_Hammer_A01_rune_side_DCCSourceCandidate.blend`
- Blender SHA-256:
  `014048ff149a98e35c5537084bee827480411929474b08b6668361d442797b4f`
- Canonical geometry SHA-256:
  `3209bcfe5893194f3f04060000a7dcfc3ba50d4cffbcc336dd8ec383d8f3980b`
- Exact dimensions, width × depth × height:
  `50719500/517681 × 9435/274 × 170/1 cm`
- Decimal dimensions:
  `97.974428267601 × 34.434306569343 × 170 cm`
- Observed triangles, not gated at this high-poly stage: `2,202,434`
- Independent saved-file audit: `105/105 PASS`

### Foe Hammer — Candidate B

- Candidate key: `metal_center_piece_side`
- Artifact status: `DCC source candidate assigned to a new asset identity`
- Current Blender source:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_Step12_SourceGeometry_A01/run_a/metal_center_piece_side/SM_DRW_SiegeBreaker_Hammer_A01_metal_center_piece_side_DCCSourceCandidate.blend`
- Blender SHA-256:
  `d98fe28d1409954069fbe77cca2fe7ae1b49c1d63bbff00096ff1986af2ef8de`
- Canonical geometry SHA-256:
  `47422ab9775847e0f66cc1db6ae587eadec46bca7dc54027f69c7fe4a3a98175`
- Exact dimensions, width × depth × height:
  `50719500/517681 × 11815/274 × 170/1 cm`
- Decimal dimensions:
  `97.974428267601 × 43.120437956204 × 170 cm`
- Observed triangles, not gated at this high-poly stage: `2,316,748`
- Independent saved-file audit: `105/105 PASS`

Candidate B's current path and internal source identity still use the Siege
Breaker name because the file was created before the dual-asset decision.
This record assigns its approved lineage to Foe Hammer; it does not authorize
copying, renaming, relinking, resaving, or otherwise modifying that source.

## Shared Identity Versus Geometry Evidence

The shared twin-asset identity and the two doubled side treatments are
authoritative.

The current saved candidates do not prove mathematical mesh identity outside
that declared treatment. Their width and height match, but their audited
depths and observed topology counts differ. Those differences remain explicit
evidence and must not be silently normalized or described as exact mesh
parity.

A future gate must decide whether the depth difference is accepted as part of
the approved head-side treatment or whether an exact geometric-parity
reconciliation is required. No such reconciliation is authorized here.

## Evidence

- Step 12 review board:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/review/STEP_12_FRESH_DCC_SOURCE_GEOMETRY_A01_REVIEW_BOARD.png`
- Review board SHA-256:
  `d5fd658eed5c62c8775ed4f53e5478d233ddc47147382f69d87c021c42a9f474`
- Dual-candidate validation:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_12_DUAL_DCC_SOURCE_CANDIDATE_A01_VALIDATION.json`
- Validation SHA-256:
  `4341a7dd0b8218731cc171ed0e1159989f585137b031019a5b8b8920b09dc6f3`
- Post-build checkpoint:
  `Saved/ProjectRecovery/20260724-082657`

The review board and validation remain `proof only`. Flamestrike's selection
and identity decision recorded here are `authoritative`.

## Authority Boundary

This decision authorizes only:

- the Candidate A to Siege Breaker identity assignment;
- the Candidate B to Foe Hammer identity assignment;
- the shared twin-identity rule;
- the two doubled head-side distinctions; and
- creation and maintenance of the corresponding authority/resume records.

It does not authorize:

- modifying either selected source;
- copying or renaming Candidate B into a Foe Hammer production directory;
- resolving the recorded depth difference;
- retopology;
- UVs, baking, textures, materials, LODs, or collision;
- export;
- Unreal work;
- `DCC game-ready candidate` classification;
- `Fully game-ready` classification; or
- Step 13.

## Next Approval Gate

The next production-moving action requires a separate visible contract. It
must state whether to:

1. preserve the two audited geometries exactly and perform a hash-verified
   Foe Hammer identity fork; or
2. run an evidence-only geometric-parity reconciliation before either asset
   advances.

Until then, both selected assets remain `DCC source candidate`.

## Superseding Depth-Ownership Core Recovery — 2026-07-24

This section supersedes the geometry-status, candidate-assignment, depth, and
next-gate statements above while preserving the original selection record as
historical evidence.

Flamestrike clarified and approved that:

- Siege Breaker and Foe Hammer must have identical overall dimensions;
- their body and hammer-face envelope is identical;
- the unequal rune and metal spans are local `C04` face-treatment extents,
  not global body depths;
- Siege Breaker remains double rune sided;
- Foe Hammer remains double metal-center-piece sided; and
- the common full body depth is the authoritative axial value
  `6644212/149985 cm = 44.299176584 cm`.

The identity selection remains `authoritative`. The assignment of the
existing Step 12 `.blend` files as current DCC source candidates is revoked.
Both geometry families are `invalid / quarantined in place`; their hashes,
measurements, and audits remain `proof only` for lineage and narrow
implementation checks.

Neither asset currently has a valid DCC source candidate. No Foe Hammer source
fork is authorized. A fresh recovery blueprint and a separately approved
build contract are required before geometry resumes.

Governing recovery record:

`docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_12_DEPTH_OWNERSHIP_CORE_RECOVERY.md`
