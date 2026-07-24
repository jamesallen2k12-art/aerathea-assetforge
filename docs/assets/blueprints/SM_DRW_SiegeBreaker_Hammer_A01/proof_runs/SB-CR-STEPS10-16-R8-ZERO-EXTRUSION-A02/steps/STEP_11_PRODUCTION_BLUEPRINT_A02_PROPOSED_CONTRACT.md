# Proposed Step 11 A02 Contract — Write The Construction Instructions Only

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Status: `draft; waiting for Flamestrike approval`
- Input gate: `Step 11 source-authority preflight A02 PASS 119/119`
- Output ceiling: `production blueprint document pending review`
- Blender / geometry / render / export / Unreal authority:
  `false / false / false / false / false`
- Step 12 authority: `false`

## Plain-English Goal

Write the exact instructions that a later Blender step would follow.

Do not build the hammer yet.

## Allowed Work

1. Use only the hash-locked source measurements, approved Step 09A component
   boundaries, approved equations, and approved closure rules.
2. State exactly which source pixels own each visible component surface.
3. State exactly which approved equation creates each non-visible connection.
4. State the exact measurements, axes, stations, and completion transform.
5. State the required no-overlap, protected-gap, no-extrusion, and
   one-visible-surface checks.
6. Independently audit every instruction against its cited evidence.
7. Present the completed blueprint and stop.

## Forbidden Work

- Blender;
- geometry;
- renders;
- exports;
- Unreal;
- Step 12;
- old meshes or old component coordinates;
- guessed shapes or hidden surfaces;
- generalized cross-sections;
- slabs or extrusions;
- copied depth faces;
- filling any protected source gap; or
- silently changing an approved Step 09A coordinate.

## Required Outputs

- one Step 11 A02 production-blueprint JSON document;
- one independent blueprint validation;
- one plain-English blueprint review;
- one output record and handoff; and
- no production asset.

## Pass Rule

Every planned surface must cite all three:

1. exact source ownership;
2. an approved equation or connection rule; and
3. an exact measurement.

If any one is missing, stop with:

`Blueprint block: source authority missing`

## Stop

Even if the document passes, do not open Blender or start Step 12. Present the
blueprint for a separate decision.
