# KIT_GIA_BloodAxeCaveRemnantCluster_A01 Implementation Readiness Matrix

## Scope

- Task id: `AET-MA-20260629-455`
- Package: `KIT_GIA_BloodAxeCaveRemnantCluster_A01`
- Source package: `docs/assets/kits/KIT_GIA_BloodAxeCaveRemnantCluster_A01/PRODUCTION_PACKAGE.md`
- Source intake: `docs/assets/kits/KIT_GIA_BloodAxeCaveRemnantCluster_A01/CHILD_ASSET_INTAKE.md`
- Closure source: `docs/assets/kits/KIT_GIA_BloodAxeCaveRemnantCluster_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`
- Status: docs-only implementation readiness classification.
- No-target-selected status: no DCC target, source asset target, Unreal target, runtime target, validator target, cave gameplay target, startup placement target, final approval target, or first build target is selected here.

This file classifies the cave-remnant package-ready, review, policy, and reference-only rows documented by child intake. It does not authorize source asset creation, DCC work, FBX export, Unreal Content, material instances, texture assets, validators, runtime source, source concept movement, Hermes files/config, route scripting, objective markers, nav/pathfinding, cave gameplay, VFX/audio, startup placement, final approvals, folder creation, folder selection, or a build sequence.

## Scale And Culture Lock

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe is a hostile Giant sub-faction only.
- Blood Axe hostile raider cave-remnant language must stay separate from neutral/civilized Giant culture.
- Neutral/civilized Giant culture remains tied to hidden highland settlements, skilled stonework, cave-town terraces, waterworks, warm hearth identity, blue-gray civic masonry, and restrained blue rune culture.

## Readiness Key

| State | Meaning |
| --- | --- |
| `package-ready; docs-only` | The production package exists and can be cited by a future separately approved lane. It is not build authorization. |
| `review-row; docs-only` | The package is a non-shipping comparison or review policy document. It must not become an Unreal actor, startup placement, capture target, or final approval artifact without new scope. |
| `policy-row; docs-only` | The package records material, LOD, or collision discipline only. It creates no assets, validators, material instances, or implementation files. |
| `reference-only` | The package can be used for restraint and continuity. It is not part of this package's implementation target set. |
| `blocked-for-build` | Any source, DCC, Unreal, runtime, validator, or final approval work is blocked until a separate owner, scope, target, and approval gate exist. |

## Package-Ready Row Matrix

| Row ID | State | Package path | Readiness blockers | Approval gates | DCC preconditions | Unreal preconditions | Validator gaps / residual risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SM_GIA_BloodAxeCaveRemnantCairn_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/props/SM_GIA_BloodAxeCaveRemnantCairn_A01/PRODUCTION_PACKAGE.md` | Build blocked by no source scope, no target selection, no mesh, no material assets, no validator. | Separate source task; DCC lead; Unreal lead; final visual/cave approval later. | Confirm low old cairn module split, centimeter scale, few-large-stones silhouette, pivot/orientation policy, static memory read. | Confirm import path only in a future task, LOD0-LOD3, 1 material target, disabled/simple collision policy. | Risk of reading as waypoint or route marker; future checks must protect low abandoned read and Giant scale. |
| `SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/props/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01/PRODUCTION_PACKAGE.md` | Build blocked by no source scope, no collapse state approval, no DCC, no FBX, no Unreal import. | Separate source task; no destructible or physics approval; final approval later. | Confirm slumped major-stone forms, cold ash contact, non-destructible static read, no pickup/interact affordance. | Confirm static mesh import scope later, collision disabled by default, LOD0-LOD3, no gameplay volumes. | Risk of being misread as destruction gameplay, cover, or traversal proof. |
| `SM_GIA_BloodAxeLowCaveStandingStone_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/props/SM_GIA_BloodAxeLowCaveStandingStone_A01/PRODUCTION_PACKAGE.md` | Build blocked by no source scope, no DCC target, no engine content, no scale validator. | Separate DCC/Unreal ownership; no objective marker or readable text approval. | Confirm short fractured slab remains below tall standing-stone identity and reads beside 442 cm / 470 cm baselines. | Confirm future static import scope, simple/disabled collision, LOD0-LOD3, no VFX/audio. | Risk of drifting into tall standing stone, cave gate, or objective frame. |
| `SM_GIA_BloodAxeBrokenLeaningCaveStone_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/props/SM_GIA_BloodAxeBrokenLeaningCaveStone_A01/PRODUCTION_PACKAGE.md` | Build blocked by no source task, no lean proof, no cave compatibility proof, no collision proof. | Separate source lane; no puzzle, destructible, traversal, or cave layout approval. | Confirm broad chipped planes, static lean, heavy mud contact, no doorway spacing. | Confirm no nav blocker, no gameplay volume, no collision correctness claim, LOD0-LOD3 only after future scope. | Risk of being promoted to puzzle state, blocker, cover, or traversal gate. |
| `SM_GIA_BloodAxeOldCaveClothWrap_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/props/SM_GIA_BloodAxeOldCaveClothWrap_A01/PRODUCTION_PACKAGE.md` | Build blocked by no cloth asset, no material, no texture, no animation/physics approval. | Separate source task; cloth remains fixed; no UI/objective marker approval. | Confirm broad static oxide red wrap, Giant-hand scale, restrained cloth coverage, no simulation target. | Confirm no cloth physics, no material pulse, no VFX/audio, no collision on cloth. | Risk of becoming a flag, quest pointer, UI marker, or simulated banner. |
| `SM_GIA_BloodAxeDrapedCaveClothScrap_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/props/SM_GIA_BloodAxeDrapedCaveClothScrap_A01/PRODUCTION_PACKAGE.md` | Build blocked by no source scope, no material assets, no final visual approval. | Separate source/DCC task; static-only cloth approval; final approval later. | Confirm draped fixed scrap with broad folds and sparse fray, not readable signage. | Confirm no animation, no collision, no interactive affordance, no startup placement. | Risk of overlarge red read becoming objective cue or route sign. |
| `SM_GIA_BloodAxeCaveAshMudBase_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/props/SM_GIA_BloodAxeCaveAshMudBase_A01/PRODUCTION_PACKAGE.md` | Build blocked by no ground asset, no terrain integration proof, no validator, no Unreal import. | Separate source task; no trigger, aura, damage, route, objective, or collision approval. | Confirm irregular non-circular ash/mud base, cold residue, no path-width or terrain proof. | Confirm collision disabled, no decal gameplay, no trigger volume, no nav/pathfinding behavior. | Risk of circular footprint reading as trigger area, aura, or objective zone. |
| `SM_GIA_BloodAxeColdCaveFireScar_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/props/SM_GIA_BloodAxeColdCaveFireScar_A01/PRODUCTION_PACKAGE.md` | Build blocked by no source scope, no active fire/VFX approval, no material state work. | Separate source task; fire scar remains cold and static; final approval later. | Confirm subtle old fire-scar and mud lip, no active flame, smoke, pickup, or resource read. | Confirm no VFX/audio, no damage volume, no material animation, no interaction. | Risk of being misread as active fire, hazard, loot spot, or resource node. |
| `KIT_GIA_BloodAxeCaveRemnantThreshold_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/kits/KIT_GIA_BloodAxeCaveRemnantThreshold_A01/PRODUCTION_PACKAGE.md` | Build blocked by no layout target, no source scope, no cave marker approval, no implementation target. | Separate kit source task; no cave entrance gameplay marker, route, spawn, or final cave approval. | Confirm compact asymmetric cairn/low stone/cloth/ash composition, visual threshold only. | Confirm no content path until future task, no nav/pathfinding, no collision guarantee, no startup placement. | Risk of being read as cave entrance gate, encounter lane, route device, or spawn marker. |
| `KIT_GIA_BloodAxeCaveBrokenSlabThreshold_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/kits/KIT_GIA_BloodAxeCaveBrokenSlabThreshold_A01/PRODUCTION_PACKAGE.md` | Build blocked by no source scope, no traversal proof, no route validation, no Unreal target. | Separate source task; no gate/objective/interaction approval. | Confirm broken slab pair remains abandoned static remnant, not doorway or path rule. | Confirm disabled/simple collision policy only if later scoped, LOD0-LOD3, no gameplay volumes. | Risk of becoming gate behavior, traversal proof, objective frame, or blocker set. |
| `KIT_GIA_BloodAxeHalfBuriedCaveStoneCluster_A01` | `package-ready; docs-only`; `blocked-for-build` | `docs/assets/kits/KIT_GIA_BloodAxeHalfBuriedCaveStoneCluster_A01/PRODUCTION_PACKAGE.md` | Build blocked by no source asset scope, no cave compatibility proof, no first target selection. | Separate source and Unreal ownership; no cover, nav blocker, encounter, or damage/aura approval. | Confirm half-buried static marker stones, mud-sunk cloth, age/readability beat only. | Confirm no collision correctness claim, no nav/pathfinding, no runtime behavior, no startup placement. | Risk of becoming cover, puzzle boundary, route blocker, or final layout cue. |

## Review / Policy Rows

| Row ID | State | Package path | Readiness blockers | Approval gates | DCC preconditions | Unreal preconditions | Validator gaps / residual risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01` | `review-row; docs-only`; `blocked-for-build` | `docs/assets/kits/DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping comparison rows only; no row geometry, capture, validator, or approval artifact exists. | Separate review-board scope before any visual sheet; final visual/cave approval later. | If a later docs-only board exists, keep rows simple and non-shipping; no source target selection. | No Unreal actor, review actor, capture automation, marker pass, startup placement, or content path. | Risk of review rows being mistaken for final silhouette approval or production item choice. |
| `DOC_GIA_BloodAxeCaveRemnantClusterScaleRows_A01` | `review-row; docs-only`; `blocked-for-build` | `docs/assets/kits/DOC_GIA_BloodAxeCaveRemnantClusterScaleRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping scale rows only; no scale-lock change, validator, capture, or shipped marker approval. | Scale remains owned by `SK_GIA_Base_A01`; separate approval needed for any visualization. | Use female 442 cm / male 470 cm baselines only as review references; no source scale change. | No Unreal scale proof, actor, import, validator, or startup placement from this row. | Risk of scale rows being mistaken for collision, camera, terrain, or final marker approval. |
| `DOC_GIA_BloodAxeCaveRemnantClusterMaterialRows_A01` | `review-row; docs-only`; `blocked-for-build` | `docs/assets/kits/DOC_GIA_BloodAxeCaveRemnantClusterMaterialRows_A01/PRODUCTION_PACKAGE.md` | Non-shipping material restraint rows only; no material instances, textures, graphs, or VFX. | Separate material authoring scope needed before any asset; no final color approval here. | If a future board exists, use broad material swatches and excluded neutral/civilized Giant comparisons only. | No material instance, texture asset, shader graph, VFX/audio, or content import. | Risk of material rows becoming final color approval, emissive approval, or neutral/civilized Giant drift. |
| `DOC_GIA_BloodAxeCaveRemnantClusterMaterialDiscipline_A01` | `policy-row; docs-only`; `blocked-for-build` | `docs/assets/kits/DOC_GIA_BloodAxeCaveRemnantClusterMaterialDiscipline_A01/PRODUCTION_PACKAGE.md` | Material policy only; no authoring, no texture set, no material graph, no implementation target. | Separate consuming package must own material creation and final color review. | Future source work must keep broad stone/soot/ash/mud/cloth material families and no default emissive. | Future Unreal work must keep material slots low and default emissive off unless separately scoped. | Risk of material discipline being treated as material graph approval or final Blood Axe culture approval. |
| `DOC_GIA_BloodAxeCaveRemnantClusterLODAndCollision_A01` | `policy-row; docs-only`; `blocked-for-build` | `docs/assets/kits/DOC_GIA_BloodAxeCaveRemnantClusterLODAndCollision_A01/PRODUCTION_PACKAGE.md` | LOD/collision policy only; no LOD source, UCX, collision proxies, validators, or Unreal settings. | Separate mesh package must own source LODs and any collision exception. | Future DCC work must define LOD0-LOD3 source and collision-source limits in its own task. | Future Unreal work must validate LOD presence and disabled/simple collision only under separate scope. | Risk of policy being mistaken for collision correctness, pathing validity, or runtime performance validation. |

## Reference-Only Rows

| Reference ID | State | Package path | Use allowed | Guardrail |
| --- | --- | --- | --- | --- |
| `SM_GIA_BloodAxeRitualCairnGuidepost_A01` | `reference-only` | `docs/assets/props/SM_GIA_BloodAxeRitualCairnGuidepost_A01/PRODUCTION_PACKAGE.md` | Restraint reference for few-large-stones construction, oxide red cloth restraint, static memory read, and no route/objective behavior. | Not an implementation target for this matrix; do not promote it into DCC, FBX, Unreal, startup placement, validator, or final approval work from here. |
| `SM_GIA_BloodAxeStandingStone_A01` | `reference-only` | `docs/assets/props/SM_GIA_BloodAxeStandingStone_A01/PRODUCTION_PACKAGE.md` | Restraint reference for rough slab silhouette, Giant scale, base contact, and Blood Axe/neutral-civilized Giant separation. | Not an implementation target for this matrix; low cave standing stones remain shorter and cluster-bound. |

## Future Path Plan

The only future path plan authorized by this file is a planning-reference map to already documented package paths. It does not create, select, reserve, or recommend any source folder, DCC folder, FBX folder, `/Game/` content folder, runtime path, validator path, startup placement path, Hermes path, or first build target.

- Parent package docs remain under `docs/assets/kits/KIT_GIA_BloodAxeCaveRemnantCluster_A01/`.
- Package-ready prop rows remain documented under their existing `docs/assets/props/.../PRODUCTION_PACKAGE.md` paths.
- Package-ready kit, review, and policy rows remain documented under their existing `docs/assets/kits/.../PRODUCTION_PACKAGE.md` paths.
- Reference-only packages remain citation sources only.
- Any future source, DCC, Unreal, validator, review-capture, or approval work requires a new task with its own file scope and target selection.

## DCC Readiness Preconditions

Before any later DCC work starts, a separate lead-approved task must define:

- Owner, writable file scope, and allowed output files.
- Source storage policy without relying on this matrix as folder authorization.
- Exact future target or targets, selected outside this matrix.
- Module split, naming policy, pivot convention, orientation convention, and centimeter scale proof.
- Blockout acceptance standard for static abandoned cave-edge memory dressing.
- Material-read standard for rough highland stone, soot, cold ash, trampled mud, cave grit, oxide red cloth, rope, rawhide, sparse blackened iron, old horn, and dull bone.
- Culture separation standard that keeps Blood Axe hostile raider dressing distinct from neutral/civilized Giant culture.
- LOD0-LOD3 source expectations and collision-source limits.
- Review artifact plan that remains non-final until a separate visual approval task exists.

Reject any DCC direction that turns the cave-remnant cluster into a functional cave entrance, route device, objective frame, encounter lane, spawn marker, cover set, damage/aura field, puzzle object, readable sign, neutral Giant civic marker, or civilized Giant settlement threshold.

## Unreal Readiness Preconditions

Before any later Unreal work starts, a separate lead-approved task must define:

- Unreal file scope, import ownership, and content path.
- Whether a row becomes a shipping static mesh, non-shipping review actor, or remains documentation-only.
- Import scale proof preserving female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines.
- Material slot limits, shared texture policy, and no-baseline-emissive behavior.
- Disabled-by-default collision policy or a separately approved simple-contact exception for large stone bodies.
- LOD0-LOD3 presence and silhouette-protection expectations.
- Validator ownership and exact validator checks.
- Any startup placement, review capture, marker pass, final visual approval, final cave approval, and final Blood Axe approval as separate tasks.

This matrix names no Unreal import target and creates no material instances, textures, Blueprints, review actors, validators, runtime source, or startup placement.

## Validator Gaps And Future Checks

Current validator status: none created or authorized by this matrix.

Future separately scoped validation should check:

- File-scope compliance against the assigned task.
- Presence of LOD0, LOD1, LOD2, and LOD3 on any future shipping static mesh.
- Disabled-by-default collision on cloth, ash, mud, soot, cave grit, small accents, review rows, scale rows, and material rows.
- Simple collision only for separately approved major stone bodies.
- Female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale references preserved.
- Approved Giant ranges preserved: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe hostile Giant sub-faction language kept separate from neutral/civilized Giant culture.
- No default emissive, VFX/audio, animated material state, objective marker, UI cue, route helper, nav/pathfinding behavior, cave gameplay, or trigger behavior.
- No claim of collision correctness, cave compatibility, terrain integration, runtime performance validation, final visual approval, final cave approval, or final Giant culture approval.

Residual risks:

- Inventory tables could be mistaken for a build sequence unless the no-target-selected state stays visible.
- Threshold kits could read as functional cave entrances or encounter lanes if future layouts become symmetrical.
- Ash/mud and cold fire-scar rows could read as trigger zones, damage fields, or objective rings if future material direction adds circles, glow, particles, or clean edge graphics.
- Cloth rows could become UI-like faction markers or simulated banners if future direction increases size or motion.
- Broken and half-buried stone rows could become blockers, cover, puzzle boundaries, or traversal claims without gameplay approval.
- Blood Axe hostile raider materials could drift into default Giant culture if neutral/civilized Giant separation is not rechecked.

## Global Stop Gates

Stop before source asset creation, DCC source, Blender files, meshes, sculpts, retopo, UVs, bakes, proof renders, LOD source, collision proxies, UCX meshes, FBX export, Unreal Content, material instances, texture assets, material graphs, import scripts, validators, runtime source, Blueprints, sockets, animation assets, VFX/audio, review actors, startup placement, source concept movement, Hermes files/config, final visual approval, final cave approval, final Blood Axe approval, final Giant culture approval, or any first build target.

Stop before cave gameplay, cave entrance gameplay marker behavior, route scripting, nav/pathfinding, path-width proof, traversal proof, encounter lanes, spawn markers, patrol logic, AI spaces, cover rules, objective markers, quest/UI markers, readable signage, interaction behavior, pickup/loot behavior, resource/crafting/economy behavior, destructible behavior, physics behavior, damage/aura behavior, trigger volumes, damage volumes, aura volumes, objective volumes, active fire, smoke, glow, particles, cloth simulation, wind animation, material pulses, or audio cues.

Stop if a row appears to require changing the validated Giant scale lock or the approved Giant ranges.

Stop if Blood Axe hostile Giant sub-faction language starts replacing neutral/civilized Giant culture.

## Maintenance Validation

Maintain this matrix only as a docs-only classification file. Future maintenance should:

- Keep the source package, child intake, and closure note as the source of truth.
- Recheck all package paths before citing them as existing.
- Recheck all 16 package-ready/review/policy IDs after child-intake edits.
- Keep reference-only rows out of implementation target lists.
- Keep no-target-selected and blocked-for-build language visible.
- Run a trailing whitespace scan on this file.
- Run `git diff --check -- docs/assets/kits/KIT_GIA_BloodAxeCaveRemnantCluster_A01/IMPLEMENTATION_READINESS_MATRIX.md`.

## Quality Checklist

- [x] Scope, source package/intake, task id, and no-target-selected status are present.
- [x] Female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock is present.
- [x] Approved Giant ranges are present.
- [x] Blood Axe hostile Giant sub-faction language is separated from neutral/civilized Giant culture.
- [x] Readiness key is present.
- [x] All 16 package-ready/review/policy IDs from child intake are classified.
- [x] `SM_GIA_BloodAxeRitualCairnGuidepost_A01` and `SM_GIA_BloodAxeStandingStone_A01` are reference-only rows, not implementation targets.
- [x] Package-ready row table includes state, package path, readiness blockers, approval gates, DCC preconditions, Unreal preconditions, and validator gaps/residual risks.
- [x] Future path plan is planning-reference only and creates/selects no folder.
- [x] DCC and Unreal readiness preconditions are documented as future gated requirements.
- [x] Validator gaps and future checks are documented without creating validators.
- [x] Global stop gates and maintenance validation are present.
- [x] This file authorizes no Content, SourceAssets, Tools/DCC, Tools/Unreal, runtime source, source concept movement, Hermes files/config, DCC target selection, build target selection, startup placement, validators, material instances, VFX/audio, cave gameplay, route scripting, objective markers, nav/pathfinding, or final approvals.

## Non-Authorization Statement

This readiness matrix is documentation only. It authorizes no source asset, source folder, DCC target, DCC file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal import, Unreal Content asset, material instance, texture asset, material graph, Blueprint, runtime source, validator, review actor, startup placement, source concept movement, Hermes work, cave gameplay, route scripting, objective marker, nav/pathfinding, VFX/audio, final visual approval, final cave approval, final Blood Axe approval, final Giant culture approval, or build target selection.
