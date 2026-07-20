# A005 S10R-003-A CL-003 Target-Space Mapping A01 Output Record

Status: `technically validated candidate interpretation; Flamestrike output decision pending`

Artifact classification: `candidate decision record`

Contract ID: `A005-CR-S10R-003-A-MAP-A01`

Date: 2026-07-17

## Decision Produced

The approved contract produced one bounded candidate for Flamestrike:

> endpoint-exclusive equal-rank parameter mapping of the sixteen authoritative
> top-view CL-003 samples to the approved K80 abstract target boundary.

This is a candidate interpretation only. Technical validation does not make
the mapping or its target coordinates authoritative.

## Execution Authority

Flamestrike approved execution of the visibly presented contract with the
statement `approved` on 2026-07-17.

The execution remained inside that contract. It did not implement a field,
close Step 10, begin Step 11, create geometry, stage, commit, or push.

Pre-action checkpoint:
`Saved/ProjectRecovery/20260717-153840/`.

## Exact Mapping Rule

For each semantic sector independently:

- source samples: four, in their authoritative recorded order;
- local rank: `r = 1,2,3,4`;
- normalized parameter: `u = r/5`;
- endpoint policy: registered K80 axis endpoints are interval limits only and
  receive no source sample;
- target curve: `abs(x / 56)^3 + abs(y / 44)^3 = 1`; and
- serialization: twelve decimal places.

Sector directions and angular rules:

- top, negative X to positive X through positive Y:
  `theta = pi * (1-u)`;
- right, positive Y to negative Y through positive X:
  `theta = pi/2 - pi*u`;
- bottom, positive X to negative X through negative Y:
  `theta = 2*pi - pi*u`; and
- left, negative Y to positive Y through negative X:
  `theta = 3*pi/2 - pi*u`.

The mapping is equal-rank in curve parameter. It is not an equal-arc-length
claim, source-distance fit, recovered source scale, physical pairing, center,
pivot, snap anchor, or geometry-vertex rule.

## Technical Result

- authoritative top-view CL-003 samples read: `16`;
- samples per sector: `4`;
- candidate mappings created: `16`;
- unique serialized target coordinates: `16`;
- registered endpoint assignments: `0`;
- duplicate target coordinates: `0`;
- source displacement: `0 px`;
- mapped non-top samples: `0`;
- physical cross-view pairs: `0`;
- source overlays or fits: `0`;
- closed contact loops or snap anchors: `0`;
- filled footprints, annuli, or hidden interfaces: `0`;
- fields, surfaces, topology, or geometry: `0`.

Maximum independently replayed K80 equation residual is below the registered
`1e-12` tolerance. Every mapped point remains strictly inside its sector
endpoint limits.

## Validation Result

Independent validation: `31 of 31 gates pass`; failures: `0`.

The auditor independently replayed all sixteen formulas without importing the
builder's result array. Every coordinate matched at twelve decimal places.
The source panel and authoritative contact manifest remained byte-identical.

## Review Artifact

The review board separates:

- the unchanged top source panel with the sixteen exact source marks; and
- the line-only K80 target curve, four endpoint-limit markers, and sixteen
  unjoined candidate interpretation points.

It contains no source/target overlay, fill, band, annulus, closed sector join,
surface, or 3D geometry preview.

## Compatibility Incident

The first builder launch stopped before the ledger or board because the local
Pillow version does not expose `Image.Resampling.NEAREST`. At that boundary:

- the valid input lock existed;
- candidate target-coordinate output remained `0`;
- no review board existed; and
- no authority or source artifact changed.

The builder was corrected mechanically to use the supported
`Image.NEAREST` constant. The mapping rule, formulas, inputs, precision,
scope, and output paths did not change. The complete build and independent
audit then passed.

This was a contained tool-compatibility interruption, not an evidence or
authority drift event.

## Files Created

- `steps/S10R_003_A_CL003_TARGET_SPACE_MAPPING_EXECUTION_A01_CONTRACT.md`;
- `manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_INPUT_LOCK.json`;
- `manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_LEDGER.json`;
- `manifests/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_VALIDATION.json`;
- `evidence/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01/SM_GIA_BloodAxeCairnstone_A005_S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_REVIEW_BOARD.png`;
- this output record;
- `handoffs/S10R_003_A_CL003_TARGET_SPACE_MAPPING_A01_TO_DECISION_HANDOFF.md`;
- `Tools/DCC/build_bloodaxe_cairnstone_a005_s10r003_mapping_a01.py`; and
- `Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r003_mapping_a01.py`.

## Artifact Routing

- approved execution contract: `authoritative for completed execution scope
  only`;
- input lock: `proof only`;
- mapping ledger: `candidate interpretation`;
- validation: `proof only`;
- review board: `proof only`;
- this output record: `candidate decision record`; and
- decision handoff: `candidate routing record`.

The authoritative K80 decision, exact source evidence, and historical Step 10R
records remain unchanged.

## Assumptions And Interpretations

New interpretation introduced:

- four sample ranks per sector are placed at endpoint-exclusive curve
  parameters `1/5`, `2/5`, `3/5`, and `4/5`.

No source-space measurement, pixel-spacing relation, cross-view association,
physical size, center, pivot, closure, field, surface, topology, or geometry
assumption was introduced.

## Current Blocks

Until Flamestrike explicitly approves the candidate output:

- the sixteen target coordinates are not authority;
- the mapping-execution block remains active;
- `S10R-003-A` is not promoted to implemented authority;
- `S10R-006-A` remains unimplemented;
- `S10R-BLOCK-006`, `S10R-BLOCK-008`, and `S10R-BLOCK-009` remain active;
- Step 10 closeout and Step 11 remain blocked; and
- DCC, Unreal, geometry, production, staging, commit, and push remain blocked.

## Mandatory Stop And Decision Gate

Stop after validation, checkpointing, and visible review.

Flamestrike must approve, reject, or leave blocked the exact endpoint-exclusive
candidate mapping. No adjacent work is authorized by a decision on this
candidate unless a separate exact contract states otherwise.

