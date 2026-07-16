# Step 07R Renewed Dependency Audit A01 Output Record

Status: approved bounded recovered Step 07 measurement authority; original package and downstream handoff remain quarantined

Artifact classification: `authoritative`

Date: 2026-07-15

## Assigned Goal

Audit the quarantined original Step 07 package against the approved Step 04R
recovery, restored Step 05 authority, approved Step 06R contact recovery, and
approved bounded Step 06Q authority. Determine whether Step 07 can be
restored, reused only through bounded authority, or must remain quarantined.
The audit did not modify original Step 07 records. Flamestrike separately
approved the exact bounded classification recorded below.

## Approved Decision

Apply **bounded recovered Step 07 measurement authority** without restoring
the original Step 07 package as a whole.

The source-linked calibration records, left/right measurement manifests,
measurement-contract sets, and seven-entry disagreement list are supported by
the authoritative left/right panels and the current recovered dependency
chain. The evidence board and original validation remain `proof only`.

The original Step 07 output may be used only through the specifically named
measurement and historical-approval sections in the audit manifest. Its old
`Next Gate` section is superseded. The original Step 07-to-Step 08 handoff
remains `quarantined/superseded` because it broadly names the original Step 06
package and advances a Step 08 gate that was later stopped by Core Recovery.

Flamestrike approved and applied this exact bounded classification on
2026-07-15. Step 08, production work, commit, and push remain unauthorized.

## Authority And Integrity Result

- authoritative recovery inputs checked: `10`;
- original Step 07 artifacts checked: `12`;
- original Step 07 artifact hashes matching: `12`;
- original Step 07 artifact hash failures: `0`;
- original Step 07 JSON records parsed: `7`;
- original Step 07 files modified: false;
- unrelated staged files: `0`.

The audit contract, manifest, and validation hashes are:

- contract:
  `45f1820454cd32ad56f7f7d7b9bdf15295864b14ef0514f3c0faf14bc18b673b`;
- audit manifest:
  `20850708491912f27620b68d803f3ce64c64c20759797beb48a7ea3dc56c3598`;
- validation:
  `b7dc9ed7b1cc34ef74025ebdaa696bf4b219cbe72636292faf715b7dc65645e7`.

## Step 06 Dependency Finding

The original Step 07 execution contract uses Step 06 only for controls,
status, and blockers and explicitly forbids front/back coordinate or
calibration reuse. The approved Step 06Q bounded authority and Step 06R
contacts now support that dependency.

The structured Step 07 measurement records contain:

- zero Step 06 file-path or hash dependencies;
- neither invalid original Step 06 coordinate `(372,360)` nor `(355,271)`;
- no reference to the original Step 06 validation manifest;
- no reference to the original Step 06 output record;
- no reference to the original Step 06-to-Step 07 handoff.

The measurement values link directly to the authoritative left/right panels.
No invalid Step 06 coordinate or invalid completion-chain record propagates
into Step 07 measurement values.

The original Step 07-to-Step 08 handoff is different: it broadly names
approved Step 06 measurements without the later bounded Step 06Q override and
advances the superseded Step 08 gate. It is therefore not recommended for
restoration.

## Focused Measurement Replay

- calibration observations checked: `8`;
- exact calibration formulas replayed: `8`;
- visible row samples checked: `26`;
- row-width and profile-center formulas replayed: `26`;
- irregular C-004 observations checked: `8`;
- contact samples checked: `36`;
- appearance landmarks checked: `20`;
- measurement contracts checked: `24`;
- unresolved contract references: `0`;
- disagreement entries checked: `7`;
- selected or averaged disagreement values: `0`;
- coordinate or formula failures: `0`.

No consolidated scale, world-space contour/contact conversion, physical
cross-view pairing, hidden closure, interpretation, or geometry was created.

## Native Contact Evidence

All 36 left/right contact coordinates were read directly from the
authoritative panels with exact RGB values recorded in the audit manifest.

- native channel range across all contact pixels: `0` through `81`;
- external white or near-white background samples: `0`;
- left samples: `18`;
- right samples: `18`.

The rejected original Step 06 background observations were RGB
`(235,237,238)` and `(249,249,249)`. No Step 07 contact sample resembles those
external background pixels. This comparison is exact source-pixel evidence;
it does not create a threshold-derived mask or candidate contour.

## Ten Disclosed Step 04 Endpoint Overlaps

The prior dependency audit correctly identified ten Step 07 contact
coordinates equal to older non-top Step 04 review-segment endpoints: six in
the left view and four in the right view.

All ten were re-read from the current authoritative left/right panels and are
dark source-visible interface pixels. Their exact coordinates and RGB values
are recorded in the renewed audit manifest.

Executable Step 05-07 builder replay remains unavailable. Therefore:

- independent original derivation is not proven;
- copying is not proven;
- coordinate equality is disclosed but is not treated as lineage proof;
- current source ownership is supported through this renewed exact native-
  pixel audit.

The approved classification does not claim independent original derivation.

## Evidence Board Result

The original Step 07 evidence board remains `proof only`.

- left untouched source tile origin: `(18,82)`;
- left changed pixels: `0`;
- left maximum RGB delta: `0`;
- right untouched source tile origin: `(18,533)`;
- right changed pixels: `0`;
- right maximum RGB delta: `0`;
- candidate fill: absent;
- hidden closure: absent;
- geometry: absent.

## Approved Artifact Classification

Approved classification:

- original Step 07 contract: restore as `authoritative for execution scope`;
- left/right calibration records: restore as `authoritative`, with all four
  calibration disagreements blocked;
- left/right measurement manifests: restore through the renewed audit
  override, with the ten endpoint overlaps disclosed and no independent-
  derivation claim;
- left/right measurement contract sets: restore as `authoritative`;
- seven-entry disagreement list: restore as `authoritative`, with every block
  preserved;
- evidence board and original validation: retain as `proof only`;
- original output record: keep whole-file `quarantined`, using only the
  explicitly named supported sections through the audit override;
- original Step 07-to-Step 08 handoff: remain
  `quarantined/superseded`;
- original Step 07 package as a whole: remain `quarantined`;
- Step 08: remain `stopped`.

## Validation Result

Focused validation:

- validators passed: `35`;
- validators failed: `0`;
- aggregate result:
  `pass_approved_bounded_recovered_step_07_measurement_authority`.

Validation manifest:

`manifests/STEP_07R_RENEWED_DEPENDENCY_AUDIT_A01_VALIDATION.json`

## Assumptions Or Interpretations

None. Exact file identities, JSON records, source pixels, formulas, and
explicit dependency text control the decision. The absence of executable
builder replay is recorded as a limitation and is not filled by inference.

## Files Changed Or Created

1. `steps/STEP_07R_RENEWED_DEPENDENCY_AUDIT_A01_CONTRACT.md`;
2. `manifests/STEP_07R_RENEWED_DEPENDENCY_AUDIT_A01.json`;
3. `manifests/STEP_07R_RENEWED_DEPENDENCY_AUDIT_A01_VALIDATION.json`;
4. this output record.

Approved classification closeout also updates:

5. `SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md`;
6. `SM_GIA_BloodAxeCairnstone_A005_CORE_RECOVERY_STATUS_20260715_STEP04_TOP_CONTACT_EVIDENCE.md`;
7. `SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md`;
8. `SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md`.

No original Step 07 record or evidence image was modified. No drift-ledger
classification was changed because this approved decision closes an existing
recovery gate and records no new drift event.

## Checkpoint And Repository State

- pre-action checkpoint: `Saved/ProjectRecovery/20260715-211549/`;
- validated-candidate checkpoint: `Saved/ProjectRecovery/20260715-212643/`;
- approved pre-classification checkpoint:
  `Saved/ProjectRecovery/20260715-212847/`;
- starting local and remote commit: `e3a0eac`;
- audit outputs: uncommitted and unpushed;
- original Step 07 source records: unchanged;
- pre-existing unrelated work: untouched;
- unrelated staged files: none.

## Artifact Status

- Step 07R contract: `authoritative for execution scope only`;
- Step 07R audit manifest and this output: `authoritative`;
- Step 07R validation: `proof only`;
- bounded Step 07 measurement authority: `authoritative` through the approved
  recovery override;
- original Step 07 package as a whole: remains `quarantined`;
- original Step 07-to-Step 08 handoff: remains
  `quarantined/superseded`;
- Step 08: remains `stopped`.

## Output Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Decision: apply the exact bounded recovered Step 07 measurement authority
  reviewed visibly
- Original Step 07 package: remains `quarantined` as a whole
- Original Step 07-to-Step 08 handoff: remains
  `quarantined/superseded`
- Step 08: remains `stopped`
- Approved pre-classification checkpoint:
  `Saved/ProjectRecovery/20260715-212847/`
- Production work, commit, and push: not authorized

## Next Approval Gate

No downstream execution is authorized. The next permitted presentation is a
separate Core reassessment and renewed Step 08 authorization contract. Step
08, production work, commit, and push remain unauthorized until separately
approved.
