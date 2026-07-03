# KIT_GIA_BloodAxeRitualBannerPoles_A01 Implementation Readiness Matrix

## Package Inputs

- Task ID: `AET-MA-20260629-483`
- Package: `KIT_GIA_BloodAxeRitualBannerPoles_A01`
- Source package: `docs/assets/kits/KIT_GIA_BloodAxeRitualBannerPoles_A01/PRODUCTION_PACKAGE.md`
- Source intake: `docs/assets/kits/KIT_GIA_BloodAxeRitualBannerPoles_A01/CHILD_ASSET_INTAKE.md`
- Matrix status: docs-only implementation readiness review.
- Output status: no source asset, DCC, FBX, Unreal Content, material instance, texture, validator, runtime file, startup placement, source concept movement, final visual approval, cloth physics, animation, faction buff behavior, morale/AI behavior, aura/VFX/audio behavior, interaction behavior, quest marker behavior, readable text, runtime behavior, or implementation target is created or selected by this matrix.

This matrix summarizes readiness inputs for the Blood Axe ritual banner pole kit without advancing any child or context row into implementation. Rows are unordered and remain package inputs, planning references, or non-shipping review references only.

## Scale And Culture Locks

- Female Giant baseline: female 442 cm / 14'6".
- Male Giant baseline: male 470 cm / 15'5".
- Approved female Giant range: females 14-15 ft / 427-457 cm.
- Approved male Giant range: males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction only.
- Blood Axe hostile raider language must remain separated from neutral/civilized Giant culture.
- Blood Axe ritual banner poles may use rough scorched timber, oxide red cloth, thick rope, hide lashings, stone weights, soot, ash, mud, sparse blackened iron, and sparse non-graphic horn markers.
- Blood Axe ritual banner poles must not use neutral Giant cave-town masonry, refined highland clan banners, warm hearth settlement ornament, terrace or waterwork motifs, civic stoneworker symbols, restrained blue runes, polished neutral/civilized Giant culture, or default emissive signal language.

## Readiness Status

- Parent package status: docs-only production package and child intake exist.
- Current readiness: package inputs are ready for later lead review only; implementation remains blocked.
- Review rows: non-shipping planning references only.
- Material and LOD/collision rows: policy references only; not build targets.
- No row selects a first DCC target, first Unreal target, first package implementation target, implementation order, source folder, final visual approval, final Blood Axe ritual approval, final Giant culture approval, cloth behavior, animation behavior, gameplay behavior, VFX/audio behavior, readable text, runtime behavior, or package closure target.

Required readiness guardrails:

- No-cloth-physics guardrail: stop before cloth physics, cloth simulation, vertex wind, flag components, dangling cloth motion, cloth collision, destructible cloth, or physics asset behavior.
- No-animation guardrail: stop before banner waving, skeletal animation, vertex animation, material animation, moving ritual states, collapse states, runtime motion, or animated review rows.
- No-build guardrail: stop before source folders, DCC files, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content, material instance, texture asset, material graph, import script, validator, runtime source, Blueprint, socket, animation asset, VFX/audio, startup placement, or external source concept movement.
- No-gameplay-buff guardrail: stop before faction buff behavior, morale/AI behavior, aura gameplay, interaction behavior, quest marker behavior, objective logic, encounter scripting, nav/pathfinding, trigger volumes, loot/resource/crafting/economy behavior, damage/destructible/pickup behavior, signal behavior, readable text, or runtime gameplay.
- No-vfx-audio guardrail: stop before aura/VFX/audio behavior, particles, glow effects, dynamic lights, sound cues, ambient emitters, signal pulses, ritual audio, or material-driven VFX states.
- No-target-selected guardrail: stop before selecting a first DCC target, first Unreal target, first package implementation target, implementation order, source folder, Content path, import path, final visual approval target, final Blood Axe ritual approval target, final Giant culture approval target, validator target, or package closure target.

## Package Inventory

| Child/context ID | Intake type | Proposed future asset or package | Intake status | Matrix readiness |
| --- | --- | --- | --- | --- |
| `BloodAxeRitualStones.png#RitualBannerPole_Tall_A01` | Tall pole | `SM_GIA_BloodAxeRitualBannerPole_Tall_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#RitualBannerPole_Secondary_A01` | Secondary pole | `SM_GIA_BloodAxeRitualBannerPole_Secondary_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#RitualPole_Pair_A01` | Paired poles | `SM_GIA_BloodAxeRitualPolePair_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#RitualPole_Cluster_A01` | Pole cluster | `SM_GIA_BloodAxeRitualPoleCluster_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#TiedCloth_Strips_A01` | Tied cloth strips | `SM_GIA_BloodAxeRitualClothStripSet_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#TiedCloth_KnotWraps_A01` | Cloth knot wraps | `SM_GIA_BloodAxeRitualClothKnotWraps_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#RopeLashing_Set_A01` | Rope lashings | `SM_GIA_BloodAxeRitualRopeLashingSet_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#StoneWeights_A01` | Stone weights | `SM_GIA_BloodAxeRitualStoneWeight_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#SparseHornMarkers_A01` | Sparse horn markers | `SM_GIA_BloodAxeRitualHornMarker_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#BlackenedIron_TieHardware_A01` | Hardware accents | `SM_GIA_BloodAxeRitualTieHardware_A01` | Package needed; planning only | Docs package input ready only; unselected. |
| `BloodAxeRitualStones.png#Review_ScaleRows_A01` | Review rows | `SM_GIA_BloodAxeRitualPoleScaleRow_A01` | Planning row only | Docs reference input ready only; non-shipping. |
| `BloodAxeRitualStones.png#Review_CompositionRows_A01` | Review rows | `DOC_GIA_BloodAxeRitualPoleReviewRows_A01` | Planning row only | Docs reference input ready only; non-shipping. |
| `BloodAxeRitualStones.png#MaterialDiscipline_A01` | Material discipline | `DOC_GIA_BloodAxeRitualPoleMaterialDiscipline_A01` | Planning row only | Policy reference input ready only; no material authoring. |
| `BloodAxeRitualStones.png#LODAndCollision_A01` | LOD/collision planning | `DOC_GIA_BloodAxeRitualPoleLODAndCollision_A01` | Planning row only | Policy reference input ready only; no LOD or collision source. |

## Per-Child Readiness Rows

| Child/context ID | Current readiness | DCC preconditions before future source work | Unreal preconditions before future import work | Validator gaps | Current stop state |
| --- | --- | --- | --- | --- | --- |
| `BloodAxeRitualStones.png#RitualBannerPole_Tall_A01` | Package input ready only. Giant-scale 520-780 cm rough pole with split top, fixed red cloth, rope lashing, and weighted base for static warning and memory dressing. | Separate task must name this exact row, confirm height against female 442 cm and male 470 cm Giants, approve broad static cloth geometry, and preserve Blood Axe hostile language. | Requires approved DCC/FBX output and later import scope defining naming, pivot, orientation, LOD0-LOD3, material slots, and disabled/simple collision policy. | No source mesh, proof render, LOD source, collision proxy, import validator, static-cloth validator, final silhouette capture, or final visual approval exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#RitualBannerPole_Secondary_A01` | Package input ready only. Shorter 320-520 cm rough pole variant for background rhythm and abandoned camp traces; not neutral/civilized Giant dressing. | Separate task must approve secondary-pole height band, simpler silhouette, static cloth amount, and material restraint before source work. | Requires approved source output and later import scope; Unreal work must not add waypoint, interaction, morale, signal, startup, or runtime behavior. | No source mesh, height-read validator, material restraint scan, import validation, collision validation, or culture separation validator exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#RitualPole_Pair_A01` | Package input ready only. Uneven pair with static tied cloth band and stone weights for visual threshold framing only. | Separate task must approve pair spacing as art composition only and confirm it is not a gate, route marker, objective frame, or nav element. | Requires approved source output and later import scope; Unreal owner must avoid gate behavior, route behavior, trigger volumes, nav/pathfinding, interaction, and startup placement. | No pair-spacing validator, route/nav exclusion proof, trigger-volume exclusion proof, import validator, collision correctness, or final visual approval exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#RitualPole_Cluster_A01` | Package input ready only. Three to five varied poles for ritual-stone approach composition and memory dressing; sparse horns and broad cloth only. | Separate task must approve cluster footprint, pole count, silhouette density, non-graphic horn restraint, and no spell-device read before source work. | Requires approved source outputs and later import scope; Unreal work must not group it as an objective, encounter, aura, signal, spawn, route, or startup actor. | No cluster-density validator, gore/readability scan, VFX/audio exclusion proof, gameplay-marker exclusion proof, import validator, or final Blood Axe ritual approval exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#TiedCloth_Strips_A01` | Package input ready only. Static oxide red cloth-strip set with broad torn shapes, soot-dark lower edges, and hide ties. | Separate task must approve sculpted/static cloth treatment, strip count, broad fold scale, and texture-vs-geometry split for weave and fray. | Requires approved source and later import scope; Unreal work must not add cloth physics, wind, banner animation, material pulses, VFX/audio, faction buffs, or objective-readable cloth states. | No static-cloth validator, material-state scan, cloth-physics absence proof, import validator, runtime behavior scan, or final color approval exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#TiedCloth_KnotWraps_A01` | Package input ready only. Reusable cloth knots and wrap shapes for pole bases and cross ties; large readable wraps only. | Separate task must approve knot scale, wrap density, static geometry approach, and assignment of tiny fray/weave to textures or normals. | Requires approved source and later import scope; Unreal work must avoid cloth collision, simulation, animation, interaction prompts, signal states, and material-driven runtime behavior. | No knot-scale validator, micro-detail scan, static-treatment validator, import validator, material behavior validator, or collision validator exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#RopeLashing_Set_A01` | Package input ready only. Thick rope, hide cord, and major knot modules for tying poles, stones, and horn markers. | Separate task must approve rope thickness, lashing module ownership, major-knot geometry, and texture-only treatment for small rope fibers. | Requires approved source and later import scope; Unreal work must not add simulated rope, dangling physics, trap behavior, interaction, individual rope collision, or runtime states. | No rope-module validator, physics absence proof, trap/interaction exclusion proof, import validator, collision validator, or material audit exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#StoneWeights_A01` | Package input ready only. Crude heavy stones, mud-packed anchors, and rope-tied base weights sized for Giant handling. | Separate task must approve stone scale, base footprint, geometry-vs-texture cracks, and visual anchoring role before source work. | Requires approved source and later import scope; Unreal work must avoid pickup, loot, resource, crafting, damage, destructible, nav, trigger, or gameplay collision behavior. | No stone-scale validator, pickup/loot exclusion proof, destructible exclusion proof, collision correctness, import validator, or terrain contact proof exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#SparseHornMarkers_A01` | Package input ready only. Sparse horn markers tied near pole tops or stone bases as restrained silhouette punctuation. | Separate task must approve low-density horn use, non-graphic presentation, attachment scale, and separation from standalone horn-marker ownership. | Requires approved source and later import scope; Unreal work must not add collectible behavior, ritual gameplay state, aura/VFX, magic state, interaction, or signal behavior. | No horn-density validator, gore/escalation scan, ownership validator, VFX/audio exclusion proof, import validator, or final culture approval exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#BlackenedIron_TieHardware_A01` | Package input ready only. Crude blackened iron rings, collars, nails, and scrap hooks used sparingly on major ties. | Separate task must approve hardware count, material-slot sharing, large-shape readability, and texture-only treatment for small pitting or scratches. | Requires approved source and later import scope; Unreal material work must wait for separate authorization and must avoid unique material slots for every small piece. | No hardware-density validator, material-slot audit, micro-detail scan, import validator, texture audit, or performance validator exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#Review_ScaleRows_A01` | Reference input ready only. Non-shipping scale rows compare pole, cloth, rope, stone, and horn variants against female 442 cm and male 470 cm Giant baselines. | DCC work is not a default next step; a separate review-only task must define row purpose, scale marker limits, and non-shipping geometry if visualization is needed. | Unreal work is not a default next step; rows must remain outside startup placement, actor approval, final visual approval, runtime behavior, and shipping content unless separately scoped. | No scale-row asset, proof render, marker validation, camera validation, startup validation, import validator, or final scale approval exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#Review_CompositionRows_A01` | Reference input ready only. Docs-only rows for single-pole, paired-pole, cluster, and ritual approach spacing as visual composition only. | DCC work is not a default next step; any visualization task must keep rows non-shipping and avoid approving route, encounter, marker, or implementation order. | Unreal work is not a default next step; no actor, validator, capture, startup placement, objective marker, route behavior, encounter scripting, or final art signoff is authorized. | No composition visualization, spacing validator, route-overclaim scan, encounter exclusion proof, import validator, startup validation, or final visual approval exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#MaterialDiscipline_A01` | Policy reference input ready only. Locks rough timber, oxide red cloth, rope, hide, stone, blackened iron, soot, ash, mud, and sparse horn material language. | DCC source work must wait for a separately selected child row and inherit this material discipline without authoring materials here. | Unreal material work must wait for a separate material task; no material instance, texture asset, graph, emissive state, VFX/audio, or final color approval is created here. | No material instance validator, texture audit, graph audit, emissive absence validator, color calibration, culture separation validator, or VFX/audio scan exists from this task. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones.png#LODAndCollision_A01` | Policy reference input ready only. Records LOD0-LOD3 and collision-limit planning for poles, cloth, rope, stones, horns, hardware, and review rows. | DCC source work must wait for a separately selected mesh target, LOD source authorization, and any separately approved simple collision proxy scope. | Unreal collision setup must wait for approved source output and must not claim collision correctness, nav behavior, gameplay volumes, trigger volumes, runtime performance validation, or import approval from this reference. | No LOD source, LOD ratio validator, collision proxy, UCX mesh, import validator, nav exclusion proof, trigger-volume exclusion proof, collision correctness validator, or runtime performance validator exists. | Hold under No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |

## DCC Preconditions

Before any future DCC work may begin, a separate authorized task must:

- Select a concrete child/context row or explicitly define a batch scope without using this matrix as implementation order.
- Confirm allowed source folder and file scope in that future task; this matrix selects none.
- Preserve the scale lock: female 442 cm / 14'6", male 470 cm / 15'5", approved female range 14-15 ft / 427-457 cm, and approved male range 14'10"-16'0" / 452-488 cm.
- Preserve Blood Axe as hostile Giant sub-faction language and keep it separated from neutral/civilized Giant culture.
- Define mesh ownership, pivots, orientation, centimeter scale proof, LOD0-LOD3 targets, material slot limits, UV/bake expectations, collision proxy scope, and proof-render expectations in the future task.
- Confirm fixed geometry or texture treatment for cloth, rope, stone, horn, hardware, ash, mud, soot, and timber; baseline cloth physics and animation remain disallowed.
- Respect the No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail until a later task changes scope.

## Unreal Preconditions

Before any future Unreal work may begin, a separate authorized task must:

- Provide approved DCC/FBX/source output or explicitly authorize an Unreal-only documentation/import step.
- Select a concrete Unreal target in that future task; this matrix selects none.
- Define game content folder, asset naming, import settings, material instance scope, texture list, LOD import policy, collision policy, and validation commands in that future task.
- Confirm no cloth physics, animation, faction buff behavior, morale/AI behavior, aura/VFX/audio behavior, interaction behavior, quest marker behavior, objective logic, encounter scripting, nav/pathfinding, trigger volumes, loot/resource/crafting/economy behavior, damage/destructible/pickup behavior, signal behavior, readable text, runtime behavior, or startup placement is implied unless separately authorized.
- Confirm final visual approval, final Blood Axe ritual approval, final Giant culture approval, final package implementation approval, and first implementation target selection remain outside this matrix.

## Unresolved Approval Gates

- Lead Producer / Orchestrator must open a separate task before any child/context row moves beyond docs-only readiness.
- Production Package must not infer implementation order from this matrix.
- DCC owner must not begin source work until a separate DCC scope is opened.
- Unreal owner must not begin import, content work, startup placement, material work, validator work, Blueprint work, socket work, physics setup, animation work, VFX/audio work, or runtime work until a separate Unreal scope is opened.
- QA / Validation must define any future focused validator scope after source or content exists; this matrix creates no validator files.
- Docs / Index owner must handle task-board, asset-index, backlog, bootstrap, or global documentation updates separately.
- Final visual approval, final Blood Axe ritual approval, final Giant culture approval, cloth behavior approval, animation approval, gameplay buff approval, VFX/audio approval, runtime behavior approval, and first implementation target selection remain unresolved.

## Validation Notes

- Readiness matrix scan: this file covers exactly the 14 required child/context IDs from the task packet.
- Package-ready row scan: package candidates, planning rows, review rows, material discipline, and LOD/collision planning are represented without selecting targets.
- Guardrail scan: No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail are explicit in readiness sections and row stop states.
- Giant scale scan: female 442 cm / 14'6", male 470 cm / 15'5", approved female range 14-15 ft / 427-457 cm, and approved male range 14'10"-16'0" / 452-488 cm are preserved.
- Culture separation scan: Blood Axe remains a hostile Giant sub-faction only and is explicitly separated from neutral/civilized Giant culture.
- Implementation-scope scan: no source folder, DCC source, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX, Unreal Content, material instance, texture asset, import script, validator, runtime source, Blueprint, socket, cloth physics, animation, VFX/audio, startup placement, external source concept movement, final visual approval, gameplay buff behavior, morale/AI behavior, aura behavior, interaction behavior, quest marker behavior, objective logic, encounter scripting, nav/pathfinding, trigger volume, loot/resource/crafting/economy behavior, damage/destructible/pickup behavior, signal behavior, readable text, runtime behavior, or first target selection is authorized.

## Quality Gate Checklist

- Docs-only matrix created in the assigned file only.
- All 14 required child/context IDs are represented exactly and explicitly.
- Package inputs, readiness status, per-child readiness rows, unresolved approval gates, validation notes, and DCC/Unreal preconditions are included.
- Required guardrail labels are explicit: No-cloth-physics guardrail, No-animation guardrail, No-build guardrail, No-gameplay-buff guardrail, No-vfx-audio guardrail, and No-target-selected guardrail.
- Giant scale and culture locks are preserved exactly.
- Blood Axe hostile raider language stays separated from neutral/civilized Giant culture.
- No first DCC target, first Unreal target, implementation order, source folder, final visual approval, cloth physics, animation, faction buff behavior, morale/AI behavior, aura/VFX/audio behavior, interaction behavior, quest marker behavior, objective logic, encounter scripting, nav/pathfinding, trigger volumes, loot/resource/crafting/economy behavior, damage/destructible/pickup behavior, signal behavior, readable text, runtime behavior, or package implementation target is selected.
- No source asset, DCC file, FBX, Unreal Content, material instance, texture, validator, runtime file, startup placement, external source concept file, task-board edit, global index edit, backlog edit, bootstrap edit, or implementation file is created or authorized.
