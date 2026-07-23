# Step 11 Contract — Zero-Extrusion Blueprint Authority Gate

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Recovery run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Parent evidence run: `SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01`
- Step: `11`
- Status: `authorized prerequisite audit`
- Artifact ceiling: `production blueprint or evidence-bound block`
- Geometry / Blender / export / Unreal authority:
  `false / false / false / false`

## Decision

Determine whether the valid Step 01-10 records contain sufficient exact
new-image ownership data to write every required component surface in a
zero-extrusion production blueprint.

The step may write a blueprint only when every proposed surface can point to:

1. an exact new-image source pixel or scanline owner;
2. an approved equation or closure rule; and
3. an exact Step 01-09 measurement.

## Exact Authority

- `AGENTS.md`;
- the authoritative Steps 01-16 plan;
- the locked R8 execution contract;
- the zero-extrusion reset handoff;
- the approved component-equation contract;
- the deterministic closure amendment;
- parent Steps 01-09 exact evidence;
- Step 10 decisions and numeric/final-depth precedence records.

## Inputs

- Step 04 component/source-ownership inventory;
- Steps 06-08 exact row and column profiles;
- Step 09 integrated index and correspondence records;
- Step 10 interpretation decisions;
- Step 10 numeric and final-depth precedence;
- approved component and closure equations.

## Required Preflight

The independent preflight must determine whether the records provide exact
coordinate-bearing ownership for:

- `C01_CENTER_CORE`;
- `C02_STONE_LEFT`;
- `C03_STONE_RIGHT`;
- `C04_STRIKE_FACE_POSITIVE_X`;
- `C06_UPPER_HAFT_CAP`;
- source-connected negative spaces;
- measured common boundaries between those components; and
- the corresponding front/right/top/bottom boundary edges needed by the
  approved ruled closures.

Qualitative labels, overall object membership, printed annotations, old
component ratios, old meshes, and visually selected boundaries are
insufficient.

## Required Outputs

- `manifests/STEP_11_SOURCE_AUTHORITY_PREFLIGHT.json`;
- `manifests/STEP_11_VALIDATION.json`;
- either:
  - `manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json` on exact pass; or
  - `steps/STEP_11_OUTPUT_RECORD.md` and a blocked handoff;
- a visible source-authority review record.

## Forbidden Methods

- importing or measuring an old component mesh;
- scaling old component intervals into the new image;
- inventing a component threshold, color classifier, contour, or owner mask;
- treating whole-object scanlines as exact component segmentation;
- filling a protected negative space;
- generalized cross-sections, slabs, primitives, extrusion, or copied depth
  faces;
- creating geometry before an exact blueprint pass.

## Validator

`Tools/DCC/audit_siegebreaker_r8_step11_source_authority.py`

The validator reads the finished evidence records directly and must return
`BLOCKED` when any required coordinate-bearing owner is absent.

## Gate

- Exact owner data present for every required surface:
  write and independently audit the production blueprint.
- Any required owner data absent:
  stop with `Blueprint block: source authority missing`.

No geometry follows a block.
