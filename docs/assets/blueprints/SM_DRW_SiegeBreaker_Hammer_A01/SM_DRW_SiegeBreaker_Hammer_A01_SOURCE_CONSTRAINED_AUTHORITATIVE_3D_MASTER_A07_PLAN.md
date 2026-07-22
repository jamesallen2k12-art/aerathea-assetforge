# Siege Breaker Source-Constrained Authoritative 3D Master A07 Plan

- Plan ID: `SB-SC3M-A07`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date approved as the next process: `2026-07-22`
- Plan status: `authoritative`
- Production state: `not started`
- Current artifact status: `process authority only; no A07 visual or geometry candidate exists`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Core Goal

Create one Hero-quality, complete, real-world-scale 3D Concept Master that
preserves the approved Siege Breaker concept, resolves every hidden surface
through explicit review, and becomes the sole geometric source for exact
measurements and orthographic projections.

The controlling rule is:

> AI proposes the shape. The original concept constrains visible design.
> Flamestrike approves interpretation. The locked 3D master establishes
> geometry, scale, and measurement.

## Approval And Direction Record

Flamestrike approved saving this method as the process to run after a context
reset. This approval establishes the A07 plan and authorizes its mandatory
read-only Gate 00 preflight after the Core resume handshake. It does not
pre-approve a generated candidate, hidden-surface interpretation, final 3D
master, game-ready derivative, Unreal import, or `Fully game-ready` status.

## Authority Hierarchy

1. Core Principles and Flamestrike's explicit decisions.
2. The original Siege Breaker concept for visual identity, silhouette,
   material language, layered form, authored asymmetry, mood, and Hero quality.
3. Approved numeric records for real-world scale and fixed mechanical anchors.
4. The Flamestrike-approved A07 3D Concept Master for geometry, depth,
   component placement, hidden surfaces, and measurement.
5. Orthographic images rendered from that locked master as calibrated
   derivative measurement evidence.
6. AI reconstructions, generated views, and earlier DCC outputs as candidates,
   proof, or reference only according to their recorded status.

The source concept currently identified for A07 intake is:

- Path: `SourceAssets/Concepts/SiegeBreaker/siege_breaker_concept_view.png`
- Format: `1122 x 1402` RGB PNG
- SHA-256: `9f1ac142a5047968bb20c74216c2dccf61470ed9f4e21689ff01934bd849c586`
- Current role: `authoritative visual target pending Gate 01 immutable intake`

The existing numeric authority remains:

- Overall envelope: `52 x 32 x 170 cm`
- Primary uniform scale anchor: overall length `170 cm`
- Coordinate origin: bottom-center of the pommel
- Shared axis: `X=0, Y=0`
- Protected stations and component constraints: those recorded in
  `manifests/MEASUREMENT_AND_OWNERSHIP_CONTRACTS.json`

The `170 cm` length is the uniform scale anchor. Width and depth are validation
constraints, not permission for independent axis scaling. If a source-faithful
master cannot satisfy the declared `52 x 32 cm` bounds without nonuniform
distortion, A07 stops for an authority decision; it does not silently warp the
model or alter the numeric record.

## Superseded Active Method

The A06 measurement-first proof run remains preserved at
`step_10_waiting_flamestrike_decision`. Its evidence retains the status already
recorded within that run, but A06 is no longer the active production route.

For A07, independently generated orthographic images are not geometric,
scale, or pixel-measurement authority. They may be historical evidence or
visual reference only. A07 must create one approved 3D object first and derive
all exact orthographic views from it afterward.

`SB-CM-VISUAL-A01` remains quarantined and may not be repaired forward or used
as an A07 construction seed.

## Method Roles

| Method | Permitted A07 role |
|---|---|
| Original concept art | Authoritative visible-design target |
| AI image-to-3D | Produces 3D hypotheses only |
| AI-generated alternative views | Interpretation/reference only; never measurement authority |
| Blender | Deterministic correction, completion, scaling, and master lock |
| Primitive construction | Local correction or replacement tool; never the design foundation |
| Pixel scanning | Exact verification only after the approved master exists |
| Master-derived orthographic images | Calibrated derivative measurement evidence |
| Flamestrike review | Final visual, hidden-surface, and authority decision |

## Mandatory Gate Sequence

### Gate 00 — Commercial-Safe Execution-Path Preflight

Before any A07 source processing or model generation:

1. Inventory every model, weight, library, exporter, renderer, and runtime
   component proposed for the reconstruction path.
2. Record exact licenses, versions, hashes, and runtime imports.
3. Prove that the production path does not import or execute restricted
   components.
4. Produce a fail-closed `go`, `blocked`, or `legal-review-required` report.

The locally installed TRELLIS/TRELLIS.2 GLB path that invokes `nvdiffrast`,
`nvdiffrec`, TRELLIS restricted render/texturing paths, or
`o_voxel.postprocess.to_glb` is blocked from A07 production. Existing outputs
from that path remain `proof only` or `reference only` and may not enter A07.

Public methods and commercially permitted implementations may inform A07.
Restricted source code or outputs may not be copied into, converted into, or
used as hidden inputs to the production path.

Gate output: `proof only` commercial-safe execution-path audit.

Stop condition: no source processing or generation until the report is `go`.

### Gate 01 — Immutable Source Lock

1. Verify the exact concept file, hash, dimensions, provenance, and approved
   visual role.
2. Verify the numeric envelope and fixed mechanical anchors.
3. Record any conflict before touching the source.

Gate output: `authoritative` A07 source and numeric authority manifest.

### Gate 02 — Source-Preserving Extraction

1. Remove only page background, annotations, dimension lines, and unrelated
   pixels.
2. Preserve every source-owned Siege Breaker pixel.
3. Record the crop, mask, dimensions, and hashes.
4. Do not repaint, smooth, extend, complete, or redesign the object.

Gate output: `candidate` source extraction plus exact source-difference proof.

Approval decision: confirm that the extraction removed no asset-owned content
and introduced no interpretation.

### Gate 03 — AI 3D Hypothesis Batch

1. Use only the Gate 00-cleared production path.
2. Generate a declared batch of independent 3D hypotheses from the same locked
   source.
3. Preserve seeds, settings, model identities, logs, and output hashes.
4. Render every candidate through one standardized review rig.

No candidate receives measurement or visual authority at this gate.

Gate output: one or more `DCC source candidates`.

Approval decision: Flamestrike selects the candidate with the strongest
silhouette, major volumes, component recovery, and Siege Breaker identity, or
rejects the complete batch.

### Gate 04 — Canonical-View Convergence

1. Import the selected candidate into Blender.
2. Solve and lock a camera matching the original concept presentation.
3. Compare source and render for outer silhouette, major component boundaries,
   negative spaces, overlaps, proportions, layered hard-surface construction,
   authored asymmetry, and material grouping.
4. Use AI-assisted modification, sculpting, hard-surface rebuilding, and local
   primitive replacement only to converge on the source.
5. Keep evidence overlays separate from candidate beauty views.

The original concept controls visible design. Technical completeness cannot
substitute for visual fidelity.

Gate output: `candidate` source-converged 3D model and registered comparison.

Approval decision: accept, revise, or reject visible-source fidelity.

### Gate 05 — Explicit 360-Degree Interpretation

1. Render front, back, left, right, top, bottom, and rear three-quarter views
   from the same model.
2. Identify every region not determined by the source.
3. Present AI-proposed hidden surfaces as interpretation, never evidence.
4. Record Flamestrike's decision for back construction, underside, plate
   thickness, mechanical connections, cavities, symmetry, and hidden ornament.

Gate output: `candidate` complete 360-degree design and hidden-surface decision
record.

Approval decision: approve, revise, or block every unresolved design region.

### Gate 06 — Uniform Scale And Coordinate Lock

1. Uniformly scale the approved design to the `170 cm` length anchor.
2. Apply transforms and verify units, origin, pivot, axes, component IDs, and
   protected stations.
3. Validate the resulting width and depth against `52 x 32 cm` without
   nonuniform distortion.
4. Stop if source fidelity and numeric authority cannot coexist.

Gate output: `candidate` scaled 3D Concept Master plus exact mesh-coordinate
measurement report.

Approval decision: approve, revise, or block the physical scale and component
proportions.

### Gate 07 — Authoritative 3D Concept Master Approval

Present one visible review package containing:

- the original concept beside the matched-camera master render;
- a registered source/render comparison;
- a clean Hero render;
- a complete turntable;
- six clean orthographic views;
- major dimensions and component positions;
- the hidden-surface decision record;
- provenance and license evidence.

Only an explicit Flamestrike approval changes the master from `candidate` to
`authoritative`.

The approved master becomes authoritative for geometry, scale, depth,
component placement, and measurements. The original concept remains
authoritative for visual identity and style.

### Gate 08 — Exact Orthographic Measurement Package

From the unchanged, approved master:

1. Lock six orthographic cameras, resolution, pixel aspect, framing, object
   transforms, and coordinate frame.
2. Render without post-render cropping, resizing, or resampling.
3. Record the exact pixel-to-world conversion for each view.
4. Produce masks, depth, normal, component-ID, calibration, and dimension
   records from the same geometry.
5. Verify critical dimensions directly against mesh coordinates.

Gate output: `authoritative` calibrated orthographic measurement package.

Pixel measurement is exact to the approved 3D master. Mesh coordinates remain
the primary authority for critical dimensions.

### Gate 09 — Game-Ready Derivative

Keep the authoritative Concept Master immutable. Create a separate production
derivative through retopology, UVs, PBR textures, baking, LOD0-LOD3, collision,
export, and clean reimport.

Validate silhouette, dimensions, component placement, and approved design
features against the master at every production gate.

Gate output: `DCC game-ready candidate` only. Unreal validation and
Flamestrike approval are still required before `Fully game-ready`.

## Stop-The-Line Conditions

A07 stops immediately if:

- the commercial license path is unclear or invokes a restricted dependency;
- the source image, hash, provenance, or numeric authority conflicts;
- extraction removes source-owned content or introduces painted interpretation;
- no AI hypothesis preserves a sufficient Siege Breaker foundation;
- a generated view is being treated as geometric evidence;
- visible-source convergence fails;
- a hidden surface lacks Flamestrike approval;
- uniform scale cannot satisfy the approved numeric constraints;
- a derivative orthographic view is cropped, resized, or generated from a
  different model state;
- a game-ready derivative materially departs from the approved master.

The response to a stop is evidence preservation and a new approval decision,
not a silent workaround or repair-forward.

## Success Criteria

A07 succeeds only when:

1. The canonical view genuinely preserves the approved concept's Hero quality.
2. Every hidden surface has an explicit decision record.
3. One complete 3D model exists at approved real-world scale.
4. The model satisfies the protected numeric constraints or carries an
   approved authority amendment.
5. The model's measurements are read directly from locked mesh coordinates.
6. Every authoritative orthographic view comes from that exact locked model.
7. Pixel-to-world conversion is recorded and reproducible.
8. The complete runtime and output path is commercially license-cleared.
9. Flamestrike explicitly approves the master as `authoritative`.

## Reset / Resume Rule

After context reset, read only the project recovery journal/latest checkpoint,
the top-level Siege Breaker reset state, this plan, the A07 reset handoff, the
Gate 00 contract, and the prior canonical-master rejection record. Report the
state summary, then execute Gate 00 only. Do not process the concept or generate
geometry until Gate 00 records `go`.
