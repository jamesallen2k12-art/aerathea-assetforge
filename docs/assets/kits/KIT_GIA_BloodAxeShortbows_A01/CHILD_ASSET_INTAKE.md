# KIT_GIA_BloodAxeShortbows_A01 Child Asset Intake

## Source

- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/BloodAxeArmory.png`
- Source region: `BloodAxeArmory.png#Bow_Shortbow_Set`
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Related packages: `SM_GIA_BloodAxeLongbow_A01`, `KIT_GIA_BloodAxeQuivers_A01`, `KIT_GIA_BloodAxeBowParts_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Intake status: first-pass shortbow mini-kit child breakdown complete
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in asset names to keep this hostile sub-faction separate from neutral/civilized Giant culture
- Source-storage guardrail: source concept remains in the external concept folder only. Do not copy, move, edit, embed, or commit the source image for this docs-only package.

## Notes

This intake covers the Giant shortbow subset from the Blood Axe armory catalog. It is a mini-kit for four Giant-scaled shortbow variants plus support pieces, not a single mesh and not a normal humanoid bow package.

Giant scale lock exactly: female Giants 14-15 ft / 427-457 cm; male Giants 14'10"-16'0" / 452-488 cm. Validated baseline references inherited from `SK_GIA_Base_A01`: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5". Normal humanoid compatibility is not required.

All children must preserve Blood Axe hostile raider identity through dark highland wood, sinew, rawhide, scorched leather, blackened iron, dark steel, horn, bone, dull red cloth markers, soot, resin, and grime. They must not import neutral/civilized Giant blue-gray stoneworker language, warm hearth craft presentation, or restrained blue rune language into this hostile sub-faction kit.

This package does not create DCC source, Blender files, FBX exports, Unreal Content assets, Unreal import, runtime source, startup-scene placement, projectile behavior, projectile collision, animation timing, combat stats, combat rules, ammunition counts, source concept copying, or final visual approval.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Variant scope | LOD0 budget | Collision and pivot | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `BloodAxeArmory.png#Shortbow_Hunter_A01` | Hunter shortbow | `SM_GIA_BloodAxeHunterShortbow_A01` | Equipped/display Giant hunter bow | 3.5k-6.5k tris | Equipped collision disabled; display uses one long capsule/box; pivot at grip center | Defined in mini-kit package | 300-335 cm Giant shortbow with sturdy dark wood limbs, heavy grip wrap, horn or iron nocks, one red cloth marker, and controlled bone/horn accent. No combat stats or projectile behavior. |
| `BloodAxeArmory.png#Shortbow_ScoutCompact_A01` | Scout compact bow | `SM_GIA_BloodAxeScoutShortbow_A01` | Compact Giant scout bow, back or side carry reference | 2.8k-5.5k tris | Equipped collision disabled; display uses one narrow capsule/box; pivot at grip center | Defined in mini-kit package | 240-290 cm tighter profile for Blood Axe scouts. Compact relative to Giant longbows only, not normal humanoid scale. Keep hanging detail minimal for clearance. |
| `BloodAxeArmory.png#Shortbow_CampRack_A01` | Camp rack bow | `SM_GIA_BloodAxeCampRackShortbow_A01` | Static camp/armory rack bow | 2.5k-5k tris | One display capsule/box if needed; pivot at grip center, optional future display pivot only by approval | Defined in mini-kit package | Less ornate rack-facing bow for tents, bowyer corners, shelters, and armory dressing. Static prop planning only; no equip, pickup, or combat behavior. |
| `BloodAxeArmory.png#Shortbow_RepairedSpare_A01` | Repaired spare bow | `SM_GIA_BloodAxeRepairedShortbow_A01` | Patched spare bow and repair storytelling | 3.5k-7k tris | One display capsule/box; no per-splint collision; pivot at grip center | Defined in mini-kit package | Giant spare bow with large splints, rawhide wraps, patch plates, replacement nock cap, and uneven curve. Keep repairs readable but not cluttered. |
| `BloodAxeArmory.png#Shortbow_StringCoils_A01` | Bow strings | `SM_GIA_BloodAxeShortbowStringCoil_A01` | Coiled, folded, and tied spare shortbow strings | 350-1.1k tris per coil | One small box/capsule if placed; pivot at coil center | Defined in mini-kit package | Thick sinew/rawhide strings for shelves, trays, and repair benches. Display only; no string deformation, draw timing, or equipped behavior. |
| `BloodAxeArmory.png#Shortbow_StringRack_A01` | Stretched string support | `SM_GIA_BloodAxeShortbowStringRack_A01` | Floor or wall support for shortbow strings | 1.8k-4.5k tris | Grouped boxes/low-count convex hulls for rack; pivot at ground center or back plane | Defined in mini-kit package | Static support showing shortbow strings under workshop tension. No runtime tension simulation, animation timing, or interactive repair behavior. |
| `BloodAxeArmory.png#Shortbow_NockCaps_A01` | Nock parts | `SM_GIA_BloodAxeShortbowNockParts_A01` | Horn caps, bone inserts, iron tip plates, grooves, anchor hooks | 800-2.8k tris per grouped set | One grouped box if needed; pivot at display center | Defined in mini-kit package | Oversized nock repair parts scaled for Giant shortbows. Keep grooves readable and shortbow-proportioned; no draw mechanics defined. |
| `BloodAxeArmory.png#Shortbow_GripWraps_A01` | Grip wraps and bindings | `SM_GIA_BloodAxeShortbowGripWrapBundle_A01` | Leather rolls, rawhide strips, red cloth ties, sinew coils | 600-2k tris | One grouped box/capsule if needed; pivot at bundle center | Defined in mini-kit package | Reusable grip and repair wrapping stock. Broad strips should read at distance; stitch and fiber detail belongs in textures. |
| `BloodAxeArmory.png#Shortbow_RepairPieces_A01` | Repair pieces | `SM_GIA_BloodAxeShortbowRepairPieces_A01` | Splints, wedge blocks, patch plates, clamp blocks, resin pot | 1.2k-4.5k tris per grouped set | One grouped box/capsule; no per-small-piece collision | Defined in mini-kit package | Crude repair set for shortbow benches and racks. Keep distinct from the larger `KIT_GIA_BloodAxeBowyerTools_A01` tool package. |
| `BloodAxeArmory.png#Shortbow_RackSupport_A01` | Shortbow rack/support | `SM_GIA_BloodAxeShortbowRackSupport_A01` | Floor rack, low cradle, and support stand variants | 3k-7k tris | Grouped boxes/low-count convex hulls for feet, uprights, and crossbars; pivot at ground center | Defined in mini-kit package | Giant-scale static rack/support pieces for the four shortbows and repair props. Preserve broad feet and crossbars; avoid dense per-part collision. |

## Display, Socket, and Import Planning Rules

- All children are static mesh planning targets in this task.
- Equipped shortbow variants should plan around `socket_bow_grip`, `socket_arrow_rest`, `socket_arrow_nock`, `socket_string_top`, `socket_string_bottom`, `socket_string_pull_ref`, `bow_grip_l`, `bow_string_pull_r`, and `arrow_nock`, but final socket naming and ownership are deferred to `SK_GIA_Base_A01` or a future Blood Axe archer task.
- Back or side carry review may reference `back_large_weapon`, `back_quiver`, and future shortbow carry sockets, but no attachment implementation is authored here.
- Rack and support props are world static dressing with ground-centered pivots unless a future wall-mounted variant approves a back-plane pivot.
- Shortbow support pieces may reuse `KIT_GIA_BloodAxeBowParts_A01` material families, but they must remain shortbow-proportioned and Giant-scaled.
- Collision remains simple: one capsule/box for bows and bundles, grouped boxes or low-count convex hulls for rack supports, and no per-string, per-nock, per-splint, per-lashing, or projectile collision.
- Material reuse is required across shortbows, strings, nocks, grip wraps, repair pieces, and rack supports.

## Immediate Package Priority

The mini-kit package is ready for future child-package split work. Suggested promotion order:

1. `SM_GIA_BloodAxeHunterShortbow_A01`
2. `SM_GIA_BloodAxeScoutShortbow_A01`
3. `SM_GIA_BloodAxeCampRackShortbow_A01`
4. `SM_GIA_BloodAxeRepairedShortbow_A01`
5. `SM_GIA_BloodAxeShortbowRackSupport_A01`
6. `SM_GIA_BloodAxeShortbowStringCoil_A01`
7. `SM_GIA_BloodAxeShortbowStringRack_A01`
8. `SM_GIA_BloodAxeShortbowNockParts_A01`
9. `SM_GIA_BloodAxeShortbowGripWrapBundle_A01`
10. `SM_GIA_BloodAxeShortbowRepairPieces_A01`

## Approval Gates

- Stop before DCC source creation, Blender source creation, FBX export, Unreal Content asset creation, Unreal import, material authoring, runtime source changes, startup-scene placement, validator creation, final visual approval, or source-concept copying.
- Stop before defining projectile behavior, projectile collision, combat rules, combat stats, ammunition counts, arrow damage, hit logic, pickup behavior, loot behavior, inventory behavior, bow draw distance, release timing, reload timing, repair interaction timing, or animation montage timing.
- Stop if the four shortbow variants, strings, nocks, grip wraps, repair pieces, and rack supports collapse into one single mesh assumption.
- Stop if shortbows appear sized for normal humanoids instead of female Giants 14-15 ft / 427-457 cm and male Giants 14'10"-16'0" / 452-488 cm.
- Stop if collision becomes dense per-string, per-nock, per-splint, per-lashing, per-repair-piece, or projectile collision.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock, `SK_GIA_Base_A01` assumptions, `SM_GIA_BloodAxeLongbow_A01` support relationship, or `KIT_GIA_BloodAxeQuivers_A01` dependency without a new approval task.
