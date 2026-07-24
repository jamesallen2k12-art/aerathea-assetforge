# SM_DRW_FoeHammer_Hammer_A01 Identity And Resume State

## 2026-07-24 Fresh Standalone Foe Hammer Source — Current State

The approved `FRESH_TWIN_DCC_SOURCE_BUILDER_A01` contract created the first
valid standalone Foe Hammer Blender source.

- Asset identity: `authoritative`.
- Treatment: double metal-center-piece sided.
- Geometry status: `DCC source candidate`.
- Visual decision: `pending Flamestrike`.
- Independent saved-file audit: `PASS`.
- Independent cross-asset audit: `PASS`.
- Exact XYZ:
  `50719500/517681 × 6644212/149985 × 170/1 cm`.
- Decimal XYZ:
  `97.974428267601 × 44.299176584 × 170 cm`.
- Observed XYZ difference from Siege Breaker:
  `0.0 × 0.0 × 0.0 cm`.
- Canonical shared-base equality with Siege Breaker: `PASS`.
- Quarantined geometry read count: `0`.
- DCC game-ready candidate: `false`.
- Fully game-ready: `false`.
- Step 13 authority: `false`.
- Unreal authority: `false`.

Current standalone source:

`SourceAssets/Blender/Weapons/Dwarven/SM_DRW_FoeHammer_Hammer_A01/A12_R10_R8_SharedDepth_DCCSource_A01/SM_DRW_FoeHammer_Hammer_A01_DCCSource_SharedDepth_A01.blend`

SHA-256:

`67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4`

Independent saved-file audit SHA-256:

`9107b943046cfe3373e301e88636ee628817c7e7766892048136de7a70e9b846`

The approved metal source interval `[418,557)` remains an exact local
registration domain. Only selected source-owned pixels create visible face
geometry; the interval rectangle is not filled. The treatment and its ruled
join remain inside the shared global depth envelope.

Review handoff:

`docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/handoffs/FRESH_TWIN_DCC_SOURCE_BUILDER_A01_VISUAL_REVIEW_HANDOFF.md`

On resume, report that Foe Hammer now has an audited standalone
`DCC source candidate`, is otherwise canonically identical to Siege Breaker,
and awaits Flamestrike's visual decision. Step 13, retopology, UVs, baking,
export, and Unreal remain locked behind a separate visible contract.

## Historical Identity Establishment And Pre-Build State

The remainder of this record preserves the identity decision, quarantined
lineage, and pre-build resume state. It does not override the current state
above.

- Date established: `2026-07-24`
- Asset name: `Foe Hammer`
- Asset ID: `SM_DRW_FoeHammer_Hammer_A01`
- Asset type: `Dwarven great hammer weapon/prop`
- Identity record status: `authoritative`
- Geometry status:
  `no valid DCC source candidate; former Step 12 source invalid / quarantined in place`
- DCC game-ready status: `false`
- Fully game-ready status: `false`
- Step 13 authority: `false`
- Unreal authority: `false`

## Governing Shared-Depth Blueprint — Historical Pre-Build Authority

Flamestrike approved `SHARED_DEPTH_RECOVERY_BLUEPRINT_A01`.

- Blueprint status: `authoritative`.
- Blueprint validation: `proof only; 66/66 PASS`.
- Authority-lock validation: `proof only; 43/43 PASS`.
- Exact Foe Hammer XYZ:
  `50719500/517681 × 6644212/149985 × 170/1 cm`.
- Decimal XYZ:
  `97.974428267601 × 44.299176584 × 170 cm`.
- Shared body: canonically identical to Siege Breaker.
- Foe Hammer distinction: double metal-center-piece sided.
- Allowed geometry difference: tagged local `C04` treatment only.
- Current valid Foe Hammer DCC source candidate: `does not exist`.
- Former Step 12 metal source: `invalid / quarantined in place`.
- Fresh builder, Blender, geometry, source fork, Step 13, and Unreal:
  `unauthorized`.

Authority lock:

`docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK.json`

Approved handoff:

`docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/handoffs/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_APPROVED_HANDOFF.md`

No production action is active. A separate visible fresh-builder contract and
separate Flamestrike approval are required before DCC work.

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

## Historical Core Recovery Override — 2026-07-24

Flamestrike clarified and approved that the unequal rune and metal source
spans are local `C04` face-treatment extents, not different global body
depths.

Foe Hammer and Siege Breaker must have exactly identical overall dimensions
and the same body and hammer-face envelope. Their common full body depth is
the approved axial value:

`6644212/149985 cm = 44.299176584 cm`.

Foe Hammer remains the double-metal-center-piece twin. Its prior Step 12
metal candidate is now `invalid / quarantined in place`, not a current DCC
source candidate. The identity decision remains `authoritative`.

Governing recovery record:

`docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_12_DEPTH_OWNERSHIP_CORE_RECOVERY.md`

## Historical Quarantined Source Lineage

- Source run:
  `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Source candidate key: `metal_center_piece_side`
- Source artifact status:
  `invalid / quarantined in place; historical Step 12 candidate lineage`
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
- Independent saved-file audit:
  `105/105 PASS; proof only for narrow implementation consistency`
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

This section records the pre-recovery evidence and is superseded by
`Current Core Recovery Override — 2026-07-24`.

Shared identity is authoritative; exact mesh parity was not proven by the
former Step 12 candidates.

The selected Foe Hammer candidate is
`43.120437956204 cm` deep. The selected Siege Breaker candidate is
`34.434306569343 cm` deep. Their observed topology counts also differ.

These measurements must remain visible. They may not be normalized, averaged,
or described as exact geometric equality without a separately approved rule
and audit. A later decision must establish whether the difference is accepted
as part of the head-side treatment or must be reconciled before advancement.

## Historical Pre-Build Artifact Vocabulary

- Foe Hammer identity and double-metal-center-piece treatment:
  `authoritative`.
- Shared-depth recovery blueprint: `authoritative`.
- Former Candidate B geometry assignment: `superseded`.
- Candidate B Blender source: `invalid / quarantined in place`.
- Candidate B validation and review renders: `proof only`.
- Standalone Foe Hammer Blender source: `does not exist`.
- Foe Hammer UVs, textures, materials, LODs, collision, and exports:
  `do not exist under the Foe Hammer identity`.
- Unreal asset: `does not exist`.
- Valid DCC source candidate: `false`.
- DCC game-ready candidate: `false`.
- Fully game-ready: `false`.

## Historical Pre-Build Resume Instruction

On resume, verify:

1. this record;
2. the shared-depth blueprint authority lock and approved handoff;
3. the governing dual-asset selection approval record;
4. the hash-locked historical Candidate B source and canonical geometry;
5. the latest recovery journal/checkpoint; and
6. git status.

Report that Foe Hammer's identity, double-metal-center-piece treatment, exact
shared XYZ, and shared-body blueprint are authoritative. Its former Step 12
source is `invalid / quarantined in place`; there is no standalone or valid
Foe Hammer DCC source candidate; and no fresh-builder contract is active.

## Historical Pre-Build Next Approval Gate

No production action is currently active.

A separate visible fresh-builder contract and separate Flamestrike approval
are required before either twin is rebuilt from the last Core-valid evidence.
The quarantined Candidate B geometry may not be forked or repaired forward.
Step 13, source modification, asset copying/renaming, export, and Unreal
remain locked.
