# KIT_GIA_BloodAxeCampTools_A01 Implementation Readiness Matrix

## Scope

- Task: `AET-MA-20260629-451`
- Scope type: docs-only implementation readiness matrix.
- Owned file: `docs/assets/kits/KIT_GIA_BloodAxeCampTools_A01/IMPLEMENTATION_READINESS_MATRIX.md`
- Source package: `docs/assets/kits/KIT_GIA_BloodAxeCampTools_A01/PRODUCTION_PACKAGE.md`
- Source intake: `docs/assets/kits/KIT_GIA_BloodAxeCampTools_A01/CHILD_ASSET_INTAKE.md`
- Validation source: `docs/agents/AET-MA-20260629-439_VALIDATION_SUMMARY.md`
- Integration source: `docs/agents/AET-MA-20260629-440_INTEGRATION_SUMMARY.md`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Clutter_ToolBucketRopeCoils`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only

This matrix classifies all 25 Blood Axe camp-tools package, review, and policy rows by documentation readiness, remaining blockers, approval gates, DCC preconditions, Unreal preconditions, and future validation needs. It does not select a first DCC target, approve implementation order, create source folders, start DCC work, export FBX files, import Unreal assets, create validators, place startup actors, approve final visuals, define usable workstation behavior, define pickup behavior, define crafting/resource/economy behavior, define interaction behavior, define NPC work loops, define nav/pathfinding behavior, author rope/cloth/physics, author VFX/audio, author material graphs, or authorize Hermes work.

## Scale And Culture Lock

- Giant scale lock: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Future source work, if separately assigned, must author in centimeters with 1 Unreal unit = 1 cm.
- Blood Axe is a hostile Giant sub-faction only. Blood Axe camp-tool dressing must remain separate from neutral/civilized Giant culture.
- Blood Axe camp-tool language may use oversized crude utility forms, rough timber, blackened iron, dark steel, thick rope, hide lashings, scorched leather, soot, ash, mud, grime, dull red cloth ties, chipped red paint, and sparse non-graphic bone or horn accents.
- Neutral/civilized Giant culture remains separate: blue-gray cave-town masonry, refined stoneworker tools, terraces, waterworks, warm hearth presentation, peaceful highland craft, civic symbols, and restrained blue rune language are not Blood Axe defaults.

## No-Target-Selected Status

- First DCC target: not selected.
- First implementation target: not selected.
- Implementation order: not selected.
- Source folder: not selected and not created.
- Export folder: not selected and not created.
- Unreal import target: not selected and not created.
- Startup placement: not selected and not created.
- Final approval: not requested and not granted.

## Readiness Key

- `Package-ready`: production package exists and can be referenced by a later separately approved lane; implementation remains blocked.
- `Policy-ready`: docs-only material, LOD, collision, review, or scale package exists for consistency; it is not a buildable mesh target.
- `Review-only`: package supports non-shipping comparison rows; it does not create an Unreal actor, validator, capture, startup placement, or final visual approval.
- `Implementation blocked`: no source, DCC, FBX, Unreal Content, runtime, validator, startup, final visual approval, first DCC target, or implementation target exists.

## Package-Ready Child Rows

| Asset/package | Current state | Package path | Readiness blockers | Approval gates | DCC preconditions | Unreal preconditions | Validator gaps and residual risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SM_GIA_BloodAxeToolBucket_A01` | Package-ready tool bucket; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeToolBucket_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, collision proxy, Unreal asset, or target selection | Static dressing only; no usable workstation, pickup, storage contents, loot, resource, economy, or interaction behavior | Future DCC must preserve 90-180 cm Giant bucket scale, thick rim, open silhouette, and sparse tool-handle read | Future Unreal work must avoid container UI, item components, pickup prompts, and startup placement | Needs future scale, material-slot, collision, and no-pickup scans; could read as loot/storage if too polished |
| `SM_GIA_BloodAxeIronRimToolBucket_A01` | Package-ready iron-rim bucket; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeIronRimToolBucket_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal asset, material instance, or target selection | Static bucket variant only; no vendor, economy, loot, resource, container, pickup, or interaction behavior | Future DCC must keep dark iron rim broad, battered, and secondary to Giant-scale bucket mass | Future Unreal work must avoid inventory/container components and material-state claims | Needs future iron/wood material validation; red accents could become item markers if overused |
| `SM_GIA_BloodAxeCarryTub_A01` | Package-ready carry tub; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeCarryTub_A01/PRODUCTION_PACKAGE.md` | No tub source, contents source, DCC, Unreal, or target selection | Static visual tub only; no resource crate, crafting bin, usable container, economy stock, pickup, or interaction behavior | Future DCC must prove scale against female 442 cm and male 470 cm Giants and keep visible contents non-specific | Future Unreal work must avoid resource, inventory, and storage UI components | Needs future scale/culture checks; could imply resource storage if contents become readable items |
| `SM_GIA_BloodAxeRopeCoil_A01` | Package-ready rope coil; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeRopeCoil_A01/PRODUCTION_PACKAGE.md` | No source mesh, rope physics, DCC, Unreal, or target selection | Static rope dressing only; no rope/cloth/physics, climbing, tripwire, pickup, nav/pathfinding, or interaction behavior | Future DCC must model broad fixed coil volumes and large knots while keeping fibers/fray in textures | Future Unreal work must avoid physics bodies, cable components, climb logic, and startup placement | Needs future rope-physics overclaim scan; could become simulation-heavy if coil turns are over-modeled |
| `SM_GIA_BloodAxeTieDownRopeCoil_A01` | Package-ready tie-down rope coil; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeTieDownRopeCoil_A01/PRODUCTION_PACKAGE.md` | No source mesh, sockets, DCC, Unreal, rope sim, or target selection | Visual tie-down language only; no gate behavior, trap logic, pathfinding, objective, physics, pickup, or interaction behavior | Future DCC must keep tie loop, stake, or ring as fixed geometry and avoid mechanical rigging claims | Future Unreal work must avoid gate links, constraints, rope simulation, nav blockers, and startup placement | Needs future gate/pathfinding guardrail scan; could drift into functional tie-down logic |
| `KIT_GIA_BloodAxeRopeBundleSet_A01` | Package-ready rope bundle set; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeRopeBundleSet_A01/PRODUCTION_PACKAGE.md` | No composed source, DCC, Unreal, physics setup, or target selection | Static bundle dressing only; no crafting ingredient, resource item, pickup, inventory, rope/cloth/physics, or interaction behavior | Future DCC must keep bundle count sparse and fixed, with thick Giant-scale knots | Future Unreal work must avoid per-rope collision, pickup components, and inventory/resource data | Needs future per-child split validation; could become pickup-like if bundled too neatly |
| `SM_GIA_BloodAxeHeavyHookSet_A01` | Package-ready heavy hook set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeHeavyHookSet_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, collision proxy, Unreal asset, or target selection | Static hook dressing only; no pickup, weapon use, trap use, interaction volume, physics, or usable workstation behavior | Future DCC must preserve 70-180 cm hook length, strong curved silhouette, and sparse count | Future Unreal work must avoid weapon traces, trap components, pickup prompts, and sharp collision gameplay | Needs future weapon/trap overclaim scan; hooks could become weapon-like if staged aggressively |
| `SM_GIA_BloodAxeStakeHook_A01` | Package-ready stake hook; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeStakeHook_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, collision proxy, Unreal asset, nav behavior, or target selection | Static support prop only; no nav blocker, trap, objective, gate logic, rope physics, pickup, or interaction behavior | Future DCC must keep stake base crude, broad, and secondary to visual tie-down role | Future Unreal work must avoid nav/pathfinding flags, physics constraints, and gameplay collision claims | Needs future nav and collision guardrail scans; could be mistaken for a blocker or trap anchor |
| `SM_GIA_BloodAxeHangingHookRail_A01` | Package-ready hanging hook rail; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeHangingHookRail_A01/PRODUCTION_PACKAGE.md` | No rail source, hanging physics, DCC, Unreal, sockets, or target selection | Static rail only; no hanging simulation, usable rack, pickup, workstation, cloth/rope physics, or interaction behavior | Future DCC must keep hooks sparse and distinguish from specialized bowyer racks | Future Unreal work must avoid sockets, simulated hanging items, pickup components, and startup actors | Needs future bowyer-boundary scan; could overlap `KIT_GIA_BloodAxeBowyerTools_A01` if over-specialized |
| `SM_GIA_BloodAxeWedgeSet_A01` | Package-ready wedge set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeWedgeSet_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal, collision proxy, or target selection | Static wedge dressing only; no harvest node, crafting ingredient, destructible setup, resource, salvage, economy, pickup, or interaction behavior | Future DCC must keep blunt triangular wedge profiles readable from MMO camera distance | Future Unreal work must avoid resource/salvage components, destructible tags, and startup placement | Needs future resource/destructible overclaim scan; could read as collectible if scaled too small |
| `SM_GIA_BloodAxeIronWedgeStack_A01` | Package-ready iron wedge stack; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeIronWedgeStack_A01/PRODUCTION_PACKAGE.md` | No stack source, material graph, DCC, Unreal, or target selection | Static forge-adjacent dressing only; no crafting/resource/economy, salvage, heat behavior, usable workstation, pickup, or VFX/audio | Future DCC must keep wedge stack broad, soot-dark, and not ore-like or treasure-like | Future Unreal work must avoid resource, salvage, heat material states, and interaction prompts | Needs future material validation; shiny metal could imply resource or loot |
| `SM_GIA_BloodAxeChockBlockSet_A01` | Package-ready chock block set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeChockBlockSet_A01/PRODUCTION_PACKAGE.md` | No source mesh, physics constraint, DCC, Unreal, gate logic, or target selection | Visual support props only; no physics constraints, gate behavior, destructible behavior, nav/pathfinding, pickup, or interaction behavior | Future DCC must keep chocks heavy and readable without implying mechanical operation | Future Unreal work must avoid constraints, gate links, nav blockers, and destructible setup | Needs future physics/gate scan; could imply functional blocking if placed at gates |
| `SM_GIA_BloodAxeMallet_A01` | Package-ready heavy mallet; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeMallet_A01/PRODUCTION_PACKAGE.md` | No source mesh, weapon setup, DCC, Unreal, animation, or target selection | Display prop only; no weapon trace, pickup, tool use, crafting loop, NPC work loop, usable workstation, or interaction behavior | Future DCC must preserve 140-260 cm Giant tool scale and utility-prop read instead of weapon read | Future Unreal work must avoid weapon collision, sockets, pickup components, animations, and startup placement | Needs future weapon/pickup/NPC-loop scans; could turn into combat prop if given sockets |
| `SM_GIA_BloodAxeSledgeMallet_A01` | Package-ready sledge mallet; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeSledgeMallet_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal, weapon/crafting setup, or target selection | Static forge-adjacent prop only; no usable workstation, crafting/resource/economy, weapon use, pickup, NPC loop, or interaction behavior | Future DCC must keep rectangular head, dark bands, and worn handle as static display geometry | Future Unreal work must avoid forge station tags, weapon traces, pickup prompts, and animation claims | Needs future workstation/crafting overclaim scan; could imply usable forge tool |
| `SM_GIA_BloodAxeMalletPair_A01` | Package-ready mallet pair; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeMalletPair_A01/PRODUCTION_PACKAGE.md` | No composed source, DCC, Unreal, sockets, animation, or target selection | Static paired dressing only; no skeletal attachment, pickup behavior, NPC work loop, usable tool behavior, or interaction behavior | Future DCC must keep pair composition sparse and shelter-edge friendly | Future Unreal work must avoid attachment sockets, NPC task links, pickup behavior, and startup placement | Needs future attachment/NPC-loop scan; crossed staging could imply usable tools if overposed |
| `KIT_GIA_BloodAxeTieHardware_A01` | Package-ready tie hardware kit; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeTieHardware_A01/PRODUCTION_PACKAGE.md` | No hardware source, per-link collision, DCC, Unreal, physics, or target selection | Secondary static detail only; no rope/cloth/physics, per-link collision, constraints, pickup, resource, objective, trap, or interaction behavior | Future DCC must keep rings, pegs, plates, and chain lengths as low-count fixed forms | Future Unreal work must avoid constraints, physics assets, per-link collision, and interaction volumes | Needs future collision/physics scans; could become expensive if chain links are over-modeled |
| `SM_GIA_BloodAxeRingPegSet_A01` | Package-ready ring peg set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeRingPegSet_A01/PRODUCTION_PACKAGE.md` | No source mesh, rope sim, DCC, Unreal, objective/nav behavior, or target selection | Static perimeter dressing only; no rope simulation, physics constraint, nav blocker, trap, objective logic, pickup, or interaction behavior | Future DCC must preserve ground-contact readability without implying active anchor logic | Future Unreal work must avoid nav/pathfinding flags, constraints, traps, and objective components | Needs future objective/nav guardrail scan; could be mistaken for route or trap system |
| `SM_GIA_BloodAxeCampUtilityCluster_A01` | Package-ready small utility cluster; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeCampUtilityCluster_A01/PRODUCTION_PACKAGE.md` | No composed source, collision proxy, DCC, Unreal, startup placement, or target selection | Non-interactive set dressing only; no usable workstation, pickup, crafting/resource/economy, interaction, NPC loop, nav/pathfinding, or startup behavior | Future DCC must keep 250-600 cm low cluster footprint with clear negative space for Giant scale | Future Unreal work must avoid startup placement, gameplay collision, nav blockers, and interaction prompts | Needs future cluster-density and nav scans; could block lanes if composed too densely |
| `SM_GIA_BloodAxePathEdgeUtilityCluster_A01` | Package-ready path-edge utility cluster; implementation blocked | `docs/assets/props/SM_GIA_BloodAxePathEdgeUtilityCluster_A01/PRODUCTION_PACKAGE.md` | No path placement, collision proxy, DCC, Unreal, nav behavior, or target selection | Static path-edge dressing only; no nav/pathfinding, route marker, encounter, cover, pickup, resource, interaction, or startup placement | Future DCC must keep low path-edge profile and preserve Giant-scale visual lanes | Future Unreal work must avoid nav blockers, path logic, cover tags, and startup actors | Needs future path/nav guardrail scan; could become route-control work if overclaimed |
| `SM_GIA_BloodAxeForgeSupportUtilityCluster_A01` | Package-ready forge support cluster; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeForgeSupportUtilityCluster_A01/PRODUCTION_PACKAGE.md` | No composed source, heat setup, DCC, Unreal, material graph, VFX/audio, or target selection | Visual forge support only; no usable workstation, heat gameplay, crafting/resource/economy, VFX/audio, material graph, pickup, or interaction behavior | Future DCC must keep forge adjacency visual without replacing forge station or scrap-sorting ownership | Future Unreal work must avoid workstation tags, heat materials, particles, audio, resource components, and startup placement | Needs future heat/workstation/material scans; could overlap forge packages if too broad |
| `SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01` | Package-ready shelter-edge utility cluster; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01/PRODUCTION_PACKAGE.md` | No shelter placement, cloth/rope physics, DCC, Unreal, NPC loop, or target selection | Static shelter-edge dressing only; no shelter interaction, NPC work loops, pickup, cloth physics, rope physics, interaction behavior, or startup actor | Future DCC must keep cluster secondary to shelter silhouette and avoid simulated hanging pieces | Future Unreal work must avoid shelter links, NPC task markers, simulated cloth/rope, pickup components, and startup placement | Needs future shelter/NPC/physics scans; could imply work-loop staging if placed too narratively |

## Review And Policy Rows

| Document/package | Current state | Package path | Use | Non-authorization | Future validation need |
| --- | --- | --- | --- | --- | --- |
| `DOC_GIA_BloodAxeCampToolsReviewRows_A01` | Review-only package-ready rows; implementation blocked | `docs/assets/kits/DOC_GIA_BloodAxeCampToolsReviewRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping comparison rows for bucket, coil, hook, wedge, mallet, tie hardware, and cluster spacing, density, and MMO readability | No Unreal actor, validator, capture automation, startup placement, final visual signoff, DCC, Unreal Content, implementation target, or first DCC target | Future QA should confirm rows remain non-shipping and do not become capture or startup tasks without approval |
| `DOC_GIA_BloodAxeCampToolsScaleRows_A01` | Review-only package-ready scale rows; implementation blocked | `docs/assets/kits/DOC_GIA_BloodAxeCampToolsScaleRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping scale rows beside female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines | No scale-lock change, shipped marker approval, DCC, FBX, Unreal, validators, captures, startup placement, final approval, or implementation target | Future QA should confirm the Giant scale lock and approved ranges remain unchanged |
| `DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01` | Policy-ready LOD/collision package; implementation blocked | `docs/assets/kits/DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01/PRODUCTION_PACKAGE.md` | LOD0-LOD3 and collision-limit policy for buckets, rope coils, hooks, wedges, mallets, tie hardware, utility clusters, and review rows | No collision proxies, UCX meshes, nav blockers, gameplay volumes, validator files, Unreal Content, DCC, final approval, first DCC target, or implementation target | Future QA should confirm simple/disabled collision, no gameplay volumes, no nav blockers, and no per-rope or per-link collision claims |
| `DOC_GIA_BloodAxeCampToolsMaterialRows_A01` | Policy-ready material package; implementation blocked | `docs/assets/kits/DOC_GIA_BloodAxeCampToolsMaterialRows_A01/PRODUCTION_PACKAGE.md` | Shared material discipline for blackened iron, dark steel, scorched timber, rope, hide, leather, soot, ash, mud, dull red ties, chipped red paint, and sparse bone or horn accents | No material instance, texture asset, material graph, VFX/audio, DCC, Unreal Content, startup placement, final color approval, first DCC target, or implementation target | Future QA should confirm no default emissive, no material graph work, red accent restraint, and no neutral/civilized Giant material drift |

## Source And Export Path Plan

The paths below are future planning references only. This matrix does not create folders, source files, exports, imports, validators, startup actors, or implementation targets.

| Family | Planned source root if later approved | Planned export root if later approved | Planned Unreal target root if later approved |
| --- | --- | --- | --- |
| Blood Axe camp-tools static props and clusters | `SourceAssets/Blender/Kits/Giants/BloodAxeCamp/CampTools/` | `SourceAssets/Exports/Kits/Giants/BloodAxeCamp/CampTools/` | `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/` |
| Camp-tools utility clusters | `SourceAssets/Blender/Kits/Giants/BloodAxeCamp/CampTools/UtilityClusters/` | `SourceAssets/Exports/Kits/Giants/BloodAxeCamp/CampTools/UtilityClusters/` | `/Game/Aerathea/Props/Giants/BloodAxeCamp/UtilityClusters/` |
| Camp-tools review and scale rows | Not selected | Not selected | Not applicable unless a later non-shipping review-scene task owns it |
| Shared camp-tools material policy | Not applicable from this matrix | Not applicable from this matrix | `/Game/Aerathea/Materials/Giants/BloodAxe/CampTools/` only if a later material task owns it |

No first source folder, export folder, Unreal folder, material folder, review actor, validator, DCC target, package implementation target, or build order is selected here.

## DCC Readiness Preconditions

A later DCC lane must explicitly approve and own all of the following before source work begins:

- Exact source and export file scope.
- Chosen DCC target or targets; this matrix does not choose them.
- Per-child module split, mesh naming, pivot, orientation, centimeter scale proof, and scale comparison against the female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines.
- LOD0-LOD3 source expectations and reduction order from `DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01`.
- Material-slot policy from `DOC_GIA_BloodAxeCampToolsMaterialRows_A01`.
- Static-shape policy for tool buckets, iron-rim buckets, carry tubs, rope coils, tie-down coils, rope bundles, hook sets, stake hooks, hanging hook rails, wedges, iron wedge stacks, chock blocks, mallets, tie hardware, ring pegs, and utility clusters.
- Culture-separation review against neutral/civilized Giant cave-town, warm hearth, and highland settlement tool language.
- Review artifact plan that remains non-final until separate visual approval exists.

The DCC lead must reject any direction that turns this kit into active workstation systems, loot piles, pickup objects, inventory items, resource nodes, crafting stations, economy objects, usable tool loops, NPC work loops, path blockers, nav markers, cover objects, destructible clutter, rope simulation, cloth simulation, physics piles, VFX emitters, audio emitters, material graph work, neutral Giant civic tool dressing, civilized Giant craft displays, or source-concept storage work.

## Unreal Readiness Preconditions

A later Unreal lane must explicitly approve and own all of the following before engine work begins:

- Import path, asset ownership, and exact file scope.
- Whether each row becomes a shipping static mesh, remains a docs-only package, or becomes a non-shipping review artifact.
- Import scale proof at 1 Unreal unit = 1 cm.
- LOD0-LOD3 presence for shipping static mesh candidates.
- Material instance and texture ownership, with no default emissive, glow, sparks, signal states, UI markers, or active material states unless a separate approved material/VFX task owns it.
- Collision disabled by default or a separately approved simple low blocking/query exception.
- Focused validation plan owned by the future Unreal/QA task.
- Any startup placement, review capture, marker pass, camera approval, final visual approval, first package implementation approval, or final package implementation approval in separately assigned tasks.

This matrix does not create Unreal Content, material instances, textures, Blueprints, sockets, collision proxies, validators, review actors, startup actors, VFX, audio, material graphs, or runtime source.

## Validator Gaps And Future Checks

No validator is authored by this matrix. Future implementation lanes should add focused validators only when they own the affected tool paths.

| Future lane | Validator need |
| --- | --- |
| DCC source/export | Confirm source path, export path, FBX name, centimeter scale, dimensions, pivot, LOD0-LOD3 sources, material slot count, and no micro-detail geometry misuse. |
| Giant scale | Compare dimensions against female 442 cm / 14'6" and male 470 cm / 15'5" baselines, plus approved Giant ranges. |
| Camp-tools import | Confirm Unreal path, LODs, material slots, simple/disabled collision policy, texture references, and no usable workstation, pickup, crafting/resource/economy, interaction, NPC work loop, nav/pathfinding, rope/cloth/physics, VFX/audio, material graph, runtime, or startup logic. |
| Material validation | Confirm shared Blood Axe material families, no default emissive, red accent restraint, roughness/metallic ranges, and no neutral/civilized Giant material drift. |
| Collision validation | Confirm collision disabled by default or simple low blocking/query only; no UCX, nav blockers, gameplay volumes, cover volumes, pickup volumes, interaction volumes, per-rope collision, per-link collision, or collision correctness claims without a later lane. |
| Review/policy validation | Confirm review rows remain non-shipping and policy rows do not create Unreal actors, captures, validators, material instances, startup placement, or final approval claims. |
| Culture separation | Confirm Blood Axe docs do not claim default Giant culture, neutral cave-town identity, warm hearth craft language, blue-gray stoneworker motifs, or civilized Giant materials. |
| Source-storage | Confirm external concept art was not copied, embedded, moved, edited, inspected for visual approval, or committed. |
| Matrix maintenance | Confirm package-ready rows, policy rows, review rows, approval gates, no-target-selected status, and package paths remain aligned after docs/index integration. |

## Global Stop Gates

- Stop before selecting a first DCC, Unreal, source asset, gameplay, review-scene, validator, material, VFX/audio, startup, or implementation target from any row.
- Stop before source folder creation, DCC source, Blender files, meshes, sculpts, retopo, UVs, bakes, proof renders, LOD source files, collision proxies, UCX meshes, FBX exports, Unreal Content assets, material instances, texture assets, material graphs, import scripts, validators, runtime source, Blueprints, sockets, animation assets, review actors, startup placement, VFX/audio, or source concept movement.
- Stop before usable workstation behavior, pickup behavior, inventory behavior, loot behavior, crafting/resource/economy behavior, salvage behavior, vendor behavior, interaction prompts, objective logic, NPC work loops, nav/pathfinding, cover behavior, destructible behavior, encounter behavior, AI behavior, patrol/spawn logic, rope/cloth/physics, material-state behavior, UI markers, quest markers, or Hermes work.
- Stop before claiming collision correctness, runtime performance validation, camera approval, final silhouette approval, final camp-tools approval, final Blood Axe camp approval, or final visual approval.
- Stop if Blood Axe hostile raider identity starts replacing neutral/civilized Giant culture.
- Stop if any future row appears to require changing the Giant scale lock from female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline, or the approved Giant ranges.

## Matrix Maintenance Validation

Use these docs-only checks after edits to this matrix:

- Matrix completeness scan: confirm all 25 package/review/policy rows from `CHILD_ASSET_INTAKE.md` are represented.
- Package-path existence scan: confirm every path listed as package-ready exists.
- Approval-gate scan: confirm DCC, FBX, Unreal, runtime, validator creation, startup placement, final visual approval, first target selection, and implementation order approval remain blocked.
- No-target-selected scan: confirm first DCC target, first implementation target, implementation order, source folder, export folder, Unreal target, startup target, and final approval remain not selected.
- Giant scale scan: confirm female 442 cm / 14'6", male 470 cm / 15'5", females 14-15 ft / 427-457 cm, and males 14'10"-16'0" / 452-488 cm remain present.
- Culture separation scan: confirm Blood Axe is described as a hostile Giant sub-faction and neutral/civilized Giant culture remains explicitly separate.
- Implementation-claim scan: confirm the matrix contains no claim that source, DCC, FBX, Unreal Content, runtime, validator, startup, visual approval, usable workstation behavior, pickup behavior, crafting/resource/economy behavior, interaction behavior, NPC work loops, nav/pathfinding, rope/cloth/physics, VFX/audio, material graph, or implementation work has started.
- Whitespace and diff validation: run `git diff --check -- docs/assets/kits/KIT_GIA_BloodAxeCampTools_A01/IMPLEMENTATION_READINESS_MATRIX.md`.

## Quality Gate Checklist

- Matrix is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, material graph, VFX/audio asset, global index, backlog, bootstrap, child intake doc, source folder, image, unrelated package file, or production package.
- All 25 camp-tools package/review/policy rows are classified by readiness using the child intake and current package files.
- Tool bucket, rope coil, hook, wedge, mallet, tie hardware, utility cluster, material policy, LOD/collision policy, review-only rows, and scale rows are represented separately.
- Giant scale lock is explicit: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Package inventory does not imply build order, implementation order, DCC target selection, Unreal target selection, startup placement, or final visual approval.
- Usable workstation, pickup, inventory, loot, crafting/resource/economy, vendor behavior, interaction prompts, objective logic, NPC work loops, nav/pathfinding, cover behavior, destructible behavior, AI/encounter behavior, rope/cloth/physics, VFX/audio, material-state behavior, material graph authoring, source asset creation, startup placement, final approval, first DCC target, and implementation target are explicitly excluded.
- Source concept remains external and is not copied, moved, edited, embedded, inspected for visual approval, or committed.

## Non-Authorization Statement

This readiness matrix is a documentation artifact only. It authorizes no source folder, DCC target, implementation order, Blender work, mesh work, FBX export, Unreal Content import, material authoring, runtime source, validator creation, startup placement, final visual approval, final Blood Axe camp-tools approval, Hermes work, usable workstation behavior, pickup behavior, crafting/resource/economy behavior, interaction behavior, NPC work loops, nav/pathfinding behavior, rope/cloth/physics, VFX/audio, material graph authoring, first DCC target, first implementation target, or final Giant culture approval.
