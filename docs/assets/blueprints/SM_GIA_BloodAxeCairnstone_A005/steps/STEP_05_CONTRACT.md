# Step 05 Contract - Pixel Convention, Coordinate Frame, And Registration Lock

Status: approved and executed through output review

Artifact classification: `authoritative`

Date: 2026-07-15

## Decision

Lock the measurement convention, world axes, origin and pivot policies,
center-authority types, orientation pixels, view-correspondence IDs,
registration rules, and later-audit tolerances without measuring or deriving
geometry.

## Governing Core Principle

Evidence-Bound Decision Rule, closed-world authorization, and strict
evidence-versus-interpretation separation. Every coordinate and correspondence
must be source-owned or explicitly classified as blocked. Similarity,
convenience, legacy data, and visual judgment are not registration authority.

## Authorizing Plan Section

`docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`,
Section 13, `Step 05 - Pixel Convention, Coordinate Frame, And Registration
Lock`.

## Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Scope: this exact Step 05 contract only
- Exclusion: Step 05 output approval, Step 06, and every action outside this
  contract

## Approved Inputs

- A005 charter, firewall, source lock, reset state, artifact index, and
  approval log;
- authoritative A02 PNG and exact scanline records;
- authoritative Step 03 crop manifest and six lossless panels;
- authoritative Step 04 component inventory, contact IDs, occluded sectors,
  blocked unknowns, output record, and handoff;
- Step 04 evidence boards only as `proof only`; their review-mark coordinates
  cannot become registration authority;
- generic AetherForge pixel-convention, coordinate-frame, center-authority,
  and registration rules containing no legacy Cairn Stone constants.

## Allowed Files

Read-only authority files named above, plus:

- `AGENTS.md`;
- the approved fresh-start plan;
- relevant generic sections of `AETHERFORGE_BLUEPRINTS.md`.

Scoped writable outputs:

- `steps/STEP_05_CONTRACT.md`;
- `manifests/STEP_05_PIXEL_COORDINATE_FRAME_RECORD.json`;
- `manifests/STEP_05_ORIENTATION_REGISTRATION_MANIFEST.json`;
- `evidence/STEP_05/SM_GIA_BloodAxeCairnstone_A005_STEP_05_REGISTRATION_EVIDENCE.png`;
- `steps/STEP_05_OUTPUT_RECORD.md`;
- `manifests/STEP_05_VALIDATION_MANIFEST.json`;
- `handoffs/STEP_05_TO_STEP_06_HANDOFF.md`;
- scoped updates to RESET_RESUME_STATE, ARTIFACT_INDEX, and APPROVAL_LOG;
- local-only checkpoints under `Saved/ProjectRecovery/`.

## Allowed Actions

- create the required pre-action checkpoint after contract approval;
- verify all authoritative input identities and hashes;
- select and declare one pixel-span convention for this measurement sequence;
- record exact formulas converting full-source coordinates to approved
  crop-local coordinates and back;
- declare world up, forward, front, back, left, right, top, centerline, origin
  policy, pivot policy, and per-component rotation-authority policy;
- declare the permitted center-authority type for each applicable component or
  registration role;
- keep bounding-box and raw color-density centers diagnostic unless explicitly
  proven suitable;
- record fresh exact source-pixel orientation marks;
- assign fresh neutral surface, edge, corner, height-station, contact,
  normal-owner, and cross-view correspondence IDs only where the source proves
  the relationship;
- reference authoritative `C-*` and `CL-*` IDs without altering their Step 04
  meaning;
- record unprovable correspondences and centers as blocked rather than
  inventing them;
- declare later-audit tolerance classes and their formulas or authority basis;
- create an unfilled registration evidence board without modifying source
  pixels;
- run focused validation;
- open all approval-ready review artifacts automatically in visible desktop
  windows;
- after separate output approval, checkpoint, commit, and push only scoped
  Step 05 tracked outputs.

## Blocked Actions And Files

- any A001-A004 asset-specific access or inherited coordinates, centers,
  formulas, registration, scripts, or outputs;
- reusing Step 04 review-mark coordinates as registration measurements;
- moving, rotating, scaling, centering, cropping for geometry, or assembling
  any component;
- selecting a bounding-box center for an irregular component;
- component masks, filled contours, threshold cleanup, smoothing, inferred
  boundaries, or geometry-owned overlays;
- per-view centimeters-per-pixel calibration or feature measurement owned by
  Steps 06-08;
- geometric registration transforms or resolving disagreement by averaging
  views;
- treating perspective as metric authority;
- resolving hidden construction, physical separability, material identity, or
  other Step 04 blocked unknowns through inference;
- geometry, DCC, texture, UV, FBX, Unreal, collision, LOD, render, or
  production-root work;
- modifying the source image or approved Step 03/04 artifacts;
- starting Step 06;
- staging or committing unrelated worktree changes.

## Expected Outputs

- one approved pixel-convention and coordinate-frame record;
- one orientation and registration manifest containing exact pixel
  coordinates, world meanings, source/overlay status, correspondence IDs,
  normal owners, contact references, and tolerance fields;
- one source-only, unfilled registration evidence board;
- explicit blocked entries wherever exact registration cannot be established;
- focused validation manifest and Step 05 output record;
- restart-safe Step 05-to-Step 06 handoff.

## Validators And Pass Conditions

- all approved input hashes remain unchanged;
- one pixel convention is declared and used consistently;
- full-source/crop-local coordinate formulas round-trip exactly;
- every recorded pixel is integer-valued, in bounds, and traceable to an
  authoritative source panel;
- every orientation or correspondence record includes its source, view,
  coordinate, world meaning, source/overlay classification, shipping
  exclusion, and applicable paired ID, height station, normal owner, contact
  ID, and tolerance;
- no uncertain correspondence is presented as exact;
- every center role has an approved authority type or an explicit blocked
  status; irregular components do not use bounding-box centers;
- perspective remains corroboration only;
- evidence marks are unfilled and do not alter the exact source tile;
- no measurement mask, calibration result, interpretation, geometry,
  production root, legacy access, or unrelated change occurs;
- focused JSON, hash, coordinate-bound, pixel-exactness, scoped-diff, and
  staged-file audits pass;
- Flamestrike visibly approves the convention and registration authority or
  marks Step 05 blocked.

## Visible Review

Before output approval, automatically open:

- the untouched authoritative panels;
- the registration evidence board;
- the complete pixel/coordinate record;
- the orientation-registration manifest;
- the blocked-correspondence list;
- the Step 05 output record.

## Artifact Status

- before output approval: records are `candidate`; evidence and validation are
  `proof only`;
- after separate Flamestrike output approval: the convention, coordinate
  frame, registration rules, approved marks, correspondence IDs, and tolerance
  declarations become `authoritative`; evidence remains `proof only`;
- honest unresolved entries remain blocked and gain no interpretation
  authority;
- on prohibited access or interpretation drift: affected outputs become
  `quarantined` and Core Recovery begins;
- Step 05 approval does not authorize Step 06.

## Stop Conditions

Source or hash mismatch; authority conflict; legacy access; a required center,
orientation mark, correspondence, or tolerance that cannot be justified
without measurement or inference; cross-view disagreement beyond the declared
tolerance; any need for a filled mask, hidden boundary, geometric transform,
or production artifact; evidence marks exceeding source-owned regions; or
unrelated staged changes.

Unprovable physical seam, corner, component-center, or pixel-to-pixel
cross-view correspondence does not receive a guessed value. It is recorded as
blocked. Step 05 stops as blocked only if the registration policy itself cannot
be made complete without inventing authority.

## Smallest Sufficient Change

Create only the convention, coordinate-frame, center-authority, orientation,
correspondence, tolerance, validation, and unfilled review records needed for
Flamestrike to approve or block registration authority.

## Context And Checkpoints

Context demand: moderate; one records/evidence/validation/review pass, with no
build or render loop.

Checkpoint points:

- after contract approval and before source access;
- after candidate validation and before visible review;
- after output approval and before scoped commit/push;
- after successful closeout or failure.

Pre-action checkpoint:

- `Saved/ProjectRecovery/20260715-134936/`
