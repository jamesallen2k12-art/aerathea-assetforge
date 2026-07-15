# Step 05 Output Record

Status: Step 05 complete; approved pending scoped closeout

Artifact classification: `authoritative`

Date: 2026-07-15

## Assigned Goal

Lock the measurement convention, world axes, origin and pivot policies,
center-authority types, orientation pixels, view-correspondence IDs,
registration rules, and later-audit tolerances without measuring or deriving
geometry.

## Approved Decision

The approved output locks one exact image-coordinate convention, one right-handed
asset frame, explicit future origin/pivot/center authority types, 46 exact
source-authored registration marks, source-proven semantic correspondence IDs,
and zero-error source-coordinate audit rules.

It does not claim pixel-to-pixel cross-view identity for irregular corners,
masonry divisions, small peripheral forms, surface motifs, or contact lines.
Those questions remain blocked rather than being converted into geometry or
registration authority.

## Pixel Convention

- point indexing: zero-based integer pixel centers;
- image origin: center of the top-left pixel is `(0, 0)`;
- image axes: `+x` right, `+y` down;
- span convention: exclusive edge-to-edge half-open bounds;
- width and height: `x1 - x0`, `y1 - y0`;
- mixed, inclusive, and center-to-center span conventions: blocked for this
  measurement sequence;
- resampling: none.

Full-source and panel-local coordinates use:

- `x_local = x_full - crop_x0`;
- `y_local = y_full - crop_y0`;
- `x_full = x_local + crop_x0`;
- `y_full = y_local + crop_y0`.

All 46 candidate marks round-trip exactly with `0 px` error.

## Coordinate Frame

- handedness: right-handed;
- world up: `+Z`;
- forward/front: `-Y`;
- back: `+Y`;
- left: `-X`;
- right: `+X`;
- top: `+Z`.

Panel mappings:

| Panel | Image +x | Image +y | Panel normal owner |
|---|---|---|---|
| Front | `+X` | `-Z` | `-Y` |
| Back | `-X` | `-Z` | `+Y` |
| Left | `-Y` | `-Z` | `-X` |
| Right | `+Y` | `-Z` | `+X` |
| Top | `+X` | `-Y` | `+Z` |
| Perspective | uncalibrated | uncalibrated | none metric |

Panel normal owners establish only the orthographic view frame. They do not
solve individual irregular facet normals.

## Origin, Pivot, Centerline, And Rotation Policy

The future numeric origin is the intersection of the Step 08-approved `C-004`
filled outer-footprint center with the approved `Z=0` ground-contact plane.
The static-mesh pivot equals that origin. The vertical centerline passes
through that center and is parallel to `+Z`.

No numeric center, origin, pivot, or centerline was created. No bounding-box
center or raw color-density center is alignment authority. No component yaw,
pitch, roll, offset, or inherited transform is authorized by Step 05.

Center-authority types:

- `C-001`: filled source-owned outer-footprint center, pending Step 08;
- `C-002`: visible-annulus center with separate inner and outer perimeters,
  pending Step 08;
- `C-003`: visible-annulus center with separate inner and outer perimeters,
  pending Step 08;
- `C-004`: filled source-owned outer-footprint center and future origin/pivot
  authority, pending Step 08;
- `C-005` through `C-007`: no alignment center while physical identity remains
  ambiguous.

The `CL-001` through `CL-003` center policy requires paired measured contact
perimeter centers in later approved measurement steps. No numeric contact
center or snap anchor exists.

## Registration Marks And Correspondence IDs

The orientation manifest contains 46 exact source-coordinate records:

- six source-authored panel-identity marks;
- sixteen source-authored height-station arrow endpoints;
- twelve source-authored X-span endpoints;
- twelve source-authored Y-span endpoints.

Every record includes panel-local and full-source coordinates, source identity,
world meaning, panel normal owner, semantic correspondence ID, exclusion from
texture/mesh/render/export, and a `0 px` source-coordinate tolerance.

The marks reference source-authored labels and dimension-arrow endpoints. They
prove view identity or the semantic role of an authored span/station. They do
not claim that annotation endpoints are geometry boundaries or that pixels in
different panels occupy one metric space.

The authoritative Step 04 `CL-001` through `CL-003` semantic relations are
preserved. Their pixel-to-pixel pairing and snap anchors remain blocked by
`U-007` and `U-008`.

## Blocked Physical Correspondence

Seven categories remain explicitly blocked:

1. `C-001` irregular physical corners or exterior seam pixels across views;
2. individual `C-002` and `C-003` masonry divisions across views;
3. individual `C-004` peripheral small-form identity across views;
4. `C-005` motif correspondence outside source-proven front/top observations;
5. individual `C-006` and `C-007` line-feature identity across views;
6. individual irregular physical-facet normal owners;
7. numeric component/contact centers, origin, pivot, centerline, calibration,
   and transforms.

Step 04 unknowns `U-001` through `U-009` remain unresolved. Step 05 provides no
interpretation authority.

## Tolerance Policy

- source file and pixel hash mismatch allowed: none;
- source-coordinate record tolerance: `0 px`;
- full-source/panel-local round-trip tolerance: `0 px`;
- evidence source-tile changed pixels allowed: `0`;
- evidence source-tile maximum RGB delta allowed: `0`;
- unapproved axis or component rotation tolerance: `0 degrees`;
- cross-view pixel-distance tolerance: not defined before calibration;
- world translation/rotation tolerances: blocked until Steps 06-09;
- disagreement rule: stop, preserve both observations, and do not average,
  shift, rotate, or select a convenient center.

## Evidence Produced

Registration evidence board:

`evidence/STEP_05/SM_GIA_BloodAxeCairnstone_A005_STEP_05_REGISTRATION_EVIDENCE.png`

The board contains paired exact source and marked copies for all six panels.
Only the right copies contain thin crosses and text labels. The left source
tiles are pixel-exact. No fill, mask, closed candidate contour, component
center, calibration, or geometry preview is present.

## Focused Validation Result

- aggregate technical result: pass;
- validators: `22` passed, `0` failed;
- orientation marks: `46`;
- blocked physical-correspondence categories: `7`;
- evidence boards: `1`;
- all six left source tiles pixel-exact: true;
- aggregate changed source-tile pixels: `0`;
- maximum RGB delta: `0`;
- full/local coordinate round-trip error: `0 px`;
- Step 04 review coordinates reused: none;
- perspective metric use: none;
- A001-A004 asset-specific access: false;
- interpretation or calibration introduced: false;
- A005 production roots: absent;
- unrelated staged files: none.

Validation manifest:

`manifests/STEP_05_VALIDATION_MANIFEST.json`

## Assumptions And Interpretations

No interpretation was introduced. Source-authored dimension labels establish
semantic station/span identity only. They are not treated as measured object
boundaries. No physical cross-view pixel identity is inferred from visual
similarity.

The future `C-004` filled outer-footprint center is an approved center-authority
type and origin policy, not a numeric result. Its value remains blocked pending
Step 08.

## Access Declaration

- no A001-A004 asset-specific artifact was opened or used;
- no Step 04 component/contact review coordinate was reused as registration
  authority;
- no approved source or panel was modified;
- no component mask, fill, contour, calibration, measurement, geometry,
  texture, export, or Unreal artifact was created;
- no A005 production root was created;
- no unrelated file was staged.

## Artifact Status

- Step 05 contract: `authoritative` for execution scope;
- pixel/coordinate-frame record: `authoritative`;
- orientation-registration manifest: `authoritative`;
- this output record: `authoritative`;
- evidence board: `proof only`;
- validation manifest: `proof only`;
- blocked correspondence: unresolved and non-authoritative as a solution;
- interpretation authority: none;
- Step 06 authority: none.

## Checkpoint

- Pre-action checkpoint: `Saved/ProjectRecovery/20260715-134936/`.
- Validated-candidate review checkpoint:
  `Saved/ProjectRecovery/20260715-140730/`.

## Output Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Visible review: untouched authoritative panels, registration evidence board,
  complete pixel/coordinate-frame record, orientation-registration manifest,
  blocked-correspondence list, validation result, and this output record
- Result: pass and authority promotion
- Approved pre-closeout checkpoint:
  `Saved/ProjectRecovery/20260715-141013/`
- Exclusion: blocked physical correspondence, numeric measurement,
  calibration, interpretation, Step 06, and production work remain
  unauthorized

## Next Gate

Complete scoped Step 05 closeout, commit, push, and mandatory restart. The next
agent may present a Step 06 contract only. Step 06 remains unauthorized.

## Commit And Push

- Scoped content commit: `5af0d91`
- Commit message: `Lock BloodAxe Cairn Stone A005 registration frame`
- Push: success; `assetforge/main` advanced from `19ebaf1` to `5af0d91`
- Scoped files: ten A005 Step 05 records and evidence files
- Unrelated changes: preserved and unstaged
