# KIT_GIA_BloodAxeBowParts_A01 Child Asset Intake

## Source

- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/BloodAxeArmory.png`
- Source region: `BloodAxeArmory.png#BowStaveParts_Set`
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Related support asset: `SM_GIA_BloodAxeLongbow_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Intake status: first-pass bow-parts mini-kit child breakdown complete
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in asset names to keep this hostile sub-faction separate from neutral/civilized Giant culture
- Source-storage guardrail: source concept remains in the external concept folder only. Do not copy, move, edit, embed, or commit the source image for this docs-only package.

## Notes

This intake covers the bow-parts subset from the Blood Axe armory catalog. It is a practical mini-kit for static rack/workshop dressing and longbow support, not a combat or projectile package. The child split keeps strings, limbs, arrow shafts, heads, wraps, racks, repair pieces, nock parts, and bundle variants separate enough for later DCC and Unreal reuse.

Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

All children must preserve Blood Axe hostile raider identity through dark highland wood, sinew, rawhide, scorched leather, blackened iron, dark steel, horn, bone, torn red cloth markers, soot, resin, and grime. They must not import neutral/civilized Giant blue-gray stoneworker language into this sub-faction kit.

This package does not create DCC source, FBX exports, Unreal Content assets, runtime source, startup-scene placement, projectile stats, combat rules, ammunition counts, animation timing, or copied concept art.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Variant scope | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| `BloodAxeArmory.png#BowParts_StringCoils_A01` | Bow strings | `SM_GIA_BloodAxeBowStringCoil_A01` | Coiled, folded, and tied spare strings | Defined in mini-kit package | Thick sinew/rawhide string coils for shelves, trays, and repair benches. Display only; no string deformation, draw timing, or equipped behavior. |
| `BloodAxeArmory.png#BowParts_StringRack_A01` | String rack | `SM_GIA_BloodAxeBowStringRack_A01` | Stretched strings on floor or wall rack | Defined in mini-kit package | Static rack showing longbow/shortbow support strings under workshop tension. Use simple rack collision and no runtime tension simulation. |
| `BloodAxeArmory.png#BowParts_ReplacementLimbs_A01` | Replacement limbs | `SM_GIA_BloodAxeReplacementLimb_A01` | Upper/lower limb sections and repaired limb variants | Defined in mini-kit package | Curved Giant longbow limb parts with horn/iron tips, repair scars, and broad Blood Axe wraps. Fit visually to `SM_GIA_BloodAxeLongbow_A01`. |
| `BloodAxeArmory.png#BowParts_StaveBlanks_A01` | Stave blanks | `SM_GIA_BloodAxeStaveBlank_A01` | Rough blanks, shaped blanks, and split-stave parts | Defined in mini-kit package | Dark highland wood blanks sized for Giant longbows and shortbows. Use large wood forms; keep fine grain in texture/normal detail. |
| `BloodAxeArmory.png#BowParts_ArrowShafts_A01` | Arrow shafts | `SM_GIA_BloodAxeArrowShaftSet_A01` | Loose shaft groups, drying shafts, and tied shaft bundles | Defined in mini-kit package | Giant-scale shaft stock for racks and benches. Static dressing only; no projectile stats, launch behavior, hit logic, or ammunition counts. |
| `BloodAxeArmory.png#BowParts_ArrowHeads_A01` | Arrow heads | `SM_GIA_BloodAxeArrowHeadTray_A01` | Broadhead, barbed, bodkin, blunt, and unfinished head displays | Defined in mini-kit package | Large blackened iron heads displayed in a tray or on rough backing. Use a limited shape set, not dense unique micro-variants. |
| `BloodAxeArmory.png#BowParts_Wraps_A01` | Wraps and bindings | `SM_GIA_BloodAxeWrapBundle_A01` | Leather rolls, red cloth ties, sinew coils, and rawhide strips | Defined in mini-kit package | Reusable grip and repair wrapping stock. Broad strips should read at distance; stitch/fiber detail belongs in textures. |
| `BloodAxeArmory.png#BowParts_NockCaps_A01` | Nock parts | `SM_GIA_BloodAxeBowNockParts_A01` | Horn caps, bone inserts, iron tip plates, string grooves, and anchor hooks | Defined in mini-kit package | Oversized nock repair pieces that visually support longbow tips. No animation or draw mechanics are defined. |
| `BloodAxeArmory.png#BowParts_RepairPieces_A01` | Repair pieces | `SM_GIA_BloodAxeBowRepairPieces_A01` | Splints, clamps, resin pot, wedges, patch plates, and alignment blocks | Defined in mini-kit package | Crude repair set for bowyer benches and racks. Keep this distinct from a future dedicated bowyer tools kit. |
| `BloodAxeArmory.png#BowParts_FloorRack_A01` | Bow parts rack | `SM_GIA_BloodAxeBowPartsRack_A01` | Floor-standing rack for limbs, strings, shafts, wraps, and repair parts | Defined in mini-kit package | Giant-scale rack with stable feet, broad crossbars, and controlled child-part density. Use grouped boxes or low-count convex collision. |
| `BloodAxeArmory.png#BowParts_WallRack_A01` | Wall rack | `SM_GIA_BloodAxeBowPartsWallRack_A01` | Wall-leaning or wall-mounted storage | Defined in mini-kit package | Static camp/workshop dressing for vertical display. Pivot at back-plane center for wall snapping; avoid per-part collision. |
| `BloodAxeArmory.png#BowParts_WorkbenchCradle_A01` | Workbench cradle | `SM_GIA_BloodAxeBowWorkbenchCradle_A01` | Low cradle for stave repair and nock fitting | Defined in mini-kit package | Support cradle for showing repaired longbow limbs and clamp points. No interactive repair behavior or animation timing. |
| `BloodAxeArmory.png#BowParts_LimbBundle_A01` | Limb bundle | `SM_GIA_BloodAxeLimbBundle_A01` | Tied spare limb and stave bundle variants | Defined in mini-kit package | Static bundle with 2-5 readable limb/stave silhouettes, red cloth tie, and simple collision. |
| `BloodAxeArmory.png#BowParts_ArrowPartsBundle_A01` | Arrow-parts bundle | `SM_GIA_BloodAxeArrowPartsBundle_A01` | Shaft/head/wrap mixed bundle variants | Defined in mini-kit package | Useful shelf or rack filler that suggests supply stock without defining projectile behavior or ammunition quantity. |
| `BloodAxeArmory.png#BowParts_MixedRepairBundle_A01` | Mixed repair bundle | `SM_GIA_BloodAxeBowPartsBundle_A01` | Combined strings, wraps, nocks, splints, and small trays | Defined in mini-kit package | Compact reusable prop for shelves, carts, and benches. Keep material slots shared and avoid cluttered one-off detail. |

## Display And Support Rules

- All children are static dressing or longbow support references in this task.
- `SM_GIA_BloodAxeLongbow_A01` remains the longbow scale and nock/string reference; this kit supplies spare and repair parts around it.
- Arrow shafts and heads are workshop parts only here. Do not infer projectile stats, combat behavior, ammo counts, hit detection, or inventory data.
- Racks should hold readable part clusters, not dense per-piece simulation.
- Bundles should imply volume through grouped silhouettes, atlased textures, and a few true parts rather than many unique meshes.
- Collision remains simple: one box/capsule for bundles and trays, grouped boxes or low-count convex hulls for racks, and no per-shaft/per-head/per-string collision.
- Material reuse is required across strings, limbs, shafts, heads, wraps, nocks, repair pieces, racks, and bundles.

## Immediate Package Priority

The mini-kit package is ready for future child-package split work. Suggested promotion order:

1. `SM_GIA_BloodAxeBowPartsRack_A01`
2. `SM_GIA_BloodAxeReplacementLimb_A01`
3. `SM_GIA_BloodAxeStaveBlank_A01`
4. `SM_GIA_BloodAxeArrowShaftSet_A01`
5. `SM_GIA_BloodAxeArrowHeadTray_A01`
6. `SM_GIA_BloodAxeBowStringCoil_A01`
7. `SM_GIA_BloodAxeBowStringRack_A01`
8. `SM_GIA_BloodAxeWrapBundle_A01`
9. `SM_GIA_BloodAxeBowNockParts_A01`
10. `SM_GIA_BloodAxeBowRepairPieces_A01`
11. `SM_GIA_BloodAxeBowPartsWallRack_A01`
12. `SM_GIA_BloodAxeBowWorkbenchCradle_A01`
13. `SM_GIA_BloodAxeLimbBundle_A01`
14. `SM_GIA_BloodAxeArrowPartsBundle_A01`
15. `SM_GIA_BloodAxeBowPartsBundle_A01`

## Approval Gates

- Stop before DCC source creation, FBX export, Unreal Content asset creation, material authoring, runtime source changes, startup-scene placement, validator creation, or source-concept copying.
- Stop before defining projectile stats, projectile behavior, combat rules, ammunition counts, bow draw distance, release timing, reload timing, repair interaction timing, inventory behavior, pickup behavior, or loot behavior.
- Stop if strings, limbs, arrow shafts, heads, wraps, racks, repair pieces, nock parts, and bundle variants collapse into one single mesh assumption.
- Stop if collision becomes dense per-shaft, per-head, per-string, or per-small-repair-piece collision.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock, `SK_GIA_Base_A01` assumptions, or `SM_GIA_BloodAxeLongbow_A01` support relationship without a new approval task.
