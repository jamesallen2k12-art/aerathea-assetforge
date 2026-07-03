# KIT_GIA_BloodAxeLowThresholdCairns_A01 Implementation Readiness Matrix

## Scope

- Task: `AET-MA-20260629-475`
- Package: `KIT_GIA_BloodAxeLowThresholdCairns_A01`
- Source docs: `PRODUCTION_PACKAGE.md` and `CHILD_ASSET_INTAKE.md`
- Matrix status: docs-only implementation readiness review
- Output status: no source asset, DCC, FBX, Unreal Content, material instance, texture, validator, runtime file, startup placement, external concept copy, final approval, or implementation target is created or selected by this matrix.

This matrix summarizes readiness inputs for the Blood Axe low-threshold cairn kit without advancing any child row into implementation. It preserves the intake rows as unordered candidates or references only.

## Scale And Culture Locks

- Giant scale lock remains female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline.
- Approved Giant ranges remain females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction only.
- Blood Axe cairns may use rough highland stone, soot, cold ash, trampled mud, cave grit, rope, rawhide, oxide red cloth, sparse blackened iron, old horn, and dull bone.
- Blood Axe low-threshold cairns must not become the default identity for neutral/civilized Giant cave towns, hidden settlements, monumental masonry, terrace systems, waterworks, hearth-warm interiors, blue-gray civic stonework, peaceful highland wayfinding, carved civic ornament, or restrained blue-rune culture.

## Required Stop Gates

- No-gate-behavior guardrail: stop before defining gates, locked passages, open/closed states, destructible entrances, objective gates, trigger gates, or cave access behavior.
- No-route guardrail: stop before route validation, path-width rules, nav/pathfinding, encounter lanes, quest pointers, objective markers, readable signage, UI arrows, spawn logic, patrol logic, AI spaces, cover rules, or trap behavior.
- No-build guardrail: stop before source folders, DCC files, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content, material instance, texture asset, material graph, import script, runtime source, Blueprint, socket, animation asset, VFX/audio, startup placement, or external concept movement.
- No-collision-guarantee guardrail: stop before claiming collision correctness, cave compatibility, traversal clearance, camera clearance, terrain integration, nav blocking, simple collision validity, UCX validity, runtime performance validation, or collision guarantee.
- No-cloth-simulation guardrail: stop before cloth simulation, flag animation, wind sway, dangling physics, material pulse, animated cloth material state, or physics asset behavior.
- No-target-selected guardrail: stop before selecting a first DCC target, first Unreal target, first package implementation target, source folder, runtime behavior, final cave approval, final Blood Axe ritual approval, final Giant culture approval, final visual approval, or implementation order.

## Package Inventory

| Intake row | Proposed future package or asset | Intake status | Matrix readiness | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeLowThresholdCairns_A01#PairedPrimary_A01` | `KIT_GIA_BloodAxeLowThresholdCairnPair_Primary_A01` | package-ready | Docs package input ready only | Primary two-cairn composition is documented for static visual threshold rhythm. No first DCC or Unreal target is selected. |
| `BloodAxeLowThresholdCairns_A01#AsymmetricPair_A01` | `KIT_GIA_BloodAxeLowThresholdCairnPair_Asymmetric_A01` | package-ready | Docs package input ready only | Offset wide/low and taller companion rhythm is documented without route clearance, objective framing, collision promise, or target selection. |
| `BloodAxeLowThresholdCairns_A01#AshBasePair_A01` | `KIT_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01` | package-ready | Docs package input ready only | Cold ash, soot, trampled mud, and cave grit grounding is material read only. No gameplay decal, damage field, aura, or trigger area is approved. |
| `BloodAxeLowThresholdCairns_A01#CollapsedPair_A01` | `KIT_GIA_BloodAxeLowThresholdCairnPair_Collapsed_A01` | package-ready | Docs package input ready only | Partly fallen large-stone read is documented as static abandoned remnant only. No destruction, physics, traversal proof, or implementation target is approved. |
| `BloodAxeLowThresholdCairns_A01#RedClothTiedPair_A01` | `KIT_GIA_BloodAxeLowThresholdCairnPair_RedClothTied_A01` | package-ready | Docs package input ready only | Broad oxide red cloth ties are documented as static Blood Axe accents only. No cloth simulation, flag animation, UI marker, material pulse, VFX, or audio is approved. |
| `BloodAxeLowThresholdCairns_A01#SpacingReviewRows_A01` | `DOC_GIA_BloodAxeLowThresholdCairnSpacingReview_A01` | package-ready | Docs reference input ready only | Non-shipping rows compare spacing, height variance, red cloth density, and Giant scale readability. No actor, capture, startup placement, validator, or final visual approval is selected. |
| `BloodAxeLowThresholdCairns_A01#MaterialDisciplineReference_A01` | `DOC_GIA_BloodAxeLowThresholdCairnMaterialDiscipline_A01` | package-ready | Docs reference input ready only | Material discipline is documented for restraint and cultural separation. No material instance, texture, material graph, final color approval, or implementation target is created. |
| `BloodAxeLowThresholdCairns_A01#LODCollisionPlanningReference_A01` | `DOC_GIA_BloodAxeLowThresholdCairnLODAndCollision_A01` | package-ready | Docs reference input ready only | LOD0-LOD3 reduction order and disabled/simple collision intent are documented. No collision proxy, UCX mesh, validator, Unreal Content, runtime implementation, or collision guarantee is approved. |
| `BloodAxeLowThresholdCairns_A01#SingleLowCairnContext_A01` | `SM_GIA_BloodAxeLowThresholdCairn_A01` | reference-only | Context reference only | Single low cairn context can inform pair consistency later, but this matrix does not select it as a source asset, DCC target, FBX target, Unreal target, startup target, final approval target, or first implementation target. |

## Readiness Matrix

| Intake row | DCC preconditions before any future source work | Unreal preconditions before any future import work | Validator gaps | Current stop state |
| --- | --- | --- | --- | --- |
| `BloodAxeLowThresholdCairns_A01#PairedPrimary_A01` | Lead must open a separate DCC/source task, select this row explicitly, confirm stone scale against female 442 cm and male 470 cm Giants, and keep cloth optional and static. | Lead must open a separate Unreal task after DCC output exists, confirm naming, pivot, material slots, LOD0-LOD3, and disabled/simple collision intent. | No DCC mesh, proof render, LOD source, collision proxy, FBX, Unreal import, material, texture, or visual validator exists. | Hold under No-build guardrail and No-target-selected guardrail. |
| `BloodAxeLowThresholdCairns_A01#AsymmetricPair_A01` | Lead must separately approve asymmetric composition limits so it avoids formal doorway language and remains a visual rhythm. | Unreal owner must wait for approved source output and avoid route, passage, or gate setup. | No asymmetry density validator, route-safety validator, import validator, or collision validator exists. | Hold under No-route guardrail and No-target-selected guardrail. |
| `BloodAxeLowThresholdCairns_A01#AshBasePair_A01` | Lead must separately define whether ash and mud are geometry, decal-like texture detail, or shared material treatment before source work starts. | Unreal owner must not create gameplay decals, trigger areas, damage fields, aura volumes, or nav-affecting surfaces from the ash base. | No ash/material density validator, terrain integration validator, collision validator, or runtime validator exists. | Hold under No-route guardrail, No-build guardrail, and No-collision-guarantee guardrail. |
| `BloodAxeLowThresholdCairns_A01#CollapsedPair_A01` | Lead must separately approve static collapsed silhouette and confirm no destruction, physics, pickup, or traversal proof is implied. | Unreal owner must wait for explicit static mesh import scope and must not add destructible behavior, physics setup, or gameplay collision claims. | No collapse-read validator, physics absence validator, import validator, or collision correctness validator exists. | Hold under No-build guardrail, No-collision-guarantee guardrail, and No-target-selected guardrail. |
| `BloodAxeLowThresholdCairns_A01#RedClothTiedPair_A01` | Lead must separately approve cloth as sculpted static geometry or texture treatment only, with broad folds and no simulation. | Unreal owner must not add cloth physics, flag components, material pulses, VFX, audio, or objective-readable cloth states. | No cloth-static validator, material pulse scan, import validator, or runtime behavior validator exists. | Hold under No-cloth-simulation guardrail, No-build guardrail, and No-target-selected guardrail. |
| `BloodAxeLowThresholdCairns_A01#SpacingReviewRows_A01` | DCC work is not a default next step. If later opened, the lead must define non-shipping review-row purpose, scale markers, and review-only geometry limits. | Unreal work is not a default next step. If later opened, rows must remain non-shipping and cannot become actors, startup placement, route validators, or final visual approval. | No review-row validator, marker validation, capture validation, camera approval, or startup validation exists. | Hold under No-route guardrail, No-build guardrail, and No-target-selected guardrail. |
| `BloodAxeLowThresholdCairns_A01#MaterialDisciplineReference_A01` | DCC source work must wait for a separately selected child asset and must inherit material restraint from this reference. | Unreal material work must wait for a separate material task and must not create material instances, textures, graphs, emissive states, or final color approval here. | No material instance validator, texture audit, graph audit, emissive absence validator, or final color validator exists. | Hold under No-build guardrail and No-target-selected guardrail. |
| `BloodAxeLowThresholdCairns_A01#LODCollisionPlanningReference_A01` | DCC source work must wait for a selected mesh target and then produce LOD0-LOD3 plus any separately approved simple collision proxy. | Unreal collision setup must wait for source output and must not claim collision correctness, route clearance, cave compatibility, or nav behavior from this reference. | No LOD presence validator, LOD ratio validator, UCX validator, collision correctness validator, or runtime performance validator exists. | Hold under No-collision-guarantee guardrail, No-build guardrail, and No-target-selected guardrail. |
| `BloodAxeLowThresholdCairns_A01#SingleLowCairnContext_A01` | Context only. Any source reuse or new source creation requires a separate task that selects a concrete asset and resolves ownership. | Context only. Any Unreal reuse or import requires a separate task with approved asset identity, folder path, collision policy, material policy, and validation scope. | No ownership validator, source availability validator, import validator, or pair-consistency validator exists in this matrix. | Hold under No-build guardrail and No-target-selected guardrail. |

## DCC Preconditions

Before any future DCC work may start, a separate authorized task must:

- Select exactly one target row or explicitly define a batch scope without using this matrix as implementation order.
- Confirm the task may create source folders or source files.
- Confirm the Giant scale lock: female 442 cm / 14'6", male 470 cm / 15'5", approved female range 14-15 ft / 427-457 cm, and approved male range 14'10"-16'0" / 452-488 cm.
- Confirm Blood Axe hostile raider language remains separate from neutral/civilized Giant culture.
- Define mesh ownership, naming, pivots, orientation, LOD0-LOD3 targets, material slot limits, UV and bake expectations, and proof-render expectations.
- Confirm collision proxy scope separately and avoid collision guarantee language.
- Confirm cloth remains static unless a separately named non-baseline variant explicitly authorizes animation or simulation.

## Unreal Preconditions

Before any future Unreal work may start, a separate authorized task must:

- Provide approved DCC/FBX/source output or explicitly authorize an Unreal-only docs/import step.
- Select a concrete Unreal target without using this matrix as priority order.
- Define game content folder path, asset naming, import settings, material instance scope, texture list, LOD import policy, collision policy, and validation commands.
- Confirm no gate behavior, route validation, nav/pathfinding, encounter lane, quest pointer, objective marker, interaction behavior, destructible behavior, cloth simulation, VFX/audio, runtime behavior, or startup placement is implied unless separately authorized.
- Confirm final cave approval and final visual approval remain outside this matrix.

## Validator Gaps

- Readiness matrix scan: this file can be scanned for all nine intake rows, required guardrail labels, Giant scale lock, and Blood Axe/civilized Giant separation.
- Package-ready row scan: source intake states are represented here, but no child package content is revalidated by this matrix.
- No-target-selected scan: required because the matrix intentionally leaves all rows unordered and targetless.
- DCC gap: no source file, mesh, UV, bake, proof render, LOD source, collision proxy, or DCC validator exists from this task.
- Unreal gap: no FBX, Unreal Content, material instance, texture, import script, Blueprint, socket, review actor, startup placement, or Unreal validator exists from this task.
- Runtime gap: no runtime source, gate behavior, route validation, nav/pathfinding, encounter lane, interaction target, quest pointer, destructible behavior, cloth simulation, VFX/audio, damage/aura behavior, pickup, loot, resource, crafting, economy, spawn, or patrol validator exists from this task.
- Collision gap: no collision proxy, UCX mesh, collision setup, collision correctness scan, traversal clearance scan, cave compatibility scan, or nav blocker scan exists from this task.
- Approval gap: no final cave approval, final Blood Axe ritual approval, final Giant culture approval, final visual approval, final color approval, or marker/camera approval exists from this task.

## Residual Approval Gates

- Lead Producer / Orchestrator must choose whether any row advances and must do so in a separate task.
- Production Package must not infer implementation order from this matrix.
- DCC owner must not begin source work until a separate DCC scope is opened.
- Unreal owner must not begin import or content work until a separate Unreal scope is opened.
- QA / Validation must define validators after source or content exists; this matrix does not create validator files.
- Docs / Index owner must handle any global index, backlog, bootstrap, or task-board updates separately.
- Final cave approval, final Blood Axe ritual approval, final Giant culture approval, and final visual approval remain unresolved.

## Quality Gate Checklist

- All nine intake rows are represented.
- The paired primary, asymmetric pair, ash-base pair, collapsed pair, red-cloth tied pair, spacing review row, material discipline reference, LOD/collision planning reference, and single low cairn context reference are covered.
- Giant scale lock is preserved exactly: female 442 cm / 14'6", male 470 cm / 15'5", female range 14-15 ft / 427-457 cm, and male range 14'10"-16'0" / 452-488 cm.
- Blood Axe hostile Giant separation from neutral/civilized Giant culture is explicit.
- No-gate-behavior guardrail, No-route guardrail, No-build guardrail, No-collision-guarantee guardrail, No-cloth-simulation guardrail, and No-target-selected guardrail are explicit.
- No first DCC target, first Unreal target, implementation order, source folder, runtime behavior, final cave approval, or final visual approval is selected.
- DCC/Unreal preconditions, validator gaps, package inventory, and residual approval gates are included.
- The file is docs-only and creates no implementation asset.
