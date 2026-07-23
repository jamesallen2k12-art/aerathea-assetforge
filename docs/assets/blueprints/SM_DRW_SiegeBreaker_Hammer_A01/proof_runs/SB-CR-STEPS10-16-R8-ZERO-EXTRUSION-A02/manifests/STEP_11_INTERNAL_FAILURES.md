# Step 11 Internal Failures

## A01 — Exact scanline schema-label mismatch

- Date: `2026-07-23`
- Stage: `Step 11 independent source-authority preflight`
- Result: `internal validator failure; no Step 11 disposition produced`
- Cause: the validator expected
  `AERATHEA_COMPLETE_HAMMER_SCANLINES_V1`; all six authoritative captures use
  the exact schema
  `AERATHEA_COMPLETE_HAMMER_RGBA_SCANLINES_V1`.
- Production effect: none. The source-authority finding, inputs, and proposed
  recovery scope were unchanged. No blueprint, geometry, Blender, render,
  export, or Unreal action occurred.
- Smallest sufficient correction: replace only the expected schema-label
  literal and rerun the same checks.
- Artifact status: the A01 validation report is `invalid`.
