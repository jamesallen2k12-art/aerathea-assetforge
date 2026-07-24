# Step 11C Bottom-View C02/C03 Label Correction A01

- Date: `2026-07-24`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Amendment ID:
  `SB-CR-R8-STEP11C-BOTTOM-C02-C03-LABEL-CORRECTION-A01`
- Recovery run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Artifact status: `authoritative`
- Decision authority: `Flamestrike`
- Amendment effect:
  `corrects the two reversed bottom-view C02/C03 semantic labels only`
- Coordinate-system change: `none`
- Source-pixel change: `none`
- Measurement change: `none`
- Step 13 authority: `false`
- Unreal authority: `false`

## Exact Clarification And Approval

Codex asked:

> I am not changing positive X to negative X or moving any geometry.
>
> The bottom-view labels are reversed:
>
> - The shape currently labelled C02 should be labelled C03.
> - The shape currently labelled C03 should be labelled C02.
>
> Everything stays exactly where it is. Only those two names switch so the
> same physical parts match across the front, top, and bottom views.
>
> If you approve that label correction, say yes and I’ll record it and resume
> the high-poly build.

Flamestrike responded:

> I aboslutely approve this change if its just a simple mislabeling issue

This response explicitly approves the label-only correction described above
and continuation of the already-approved Step 12 high-poly build after the
correction is recorded and independently validated.

## Proven Conflict

The approved source pixels and equations resolve to these world-X sides:

| Stored semantic record | Front | Top | Bottom |
|---|---:|---:|---:|
| `C02` | negative X | negative X | positive X |
| `C03` | positive X | positive X | negative X |

The bottom-view records therefore contain the correct source evidence but have
the C02 and C03 identities reversed relative to the front and top views.

The approved bottom-view equation remains:

`X=(1529/2-x)*52020/517681`

No sign, axis, pixel coordinate, world coordinate, scale, bound, or equation
is changed by this amendment.

## Exact Label-Correction Rule

For Step 12 construction and independent validation, preserve every byte of
the approved Step 09A bottom-view source records while resolving the logical
component identities as follows:

1. logical bottom component `C02_STONE_LEFT` must consume the complete stored
   payload currently identified as `C03_STONE_RIGHT`;
2. logical bottom component `C03_STONE_RIGHT` must consume the complete stored
   payload currently identified as `C02_STONE_LEFT`;
3. logical evidence reference `OWN_BOTTOM_C02` must therefore resolve to the
   exact stored payload and canonical row set of `OWN_BOTTOM_C03`;
4. logical evidence reference `OWN_BOTTOM_C03` must therefore resolve to the
   exact stored payload and canonical row set of `OWN_BOTTOM_C02`;
5. logical boundary reference `BOTTOM_C02_INNER_OWNER_EDGE` must resolve to the
   exact stored ordered boundary payload of
   `BOTTOM_C03_INNER_OWNER_EDGE`;
6. logical boundary reference `BOTTOM_C03_INNER_OWNER_EDGE` must resolve to the
   exact stored ordered boundary payload of
   `BOTTOM_C02_INNER_OWNER_EDGE`;
7. within
   `CORR_C02_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES`, the bottom member must use
   the corrected logical C02 boundary payload described in item 5; and
8. within
   `CORR_C03_FRONT_TOP_BOTTOM_INNER_OWNER_EDGES`, the bottom member must use
   the corrected logical C03 boundary payload described in item 6.

The stored records are not renamed, rewritten, rehashed, resampled, reflected,
or moved. The builder and validator apply this additive semantic-resolution
map after verifying the original byte-locked evidence.

## Authority Preserved Without Change

This amendment is additive. It does not edit or replace:

- the Step 11 construction blueprint;
- the Step 11 authority lock;
- the Step 09A scanline or boundary evidence;
- the approved Step 12 contract or approval record;
- the Step 11B high-poly Nanite amendment;
- any front, top, left, right, or axial ownership record;
- either candidate's approved dimensions;
- the exact `64` positive-X angular divisions;
- protected negative spaces;
- the zero-extrusion rule;
- the one C04 local `Y=0` mirror;
- the one whole-asset Rz180 completion;
- coordinate-equal seam welding only;
- pivot `(0,0,0)` and exact `170 cm` height; or
- the stop before Step 13.

## Construction Effect

After this amendment passes independent validation:

- `SURF_C02_BOTTOM_HALF` uses the corrected logical C02 payload, which lies on
  the same negative-X side as front/top C02;
- `SURF_C03_BOTTOM_HALF` uses the corrected logical C03 payload, which lies on
  the same positive-X side as front/top C03;
- `CLOSURE_C02_INNER` and `CLOSURE_C03_INNER` use their corrected ordered
  bottom boundary payloads; and
- `CLOSURE_C03_TO_C04_RUNE` and `CLOSURE_C03_TO_C04_METAL` use the corrected
  positive-X bottom C03 owner rather than crossing the central structure.

This is a semantic correction only. It supplies no new contour, shape,
coordinate, smoothing rule, topology shortcut, or visual interpretation.

## Amended Production Entry Point

The only permitted Step 12 production entry point now verifies both additive
amendments:

```text
python3 Tools/DCC/build_siegebreaker_r8_step12_source_geometry_a01.py \
  --blueprint docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/manifests/STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json \
  --amendment docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/STEP_11B_HIGH_POLY_NANITE_PERFORMANCE_AMENDMENT_A01.md \
  --parity-amendment docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/proof_runs/SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02/steps/STEP_11C_BOTTOM_C02_C03_LABEL_CORRECTION_A01.md \
  --candidate {rune_side|metal_center_piece_side} \
  --output-root SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A12_R10_R8_Step12_SourceGeometry_A01/run_a/{candidate}
```

The builder and independent validator must stop before geometry if:

- this amendment does not hash-match its independent validation record;
- either corrected logical owner fails its expected world-X side;
- either exact stored payload changes;
- an unapproved owner or boundary substitution occurs; or
- any other controlling authority fails.

## Additional Allowed Records

Flamestrike's approval of recording this correction and resuming Step 12
authorizes these additive records:

- this amendment;
- `../manifests/STEP_11C_BOTTOM_C02_C03_LABEL_CORRECTION_A01_VALIDATION.json`;
- additive correction-clearance events in
  `../manifests/STEP_12_SOURCE_GEOMETRY_A01_EVENT_TRACE.jsonl`; and
- additive references in the final Step 12 manifest, output record, and
  handoff.

## Block Disposition And Resume State

The historical parity block remains preserved:

`Blueprint block: source authority conflicting — bottom-view C02/C03 world-ownership parity`

This exact amendment resolves that block as a confirmed mislabeling issue.
After independent validation, Step 12 may resume from:

`STEP_12_AUTHORITY_VERIFIED`

The high-poly build remains limited to both separate Step 12 candidates,
technical audits, proof renders, the visible comparison board, a scoped
checkpoint/commit/push, and the stop before Step 13.
