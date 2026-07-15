# Step 07 Output Record

Status: Step 07 complete; approved pending scoped closeout

Artifact classification: `authoritative`

Date: 2026-07-15

## Assigned Goal

Derive formula-linked calibration, exact side contours, per-view depth-profile
centers, thickness stations, component boundaries, exposed contact lines, and
source-owned feature measurements from only the authoritative left and right
panels. Preserve all unresolved disagreement without averaging, visual
thickness fitting, or interpretation.

## Candidate Decision

The exact source pixels support a complete left/right pixel-space measurement
record and the four matching printed dimensions:

- overall height: `220 cm`;
- base height: `35 cm`;
- C-001 maximum depth: `90 cm`;
- C-004 footprint depth: `110 cm`.

They do not support one consolidated Y or Z centimeters-per-pixel scale in
either view. Each independent printed span produces a different exact scale.
All four within-view conflicts are preserved as blocked. No scale was selected
or averaged, and no visual thickness fitting was performed, so derived
contour/contact world measurements remain blocked.

## Exact Calibration Observations

Left:

| Axis / source span | Pixels | Real span | Exact cm/px | Status |
|---|---:|---:|---:|---|
| Z overall height | 277 | 220 cm | `220/277` | blocked against base-height scale |
| Z base height | 52 | 35 cm | `35/52` | blocked against overall-height scale |
| Y C-001 depth | 168 | 90 cm | `15/28` | blocked against C-004 scale |
| Y C-004 footprint | 225 | 110 cm | `22/45` | blocked against C-001 scale |

Right:

| Axis / source span | Pixels | Real span | Exact cm/px | Status |
|---|---:|---:|---:|---|
| Z overall height | 254 | 220 cm | `110/127` | blocked against base-height scale |
| Z base height | 47 | 35 cm | `35/47` | blocked against overall-height scale |
| Y C-001 depth | 144 | 90 cm | `5/8` | blocked against C-004 scale |
| Y C-004 footprint | 193 | 110 cm | `110/193` | blocked against C-001 scale |

Annotation endpoints remain calibration evidence only. They were not promoted
to geometry boundaries.

## Pixel-Space Measurements

- Left visible side-row samples: `13` across C-001, C-002, and C-003.
- Right visible side-row samples: `13` across C-001, C-002, and C-003.
- Irregular C-004 outer-edge observations: `4` per view; intervening pixels
  and gaps are not claimed as C-004 ownership.
- Exposed contact sample pixels: `18` left and `18` right across CL-001,
  CL-002, and CL-003.
- Source appearance landmarks: `10` left and `10` right.
- Feature measurement contracts: `24`.
- Disagreement records: `7`.

Every retained coordinate is integer-valued, in bounds, and source-linked.
Each row distance uses `width = x1 - x0`; each view-local depth-profile center
uses `(x0 + x1 - 1) / 2`. These profile centers are observations only and are
not final component centers, alignment authority, or cross-view pairing.

## Component And Contact Boundary

- C-001 through C-003 have exact visible outer-edge row samples only.
- C-004 remains an irregular discontinuous layer; no filled footprint or
  interior ownership was created.
- CL-001 through CL-003 contain only exposed open sample sequences.
- OS-001 through OS-003 remain occluded; no hidden interface was closed.
- C-005 remains ambiguous in both side views; absence is not proven.
- C-006 and C-007 landmarks remain appearance evidence without physical
  geometry or cross-view identity authority.

## Blocked Disagreement

Seven entries are preserved in
`manifests/STEP_07_LEFT_RIGHT_DISAGREEMENT_LIST.json`:

1. left Z calibration;
2. left Y calibration;
3. right Z calibration;
4. right Y calibration;
5. left/right visible depth-profile comparison without a common calibration
   or physical pixel pairing;
6. C-005 left/right identity;
7. CL-001 through CL-003 physical pixel pairing and hidden closure.

No average, mean, scale selection, shift, stretch, rotation, inferred
correspondence, or visual thickness fit was used.

## Evidence Produced

`evidence/STEP_07/SM_GIA_BloodAxeCairnstone_A005_STEP_07_LEFT_RIGHT_MEASUREMENT_EVIDENCE.png`

The board pairs untouched left/right panels with mark-only copies. Green marks
show calibration endpoints, cyan marks show one-pixel row distances and
irregular edge observations, yellow crosses show exposed contact samples, and
magenta crosses show appearance landmarks. It contains no mask, fill, closed
candidate contour, inferred backside, center solution, or geometry preview.

Both source tiles are pixel-exact with `0` changed pixels and `0` maximum RGB
delta.

## Focused Validation Result

- aggregate technical result: pass with blocked disagreements preserved;
- validators: `31` passed, `0` failed;
- JSON outputs parsed: `7`;
- all recorded coordinates in bounds: true;
- all row-span and profile-center formulas: pass;
- all calibration formulas: pass;
- contract references: pass;
- consolidated Y/Z scales: none;
- derived contour world measurements: blocked;
- visual thickness fitting: absent;
- source or panel mutation: none;
- candidate fill, interpretation, or geometry: none;
- A001-A004 asset-specific access: false;
- A005 production roots: absent;
- unrelated staged files: none.

Validation manifest:

`manifests/STEP_07_VALIDATION_MANIFEST.json`

## Assumptions And Interpretations

No interpretation was introduced. Native-pixel diagnostic scans were used only
to locate possible review coordinates; they were not accepted as authority.
Every retained coordinate was manually audited against the source panel. Row
marks are distance samples between visible edge pixels, not masks or candidate
fills.

The candidate does not assume that left/right irregular pixels correspond to
the same physical corners, stones, seams, contacts, or thickness stations.

## Access Declaration

- no A001-A004 asset-specific artifact was opened or used;
- no front, back, top, or perspective measurement was performed;
- no approved source or panel was modified;
- no filled mask, inferred contour, hidden closure, geometry, texture, export,
  or Unreal artifact was created;
- no A005 production root was created;
- no unrelated file was staged.

## Artifact Status

- Step 07 contract: `authoritative` for execution scope;
- calibration records: `authoritative` for their declared source observations;
- measurement manifests and contract sets: `authoritative`;
- disagreement list: `authoritative` record of blocked questions;
- evidence board and validation manifest: `proof only`;
- derived world-space contour/contact measurements: blocked;
- interpretation and geometry authority: none;
- Step 08 authority: none.

## Checkpoint

- Pre-action checkpoint: `Saved/ProjectRecovery/20260715-152620/`.
- Validated-candidate review checkpoint:
  `Saved/ProjectRecovery/20260715-154227/`.

## Output Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Visible review: untouched left/right panels, exact unfilled measurement
  evidence, calibration records, measurement manifests and contracts,
  disagreement list, validation result, and this output record
- Result: source-linked left/right pixel measurements and measurement
  contracts promoted to `authoritative`
- Preserved blocked scope: all seven disagreement entries, consolidated Y/Z
  scales, derived contour/contact world measurements, hidden contact closure,
  final centers, physical cross-view identity, visual thickness fitting,
  interpretation, geometry, and production work
- Approved pre-closeout checkpoint:
  `Saved/ProjectRecovery/20260715-154456/`

## Next Gate

Complete scoped Step 07 closeout, commit, push, and mandatory restart. The next
agent may present a Step 08 contract only. Step 08 remains unauthorized.
