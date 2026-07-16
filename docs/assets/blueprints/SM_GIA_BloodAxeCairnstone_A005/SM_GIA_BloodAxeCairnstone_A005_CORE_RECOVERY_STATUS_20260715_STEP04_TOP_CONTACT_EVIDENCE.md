# SM_GIA_BloodAxeCairnstone_A005 Core Recovery Status

Status: `Step 08R exact top evidence approved; original Step 06 and Step 07 packages remain quarantined as wholes; footprints and centers blocked`

Artifact classification: `authoritative recovery status`

Date: 2026-07-15

## Drift Event

During the approved Step 08 pre-action measurement audit, the final approved
Step 04 top ownership evidence was compared against the authoritative native
top panel. Multiple recorded top contact-mark coordinates are visibly outside
the source-owned object or extend into white annotation/background pixels.

Direct examples from the approved Step 04 inventory are:

- `CL-003` top segment samples at `(140,27)`, `(167,27)`, and `(195,27)`;
  their source RGB values are `(248,248,248)`, `(253,253,253)`, and
  `(254,254,254)` respectively;
- the `CL-002` top segment endpoint `(195,38)` has source RGB
  `(254,254,254)`;
- the `CL-003` left-side endpoint `(31,130)` has source RGB `(255,255,255)`.

These are unambiguous non-object pixels. This conflicts with the Step 04
output and validator claims that all final contact marks remain on
source-owned visible contacts.

## Governing Core Decision

Stop-the-line and Core Recovery apply. Step 08 production stopped before any
tracked Step 08 output was created. No Step 04 proof may be repaired forward
inside Step 08.

## Last Known Core-Valid State

The last fully completed Core-valid gate is Step 03: approved lossless panel
decomposition at commit `2cee686`, with final Step 03 handoff at `f2fb2b8`.

The authoritative A02 source, exact scanline evidence, A005 charter/firewall,
Step 01-03 contracts, source lock, crop manifest, and six lossless crops remain
authoritative.

The Step 04R recovery state added the Flamestrike-approved recovered semantic
inventory and 48 exact top-contact observations. Step 04R alone did not
restore the original Step 04 completion proof or any Step 05-07 authority.
The later approved Dependency Audit A01 restores Step 05, as recorded below.
The subsequently approved Step 06R package restores exact front/back contact
evidence. The approved Step 06Q classification restores a bounded recovered
Step 06 authority set from named unaffected records/sections plus Step 06R,
while keeping the original mixed-validity Step 06 package quarantined as a
whole. The approved Step 07R classification restores a bounded recovered Step
07 measurement authority set from the source-linked side-view records while
keeping the original Step 07 package and downstream handoff quarantined.

## First Drift Action

The final Step 04 correction pass retained top contact-mark coordinates that
still exceeded the source-owned object, then the final board and validation
manifest were accepted as source-bounded.

## Assumption That Caused Drift

Visual proximity on the composite evidence board was treated as sufficient
proof of source ownership. The final coordinate set was not audited against
the authoritative top panel at native pixel resolution with a deterministic
object-versus-background check.

## Affected Outputs And Statuses

- `evidence/STEP_04/SM_GIA_BloodAxeCairnstone_A005_STEP_04_TOP_OWNERSHIP_EVIDENCE.png`:
  `quarantined; invalid as source-bounded Step 04 proof`.
- `manifests/STEP_04_COMPONENT_OWNERSHIP_INVENTORY.json`:
  `quarantined/superseded for active authority`; embedded top review
  coordinates are `invalid`. Its semantic IDs and relations are preserved in
  the authoritative Step 04R recovery inventory.
- `manifests/STEP_04_VALIDATION_MANIFEST.json`:
  `quarantined; invalid as proof that all final boards are source-bounded`.
- `steps/STEP_04_OUTPUT_RECORD.md`, Step 04 approval-log claims, and the Step
  04 handoff: `quarantined/superseded as completion authority`.
- The Step 04 contract remains `authoritative` as the approved scope boundary.
- Step 05 is restored within its prior approved convention, frame,
  registration, and blocking boundaries by the approved Dependency Audit A01.
- The original Step 06 package remains `quarantined` after Dependency Audit
  A01 proved two invalid background contact observations. The two named
  original observations remain `invalid`. The approved Step 06R front/back
  recovery manifests are `authoritative` recovered contact evidence.
- The approved Step 06Q record makes only its explicitly named unaffected
  calibration records, non-contact measurement sections, contract definitions,
  and disagreement record authoritative as a bounded recovered authority set.
  The original contact arrays and original validation/evidence/output/handoff
  completion chain remain `quarantined/superseded`.
- Step 07 measurement records are `authoritative` only through the approved
  Step 07R bounded recovery override. The original Step 07 package remains
  `quarantined` as a whole; its original output `Next Gate` is superseded and
  its Step 07-to-Step 08 handoff remains `quarantined/superseded`.
- The original approved Step 08 boundary remains `suspended/superseded
  historical authority` and created no tracked output. The later approved
  Step 08R package is the only current top-measurement authority and is bounded
  as recorded below.

## Partial Original Step 08 Artifacts

- Pre-action checkpoint: `Saved/ProjectRecovery/20260715-160008/`.
- Recovery-boundary checkpoint: `Saved/ProjectRecovery/20260715-160608/`.
- No tracked Step 08 contract file, manifest, evidence board, output record, or
  handoff was created.
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/CoreRecovery/20260715_STEP04_TopContactEvidenceDrift/A005_STEP04_TopContactCoordinates_RejectionDiagnostic.png`:
  `invalid internal diagnostic; rejection evidence only`, SHA256
  `608c3660a5b7be1e0c8b31d4a5de75e465b50cb89b4115b355c57407662dd9e9`.
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/CoreRecovery/20260715_STEP04_TopContactEvidenceDrift/A005_STEP08_OuterEndpointDiagnostic_ReferenceOnly.png`:
  `reference only; unapproved partial Step 08 diagnostic`, SHA256
  `2a3df099fedb5a85dd34031f4810b46899e7a4178226815c79d73a33e302988b`.

Neither local diagnostic is authority.

## Step 04R Approved Recovery Result

Flamestrike approved the exact Step 04R recovery contract and visible output.
The approved package contains 48 fresh, discrete top-contact pixels: 16 each for `CL-001`,
`CL-002`, and `CL-003`, with four samples per visible cardinal sector.

Builder validation passed `24/24`; an independent read-only audit passed 30
additional checks. The source tile is pixel-exact with `0` changed pixels and
`0` maximum RGB delta. The marked tile reconstructs exactly from the manifest.
Original quarantined artifacts remain byte-identical. Step 05-07 remain
suspended and no Step 08 output exists.

Validated-candidate checkpoint:
`Saved/ProjectRecovery/20260715-163538/`.

Approved review board:

`evidence/STEP_04_RECOVERY/SM_GIA_BloodAxeCairnstone_A005_STEP_04_TOP_OWNERSHIP_EVIDENCE_RECOVERY_A01.png`

Flamestrike approved the visible Step 04R recovered top-contact package on
2026-07-15. The recovered inventory and exact contact manifest are now
`authoritative`; the board and validation remain `proof only`. Approved
pre-closeout checkpoint: `Saved/ProjectRecovery/20260715-163837/`.

Scoped recovery content commit `a8ae9ec` was pushed to `assetforge/main`,
advancing the remote from `3e219f0`. Restart handoff:
`handoffs/STEP_04R_TO_STEP_05_07_DEPENDENCY_AUDIT_HANDOFF.md`.
Final restart-handoff checkpoint: `Saved/ProjectRecovery/20260715-164736/`.

## Dependency Audit A01 Approved Classification

Flamestrike approved Dependency Audit A01 execution and subsequently approved
its visible output classification on 2026-07-15.

The audit proved that Step 05 did not reuse any Step 04 review coordinates.
Its 46 registration marks have zero same-view overlap with the quarantined
Step 04 review marks, and its semantic dependencies are preserved by Step
04R. Step 05 is therefore restored within its prior approved boundaries.

The audit also proved a new Step 06 drift:

- front CL-002 at (372,360), RGB (235,237,238), is external anti-aliased
  background;
- back CL-002 at (355,271), RGB (249,249,249), is external white background.

Step 06 remains quarantined. Step 07 remains quarantined behind Step 06.
Step 08 remains stopped. No measurement source record was modified.

Audit manifest:
`manifests/STEP_05_07_DEPENDENCY_AUDIT_A01.json`.

Audit validation:
`manifests/STEP_05_07_DEPENDENCY_AUDIT_A01_VALIDATION.json`.

Audit output:
`steps/STEP_05_07_DEPENDENCY_AUDIT_A01_OUTPUT_RECORD.md`.

## Step 06R Approved Recovered Contact Evidence

Flamestrike approved the Step 06R execution contract and subsequently
approved its visible output classification on 2026-07-15.

All 43 original front/back contact samples were re-audited at native
resolution for source ownership and named-contact role. Forty-one supported
samples were retained. The two invalid `CL-002` observations were replaced:

- front `(372,360)` background was superseded by `(371,360)`, full-source
  `(923,490)`, RGB `(144,143,144)`;
- back `(355,271)` background was superseded by `(345,270)`, full-source
  `(364,933)`, RGB `(165,166,164)`.

The front and back recovery manifests are `authoritative` recovered contact
evidence. The board and validation remain `proof only`. The original Step 06
package remains `quarantined`; Step 06 restoration was not authorized. Step
07 remains `quarantined`, Step 08 remains `stopped`, and commit/push remain
unauthorized.

Step 06R output:
`steps/STEP_06R_CONTACT_EVIDENCE_RECOVERY_A01_OUTPUT_RECORD.md`.

Step 06R pre-classification checkpoint:
`Saved/ProjectRecovery/20260715-192306/`.

## Step 06Q Approved Bounded Classification

Flamestrike approved Step 06Q Quarantine Reconsideration A01 execution and
subsequently approved its visible output classification on 2026-07-15.

The audit compared all 43 original contact observations with the approved
recovered observations: 41 are identical and two are the approved
replacements. It proved that the invalid points do not feed calibration,
height stations, visible row observations, C-004 observations, appearance
landmarks, contract values, or blocked-disagreement values.

The approved bounded authority set therefore contains:

- the Step 06 contract as scope authority;
- both calibration records with all four X/Z disagreements preserved;
- only the non-contact measurement-manifest sections explicitly listed by
  Step 06Q;
- both measurement-contract sets with contacts resolved through Step 06R;
- the seven-entry disagreement list with every block preserved;
- the authoritative Step 06R front/back contact manifests;
- the Step 06Q audit manifest and approved output record.

The original Step 06 package remains quarantined as a whole. Its original
contact arrays, validation aggregate pass, evidence board as complete contact
proof, output completion claim, and Step 07 handoff claim remain
quarantined/superseded. Step 07 authority is controlled separately by the
approved Step 07R bounded classification below. Step 08 remains stopped;
commit and push remain unauthorized.

Step 06Q output:
`steps/STEP_06Q_QUARANTINE_RECONSIDERATION_A01_OUTPUT_RECORD.md`.

Step 06Q pre-classification checkpoint:
`Saved/ProjectRecovery/20260715-195001/`.

## Step 07R Approved Bounded Classification

Flamestrike approved Step 07R Renewed Dependency Audit A01 execution and
subsequently approved its visible bounded classification on 2026-07-15.

The audit checked all twelve original Step 07 artifacts and found all twelve
hashes unchanged. Thirty-five focused validators pass with zero failures. It
replayed eight calibration observations, 26 row formulas, eight irregular
C-004 observations, 36 contact samples, 20 appearance landmarks, 24
measurement-contract references, and seven blocked disagreements.

All 36 contact samples are dark source-visible interface pixels with exact
native channel values ranging from 0 through 81. No invalid original Step 06
coordinate or invalid Step 06 completion-chain record propagates into Step 07
measurement values. Ten Step 07 contact coordinates equal older non-top Step
04 review endpoints; the overlaps remain disclosed, their current source
ownership was re-audited, and no independent original derivation claim is
made.

The approved bounded authority set therefore contains:

- the Step 07 contract as scope authority;
- both calibration records with all four Y/Z disagreements preserved;
- both source-linked measurement manifests through the Step 07R native-pixel
  recovery override;
- both measurement-contract sets;
- the seven-entry disagreement list with every block preserved;
- the evidence board and historical validation as `proof only`;
- only the original output-record headings explicitly named by Step 07R;
- the Step 07R audit manifest and approved output record.

The original Step 07 package remains quarantined as a whole. The original
output `Next Gate` section is superseded. The original Step 07-to-Step 08
handoff remains quarantined/superseded. Step 08 remains stopped; production
work, commit, and push remain unauthorized.

Step 07R output:
`steps/STEP_07R_RENEWED_DEPENDENCY_AUDIT_A01_OUTPUT_RECORD.md`.

Step 07R approved pre-classification checkpoint:
`Saved/ProjectRecovery/20260715-212847/`.

## Step 08R Approved Exact Top Evidence

Flamestrike approved the separate Core-reassessed Step 08R contract and its
visible output package on 2026-07-15.

Step 08R records four independent source-authored top calibrations:

- `159 px = 120 cm` for C-001 X;
- `208 px = 140 cm` for C-004 X;
- `94 px = 90 cm` for C-001 Y;
- `140 px = 110 cm` for C-004 Y.

All four calibration disagreements remain explicit. No unified scale was
selected, averaged, stretched, or created. All 48 authoritative Step 04R
top-contact observations were freshly reverified with zero RGB mismatches and
zero coordinate round-trip failures.

No fully enumerated, closed, annotation-excluded source-owned footprint was
established without inference. Therefore no filled footprint, closed
perimeter, exact pixel set, component or contact center, world conversion,
origin, pivot, centerline, transform, snap anchor, interpretation, or geometry
was created. Those results remain blocked.

Step 08R measurement, perimeter/center, sector, disagreement, and output
records are `authoritative` within their approved boundaries. The evidence
board and 37-check validation remain `proof only`.

Flamestrike also approved a future rectification direction using `120 x 90
cm` for C-001 and `140 x 110 cm` for C-004. That direction is not current
interpretation authority. Step 09 must audit the cross-view dataset first;
rectification then requires a separate approved interpretation contract.

Step 08R handoff:
`handoffs/STEP_08R_TO_STEP_09_HANDOFF.md`.

Approved pre-closeout checkpoint:
`Saved/ProjectRecovery/20260715-223831/`.

## Smallest Sufficient Recovery

1. Completed: approve a Step 04 top-contact evidence recovery contract.
2. Completed: re-audit and rebuild only the Step 04 top contact marks from the
   authoritative top panel at native resolution; do not alter semantic IDs or
   solve hidden contacts.
3. Completed: regenerate focused Step 04 validation and present the repaired top board in
   a visible desktop review.
4. Completed: audit Step 05-07 and approve the classification restoring Step
   05 while keeping Steps 06-07 quarantined.
5. Completed: approve and execute Step 06R, validate all 43 front/back
   contact samples, and approve the recovered contact evidence.
6. Completed: approve and execute Step 06Q, then approve the bounded recovered
   Step 06 authority while keeping the original package quarantined.
7. Completed: approve and execute Step 07R, then approve bounded recovered
   Step 07 measurement authority while keeping the original package and
   downstream handoff quarantined.
8. Completed: approve and execute the separate Core-reassessed Step 08R
   contract, then approve exact top calibration/contact evidence with all
   filled footprints and centers blocked.
9. Next separate gate after mandatory restart: present a Step 09 cross-view
   exact-dataset audit contract.

No original Step 06 or Step 07 whole-package restoration, Step 09 execution,
rectification, interpretation, geometry, or production work is authorized by
this status record.

## Approval Needed

No downstream execution is active. After dependency-complete A005-only
closeout and the mandatory restart, the next permitted presentation is a Step
09 cross-view exact-dataset audit contract only. Rectification remains pending
that audit and a separate interpretation approval.
