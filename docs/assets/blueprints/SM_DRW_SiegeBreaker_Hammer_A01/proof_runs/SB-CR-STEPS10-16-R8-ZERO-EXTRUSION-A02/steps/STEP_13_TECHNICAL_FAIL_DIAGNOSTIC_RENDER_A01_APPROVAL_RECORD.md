# Step 13 Technical-Fail Diagnostic Render A01 Approval Record

- Date: `2026-07-24`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01`
  - `SM_DRW_FoeHammer_Hammer_A01`
- Artifact status: `authoritative approval record`
- Technical source state: `Step 13 FAIL / BLOCKED`
- Geometry authority: `false`
- Source-save authority: `false`
- Repair / rebuild authority: `false`
- Step 14 / export / Unreal authority: `false`

## Flamestrike Approval

Flamestrike approved the following exact next step:

1. commit and push the existing Step 13 failure records;
2. produce one read-only diagnostic image per hammer, showing the normal model
   beside highlighted faulty joins;
3. do not edit either Blender source;
4. stop for Flamestrike's feedback; and
5. handle any mirror-and-weld rebuild under a separate later contract.

Approval evidence: Flamestrike replied `approved` to that explicit five-item
scope on `2026-07-24`.

## Diagnostic Presentation

Each final image may contain:

- a normal matched three-quarter view;
- the same matched view with technical overlays;
- red lines for exact saved panel edges with no matching partner;
- yellow lines for exact saved boundary edges used by more than two panels;
- magenta lines for directly observed local-C04 face-winding errors;
- a plain-English legend and directly observed counts.

Supporting raw clean and overlay renders may be retained beside the final
image. They are `proof only` and cannot act as geometry, visual-canon,
artistic-approval, Step 13-pass, Step 14, export, or Unreal authority.

## Read-Only Boundary

The diagnostic renderer may:

- open each locked `.blend` directly;
- create a camera, temporary display settings, curve overlays, and labels in
  memory;
- save only new PNG evidence outside the source directories; and
- record source hashes before and after.

It may not:

- call a Blender save operator;
- edit, resave, replace, copy, move, or rename either source `.blend`;
- repair or join geometry;
- mirror, rotate, weld, recalculate, delete, add, or otherwise change
  production geometry;
- reinterpret the diagnostic overlays as a candidate solution; or
- begin the separately discussed mirror-and-weld rebuild.

## Required Stop

After both diagnostic images are verified and opened visibly, stop for
Flamestrike's feedback and any additional source data. No repair or rebuild
may begin from this approval.
