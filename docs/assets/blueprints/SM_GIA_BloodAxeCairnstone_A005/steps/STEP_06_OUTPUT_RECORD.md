# Step 06 Output Record

Status: Step 06 complete; approved pending scoped closeout

Artifact classification: `authoritative`

Date: 2026-07-15

## Assigned Goal

Derive formula-linked calibration, visible contours, per-view profile-center
observations, height stations, component boundaries, exposed contact lines,
and source-owned feature measurements from only the authoritative front and
back panels. Preserve all unresolved disagreement without averaging or
interpretation.

## Candidate Decision

The exact source pixels support a complete front/back pixel-space measurement
record and the four matching printed dimensions:

- overall height: `220 cm`;
- base height: `35 cm`;
- C-001 maximum width: `120 cm`;
- C-004 footprint width: `140 cm`.

They do not support one consolidated X or Z centimeters-per-pixel scale in
either view. Each independent printed span produces a different exact scale.
All four within-view conflicts are preserved as blocked. No scale was selected
or averaged, so derived contour/contact world measurements remain blocked.

## Exact Calibration Observations

Front:

| Axis / source span | Pixels | Real span | Exact cm/px | Status |
|---|---:|---:|---:|---|
| Z overall height | 375 | 220 cm | `44/75` | blocked against base-height scale |
| Z base height | 62 | 35 cm | `35/62` | blocked against overall-height scale |
| X C-001 width | 230 | 120 cm | `12/23` | blocked against C-004 scale |
| X C-004 footprint | 290 | 140 cm | `14/29` | blocked against C-001 scale |

Back:

| Axis / source span | Pixels | Real span | Exact cm/px | Status |
|---|---:|---:|---:|---|
| Z overall height | 275 | 220 cm | `4/5` | blocked against base-height scale |
| Z base height | 52 | 35 cm | `35/52` | blocked against overall-height scale |
| X C-001 width | 189 | 120 cm | `40/63` | blocked against C-004 scale |
| X C-004 footprint | 245 | 140 cm | `4/7` | blocked against C-001 scale |

Annotation endpoints remain calibration evidence only. They were not promoted
to geometry boundaries.

## Pixel-Space Measurements

- Front visible row samples: `13` across C-001, C-002, and C-003.
- Back visible row samples: `13` across C-001, C-002, and C-003.
- Irregular C-004 outer-edge observations: `4` per view; intervening pixels
  and gaps are not claimed as C-004 ownership.
- Exposed contact sample pixels: `21` front and `22` back across CL-001,
  CL-002, and CL-003.
- Source appearance landmarks: `22` front and `10` back.
- Feature measurement contracts: `24`.
- Disagreement records: `7`.

Every retained coordinate is integer-valued, in bounds, and source-linked.
Each row distance uses `width = x1 - x0`; each row profile-center observation
uses `(x0 + x1 - 1) / 2`. These per-view profile centers are measurement
observations only and are not final component centers or alignment authority.

## Component And Contact Boundary

- C-001 through C-003 have exact visible outer-edge row samples only.
- C-004 remains an irregular discontinuous layer; no filled footprint or
  interior ownership was created.
- CL-001 through CL-003 contain only exposed open sample sequences.
- OS-001 through OS-003 remain occluded; no hidden interface was closed.
- C-005 is visible on the front and remains ambiguous on the back; absence is
  not proven.
- C-006 and C-007 landmarks remain appearance evidence without physical
  geometry or cross-view identity authority.

## Blocked Disagreement

Seven entries are preserved in
`manifests/STEP_06_FRONT_BACK_DISAGREEMENT_LIST.json`:

1. front Z calibration;
2. front X calibration;
3. back Z calibration;
4. back X calibration;
5. front/back visible-profile comparison without a common calibration or
   physical pixel pairing;
6. C-005 front/back identity;
7. CL-001 through CL-003 physical pixel pairing and hidden closure.

No average, mean, scale selection, shift, stretch, rotation, or inferred
correspondence was used.

## Evidence Produced

`evidence/STEP_06/SM_GIA_BloodAxeCairnstone_A005_STEP_06_FRONT_BACK_MEASUREMENT_EVIDENCE.png`

The board pairs untouched front/back panels with mark-only copies. Green marks
show calibration endpoints, cyan marks show one-pixel row distances and
irregular edge points, yellow crosses show exposed contact samples, and
magenta crosses show appearance landmarks. It contains no mask, fill, closed
candidate contour, inferred backside, center solution, or geometry preview.

Both source tiles are pixel-exact with `0` changed pixels and `0` maximum RGB
delta.

## Focused Validation Result

- aggregate technical result: pass with blocked disagreements preserved;
- validators: `28` passed, `0` failed;
- JSON outputs parsed: `7`;
- all recorded coordinates in bounds: true;
- all row-span and center formulas: pass;
- all calibration formulas: pass;
- contract references: pass;
- consolidated X/Z scales: none;
- derived contour world measurements: blocked;
- source or panel mutation: none;
- candidate fill, interpretation, or geometry: none;
- A001-A004 asset-specific access: false;
- A005 production roots: absent;
- unrelated staged files: none.

Validation manifest:

`manifests/STEP_06_VALIDATION_MANIFEST.json`

## Assumptions And Interpretations

No interpretation was introduced. Native-pixel diagnostic scans were used only
to locate possible review coordinates; they were not accepted as authority.
Every retained coordinate was audited against the source panel. Row marks are
distance samples between visible edge pixels, not masks or candidate fills.

The candidate does not assume that front/back irregular pixels correspond to
the same physical corners, stones, seams, or contacts.

## Access Declaration

- no A001-A004 asset-specific artifact was opened or used;
- no left, right, top, or perspective measurement was performed;
- no approved source or panel was modified;
- no filled mask, inferred contour, hidden closure, geometry, texture, export,
  or Unreal artifact was created;
- no A005 production root was created;
- no unrelated file was staged.

## Artifact Status

- Step 06 contract: `authoritative` for execution scope;
- calibration records: `candidate`;
- measurement manifests and contract sets: `candidate`;
- disagreement list: `candidate` record of blocked questions;
- evidence board and validation manifest: `proof only`;
- derived world-space contour/contact measurements: blocked;
- interpretation and geometry authority: none;
- Step 07 authority: none.

## Checkpoint

- Pre-action checkpoint: `Saved/ProjectRecovery/20260715-142939/`.

## Output Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Visible review: untouched front/back panels, exact unfilled measurement
  evidence, calibration records, measurement manifests and contracts,
  disagreement list, validation result, and this output record
- Result: source-linked front/back pixel measurements and measurement
  contracts promoted to `authoritative`
- Preserved blocked scope: all seven disagreement entries, consolidated X/Z
  scales, derived contour/contact world measurements, hidden contact closure,
  final centers, physical cross-view identity, interpretation, geometry, and
  production work
- Approved pre-closeout checkpoint:
  `Saved/ProjectRecovery/20260715-150643/`

## Next Gate

Complete scoped Step 06 closeout, commit, push, and mandatory restart. The next
agent may present a Step 07 contract only. Step 07 remains unauthorized.
