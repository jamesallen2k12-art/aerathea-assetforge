# KIT_GIA_BloodAxeAshSlagFirewood_A01 Implementation Readiness Matrix

## Scope

- Task: `AET-MA-20260629-448`
- Scope type: docs-only implementation readiness matrix.
- Owned file: `docs/assets/kits/KIT_GIA_BloodAxeAshSlagFirewood_A01/IMPLEMENTATION_READINESS_MATRIX.md`
- Source package: `docs/assets/kits/KIT_GIA_BloodAxeAshSlagFirewood_A01/PRODUCTION_PACKAGE.md`
- Source intake: `docs/assets/kits/KIT_GIA_BloodAxeAshSlagFirewood_A01/CHILD_ASSET_INTAKE.md`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Clutter_AshSlagFirewood`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only

This matrix classifies the Blood Axe ash piles, slag lumps, charcoal heaps, firewood stacks, scorched debris, forge clutter cluster, review rows, scale rows, material policy, and LOD/collision policy by documentation readiness, blockers, approval gates, and future validation needs. It does not select a first DCC target, approve implementation order, create source folders, start DCC work, export FBX files, import Unreal assets, create validators, place startup actors, approve final visuals, define resource gameplay, define heat or damage behavior, author VFX/audio, or authorize Hermes work.

## Scale And Culture Lock

- Giant scale lock: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Future source work, if separately assigned, must author in centimeters with 1 Unreal unit = 1 cm.
- Blood Axe is a hostile Giant sub-faction only. Ash, slag, charcoal, firewood, and scorched debris must remain separate from neutral/civilized Giant culture.
- Blood Axe residue language may use matte ash, gray soot, black dust, cooled slag, charcoal, charred bark, split raw wood, blackened metal scraps, scorched hide, mud, and restrained oxide red cloth or paint.
- Neutral/civilized Giant culture remains separate: blue-gray civic masonry, refined stoneworker craft, warm peaceful hearths, terraces, waterworks, restrained blue runes, and civic forge order are not Blood Axe defaults.

## Readiness Key

- `Package-ready`: production package exists and can be referenced by a later separately approved lane; implementation remains blocked.
- `Policy-ready`: docs-only material, LOD, collision, review, or scale package exists for consistency; it is not a buildable mesh target.
- `Review-only`: package supports non-shipping comparison rows; it does not create an Unreal actor, validator, capture, startup placement, or final visual approval.
- `Implementation blocked`: no source, DCC, FBX, Unreal Content, runtime, validator, startup, final visual approval, first DCC target, or implementation target exists.

## Package-Ready Child Rows

| Asset/package | Current state | Package path | Readiness blockers | Approval gates | DCC preconditions | Unreal preconditions | Residual risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SM_GIA_BloodAxeAshPiles_A01` | Package-ready ash pile set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeAshPiles_A01/PRODUCTION_PACKAGE.md` | No source mesh, terrain blend, collision proxy, Unreal asset, or target selection | Static residue only; no heat, ash drift VFX, damage, gatherable ash, crafting, or interaction | Future DCC must preserve low broad mound read and cheap silhouette | Future Unreal work must avoid particles, damage volumes, gatherable components, and startup placement | Could become VFX or terrain work if ash drift language is overclaimed |
| `SM_GIA_BloodAxeAshDrifts_A01` | Package-ready thin ash drift set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeAshDrifts_A01/PRODUCTION_PACKAGE.md` | No source mesh, terrain blend, DCC, Unreal, or target selection | Static visual drift only; no terrain system, VFX, collision proxy, or heat/damage behavior | Future DCC must keep forms low, broad, and non-simulated | Future Unreal work must avoid decals, landscape blending claims, and particles unless separately assigned | Could imply terrain blending or live ash movement |
| `SM_GIA_BloodAxeSlagLumps_A01` | Package-ready cooled slag set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeSlagLumps_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal, material graph, or target selection | Static cooled residue only; no ore, loot, salvage, harvestable resource, or economy behavior | Future DCC must keep matte crusted clumps distinct from ore or treasure | Future Unreal work must avoid resource components, pickup prompts, and hot material states | Slag could read as ore if color or shine drifts |
| `SM_GIA_BloodAxeSlagSpillStrips_A01` | Package-ready low slag spill set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeSlagSpillStrips_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal, material graph, or target selection | Static spill dressing only; no heat damage, VFX, resource, salvage, or economy behavior | Future DCC must keep spill strips low and separate from anvil/quench ownership | Future Unreal work must avoid hot-surface materials and damage volumes | Could overlap `SM_GIA_BloodAxeAnvilQuench_A01` if ownership boundaries blur |
| `SM_GIA_BloodAxeCharcoalHeaps_A01` | Package-ready charcoal heap set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeCharcoalHeaps_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal, pickup logic, or target selection | Static fuel residue only; no pickup, fuel count, cooking, crafting, economy, or interaction | Future DCC must keep broad heap silhouettes and avoid item-like chunks | Future Unreal work must avoid inventory, fuel, cooking, and resource components | Could become resource gameplay if staged like collectible fuel |
| `SM_GIA_BloodAxeCharcoalBins_A01` | Package-ready charcoal bin/tray set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeCharcoalBins_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal, workstation link, or target selection | Static tray dressing only; no workstation, inventory, resource, heat, or VFX behavior | Future DCC must keep bin forms crude and non-interactive | Future Unreal work must avoid workstation tags, pickup prompts, and heat states | Bin shape could imply usable forge supply without guardrails |
| `SM_GIA_BloodAxeFirewoodStacks_A01` | Package-ready Giant log stack set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeFirewoodStacks_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal, physics, or target selection | Static log dressing only; no gatherable, consumable, pickup, destructible, crafting, or inventory behavior | Future DCC must preserve Giant-scale log thickness and non-physics stack read | Future Unreal work must avoid per-log collision, resource components, and destructible states | Logs could become gatherable or destructible if item-like |
| `SM_GIA_BloodAxeFirewoodBundles_A01` | Package-ready tied firewood bundle set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeFirewoodBundles_A01/PRODUCTION_PACKAGE.md` | No source mesh, rope simulation, DCC, Unreal, or target selection | Static bundle dressing only; no rope physics, pickup, inventory, economy, resource, or interaction | Future DCC must keep ties as fixed forms and avoid simulated rope | Future Unreal work must avoid pickup, physics bodies, and resource data | Bundles could drift into inventory or physics work |
| `SM_GIA_BloodAxeScorchedDebris_A01` | Package-ready scorched debris row; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeScorchedDebris_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal, destructible setup, or target selection | Static non-graphic debris only; no destructible, cover, loot, resource, heat, damage, or startup behavior | Future DCC must keep burned beams and scraps broad, sparse, and non-graphic | Future Unreal work must avoid destructible components, cover tags, damage volumes, and startup placement | Debris could become cover or destructible if oversized or tagged |
| `SM_GIA_BloodAxeDebrisEdgeScatter_A01` | Package-ready edge scatter set; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeDebrisEdgeScatter_A01/PRODUCTION_PACKAGE.md` | No source mesh, DCC, Unreal, collision behavior, or target selection | Static edge dressing only; no nav, collision, interaction, economy, loot, or resource behavior | Future DCC must keep path-marker and barricade ownership separate | Future Unreal work must avoid nav blockers, collision correctness, and route-marker logic | Could be mistaken for path markers or barricade rubble |
| `SM_GIA_BloodAxeForgeClutterCluster_A01` | Package-ready composed forge clutter cluster; implementation blocked | `docs/assets/props/SM_GIA_BloodAxeForgeClutterCluster_A01/PRODUCTION_PACKAGE.md` | No composed source, DCC, Unreal, startup placement, or target selection | Static cluster only; no forge hearth, anvil/quench, scrap sorting, cooking, crafting, heat, or resource behavior | Future DCC must maintain enough negative space for Giant work-lane clearance | Future Unreal work must avoid workstation, heat, and startup placement claims | Could collapse sibling package ownership if too broad |

## Policy And Review Rows

| Document/package | Current state | Package path | Use | Non-authorization |
| --- | --- | --- | --- | --- |
| `KIT_GIA_BloodAxeAshSlagReviewRows_A01` | Review-only package-ready rows | `docs/assets/kits/KIT_GIA_BloodAxeAshSlagReviewRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping comparison rows for ash piles, ash drifts, slag lumps, slag spill strips, and charcoal heaps | No Unreal actor, validator, capture automation, startup placement, final visual signoff, DCC, Unreal Content, resource behavior, heat behavior, or implementation target |
| `KIT_GIA_BloodAxeFirewoodDebrisReviewRows_A01` | Review-only package-ready rows | `docs/assets/kits/KIT_GIA_BloodAxeFirewoodDebrisReviewRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping comparison rows for firewood stacks, firewood bundles, scorched beams, and debris-edge scatter | No Unreal placement, nav behavior, collision correctness, interaction behavior, resource behavior, DCC, Unreal Content, or implementation target |
| `DOC_GIA_BloodAxeAshSlagFirewoodScaleRows_A01` | Review-only package-ready rows | `docs/assets/kits/DOC_GIA_BloodAxeAshSlagFirewoodScaleRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping scale rows beside female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines | No scale-lock change, shipped marker approval, DCC, FBX, Unreal, validators, captures, startup placement, or implementation target |
| `DOC_GIA_BloodAxeAshSlagFirewoodMaterialRows_A01` | Policy-ready material package | `docs/assets/kits/DOC_GIA_BloodAxeAshSlagFirewoodMaterialRows_A01/PRODUCTION_PACKAGE.md` | Shared material discipline for ash, soot, slag, charcoal, scorched wood, blackened metal scraps, red cloth, and neutral/civilized Giant separation | No material instance, texture asset, material graph, VFX/audio, DCC, Unreal Content, startup placement, final color approval, or implementation target |
| `DOC_GIA_BloodAxeAshSlagFirewoodLODAndCollision_A01` | Policy-ready LOD/collision package | `docs/assets/kits/DOC_GIA_BloodAxeAshSlagFirewoodLODAndCollision_A01/PRODUCTION_PACKAGE.md` | LOD0-LOD3 and collision-limit policy for ash, slag, charcoal, firewood, scorched debris, review rows, and forge clutter clusters | No collision proxies, UCX meshes, nav blockers, gameplay volumes, validator files, Unreal Content, DCC, final approval, or implementation target |

## Source And Export Path Plan

The paths below are future planning references only. This matrix does not create folders, source files, exports, imports, validators, startup actors, or implementation targets.

| Family | Planned source root if later approved | Planned export root if later approved | Planned Unreal target root if later approved |
| --- | --- | --- | --- |
| Blood Axe ash, slag, charcoal, firewood, debris, and cluster static props | `SourceAssets/Blender/Kits/Giants/BloodAxeCamp/AshSlagFirewood/` | `SourceAssets/Exports/Kits/Giants/BloodAxeCamp/AshSlagFirewood/` | `/Game/Aerathea/Props/Giants/BloodAxeCamp/AshSlagFirewood/` |
| Ash/slag/firewood review and scale rows | Not selected | Not selected | Not applicable unless a later non-shipping review-scene task owns it |
| Shared ash/slag/firewood material policy | Not applicable from this matrix | Not applicable from this matrix | `/Game/Aerathea/Materials/Giants/BloodAxe/AshSlagFirewood/` only if a later material task owns it |

No first source folder, export folder, Unreal folder, material folder, review actor, validator, DCC target, package implementation target, or build order is selected here.

## DCC Readiness Preconditions

A later DCC lane must explicitly approve and own all of the following before source work begins:

- Exact source and export file scope.
- Chosen DCC target or targets; this matrix does not choose them.
- Per-child module split, mesh naming, pivot, orientation, centimeter scale proof, and scale comparison against the female 442 cm and male 470 cm Giant baselines.
- LOD0-LOD3 source expectations and reduction order from `DOC_GIA_BloodAxeAshSlagFirewoodLODAndCollision_A01`.
- Material-slot policy from `DOC_GIA_BloodAxeAshSlagFirewoodMaterialRows_A01`.
- Static-shape policy for ash piles, ash drifts, slag lumps, slag spill strips, charcoal heaps, charcoal bins, firewood stacks, firewood bundles, scorched debris, edge scatter, and forge clutter clusters.
- Culture-separation review against neutral/civilized Giant cave-town, warm hearth, and highland settlement forge language.
- Review artifact plan that remains non-final until separate visual approval exists.

The DCC lead must reject any direction that turns this kit into active resource nodes, loot piles, pickup objects, inventory items, fuel counters, cooking stations, crafting stations, economy objects, heat hazards, damage volumes, destructible debris, physics piles, rope simulation, VFX emitters, neutral Giant civic forge dressing, civilized Giant hearth clutter, or source-concept storage work.

## Unreal Readiness Preconditions

A later Unreal lane must explicitly approve and own all of the following before engine work begins:

- Import path, asset ownership, and exact file scope.
- Whether each row becomes a shipping static mesh, remains a docs-only package, or becomes a non-shipping review artifact.
- Import scale proof at 1 Unreal unit = 1 cm.
- LOD0-LOD3 presence for shipping static mesh candidates.
- Material instance and texture ownership, with no default emissive, smoke, sparks, ash drift, flame, heat shimmer, or active ember state unless a separate approved VFX/material task owns it.
- Collision disabled by default or a separately approved simple low blocking/query exception.
- Focused validation plan owned by the future Unreal/QA task.
- Any startup placement, review capture, marker pass, camera approval, final visual approval, or final package implementation approval in separately assigned tasks.

This matrix does not create Unreal Content, material instances, textures, Blueprints, sockets, collision proxies, validators, review actors, startup actors, VFX, audio, or runtime source.

## Validator Gaps And Future Checks

No validator is authored by this matrix. Future implementation lanes should add focused validators only when they own the affected tool paths.

| Future lane | Validator need |
| --- | --- |
| DCC source/export | Confirm source path, export path, FBX name, centimeter scale, dimensions, pivot, LOD0-LOD3 sources, material slot count, and no micro-detail geometry misuse. |
| Giant scale | Compare dimensions against female 442 cm / 14'6" and male 470 cm / 15'5" baselines. |
| Ash/slag/firewood import | Confirm Unreal path, LODs, material slots, simple/disabled collision policy, texture references, and no gatherable, heat, damage, resource, crafting, economy, pickup, nav, cover, destructible, VFX, or interaction logic. |
| Material validation | Confirm ash/soot/slag/charcoal/scorched wood material families, no default emissive, red accent restraint, roughness/metallic ranges, and no neutral/civilized Giant material drift. |
| Collision validation | Confirm collision disabled by default or simple low blocking/query only; no UCX, nav blockers, gameplay volumes, damage volumes, cover volumes, pickup volumes, interaction volumes, or collision correctness claims without a later lane. |
| Culture separation | Confirm Blood Axe docs do not claim default Giant culture, neutral cave-town identity, warm hearth forge language, blue-gray stoneworker motifs, or civilized Giant materials. |
| Source-storage | Confirm external concept art was not copied, embedded, moved, edited, inspected for visual approval, or committed. |
| Matrix maintenance | Confirm package-ready rows, policy rows, review rows, approval gates, and no-target-selected status remain aligned after docs/index integration. |

## Global Stop Gates

- Stop before selecting a first DCC, Unreal, source asset, gameplay, review-scene, validator, material, VFX/audio, startup, or implementation target from any row.
- Stop before source folder creation, DCC source, Blender files, meshes, sculpts, retopo, UVs, bakes, proof renders, LOD source files, collision proxies, UCX meshes, FBX exports, Unreal Content assets, material instances, texture assets, material graphs, import scripts, validators, runtime source, Blueprints, sockets, animation assets, review actors, startup placement, VFX/audio, or source concept movement.
- Stop before gatherable resources, resource nodes, firewood pickups, charcoal pickups, slag harvesting, loot, salvage, crafting, cooking, economy, inventory, vendors, workstation behavior, interaction prompts, heat damage, burn damage, damage volumes, destructible behavior, physics simulation, cover behavior, nav/pathfinding, encounter behavior, material-state behavior, or Hermes work.
- Stop before claiming collision correctness, runtime performance validation, camera approval, final silhouette approval, final ash/slag/firewood approval, final Blood Axe camp approval, or final visual approval.
- Stop if Blood Axe hostile raider identity starts replacing neutral/civilized Giant culture.
- Stop if any future row appears to require changing the Giant scale lock from female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline, or the approved Giant ranges.

## Matrix Maintenance Validation

Use these docs-only checks after edits to this matrix:

- Matrix completeness scan: confirm parent package, package-ready child rows, material policy, LOD/collision policy, review rows, and scale rows from `CHILD_ASSET_INTAKE.md` are represented.
- Package-path existence scan: confirm every path listed as package-ready exists.
- Approval-gate scan: confirm DCC, FBX, Unreal, runtime, validator creation, startup placement, final visual approval, first target selection, and implementation order approval remain blocked.
- Giant scale scan: confirm female 442 cm / 14'6", male 470 cm / 15'5", females 14-15 ft / 427-457 cm, and males 14'10"-16'0" / 452-488 cm remain present.
- Culture separation scan: confirm Blood Axe is described as a hostile Giant sub-faction and neutral/civilized Giant culture remains explicitly separate.
- Implementation-claim scan: confirm the matrix contains no claim that source, DCC, FBX, Unreal Content, runtime, validator, startup, visual approval, resource gameplay, heat/damage behavior, VFX/audio, or implementation work has started.
- Whitespace and diff validation: run `git diff --check -- docs/assets/kits/KIT_GIA_BloodAxeAshSlagFirewood_A01/IMPLEMENTATION_READINESS_MATRIX.md`.

## Quality Gate Checklist

- Matrix is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, material graph, VFX/audio asset, global index, backlog, bootstrap, child intake doc, source folder, image, unrelated package file, or production package.
- Ash/slag/firewood package rows are classified by readiness using the child intake and current package files.
- Material policy, LOD/collision policy, review-only rows, and scale rows are represented separately from buildable static-mesh candidates.
- Giant scale lock is explicit: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Package inventory does not imply build order, implementation order, DCC target selection, Unreal target selection, or final visual approval.
- Gatherable resource, heat/damage, VFX/audio, material-state behavior, crafting/economy, vendor behavior, interaction prompts, objective logic, nav/pathfinding, cover behavior, destructible behavior, AI/encounter behavior, physics, source asset creation, startup placement, and final approval are explicitly excluded.
- Source concept remains external and is not copied, moved, edited, embedded, inspected for visual approval, or committed.

## Non-Authorization Statement

This readiness matrix is a documentation artifact only. It authorizes no source folder, DCC target, implementation order, Blender work, mesh work, FBX export, Unreal Content import, material authoring, runtime source, validator creation, startup placement, final visual approval, final Blood Axe ash/slag/firewood approval, Hermes work, gatherable resource behavior, heat/damage behavior, VFX/audio, crafting/economy behavior, pickup/inventory behavior, or final Giant culture approval.
