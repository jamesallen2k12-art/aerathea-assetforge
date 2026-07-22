# A07 Gate 00 Commercial-Safe Execution-Path Contract

- Contract ID: `SB-SC3M-A07-GATE00-LICENSE-PREFLIGHT`
- Date: `2026-07-22`
- Contract status: `approved for post-reset execution`
- Artifact status on completion: `proof only`
- Production mutation authorized: `false`

## Governing Core Principle

Evidence-Bound Decision Rule and Stop-the-Line govern this gate. A permissive
top-level model license is not evidence that every runtime, renderer, exporter,
or generated output path is commercially permitted.

## Authority

- Flamestrike's 2026-07-22 approval to save and run `SB-SC3M-A07` after reset.
- `SM_DRW_SiegeBreaker_Hammer_A01_SOURCE_CONSTRAINED_AUTHORITATIVE_3D_MASTER_A07_PLAN.md`.
- Local license files, package metadata, import paths, runtime evidence, and
  primary publisher license records.

## Exact Scope

1. Inspect the local TripoSR, TRELLIS-AMD, and TRELLIS.2 installations only as
   needed to map the proposed A07 execution path.
2. Record the exact model weights, encoder, core inference modules, geometry
   representation, simplifier, exporter, renderer, and texturing dependencies.
3. Record each component's license and classify it as `allowed`, `restricted`,
   `unclear`, or `not used` for commercial A07 production.
4. Trace imports and calls for a proposed raw-geometry path without running
   image-to-3D inference.
5. Verify whether the proposed path avoids `nvdiffrast`, `nvdiffrec`, the
   restricted TRELLIS render/texturing path, and
   `o_voxel.postprocess.to_glb`.
6. Define an independently licensed raw OBJ/PLY or equivalent exporter route
   and Blender intake boundary.
7. Produce one audit report with exact evidence and a final `go`, `blocked`, or
   `legal-review-required` decision.

## Forbidden Actions

- No source-image processing or modification.
- No model inference or candidate generation.
- No Blender geometry creation or modification.
- No use of any prior research output as a production input.
- No copying restricted implementation code into a new exporter or wrapper.
- No package installation, dependency replacement, or environment mutation.
- No legal conclusion beyond license-path classification and the declared need
  for qualified legal review.

## Acceptance Conditions

Gate 00 may report `go` only when:

- every runtime and export component is identified;
- every used component has a recorded production-permitting license;
- restricted components are absent from the proposed execution and import
  graph;
- the exporter route is independently licensed and does not call restricted
  rasterization or texturing code;
- the audit can be repeated from recorded commands and hashes;
- all uncertainty is either resolved or causes a fail-closed result.

Any unresolved license, missing license, ambiguous runtime import, restricted
component, or inability to prove isolation produces `blocked` or
`legal-review-required`, not `go`.

## Output And Decision

Output: a tracked Gate 00 audit report and, where useful, local-only raw logs.

Decision enabled: whether A07 may advance to Gate 01 immutable source lock.
