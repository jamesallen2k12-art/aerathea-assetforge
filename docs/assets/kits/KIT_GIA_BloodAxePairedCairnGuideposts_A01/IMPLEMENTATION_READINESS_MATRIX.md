# KIT_GIA_BloodAxePairedCairnGuideposts_A01 Implementation Readiness Matrix

## Readiness Scope

- Task ID: `AET-MA-20260629-495`
- Package: `KIT_GIA_BloodAxePairedCairnGuideposts_A01`
- Source package: `docs/assets/kits/KIT_GIA_BloodAxePairedCairnGuideposts_A01/PRODUCTION_PACKAGE.md`
- Source intake: `docs/assets/kits/KIT_GIA_BloodAxePairedCairnGuideposts_A01/CHILD_ASSET_INTAKE.md`
- Matrix status: docs-only implementation readiness review.
- Output status: no source asset, source folder, DCC, FBX, Unreal Content, material instance, texture asset, validator, runtime file, startup placement, waypoint behavior, nav gate logic, route scripting, quest pointer behavior, encounter lane planning, collision correctness, traversal proof, path-width gameplay values, pathfinding proof, readable text, UI marker language, interaction behavior, objective markers, pickup behavior, loot/resource/crafting/economy behavior, VFX/audio, final visual approval, or implementation target is created or selected by this matrix.

This matrix summarizes the package inventory, row readiness, preconditions, approval gates, validator gaps, and residual risk for the paired cairn guidepost kit. Rows are unordered. No first DCC target, first Unreal target, first package implementation target, implementation order, source folder, Content path, validator target, review target, or final visual approval target is selected here.

## Scale And Culture Locks

- Giant scale lock from the package and intake: female baseline 442 cm / 14 ft 6 in, male baseline 470 cm / 15 ft 5 in, approved Giant ranges females 14-15 ft and males 14 ft 10 in-16 ft.
- Compact scan forms: female 442 cm / 14'6" and male 470 cm / 15'5".
- This matrix does not change Giant race scale, skeleton policy, socket policy, capsule expectations, body proportions, or character collision assumptions.
- Blood Axe remains a hostile Giant sub-faction only.
- Blood Axe hostile raider language must remain separate from neutral/civilized Giant culture.
- Allowed Blood Axe material language: crude highland stone, soot, ash, trampled mud, cold cave stone, oxide red cloth, faded maroon strips, hide cord, rawhide knots, rough rope, scorched leather, sparse blackened iron, old horn, aged bone, and dull scrap.
- Excluded neutral/civilized Giant defaults: refined cave-town masonry, blue-gray civic stonework, terrace or waterwork motifs, warm hearth settlement identity, peaceful highland guide language, carved civic ornament, restrained blue-rune culture, and polished stoneworker finish.

## Required Guardrails

- No-waypoint guardrail: stop before waypoint behavior, breadcrumb logic, route pointer behavior, quest pointer behavior, UI arrows, map markers, minimap markers, directional marker behavior, readable text, in-world instructions, or objective-readable shapes.
- No-nav-route guardrail: stop before nav gate logic, route scripting, route validation, nav/pathfinding, traversal proof, path-width gameplay values, encounter lane planning, patrol lanes, spawn lanes, route blocker behavior, smart links, or any claim that a player path has been proven.
- No-build guardrail: stop before source folders, DCC files, Blender scenes, meshes, sculpt, retopo, UVs, bakes, proof renders, LOD source, collision proxies, FBX exports, Unreal Content, material instances, texture assets, material graphs, import scripts, validators, runtime source, Blueprints, sockets, animation assets, VFX/audio assets, startup actors, external source concept movement, or Hermes file/configuration work.
- No-collision-correctness guardrail: stop before collision correctness claims, collision proxy authoring, UCX meshes, Unreal collision setup, physics bodies, gameplay volumes, trigger volumes, objective volumes, nav blockers, invisible blockers, traversal validation, camera clearance proof, or runtime performance validation.
- No-vfx-audio guardrail: stop before glow, particles, dynamic lights, signal light, ritual light, shamanic pulse, torch state, animated material state, sound cue, ambient emitter, audio behavior, Niagara, material-driven VFX, or VFX/audio approval.
- No-target-selected guardrail: stop before selecting a first DCC target, first Unreal target, first package implementation target, implementation order, source folder, Content path, import path, validator target, package closure target, final Blood Axe approval target, final Giant culture approval target, or final visual approval target.

## Package Inventory

| Child/context ID | Intake type | Proposed future asset or package | Intake status | Matrix readiness |
| --- | --- | --- | --- | --- |
| `BloodAxeRitualStones_A01#PairedCairnGuideposts_ClosePair_A01` | Close pair | `SM_GIA_BloodAxePairedCairnClosePair_A01` | package-ready | Docs package input ready for later lead review only; unselected. |
| `BloodAxeRitualStones_A01#PairedCairnGuideposts_StaggeredPair_A01` | Staggered pair | `SM_GIA_BloodAxePairedCairnStaggeredPair_A01` | package-ready | Docs package input ready for later lead review only; unselected. |
| `BloodAxeRitualStones_A01#PairedCairnGuideposts_CaveThresholdPair_A01` | Cave-threshold pair | `SM_GIA_BloodAxeCaveThresholdCairnPair_A01` | package-ready | Docs package input ready for later lead review only; unselected. |
| `BloodAxeRitualStones_A01#PairedCairnGuideposts_MovedCampPair_A01` | Moved-camp pair | `SM_GIA_BloodAxeMovedCampCairnPair_A01` | package-ready | Docs package input ready for later lead review only; unselected. |
| `BloodAxeRitualStones_A01#ReviewOnly_PairedCairnSpacingRows_A01` | Review-only spacing rows | `DOC_GIA_BloodAxePairedCairnSpacingRows_A01` | package-ready | Non-shipping docs package input ready for later lead review only; unselected. |

## Row-By-Row Readiness Matrix

| Child/context ID | Current readiness | DCC preconditions before future source work | Unreal preconditions before future import work | Validator gaps | Residual risk and stop state |
| --- | --- | --- | --- | --- | --- |
| `BloodAxeRitualStones_A01#PairedCairnGuideposts_ClosePair_A01` | Package-ready for later lead review only. Compact unequal two-cairn composition uses crude Giant-built stone mass, ash, soot, trampled mud, and restrained red cloth as visual route memory only. | A separate authorized task must name this exact row, confirm close-pair spacing as art composition only, preserve female 442 cm / 14'6" and male 470 cm / 15'5" scale comparison, define few-large-stone construction, and restate no waypoint or target behavior. | Requires approved source output and later import scope defining naming, pivot, orientation, LOD0-LOD3, material slot limits, texture list, and disabled/simple collision policy. Unreal work must not add waypoint behavior, nav gate logic, route scripting, objective markers, collision correctness, or startup placement. | No source mesh, proof render, LOD source, collision proxy, import validator, scale-row proof, waypoint exclusion proof, collision correctness validation, or final visual approval exists. | Residual risk is close pairing being over-read as a marker or objective bracket. Hold under No-waypoint guardrail, No-nav-route guardrail, No-build guardrail, No-collision-correctness guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones_A01#PairedCairnGuideposts_StaggeredPair_A01` | Package-ready for later lead review only. Depth-offset cairns create a repeated Blood Axe memory beat through silhouette asymmetry, ash, soot, and sparse cloth without lane or route meaning. | A separate authorized task must approve offset depth as visual composition only, Giant-scale massing, uneven heights, material restraint, and no encounter lane, nav, route, or pathfinding purpose before source work. | Requires approved source output and later import scope; Unreal work must not add route validation, nav/pathfinding, route blockers, patrol lanes, spawn lanes, encounter lanes, quest pointer behavior, or startup placement. | No source mesh, offset-composition proof, route-overclaim scan, nav/pathfinding exclusion proof, collision correctness validation, import validator, startup validation, or final visual approval exists. | Residual risk is staggered depth being treated as route evidence. Hold under No-waypoint guardrail, No-nav-route guardrail, No-build guardrail, No-collision-correctness guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones_A01#PairedCairnGuideposts_CaveThresholdPair_A01` | Package-ready for later lead review only. Rough cairns or stone-and-cloth markers visually suggest an old Blood Axe cave threshold while staying non-interactive and non-authoritative. | A separate authorized task must approve threshold read as art direction only, preserve Giant scale lock, define stone and cloth ownership, and restate no gate, traversal, path-width, collision, quest pointer, or cave approval purpose. | Requires approved source output and later import scope; Unreal work must not add gate logic, doorway behavior, traversal proof, pathfinding proof, collision correctness, trigger volumes, objective volumes, UI marker language, or startup placement. | No source mesh, proof render, cave-read validation, traversal proof, pathfinding proof, collision correctness validation, trigger-volume exclusion proof, import validator, or final visual approval exists. | Residual risk is threshold framing being misused as gate, doorway, traversal, or collision evidence. Hold under No-waypoint guardrail, No-nav-route guardrail, No-build guardrail, No-collision-correctness guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones_A01#PairedCairnGuideposts_MovedCampPair_A01` | Package-ready for later lead review only. Older collapsed pair uses shifted stones, faded cloth, cold ash, mud, and weathered ties as abandoned Blood Axe environmental history only. | A separate authorized task must approve static collapsed silhouette, aged material state, texture-led wear, no tracking mechanic, no salvage or pickup purpose, no loot/resource/crafting/economy purpose, and no implementation target selection. | Requires approved source output and later import scope; Unreal work must not add destructible setup, physics setup, loot behavior, pickup behavior, interaction behavior, objective state, route behavior, VFX/audio, or startup placement. | No source mesh, collapse-read proof, physics/destruction exclusion proof, pickup/loot exclusion proof, interaction exclusion proof, collision correctness validation, import validator, or final visual approval exists. | Residual risk is abandoned-camp language being promoted into interactable, pickup, loot, or tracking behavior. Hold under No-waypoint guardrail, No-nav-route guardrail, No-build guardrail, No-collision-correctness guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |
| `BloodAxeRitualStones_A01#ReviewOnly_PairedCairnSpacingRows_A01` | Package-ready as non-shipping docs reference only. Review rows compare close, staggered, cave-threshold, and moved-camp spacing against female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in Giant baselines. | DCC visualization is not a default next step. A separate review-only task must define non-shipping row purpose, scale-marker limits, visual-composition-only spacing, and no first target or implementation order if any visualization is later needed. | Unreal visualization is blocked unless a separate review-only task defines scope. No actor, capture, startup placement, validator, collision setup, route validation, pathfinding proof, final visual approval, or shipping content is authorized here. | No review-row asset, proof render, capture, scale-row proof, camera validation, collision correctness validation, startup validation, final scale approval, or final visual approval exists. | Residual risk is review material being mistaken for shipping content, route spacing evidence, traversal proof, or target selection. Hold under No-waypoint guardrail, No-nav-route guardrail, No-build guardrail, No-collision-correctness guardrail, No-vfx-audio guardrail, and No-target-selected guardrail. |

## General DCC Preconditions

Before any future DCC work may begin, a separate authorized task must:

- Name a concrete child/context row or approved batch scope without using this matrix as implementation order.
- Define allowed source folder and file scope in that future task; this matrix selects none.
- Preserve Giant scale lock: female baseline 442 cm / 14 ft 6 in, male baseline 470 cm / 15 ft 5 in, approved Giant ranges females 14-15 ft and males 14 ft 10 in-16 ft.
- Preserve compact scan forms where useful: female 442 cm / 14'6" and male 470 cm / 15'5".
- Preserve Blood Axe as hostile Giant sub-faction language and keep it separated from neutral/civilized Giant culture.
- Define mesh ownership, pivots, orientation, centimeter scale proof, LOD0-LOD3 targets, material slot limits, UV/bake expectations, collision proxy scope if any, and proof-render expectations in the future task.
- Confirm static treatment for stones, cloth, ash, mud, soot, rope, rawhide, horn, bone, and sparse blackened iron unless a separately named non-baseline variant authorizes otherwise.
- Keep review-only spacing rows as non-shipping planning inputs unless a later task explicitly changes scope.
- Respect the No-waypoint guardrail, No-nav-route guardrail, No-build guardrail, No-collision-correctness guardrail, No-vfx-audio guardrail, and No-target-selected guardrail until a later task changes scope.

## General Unreal Preconditions

Before any future Unreal work may begin, a separate authorized task must:

- Provide approved DCC/FBX/source output or explicitly authorize an Unreal-only documentation/import step.
- Select a concrete Unreal target in that future task; this matrix selects none.
- Define game content folder, asset naming, import settings, material instance scope, texture list, LOD import policy, collision policy, and validation commands in that future task.
- Confirm no waypoint behavior, nav gate logic, route scripting, quest pointer behavior, encounter lane planning, collision correctness, traversal proof, path-width gameplay values, pathfinding proof, readable text, UI marker language, interaction behavior, objective markers, pickup behavior, loot/resource/crafting/economy behavior, VFX/audio, runtime behavior, or startup placement is implied unless separately authorized.
- Confirm final Blood Axe approval, final Giant culture approval, final visual approval, final package implementation approval, and first implementation target selection remain outside this matrix.

## Required Approvals Before Any Later Promotion

- Lead Producer / Orchestrator must open a separate task before any child/context row moves beyond docs-only readiness.
- Production Package must not infer implementation order from this matrix.
- DCC ownership must be assigned separately before source asset folders, Blender files, proof renders, LOD source, collision proxies, or FBX exports are created.
- Unreal ownership must be assigned separately before game content folders, imports, material instances, textures, validators, review actors, startup placement, Blueprints, sockets, runtime files, collision setup, VFX/audio, or performance claims are created.
- QA / Validation must define any future focused validator scope after source or content exists; this matrix creates no validator files.
- Docs / Index owner must handle task-board, asset-index, backlog, bootstrap, approval queue, or global documentation updates separately.
- Final Blood Axe approval, final Giant culture approval, final visual approval, waypoint behavior approval, nav/route approval, collision correctness approval, VFX/audio approval, runtime behavior approval, and first implementation target selection remain unresolved.

## Cross-Row Validator Gaps

- Readiness matrix scan: this file must remain docs-only and scoped to `IMPLEMENTATION_READINESS_MATRIX.md`.
- Child ID presence scan: all 5 required child/context IDs from the task packet must remain represented exactly and explicitly.
- Package-ready row scan: close pair, staggered pair, cave-threshold pair, moved-camp pair, and review-only spacing rows are represented without selecting targets.
- Guardrail label scan: No-waypoint guardrail, No-nav-route guardrail, No-build guardrail, No-collision-correctness guardrail, No-vfx-audio guardrail, and No-target-selected guardrail must remain explicit.
- Giant scale scan: female baseline 442 cm / 14 ft 6 in, male baseline 470 cm / 15 ft 5 in, approved Giant ranges females 14-15 ft and males 14 ft 10 in-16 ft, plus compact forms female 442 cm / 14'6" and male 470 cm / 15'5", must remain unchanged.
- Blood Axe/civilized Giant separation scan: Blood Axe remains a hostile Giant sub-faction only and must not replace neutral/civilized Giant culture.
- DCC gap: no source concept approval, source folder, DCC source, sculpt, retopo, UV, bake, LOD source, proof render, collision proxy, or FBX exists.
- Unreal gap: no Unreal Content, material instance, texture asset, import script, validator, review actor, startup placement, Blueprint, runtime file, socket, VFX/audio, collision setup, nav setup, gameplay setup, or final visual approval exists.
- Positive-claim gap: no waypoint behavior, nav gate logic, route scripting, quest pointer behavior, encounter lane planning, collision correctness, traversal proof, path-width gameplay values, pathfinding proof, readable text, UI marker language, interaction behavior, objective markers, pickup behavior, loot/resource/crafting/economy behavior, VFX/audio, final visual approval, runtime behavior, or first target selection is claimed.

## Residual Risk

- Paired compositions can be misread as waypoint, objective, route, or gate language if later tasks omit the required guardrails.
- Cave-threshold pairing can be misused as traversal, path-width, pathfinding, or collision evidence without actual DCC, Unreal, and QA proof.
- Moved-camp pairing can drift into interactable, pickup, loot, tracking, or salvage behavior if abandoned-camp language is overextended.
- Review-only spacing rows can be mistaken for shipping content or implementation order if non-shipping status is not rechecked.
- Oxide red cloth and chipped red paint can drift into readable text, UI marker language, or VFX/audio cues if material restraint is not enforced.
- Blood Axe hostile sub-faction identity can drift into neutral/civilized Giant culture if cave-town masonry, civic blue-gray stonework, warm hearth identity, peaceful wayfinding, or restrained blue-rune language is introduced as a default.
- LOD and collision planning can be mistaken for implemented collision correctness or performance validation if future tasks do not require source, import, and validation evidence.

## Quality Gate Checklist

- Docs-only matrix created in the assigned file only.
- All 5 required child/context IDs are represented exactly and explicitly.
- Package inventory, row-by-row readiness, DCC/Unreal preconditions, required approvals, validator gaps, and residual risk are included.
- Required guardrail labels are explicit: No-waypoint guardrail, No-nav-route guardrail, No-build guardrail, No-collision-correctness guardrail, No-vfx-audio guardrail, and No-target-selected guardrail.
- Giant scale lock is preserved: female baseline 442 cm / 14 ft 6 in, male baseline 470 cm / 15 ft 5 in, approved Giant ranges females 14-15 ft and males 14 ft 10 in-16 ft.
- Compact Giant scan forms are present: female 442 cm / 14'6" and male 470 cm / 15'5".
- Blood Axe hostile Giant sub-faction separation from neutral/civilized Giant culture is preserved.
- No first DCC target, first Unreal target, implementation order, source folder, Content path, final Blood Axe approval, final Giant culture approval, final visual approval, waypoint behavior, nav gate logic, route scripting, quest pointer behavior, encounter lane planning, collision correctness, traversal proof, path-width gameplay values, pathfinding proof, readable text, UI marker language, interaction behavior, objective markers, pickup behavior, loot/resource/crafting/economy behavior, VFX/audio, runtime behavior, or package implementation target is selected.
- No source asset, source folder, DCC file, FBX, Unreal Content, material instance, texture asset, validator, runtime file, startup placement, external source concept file, task-board edit, global index edit, backlog edit, bootstrap edit, approval-queue edit, Hermes file/configuration work, or implementation file is created or authorized.
