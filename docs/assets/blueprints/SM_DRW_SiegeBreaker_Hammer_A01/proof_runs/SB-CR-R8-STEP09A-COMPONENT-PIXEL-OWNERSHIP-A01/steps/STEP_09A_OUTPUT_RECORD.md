# Step 09A Output Record — Exact Component-Pixel Ownership

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Run: `SB-CR-R8-STEP09A-COMPONENT-PIXEL-OWNERSHIP-A01`
- Technical result: `PASS 79/79`
- Artifact status: `candidate`
- Decision status: `pending Flamestrike source-ownership decision`
- Step 11 unlocked: `false`
- Blender / geometry / export / Unreal created:
  `false / false / false / false`

## What Was Produced

The approved measurement-only pass produced:

1. a hash-locked interpretation input covering all six immutable R8 sources;
2. exact half-open owner scanlines for the required front, right, top, and
   bottom component observations;
3. exact exterior-connected protected-space records;
4. thirteen ordered boundary-edge sets and four order-only correspondence
   groups;
5. four source crops with one-pixel marks; and
6. one combined review board with no component fills or hidden-shape preview.

Back and left remain locked non-owning references in this amendment. They were
hash-verified but were not assigned new component ownership.

## Independent Result

The independent validator did not import the builder. It independently:

- decoded all six immutable scanline captures;
- repeated the 4-connected exterior flood;
- rebuilt every candidate component mask;
- proved zero component overlap in every owning view;
- proved every owner pixel is selected source evidence or an exactly enclosed
  source pixel;
- proved all protected pixels are exterior-connected and unowned;
- replayed all thirteen boundary sets and four order-only correspondence
  groups;
- reproduced every marked review and the combined board exactly at the pixel
  level; and
- confirmed that the run contains no Blender, mesh, export, Unreal, or filled
  candidate artifact.

Result: `PASS 79/79`.

## Coordinate Totals

### Front

- `C01_CENTER_CORE`: `46,183` owner pixels.
- `C02_STONE_LEFT`: `71,788` owner pixels.
- `C03_STONE_RIGHT`: `71,689` owner pixels.
- `C06_UPPER_HAFT_CAP`: `6,068` owner pixels.
- reserved existing `C12` visibility: `6,463` owner pixels.
- protected-space records: `308`.

### Right

- metal-center-piece `C04` candidate half: `37,508` owner pixels.
- rune-side `C04` candidate half: `42,029` owner pixels.
- reserved `C01` side visibility: `9,832` owner pixels.
- protected-space records: `0`.

### Top

- `C02_STONE_LEFT`: `141,087` owner pixels.
- `C03_STONE_RIGHT`: `140,054` owner pixels.
- reserved central non-stone visibility: `103,446` owner pixels.
- protected-space records: `463`.

### Bottom

- `C02_STONE_LEFT`: `132,685` owner pixels.
- `C03_STONE_RIGHT`: `133,227` owner pixels.
- reserved central non-stone visibility: `109,361` owner pixels.
- protected-space records: `476`.

## Evidence And Interpretation

- Immutable source pixels, capture memberships, hashes, axes, rectangles, and
  stations remain `authoritative`.
- The new component assignments, contact cuts, and named edge-set
  correspondences are `candidate`.
- The independent validation is `proof only`.
- No hidden surface, ruled face, production blueprint, or geometry has been
  approved or created.

## Internal Review Correction

The first internal combined-board layout was rejected because the final legend
label was clipped. It was a presentation-only defect; the coordinate evidence
and one-pixel marks were unchanged. That board was overwritten before review.
The final board at the hash below has no clipped or overlapping panel.

## Hashes

- Interpretation input:
  `8055611c52e4883127e705f6419b4c8dd09ae7d8c76ba38e4130fafbbd45cbcd`.
- Component scanline file:
  `396adfbaaefc8a8ea35104e5e96dfde322510fb4ce88530fbb32f7f3073b3562`.
- Boundary/correspondence index:
  `e190ed266753c797d4f9ec812154ff3b29f5d5d780e53e235e780c43492d0bd8`.
- Independent validation:
  `1e02aecf558145d4e440b1cdda90513fb28a0075149b1bf24f7ed3c00f7c3e60`.
- Final review board:
  `62d585a56d59b57c0a3d09413fe9e82df28db7005cab25b67489f82d44ff35e5`.

## Required Gate

Stop for Flamestrike to approve, revise, reject, or keep blocked this exact
ownership interpretation. A technical pass does not self-approve the
candidate. Step 11 remains locked.
