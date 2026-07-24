# Step 11B High-Poly Nanite Performance Amendment A01

- Date: `2026-07-24`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Amendment ID:
  `SB-CR-R8-STEP11B-HIGH-POLY-NANITE-PERFORMANCE-AMENDMENT-A01`
- Recovery run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Artifact status: `authoritative`
- Decision authority: `Flamestrike`
- Amendment effect: `clears the Step 12 pregeometry polygon-cap block only`
- Step 13 authority: `false`
- Unreal authority: `false`

## Exact Flamestrike Direction

Flamestrike stated:

> therefore ignore Polycount Limits in this instance

Flamestrike also stated:

> we can discuss our approach after this asset is complete

Flamestrike then confirmed:

> I am working with UE5 and yes it has Nanite

These statements are the direct authority for this asset-specific amendment.
They do not amend Aerathea's general performance budgets or another asset.

## Core Decision

Step 12 is a high-poly source reconstruction stage for a Nanite-capable Unreal
Engine 5 target. It is not the final optimized LOD0.

For this Step 12 execution only:

1. the Step 11 `8,000`-triangle target is superseded;
2. the Step 11 `10,000`-triangle hard cap is superseded;
3. triangle count is an observed technical metric, not a pass/fail gate;
4. fidelity to the approved source ownership, equations, contacts, protected
   spaces, and silhouette takes precedence over polygon reduction; and
5. the output ceiling is a high-poly `DCC source candidate`.

This amendment does not classify either result as a `DCC game-ready
candidate`, `Fully game-ready`, production Nanite mesh, or approved final
asset.

## Angular Tessellation Authority

The existing hash-locked source-half authority explicitly specifies `64`
positive-X angular divisions. Flamestrike did not supersede that fidelity
rule; only the polygon limit was superseded.

Therefore:

- Step 12 must retain exactly `64` positive-X angular divisions;
- the one whole-asset Rz180 completion supplies the complementary occurrence;
- no `6`, `8`, or other reduced subdivision candidate is authorized;
- no adaptive reduction rule is authorized; and
- continuous proportional source-column U ownership remains mandatory, with
  no nearest-pixel skipping or repetition.

The previously measured `52,736` rotational-triangle lower bound is accepted
as a valid high-poly consequence rather than a performance failure. It remains
a lower bound, not the final observed whole-asset count.

## Authority Preserved Without Change

This amendment changes only the Step 12 topology-budget disposition.

The following remain mandatory and byte-locked:

- authoritative Step 11 construction blueprint SHA-256:
  `2b598497ba5e61a4352c217f3fb20b3545189c710934f3a21d9b7398ddb472c7`;
- Step 11 authority lock SHA-256:
  `3235fcc9480ad246f968b275792aa3a309aa34710b5bfec3fc005980ae3d5069`;
- approved Step 12 contract SHA-256:
  `a3f16266da53ed28a0c849818271dea0c07cd8ba8005e05a6778e2a0f6d2935b`;
- Step 12 approval record SHA-256:
  `2b6fedd15020808beb63ff556c66bc52114a06cd69331f72bfe637caea69e7d7`;
- all `34` authority-file hashes embedded in the Step 11 blueprint;
- all `17` surface instructions;
- all `16` closure, contact, guard, cap, and completion instructions;
- both separate candidate variants;
- exact variant-specific dimensions;
- the zero-extrusion rule;
- the one C04 local mirror;
- the one whole-asset Rz180 completion;
- coordinate-equal seam welding only;
- protected negative-space requirements;
- pivot `(0,0,0)` and exact `170 cm` height;
- fresh isolated output roots;
- independent saved-candidate audits;
- proof renders and the visible comparison board; and
- the stop before Step 13.

No approved Step 11 or Step 12 authority file may be edited to implement this
amendment. The amendment is additive and hash-locked as a new input.

## Block Disposition

The authoritative Step 12 block record remains valid historical evidence:

`Blueprint block: rule missing — performance amendment required`

Flamestrike's direct high-poly/Nanite decision now supplies the missing
performance disposition:

- the inherited `64`-division rule remains authoritative;
- the high-poly source stage has no polygon target or hard cap;
- Step 12 may resume from the last verified state
  `STEP_12_AUTHORITY_VERIFIED`; and
- the prior block must be preserved in the append-only event trace as cleared
  by this exact amendment, never deleted or rewritten.

## Amended Entry Point

The only permitted production entry point now adds this amendment as an exact
hash-verified input:

```text
python3 Tools/DCC/build_siegebreaker_r8_step12_source_geometry_a01.py \
  --blueprint docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json \
  --amendment docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/STEP_11B_HIGH_POLY_NANITE_PERFORMANCE_AMENDMENT_A01.md \
  --candidate {rune_side|metal_center_piece_side} \
  --output-root SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_Step12_SourceGeometry_A01/run_a/{candidate}
```

The builder and independent validator must fail before geometry if the final
amendment hash does not match the hash recorded by the amendment validation.

## Additional Allowed Records

This amendment authorizes only these additive records beyond the original
Step 12 allowed-file list:

- this amendment;
- `../manifests/STEP_11B_HIGH_POLY_NANITE_PERFORMANCE_AMENDMENT_A01_VALIDATION.json`;
- an additive amendment-clearance event in
  `../manifests/STEP_12_SOURCE_GEOMETRY_A01_EVENT_TRACE.jsonl`; and
- additive references to this amendment in final Step 12 manifests, output
  records, and handoffs.

## Deferred High-To-Low And Nanite Decisions

The following remain deferred until the high-poly Step 12 candidates are
complete and reviewed:

- selecting one of the two variants;
- direct Nanite import versus retopology;
- a mid-poly or low-poly derivative;
- production UV unwrapping;
- Normal, AO, Curvature, ORM, or other baking;
- texture and material production;
- production collision;
- LOD policy;
- FBX or GLB export;
- Unreal import and Nanite configuration; and
- gameplay/performance validation.

Nanite capability does not itself authorize skipping later UV, material,
collision, scale, silhouette, or runtime validation decisions.

## Required Stop

After both high-poly candidates pass their independent technical audits and
the visible comparison board opens, stop.

Present:

- both high-poly candidate classifications;
- observed triangle counts;
- all source-fidelity and topology audit results;
- proof renders;
- files created;
- assumptions or interpretations;
- blockers or uncertainty; and
- the exact next review decision.

Do not begin retopology, UVs, baking, export, Unreal, or Step 13 automatically.
