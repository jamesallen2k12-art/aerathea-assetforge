# Twin Hammer Measurement Authority Lock A01 — Failed Validation Review

- Date: `2026-07-24`
- Assets:
  `SM_DRW_SiegeBreaker_Hammer_A01` and
  `SM_DRW_FoeHammer_Hammer_A01`
- Contract SHA-256:
  `03f0f933aadc516ba639fc47450465b2144f8eb828642a36d88dd7cbbe93e9e6`
- Contract execution decision: `approved`
- Validation result: `FAIL 59/61`
- Authority-lock status: `invalid`
- Production status: `stopped`
- Review decision: `blocked`

## Outcome

The approved contract created the declared A01 lock record, then stopped when
its independent validation failed two required gates.

The lock is not effective. It promotes no measurement authority and unlocks
no production action.

## Exact Records

### Invalid Lock

- Path:
  `../manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01.json`
- SHA-256:
  `e57b88d53724f69b4d7179a2616316820f9ef669699e074d5c74aa1ea59c6cd9`
- Effective status: `invalid`

### Failed Independent Validation

- Path:
  `../manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_VALIDATION.json`
- SHA-256:
  `25b8eea66a442c512e8e59dd02fb48c2487e708495a40e88e40e4e03379d40b5`
- Checks passed: `59`
- Checks total: `61`
- Failed IDs: `E08`, `E09`

## Failure Evidence

| Gate | Required observation | Validation observation | Result |
|---|---|---|---|
| `E08` | integer `0` new project authority-lock tools | empty numeric operand after a zero-match `rg -c` pipeline | `FAIL` |
| `E09` | integer `0` forbidden authority-lock output extensions | empty numeric operand after a zero-match `rg -ci` pipeline | `FAIL` |

The validation command treated the empty operands as failed numeric
assertions.

## Diagnostic Evidence

A later read-only diagnosis observed:

| Diagnostic | Count |
|---|---:|
| New project authority-lock tools matching the A01 name | `0` |
| Forbidden authority-lock output extensions matching the A01 name | `0` |

The diagnosis indicates that the failed gates came from the zero-match
counter implementation, not from discovered forbidden output.

Core does not allow this diagnostic to be substituted for the contracted
validation result. The A01 lock remains invalid.

## Passed Evidence

The independent validation passed:

- all `11` governing input hashes;
- all `5` canonical partial-lock section digests;
- exact candidate-manifest SHA-256;
- exact contract SHA-256 and approval;
- measurement audit `261/261`;
- three exact 2D projected contacts and `333` unit edges;
- four exact C04 projected owner boundaries;
- the bottom-center absence record without fill authority;
- seven C06-C11 half-open intervals;
- eight station edges;
- all three physical-Z formulas;
- exact continuity at source edges `955` and `1110`;
- `155` exact C08 radius rows;
- radial scale `11/136 cm/px`;
- exact C08 radius range
  `363/136 cm` through `209/68 cm`;
- exclusion of the complete rotational-transition table from lock authority;
- `2,566` incomplete head boundary samples;
- `0` complete head XYZ samples;
- `0` approved point correspondences;
- `0` head triangle index triplets;
- all five governing stop conditions;
- all production-boundary booleans; and
- byte-identical approved manifest, audit, resolver, and auditor.

These passed subchecks remain proof only because the overall validation
failed.

## Evidence Versus Interpretation

### Evidence

- The approved measurement manifest remains byte-identical at SHA-256
  `7a7c633587b4d39797339077685109eb28c31ca8e28e36f1e888d0506fec2ceb`.
- The prior independent audit remains byte-identical at SHA-256
  `837ebb6778867efa4f4228d30ac2f7d8e3c48f4303a3ea651b675f311995eaaa`.
- The A01 lock validation result is exactly `FAIL 59/61`.
- No project tool, Blender, geometry, image, render, export, or Unreal
  artifact was created by this execution.

### Interpretation

- The five approved manifest subsets remain approved candidate measurement
  interpretations.
- They did not become authoritative through A01.
- The diagnostic explanation for `E08` and `E09` is not a substitute pass.

## Preserved Blocks

### Blueprint block: source authority missing

- complete head XYZ embedding;
- corner incidence;
- hidden-boundary owner;
- bottom center-gap disposition; and
- C04 adjacent stone owner and full perimeter incidence.

### Blueprint block: rule missing

- cyclic head incidence;
- hidden-closure equation;
- unequal-radius shoulder/contact equations; and
- terminal-cap closure.

### Blueprint block: source authority conflict

- head station `A=600` maps to `114070/1063 cm` in the global front view;
- later physical authority places it at `132 cm`; and
- no approved reconciliation exists.

The full rotational-transition table remains proof-only candidate evidence,
including the coordinate-equal C08/C09 row.

## Authority Boundary

- Valid measurement authority lock: `false`
- Complete head authority: `false`
- Builder authority: `false`
- Blender authority: `false`
- Geometry authority: `false`
- Imagery / render authority: `false`
- Export authority: `false`
- Step 13 / Step 14 authority: `false / false`
- Unreal authority: `false`
- Production authority: `false`

## Stop And Recovery Need

Do not rerun, edit, repair, or promote A01.

The last Core-valid state remains the Flamestrike-approved candidate
measurement package. A clean A02 attempt would require a separate Core
recovery contract and separate Flamestrike approval.
