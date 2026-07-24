# Step 11E — Axial Width Intersection Amendment A01 (Proposed)

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Artifact status: `candidate`
- Authority status: `not approved`
- Step 13 authority: `false`
- Unreal authority: `false`

## Why this rule is needed

The first `rune_side` Step 12 build stopped at its pre-save bounds gate.
No `.blend` file or render was accepted.

The authoritative records currently require both:

1. exact top/bottom owner-cell replay using integer half-open pixel edges; and
2. the completed front-owned width `104040/1063 cm`
   (`97.873941674506 cm`).

After the approved Step 11C bottom C02/C03 label correction, the exact bottom
owner domains reach:

- positive-X source edge `x=277`, which maps to
  `+25359750/517681 cm`; and
- negative-X source edge `x=1252`, which maps to
  `-25359750/517681 cm`.

That produces the exact completed width:

`50719500/517681 cm = 97.974428267601 cm`.

The approved front-width boundary is:

`X=±52020/1063 cm = ±25333740/517681 cm`.

The bottom-view owner cells therefore exceed the front-owned boundary by
exactly:

- `26010/517681 cm = 0.050243296548 cm` per side; and
- `52020/517681 cm = 0.100486593095 cm` over the completed width.

The approved depth and height remain exact. This is a cross-view boundary
intersection question only.

## Proposed exact rule

For `SURF_C02_TOP_HALF`, `SURF_C03_TOP_HALF`,
`SURF_C02_BOTTOM_HALF`, and `SURF_C03_BOTTOM_HALF`, apply the existing exact
candidate-depth intersection first. Then intersect every remaining exact
owner cell with the closed front-owned width slab:

`-52020/1063 <= X <= +52020/1063`.

Apply the same width intersection to the stone exterior boundary used by
`CLOSURE_C03_TO_C04_RUNE` and `CLOSURE_C03_TO_C04_METAL`.

The implementation must:

- retain every nonzero-area intersection;
- retain every original cell edge already inside the slab;
- create a new vertex only at an exact owner-edge/width-boundary
  intersection;
- leave protected pixels empty;
- never stretch, shift, smooth, average, resample, or tolerance-weld an owner
  cell;
- never change the approved bottom-view equation or Step 11C label mapping;
- keep C04 at the exact positive-X front-width plane before the one approved
  whole-asset `Rz180`;
- keep polygon count observed rather than limited during this high-poly
  Nanite source stage.

For the currently detected bottom-view overrun, this clips only the outer
half of the two boundary pixels:

- positive side: source `x=277` is intersected at exact source
  `x=555/2` (`277.5`);
- negative side: source `x=1252` is intersected at exact source
  `x=2503/2` (`1251.5`).

No inner stone boundary, protected gap, height station, candidate depth, C04
profile, rotational radius, or label is changed.

## Approval question

May Codex apply this exact width-intersection rule, rebuild both Step 12
high-poly candidates, run the independent saved-file audits, and present the
comparison board while still stopping before Step 13?
