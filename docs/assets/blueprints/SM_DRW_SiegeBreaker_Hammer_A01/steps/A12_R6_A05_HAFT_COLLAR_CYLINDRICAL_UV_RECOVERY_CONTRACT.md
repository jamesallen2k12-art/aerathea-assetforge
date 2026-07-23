# A12 R6 A05 Haft/Collar Cylindrical-UV Recovery Contract

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Parent contract: `SB-AXIAL-A12-R6-A04-FRONT-HALF-DEPTH-MIRROR`
- Proposed contract ID: `SB-AXIAL-A12-R6-A05-HAFT-COLLAR-CYLINDRICAL-UV`
- Date: `2026-07-22`
- Status: `draft; Flamestrike approval required before execution`
- Artifact ceiling if approved: `DCC source candidate pending Flamestrike visual decision`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Decision This Contract Produces

Determine whether one fresh A04-method depth-mirrored mesh can present the
entire haft and collar below the head as one vertically registered cylinder
with complete source-pixel ownership and no visible material break.

## Proposed Exact Correction

1. Rebuild fresh from the immutable source PNGs. Do not load or modify the A04
   A01 blend, mesh, UVs, materials, or derived outputs.
2. Preserve the approved proper-axis duplicate
   `(X,Y,Z)->(X,-Y,Z)`, outward-normal correction, `Y=0` weld, source-derived
   proportions, and existing fail-closed topology gates.
3. Give the complete front haft and all of its collar geometry below the exact
   head transition one component-specific owner. The interval is
   `haft_start <= Z < head_onset`; its current evidence values are
   `27.236723672367237 <= Z < 110.32403240324034 cm`.
4. Derive the haft/collar texture fresh from exact front-source pixels. Apply
   Flamestrike's declared `157.08%` (`pi/2`) horizontal widening rule and use
   nearest exact source-pixel sampling only; no generative fill, painting, or
   background pixel is permitted.
5. Map the front 180-degree cylindrical half to one static UV island spanning
   exact `U=0..1`, with V registered once from the front source's locked rows.
   Preserve those UVs unchanged on the Y-depth-mirrored back half before weld.
6. Within the haft/collar interval, left-source and right-source material
   ownership must both equal `0` faces. They remain permitted only on the
   corresponding head strike faces above `head_onset`.
7. The collar's final front-owned row must meet the first head-owned row with
   geometric gap `0`, missing UV owner `0`, background sample `0`, and vertical
   UV discontinuity `0`.

## Fail-Closed Gates

- one connected closed mesh;
- every final edge has exactly two incident faces;
- internal center faces and duplicate faces: `0`;
- missing Y-depth-mirrored vertices: `0`;
- outward signed volume: positive;
- haft/collar left-owner faces: `0`;
- haft/collar right-owner faces: `0`;
- front-half static cylinder UV range: exact `U=0..1`;
- mirrored-half UV coordinates preserved exactly;
- common front-source V registration on both halves;
- collar-to-head geometric and UV-owner gap: `0`;
- source-background pixels: `0`;
- colored and flat-gray proofs materially independent.

Any failure makes the attempt invalid and stops before visible presentation.

## Required Review

- enlarged colored three-quarter view of the head/upper collar/haft join;
- enlarged left and right join views;
- full colored and independent flat-gray three-quarter views;
- front/back/left/right comparison board;
- validation manifest and independent audit;
- automatic visible-window presentation, then stop for Flamestrike decision.

## Explicit Exclusions

- no reuse or repair of the A04 A01 blend;
- no left/right source ownership on the haft or collar;
- no independent back-source normalization;
- no image generation, TRELLIS, diffusion, image-to-3D, or procedural shader
  coordinate nodes;
- no FBX, Unreal, LOD, collision, packaging, or game-ready escalation;
- no self-approval.
