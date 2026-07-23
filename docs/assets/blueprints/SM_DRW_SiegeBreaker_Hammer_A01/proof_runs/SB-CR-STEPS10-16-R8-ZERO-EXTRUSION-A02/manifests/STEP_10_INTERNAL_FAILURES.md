# Step 10 Internal Failures

## A01 — Independent-report JSON serialization

- Date: `2026-07-23`
- Stage: `Step 10 independent audit report writing`
- Result: `internal tool failure; no validation disposition produced`
- Cause: the independent validator compared exact ID sets correctly in memory
  but passed the Python set objects directly to `json.dumps`.
- Production effect: none. The Step 10 decision record and every authority
  input remained unchanged. No geometry, Blender, render, export, or Unreal
  action occurred.
- Smallest sufficient correction: sort exact set values into JSON arrays only
  when writing the evidence report. Do not change any comparison, authority,
  expected ID, or decision rule.
- Artifact status: this failure record is `proof only`.

## A02 — Incomplete numeric-precedence audit

- Date: `2026-07-23`
- Stage: `post-A01 Step 10 Core review before Step 11`
- Result: `A01 validation and output record invalidated before blueprint work`
- Cause: the A01 audit covered every named Step 09 disagreement and unknown
  but did not independently test the active R8 contract's numeric-substitution
  boundary against the older fixed component values.
- Controlling authority: the newer R8 contract fixes only total length at
  `170 cm`; it requires every other overall and component dimension to remain
  an observed consequence of the new pixels and forbids separate scaling for
  shaft, ferrule, grip, collar, pommel, or any other component.
- Production effect: none. Step 11 had not begun. No geometry, Blender,
  render, export, or Unreal action occurred.
- Smallest sufficient correction: add a separate machine-readable
  numeric-precedence record, extend the independent audit to test it, and
  rerun Step 10.
- Artifact status: the A01 validation, output record, and handoff are
  `invalid`; the underlying Step 10 decision record remains `candidate`
  pending the corrected audit.

## A03 — Incomplete final-depth precedence audit

- Date: `2026-07-23`
- Stage: `post-A02 Step 10 Core review before Step 11`
- Result: `A02 validation and output record invalidated before blueprint work`
- Cause: the A02 audit verified the top/bottom axial mean and the two unequal
  right-side consequences independently but did not require an explicit rule
  naming which measurement controls final candidate depth.
- Controlling authority: the later active R8 candidate-boundary rule requires
  each candidate to retain its own observed right-half span at one common
  right-view scale. It forbids normalization to the centered axial mean.
- Production effect: none. Step 11 had not begun. No geometry, Blender,
  render, export, or Unreal action occurred.
- Smallest sufficient correction: state that the candidate-specific right-view
  depths control final completed geometry and the centered top/bottom mean is
  comparison/orientation evidence only; extend the independent audit to test
  that hierarchy.
- Artifact status: the A02 validation, output record, and handoff are
  `invalid`; the Step 10 decision record remains `candidate`.
