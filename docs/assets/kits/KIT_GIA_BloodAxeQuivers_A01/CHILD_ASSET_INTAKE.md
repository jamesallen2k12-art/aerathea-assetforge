# KIT_GIA_BloodAxeQuivers_A01 Child Asset Intake

## Source

- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/BloodAxeArmory.png`
- Source region: `BloodAxeArmory.png#QuiverArrow_Set`
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Intake status: first-pass quiver mini-kit child breakdown complete
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in asset names to keep this hostile sub-faction separate from neutral/civilized Giant culture
- Source-storage guardrail: source concept remains in the external concept folder only. Do not copy, move, edit, embed, or commit the source image for this docs-only package.

## Notes

This intake covers the quiver and arrow subset from the Blood Axe armory catalog. It is a mini-kit, not a single mesh. Belt quivers, back quivers, rack quivers, loose arrows, arrow bundles, display arrow heads, strap variants, and trophy tags each need separate identity so future DCC or Unreal work can reuse parts without overbuilding unique one-off variants.

Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

All children must preserve Blood Axe hostile raider identity through scorched leather, blackened iron, dark steel, rough wood shafts, red cloth warnings, bone/horn tags, soot, and grime. They must not import neutral/civilized Giant blue-gray stoneworker language into this sub-faction kit.

This package does not create DCC source, FBX exports, Unreal Content assets, runtime source, startup-scene placement, projectile behavior, animation timing, or copied concept art.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Variant scope | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| `BloodAxeArmory.png#Quiver_Belt_A01` | Belt quiver | `SM_GIA_BloodAxeBeltQuiver_A01` | Wearable hip or belt carry | Defined in mini-kit package | Shorter angled quiver with scorched leather shell, blackened iron rim, broad belt loop, large buckle, a few visible arrows, and simple display collision. Fit to Giant belt/pelvis clearance. |
| `BloodAxeArmory.png#Quiver_Back_A01` | Back quiver | `SM_GIA_BloodAxeBackQuiver_A01` | Wearable back carry | Defined in mini-kit package | Tall back-carry quiver with reinforced top mouth, bottom cup, wide cross straps, optional trophy tie points, and clearance against Giant shoulders, spine, arms, and back weapon space. |
| `BloodAxeArmory.png#Quiver_Rack_A01` | Rack quiver | `SM_GIA_BloodAxeRackQuiver_A01` | Static camp/armory rack | Defined in mini-kit package | Floor or frame-supported quiver for camp dressing; should read as Giant-scale beside a 470 cm male Giant. Use grouped simple collision and moderate arrow count. |
| `BloodAxeArmory.png#Arrows_Loose_A01` | Loose arrows | `SM_GIA_BloodAxeArrow_A01` | Reusable display arrow set | Defined in mini-kit package | Giant arrows with thick shaft, large fletching, and broadhead/barbed/bodkin/blunt head options. Display geometry only; no projectile behavior defined. |
| `BloodAxeArmory.png#Arrows_Bundle_A01` | Arrow bundle | `SM_GIA_BloodAxeArrowBundle_A01` | Tied bundle prop | Defined in mini-kit package | Cluster of 4-10 visible arrows tied with cord or red cloth. Use a grouped silhouette and one simple collision shape for world dressing. |
| `BloodAxeArmory.png#ArrowHeads_Display_A01` | Display arrow heads | `KIT_GIA_BloodAxeArrowHeads_A01` | Bowyer/armory display variants | Defined in mini-kit package | Large head variants on hide, wood, or iron backing. Use a limited set of readable shapes rather than many tiny unique heads. |
| `BloodAxeArmory.png#Straps_Variants_A01` | Strap variants | `KIT_GIA_BloodAxeQuiverStraps_A01` | Reusable carry straps and buckles | Defined in mini-kit package | Broad scorched leather straps, hide cords, oversized buckles, rings, and anchor patches for belt/back quiver reuse. No unique material slot per strap. |
| `BloodAxeArmory.png#TrophyTags_A01` | Trophy tags | `KIT_GIA_BloodAxeTrophyTags_A01` | Reusable accent tags | Defined in mini-kit package | Bone, tooth, broken token, and red cloth tag clusters used sparingly. Keep tags large enough to read and avoid dense trophy clutter. |

## Attachment And Display Rules

- Belt quiver variants should plan around `belt_quiver_l`, `belt_quiver_r`, `belt_tool_l`, or `belt_tool_r` attachment references, with final socket ownership deferred to `SK_GIA_Base_A01` or a future Blood Axe archer task.
- Back quiver variants should plan around `back_quiver` while respecting `back_large_weapon` space.
- Rack quivers are world static props with ground-centered pivots.
- Loose arrows and arrow bundles are display geometry only in this task and should not define projectile, damage, or ammunition behavior.
- Strap variants and trophy tags should be reusable across quivers and should not force one-off material or mesh duplication.
- Collision remains simple: one capsule/box for quiver bodies or bundles, grouped boxes for rack frames, and no per-arrow collision in clusters.

## Immediate Package Priority

The mini-kit package is ready for future child-package split work. Suggested promotion order:

1. `SM_GIA_BloodAxeBackQuiver_A01`
2. `SM_GIA_BloodAxeBeltQuiver_A01`
3. `SM_GIA_BloodAxeRackQuiver_A01`
4. `SM_GIA_BloodAxeArrow_A01`
5. `SM_GIA_BloodAxeArrowBundle_A01`
6. `KIT_GIA_BloodAxeQuiverStraps_A01`
7. `KIT_GIA_BloodAxeTrophyTags_A01`
8. `KIT_GIA_BloodAxeArrowHeads_A01`

## Approval Gates

- Stop before DCC source creation, FBX export, Unreal Content asset creation, runtime source changes, startup-scene placement, or source-concept copying.
- Stop before defining projectile behavior, combat rules, ammunition counts, animation timing, inventory behavior, pickup behavior, or loot behavior.
- Stop if the mini-kit collapses belt quiver, back quiver, rack quiver, loose arrows, arrow bundle, display arrow heads, strap variants, and trophy tags into one mesh assumption.
- Stop if arrow collision becomes dense per-arrow collision rather than simple display collision.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock or `SK_GIA_Base_A01` attachment assumptions without a new approval task.
