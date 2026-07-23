# A12 R10 R8 Zero-Extrusion Reset Handoff

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Status: `authoritative reset handoff`
- Last valid production state:
  `SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01 Step 09`
- Next permitted entry:
  `Step 10 only after the authority and zero-extrusion checks below pass`
- DCC / export / Unreal authority at reset:
  `false / false / false`

## First Message After Reset

The next agent must perform the Aerathea resume handshake, then report in plain
English:

1. exact new-image scanline evidence through Step 09 is valid;
2. Steps 10-16 and the final board are invalid and quarantined;
3. the failure was an unauthorized extrusion/cross-section method;
4. the next construction must replay yesterday's zero-extrusion component
   process with only the new measurements substituted.

Do not show the rejected board as a candidate. Do not begin Blender during the
resume handshake.

## Exact Process Authority To Read — Do Not Paraphrase Or Replace

Read these files completely and verify the recorded SHA-256 values before
writing a new Step 10 or Step 11 artifact:

1. Sixteen-step production plan:
   `SM_DRW_SiegeBreaker_Hammer_A01_STEPS_01_16_PROOF_OF_CONCEPT_PIPELINE_PLAN.md`
   — SHA-256
   `53046eb839b94d9548dfc2e49471b3605a2fc882228ca5e4291db7390e584a2a`.
2. Yesterday's component reconstruction plan:
   `SM_DRW_SiegeBreaker_Hammer_A01_A12_R7_COMPONENT_GEOMETRY_RECOVERY_PLAN.md`
   — SHA-256
   `b0b077c8d39a07e5d1ab12309e77560afa1c407fe3bb3e6272a0c4e6d568b22e`.
3. Flamestrike-approved component equations:
   `steps/A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_DRAFT.md`
   — approved byte hash
   `a40d0b67d802687ac3c9ec9ad8e00a915cc1dc730ce31f3fab00b18a1837a21c`.
4. Approval proof:
   `steps/A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_A01_APPROVAL_RECORD.md`.
5. Proven complete-half implementation record:
   `steps/A12_R10_A09_PROCESS_COMPLETE_RZ180_A02_OUTPUT_RECORD.md`
   — SHA-256
   `639db9d0c565aae7b974dab6fce9fb888f1b8412c77bbb2f6046413a7dbdff52`.
6. Proven process implementation, to be used as algorithmic reference only:
   `Tools/DCC/build_siegebreaker_a12_r10_a09_process_complete_rz180.py`
   — SHA-256
   `088ec22595437611e4f0e136db13b49d32ce3caaf8224c60f145f1c15153f235`.
7. Proven independent audit:
   `Tools/DCC/audit_siegebreaker_a12_r10_a09_process_complete_rz180.py`
   — SHA-256
   `6db37706e87021cf1ea978091c1e7b9f30c21163a5d5bd64bb6b32919ee352e0`.
8. New-data execution boundary:
   `steps/A12_R10_R8_PIXEL_EXACT_STEPS01_16_A01_CONTRACT.md`
   — SHA-256
   `77b0339126388be01f59532cd6b79228450b61e739ebc10c2f849833fd337bd4`.

## Flamestrike-Approved Authority Reconciliation

On `2026-07-23`, Flamestrike approved the authority-only correction recorded
in:

`steps/A12_R10_R8_ZERO_EXTRUSION_AUTHORITY_RECOVERY_A01_APPROVAL_RECORD.md`.

For this R8 pixel-exact run only:

- the new-data execution-boundary bytes at SHA-256
  `77b0339126388be01f59532cd6b79228450b61e739ebc10c2f849833fd337bd4`
  are the locked contract authority;
- the whole-asset completion transform is exactly one
  `Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)`;
- that R8-specific transform supersedes the older final Y-depth reflection
  clause in
  `steps/A12_R10_STEP02_COMPONENT_EQUATION_CONTRACT_DRAFT.md`;
- every other approved component equation, source-ownership rule, closure
  rule, measurement, and fail-closed gate remains unchanged.

This reconciliation authorizes documentation consistency only. It does not
authorize geometry, Blender, rendering, export, or Unreal work. The next
permitted gate is a fresh Step 10 zero-extrusion production blueprint bound
directly to the valid Step 01-09 evidence.

The old A09 builder imports old approved component meshes. Those meshes are
forbidden in the new build. The next agent must replay its construction logic
fresh against the new measurements; it may not append, scale, or modify an old
`.blend`.

## Authoritative New Data — Preserve Exactly

Use the existing Step 01-09 records under:

`proof_runs/SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01/`

The controlling Step 09 files are:

- `manifests/STEP_09_INTEGRATED_EXACT_MEASUREMENT_INDEX.json`
  — SHA-256
  `5a0a3eea8f877d55216f9efabe15b0ee1cf938e4c15a825a0e218f72ba76839a`;
- `manifests/STEP_09_PRE_GEOMETRY_EXACT_DATA_AUDIT.json`
  — SHA-256
  `260c79857fe059517b4076bcc65b538aef807a7be33a58a4a46edc32c2150fdb`;
- `manifests/STEP_09_DISAGREEMENT_UNKNOWN_MATRIX.json`;
- all Step 02-08 source locks, scanline captures, registrations,
  measurements, validations, and independent audits referenced by the Step 09
  index.

Do not remeasure, resample, resize, normalize, smooth, average, or visually fit
the new pixels unless a hash failure forces a fresh evidence run.

## The Exact Construction Process

Follow this sequence without substituting another modeling technique:

1. Preserve the completed Step 01 charter and firewall.
2. Preserve the Step 02 immutable six-source and full-scanline lock.
3. Preserve the Step 03 pixel-identical source decomposition.
4. Preserve the Step 04 physical-component and source-ownership inventory.
5. Preserve the Step 05 coordinate frame and one uniform scale per whole view.
6. Preserve the Step 06 independent front/back measurements.
7. Preserve the Step 07 independent left/right measurements.
8. Preserve the Step 08 independent top/bottom measurements.
9. Preserve the Step 09 cross-view audit and every explicit block.
10. Resolve Step 09 blocks only with an existing explicit Flamestrike decision.
    Missing authority stops the run; it is never replaced by agent judgment.
11. Write a production blueprint that is a direct parameter substitution into
    the approved R7/R10 component equations and A09 combined-boundary method.
    It must not define a new cross-section, extrusion, primitive, or
    simplification method.
12. Build every physical component fresh from its new owner-view scanlines:
    strike-face half; core; left and right stones; upper coupler/cap; haft;
    ferrule; grip; collar; pommel body; terminal cap; and upper head
    cap/spire. Assemble one coherent source half only.
13. Independently audit the byte-identical Step 12 source for source ownership,
    bounds, contacts, negative spaces, component identity, rotation, six-view
    projection agreement, and the zero-extrusion rule.
14. Define UV/material ownership without changing geometry.
15. Apply the approved source-pixel color registration, exact cylinder wrap,
    and material plan without changing geometry.
16. Only after all preceding gates pass, create LOD/collision/export/reimport
    evidence and present the two completed candidate hammers for Flamestrike's
    final decision.

## Zero-Extrusion Rule

There are zero extrusions in the approved reconstruction.

The next agent must reject the build before Blender if the blueprint or builder
does any of the following:

- pushes a 2D silhouette, scanline fill, rectangle, polygon, or image plane
  through depth;
- copies the same 2D face to a second depth and connects the copies as a prism;
- uses Blender Extrude, Solidify, `bmesh.ops.extrude_*`, a cube, a slab, or a
  rectangular cross-section as a reconstruction shortcut;
- reduces the head to generalized front/right rings or slices;
- chooses segment counts or shape simplifications to satisfy the triangle
  budget before exact source fidelity is proven;
- uses one view to invent a surface owned by another view;
- fills a source-connected negative space;
- uses any Step 10-16 artifact or geometry from the rejected run.

The independent validator must inspect both the blueprint and implementation,
not builder-authored pass booleans. It must fail if any forbidden method is
present.

## Required Surface Construction

- Strike faces:
  build one measured face half about its own measured centerline; duplicate it
  once to form one complete motif.
- Core, stones, and coupler:
  build their separately owned source surfaces and common measured contacts;
  use one combined exterior boundary and no per-component backing walls.
- Hidden closure:
  connect corresponding measured boundary edges only by the approved ruled
  faces inside the owning component domain. A closure may not become a new
  exterior silhouette.
- Rotational components:
  construct exact measured radius-by-Z surfaces using
  `P(z,theta)=(r(z)cos(theta),r(z)sin(theta),z)`.
- Haft:
  use the exact per-source-column cylinder mapping
  `theta(U)=-pi/2+pi*U`,
  `X=r(z)cos(theta)`,
  `Y=r(z)sin(theta)`,
  with the exact `pi/2` flat-diameter-to-half-circumference factor.
- Whole asset:
  create one coherent measured source half, then perform exactly one
  `Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)` completion and weld only
  coordinate-equal seam vertices.

## No-Deviation Stop Rule

If the next agent cannot point from every constructed surface to:

1. a new-image source pixel/scanline owner;
2. an approved equation or closure rule; and
3. an exact Step 01-09 measurement,

the agent must stop before geometry and report the missing authority. It may
not invent, approximate, extrude, simplify, or repair forward.

## Quarantined Inputs

Do not execute or import:

- `Tools/DCC/build_siegebreaker_r8_pixel_exact_steps10_11.py`;
- `Tools/DCC/build_siegebreaker_r8_pixel_exact_steps12_16.py`;
- the corresponding Step 12-16 audit as production authority;
- `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/R8_PixelExact_Steps01_16_A01/`;
- any Step 10-16 blueprint, geometry, texture, render, LOD, collision, export,
  or review asset from `SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01`.

They are preserved only to prove the failure and must not influence the next
shape.
