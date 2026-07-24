# Step 13 Immutable Geometry And Artistic Review A01 Output Record

- Date: `2026-07-24`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Approved contract SHA-256:
  `cc5b3185c851a229f44428b4544a19c490025095fcae2b5313fc3f5ae3f5d74b`
- Technical disposition: `FAIL`
- Keeper-feature disposition: `BLOCKED`
- Step 13 complete: `false`
- Asset pipeline status: `DCC source candidate` for both sources, unchanged
- Artifact disposition: both sources are `quarantined in place` as Step
  13-pass, Step 14, export, or Unreal authority
- Step 14 authority: `false`
- Geometry modification / repair authority: `false`
- Export / Unreal authority: `false`

## Production Decision

Step 13 stops at its fail-closed technical gate. The read-only auditor directly
observed saved topology and declared-contact failures in both immutable
sources. The contract permits rendering only after a complete technical PASS,
so no Step 13 candidate render or geometry-readable artistic decision was
created.

Both sources remain reviewable DCC files and therefore retain the pipeline
vocabulary `DCC source candidate`. They do not pass Step 13 and cannot provide
Step 14 or downstream authority.

## Immutable Source Hash Result

### Siege Breaker

- Path:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_SharedDepth_DCCSource_A01/SM_DRW_SiegeBreaker_Hammer_A01_DCCSource_SharedDepth_A01.blend`
- SHA-256 before:
  `c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537`
- SHA-256 after:
  `c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537`
- Byte-identical: `PASS`

### Foe Hammer

- Path:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_FoeHammer_Hammer_A01/A12_R10_R8_SharedDepth_DCCSource_A01/SM_DRW_FoeHammer_Hammer_A01_DCCSource_SharedDepth_A01.blend`
- SHA-256 before:
  `67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4`
- SHA-256 after:
  `67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4`
- Byte-identical: `PASS`

Neither source was modified, resaved, copied, moved, renamed, or repaired.

## Technical Evidence

Corrected technical audit:

- Path:
  `../manifests/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_TECHNICAL_AUDIT.json`
- SHA-256:
  `e1c2e6bcbc4f2cf7b7ff991c8ea8fa25f72ecf2ae4913683b1d9ba1ab1a945ad`
- Artifact status: `proof only; FAIL`

The first audit pass also returned `FAIL`, but one Foe Hammer local-C04 check
incorrectly required the visible owner pixels to fill a registration interval.
The corrected audit records the superseded audit and hash, removes only that
false condition, and still returns `FAIL`.

### Direct Failures

| Evidence | Siege Breaker | Foe Hammer |
| --- | ---: | ---: |
| Unpaired exact assembled boundary edges | `19,200` | `18,900` |
| Boundary incidences greater than two | `890` | `890` |
| Assembled boundary-winding mismatches | `2,978` | `2,936` |
| Positive local-C04 closure winding mismatches | `138` | `118` |
| Rz180 local-C04 closure winding mismatches | `138` | `118` |
| Assembled closed/manifold volume | `FAIL` | `FAIL` |
| Declared contacts | `FAIL` | `FAIL` |
| Protected-negative-space completion | `FAIL` | `FAIL` |

The local C04 closure winding failures were independently confirmed through
native Blender `bmesh` observations; no builder claim was used to establish
the counts.

### Exact Results That Remain Valid

- Observed twin XYZ difference:
  `0.0 × 0.0 × 0.0 cm`.
- Locked exact XYZ:
  `50719500/517681 × 6644212/149985 × 170/1 cm`.
- Shared saved-base canonical equality: `PASS`.
- No geometry difference outside tagged local `C04`: `PASS`.
- Correct double-rune versus double-metal-center-piece identity: `PASS`.
- Source identity, lineage, provenance, applied transforms, pivot,
  dependency, forbidden-method, and quarantined-input checks: `PASS`.
- High-poly triangle counts remain observed metrics only; no optimization
  decision was made.

These narrow PASS results do not override the closed/manifold, contact, or
protected-negative-space failures.

## Renderer And Keeper Gate

- Renderer file created: `false`.
- Renderer run: `false`.
- Candidate renders: `0`.
- Silhouette / XOR / thumbnail / wireframe / turntable images: `0`.
- Keeper-feature audit:
  `../manifests/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_KEEPER_FEATURE_AUDIT.json`.
- Keeper-feature audit SHA-256:
  `8dac9b954e6758812f634a48a74171c232b852d8b086c2ffcb37fdd5415b1bc5`.
- Keeper-feature result: `BLOCKED`.
- All ten geometry-readable keeper features: `BLOCKED`.
- Material-dependent keeper features:
  `not evaluated at this geometry-only gate`.

The visible board is a non-render technical-stop board. It cannot be mistaken
for a geometry candidate or artistic approval:

- Path:
  `../review/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_REVIEW.png`.
- SHA-256:
  `9d7b7d2331a33b77fd82b84f82055bc7f6a9f39f3e31a2492aa5bf0a2f117710`.
- Artifact status: `proof only`.

## Core Recovery Classification

- Last known Core-valid construction state:
  approved `SHARED_DEPTH_RECOVERY_BLUEPRINT_A01`, its immutable authority, and
  the fresh-builder approval boundary before geometry readiness was inferred.
- First drift action:
  the fresh builder saved the local C04 ruled closures and broader surface
  assembly without proving winding consistency, exact closed/manifold
  boundary incidence, and every declared contact before advancement.
- Causing assumption:
  narrow dimensional, provenance, identity, hash, and visual checks were
  treated as sufficient technical-readiness evidence.
- Affected outputs:
  both `.blend` sources, build/pre-save manifests, the earlier narrow
  independent audit, fresh visual advancement record, and Step 13 readiness.
- Preserved valid evidence:
  exact dimensions, shared-base equality, local twin identity, source
  provenance, and immutable source hashes.
- Invalid or blocked implication:
  Step 13 readiness and any Step 14/downstream use.
- Smallest sufficient recovery:
  stop; return to the approved shared-depth blueprint; prepare a separately
  approved Core recovery/fresh-builder contract with mandatory pre-save and
  independent topology/contact checks. Any alternative repair route requires
  a Core reassessment and Flamestrike approval.
- Drift ledger:
  `docs/projects/assetforge/DRIFT_LEDGER.md`, entry
  `Twin Hammer Fresh-Source Topology And Contact Drift`.
- Drift-ledger SHA-256 at this record:
  `c72a42db610de5409a7090bdb304246c2bbcd415dad3446a3bcdb8b110b2a9f1`.

## Files Created Or Updated

| Path | Classification |
| --- | --- |
| `Tools/DCC/audit_siegebreaker_foehammer_step13_immutable_geometry_a01.py` | `proof-producing tool`; SHA-256 `0a1273392baab4d62edbd86691e3c782e5d25737f1fe9b1f3a522f389e17e0f9` |
| `../manifests/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_TECHNICAL_AUDIT.json` | `proof only; FAIL` |
| `../manifests/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_KEEPER_FEATURE_AUDIT.json` | `proof only; BLOCKED` |
| `../review/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01/RENDER_NOT_RUN.md` | `proof only`; SHA-256 `4b4b4800c923f9f5f1dc6ed3b6d30da14117fc4d08b540af16b59347b5592217` |
| `../review/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_REVIEW.png` | `proof only` |
| `STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_OUTPUT_RECORD.md` | `authoritative within the approved stop/recovery boundary` |
| `../handoffs/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_STOP_HANDOFF.md` | `authoritative stop handoff` |
| `../manifests/STEP_STATE.json` | `authoritative run status` |
| `docs/projects/assetforge/DRIFT_LEDGER.md` | `authoritative Core drift ledger` |
| `docs/projects/assetforge/RECOVERY_JOURNAL.md` | `authoritative recovery journal`; pre-job and post-job entries |

The separately approved documentation-gate files are also part of the scoped
Step 13 commit:

- `STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_CONTRACT.md`
  (`candidate approved for this execution`);
- `../manifests/STEP_13_IMMUTABLE_GEOMETRY_ARTISTIC_REVIEW_A01_CONTRACT_VALIDATION.json`
  (`proof only; PASS 46/46`).

## Recovery Checkpoints

- Pre-job checkpoint:
  `Saved/ProjectRecovery/20260724-125356/`.
- Post-job failure/stop checkpoint:
  `Saved/ProjectRecovery/20260724-132221/`.
- Checkpoint artifact status:
  `local-only recovery evidence`.

## Assumptions, Interpretations, And Uncertainty

- Unapproved assumptions: `none`.
- Evidence-bound interpretation:
  the saved mesh objects are source-owned surface patches; each was audited
  individually, and closed/manifold volume was assessed through exact
  assembled boundary incidence. Even under that less restrictive
  assembly-level treatment, both sources fail.
- Unapproved tolerance use: `none`.
- Remaining uncertainty:
  the exact recovery implementation has not been selected or approved.

## Stop And Next Approval Need

Step 13 is `FAIL / BLOCKED`, not complete. Step 14 remains locked.

The next permitted action is only a Flamestrike decision on a separate Core
recovery reassessment and exact fresh-rebuild contract. No geometry repair,
rebuild, renderer, retopology, UV, bake, material, LOD, collision, export,
Unreal, or Step 14 work is authorized by this record.
