# Siege Breaker A12 R7 Component-Geometry Recovery Plan

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: `2026-07-22`
- Status: `draft plan; Flamestrike approval required before Step 01 execution`
- Starting state: `Core Recovery; A05 A01-A03 invalid/quarantined`
- DCC production authority: `false`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Goal

Reconstruct Siege Breaker from exact source-pixel component measurements so
that one correct physical front half is built and mirrored without stretched
head geometry, duplicated strike-face motifs, stone in the upper haft-cap
negative space, or extruded substitutes for tapered rotational parts.

## Governing Truths

1. The six immutable source images and their locked hashes are the visual
   evidence.
2. Printed centimeter labels do not override the approved pixel scale.
3. The strike face has its own source-image centerline. That centerline must be
   registered to world `Y=0`; the shaft's source-image pixel column cannot be
   substituted for it.
4. Only one measured half of the strike face is constructed. Its division line
   runs down the vertical middle of the face. The opposite half is an exact
   duplicate across that line, producing one complete face motif—not two.
5. The strike-face piece pitches inward toward the head at the bottom and
   preserves its visible narrow-top/wide-bottom geometry. Its pitch and widths
   must be measured before modeling.
6. Center core, left stone, right stone, upper haft cap, haft, grip, collars,
   pommel, and upper head cap/spire are distinct physical components or
   declared joined volumes. A front-X × side-Y Cartesian product is forbidden.
7. Stone occupancy between the two upper haft-cap halves is exactly zero.
8. The pommel and upper head cap/spire are tapered rotational solids derived
   from measured radius-by-Z profiles, not silhouette extrusions.
9. Blender is the only permitted construction software. Image generation,
   TRELLIS, diffusion, generated views, and image-to-3D remain forbidden.

## Component Ledger Required Before Geometry

The measurement pass must assign every source-owned region to one of these
IDs, or explicitly mark it blocked:

- `C01_CENTER_CORE`
- `C02_STONE_LEFT`
- `C03_STONE_RIGHT`
- `C04_STRIKE_FACE_HALF_POSITIVE_X`
- `C05_STRIKE_FACE_HALF_NEGATIVE_X`
- `C06_UPPER_HAFT_CAP`
- `C07_HAFT`
- `C08_GRIP`
- `C09_LOWER_COLLAR`
- `C10_POMMEL_BODY`
- `C11_POMMEL_TERMINAL_CAP`
- `C12_UPPER_HEAD_CAP_SPIRE`

The ledger must record source view, exact half-open pixel bounds, component
centerline, world-Z interval, owning view, mirror plane, rotational axis where
applicable, and blocked/known status. A component ID may not borrow another
component's source axis or bounds.

## Step Sequence And Approval Gates

### Step 01 — Measurement-Only Component Registration

- Scan source pixels only.
- Measure the strike face's own vertical centerline, one half-face bounds,
  top width, bottom width, top/bottom Z stations, and side-view horizontal
  offsets needed to calculate its inward pitch.
- Measure the centered-core/two-stone boundaries and the empty upper haft-cap
  region.
- Measure radius-by-Z profiles for the pommel body, pommel terminal cap, and
  upper head cap/spire.
- Output only source crops, exact marks, tables, formulas, pass/fail findings,
  and blocked unknowns. No filled candidate shape or geometry preview.
- Gate: Flamestrike approves or revises the measurement record.

### Step 02 — Component Geometry Contract

- Convert only approved Step 01 measurements into explicit construction rules.
- Declare the two distinct operations:
  1. component-local half construction/mirror at the registered world plane;
  2. final whole-front-half Y-depth duplicate/weld where still required.
- Declare exactly how the strike-face half becomes one complete face without
  duplicating its motif.
- Declare loft/revolution formulas and zero-occupancy negative spaces.
- Gate: Flamestrike approves the exact contract before Blender runs.

### Step 03 — Isolated Strike-Face Half Proof

- Build only one measured half of one strike face.
- Mirror it across the face centerline.
- Prove one center division, one face motif, correct narrow-top/wide-bottom
  taper, exact inward pitch, and no head-width growth.
- Show source-aligned side, front-edge, and three-quarter gray/color proofs.
- Gate: Flamestrike approves or revises this component.

### Step 04 — Center Core, Stones, And Upper Haft-Cap Proof

- Build the centered core and the two stone components separately.
- Preserve the approved component widths unless Step 01 produces an explicit
  source conflict for decision.
- Prove zero stone occupancy in the upper haft-cap negative space.
- Gate: Flamestrike approves or revises this component assembly.

### Step 05 — Rotational Cap And Pommel Proof

- Build the pommel body, terminal cap, and upper head cap/spire as measured
  tapered surfaces of revolution.
- Prove shared axes, circular sections, top/bottom radii, Z stations, and taper
  direction.
- Gate: Flamestrike approves or revises the rotational components.

### Step 06 — One Complete Physical Front Half

- Assemble only approved isolated components.
- Every visible surface occurs once.
- No facade, overlay, hidden backing, Cartesian-product fill, or unapproved
  inter-component bridge is permitted.
- Run the open-boundary and component-intersection audits before duplication.
- Gate: technical pass plus Flamestrike visual approval of the half.

### Step 07 — Exact Duplicate, Weld, UV, And Complete Review

- Duplicate only the approved physical half using the approved proper-axis
  operation.
- Weld the declared center boundary and recalculate outward normals.
- Apply component-specific static UV rules only after geometry authority is
  locked; preserve approved inherited UVs where the contract requires it.
- Present complete colored and independent gray three-quarter views plus
  front/back/left/right/top/bottom component-aware comparisons.
- Gate: Flamestrike approves, revises, rejects, or blocks the DCC source
  candidate. No automatic escalation follows.

## Fail-Closed Audits

Every applicable step must stop on any of the following:

- a complete strike-face motif exists inside the source half before mirror;
- the completed strike face contains more than one motif;
- face division line differs from the approved face centerline;
- top/bottom face widths or pitch differ from the approved measurements;
- total head width/depth/height exceeds approved pixel bounds;
- stone cells/faces occupy the declared upper haft-cap negative space;
- pommel or upper cap cross-sections are non-circular where rotational;
- tapered rotational radii do not match the approved radius-by-Z table;
- separate component surfaces overlap, duplicate, or leave an undeclared gap;
- any component uses another component's source-image axis;
- any unapproved source, old blend, inferred fill, background pixel,
  procedural coordinate node, image-generation tool, or TRELLIS output is used.

## Explicit Exclusions

- no A04/A05 blend, mesh, UV, material, texture, or derived image as a
  construction input;
- no repair-forward from the monolithic occupancy builder;
- no new geometry before Step 01 measurement approval and Step 02 contract
  approval;
- no FBX, Unreal, LOD, collision, packaging, or game-ready claim;
- no self-approval.

## Exact Next Action After Context Reset

Read the reset state and
`steps/A12_R6_A05_CORE_REASSESSMENT_AND_RECOVERY.md`, then present this R7 plan
for Flamestrike approval or revision. Do not start Step 01 until Flamestrike
approves the plan.
