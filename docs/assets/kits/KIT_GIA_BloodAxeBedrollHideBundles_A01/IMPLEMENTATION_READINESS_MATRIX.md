# KIT_GIA_BloodAxeBedrollHideBundles_A01 Implementation Readiness Matrix

## Scope

- Task: `AET-MA-20260629-401`
- Scope type: docs-only implementation readiness matrix.
- Owned file: `docs/assets/kits/KIT_GIA_BloodAxeBedrollHideBundles_A01/IMPLEMENTATION_READINESS_MATRIX.md`
- Source package: `docs/assets/kits/KIT_GIA_BloodAxeBedrollHideBundles_A01/PRODUCTION_PACKAGE.md`
- Source intake: `docs/assets/kits/KIT_GIA_BloodAxeBedrollHideBundles_A01/CHILD_ASSET_INTAKE.md`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Clutter_BedrollHideBundles`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only

This matrix classifies the Blood Axe bedroll and hide-bundle package set by documentation readiness, remaining blockers, approval gates, and future validation needs. It does not select a first DCC target, approve implementation order, create source folders, start DCC work, export FBX files, import Unreal assets, create validators, place startup actors, approve final visuals, define sleeping/resting gameplay, define inventory or loot behavior, or authorize Hermes work.

## Scale And Culture Lock

- Giant scale lock: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Future source work, if separately assigned, must author in centimeters with 1 Unreal unit = 1 cm.
- Blood Axe is a hostile Giant sub-faction only. Blood Axe bedroll, hide, and bundle dressing must remain separate from neutral/civilized Giant culture.
- Blood Axe bedroll language may use rough hide, patched leather, old fur edges, thick rope, rawhide lashings, scorched timber stakes, blackened iron rings, soot, ash, mud, and restrained oxide red cloth.
- Neutral/civilized Giant culture remains separate: refined cave-town masonry, blue-gray stoneworker craft, terraces, warm hearth bedding, peaceful highland camp gear, civic symbols, clean nomad craft, and restrained blue rune language are not Blood Axe defaults.

## Readiness Key

- `Package-ready`: production package exists and can be referenced by a later separately approved lane; implementation remains blocked.
- `Policy-ready`: docs-only material, LOD, collision, review, or scale package exists for consistency; it is not a buildable mesh target.
- `Review-only`: package supports non-shipping comparison rows; it does not create an Unreal actor, validator, capture, startup placement, or final visual approval.
- `Implementation blocked`: no source, DCC, FBX, Unreal Content, runtime, validator, startup, final visual approval, first DCC target, or implementation target exists.

## Package-Ready Child Rows

| Asset/package | Current state | Package path | Readiness blockers | Approval gates | DCC preconditions | Unreal preconditions | Residual risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SM_GIA_BloodAxeHideRoll_A01` | Package-ready single hide roll; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeHideRoll_A01/PRODUCTION_PACKAGE.md` | No source mesh, collision proxy, Unreal asset, or target selection | Static visual dressing only; no pickup, loot, resource, inventory, interaction, or rest behavior | Future DCC must preserve flattened Giant-scale roll, two broad straps, one red tag, and no human-scale bedding | Future Unreal work must avoid item pickup, container UI, gameplay traces, and startup placement | Could read as a lootable roll if red tag or straps become item-like |
| `KIT_GIA_BloodAxeHideRollStack_A01` | Package-ready hide-roll stack; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeHideRollStack_A01/PRODUCTION_PACKAGE.md` | No composed source, physics pile, collision setup, or first target selection | Visual pile approval only; no storage, loot, resource, or physics behavior | Future DCC must keep two to five broad rolls varied but not noisy | Future Unreal work must avoid physics simulation, inventory container behavior, and destructible pile logic | Could be mistaken for storage or resource stacks if arranged too neatly |
| `SM_GIA_BloodAxeOpenHideRoll_A01` | Package-ready open hide roll; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeOpenHideRoll_A01/PRODUCTION_PACKAGE.md` | No cloth source, cloth collision, rest marker, DCC, Unreal, or target selection | Static shaped prop only; no usable bed, sleep marker, or rest behavior | Future DCC must model fixed broad flaps, not simulated cloth | Future Unreal work must avoid bed interaction, cloth setup, and rest prompts | Open shape could imply usable bedding without guardrails |
| `SM_GIA_BloodAxeRoughBeddingPallet_A01` | Package-ready rough bedding pallet; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeRoughBeddingPallet_A01/PRODUCTION_PACKAGE.md` | No source mesh, collision proxy, usable bed logic, DCC, Unreal, or target selection | Non-interactive prop approval only; no checkpoint or rest buff | Future DCC must preserve 500-650 cm Giant sleeping footprint without interaction affordances | Future Unreal work must avoid bed usable state, checkpoint logic, and AI rest markers | Could become a gameplay bed if future naming or placement overclaims |
| `SM_GIA_BloodAxeGroundBedding_A01` | Package-ready ground bedding; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeGroundBedding_A01/PRODUCTION_PACKAGE.md` | No cloth collision, physics, nav rule, DCC, Unreal, or target selection | Static visual dressing only; no rest, interaction, or nav behavior | Future DCC must keep low spread shape readable and avoid cloth sim | Future Unreal work must avoid walkable/nav claims and rest prompts | Low profile could be confused with nav-safe placement if collision is overclaimed |
| `SM_GIA_BloodAxeFurSleepLayer_A01` | Package-ready fur sleep layer; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeFurSleepLayer_A01/PRODUCTION_PACKAGE.md` | No harvesting, resource, inventory, cloth physics, DCC, Unreal, or target selection | Non-graphic static dressing only | Future DCC must keep old practical fur/hide read, not trophy or gore escalation | Future Unreal work must avoid harvest, pickup, resource, and cloth behavior | Fur layer could drift into trophy, gore, or resource language |
| `SM_GIA_BloodAxeTiedCampBundle_A01` | Package-ready tied camp bundle; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeTiedCampBundle_A01/PRODUCTION_PACKAGE.md` | No inventory bag, loot table, pickup, DCC, Unreal, or target selection | Visual camp packing approval only | Future DCC must keep lumpy Giant-scale bundle, broad straps, and one large knot | Future Unreal work must avoid bag inventory, container UI, loot, salvage, and interaction | Bundle could read as a lootable container |
| `KIT_GIA_BloodAxeTiedBundleSet_A01` | Package-ready bundle set; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeTiedBundleSet_A01/PRODUCTION_PACKAGE.md` | No randomized loot, economy data, source split, DCC, Unreal, or target selection | Static set dressing only | Future DCC must preserve squat, long, strapped, and overstuffed variants as broad reusable shapes | Future Unreal work must avoid randomized contents, resource values, and destructible behavior | Set could become an implicit storage/economy kit |
| `SM_GIA_BloodAxeFrameStrappedBundle_A01` | Package-ready frame-strapped bundle; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeFrameStrappedBundle_A01/PRODUCTION_PACKAGE.md` | No movable prop, carry socket, physics body, DCC, Unreal, or target selection | Dressing only; no transport behavior | Future DCC must keep crude timber frame static, broad, and heavy | Future Unreal work must avoid carry sockets, movable state, physics, and vehicle/transport behavior | Frame silhouette could imply a movable carry system |
| `KIT_GIA_BloodAxeRawhideLashingSet_A01` | Package-ready lashing set; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeRawhideLashingSet_A01/PRODUCTION_PACKAGE.md` | No rope physics, sockets, cloth setup, DCC, Unreal, or target selection | Static reusable lashing shapes only | Future DCC must keep loops, strap bands, and knots thick and fixed | Future Unreal work must avoid rope simulation, dangling motion, sockets, and crafting resources | Could become micro-detail or physics-heavy if over-modeled |
| `SM_GIA_BloodAxeRopeCoilTie_A01` | Package-ready rope coil; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeRopeCoilTie_A01/PRODUCTION_PACKAGE.md` | No usable rope, pickup, crafting resource, physics coil, DCC, Unreal, or target selection | Static prop only | Future DCC must preserve thick visible turns without per-fiber geometry | Future Unreal work must avoid interaction prompts, pickup, crafting, and physics behavior | Rope coil could be mistaken for a usable item |
| `SM_GIA_BloodAxeBundleStakeAnchor_A01` | Package-ready stake anchor; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeBundleStakeAnchor_A01/PRODUCTION_PACKAGE.md` | No tent rigging behavior, physics constraint, collision proxy, nav blocker, DCC, Unreal, or target selection | Visual anchoring only | Future DCC must keep short stake, tie ring, and rawhide strap blunt and secondary | Future Unreal work must avoid constraint setup, nav blockers, tent behavior, and interaction | Stake anchor could read as a gameplay blocker or rigging system |
| `KIT_GIA_BloodAxeShelterPile_A01` | Package-ready shelter-side pile; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeShelterPile_A01/PRODUCTION_PACKAGE.md` | No storage, rest, collision proxy, DCC, Unreal, startup, or target selection | Review composition only; no final visual approval | Future DCC must compose hide rolls, bedding, one bundle, stakes, and rope coil without owning shelter structures | Future Unreal work must avoid storage logic, usable bed behavior, startup placement, and nav claims | Could be mistaken for a selected first composition target |
| `KIT_GIA_BloodAxeLeanToEdgePile_A01` | Package-ready lean-to edge pile; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeLeanToEdgePile_A01/PRODUCTION_PACKAGE.md` | No nav/pathfinding rule, collision proxy, usable bed, DCC, Unreal, or target selection | Static camp dressing only | Future DCC must keep narrow pile low and shelter-adjacent without redefining lean-to structure | Future Unreal work must avoid path clearance claims, collision correctness, and rest behavior | Could overclaim route clearance if used as path-edge logic |
| `KIT_GIA_BloodAxeSleepingRow_A01` | Package-ready sleeping row; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeSleepingRow_A01/PRODUCTION_PACKAGE.md` | No sleeping system, spawn point, AI rest behavior, DCC, Unreal, or target selection | Non-shipping review composition only | Future DCC must keep two to four bedding forms as visual scale rhythm, not gameplay beds | Future Unreal work must avoid spawn markers, AI rest states, and interaction markers | Could become an encounter/spawn layout without a gameplay task |
| `SM_GIA_BloodAxeThresholdBundle_A01` | Package-ready threshold bundle; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeThresholdBundle_A01/PRODUCTION_PACKAGE.md` | No objective marker, cover definition, lootable bag, blocker rule, DCC, Unreal, or target selection | Visual dressing only | Future DCC must keep the single bundle low, readable, and non-interactive | Future Unreal work must avoid objective, cover, pickup, blocker, and startup claims | Threshold placement could imply cover or objective affordance |

## Policy And Review Rows

| Document/package | Current state | Package path | Use | Non-authorization |
| --- | --- | --- | --- | --- |
| `DOC_GIA_BloodAxeBedrollReviewRows_A01` | Review-only package-ready rows | `docs/assets/kits/DOC_GIA_BloodAxeBedrollReviewRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping review rows for hide-roll stacks, bedding rhythm, tied-bundle variation, shelter-edge pile spacing, and camera readability | No Unreal actor, validator, capture automation, startup placement, final visual signoff, DCC, Unreal Content, or implementation target |
| `DOC_GIA_BloodAxeBedrollScaleRows_A01` | Review-only package-ready rows | `docs/assets/kits/DOC_GIA_BloodAxeBedrollScaleRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping scale rows beside female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in Giant baselines | No scale-lock change, shipped marker approval, DCC, FBX, Unreal, validators, captures, startup placement, or implementation target |
| `DOC_GIA_BloodAxeBedrollLODAndCollision_A01` | Policy-ready LOD/collision package | `docs/assets/kits/DOC_GIA_BloodAxeBedrollLODAndCollision_A01/PRODUCTION_PACKAGE.md` | LOD0-LOD3 and collision-limit policy for rolls, bedding, bundles, lashings, stakes, piles, and review markers | No collision proxies, cloth collision, physics bodies, nav blockers, gameplay volumes, validator files, Unreal Content, DCC, final approval, or implementation target |
| `DOC_GIA_BloodAxeBedrollMaterialDiscipline_A01` | Policy-ready material package | `docs/assets/kits/DOC_GIA_BloodAxeBedrollMaterialDiscipline_A01/PRODUCTION_PACKAGE.md` | Shared material discipline for rough hide, patched leather, fur edges, rope, rawhide, scorched timber, blackened iron, soot, ash, mud, and oxide red cloth | No material instance, texture asset, material graph, emissive, VFX/audio, DCC, Unreal Content, startup placement, final color approval, or implementation target |

## Source And Export Path Plan

The paths below are future planning references only. This matrix does not create folders, source files, exports, imports, validators, startup actors, or implementation targets.

| Family | Planned source root if later approved | Planned export root if later approved | Planned Unreal target root if later approved |
| --- | --- | --- | --- |
| Bedroll and hide-bundle static props | `SourceAssets/Blender/Kits/Giants/BloodAxeCamp/BedrollHideBundles/` | `SourceAssets/Exports/Kits/Giants/BloodAxeCamp/BedrollHideBundles/` | `/Game/Aerathea/Props/Giants/BloodAxeCamp/BedrollHideBundles/` |
| Bedroll review and scale rows | Not selected | Not selected | Not applicable unless a later non-shipping review-scene task owns it |
| Shared material policy | Not applicable from this matrix | Not applicable from this matrix | `/Game/Aerathea/Materials/Giants/BloodAxe/` only if a later material task owns it |

No first source folder, export folder, Unreal folder, material folder, review actor, validator, DCC target, package implementation target, or build order is selected here.

## DCC Readiness Preconditions

A later DCC lane must explicitly approve and own all of the following before source work begins:

- Exact source and export file scope.
- Chosen DCC target or targets; this matrix does not choose them.
- Per-child module split, mesh naming, pivot, orientation, centimeter scale proof, and scale comparison against the female 442 cm and male 470 cm Giant baselines.
- LOD0-LOD3 source expectations and reduction order from `DOC_GIA_BloodAxeBedrollLODAndCollision_A01`.
- Material-slot policy from `DOC_GIA_BloodAxeBedrollMaterialDiscipline_A01`.
- Static-shape policy for hide rolls, bedding, fur layers, tied bundles, rope coils, lashings, stakes, and shelter-edge piles.
- Culture-separation review against neutral/civilized Giant cave-town, warm hearth, and highland bedding language.
- Review artifact plan that remains non-final until separate visual approval exists.

## Unreal Readiness Preconditions

A later Unreal lane must explicitly approve and own all of the following before engine work begins:

- Import path, asset ownership, and exact file scope.
- Whether each row becomes a shipping static mesh, remains a docs-only package, or becomes a non-shipping review artifact.
- Import scale proof at 1 Unreal unit = 1 cm.
- LOD0-LOD3 presence for shipping static mesh candidates.
- Material instance and texture ownership, with no default emissive unless a separate approved magical, forge, or shamanic variant exists.
- Collision disabled by default or a separately approved simple low blocking/query exception.
- Focused validation plan owned by the future Unreal/QA task.
- Any startup placement, review capture, marker pass, camera approval, final visual approval, or final package implementation approval in separately assigned tasks.

This matrix does not create Unreal Content, material instances, textures, Blueprints, sockets, collision proxies, validators, review actors, startup actors, or runtime source.

## Validator Gaps And Future Checks

No validator is authored by this matrix. Future implementation lanes should add focused validators only when they own the affected tool paths.

| Future lane | Validator need |
| --- | --- |
| DCC source/export | Confirm source path, export path, FBX name, centimeter scale, dimensions, pivot, LOD0-LOD3 sources, material slot count, and no micro-detail geometry misuse. |
| Giant scale | Compare dimensions against female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in baselines. |
| Bedroll import | Confirm Unreal path, LODs, material slots, simple/disabled collision policy, texture references, and no rest, pickup, inventory, or loot logic. |
| Material validation | Confirm shared Blood Axe material families, no default emissive, red accent restraint, roughness/metallic ranges, and no neutral/civilized Giant material drift. |
| Collision validation | Confirm collision disabled by default or simple low blocking/query only; no UCX, nav blockers, gameplay volumes, pickup volumes, rest volumes, trigger volumes, or collision correctness claims without a later lane. |
| Culture separation | Confirm Blood Axe docs do not claim default Giant culture, neutral cave-town identity, warm hearth bedding, blue-gray stoneworker motifs, or civilized Giant materials. |
| Source-storage | Confirm external concept art was not copied, embedded, moved, edited, inspected for visual approval, or committed. |
| Matrix maintenance | Confirm package-ready rows, policy rows, review rows, approval gates, and no-target-selected status remain aligned after docs/index integration. |

## Global Stop Gates

- Stop before selecting a first DCC, Unreal, source asset, gameplay, review-scene, validator, material, VFX/audio, startup, or implementation target from any row.
- Stop before source folder creation, DCC source, Blender files, meshes, sculpts, retopo, UVs, bakes, proof renders, LOD source files, collision proxies, UCX meshes, FBX exports, Unreal Content assets, material instances, texture assets, material graphs, import scripts, validators, runtime source, Blueprints, sockets, animation assets, review actors, startup placement, or source concept movement.
- Stop before pickup, loot, inventory, storage UI, resource, salvage, harvesting, crafting/economy, vendor, usable bed, rest, sleeping, interaction prompts, objective logic, nav/pathfinding, cover tagging, destructible behavior, faction buffs, morale behavior, AI behavior, patrol/spawn logic, encounter scripting, VFX/audio, material-state behavior, or Hermes work.
- Stop before claiming collision correctness, runtime performance validation, camera approval, final silhouette approval, final bedroll approval, final Blood Axe camp approval, or final visual approval.
- Stop if Blood Axe hostile raider identity starts replacing neutral/civilized Giant culture.
- Stop if any future row appears to require changing the Giant scale lock from female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline, or the approved Giant ranges.

## Matrix Maintenance Validation

Use these docs-only checks after edits to this matrix:

- Matrix completeness scan: confirm parent package, package-ready child rows, material policy, LOD/collision policy, review rows, and scale rows from `CHILD_ASSET_INTAKE.md` are represented.
- Package-path existence scan: confirm every path listed as package-ready exists.
- Approval-gate scan: confirm DCC, FBX, Unreal, runtime, validator creation, startup placement, final visual approval, first target selection, and implementation order approval remain blocked.
- Giant scale scan: confirm female 442 cm / 14 ft 6 in, male 470 cm / 15 ft 5 in, females 14-15 ft / 427-457 cm, and males 14 ft 10 in-16 ft 0 in / 452-488 cm remain present.
- Culture separation scan: confirm Blood Axe is described as a hostile Giant sub-faction and neutral/civilized Giant culture remains explicitly separate.
- Implementation-claim scan: confirm the matrix contains no claim that source, DCC, FBX, Unreal Content, runtime, validator, startup, visual approval, sleeping/resting gameplay, inventory/loot behavior, or implementation work has started.
- Whitespace and diff validation: run `git diff --check -- docs/assets/kits/KIT_GIA_BloodAxeBedrollHideBundles_A01/IMPLEMENTATION_READINESS_MATRIX.md`.

## Quality Gate Checklist

- Matrix is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, material graph, VFX/audio asset, global index, backlog, bootstrap, child intake doc, source folder, image, unrelated package file, or production package.
- Bedroll and hide-bundle package rows are classified by readiness using the child intake and current package files.
- Material policy, LOD/collision policy, review-only rows, and scale rows are represented separately from buildable static-mesh candidates.
- Giant scale lock is explicit: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline; approved Giant ranges females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Package inventory does not imply build order, implementation order, DCC target selection, Unreal target selection, or final visual approval.
- Pickup, loot, inventory, storage UI, resource, salvage, crafting/economy, vendor behavior, sleeping/resting gameplay, usable bed behavior, interaction prompts, objective logic, nav/pathfinding, cover behavior, destructible behavior, AI/encounter behavior, VFX/audio, material-state behavior, cloth/physics, source asset creation, startup placement, and final approval are explicitly excluded.
- Source concept remains external and is not copied, moved, edited, embedded, inspected for visual approval, or committed.

## Non-Authorization Statement

This readiness matrix is a documentation artifact only. It authorizes no source folder, DCC target, implementation order, Blender work, mesh work, FBX export, Unreal Content import, material authoring, runtime source, validator creation, startup placement, final visual approval, final Blood Axe bedroll approval, Hermes work, sleeping/resting gameplay, pickup/loot/inventory behavior, or final Giant culture approval.
