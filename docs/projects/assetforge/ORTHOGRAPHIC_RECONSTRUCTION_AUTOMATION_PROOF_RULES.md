# Orthographic Reconstruction Automation Proof Rules

- Date saved: 2026-07-21
- Requested by: Flamestrike
- Artifact status: `reference only`
- Purpose: preserve the agreed proof-first rules for tomorrow's planning
- Implementation authority: `false`
- Production authority: `false`
- Unreal authority: `false`

## Goal

Build a local desktop application that turns supplied orthographic evidence into
a measurable, reproducible reconstruction workflow. Exact measurements,
authority, state transitions, and pass/fail decisions must be owned by
deterministic software and Flamestrike—not by a language model.

The application must prove its method on an isolated calibration dataset before
it touches an Aerathea production asset.

## Governing Boundary

- Deterministic code owns pixels, transforms, measurements, hashes,
  reconstruction, validation, audit results, and gate transitions.
- Flamestrike owns source authority, ambiguous pixel classification, unknown
  depth decisions, approval, and visual judgment.
- A language model may assist with code, explanations, interface support, and
  non-authoritative suggestions.
- A language model may not set `pass`, `approved`, `authoritative`, or any other
  production status.
- Model reasoning effort does not replace executable validation.
- A second model may review code, but it is not an independent measurement
  authority.

## Required User Interface

Use a local tabbed desktop interface, provisionally PySide6/Qt, with advanced
controls collapsed by default to reduce visual noise.

### Intake

- Drag-and-drop input files.
- Preserve immutable originals.
- Compute SHA-256 hashes.
- Identify the required source set.
- Block if any required source is missing.

### View Setup

- Register front, back, left, right, top, and bottom panels.
- Show exact integer pixel rectangles.
- Require Flamestrike confirmation of panel boundaries.
- Do not derive exact orthographic views from a perspective image.

### Registration

- Record world axes and dimension endpoints.
- Use one uniform transform for each complete view.
- Never scale, center, rotate, or reposition individual components
  independently.
- Display the full pixel-to-centimeter formula and computed residuals.

### Masks

- Create binary object and component masks.
- Use lossless image decoding.
- Use nearest-neighbor sampling when mask resampling is unavoidable.
- Classify every pixel as owned, excluded, or unknown.
- Require user confirmation for ambiguous segmentation.
- Do not allow an automatically inferred mask to become authority by itself.

### Measurements

- Extract exact contours, landmarks, stations, intervals, and dimensions from
  source pixels.
- Keep expected values separate from observed values.
- Recompute all observations from source evidence.
- Never copy design targets into observed fields.

### Volume

- Construct an orthographic visual hull from the approved six-view masks.
- Every constructed volume must consume the registered source data directly.
- Block hard-coded substitute geometry unless the exact primitive is explicitly
  declared by approved authority.
- Preserve unknown regions rather than inventing a solution.

### Validation

- Render the reconstruction through the same six fixed orthographic cameras.
- Use fixed resolution, fixed transforms, binary output, and no antialiasing for
  the exact silhouette gate.
- Compute per-view XOR difference images.
- Default pass requirement: zero differing silhouette pixels.
- Also report IoU, boundary displacement, landmark error, and component-order
  agreement without allowing them to override a failed zero-XOR requirement.
- Block advancement while any required gate fails.

### Depth Detail

- Accept only explicit depth maps, cross-sections, or Flamestrike-approved depth
  constraints.
- Label hidden, concave, obscured, or otherwise unproven surfaces as `unknown`.
- Do not infer relief depth, recesses, intersections, or backside ornament from
  silhouettes alone.

### Review

- Display source, render, overlay, XOR difference, and exact numeric results.
- Keep evidence and candidate output visibly separate.
- Present only a result whose mandatory gates pass.
- Flamestrike remains the final approval authority.

### Audit

- Preserve an immutable event trace.
- Record tool versions, commands, inputs, hashes, formulas, and outputs.
- Use an independent validator that reads finished artifacts directly.
- The validator may not trust builder properties, declared booleans, target
  values, or the builder's own manifest as proof.
- A skipped, missing, unread, or unevaluated gate is a failure.

## Exact Pixel Rules

1. Preserve original image bytes and hashes.
2. Decode without lossy conversion.
3. Use integer source coordinates for crops and landmarks.
4. Prohibit silent resize, filtering, color conversion, or panel warping.
5. Permit only the declared whole-view registration transform.
6. Preserve explicit unknown pixels.
7. Render validation masks deterministically.
8. Require zero differing pixels for the exact silhouette proof unless
   Flamestrike explicitly approves a different gate in advance.
9. Generate a visible difference image even when the difference count is zero.
10. Fail closed on missing evidence or conflicting views.

## Mathematical Limit

Six orthographic silhouettes constrain a visual hull; they do not uniquely
define all three-dimensional surfaces. They cannot prove hidden recesses,
unseen concavities, relief depth, obscured intersections, or backside ornament.

A single three-quarter concept image cannot be converted into exact
orthographic views without interpretation. It may serve as style evidence, but
not as an exact orthographic construction dataset.

When evidence is insufficient, the program must stop and report the unknown. It
must not create an inferred substitute.

## Proof-First Calibration Contract

The first implementation milestone must be isolated from Aerathea production:

1. Start with a known ground-truth 3D calibration object.
2. Render six lossless binary orthographic masks from fixed cameras.
3. Drop those six masks and declared dimensions into the application.
4. Hash and register all inputs.
5. Reconstruct only the permitted orthographic visual hull.
6. Rerender it through the same six cameras.
7. Require zero differing silhouette pixels in all six views.
8. Deliberately corrupt a crop, scale, mask, landmark, and axis in separate
   tests.
9. Prove that each corruption fails closed at the correct tab and cannot be
   bypassed.
10. Produce one readable audit board for Flamestrike review.
11. Stop for approval.

## Calibration Completion Boundary

The proof milestone ends with a visible, reproducible calibration result and
negative tamper tests. It does not authorize:

- Siege Breaker reconstruction.
- Any other Aerathea production asset.
- Texture or material creation.
- Production Blender packaging.
- Unreal import or validation.
- Reclassification of any quarantined or rejected artifact.
- Editing `AGENTS.md` or foundational Core rules.

Implementation requires a separate explicit step contract and Flamestrike
approval.

## Model Selection Conclusion

Changing models may be useful for independent code review, but it cannot replace
the deterministic measurement and validation architecture above. GPT-5.6 Sol
can assist with implementation; it must not be the measurement authority or
gatekeeper.

Official model references consulted on 2026-07-21:

- <https://developers.openai.com/api/docs/models>
- <https://developers.openai.com/api/docs/guides/latest-model>
