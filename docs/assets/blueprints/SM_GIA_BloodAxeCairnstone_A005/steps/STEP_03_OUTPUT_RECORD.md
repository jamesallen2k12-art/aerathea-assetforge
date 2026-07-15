# Step 03 Output Record

Status: Step 03 complete and pushed

Artifact classification: `authoritative`

Date: 2026-07-15

## Assigned Goal

Lock lossless full-source crop formulas for the perspective, front, back, left,
right, and top panels while excluding borders and unrelated annotations from
panel ownership.

## Approved Decision

Pass. Six crops reproduce their declared source regions exactly. Flamestrike
approved all six visible boundaries as source ownership on 2026-07-15. The
crop formulas and panel images are authoritative for A005.

## Authority

- `AGENTS.md`;
- authoritative fresh-start multi-step plan;
- approved A005 Step 01 governance package;
- approved Step 02 source-authority package;
- approved `steps/STEP_03_CONTRACT.md`.

## Exact Crop Formulas

Coordinates use top-left origin, x right, y down, and integer half-open bounds
`[x0, y0, x1, y1)`.

| Panel | Half-open crop | Output size |
|---|---:|---:|
| Perspective | `[19, 130, 541, 655)` | `522 x 525` |
| Front | `[552, 130, 1035, 655)` | `483 x 525` |
| Back | `[19, 663, 541, 1064)` | `522 x 401` |
| Left | `[552, 663, 1036, 1064)` | `484 x 401` |
| Right | `[19, 1073, 386, 1445)` | `367 x 372` |
| Top | `[393, 1073, 730, 1444)` | `337 x 371` |

Width is `x1 - x0`; height is `y1 - y0`.

## Source-Ownership Boundary

- Sheet header and footer are excluded.
- Panel-frame pixels are excluded.
- Each view label and its view-specific dimension annotations remain untouched
  inside its crop.
- The top crop ends at `x1 = 730`, the exact source divider before the unrelated
  specifications table; the divider and table are excluded.
- Perspective is visual corroboration unless separately calibrated.

## Files Created Or Updated

Created:

- approved Step 03 contract record;
- Step 03 panel crop manifest;
- six A005-namespaced lossless panel PNGs;
- source-only boundary evidence board;
- Step 03 validation manifest;
- this output record;
- Step 03-to-Step 04 handoff.

Updated as Step 03 records:

- RESET_RESUME_STATE;
- ARTIFACT_INDEX;
- APPROVAL_LOG.

## Evidence Produced

- authoritative source identity recheck;
- six integer half-open crop formulas;
- decoded pixel hashes for each crop and direct source region;
- zero-difference decoded-pixel comparison for every panel;
- full-source boundary board containing exact unfilled boundaries and
  coordinate labels only.

## Exact Results

- Source file SHA256:
  `4b953abb87f5f254a5f51c6214e76d3f72c4fc55bc2fa4e4d605b2440d6e53c2`
- Source pixel SHA256:
  `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- Panel count: `6`
- Aggregate changed pixels: `0`
- Maximum RGB delta: `0`
- All panels pixel exact: `true`
- Scaling, filtering, rotation, recoloring, cleanup, and annotation removal:
  none

## Internal Candidate Correction

The first internal right-view preview used `[19, 1073, 386, 1444)` and omitted
source row `1444`. Pixel-line inspection proved that the right-view bottom
border begins at row `1445`, so row `1444` remains panel-owned. Before manifest
lock or user presentation, the right crop was corrected to
`[19, 1073, 386, 1445)` and the evidence board was regenerated.

The overwritten right crop with file SHA256
`1600ff7eaecb22c37076abde1f021fe0641956596070c252524cd819fa92b425` and
the overwritten board with file SHA256
`b0d73c26750bbee2bd390da48fa0451dcdf33d6771469d5e5b342c51e5e21908`
are classified `invalid`. They no longer exist and were never presented for
approval. This was a pre-lock candidate correction, not a Core drift event.

## Assumptions And Interpretations

None. Boundaries follow explicit source frame interiors and the explicit
source divider before the specifications table. No component, contour, hidden
surface, calibration, or production solution was inferred.

## Access Declaration

- No A001-A004 asset-specific artifact was opened or read.
- The authoritative source was not modified.
- No pixel inside a panel crop was altered.
- No component mask, fill, silhouette, geometry, or texture was created.
- No A005 production root was created.

## Artifact Status

- Step 03 contract: `authoritative`.
- Panel crop manifest and six panel images: `authoritative`.
- Boundary evidence board and validation manifest: `proof only`.
- Step 03 output record and handoff: `authoritative`.
- Interpretation authority: none.
- Production artifacts: none.

## Checkpoints

- Pre-action checkpoint: `Saved/ProjectRecovery/20260715-123416/`.
- Candidate review checkpoint: `Saved/ProjectRecovery/20260715-124330/`.
- Approved pre-closeout checkpoint: `Saved/ProjectRecovery/20260715-125003/`.

## Output Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Visible review: untouched source, exact-boundary board, six lossless crops,
  and this record
- Result: pass and authority promotion
- Exclusion: Step 04 remains unauthorized

## Next Gate

Create the final handoff closeout commit and completion checkpoint, then stop
for the mandatory restart. Step 04 remains unauthorized.

## Commit And Push

- Scoped content commit: `2cee686`
- Commit message: `Lock BloodAxe Cairn Stone A005 panel decomposition`
- Push: success; `assetforge/main` advanced from `ac3be5d` to `2cee686`
- Scoped files: fifteen A005 Step 03 records and images
- Unrelated changes: preserved and unstaged
