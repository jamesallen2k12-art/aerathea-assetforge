# A005 Scale-Authority Recovery A01 Output Record

Status: `candidate; blocked by unresolved source/target conflict`

Artifact classification: `candidate`

Contract: `A005-CR-SAR-A01`

Approved physical-bounds choice: `A005-SAR-BOUNDS-A`

Date: 2026-07-17

## Controlling Decision

`blocked_by_unresolved_source_target_conflict`

The approved global-transform test completed without clipping, local warping, geometry, or historical-record edits. It did not recover one honest world-space construction frame because the source-authored component proportions do not agree with all six approved physical targets.

A single global scale on an axis preserves the source ratio between components. The source ratios and target ratios differ in every tested X, Y, and Z comparison. Satisfying all targets would therefore require a forbidden local/component warp, a change to the physical targets, or a later explicit interpretation decision.

## What The Contract Proved

- The approved physical targets were recorded separately from source-pixel evidence: overall height `220 cm`; C-001 width/depth `120/90 cm`; C-004 width/depth `140/110 cm`; C-004 height `35 cm`.
- Front is the primary X/Z upright source owner.
- Left is the primary Y/Z upright source owner.
- Back and right remain validation views with ownership only for non-conflicting source-visible details.
- The top derivative uses the approved global X/Y factor `1.1260059213`, with Y held at `1.0`.
- Five complete-panel transforms and exact inverses were recorded.
- Maximum forward/inverse round-trip error is `0 px`.
- No transformed panel clips source pixels.
- Derivatives were inverse-sampled from the original Step 03 panels using nearest-neighbor sampling.
- No local, component, row, feature, perspective, cage, lattice, spline, or content-aware warp was used.
- No center, origin, pivot, snap anchor, hidden surface, interpretation, or geometry was created.
- No existing Step 01-Step 10 record was edited by this recovery execution.

## Holdout Evidence

| Diagnostic | Result | Authority |
|---|---:|---|
| Front/back full-silhouette IoU | `0.783536692570` | proof only |
| Front/back median / maximum edge difference | `18 px / 88 px` | proof only |
| Left/right full-silhouette IoU | `0.892233140396` | proof only |
| Left/right median / maximum edge difference | `5 px / 87 px` | proof only |
| Top observed X/Y ratio | `0.935344830000` | proof only |
| Top transformed X/Y ratio | `1.053203817037` | proof only |

No holdout was used as a local fitting input. No production pass threshold was invented.

## Source/Target Conflicts

All `10` exact within-axis ratio checks conflict:

| Check group | Source ratio range | Target ratio | Relative difference range |
|---|---:|---:|---:|
| C-004/C-001 X, front/back | `1.260870-1.296296` | `1.166667` | `+8.07% to +11.11%` |
| C-004/C-001 Y, left/right | `1.339286-1.340278` | `1.222222` | `+9.58% to +9.66%` |
| Base/overall Z, upright views | `0.165333-0.189091` | `0.159091` | `+3.92% to +18.86%` |
| Top C-004/C-001 X | `1.308176` | `1.166667` | `+12.13%` |
| Top C-004/C-001 Y | `1.489362` | `1.222222` | `+21.86%` |

The detailed values and formulas are preserved in `manifests/SCALE_AUTHORITY_RECOVERY_A01_DISTORTION_HOLDOUT.json`.

## World/Integration Result

The recovery override traced all `63` routed records and `818` affected field matches without rewriting history:

- `595` fields: `reference_only_after_recovery`;
- `142` fields: `valid_physical_target_only`;
- `81` fields: `valid_raw_evidence_only`;
- `0` fields: `recovered_authority_candidate`.

World conversion and the integrated construction frame remain blocked. The seven Step 10 records reserved by the reassessment remain unchanged and reserved for a later contract.

## Rejected Internal Proof

The first diagnostic mask attempt attached printed dimension annotations to source silhouettes and contaminated the holdout metrics. It was internally rejected, preserved locally as `quarantined local proof only`, and never used as authority. The source panels and approved transforms did not change during the correction.

## Output Classification

- Input lock and validation: `proof only`.
- Derivative panels and review board: `proof only`.
- Physical-bounds, transform, distortion/holdout, world/integration, this output record, and the handoff: `candidate`.
- Rejected first diagnostic attempt: `quarantined local proof only`.
- Original source and prior approved authority: unchanged.

## Checkpoints

- Pre-action: `Saved/ProjectRecovery/20260717-090216/`.
- After input lock and physical bounds: `Saved/ProjectRecovery/20260717-090714/`.
- After transforms, evidence, and world classification: `Saved/ProjectRecovery/20260717-092045/`.

## Required Flamestrike Decision

This output cannot honestly be approved as a recovered world-space construction frame.

Flamestrike must decide, in a separate explicit contract, which authority controls when the source proportions and physical targets disagree. Until then, Step 10 revision, Step 11, geometry, Blender, FBX, textures, materials, Unreal, collision, LODs, commit, and push remain stopped.

