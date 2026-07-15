# Step 07 Contract - Left And Right Exact Measurement Contracts

Status: approved for execution

Artifact classification: `authoritative` for execution scope

Date: 2026-07-15

## Decision

Derive formula-linked left/right calibration, exact source-visible side
contours, per-view depth-profile centers, thickness stations, component
boundaries, exposed contact lines, and source-owned feature measurements.
Every measurement must link to exact source pixels and a declared formula.

## Governing Core Principle

Evidence-Bound Decision Rule, closed-world authorization, and strict
evidence-versus-interpretation separation. Source pixels and approved records
are authority. Missing correspondence, hidden construction, and conflicting
calibration remain blocked rather than being averaged, visually fitted, or
inferred.

## Authorizing Plan Section

`docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`,
Section 13, `Step 07 - Left And Right Exact Measurement Contracts`.

## Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Scope: the exact visible Step 07 contract presented after the Core resume
  handshake
- Exclusion: Step 07 output approval, Step 08, geometry, interpretation, and
  every action outside this contract

## Approved Inputs

- A005 charter, firewall, source lock, reset state, artifact index, and
  approval log;
- authoritative A02 PNG and exact scanline evidence;
- authoritative Step 03 left and right lossless panels and crop formulas;
- authoritative Step 04 component IDs `C-001` through `C-007`, discontinuous
  contacts `CL-001` through `CL-003`, occluded sectors `OS-001` through
  `OS-003`, and blocked unknowns `U-001` through `U-009`;
- authoritative Step 05 pixel convention, coordinate frame, left/right
  registration marks, correspondence rules, center-authority policies, and
  tolerances;
- authoritative Step 06 records only for established controls, status, and
  blockers, not for front/back coordinate or calibration reuse;
- prior evidence and validation only as `proof only`;
- generic measurement rules containing no legacy Cairn Stone constants.

## Allowed Files

Read-only authority files named above, `AGENTS.md`, the approved fresh-start
plan, and relevant generic measurement rules.

Scoped writable outputs:

- `steps/STEP_07_CONTRACT.md`;
- `manifests/STEP_07_LEFT_CALIBRATION_RECORD.json`;
- `manifests/STEP_07_RIGHT_CALIBRATION_RECORD.json`;
- `manifests/STEP_07_LEFT_MEASUREMENT_MANIFEST.json`;
- `manifests/STEP_07_RIGHT_MEASUREMENT_MANIFEST.json`;
- `manifests/STEP_07_LEFT_MEASUREMENT_CONTRACTS.json`;
- `manifests/STEP_07_RIGHT_MEASUREMENT_CONTRACTS.json`;
- `manifests/STEP_07_LEFT_RIGHT_DISAGREEMENT_LIST.json`;
- `evidence/STEP_07/SM_GIA_BloodAxeCairnstone_A005_STEP_07_LEFT_RIGHT_MEASUREMENT_EVIDENCE.png`;
- `steps/STEP_07_OUTPUT_RECORD.md`;
- `manifests/STEP_07_VALIDATION_MANIFEST.json`;
- `handoffs/STEP_07_TO_STEP_08_HANDOFF.md`;
- scoped updates to RESET_RESUME_STATE, ARTIFACT_INDEX, and APPROVAL_LOG;
- local-only checkpoints under `Saved/ProjectRecovery/`.

## Allowed Actions

- create the required pre-action checkpoint;
- verify every authoritative input identity and hash;
- calibrate left and right independently from the exact source-authored
  `220 cm`, `35 cm`, `90 cm`, and `110 cm` dimension endpoints;
- use `pixel_span = second_axis_endpoint - first_axis_endpoint` and
  `cm_per_px = declared_real_span_cm / pixel_span`;
- preserve every independent Y/Z calibration observation separately;
- record integer source pixels, ordered visible row-boundary samples,
  thickness stations, component-boundary observations, and exposed contacts;
- record left/right view-local depth-profile centers only when the declared
  `(x0 + x1 - 1) / 2` source-owned formula supports them;
- keep final centers, origin, pivot, centerline, transforms, cross-view
  pairing, and snap anchors blocked;
- preserve `C-005` as ambiguous in both side views;
- record visible `C-006` and `C-007` appearance landmarks without physical
  geometry or cross-view identity authority;
- preserve discontinuous `CL-*` observations without closing occluded sectors;
- create unfilled source-only marks and focused pass/fail evidence;
- open approval-ready artifacts in visible desktop windows;
- after separate output approval, checkpoint, commit, and push only scoped
  Step 07 tracked outputs.

## Blocked Actions And Files

- left/right averaging or visual thickness fitting;
- candidate fills, component masks, threshold-derived geometry authority,
  smoothing, or inferred contour closure;
- inferred backsides, hidden interfaces, or physical feature identity;
- calibration reuse between views, conflicting spans, or other panels;
- front, back, top, or perspective measurement;
- physical pixel pairing between left and right;
- old crop/formula constants, legacy scripts, or A001-A004 data;
- treating annotation endpoints as object boundaries;
- final component centers, origin, pivot, centerline, transforms, snap anchors,
  or geometry authority;
- geometry previews, DCC, texture, UV, FBX, Unreal, collision, LOD, render, or
  production-root work;
- modifying approved sources or panels;
- starting Step 08;
- staging or committing unrelated changes.

## Expected Outputs

- independent left and right calibration records;
- left and right measurement manifests;
- formula-linked left and right feature-measurement contracts;
- explicit left/right disagreement list;
- one unfilled source-only measurement review board;
- focused validation manifest and output record;
- restart-safe Step 07-to-Step 08 handoff.

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
- no calibration or measurement is averaged or visually thickness-fitted;
- unresolved disagreement remains explicitly blocked;
- `C-005` remains ambiguous in both side views;
- `CL-001` through `CL-003` remain discontinuous and stop at occlusion;
- review marks remain unfilled and source pixels remain unchanged;
- no interpretation, geometry, production root, legacy access, or unrelated
  staged change occurs;
- Flamestrike separately approves or rejects the completed output.

## Visible Review

Before output approval, automatically open the untouched left and right
panels, measurement evidence board, both calibration records, both measurement
manifests and contract sets, disagreement list, validation manifest, and Step
07 output record.

## Artifact Status

Before output approval, measurement records are `candidate`; evidence and
validation are `proof only`. After separate Flamestrike approval, only the
source-owned side-view observations accepted in that decision become
`authoritative` for their declared views and features. Disagreements and
hidden construction remain blocked. Failed or rejected outputs become
`invalid` or `quarantined`; existing authority remains unchanged.

## Stop Conditions

Source or hash mismatch; undeclared selection method; formula-free
measurement; inference-dependent boundary; attempted closure through
occlusion; calibration disagreement requiring a selected value; legacy-data
need; candidate fill; visual thickness fitting; or unrelated staged change.
A preserved disagreement may remain blocked while non-conflicting source
evidence is completed.

## Smallest Sufficient Change

Create only the left/right calibration, exact pixel measurement,
disagreement, validation, and unfilled review records needed for Flamestrike
to approve, reject, or mark the Step 07 result blocked.

## Context And Checkpoints

Context demand: moderate; one source-measurement/evidence/validation/review
pass with no geometry or render loop.

Pre-action checkpoint:

- `Saved/ProjectRecovery/20260715-152620/`
