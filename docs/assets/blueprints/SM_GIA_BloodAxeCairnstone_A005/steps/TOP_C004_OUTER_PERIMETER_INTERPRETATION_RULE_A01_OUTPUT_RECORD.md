# A005 Top C-004 Outer-Perimeter Interpretation Rule A01 Output Record

Status: `candidate result; three target-space options ready for Flamestrike decision`

Artifact classification: `candidate`

Contract: `A005-CR-TOP-C004-OPIR-A01`

Date: 2026-07-17

## Plain-English Result

The bounded pass produced three exact, unfilled target-space perimeter options
at the approved `140 cm × 110 cm` C-004 extents:

- N2 ellipse;
- N3 rounded oval;
- N4 rounded rectilinear.

All three use the same neutral frame, sampling, scale, grid, line weight, and
framing. Their maximum target-extent error is
`0 cm`.

The unchanged top source is shown separately with its 16 exact CL-003 samples.
No option is overlaid or aligned to the source, and no CL-003 sample is mapped
into target space.

## Technical Result

`three_target_space_options_ready_for_Flamestrike_decision`

## Shared Pass Facts

- Candidate options: `3`.
- Source-owned top outer anchors: `0`.
- Exact top CL-003 samples preserved: `16`.
- Source overlays: `0`.
- Source-contact mappings: `0`.
- Filled footprints or masks: `0`.
- Source centers, pivots, topology, or geometry: `0`.
- Automatic ranking or technical selection: none.

## Decision Boundary

Flamestrike may select:

- `TOP_C004_OPIR_N2_ELLIPSE`;
- `TOP_C004_OPIR_N3_ROUNDED_OVAL`;
- `TOP_C004_OPIR_N4_ROUNDED_RECTILINEAR`;
- `TOP_C004_OPIR_LEAVE_BLOCKED`.

Selection would approve only the abstract target-space perimeter-shape rule.
Source placement, CL-003 mapping, a continuous transition field, filled
footprint, center, pivot, Step 10 revision, topology, geometry, production,
commit, and push would remain blocked.

## Artifact Routing Before Option Decision

- Contract: `authoritative for completed execution scope only` after its
  execution approval.
- Input lock, option registry, curve ledger, validation, and board: `proof
  only`.
- N2, N3, and N4 curves: `candidate interpretation`.
- This output and handoff: `candidate` pending Flamestrike's option decision.
- Original A005 authority and stop state: unchanged.
