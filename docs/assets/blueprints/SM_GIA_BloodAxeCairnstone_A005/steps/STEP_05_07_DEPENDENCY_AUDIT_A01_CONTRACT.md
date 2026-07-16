# Step 05-07 Dependency Audit A01 Contract

Status: approved for execution; execution stopped at newly proven Step 06 drift

Artifact classification: authoritative for execution scope

Date: 2026-07-15

## Decision

Determine separately for Steps 05, 06, and 07 whether their suspended
authority relied on, copied, transformed, validated, or otherwise propagated
the invalid original Step 04 top coordinates or completion claims.

The audit may recommend restore, remain quarantined, or invalidate. It may not
perform the reclassification.

## Approval

- Approver: Flamestrike.
- Statement: approved.
- Date: 2026-07-15.
- Scope: the exact Step 05-07 Dependency Audit A01 contract presented after
  the mandatory Step 04R restart.
- Exclusion: automatic restoration or invalidation, source-record edits, Step
  08, interpretation, geometry, production work, commit, and push.

## Governing Authority

1. AGENTS.md and Core Recovery Protocol.
2. The approved fresh-start multi-step plan.
3. The A005 charter, firewall, and source lock.
4. The A005 Step 04 top-contact Core Recovery status.
5. The approved Step 04R contract, recovery manifests, output record, and
   restart handoff.
6. This contract.

## Approved Inputs

- authoritative A02 source and Step 03 lossless panels;
- quarantined original Step 04 inventory, evidence, validation, output, and
  handoff only for dependency and drift comparison;
- authoritative Step 04R recovery inventory and exact contact manifest;
- suspended Step 05-07 contracts, manifests, evidence, validations, output
  records, and handoffs;
- scoped git history and any tracked A005 generation scripts needed to prove
  lineage;
- generic read-only audit rules containing no legacy Cairn Stone constants.

## Allowed Actions

- checkpoint before the audit;
- verify file identities, hashes, JSON parsing, source-panel lineage, and git
  history;
- enumerate direct references to the original Step 04 inventory, hashes,
  evidence paths, coordinates, and completion claims;
- compare same-view coordinates while distinguishing semantic reuse from
  coordinate propagation;
- verify whether Step 05 registration marks reuse Step 04 review coordinates;
- verify whether Steps 06-07 use the top panel or invalid Step 04 top
  coordinates;
- disclose exact non-top coordinate overlap rather than treating it as proof
  of independent derivation;
- create exact local native-pixel diagnostics when a source-ownership claim
  requires verification;
- produce a candidate per-step classification recommendation and proof-only
  validation;
- open the approval-ready review records visibly.

## Scoped Writable Outputs

- steps/STEP_05_07_DEPENDENCY_AUDIT_A01_CONTRACT.md;
- manifests/STEP_05_07_DEPENDENCY_AUDIT_A01.json;
- manifests/STEP_05_07_DEPENDENCY_AUDIT_A01_VALIDATION.json;
- steps/STEP_05_07_DEPENDENCY_AUDIT_A01_OUTPUT_RECORD.md;
- local-only checkpoints and diagnostics under Saved/.

Core Recovery additionally requires the single A005 drift-ledger entry created
after the audit proved a new Step 06 source-ownership violation.

## Blocked

- modifying any Step 05-07 source record;
- treating a declaration as proven when direct evidence conflicts with it;
- automatic restoration or invalidation;
- repairing Step 06 inside the dependency audit;
- presenting a renewed Step 08 contract;
- A001-A004 asset-specific data;
- interpretation, candidate geometry, DCC, texture, FBX, Unreal, or
  production-root work;
- staging, committing, or pushing before separate output approval.

## Validators

- all scoped JSON inputs parse;
- current hashes match embedded validation and source-panel identities;
- original and recovered Step 04 inputs remain byte-identical;
- same-view coordinate comparisons are exact and do not compare unrelated
  panel coordinate spaces;
- semantic IDs and relations used downstream match the approved Step 04R
  preservation record;
- every newly challenged source-ownership claim is checked at native pixel
  resolution;
- missing executable lineage is recorded as a limitation;
- no source records are modified;
- no interpretation, geometry, legacy access, Step 08 output, or unrelated
  staging occurs.

## Artifact Status

This contract is authoritative for its approved execution boundary. The audit
manifest and output record begin as candidate. Validation and local
diagnostics are proof only. All Step 05-07 classifications remain suspended
until separate Flamestrike approval.

## Stop Conditions

Hash mismatch, ambiguous lineage treated as proof, newly discovered invalid
source ownership, source-record modification, legacy-data need,
interpretation, geometry, Step 08 work, or unrelated staging.

The newly proven Step 06 background contact samples triggered this stop
condition. Core Recovery supersedes normal audit continuation.

## Checkpoints

- Pre-action: Saved/ProjectRecovery/20260715-181325/.
- Step 06 drift boundary: Saved/ProjectRecovery/20260715-182015/.

## Next Gate

Present the candidate dependency-audit package for Flamestrike approval or
rejection. No classification changes occur automatically.
