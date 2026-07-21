# A005 A07 Visual Rejection / A08 Restart Handoff

Status: `authoritative fresh-context restart handoff`

Date: 2026-07-21

## Flamestrike Decision

The exact A07 final image is rejected.

Observed failures:

1. The bottom ring's right side is vertically stretched and rises above the
   top base course.
2. The bottom ring is deformed on the left side.
3. The A07 top render does not geometrically match the original top view.
4. The rings do not visibly consist of individual stones as shown in the
   concept art.

Flamestrike requested this save point and a context reset before another
attempt using these findings.

## Core Recovery

- A07 Blender, textures, FBXs, final image, top image, and candidate
  classification: `quarantined`.
- A07 `20/20` audit: `proof only`; it proves the bounded technical checks but
  not visual equivalence.
- A07 scripts: `reference only` for defect analysis and invalid as A08
  construction authority.
- A07 dimensions: `reference only`; correct bounds did not prove correct
  course geometry.
- A06 exterior measurement record: remains `authoritative evidence`.
- Exact A04 plinth: remains an `authoritative visual reference`.
- Original source and top panel: remain `authoritative`.

The first A07 drift action was retaining the continuous annular masonry-shell
method while changing only crown spans. The invalid assumption was that
simulated joints on one ring shell could satisfy the source's individual-stone
geometry.

The technical overlap is explicit: C003 reaches `Z=25.248524 cm`, while C002
dips to `Z=24.577829 cm`, producing a `0.670695 cm` overlap that can let the
lower course visually overtake the upper course.

## A08 First Action After Resume

Perform a measurement-only audit of the authoritative original top panel.
Record, without geometry or filled candidate shapes:

- source-visible stone counts or explicitly blocked ambiguous counts for each
  ring;
- visible angular segment boundaries and irregular width distribution;
- ring inner/outer radial limits and stone projection;
- C002/C003/C004 vertical ordering and required positive clearances;
- source-visible top silhouettes needed to distinguish individual stones;
- UV orientation requirements needed to prevent vertical stretching.

If the source cannot support an exact count or boundary, record the ambiguity
and use a separately approved bounded rule. Do not invent a count.

## A08 Construction Requirements After Measurement Authority

- Fresh A08-only outputs; A07 geometry inputs `0`.
- Actual individual watertight stone islands for each visible ring, not one
  continuous annular shell with simulated joints.
- Positive C002-over-C003 and C003-over-C004 clearance gates at every sampled
  angular sector.
- Per-stone UV projection/orientation and distortion limits; no vertically
  smeared side faces.
- Fixed front, left, right, and true orthographic top proofs before the final
  perspective render.
- Top proof must visibly match the concept's individual-stone organization,
  not only the `140 x 110 cm` outer bounds.
- Preserve the exact A04 plinth unless new Flamestrike direction changes it.

## Stop Boundary

This handoff authorizes the A08 measurement-only first action after the fresh
context resume. It does not authorize geometry until that measurement gate
passes. Unreal/Step 17 and `Fully game-ready` remain forbidden.
