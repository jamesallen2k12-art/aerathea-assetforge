# A12 R10 R8 Correct-Axis Two-Hammer A01 Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract ID: `SB-A12-R10-R8-CORRECT-AXIS-TWO-HAMMER-A01`
- Date: `2026-07-23`
- Status: `authorized by Flamestrike`
- Output ceiling: `two DCC source candidates pending Flamestrike comparison`
- FBX / Unreal / LOD / collision / game-ready authority:
  `false / false / false / false / false`

## Flamestrike Authorization

Flamestrike rejected the preceding reconstruction because the bisected image
was duplicated around the wrong physical axis and the handle was not scaled
correctly.

Flamestrike explicitly authorized Codex to complete the correction without
intermediate approval and required two completed review hammers:

1. one generated from the rune-side half of the new R8 right image;
2. one generated from the metal-center-piece half of the same image.

This authorization covers the exact reconstruction, repeat audit, rendering,
review-board creation, and visible presentation defined below.

## Core Recovery Findings

The preceding A01 retained the new front-image `X>=0` half and applied:

`Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)`.

That is the wrong source-half axis. The authoritative R8 diamond record
requires the right-view image to be bisected vertically through:

`x=557 px`.

The source half is a depth half in the right-view image:

`Y<=0`.

The same Rz transform then creates the opposite depth half.

The preceding handle ended at original boundary `C`, the straight-shaft
start, at:

`Z=113220/1111 = 101.908190819082 cm`.

The approved boundary `A` is the beginning of the haft including the upper
coupler and belongs at:

`Z=132 cm`.

The omitted handle/coupler span was therefore:

`132 - 113220/1111 = 33432/1111 = 30.091809180918 cm`.

The old candidate also sampled new handle rows through one global `170 cm`
image scale instead of using component-local longitudinal locks.

## Immutable Source Authority

- New R8 front source SHA-256:
  `9a34588afd4fef32001cd9cb2115699e7506ef1e90331c19f4d32483c60aab8c`
- New R8 back source SHA-256:
  `f09dd1ad3978f39e10ecee8ea7efa84336520f0cea4921fe3c410dfd04019694`
- New R8 right source SHA-256:
  `58f3199babbcf9323751d04f0ffafa4316048243cf2f39992cdb6b04176306e8`
- Complete right object rectangle:
  `[418,166,668,1262)`
- Exact diamond-center source edge:
  `x=557`
- New physical envelope:
  `97.873941674506 x 47.479915237376 x 170 cm`

The hash-locked lossless scanline captures remain the source-pixel authority.

## Exact Two Source Halves

### Metal-center-piece candidate

- right-image half-open source interval:
  `[418,557)`
- source span:
  `139 px`
- source seam:
  `x=557 -> Y=0`
- source outer edge:
  `x=418 -> Y=-47.479915237376/2 cm`

### Rune-side candidate

- right-image half-open source interval:
  `[557,668)`
- source span:
  `111 px`
- source seam:
  `x=557 -> Y=0`
- source outer edge:
  `x=668 -> Y=-47.479915237376/2 cm`

Each candidate is built once from its declared `Y<=0` image half. Each is
completed once with:

`Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)`.

Only coordinate-equal seam vertices may weld.

## Exact New-R8 Scanline Stations

The stations below are exact new-image scanline events, not old-image row
substitutions.

### New right-view head station

- complete-source top:
  `166`
- rune-half first owned row:
  `166`
- metal-half first owned row:
  `170`
- `A`, head meets upper coupler:
  `647`
- rule: first post-head span contraction of at least `15 px`
- physical mapping: each candidate's first owned row maps to `Z=170 cm` and
  row `647` maps to `Z=132 cm`. This preserves the exact complete height
  without inventing the four top rows absent from the metal-side half.

### New front-view handle stations

- `A`, upper coupler begins:
  `600`
- `C`, straight haft begins:
  `670`
- `H1`, haft meets ferrule:
  `870`
- `H8`, ferrule meets grip:
  `955`
- `U1`, grip meets lower collar:
  `1110`
- `U3`, lower collar meets pommel:
  `1150`
- `L4`, pommel meets terminal cap:
  `1220`
- terminal:
  `1271`

The repeatable scanline rules are:

- `A`: first row after the full head whose exact selected span is at most
  `120 px` for at least ten consecutive rows;
- `C`: first row after `A` beginning the sustained near-constant shaft span
  of at most `70 px`;
- `H1`: first post-shaft expansion reaching at least `75 px`;
- `H8`: first post-ferrule row beginning the sustained grip span of at most
  `71 px`;
- `U1`: first post-grip expansion reaching at least `78 px`;
- `U3`: first lower-assembly expansion reaching at least `115 px`;
- `L4`: first post-pommel contraction reaching at most `107 px`;
- terminal: exact scanline rectangle bottom edge.

## Corrected Longitudinal Registration

Physical locks:

- `Z_A=132 cm`;
- grip length:
  `42 cm`;
- pommel length:
  `18 cm`;
- total:
  `170 cm`.

The new lower-assembly scale is:

`s_lower = 18/(1271-1150) = 18/121 cm/px`.

Therefore:

- `Z_U3=18 cm`;
- `Z_U1=18+(1150-1110)*18/121 = 2898/121 cm`;
- `Z_H8=Z_U1+42 = 7980/121 cm`.

Rows `A..H8` share one uniform upper-handle scale so their new source-pixel
ratios fill the exact approved `Z_A..Z_H8` interval.

Rows `H8..U1` map to exactly `42 cm`.

Rows `U1..terminal` use the same lower-assembly scale, so the collar, pommel
body, and terminal preserve their new-R8 source-row proportions while the
pommel remains exactly `18 cm`.

## Corrected Radial Registration

- true straight haft radius:
  `2.5 cm`;
- true straight haft diameter:
  `5 cm`;
- pommel maximum radius:
  `5.5 cm`;
- pommel maximum width:
  `11 cm`.

The new front scanlines own the rotational handle profile. One uniform
decorative-handle radial factor registers the measured maximum lower
source radius to `5.5 cm`; the true straight-haft rows remain fixed at
`2.5 cm`.

Every positive-X handle half uses:

`theta(U)=-pi/2+pi*U`, `U in [0,1]`

`X=r(z)cos(theta)`

`Y=r(z)sin(theta)`.

The flat-diameter-to-half-circumference factor remains exactly:

`pi/2`.

## Authorized Outputs

1. Rune-side completed Blender candidate.
2. Metal-center-piece completed Blender candidate.
3. Front, right, and color/gray three-quarter renders for each.
4. One side-by-side two-hammer review board.
5. Validation manifest and independent saved-file audit for each candidate.
6. One comparison/output record.
7. Automatic visible opening of the final comparison board.

## Mandatory Gates

- exact three source hashes and scanline replays;
- exact bisection edge `x=557`;
- source-half axis is `Y`, not front-image `X`;
- exact rune and metal source intervals;
- exactly one Rz180 completion per candidate;
- coordinate-equal seam welding only;
- exact new physical bounds;
- handle top reaches `Z=132 cm`;
- omitted-handle span from the rejected candidate is recorded;
- true haft radius `2.5 cm`;
- exact `pi/2` formula;
- exact `42 cm` grip;
- exact `18 cm` pommel;
- exact `11 cm` pommel maximum width;
- source-background UV samples zero;
- corrected camera framing;
- independent gray proofs differ from color renders;
- no rejected geometry, FBX, Unreal, LOD, collision, or game-ready escalation.

## Stop

After both candidates pass the saved-file audit and the final comparison board
is opened visibly, stop for Flamestrike to compare the rune-side and
metal-center-piece results.
