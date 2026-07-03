# KIT_GIA_BloodAxePathMarkers_A01 Implementation Readiness Matrix

## Scope

- Task: `AET-MA-20260629-373`
- Scope type: docs-only implementation readiness matrix.
- Owned file: `docs/assets/kits/KIT_GIA_BloodAxePathMarkers_A01/IMPLEMENTATION_READINESS_MATRIX.md`
- Source package: `docs/assets/kits/KIT_GIA_BloodAxePathMarkers_A01/PRODUCTION_PACKAGE.md`
- Source intake: `docs/assets/kits/KIT_GIA_BloodAxePathMarkers_A01/CHILD_ASSET_INTAKE.md`
- Material policy: `docs/assets/kits/DOC_GIA_BloodAxePathMarkerMaterialDiscipline_A01/PRODUCTION_PACKAGE.md`
- LOD/collision policy: `docs/assets/kits/DOC_GIA_BloodAxePathMarkerLODAndCollision_A01/PRODUCTION_PACKAGE.md`

This matrix classifies the Blood Axe path-marker package set by documentation readiness and remaining blockers. It does not select a first DCC target, approve implementation order, create source folders, start DCC work, export FBX files, import Unreal assets, create validators, place startup actors, approve final visuals, define path gameplay, or authorize Hermes work.

## Scale And Culture Lock

- Giant scale lock: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline; approved Giant ranges females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Future source work, if separately assigned, must preserve centimeter scale with 1 Unreal unit = 1 cm.
- Blood Axe is a hostile Giant sub-faction only. Blood Axe path-marker language must remain separate from neutral/civilized Giant culture.
- Blood Axe path-marker language may use rough field stone, scorched timber, hide ties, rope, blackened iron, broken shield scrap, soot, ash, mud, oxide red cloth, dull bone, and horn.
- Neutral/civilized Giant culture remains separate: refined cave-town masonry, blue-gray civic stonework, terraces, waterworks, warm hearth settlement identity, peaceful highland route markers, civic mason marks, restrained blue rune culture, and hidden-settlement polish are not Blood Axe defaults.

## Readiness Key

- `Package-ready`: production package exists and can be referenced by a later separately approved lane; implementation remains blocked.
- `Policy-ready`: docs-only material, LOD, collision, review, or scale package exists for consistency; it is not a buildable mesh target.
- `Review-only`: package supports non-shipping comparison rows; it does not create an Unreal actor, validator, capture, startup placement, or final visual approval.
- `Implementation blocked`: no source, DCC, FBX, Unreal Content, runtime, validator, startup, final visual approval, first DCC target, or implementation target exists.

## Package-Ready Path-Marker Rows

| Asset/package | Current state | Package path | Readiness blockers | Approval gates | DCC preconditions | Unreal preconditions | Residual risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `KIT_GIA_BloodAxePathMarkers_A01` | Parent kit package and child intake ready; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxePathMarkers_A01/PRODUCTION_PACKAGE.md` | Child packages are docs-only; no DCC, Unreal, validator, startup, final visual, or target selection exists | Lead must approve any later implementation lane without selecting it here | Separate task must own source scope, module split, pivots, scale proof, LOD source plan, and collision policy | Separate task must own import scope, material instances, LODs, collision setup, validation, and placement scope | Parent kit could be mistaken for a single collapsed mesh or implementation queue |
| `SM_GIA_BloodAxeCairnPathMarker_A01` | Package-ready single cairn; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeCairnPathMarker_A01/PRODUCTION_PACKAGE.md` | No source mesh, collision proxy, Unreal asset, or target selection | Static visual marker approval only; no waypoint or route behavior | Future DCC must preserve few large stones, soot/mud base, Giant scale, and no pebble carpet | Future Unreal work must keep collision disabled by default or simple non-blocking query only | Could become a breadcrumb waypoint if repeated too evenly |
| `KIT_GIA_BloodAxeCairnPathMarkerCluster_A01` | Package-ready cairn cluster; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeCairnPathMarkerCluster_A01/PRODUCTION_PACKAGE.md` | No source folders, placement plan, collision setup, or review actor | Visual cluster approval only; no encounter lane or nav helper | Future DCC must keep two to five chunky cairns modular and uneven | Future Unreal work must avoid route scripting, nav helpers, objective clusters, and startup placement | Cluster could read as a formal path guide if spacing is too regular |
| `SM_GIA_BloodAxeCairnScrapCap_A01` | Package-ready scrap-cap cairn; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeCairnScrapCap_A01/PRODUCTION_PACKAGE.md` | No salvage, destructible, loot, DCC, Unreal, or implementation target | Static warning dressing approval only | Future DCC must keep shield rim or scrap cap large and sparse | Future Unreal work must avoid pickup, salvage, loot, destructible, and cover claims | Scrap cap could imply loot or destructible salvage |
| `SM_GIA_BloodAxeClothStakeMarker_A01` | Package-ready cloth stake; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeClothStakeMarker_A01/PRODUCTION_PACKAGE.md` | No cloth simulation, wind animation, DCC, Unreal, or target selection | Static cloth silhouette approval only | Future DCC must model broad static cloth, scorched timber, hide wrap, and few large ties | Future Unreal work must avoid cloth, wind, UI arrow, waypoint, and startup placement | Red cloth could overread as UI or objective marker |
| `KIT_GIA_BloodAxeClothStakeMarkerSet_A01` | Package-ready cloth stake set; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeClothStakeMarkerSet_A01/PRODUCTION_PACKAGE.md` | No fence collision, pathfinding blocker, trap, DCC, Unreal, or target selection | Static visual rhythm approval only | Future DCC must keep uneven spacing and per-stake reuse | Future Unreal work must avoid fence blockers, tripwire, trap, path boundary, and objective logic | Set could become a fence or gameplay boundary |
| `SM_GIA_BloodAxeLowRedRagMarker_A01` | Package-ready low rag marker; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeLowRedRagMarker_A01/PRODUCTION_PACKAGE.md` | No collectible flag, capture marker, patrol marker, DCC, Unreal, or target selection | Static low warning read only | Future DCC must keep low rag broad, sparse, and ground-adjacent | Future Unreal work must avoid capture marker, collectible flag, UI arrow, patrol marker, and trail gameplay | Low red accent could look like an objective cue |
| `SM_GIA_BloodAxeBoneHornPathMarker_A01` | Package-ready bone/horn marker; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeBoneHornPathMarker_A01/PRODUCTION_PACKAGE.md` | No pickup, loot, crafting resource, ritual mechanic, DCC, Unreal, or target selection | Non-graphic warning approval only | Future DCC must keep horn/bone sparse, blunt, large, and non-graphic | Future Unreal work must avoid pickup, loot, resource, ritual state, VFX, and startup placement | Bone/horn detail could drift into gore or loot language |
| `SM_GIA_BloodAxeHornForkMarker_A01` | Package-ready horn fork marker; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeHornForkMarker_A01/PRODUCTION_PACKAGE.md` | No signal device, faction aura, VFX pulse, DCC, Unreal, or implementation target | Static warning silhouette approval only | Future DCC must preserve forked silhouette and ash-dark base without dense tokens | Future Unreal work must avoid signal, aura, shamanic state, VFX/audio, and startup placement | Fork silhouette could imply a magic signal device |
| `KIT_GIA_BloodAxeBoneHornTokenSet_A01` | Package-ready token set; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeBoneHornTokenSet_A01/PRODUCTION_PACKAGE.md` | No pickups, inventory items, crafting ingredients, loot, ritual mechanics, DCC, Unreal, or target selection | Visual parts approval only | Future DCC must keep tokens modular but not item-like | Future Unreal work must avoid pickup, inventory, crafting, loot, and interaction tags | Token set could be mistaken for collectible resources |
| `SM_GIA_BloodAxeBrokenShieldPathMarker_A01` | Package-ready broken shield marker; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeBrokenShieldPathMarker_A01/PRODUCTION_PACKAGE.md` | No usable shield, pickup, loot, destructible, combat cover, DCC, Unreal, or target selection | Static hostile warning approval only | Future DCC must keep one large broken shield fragment and simple ties | Future Unreal work must avoid shield use, pickup, loot, cover definition, and destructible setup | Shield silhouette could imply cover or usable gear |
| `SM_GIA_BloodAxeScrapShieldLeanMarker_A01` | Package-ready scrap shield lean marker; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeScrapShieldLeanMarker_A01/PRODUCTION_PACKAGE.md` | No blocker behavior, gate logic, nav hint, objective marker, pickup, loot, DCC, Unreal, or target selection | Static gate-adjacent dressing approval only | Future DCC must keep lean stable, broad, and non-interactive | Future Unreal work must avoid gate logic, blockers, nav hints, objective markers, and startup placement | Lean marker could be misread as a gate blocker |
| `SM_GIA_BloodAxeAshStainedBase_A01` | Package-ready ash base; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeAshStainedBase_A01/PRODUCTION_PACKAGE.md` | No decal gameplay, trail tracking, gatherable ash, damage field, VFX, DCC, Unreal, or target selection | Static ground dressing approval only | Future DCC must keep ash broad, matte, low, and non-directional | Future Unreal work must avoid particles, damage fields, trail tracking, decals-as-gameplay, and startup placement | Ash base could read as route or hazard if too directional |
| `KIT_GIA_BloodAxeAshPathBaseSet_A01` | Package-ready ash path base set; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxeAshPathBaseSet_A01/PRODUCTION_PACKAGE.md` | No trail-marker gameplay, nav hints, objective pathing, footprint tracking, DCC, Unreal, or target selection | Static visual rhythm approval only | Future DCC must keep pads irregular and visually subordinate to markers | Future Unreal work must avoid nav hints, objective pathing, trail tracking, and startup placement | Set could become a gameplay trail if arranged continuously |
| `KIT_GIA_BloodAxePathMarkerCluster_A01` | Package-ready mixed cluster; implementation blocked | `docs/assets/kits/KIT_GIA_BloodAxePathMarkerCluster_A01/PRODUCTION_PACKAGE.md` | No review actor, objective cluster, route scripting, encounter setup, DCC, Unreal, or target selection | Static composition approval only | Future DCC must preserve one dominant marker and reuse child modules | Future Unreal work must avoid review actors, route scripts, objective clusters, encounter setup, and startup placement | Cluster could be overused as an encounter/objective marker |

## Policy And Review Rows

| Document/package | Current state | Package path | Use | Non-authorization |
| --- | --- | --- | --- | --- |
| `DOC_GIA_BloodAxePathMarkerMaterialDiscipline_A01` | Policy-ready material package | `docs/assets/kits/DOC_GIA_BloodAxePathMarkerMaterialDiscipline_A01/PRODUCTION_PACKAGE.md` | Shared material rules for rough field stone, scorched timber, hide, rope, blackened iron, ash, mud, oxide red cloth, dull bone, and horn | No material instance, texture asset, material graph, shader, emissive, VFX, Unreal Content, DCC, final color approval, or implementation target |
| `DOC_GIA_BloodAxePathMarkerLODAndCollision_A01` | Policy-ready LOD/collision package | `docs/assets/kits/DOC_GIA_BloodAxePathMarkerLODAndCollision_A01/PRODUCTION_PACKAGE.md` | LOD0-LOD3 reduction and disabled-by-default collision policy for all marker families | No LOD source, collision proxy, UCX mesh, nav blocker, gameplay volume, validator, Unreal Content, DCC, final visual approval, or implementation target |
| `DOC_GIA_BloodAxePathMarkerReviewRows_A01` | Review-only package-ready rows | `docs/assets/kits/DOC_GIA_BloodAxePathMarkerReviewRows_A01/PRODUCTION_PACKAGE.md` | Route rhythm, marker repetition, low/mid silhouette variation, camp approach bends, mixed clusters, and camera-readability planning | No Unreal actor, capture automation, validator, startup placement, final visual signoff, DCC, Unreal Content, or implementation target |
| `DOC_GIA_BloodAxePathMarkerScaleRows_A01` | Review-only package-ready rows | `docs/assets/kits/DOC_GIA_BloodAxePathMarkerScaleRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping scale rows beside female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in Giant baselines | No scale-lock change, shipped marker approval, DCC, FBX, Unreal, validator, capture, startup placement, final approval, or implementation target |

## Source And Export Path Plan

The paths below are future planning references only. This matrix does not create folders, source files, exports, imports, validators, startup actors, or implementation targets.

| Family | Planned source root if later approved | Planned export root if later approved | Planned Unreal target root if later approved |
| --- | --- | --- | --- |
| Path-marker static props | `SourceAssets/Blender/Kits/Giants/BloodAxeCamp/PathMarkers/` | `SourceAssets/Exports/Kits/Giants/BloodAxeCamp/PathMarkers/` | `/Game/Aerathea/Props/Giants/BloodAxeCamp/PathMarkers/` |
| Path-marker review rows | Not selected | Not selected | Not applicable unless a later non-shipping review-scene task owns it |
| Shared material policy | Not applicable from this matrix | Not applicable from this matrix | `/Game/Aerathea/Materials/Giants/BloodAxe/` only if a later material task owns it |

No first source folder, export folder, Unreal folder, material folder, review actor, validator, or implementation target is selected here.

## DCC Readiness Preconditions

A later DCC lane must explicitly approve and own all of the following before source work begins:

- Exact source and export file scope.
- Chosen DCC target or targets; this matrix does not choose them.
- Per-child module split, mesh naming, pivot, orientation, centimeter scale proof, and scale comparison against the female 442 cm and male 470 cm Giant baselines.
- LOD0-LOD3 source expectations and reduction order from `DOC_GIA_BloodAxePathMarkerLODAndCollision_A01`.
- Material-slot policy from `DOC_GIA_BloodAxePathMarkerMaterialDiscipline_A01`.
- Static-shape policy for cloth, rope, ash, mud, horn, bone, and shield scrap.
- Culture-separation review against neutral/civilized Giant cave-town and highland route-marker language.
- Review artifact plan that remains non-final until separate visual approval exists.

## Unreal Readiness Preconditions

A later Unreal lane must explicitly approve and own all of the following before engine work begins:

- Import path, asset ownership, and file scope.
- Whether each row becomes a shipping static mesh, remains a docs-only package, or becomes a non-shipping review artifact.
- Import scale proof at 1 Unreal unit = 1 cm.
- LOD0-LOD3 presence for shipping static mesh candidates.
- Material instance and texture ownership, with no default emissive unless a separate approved variant exists.
- Disabled-by-default collision or a separately approved simple non-blocking query exception.
- Focused validation plan owned by the future Unreal/QA task.
- Any startup placement, review capture, marker pass, final visual approval, or final package implementation approval in separately assigned tasks.

This matrix does not create Unreal Content, material instances, textures, Blueprints, sockets, collision proxies, validators, review actors, startup actors, or runtime source.

## Validator Gaps And Future Checks

No validator is authored by this matrix. Future implementation lanes should add focused validators only when they own the affected tool paths.

| Future lane | Validator need |
| --- | --- |
| DCC source/export | Confirm source path, export path, FBX name, centimeter scale, dimensions, pivot, LOD0-LOD3 sources, material slot count, and no micro-detail geometry misuse. |
| Giant scale | Compare dimensions against female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in baselines. |
| Path-marker import | Confirm Unreal path, LODs, material slots, simple/disabled collision policy, texture references, and no gameplay marker logic. |
| Material validation | Confirm shared Blood Axe material families, no default emissive, red accent restraint, roughness/metallic ranges, and no neutral/civilized Giant material drift. |
| Collision validation | Confirm collision disabled by default or simple non-blocking query only; no UCX, nav blockers, gameplay volumes, pickup volumes, trigger volumes, or collision correctness claims without a later lane. |
| Culture separation | Confirm Blood Axe docs do not claim default Giant culture, neutral cave-town identity, blue-gray stoneworker motifs, warm hearth language, or civilized Giant materials. |
| Source-storage | Confirm external concept art was not copied, embedded, moved, edited, inspected for visual approval, or committed. |
| Matrix maintenance | Confirm package-ready rows, policy rows, review rows, approval gates, and no-target-selected status remain aligned after docs/index integration. |

## Global Stop Gates

- Stop before selecting a first DCC, Unreal, source asset, gameplay, review-scene, validator, material, VFX/audio, startup, or implementation target from any row.
- Stop before source folder creation, DCC source, Blender files, meshes, sculpts, retopo, UVs, bakes, proof renders, LOD source files, collision proxies, UCX meshes, FBX exports, Unreal Content assets, material instances, texture assets, material graphs, import scripts, validators, runtime source, Blueprints, sockets, animation assets, review actors, startup placement, or source concept movement.
- Stop before waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, resource behavior, crafting/economy behavior, route validation, encounter scripting, AI patrol markers, spawn markers, interaction behavior, damage/aura volumes, UI arrows, readable signage, combat cover rules, destructible behavior, material-state behavior, VFX/audio, or Hermes work.
- Stop before claiming collision correctness, runtime performance validation, camera approval, final silhouette approval, final path-marker approval, final Giant culture approval, or final visual approval.
- Stop if Blood Axe hostile raider identity starts replacing neutral/civilized Giant culture.
- Stop if any future row appears to require changing the Giant scale lock from female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline, or the approved Giant ranges of females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.

## Matrix Maintenance Validation

Use these docs-only checks after edits to this matrix:

- Matrix completeness scan: confirm parent, package-ready child rows, material policy, LOD/collision policy, review rows, and scale rows from `CHILD_ASSET_INTAKE.md` are represented.
- Package-path existence scan: confirm every path listed as package-ready exists.
- Approval-gate scan: confirm DCC, FBX, Unreal, runtime, validator creation, startup placement, final visual approval, first target selection, and implementation order approval remain blocked.
- Giant scale scan: confirm female 442 cm / 14 ft 6 in, male 470 cm / 15 ft 5 in, females 14-15 ft / 427-457 cm, and males 14 ft 10 in-16 ft 0 in / 452-488 cm remain present.
- Culture separation scan: confirm Blood Axe is described as a hostile Giant sub-faction and neutral/civilized Giant culture remains explicitly separate.
- Implementation-claim scan: confirm the matrix contains no claim that source, DCC, FBX, Unreal Content, runtime, validator, startup, visual approval, path gameplay, or implementation work has started.
- Whitespace and diff validation: run `git diff --check -- docs/assets/kits/KIT_GIA_BloodAxePathMarkers_A01/IMPLEMENTATION_READINESS_MATRIX.md`.

## Quality Gate Checklist

- Matrix is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, material graph, VFX/audio asset, global index, task board, backlog, bootstrap, child intake doc, source folder, image, unrelated package file, or production package.
- Path-marker package rows are classified by readiness using the child intake and current package files.
- Material policy, LOD/collision policy, review-only rows, and scale rows are represented separately from buildable static-mesh candidates.
- Giant scale lock is explicit: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline; approved Giant ranges females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Package inventory does not imply build order, implementation order, DCC target selection, Unreal target selection, or final visual approval.
- Waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, resource behavior, crafting/economy behavior, AI/encounter behavior, VFX/audio, material-state behavior, cloth/physics, source asset creation, startup placement, and final approval are explicitly excluded.
- Source concept remains external and is not copied, moved, edited, embedded, inspected for visual approval, or committed.

## Non-Authorization Statement

This readiness matrix is a documentation artifact only. It authorizes no source folder, DCC target, implementation order, Blender work, mesh work, FBX export, Unreal Content import, material authoring, runtime source, validator creation, startup placement, final visual approval, final Blood Axe path-marker approval, Hermes work, or final Giant culture approval.
