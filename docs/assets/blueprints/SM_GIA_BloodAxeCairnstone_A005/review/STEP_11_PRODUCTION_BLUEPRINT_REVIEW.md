# A005 Step 11 Production Blueprint Review

> **PLANNING ONLY — NO GEOMETRY — NO DCC — NO UNREAL**

Contract: `A005-CR-STEP11-PROD-SPEC-GCB-A01`

Decision: `approved authoritative Step 11 construction blueprint`

Artifact classification: `authoritative planning review`

## What This Review Approves

One buildable construction plan for
`SM_GIA_BloodAxeCairnstone_A005`, mapped to the approved A005 source,
measurements, ten Step 10 rules, and ten bounded Step 11 technical rules.

This review does not approve or show a mesh, surface, texture, FBX, collision
asset, LOD, Unreal asset, or visual implementation.

## Authority Boundary

| Subject | Approved authority | Explicit non-claim |
|---|---|---|
| Scale | 220 cm height; C-001 120 x 90 cm; C-004 140 x 110 cm; 35 cm base span | No unified source-pixel scale |
| Frame | +X right, +Y back, +Z up; pivot/origin at (0,0,0) | No source center or recovered placement |
| C-001 | Front owns XZ; left owns YZ; top owns +Z; direct planar corner joins | No physical cross-view corner pairs or smoothed primitive |
| C-002/C-003 | Separate owner-view faceted masonry courses | No copied course, source-exact individual height, or shared hidden loop |
| C-004 | N3 outer/bottom containment, K80 at CL-003, R5/R7/R9 owner routing | N3/K80 are not source footprints or source centers |
| CL-001/002/003 | 127 source-visible contact samples plus independent hidden closure | No snap anchor or shared source loop |
| Bottom | Flat undecorated Z=0 N3-bounded cap | No source-authored underside |
| C-005/006/007 | Face-owned later UV/BaseColor/Normal consumers | No Step 12 geometry, cross-face copy, or emissive approval |

## Construction Stack

| Order | Component | Visible span | Hidden overlap span | Construction result planned for Step 12 |
|---:|---|---:|---:|---|
| 1 | C-004 apron | Z 0–10 cm | Z 0–10.5 cm | N3/K80 transition shell with source-owned inward silhouette refinement and flat bottom |
| 2 | C-003 lower tier | Z 10–23 cm | Z 9.5–23.5 cm | Independent watertight faceted course; K80 only at CL-003 |
| 3 | C-002 upper tier | Z 23–35 cm | Z 22.5–35.5 cm | Independent watertight faceted course; never copied from C-003 |
| 4 | C-001 body | Z 35–220 cm | Z 34.5–220 cm | Front/left owner-view faceted envelope with hidden bottom cap |
| 5 | C-005/006/007 | face-owned only | none | Zero Step 12 vertices; later Step 14 texture/material decision |

Every contact receives exactly 1 cm of planned positive hidden intersection:
0.5 cm from each adjacent component. Allowed visible exposure is zero pixels.

## Planned Topology And Runtime

- Four DCC objects: `C001_BODY`, `C002_UPPER_TIER`, `C003_LOWER_TIER`, and
  `C004_APRON`.
- Each object must be independently watertight.
- Runtime package: one Unreal Static Mesh containing four disconnected,
  positively overlapping shells.
- Every Step 12 vertex must resolve to exactly one of fourteen authority
  groups in `STEP_11_VERTEX_AUTHORITY_MAP.json`.
- C-004 uses a 32-column by 3-row planned transition lattice before caps and
  source-owned silhouette refinement.
- Back and right views remain validation holdouts; they cannot silently replace
  front/left construction ownership.

## Performance Plan

| Level | Triangle target | Primary preservation rule |
|---|---:|---|
| LOD0 | 8,000; hard cap 10,000 | All source-critical silhouettes and four-layer read |
| LOD1 | 4,000 | Preserve C-001, course separation, and N3 outline |
| LOD2 | 1,800 | Preserve main taper and stepped base |
| LOD3 | 700 | Preserve 220/140/110 macro silhouette first |

Planning-level support:

- one material slot;
- 2K Base Color, Normal, and packed ORM name plan;
- emissive absent unless Step 14 later approves it;
- four custom convex collision hulls planned;
- no UV, material, map, LOD, or collision asset exists in Step 11.

## Required Future Review Views

- Front: camera on -Y, looking +Y, +Z up.
- Back: camera on +Y, looking -Y, +Z up.
- Left: camera on -X, looking +X, +Z up.
- Right: camera on +X, looking -X, +Z up.
- Top: camera on +Z, looking -Z, +Y up.
- Perspective: match the source only after the A/B/C/D/E marker orientation
  pass; treat as non-metric corroboration.

All clean comparisons use 10% framing margin. Any underside, side-on plane,
clipping, marker contamination, or orientation mismatch is not review-ready.

## Fail-Closed Step 12 Boundary

Step 12 must block without repair-forward if any vertex lacks authority, any
N3 exceedance occurs, K80 is reused outside CL-003, a back/right holdout fails,
an overlap becomes visible, a shell is not watertight, the LOD0 hard cap is
exceeded, or any A001-A004 asset-specific input/path is accessed.

Step 12 is not authorized in this session. It requires a new visible contract
after the mandatory restart.
