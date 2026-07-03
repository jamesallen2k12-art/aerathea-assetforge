# KIT_GIA_BloodAxeCaveApproachStandingPair_A01 Implementation Readiness Matrix

## Scope

- Task ID: `AET-MA-20260629-467`
- Asset package: `KIT_GIA_BloodAxeCaveApproachStandingPair_A01`
- Owner lane: Production Package
- Matrix status: docs-only readiness summary.
- This file creates no source asset, DCC source, source-folder creation, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content, material instance, texture asset, validator file, startup placement, runtime source, Blueprint, socket authoring, physics setup, animation asset, material graph, VFX/audio, final cave approval, final visual approval, first implementation target selection, implementation order, or Hermes work.
- This file does not select a source folder, DCC target, Unreal target, validator target, startup placement, final cave approval target, final visual approval target, or cave gameplay/doorway/nav/route/encounter target.

## Source-Of-Truth References

| Reference | Readiness use | Current source status |
| --- | --- | --- |
| `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachStandingPair_A01/PRODUCTION_PACKAGE.md` | Parent package for standing-pair kit scope, art direction, scale, material, LOD, collision, and import-planning guardrails. | Docs-only package source; no build output created by this matrix. |
| `docs/assets/kits/KIT_GIA_BloodAxeCaveApproachStandingPair_A01/CHILD_ASSET_INTAKE.md` | Child row source for all eight planning rows covered below. | Docs-only intake source; no child row is promoted by this matrix. |
| `KIT_GIA_BloodAxeCaveApproachMarkers_A01` | Parent cave approach marker kit and shared static threshold-readability context. | Package/reference source only. |
| `SM_GIA_BloodAxeCaveApproachStandingPair_A01` | Primary standing-pair restraint reference for tall/short asymmetry, Giant-scale massing, and static cave-threshold visual framing. | Package-ready reference only; no implementation target selected. |
| `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01` | Shared material policy for rough highland stone, soot, ash, cave grit, trampled mud, oxide red cloth, rope, rawhide, blackened iron, old horn, and dull bone. | Reference-only policy; no material instance, texture asset, or graph authoring. |
| `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01` | Shared LOD0-LOD3 reduction and disabled/simple collision policy. | Reference-only policy; no validator, collision proxy, UCX mesh, or Unreal setting. |
| `SK_GIA_Base_A01` | Validated Giant scale lock and neutral/civilized Giant culture anchor. | Existing scale dependency only; no character source or runtime edit. |

## Global Art And Scale Guardrails

- female baseline 442 cm / 14'6"
- male baseline 470 cm / 15'5"
- approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm
- Blood Axe is a hostile Giant sub-faction only.
- Blood Axe cave approach standing-pair readiness rows do not replace neutral/civilized Giant culture, cave-town masonry, blue-gray civic stonework, terraces/waterworks, warm hearth settlement identity, peaceful highland markers, carved civic ornament, or restrained blue rune culture.
- Standing-pair rows are static cave-threshold visual framing only. Negative space, gaps, and paired placement are visual reads, not traversal proof, gameplay lanes, route gates, or approved cave entry dimensions.
- Giant-scale readability must preserve broad slab massing, tall/short asymmetry, embedded bases, restrained oxide red warning accents, and Blood Axe separation before any later production lane reduces detail.

## Readiness Matrix

| Child intake row | Package/reference/policy ID | Source status | Package/reference readiness | Art/scale guardrails | Material/LOD/collision guardrails | Blocked implementation decisions | Validator gaps | Approval gates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BloodAxeCaveApproachStandingPair_A01#PrimaryPairContext_A01` | `SM_GIA_BloodAxeCaveApproachStandingPair_A01` | Existing docs-only prop package is the restraint source; no source folder, mesh, DCC, FBX, or Unreal asset is selected. | Reference-only child row; ASSET_INDEX records the prop package as ready for planning reference. | Preserve asymmetric tall/short rough standing stones, broad embedded bases, restrained red accents, and Giant scale lock. | Use cave approach material discipline and LOD/collision policy; collision remains disabled or simple-only only under later separate scope. | No functional doorway behavior, path-width promise, route validation, nav gate, DCC target, Unreal target, startup target, or first implementation target. | No validator file or validator target is selected; no traversal, route, nav, or cave compatibility proof exists. | Final cave approval and final visual approval remain stopped. |
| `BloodAxeCaveApproachStandingPair_A01#LeaningPair_A01` | `KIT_GIA_BloodAxeLeaningCaveStandingPair_A01` | Package docs may be referenced later; this matrix creates no DCC source, sculpt, retopo, UV, proof render, export, or Unreal Content. | Child intake status is planned; ASSET_INDEX records a package-ready leaning variant reference. | Controlled static lean only; keep broad chipped planes, embedded base weight, old mud/ash grounding, and Giant-scale stability read. | Follow shared rough stone, soot, ash, mud, oxide red, LOD0-LOD3, and simple-only collision policy. | No collapse behavior, traversal clearance, route validation, nav/pathfinding, collision correctness claim, source target, DCC target, Unreal target, or first implementation target. | No validator file or leaning-specific validation target is selected. | Later lead/DCC/Unreal approval required before any build or visual signoff. |
| `BloodAxeCaveApproachStandingPair_A01#BrokenPair_A01` | `KIT_GIA_BloodAxeBrokenCaveStandingPair_A01` | Package docs may be referenced later; this matrix creates no broken mesh, physics setup, destructible setup, source folder, FBX, or Unreal asset. | Child intake status is planned; ASSET_INDEX records a package-ready broken variant reference. | Static visual history only: one upright slab plus one snapped, shortened, or fallen companion while preserving Giant-scale readability. | Keep broad broken planes as geometry in later scope; small cracks, chips, soot, ash, and mud detail stay texture/normal work; collision disabled/simple-only by policy. | No destructible behavior, puzzle state, objective marker, encounter trigger, interaction target, physics behavior, DCC target, Unreal target, startup target, or first implementation target. | No validator file or broken-variant validation target is selected. | Final cave approval, final visual approval, and gameplay approval remain stopped. |
| `BloodAxeCaveApproachStandingPair_A01#ClothTiedPair_A01` | `KIT_GIA_BloodAxeClothTiedCaveStandingPair_A01` | Package-ready docs reference exists; this matrix creates no cloth mesh, material instance, material graph, animation asset, source folder, FBX, or Unreal asset. | Package-ready child row focused on broad static oxide red cloth, rawhide lashings, and Giant-tied knots. | Cloth must remain broad, static, restrained, and secondary to standing-stone massing; no UI or quest readability. | Cloth/hide may be a second material only in later scope; no default emissive, material pulse, VFX/audio, cloth simulation, wind sway, or per-strip collision. | No UI marker behavior, quest pointer, objective cue, material pulse, DCC target, Unreal target, startup target, or first implementation target. | No validator file or cloth-tied validation target is selected. | Final color approval and final visual approval remain stopped. |
| `BloodAxeCaveApproachStandingPair_A01#LowChockStonesBase_A01` | `SM_GIA_BloodAxeCaveStandingPairChockStoneBase_A01` | Package-ready docs reference exists; this matrix creates no support mesh, terrain integration proof, collision proxy, source folder, FBX, or Unreal asset. | Package-ready child row for a few large wedge stones, buried base forms, mud pads, cold ash pads, cave grit, and contact-shadow grounding. | Support stones must read as Giant-scale base weight, not pebble clutter or route blockers. | Stone/ash/mud should stay low-material and texture-supported; collision disabled by default, with one broad simple hull only if separately scoped later. | No route blocker behavior, collision correctness claim, terrain integration proof, cave compatibility proof, interaction behavior, DCC target, Unreal target, startup target, or first implementation target. | No validator file, terrain validator, collision validator, or startup validator target is selected. | Final cave approval and final visual approval remain stopped. |
| `BloodAxeCaveApproachStandingPair_A01#SpacingReviewRow_A01` | `DOC_GIA_BloodAxeCaveApproachStandingPairSpacingReview_A01` | Package-ready docs reference exists for non-shipping review rows; this matrix creates no capture, validator, Unreal actor, startup placement, DCC row geometry, or source folder. | Package-ready documentation row for visual gaps, tall/short height rhythm, cloth density, base footprint, and Giant baseline readability. | Review rows must stay non-shipping and visual-only beside female and male Giant baselines. | Collision disabled; no material graph, runtime asset, gameplay lane, or path-width value. | No gameplay lane, path-width promise, nav/pathfinding value, encounter spacing, trigger size, validator target, capture target, Unreal actor target, startup target, or first implementation target. | Review-row approval is not final cave approval or final visual approval. |
| `BloodAxeCaveApproachStandingPair_A01#MaterialDisciplineReference_A01` | `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01` | Reference-only policy source; this matrix creates no texture asset, material instance, material graph, VFX/audio, source folder, FBX, or Unreal Content. | Reference-only child row for shared cave approach material discipline. | Protect rough highland stone, soot, ash, cave grit, trampled mud, oxide red cloth, rope, rawhide, blackened iron, old horn, dull bone, and neutral/civilized Giant separation. | No default emissive; fine cracks, soot speckles, ash flecks, cloth weave, rope fibers, lichen, paint chips, horn rings, and bone pores remain texture/normal planning only. | No material instance creation, texture creation, material graph authoring, VFX/audio, final color approval, final visual approval, DCC target, Unreal target, or first implementation target. | No material validator file or material authoring target is selected. | Final color approval and final visual approval remain stopped. |
| `BloodAxeCaveApproachStandingPair_A01#LODCollisionReference_A01` | `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01` | Reference-only policy source; this matrix creates no LOD source, collision proxy, UCX mesh, validator file, engine setting, source folder, FBX, or Unreal Content. | Reference-only child row for LOD0-LOD3 reduction order and disabled/simple collision policy across standing-pair variants. | Preserve Giant-scale relationship, Blood Axe red/black warning identity, static cave-threshold read, and primary paired-stone silhouettes before reducing small detail. | Collision disabled by default for review rows, cloth, ash, mud, cave grit, small accents, paint, lichen, and texture-only detail; simple primitives only under later separate implementation scope. | No nav blocker, gameplay volume, trigger volume, objective volume, collision correctness claim, runtime implementation, DCC target, Unreal target, validator target, or first implementation target. | No collision validator, LOD validator, startup validator, or route validator target is selected. | Final cave approval and final visual approval remain stopped. |

## Source Status

- Source status is docs-only for every row in this matrix.
- No external source concept is copied, moved, edited, embedded, cropped, renamed, inspected for final approval, or committed by this task.
- No source folder, DCC source, Blender file, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content folder, runtime source, or Hermes file is created.
- Existing package/reference docs are treated as planning sources only; this matrix does not promote any row into production implementation.

## Package And Reference Readiness

- `SM_GIA_BloodAxeCaveApproachStandingPair_A01` is ready as the primary static prop restraint reference only.
- `KIT_GIA_BloodAxeLeaningCaveStandingPair_A01` is ready as an unordered leaning-variant package/reference candidate only.
- `KIT_GIA_BloodAxeBrokenCaveStandingPair_A01` is ready as an unordered broken-variant package/reference candidate only.
- `KIT_GIA_BloodAxeClothTiedCaveStandingPair_A01` is ready as an unordered cloth-tied package/reference candidate only.
- `SM_GIA_BloodAxeCaveStandingPairChockStoneBase_A01` is ready as an unordered chock-stone/base package/reference candidate only.
- `DOC_GIA_BloodAxeCaveApproachStandingPairSpacingReview_A01` is ready as a non-shipping documentation review-row reference only.
- `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01` is ready as material policy only.
- `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01` is ready as LOD/collision policy only.
- Readiness here means a later lead can open a separate scoped DCC, Unreal, QA, or docs task. It does not create implementation permission or sequence.

## Material, LOD, And Collision Guardrails

- Material baseline: rough highland stone, soot, ash, cave grit, trampled mud, oxide red cloth, rope, rawhide, blackened iron, old horn, and dull bone.
- Material exclusions: no neutral/civilized Giant civic masonry as Blood Axe default, no default emissive, no glow/readable signage/UI cue material, no material pulse, no VFX/audio, no material graph work.
- Texture/detail policy: tiny cracks, soot speckles, ash flecks, cave grit, cloth weave, rope fibers, paint chips, lichen specks, horn rings, bone pores, mud streaks, and small scratches stay in future texture, normal, AO, roughness, or mask planning.
- LOD policy: all important future static meshes need LOD0, LOD1, LOD2, and LOD3 before shipping use; small detail is removed before primary Giant-scale silhouettes.
- Collision policy: disabled by default for review rows, cloth, rope, ash, mud, cave grit, small accents, lichen, paint, and texture-only detail. Simple primitives around major stone masses require a later separate implementation task.
- This matrix makes no collision correctness, cave compatibility, traversal clearance, route clearance, camera clearance, player movement, runtime performance, or terrain integration claim.

## Blocked Implementation Decisions

- No first implementation target or implementation order is selected.
- No source folder, DCC target, FBX target, Unreal target, validator target, startup placement, final cave approval target, final visual approval target, or cave gameplay/doorway/nav/route/encounter target is selected.
- No child row is promoted above another child row.
- No row becomes a DCC task, Unreal task, QA validator task, material authoring task, gameplay task, runtime task, startup-scene task, source-concept task, final cave approval task, or final visual approval task through this matrix.

## Validator Gaps

- No validator file is created.
- No validator target is selected.
- No route, nav/pathfinding, traversal, doorway, encounter, interaction, AI, spawn, patrol, objective, quest/UI, material, LOD, collision, startup, final cave, final visual, DCC, FBX, or Unreal validator exists from this task.
- Local readiness checks for this matrix are documentation scans only and do not validate runtime behavior, source assets, imported assets, materials, collisions, placement, or visuals.

## Approval Gates

### `No-doorway guardrail`

Stop before functional doorway behavior, cave gameplay, traversal proof, path widths as gameplay values, nav/pathfinding, route validation, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, UI arrows, spawn logic, patrol logic, AI spaces, damage/aura behavior, cover rules, trap behavior, destructible behavior, pickup/loot/resource/crafting/economy behavior, or final cave approval.

### `No-build guardrail`

Stop before DCC source, source-folder creation, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content, material instance, texture asset, validator file, startup placement, runtime source, Blueprint, socket authoring, physics setup, animation asset, material graph, VFX/audio, final visual approval, first implementation target selection, or Hermes work.

### `No-target-selected guardrail`

This matrix does not select a first implementation target, implementation order, source folder, DCC target, Unreal target, validator target, startup placement, final cave approval target, final visual approval target, or any cave gameplay/doorway/nav/route/encounter target.

## Quality Gate Checklist

- All eight child intake rows are represented.
- All eight package/reference/policy IDs are represented.
- Source-of-truth references are listed for the parent package, child intake, parent cave approach marker kit, primary standing-pair prop, material discipline policy, LOD/collision policy, and `SK_GIA_Base_A01`.
- Giant scale lock appears exactly in the global guardrails.
- Blood Axe hostile sub-faction separation from neutral/civilized Giant culture is explicit.
- Readiness sections cover source status, package/reference readiness, art/scale guardrails, material/LOD/collision guardrails, blocked implementation decisions, validator gaps, and approval gates.
- No implementation order, first target, source folder, DCC target, Unreal target, validator target, startup target, final cave approval target, final visual approval target, or gameplay/doorway/nav/route/encounter target is selected.
- The matrix remains docs-only and changes no blocked file or area.
