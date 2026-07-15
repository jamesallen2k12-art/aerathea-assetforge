# Step 06 Contract - Front And Back Exact Measurement Contracts

Status: approved for execution

Artifact classification: `authoritative` for execution scope

Date: 2026-07-15

## Decision

Derive formula-linked front/back calibration, exact source-visible contours,
per-view profile-center observations, height stations, component boundaries,
exposed contact lines, and source-owned feature measurements. Every
measurement must link to exact source pixels and a declared formula.

## Governing Core Principle

Evidence-Bound Decision Rule, closed-world authorization, and strict
evidence-versus-interpretation separation. Source pixels and approved records
are authority. Missing correspondence, hidden construction, and conflicting
calibration remain blocked rather than being averaged or inferred.

## Authorizing Plan Section

`docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`,
Section 13, `Step 06 - Front And Back Exact Measurement Contracts`.

## Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Scope: the exact visible Step 06 contract presented after the Core resume
  handshake
- Exclusion: Step 06 output approval, Step 07, geometry, interpretation, and
  every action outside this contract

## Approved Inputs

- A005 charter, firewall, source lock, reset state, artifact index, and
  approval log;
- authoritative A02 PNG and exact scanline evidence;
- authoritative Step 03 front and back lossless panels and crop formulas;
- authoritative Step 04 component IDs `C-001` through `C-007`, discontinuous
  contacts `CL-001` through `CL-003`, occluded sectors `OS-001` through
  `OS-003`, and blocked unknowns `U-001` through `U-009`;
- authoritative Step 05 pixel convention, coordinate frame, registration
  marks, correspondence rules, center-authority policies, and tolerances;
- Step 03-05 evidence and validation only as `proof only`;
- generic measurement rules containing no legacy Cairn Stone constants.

## Allowed Files

Read-only authority files named above, `AGENTS.md`, the approved fresh-start
plan, and relevant generic measurement rules.

Scoped writable outputs:

- `steps/STEP_06_CONTRACT.md`;
- `manifests/STEP_06_FRONT_CALIBRATION_RECORD.json`;
- `manifests/STEP_06_BACK_CALIBRATION_RECORD.json`;
- `manifests/STEP_06_FRONT_MEASUREMENT_MANIFEST.json`;
- `manifests/STEP_06_BACK_MEASUREMENT_MANIFEST.json`;
- `manifests/STEP_06_FRONT_MEASUREMENT_CONTRACTS.json`;
- `manifests/STEP_06_BACK_MEASUREMENT_CONTRACTS.json`;
- `manifests/STEP_06_FRONT_BACK_DISAGREEMENT_LIST.json`;
- `evidence/STEP_06/SM_GIA_BloodAxeCairnstone_A005_STEP_06_FRONT_BACK_MEASUREMENT_EVIDENCE.png`;
- `steps/STEP_06_OUTPUT_RECORD.md`;
- `manifests/STEP_06_VALIDATION_MANIFEST.json`;
- `handoffs/STEP_06_TO_STEP_07_HANDOFF.md`;
- scoped updates to RESET_RESUME_STATE, ARTIFACT_INDEX, and APPROVAL_LOG;
- local-only checkpoints under `Saved/ProjectRecovery/`.

## Allowed Actions

- create the required pre-action checkpoint;
- verify every authoritative input identity and hash;
- calibrate front and back independently from exact source-authored dimension
  endpoints;
- use `pixel_span = upper_edge - lower_edge` and
  `cm_per_px = declared_real_span_cm / pixel_span`;
- preserve every independent X/Z calibration observation separately;
- record integer source pixels, ordered visible row-boundary samples, height
  stations, component-boundary observations, and exposed contact samples;
- record front/back X/Z profile-center observations only when a declared
  source-owned pixel formula supports them;
- keep final footprint centers, origin, pivot, centerline, transforms, and snap
  anchors blocked pending later steps;
- measure `C-005` only where directly visible and keep back-view identity
  ambiguous;
- measure visible `C-006` and `C-007` appearance features without
  reclassifying them as physical geometry;
- preserve discontinuous `CL-*` observations without closing occluded sectors;
- create unfilled source-only measurement marks and pass/fail evidence;
- run focused deterministic validation;
- open approval-ready artifacts in visible desktop windows;
- after separate output approval, checkpoint, commit, and push only scoped
  Step 06 tracked outputs.

## Blocked Actions And Files

- candidate fills, component masks, threshold-derived geometry authority,
  smoothing, or inferred contour closure;
- inferred backsides, hidden interfaces, or physical feature identity;
- average or blended front/back dimensions;
- calibration reuse between views or between conflicting source spans;
- left, right, top, or perspective measurement;
- old crop/formula constants, legacy scripts, or A001-A004 data;
- treating annotation endpoints as object boundaries;
- final component centers, origin, pivot, centerline, transforms, snap anchors,
  or geometry authority;
- geometry previews, DCC, texture, UV, FBX, Unreal, collision, LOD, render, or
  production-root work;
- modifying approved sources or panels;
- starting Step 07;
- staging or committing unrelated changes.

## Expected Outputs

- independent front and back calibration records;
- front and back measurement manifests;
- formula-linked front and back feature-measurement contracts;
- explicit front/back disagreement list;
- one unfilled source-only measurement review board;
- focused validation manifest and output record;
- restart-safe Step 06-to-Step 07 handoff.

## Validators And Pass Conditions

- all source and panel hashes remain unchanged;
- coordinates are integer-valued, in bounds, and round-trip between full-source
  and panel-local spaces with `0 px` error;
- each calibration records source span, real span, formula, axis, view, and
  exact result;
- each measurement records feature/component ID, source view, exact source
  pixels, selection method, formula ID, pixel value, centimeter value or
  blocked status, visibility, and tolerance;
- no inferred measurement is presented as visible evidence;
- no calibration or measurement is averaged;
- unresolved disagreement remains explicitly blocked;
- `C-005` remains ambiguous on the back;
- `CL-001` through `CL-003` remain discontinuous and stop at occlusion;
- review marks remain unfilled and source pixels remain unchanged;
- no interpretation, geometry, production root, legacy access, or unrelated
  staged change occurs;
- Flamestrike separately approves or rejects the completed output.

## Visible Review

Before output approval, automatically open the untouched front and back panels,
the measurement evidence board, both calibration records, both measurement
manifests and contract sets, the disagreement list, validation manifest, and
Step 06 output record.

## Artifact Status

Before output approval, measurement records are `candidate`; evidence and
validation are `proof only`. After separate Flamestrike approval, only the
source-owned front/back calibration observations and measurements accepted in
that decision become `authoritative` for their declared views and features.
Disagreements and hidden construction remain blocked. Step 06 approval does not
authorize Step 07 or production work.

## Stop Conditions

Source or hash mismatch; undeclared selection method; formula-free
measurement; boundary requiring inference; attempted closure through
occlusion; calibration or cross-view disagreement; legacy-data need;
candidate fill; or unrelated staged change. A preserved disagreement does not
receive a guessed solution and may remain blocked while non-conflicting source
evidence is completed.

## Smallest Sufficient Change

Create only the front/back calibration, exact pixel measurement,
disagreement, validation, and unfilled review records needed for Flamestrike
to approve, reject, or mark the Step 06 result blocked.

## Context And Checkpoints

Context demand: moderate; one source-measurement/evidence/validation/review
pass with no geometry or render loop.

Pre-action checkpoint:

- `Saved/ProjectRecovery/20260715-142939/`
