# A005 A06 Top-Projection Rejection / A07 Restart Handoff

Status: `authoritative Core recovery handoff`

Date: 2026-07-21

## Decision

Flamestrike rejected the exact A06 review image and directed comparison with
the original top-down view to determine the rings' required projection.

The comparison confirms that A06's whole-shell maximum bounds were correct,
but its visible upper crowns were not. C002's visible crown was only
`116 x 87 cm` against the authoritative `123.846154 x 92.707424 cm` exterior
target. C003's visible crown was only `130 x 99 cm` against the authoritative
`137.307692 x 105.196507 cm` exterior target.

## Core Recovery

- Last Core-valid state: unchanged source/top panel, authoritative A06
  exterior-edge measurement record, exact A04 plinth visual construction,
  and non-conflicting Step 11/14 rules.
- First drift: A06 tapered the exterior target inward before the visible top
  crown and validated only whole-component maximum bounds.
- Invalid assumption: maximum bounds anywhere on a shell prove its top-visible
  silhouette.
- A06 package and exact final image: `quarantined`.
- A06 validation: `proof only`; invalid as top-view silhouette authority.
- A06 exterior measurement record: remains `authoritative`; its geometry
  application was invalid.
- A06 diagnostic board/audit: `proof only`.

## Authorized A07 Boundary

Build a fresh isolated A07 correction from the exact A04 plinth plus the
unchanged source and exterior-measurement authorities. Do not load or modify
the A06 Blender/FBX package as geometry input.

The top-visible outer crown of C002 must reach
`123.846154 x 92.707424 cm`; C003 must reach
`137.307692 x 105.196507 cm`; C004's visible peripheral crown must reach the
approved `140 x 110 cm` envelope. A true orthographic top render and a
top-band geometry measurement must pass before the final review render.

Preserve the exact A04 plinth geometry/UV signatures, source-owned RGB, oval
masonry treatment, overall `140 x 110 x 220 cm` bounds, pivot, LOD/collision/
FBX requirements, and the Unreal firewall.

## Stop Boundary

End with one audited A07 DCC review image for Flamestrike approval. Do not
perform Unreal/Step 17 work or classify the asset as `Fully game-ready`.
