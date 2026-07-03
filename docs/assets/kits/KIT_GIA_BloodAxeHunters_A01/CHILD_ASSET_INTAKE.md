# KIT_GIA_BloodAxeHunters_A01 Child Asset Intake

## Source

- Source concept reference: `GiantBloodAxeHuntersMale.png` routing from existing Giant/Blood Axe slate documentation
- Parent visual language: `KIT_GIA_BloodAxeArmory_A01`
- Approved bow dependencies: `SM_GIA_BloodAxeLongbow_A01`, `SM_GIA_BloodAxeLongbow_A02`, `SM_GIA_BloodAxeLongbow_A03`, `KIT_GIA_BloodAxeShortbows_A01`
- Approved quiver dependency: `KIT_GIA_BloodAxeQuivers_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Intake status: first-pass hunter child planning table complete
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in asset names to keep this hostile sub-faction separate from neutral/civilized Giant culture
- Source-storage guardrail: source concept remains external. Do not copy, move, inspect, edit, embed, or commit the source image for this docs-only package.

## Notes

This intake covers the Blood Axe hunter role kit as planning-only rows. It does not create child production packages, SourceAssets folders, Blender files, FBX exports, Unreal Content, runtime source, validators, startup placements, copied concepts, final visual approval, or a first DCC target selection.

Use the validated `SK_GIA_Base_A01` scale lock exactly: female 442 cm / 14'6" and male 470 cm / 15'5", with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm. Normal humanoid compatibility is not required.

All rows must reuse approved bow/quiver planning instead of redefining ranged mechanics:

- Longbow planning: `SM_GIA_BloodAxeLongbow_A01`, `SM_GIA_BloodAxeLongbow_A02`, `SM_GIA_BloodAxeLongbow_A03`
- Shortbow planning: `KIT_GIA_BloodAxeShortbows_A01`
- Quiver, arrow, strap, and trophy tag planning: `KIT_GIA_BloodAxeQuivers_A01`

Stop before projectile behavior, ammo rules, AI, stealth, patrol logic, combat stats, animation timing, final visual approval, first DCC target selection, trap behavior, pickup logic, loot rules, inventory behavior, crafting, economy, or encounter tuning.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Approved reuse dependency | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| `GiantBloodAxeHuntersMale.png#Role_Archer_A01` | Archer role loadout | `KIT_GIA_BloodAxeHunterArcher_A01` | `SM_GIA_BloodAxeLongbow_A01`, `SM_GIA_BloodAxeLongbow_A02`, `KIT_GIA_BloodAxeQuivers_A01` | Planning only | Giant archer silhouette with approved longbow, back or belt quiver, heavy bracer, sparse red cloth, and limited trophy tags. No projectile behavior, ammo rules, combat stats, AI, or animation timing. |
| `GiantBloodAxeHuntersMale.png#Role_Scout_A01` | Scout role loadout | `KIT_GIA_BloodAxeHunterScout_A01` | `KIT_GIA_BloodAxeShortbows_A01`, `KIT_GIA_BloodAxeQuivers_A01` | Planning only | Cleaner compact Giant scout silhouette using approved scout shortbow and restrained side/back carry. Visual role only; no stealth, patrol logic, AI sensing, or movement rules. |
| `GiantBloodAxeHuntersMale.png#Role_Trapper_A01` | Trapper role loadout | `KIT_GIA_BloodAxeHunterTrapper_A01` | `KIT_GIA_BloodAxeShortbows_A01`, `KIT_GIA_BloodAxeQuivers_A01`, `KIT_GIA_BloodAxeArmory_A01` | Planning only | Hide-wrapped rope, hooks, static trap bundle, and field gear scaled for Giants. Props are visual dressing only; no trap trigger, damage, pickup, crafting, or interaction behavior. |
| `GiantBloodAxeHuntersMale.png#Role_Tracker_A01` | Tracker role loadout | `KIT_GIA_BloodAxeHunterTracker_A01` | `KIT_GIA_BloodAxeQuivers_A01` trophy tag and strap planning | Planning only | Hide cloak, field satchel, bone/horn markers, red tag strand, and terrain-worn gear. Visual tracker identity only; no stealth, patrol logic, AI tracking, scent, or encounter behavior. |
| `GiantBloodAxeHuntersMale.png#Wearable_HideCloak_A01` | Hide-cloak wearable | `SK_GIA_BloodAxeHideCloak_A01` | Reuses Blood Axe hide/leather material language and quiver clearance from `KIT_GIA_BloodAxeQuivers_A01` | Planning only | Broad shoulder mantle and ragged hide/fur cloak that clears back quiver, bow carry, shoulders, and head. No cloth simulation, physics setup, skeletal fit, or animation timing in this task. |
| `GiantBloodAxeHuntersMale.png#Loadout_Quiver_A01` | Quiver loadout | `KIT_GIA_BloodAxeHunterQuiverLoadout_A01` | `KIT_GIA_BloodAxeQuivers_A01`, plus longbow and shortbow packages for scale context | Planning only | Selection plan for back quiver, belt quiver, arrow bundle, broad straps, and reusable arrow/head variants. Must inherit approved quiver dimensions, pivots, collision policy, and no-projectile guardrails. |
| `GiantBloodAxeHuntersMale.png#Accent_TrophyTags_A01` | Trophy tags | `KIT_GIA_BloodAxeHunterTrophyTags_A01` | `KIT_GIA_BloodAxeQuivers_A01` trophy tag planning | Planning only | Reusable bone, tooth, token, and red cloth tag clusters for hunter cloaks, quivers, belts, and racks. Use sparingly; no gore escalation, loot rules, inventory meaning, or one-off material slots. |
| `GiantBloodAxeHuntersMale.png#Camp_RackVariants_A01` | Camp/rack variants | `KIT_GIA_BloodAxeHunterCampRack_A01` | `KIT_GIA_BloodAxeShortbows_A01` camp rack planning and `KIT_GIA_BloodAxeQuivers_A01` rack quiver/arrow bundle planning | Planning only | Giant-scale bow racks, quiver racks, hide drying frame, arrow bundle rests, tag strings, and field-gear pegs for camp dressing. Static props only; no workstation, crafting, loot, AI, or patrol behavior. |

## Display, Socket, and Reuse Rules

- All rows are planning-only and must not be treated as DCC-ready child packages without a separate approval task.
- Archer and scout rows reuse approved longbow/shortbow proportions and do not change bow package budgets, pivots, sockets, or variant identity.
- Quiver loadout and trophy tag rows reuse `KIT_GIA_BloodAxeQuivers_A01` child planning for belt quiver, back quiver, rack quiver, loose arrows, arrow bundle, display arrow heads, strap variants, and trophy tags.
- Candidate attachment references include `back_quiver`, `belt_quiver_l`, `belt_quiver_r`, `belt_tool_l`, `belt_tool_r`, `back_large_weapon`, `hand_l_offhand`, `bow_grip_l`, `bow_string_pull_r`, and `arrow_nock`; final ownership remains deferred to `SK_GIA_Base_A01` or future Blood Axe archer work.
- Camp/rack variants are static dressing with ground-centered pivots unless a future wall/rack variant approves a different pivot.
- Collision remains simple and display-focused: attachment preview bounds for wearables, one capsule/box for bundles, grouped boxes or low-count convex hulls for racks, and no per-arrow, per-tag, per-rope, per-hook, projectile, trap, stealth, patrol, or AI collision.

## Immediate Package Priority

This hunter kit is ready only as docs-only child intake and package planning. Suggested future split order, if the lead approves a later documentation pass:

1. `KIT_GIA_BloodAxeHunterArcher_A01`
2. `KIT_GIA_BloodAxeHunterScout_A01`
3. `SK_GIA_BloodAxeHideCloak_A01`
4. `KIT_GIA_BloodAxeHunterQuiverLoadout_A01`
5. `KIT_GIA_BloodAxeHunterTrophyTags_A01`
6. `KIT_GIA_BloodAxeHunterCampRack_A01`
7. `KIT_GIA_BloodAxeHunterTrapper_A01`
8. `KIT_GIA_BloodAxeHunterTracker_A01`

This order is planning guidance only and does not select or authorize the first DCC target.

## Approval Gates

- Stop before DCC source creation, source folder creation, Blender source creation, FBX export, Unreal Content asset creation, Unreal import, material authoring, runtime source changes, startup-scene placement, validator creation, final visual approval, first DCC target selection, or source-concept copying.
- Stop before projectile behavior, ammo rules, combat stats, combat traces, hit logic, AI, stealth, patrol logic, trap behavior, pickup behavior, loot behavior, inventory behavior, crafting, economy, bow draw distance, release timing, reload timing, or animation timing.
- Stop if archer, scout, trapper, tracker, hide-cloak, quiver loadout, trophy tags, or camp/rack variants collapse into one single mesh assumption.
- Stop if hunter gear appears sized for normal humanoids instead of female 442 cm and male 470 cm Giant baselines.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop before changing approved longbow, shortbow, quiver, or Giant scale-lock assumptions without a new approval task.
