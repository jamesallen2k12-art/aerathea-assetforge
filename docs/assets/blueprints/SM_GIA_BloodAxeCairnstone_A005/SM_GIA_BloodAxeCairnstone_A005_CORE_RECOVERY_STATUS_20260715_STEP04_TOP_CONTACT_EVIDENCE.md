# SM_GIA_BloodAxeCairnstone_A005 Core Recovery Status

Status: `Step 04R approved and pushed; mandatory restart`

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

The latest Core-valid recovery state adds the Flamestrike-approved Step 04R
recovered semantic inventory and 48 exact top-contact observations. This does
not restore the original Step 04 completion proof or any Step 05-07 authority.

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
- Step 05-07 records are `quarantined/suspended authority pending dependency
  audit`; they are not declared invalid. Their records state that Step 04
  review coordinates were not reused, and Step 06-07 performed independent
  source-linked measurements, but this must be confirmed before restoration.
- The approved Step 08 contract is `authoritative as the approved execution
  boundary but suspended by Core Recovery`; Step 08 has no output authority.

## Partial Step 08 Artifacts

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

## Smallest Sufficient Recovery

1. Completed: approve a Step 04 top-contact evidence recovery contract.
2. Completed: re-audit and rebuild only the Step 04 top contact marks from the
   authoritative top panel at native resolution; do not alter semantic IDs or
   solve hidden contacts.
3. Completed: regenerate focused Step 04 validation and present the repaired top board in
   a visible desktop review.
4. Next separate gate: audit
   Step 05-07 for propagation and explicitly restore, quarantine, or reject
   each downstream authority set.
5. Create a restart handoff. Step 08 may resume only after the recovered
   authority chain and a renewed Step 08 authorization are explicit.

No Step 05-07 audit, restoration, or Step 08 work is authorized by this status
record.

## Approval Needed

After the mandatory restart and Core resume handshake, the next agent may
present a Step 05-07 dependency-audit contract only. Flamestrike approval is
required before that audit begins. Step 08 remains suspended.
