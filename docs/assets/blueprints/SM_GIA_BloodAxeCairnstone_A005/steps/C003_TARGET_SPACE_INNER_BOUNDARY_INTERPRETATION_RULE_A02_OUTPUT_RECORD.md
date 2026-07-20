# A005 C-003 Target-Space Inner-Boundary Interpretation Rule A02 Output Record

Status: `technical pass validated; visible Flamestrike decision pending`

Artifact classification: `candidate`

Contract ID: `A005-CR-C003-TSIB-A02`

Date: 2026-07-17

## Result

The approved bounded technical pass produced three deterministic, unfilled,
source-independent target-space boundary options inside the unchanged abstract
N3 outer curve:

| Choice | Ratio | Inner target extent | Axis separation from outer N3 |
|---|---:|---:|---:|
| `K90` narrow apron | 0.90 | `126 x 99 cm` | X `7 cm/side`; Y `5.5 cm/side` |
| `K80` medium apron | 0.80 | `112 x 88 cm` | X `14 cm/side`; Y `11 cm/side` |
| `K70` broad apron | 0.70 | `98 x 77 cm` | X `21 cm/side`; Y `16.5 cm/side` |
| leave blocked | none | none | preserves `S10R-BLOCK-003` |

No option is recommended, selected, or approved by the technical pass.

Technical result:
`three_C003_target_space_boundary_options_ready_for_Flamestrike_decision`.

## Formula And Containment Result

Every candidate uses only:

`abs(x / (70 * k))^3 + abs(y / (55 * k))^3 = 1`

inside the unchanged approved outer rule:

`abs(x / 70)^3 + abs(y / 55)^3 = 1`

Each curve contains 721 deterministic samples. Cardinal endpoints are exact
formula evaluations at 0/90/180/270/360 degrees, not hand-tuned points.

- K90 maximum outer-N3 equation value: approximately `0.729`.
- K80 maximum outer-N3 equation value: approximately `0.512`.
- K70 maximum outer-N3 equation value: approximately `0.343`.
- Intersections or escapes: `0`.
- Extent error: `0 cm` on every registered axis.
- Mathematical closure error: `0 cm` for every candidate.

## Evidence Preserved

- Machine-hashed inputs: `32 of 32 matched`.
- A01 contract: `quarantined`, byte-identical.
- A01 input lock: `invalid`, byte-identical.
- A01 option registry: `quarantined`, byte-identical.
- Exact CL-003 samples: `16` top and `47` across all views, unchanged.
- Exact CL-002 samples: `40`, unchanged; closure remains blocked.
- Physical cross-view pixel pairs: `0`.
- Target CL-003 coordinates: `0`.
- Source overlays in candidate target panels: `0`.
- Candidate fills, annuli, fields, surfaces, topology, and geometry: `0`.
- Automatic ranking or selection: none.
- Final validation: `26 of 26 gates pass`.
- Final source display: native 1:1 pixels; all unmarked source-display pixels
  independently matched the authoritative top panel.

## Evidence Versus Interpretation

The final board separates:

- unchanged top source evidence with the 16 exact discontinuous CL-003 marks;
- the approved abstract outer N3 target curve;
- the three unfilled K90/K80/K70 interpretation curves; and
- blocked/unknown downstream authority.

The candidate curves are not source measurements, source fits, physical C-003
dimensions, contact mappings, footprints, masks, surfaces, or geometry.

## Internal Rejected Proofs

These internal outputs were rejected before visible presentation and are not
authority:

1. Review board SHA-256
   `4e24c35e8e08d7298e084f8b353f6a2364c9a0c32bc3e9dbb56a99afec9669b2`:
   `rejected internal proof; superseded; not presented`. The Leave Blocked
   description touched its label. Only text spacing changed.
2. Curve-ledger SHA-256
   `948b8bfc2034a66f29cfa91047ab41db2e241acdb6002b63007f98de0bcc7684`:
   `rejected internal proof; superseded; not presented`. Floating evaluation
   of `sin(2*pi)` produced a roughly `1.9e-9 cm` serialized closure gap.
   Exact registered cardinal formula evaluation corrected it without changing
   the option rule.
3. Review board SHA-256
   `ef2116ec62de426564f84e2926d443628e791c5327214a4c7b1527cbe3c5fede`
   and validation SHA-256
   `1a01155fbbf6a7ea061021460a5b64e0ad1cb42b5ff78d19df929a06a00faee4`:
   `rejected internal proof; superseded; not presented`. A decorative red
   review-frame border touched the outermost source-copy pixels. Moving that
   border fully outside the source rectangle produced the final passing board.
   The authoritative source file never changed.

## Final Artifact Hashes

- Contract: `ea55cd69c494b17cfcc06e324552da2df789a6415f3eceef1112ea3110662d0b`.
- Input lock: `1208892b0c2e50a15e88062e656374a8183defec8c8d3fe70ba453f3c1b2d541`.
- Frozen option registry: `ba24e6b5803deb6af15b5fcf1d7e95f2f088321a63775a32ff39d6350b7423aa`.
- Curve ledger: `dc04dab52e922786a99eaa7bbc52cb3620ac41c4784aae56a10b098423952410`.
- Validation: `989c2a8e79addf2aba1cbc74a344a1a5e22d3ca1ba5e763b8bcacf4ce6ff18b1`.
- Review board: `717ed5ca38947f21bd56b5e2ee13cb060fae17579686b59e83abed8e52e077c9`.

## Authority Effect

Technical execution creates no approved inner-boundary rule. Flamestrike must
choose `K90`, `K80`, `K70`, or `leave blocked`.

Even if Flamestrike selects a curve:

- it can become authority only for the abstract C-003/C-004 target-space
  boundary;
- `S10R-003-A` remains conditional and unimplemented;
- no CL-003 target coordinate or mapping is authorized;
- `S10R-006-A` remains conditional and unimplemented;
- CL-002 closure and the C-003 annulus remain blocked; and
- fields, surfaces, topology, geometry, Step 10 closeout, Step 11, production,
  staging, commit, and push remain blocked.

## Next Approval Gate

Choose exactly one:

- `K90`
- `K80`
- `K70`
- `leave blocked`

After recording that decision, stop. Any status-record closeout or mapping
execution requires a separate stated contract.
