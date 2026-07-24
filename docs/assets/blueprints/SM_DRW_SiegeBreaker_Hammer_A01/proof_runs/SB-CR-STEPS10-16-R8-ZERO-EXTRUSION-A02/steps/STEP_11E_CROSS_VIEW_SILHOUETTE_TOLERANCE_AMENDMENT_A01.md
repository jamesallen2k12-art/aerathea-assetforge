# Step 11E — Cross-View Silhouette Tolerance Amendment A01

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Artifact status: `authoritative`
- Scope: Step 12 high-poly DCC source reconstruction only
- Step 13 authority: `false`
- Unreal authority: `false`

## Flamestrike approval

Codex proposed:

> Cross-view silhouette differences may pass when they are within one source
> pixel per side, below 0.25% of the asset dimension, and no more than 2 mm.
> Pivot, scale anchor, orientation, component labels, protected gaps,
> symmetry operations, and matching seams remain exact. Expected and observed
> dimensions are always recorded. Keep the measured geometry instead of
> trimming it.

Flamestrike replied:

> agreed ... proceed with this change

This approval authorizes only the rule below and resumption of the already
approved Step 12 dual-candidate high-poly build. It does not authorize
clipping, rescaling, smoothing, retopology, UVs, baking, export, selection,
Step 13, or Unreal work.

## Controlling principle

Pixel-exact source ownership remains evidence. A cross-view raster silhouette
is not treated as engineering/CAD truth when two approved views differ by a
sub-pixel amount. The measured owner geometry is preserved, and the
disagreement is reported rather than hidden.

## Exact tolerance rule

This rule applies only when a completed silhouette dimension is reconstructed
from an approved secondary view and compared with an approved controlling
dimension from another view.

Let:

- `E` be the approved controlling completed dimension in centimeters;
- `O` be the observed completed dimension replayed from exact owner cells;
- `S` be the exact centimeter-per-source-pixel scale of the secondary view;
- `D=abs(O-E)` be the completed absolute difference;
- `Dminus` and `Dplus` be the absolute negative- and positive-side boundary
  differences from the centered controlling envelope;
- `P=max(Dminus,Dplus)/S` be the maximum per-side difference in source pixels;
- `R=D/E` be the completed relative difference.

The cross-view silhouette dimension passes only when all three limits pass:

1. `P <= 1` source pixel per side;
2. `R <= 1/400` (`0.25%`);
3. `D <= 1/5 cm` (`2 mm`).

Equality at a limit passes. Failure of any one limit blocks the candidate.

The audit must record `E`, `O`, `D`, `Dminus`, `Dplus`, `S`, `P`, and `R`
using exact fractions where the source equations permit them, plus readable
decimal values.

## Exact constraints not relaxed

This amendment does not add tolerance to:

- the world `(0,0,0)` pivot;
- the fixed `170 cm` overall-height scale anchor;
- candidate-specific right-view depth;
- world-axis orientation;
- Step 11C component labels and bottom-view equation;
- source-owner membership;
- protected negative spaces;
- the single local C04 `Y` mirror;
- the single whole-asset `Rz180`;
- the exact `64` positive-X angular divisions;
- coordinate-equal matching seams and contacts;
- closure topology and manifold checks;
- forbidden-method checks;
- file hashes, output inventory, or stage locks.

Polygon count remains observed rather than limited only because Step 11B
already authorizes the high-poly Nanite source stage.

## Current width decision

For the current Step 12 candidates:

- controlling front-owned width:
  `E=104040/1063 cm = 97.873941674506 cm`;
- observed exact corrected-bottom owner width:
  `O=50719500/517681 cm = 97.974428267601 cm`;
- axial-view pixel scale:
  `S=52020/517681 cm = 1.004865930952 mm`;
- completed difference:
  `D=52020/517681 cm = 1.004865930952 mm`;
- difference per side:
  `Dminus=Dplus=26010/517681 cm = 0.502432965476 mm`;
- per-side source-pixel difference:
  `P=1/2`;
- completed relative difference:
  `R=1/974 = 0.102669404517%`.

All three tolerance limits pass. The exact measured bottom owner cells remain
unchanged. No width clipping is permitted or required.

## Prior proposal disposition

`STEP_11E_AXIAL_WIDTH_INTERSECTION_AMENDMENT_A01_PROPOSED.md` is rejected as
a production rule and retained as `reference only` evidence of the blocked
alternative. It is not geometry authority.

## Stop conditions

Stop before saving a candidate if:

- any one cross-view tolerance limit fails;
- expected or observed dimensions are not recorded;
- a source cell is clipped, moved, stretched, resampled, or relabeled to make
  the comparison pass;
- an exact constraint listed above fails;
- a protected gap is filled;
- a tolerance weld or unapproved repair is attempted.

Even after both candidates pass and their comparison board is ready:

- candidate selection remains unapproved;
- Step 13 remains locked;
- retopology, UV, baking, export, and Unreal remain locked.
