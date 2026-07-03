# KIT_GIA_BloodAxeCratesSacksBaskets_A01 Implementation Readiness Matrix

## Scope

- Task: `AET-MA-20260629-427`
- Scope type: docs-only implementation readiness matrix.
- Owned file: `docs/assets/kits/KIT_GIA_BloodAxeCratesSacksBaskets_A01/IMPLEMENTATION_READINESS_MATRIX.md`
- Source package: `docs/assets/kits/KIT_GIA_BloodAxeCratesSacksBaskets_A01/PRODUCTION_PACKAGE.md`
- Source intake: `docs/assets/kits/KIT_GIA_BloodAxeCratesSacksBaskets_A01/CHILD_ASSET_INTAKE.md`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Clutter_CratesSacksBaskets`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only

This matrix classifies the Blood Axe crates, sacks, baskets, rope bindings, covered bundles, storage clusters, review rows, scale rows, material policy, and LOD/collision policy by documentation readiness, remaining blockers, approval gates, and future validation needs. It does not select a first DCC target, approve implementation order, create source folders, start DCC work, export FBX files, import Unreal assets, create validators, place startup actors, approve final visuals, define storage gameplay, define inventory or loot behavior, or authorize Hermes work.

## Scale And Culture Lock

- Giant scale lock: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Future source work, if separately assigned, must author in centimeters with 1 Unreal unit = 1 cm.
- Blood Axe is a hostile Giant sub-faction only. Blood Axe storage clutter must remain separate from neutral/civilized Giant culture.
- Blood Axe storage language may use rough timber, scorched boards, blackened iron, dirty sackcloth, patched hide, thick basket weave, rope, rawhide, soot, ash, mud, and restrained oxide red cloth or paint.
- Neutral/civilized Giant culture remains separate: refined cave-town masonry, blue-gray stoneworker craft, terraces, warm hearth market storage, peaceful highland supplies, civic symbols, and restrained blue rune language are not Blood Axe defaults.

## Readiness Key

- `Package-ready`: production package exists and can be referenced by a later separately approved lane; implementation remains blocked.
- `Policy-ready`: docs-only material, LOD, collision, review, or scale package exists for consistency; it is not a buildable mesh target.
- `Review-only`: package supports non-shipping comparison rows; it does not create an Unreal actor, validator, capture, startup placement, or final visual approval.
- `Implementation blocked`: no source, DCC, FBX, Unreal Content, runtime, validator, startup, final visual approval, first DCC target, or implementation target exists.

## Package-Ready Child Rows

| Asset/package | Current state | Package path | Readiness blockers | Approval gates | DCC preconditions | Unreal preconditions | Residual risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SM_GIA_BloodAxeOversizedCrate_A01` | Package-ready oversized crate; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeOversizedCrate_A01/PRODUCTION_PACKAGE.md` | No source mesh, collision proxy, Unreal asset, or target selection | Static dressing only; no loot, reward, pickup, vendor, inventory, resource, destructible, or interaction behavior | Future DCC must preserve Giant-scale plank mass, blunt straps, and no treasure-chest read | Future Unreal work must avoid container UI, openable states, reward glints, and startup placement | Could read as a loot chest if hardware or red marks become too item-like |
| `SM_GIA_BloodAxeOpenSupplyCrate_A01` | Package-ready open supply crate; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeOpenSupplyCrate_A01/PRODUCTION_PACKAGE.md` | No contents source, DCC, Unreal, or target selection | No treasure, pickup, inventory, resource, or vendor behavior | Future DCC must keep contents non-specific and covered where needed | Future Unreal work must avoid item components and interaction prompts | Open form could imply loot without strong guardrails |
| `KIT_GIA_BloodAxeFlatCrateStack_A01` | Package-ready flat crate stack; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeFlatCrateStack_A01/PRODUCTION_PACKAGE.md` | No composed source, collision proxy, DCC, Unreal, or target selection | Static composition only; no cover, blocker, destructible, or first target claim | Future DCC must keep low stack readable and not wall-like | Future Unreal work must avoid cover tags, collision correctness claims, and startup placement | Could be mistaken for a cover prop or route blocker |
| `SM_GIA_BloodAxeHeavySack_A01` | Package-ready single heavy sack; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeHeavySack_A01/PRODUCTION_PACKAGE.md` | No source, cloth setup, DCC, Unreal, or target selection | Visual storage only; no pickup, loot, inventory, resource, or crafting behavior | Future DCC must preserve broad tied neck and dirt-weighted base | Future Unreal work must avoid pickup, physics, and inventory affordances | Sack could become item-like if scaled too small or tagged |
| `KIT_GIA_BloodAxeSackGroup_A01` | Package-ready sack group; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeSackGroup_A01/PRODUCTION_PACKAGE.md` | No composed source, collision proxy, DCC, Unreal, or target selection | Static dressing only; no grain-resource, vendor stockpile, storage UI, or destructible behavior | Future DCC must keep three to seven broad masses without micro-clutter | Future Unreal work must avoid resource, vendor, inventory, and destructible claims | Could imply economy/resource gameplay if arranged like stock |
| `SM_GIA_BloodAxeHideReinforcedSack_A01` | Package-ready hide-reinforced sack; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeHideReinforcedSack_A01/PRODUCTION_PACKAGE.md` | No DCC, Unreal, material-state setup, or target selection | Static set dressing only; no pickup, inventory, resource, or material-state gameplay | Future DCC must keep rawhide reinforcement as silhouette-supporting detail | Future Unreal work must avoid material states and interaction prompts | Reinforcement could drift into armor/loot readability |
| `SM_GIA_BloodAxeWovenBasket_A01` | Package-ready woven basket; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeWovenBasket_A01/PRODUCTION_PACKAGE.md` | No DCC, Unreal, startup, final approval, or implementation target | Static dressing only; no human-scale basket language, vendor display, or resource container behavior | Future DCC must keep broad thick weave, large rim, and Giant scale | Future Unreal work must avoid pickup, vendor, and inventory behavior | Could become cozy market/civilized Giant read if too clean |
| `KIT_GIA_BloodAxeBasketSet_A01` | Package-ready basket set; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeBasketSet_A01/PRODUCTION_PACKAGE.md` | No source split, DCC, Unreal, or target selection | Visual dressing only; no individual item pickups, inventory containers, or loot behavior | Future DCC must preserve varied basket silhouettes without dense weave geometry | Future Unreal work must avoid per-basket interaction and vendor layout | Could read as market display if too organized |
| `KIT_GIA_BloodAxeRopeBindingCoils_A01` | Package-ready rope binding set; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeRopeBindingCoils_A01/PRODUCTION_PACKAGE.md` | No rope physics, sockets, DCC, Unreal, or target selection | Static rope dressing only; no physics, crafting ingredient, or pickup behavior | Future DCC must keep coils and knots thick, fixed, and non-simulated | Future Unreal work must avoid rope physics, pickup, and crafting/resource components | Could become physics-heavy if over-modeled |
| `KIT_GIA_BloodAxeCrateLashingSet_A01` | Package-ready crate lashing set; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeCrateLashingSet_A01/PRODUCTION_PACKAGE.md` | No sockets, Blueprint behavior, physics, DCC, Unreal, or target selection | Planning/static dressing only | Future DCC must keep broad crossed bands and large knots as fixed forms | Future Unreal work must avoid socket authoring and destructible/constraint behavior | Could become attachment-system work without a later lane |
| `SM_GIA_BloodAxeCoveredBundle_A01` | Package-ready covered bundle; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeCoveredBundle_A01/PRODUCTION_PACKAGE.md` | No DCC, Unreal, startup, final approval, or implementation target | Static dressing only; no revealed loot, weapon rewards, quest items, resources, or vendor stock | Future DCC must keep broad hidden mass and non-specific contents | Future Unreal work must avoid reveal states, pickup prompts, and container behavior | Covered form could imply hidden reward |
| `KIT_GIA_BloodAxeHideRollBundle_A01` | Package-ready hide roll bundle; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeHideRollBundle_A01/PRODUCTION_PACKAGE.md` | No DCC, Unreal, cloth simulation, startup, or target selection | Static dressing only; no bedroll interaction, resting, inventory, pickup, or cloth sim | Future DCC must keep roll-like covered mass and thick rope bands | Future Unreal work must avoid rest, inventory, pickup, and cloth setup | Could overlap bedroll gameplay if placed like bedding |
| `SM_GIA_BloodAxeStakedCoveredBundle_A01` | Package-ready staked covered bundle; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeStakedCoveredBundle_A01/PRODUCTION_PACKAGE.md` | No trap, objective, destructible, nav behavior, DCC, Unreal, or target selection | Visual anchoring only | Future DCC must keep stakes short and secondary | Future Unreal work must avoid tripwire, trap, objective, and nav behavior | Could imply trap or blocker if stakes dominate |
| `KIT_GIA_BloodAxeStorageStackCluster_A01` | Package-ready storage stack cluster; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeStorageStackCluster_A01/PRODUCTION_PACKAGE.md` | No startup placement, collision proxy, DCC, Unreal, or first target selection | Static level-art dressing only; no loot, inventory, vendor, or cover behavior | Future DCC must preserve stepped storage pile and non-barricade read | Future Unreal work must avoid startup placement and collision correctness claims unless assigned | Could be mistaken for cover or a selected first target |
| `KIT_GIA_BloodAxeShelterEdgeStorageCluster_A01` | Package-ready shelter-edge cluster; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeShelterEdgeStorageCluster_A01/PRODUCTION_PACKAGE.md` | No shelter interaction, DCC, Unreal, collision, or target selection | Static shelter-edge dressing only; no cover, nav/pathfinding, destructible, or gameplay collision behavior | Future DCC must keep low under-sightline mass and avoid redefining shelter structure | Future Unreal work must avoid shelter linkage, cover tags, nav claims, and gameplay collision | Could overclaim cover or shelter interaction if placed poorly |
| `KIT_GIA_BloodAxeGateInteriorStorageCluster_A01` | Package-ready gate-interior cluster; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeGateInteriorStorageCluster_A01/PRODUCTION_PACKAGE.md` | No gate behavior, DCC, Unreal, collision, or target selection | Static gate-adjacent dressing only; no barricade, loot cache, vendor stall, quest, cover, or gate interaction | Future DCC must keep storage read and leave negative space so it is not a wall | Future Unreal work must avoid gate linkage, cover tags, nav claims, and interaction volumes | Could drift into barricade or gate component language |

## Policy And Review Rows

| Document/package | Current state | Package path | Use | Non-authorization |
| --- | --- | --- | --- | --- |
| `DOC_GIA_BloodAxeStorageCompositionRows_A01` | Review-only package-ready rows | `docs/assets/kits/DOC_GIA_BloodAxeStorageCompositionRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping comparison rows for crate, sack, basket, rope, covered-bundle, shelter-edge, gate-interior, and stacked-cluster rhythm | No Unreal actor, validator, capture automation, startup placement, final visual signoff, DCC, Unreal Content, or implementation target |
| `DOC_GIA_BloodAxeStorageScaleRows_A01` | Review-only package-ready rows | `docs/assets/kits/DOC_GIA_BloodAxeStorageScaleRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping scale rows beside female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in Giant baselines | No scale-lock change, shipped asset approval, DCC, FBX, Unreal, validators, captures, startup placement, or implementation target |
| `DOC_GIA_BloodAxeStorageLODAndCollision_A01` | Policy-ready LOD/collision package | `docs/assets/kits/DOC_GIA_BloodAxeStorageLODAndCollision_A01/PRODUCTION_PACKAGE.md` | LOD0-LOD3 and collision-limit policy for crates, sacks, baskets, rope bindings, covered bundles, and clusters | No collision proxies, UCX meshes, nav blockers, gameplay volumes, validator files, Unreal Content, DCC, final approval, or implementation target |
| `DOC_GIA_BloodAxeStorageMaterialDiscipline_A01` | Policy-ready material package | `docs/assets/kits/DOC_GIA_BloodAxeStorageMaterialDiscipline_A01/PRODUCTION_PACKAGE.md` | Shared material discipline for rough timber, blackened iron, rope, rawhide, sackcloth, basket weave, hide covers, soot, ash, mud, and restrained oxide red | No material instance, texture asset, material graph, VFX/audio, DCC, Unreal Content, startup placement, final color approval, or implementation target |

## Source And Export Path Plan

The paths below are future planning references only. This matrix does not create folders, source files, exports, imports, validators, startup actors, or implementation targets.

| Family | Planned source root if later approved | Planned export root if later approved | Planned Unreal target root if later approved |
| --- | --- | --- | --- |
| Blood Axe storage static props and clusters | `SourceAssets/Blender/Kits/Giants/BloodAxeCamp/CratesSacksBaskets/` | `SourceAssets/Exports/Kits/Giants/BloodAxeCamp/CratesSacksBaskets/` | `/Game/Aerathea/Props/Giants/BloodAxeCamp/Storage/` |
| Storage review and scale rows | Not selected | Not selected | Not applicable unless a later non-shipping review-scene task owns it |
| Shared storage material policy | Not applicable from this matrix | Not applicable from this matrix | `/Game/Aerathea/Materials/Giants/BloodAxe/Storage/` only if a later material task owns it |

No first source folder, export folder, Unreal folder, material folder, review actor, validator, DCC target, package implementation target, or build order is selected here.

## DCC Readiness Preconditions

A later DCC lane must explicitly approve and own all of the following before source work begins:

- Exact source and export file scope.
- Chosen DCC target or targets; this matrix does not choose them.
- Per-child module split, mesh naming, pivot, orientation, centimeter scale proof, and scale comparison against the female 442 cm and male 470 cm Giant baselines.
- LOD0-LOD3 source expectations and reduction order from `DOC_GIA_BloodAxeStorageLODAndCollision_A01`.
- Material-slot policy from `DOC_GIA_BloodAxeStorageMaterialDiscipline_A01`.
- Static-shape policy for crates, sacks, baskets, rope bindings, covered bundles, shelter-edge clusters, gate-interior clusters, and stacked storage clusters.
- Culture-separation review against neutral/civilized Giant cave-town, warm hearth, and highland settlement storage language.
- Review artifact plan that remains non-final until separate visual approval exists.

The DCC lead must reject any direction that turns this kit into active storage systems, loot containers, pickup objects, inventory containers, vendor stock, resource goods, crafting ingredients, gate components, cover objects, destructible clutter, physics piles, rope/cloth simulation, nav/pathfinding markers, neutral Giant domestic storage, civilized Giant market dressing, or source-concept storage work.

## Unreal Readiness Preconditions

A later Unreal lane must explicitly approve and own all of the following before engine work begins:

- Import path, asset ownership, and exact file scope.
- Whether each row becomes a shipping static mesh, remains a docs-only package, or becomes a non-shipping review artifact.
- Import scale proof at 1 Unreal unit = 1 cm.
- LOD0-LOD3 presence for shipping static mesh candidates.
- Material instance and texture ownership, with no default emissive unless a separate approved magical, forge, or signal variant exists.
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
| Storage import | Confirm Unreal path, LODs, material slots, simple/disabled collision policy, texture references, and no loot, pickup, inventory, vendor, resource, gate, cover, nav, or destructible logic. |
| Material validation | Confirm shared Blood Axe material families, no default emissive, red accent restraint, roughness/metallic ranges, and no neutral/civilized Giant material drift. |
| Collision validation | Confirm collision disabled by default or simple low blocking/query only; no UCX, nav blockers, gameplay volumes, cover volumes, pickup volumes, interaction volumes, or collision correctness claims without a later lane. |
| Culture separation | Confirm Blood Axe docs do not claim default Giant culture, neutral cave-town identity, warm hearth storage, blue-gray stoneworker motifs, or civilized Giant materials. |
| Source-storage | Confirm external concept art was not copied, embedded, moved, edited, inspected for visual approval, or committed. |
| Matrix maintenance | Confirm package-ready rows, policy rows, review rows, approval gates, and no-target-selected status remain aligned after docs/index integration. |

## Global Stop Gates

- Stop before selecting a first DCC, Unreal, source asset, gameplay, review-scene, validator, material, VFX/audio, startup, or implementation target from any row.
- Stop before source folder creation, DCC source, Blender files, meshes, sculpts, retopo, UVs, bakes, proof renders, LOD source files, collision proxies, UCX meshes, FBX exports, Unreal Content assets, material instances, texture assets, material graphs, import scripts, validators, runtime source, Blueprints, sockets, animation assets, review actors, startup placement, or source concept movement.
- Stop before pickup, loot, inventory, storage UI, resource, salvage, harvesting, crafting/economy, vendor, workstation, usable storage, interaction prompts, objective logic, gate behavior, nav/pathfinding, cover tagging, destructible behavior, faction buffs, morale behavior, AI behavior, patrol/spawn logic, encounter scripting, VFX/audio, material-state behavior, or Hermes work.
- Stop before claiming collision correctness, runtime performance validation, camera approval, final silhouette approval, final storage approval, final Blood Axe camp approval, or final visual approval.
- Stop if Blood Axe hostile raider identity starts replacing neutral/civilized Giant culture.
- Stop if any future row appears to require changing the Giant scale lock from female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline, or the approved Giant ranges.

## Matrix Maintenance Validation

Use these docs-only checks after edits to this matrix:

- Matrix completeness scan: confirm parent package, package-ready child rows, material policy, LOD/collision policy, review rows, and scale rows from `CHILD_ASSET_INTAKE.md` are represented.
- Package-path existence scan: confirm every path listed as package-ready exists.
- Approval-gate scan: confirm DCC, FBX, Unreal, runtime, validator creation, startup placement, final visual approval, first target selection, and implementation order approval remain blocked.
- Giant scale scan: confirm female 442 cm / 14 ft 6 in, male 470 cm / 15 ft 5 in, females 14-15 ft / 427-457 cm, and males 14 ft 10 in-16 ft 0 in / 452-488 cm remain present.
- Culture separation scan: confirm Blood Axe is described as a hostile Giant sub-faction and neutral/civilized Giant culture remains explicitly separate.
- Implementation-claim scan: confirm the matrix contains no claim that source, DCC, FBX, Unreal Content, runtime, validator, startup, visual approval, storage gameplay, inventory/loot behavior, or implementation work has started.
- Whitespace and diff validation: run `git diff --check -- docs/assets/kits/KIT_GIA_BloodAxeCratesSacksBaskets_A01/IMPLEMENTATION_READINESS_MATRIX.md`.

## Quality Gate Checklist

- Matrix is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, material graph, VFX/audio asset, global index, backlog, bootstrap, child intake doc, source folder, image, unrelated package file, or production package.
- Storage package rows are classified by readiness using the child intake and current package files.
- Material policy, LOD/collision policy, review-only rows, and scale rows are represented separately from buildable static-mesh candidates.
- Giant scale lock is explicit: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline; approved Giant ranges females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Package inventory does not imply build order, implementation order, DCC target selection, Unreal target selection, or final visual approval.
- Pickup, loot, inventory, storage UI, resource, salvage, crafting/economy, vendor behavior, usable storage, interaction prompts, objective logic, gate behavior, nav/pathfinding, cover behavior, destructible behavior, AI/encounter behavior, VFX/audio, material-state behavior, cloth/physics, source asset creation, startup placement, and final approval are explicitly excluded.
- Source concept remains external and is not copied, moved, edited, embedded, inspected for visual approval, or committed.

## Non-Authorization Statement

This readiness matrix is a documentation artifact only. It authorizes no source folder, DCC target, implementation order, Blender work, mesh work, FBX export, Unreal Content import, material authoring, runtime source, validator creation, startup placement, final visual approval, final Blood Axe storage approval, Hermes work, storage gameplay, pickup/loot/inventory/vendor/resource behavior, or final Giant culture approval.
