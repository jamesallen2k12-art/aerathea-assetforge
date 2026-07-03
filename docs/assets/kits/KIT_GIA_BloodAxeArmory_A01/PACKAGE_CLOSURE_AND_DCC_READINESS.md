# KIT_GIA_BloodAxeArmory_A01 Package Closure and DCC Readiness

## Scope

- Task: `AET-MA-20260629-079`
- Scope type: docs-only Blood Axe armory package-closure and DCC-readiness refresh
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source concept: `BloodAxeArmory.png`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: package-planning closure ready; no DCC target selected
- Scale dependency: validated `SK_GIA_Base_A01` scale lock, female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Source-storage guardrail: source concept remains in the external concept folder only. Do not copy, move, edit, embed, or commit the source image for this docs-only readiness document.

This document closes the current docs-only package-planning pass for the Blood Axe armory. It does not select a first DCC build target, create source folders, author meshes, export FBX, import Unreal Content, change runtime source, place startup actors, define combat/projectile/crafting/economy behavior, copy source concepts, or claim final visual approval.

## Closure Result

The Blood Axe armory now has package-ready planning coverage for the primary child assets from the original 22-child intake. The remaining work is no longer package discovery; it is approval-gated build selection, DCC/export/Unreal implementation, material authoring, focused validator creation, skeletal fit, animation/gameplay definition, and final visual review.

The armory should stay a hostile Giant sub-faction kit. Red-black raider materials, trophy armor, crude forge language, and stolen-metal reforging must not become neutral or civilized Giant culture.

## Package Closure Map

| Area | Package or document | Current docs status | Future gate |
| --- | --- | --- | --- |
| Parent kit | `KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md` | Ready | Lead approval before any DCC target is selected. |
| Child intake | `KIT_GIA_BloodAxeArmory_A01/CHILD_ASSET_INTAKE.md` | Ready; global status refresh handled by integration | Docs/Index integration before source-of-truth docs mark every final child ready. |
| Initial readiness | `KIT_GIA_BloodAxeArmory_A01/IMPLEMENTATION_READINESS_MATRIX.md` | Ready for first package set | Superseded by this broader closure map for future approval discussion. |
| Double axe | `SM_GIA_BloodAxeDoubleAxe_A01/PRODUCTION_PACKAGE.md` | Ready | Visual approval for blade shape, trophy density, and hero/chieftain variants before final art. |
| Cleaver | `SM_GIA_BloodAxeCleaver_A01/PRODUCTION_PACKAGE.md` | Ready | DCC build target approval and combat trace policy before implementation. |
| Crusher hammer | `SM_GIA_BloodAxeCrusherHammer_A01/PRODUCTION_PACKAGE.md` | Ready | DCC build target approval and grip/pivot confirmation before implementation. |
| Hook spear | `SM_GIA_BloodAxeHookSpear_A01/PRODUCTION_PACKAGE.md` | Ready | Gameplay approval before pull, drag, reach, or special attack behavior. |
| Skinning knife | `SM_GIA_BloodAxeSkinningKnife_A01/PRODUCTION_PACKAGE.md` | Ready | Explicit approval before loot, harvesting, inventory, or gore escalation. |
| Longbow A01 | `SM_GIA_BloodAxeLongbow_A01/PRODUCTION_PACKAGE.md` | Ready | Bow socket, quiver clearance, animation, and projectile approval before implementation. |
| Longbow A02 | `SM_GIA_BloodAxeLongbow_A02/PRODUCTION_PACKAGE.md` | Ready | Variant distinction and common-archer use must survive visual/DCC review. |
| Longbow A03 | `SM_GIA_BloodAxeLongbow_A03/PRODUCTION_PACKAGE.md` | Ready | Variant distinction and battle-scar damage density must survive visual/DCC review. |
| Shortbows | `KIT_GIA_BloodAxeShortbows_A01/PRODUCTION_PACKAGE.md` and child intake | Ready | Variant export manifest and projectile/animation approval before implementation. |
| Quivers | `KIT_GIA_BloodAxeQuivers_A01/PRODUCTION_PACKAGE.md` and child intake | Ready | Variant export manifest and back/belt clearance validation before implementation. |
| Bow parts | `KIT_GIA_BloodAxeBowParts_A01/PRODUCTION_PACKAGE.md` and child intake | Ready | Static workshop/dressing approval before DCC; no projectile stats or animation timing. |
| Bowyer tools | `KIT_GIA_BloodAxeBowyerTools_A01/PRODUCTION_PACKAGE.md` and child intake | Ready | Usable workstation, crafting, and economy behavior require separate approval. |
| Trophy helm | `SM_GIA_BloodAxeTrophyHelm_A01/PRODUCTION_PACKAGE.md` | Ready | Head/neck fit, face visibility, and skeletal/wearable review before implementation. |
| Raider chest | `SK_GIA_BloodAxeRaiderChest_A01/PRODUCTION_PACKAGE.md` | Ready | Skeletal fit, shoulder clearance, and physics/cloth policy before implementation. |
| Harness | `SK_GIA_BloodAxeHarness_A01/PRODUCTION_PACKAGE.md` | Ready | Skeletal fit, carry sockets, and cloth/physics policy before implementation. |
| Trophy belt | `SK_GIA_BloodAxeTrophyBelt_A01/PRODUCTION_PACKAGE.md` | Ready | Pelvis/thigh clearance and loot/inventory guardrails before implementation. |
| Greaves | `SK_GIA_BloodAxeGreaves_A01/PRODUCTION_PACKAGE.md` | Ready | Knee/ankle/foot clearance, gait, and IK review before implementation. |
| War banner | `SM_GIA_BloodAxeWarBanner_A01/PRODUCTION_PACKAGE.md` | Ready | Static mesh approval before DCC; cloth simulation and faction aura behavior remain separate gates. |
| Reforged metal | `MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md` | Ready | Material graph, texture, shader, and emissive/forge-heat approval before Unreal authoring. |
| Scrap pile | `KIT_GIA_BloodAxeScrapPile_A01/PRODUCTION_PACKAGE.md` and child intake | Ready | No loot/resource/destructible/crafting behavior without separate approval. |
| Reforging process | `KIT_GIA_BloodAxeReforging_A01/PRODUCTION_PACKAGE.md` and child intake | Ready | No crafting/economy/resource/material-graph behavior without separate approval. |

## Remaining Gaps

No primary Blood Axe armory child still needs an initial docs-only production package after this cycle. The remaining gaps are implementation and approval gates:

- Docs/Index integration still needs to update the original child intake and global source-of-truth docs so `SM_GIA_BloodAxeLongbow_A02`, `SM_GIA_BloodAxeLongbow_A03`, `KIT_GIA_BloodAxeShortbows_A01`, and `KIT_GIA_BloodAxeReforging_A01` are marked ready everywhere.
- A first DCC target has not been selected.
- No Blender source folders, source meshes, LOD source files, FBX exports, proof renders, Unreal Content assets, material graphs, Blueprints, validators, or startup actors exist for this Blood Axe armory package set.
- Mini-kits still need variant export manifests before DCC implementation: quivers, shortbows, bow parts, bowyer tools, scrap pile, and reforging process.
- Wearable armor still needs a skeletal-fit lane against `SK_GIA_Base_A01` before implementation.
- Bow and quiver work still needs animation, socket, projectile, and arrow-scale approval before any gameplay-facing behavior.
- Material work still needs a separate VFX/materials or Unreal task before texture assets, master material instances, forge-heat states, or emissive variants are authored.

## DCC Candidate Risk Ranking

This ranking supports future approval discussion. It does not choose or authorize the first build target.

| Rank | Candidate | Risk | Why | Required approval before build |
| ---: | --- | --- | --- | --- |
| 0 | `MI_GIA_BloodAxeReforgedMetal_A01` | Medium | Shared material language affects every weapon, armor plate, bow fitting, quiver rim, scrap pile, and forge prop. | Material/Unreal task approval for shader graph, texture assets, default no-emissive policy, and validator scope. |
| 1 | `SM_GIA_BloodAxeCrusherHammer_A01` | Low | Broad silhouette, simple mass, limited trophies, clear grip, and low socket complexity. | Lead approval for first static-mesh DCC target, grip pivot, collision policy, and material dependency. |
| 2 | `SM_GIA_BloodAxeCleaver_A01` | Low-medium | Simple slab silhouette and readable sidearm shape, but combat trace policy still matters. | Lead approval for DCC target and combat-trace boundaries. |
| 3 | `SM_GIA_BloodAxeDoubleAxe_A01` | Medium | Signature hero weapon with higher trophy/detail risk and stronger visual-approval dependency. | Visual approval for blade shape, trophy density, red paint placement, and chieftain/boss variant separation. |
| 4 | `SM_GIA_BloodAxeLongbow_A02` | Medium | Clean common-archer bow is simpler than A01/A03, but string, nock, back-carry, and quiver clearance still require coordination. | Bow socket, string locator, back-carry, and quiver-clearance approval; no projectile/animation scope. |
| 5 | `SM_GIA_BloodAxeLongbow_A01` and `SM_GIA_BloodAxeLongbow_A03` | Medium-high | Larger or heavier visual variants need tighter variant separation and damage/trophy-density control. | Variant visual approval, socket policy, and no gameplay-stat claims. |
| 6 | `KIT_GIA_BloodAxeQuivers_A01` and `KIT_GIA_BloodAxeShortbows_A01` | Medium-high | Mini-kit breadth, carry clearance, child naming, and arrow scale can create drift if collapsed. | Variant export manifest, carry socket policy, and projectile/animation approval boundaries. |
| 7 | `KIT_GIA_BloodAxeBowParts_A01`, `KIT_GIA_BloodAxeBowyerTools_A01`, `KIT_GIA_BloodAxeScrapPile_A01`, `KIT_GIA_BloodAxeReforging_A01` | Medium | Static props are straightforward but have crafting/economy/resource overclaim risk and many child meshes. | Variant manifest plus explicit no-crafting/no-economy/no-resource behavior gate. |
| 8 | Wearable armor modules | High | Harness, trophy belt, greaves, chest, and helm depend on skeletal fit, locomotion clearance, physics/cloth policy, and attachment sockets. | Dedicated wearable fit lane, Giant base validation, and final armor visual approval. |
| 9 | `SM_GIA_BloodAxeWarBanner_A01` | Medium-high if cloth is requested | Static version is manageable; cloth simulation, carried variants, and faction gameplay effects increase risk. | Static-or-cloth decision, cloth simulation approval, and faction-effect gameplay approval if any. |

## Required Variant Manifests Before DCC

The following packages should not enter DCC as one collapsed mesh:

- `KIT_GIA_BloodAxeQuivers_A01`: belt quiver, back quiver, rack quiver, loose arrow, arrow bundle, arrow-head display, strap variants, trophy tags.
- `KIT_GIA_BloodAxeShortbows_A01`: hunter shortbow, scout compact shortbow, camp rack shortbow, repaired spare shortbow, string rack, nock support pieces.
- `KIT_GIA_BloodAxeBowParts_A01`: strings, limbs, shafts, heads, wraps, racks, repair pieces, nocks, bundles.
- `KIT_GIA_BloodAxeBowyerTools_A01`: clamps, draw knives, stringing frame, glue pot, measuring jig, rasp, blade scraper, tool rack, repair bench pieces.
- `KIT_GIA_BloodAxeScrapPile_A01`: metal chunks, broken blades, failed casts, chained bundles, forge bins, rack scatter, slag trays, reforging stock.
- `KIT_GIA_BloodAxeReforging_A01`: stolen scrap intake, broken metal sorting, billets/ingots, heated blanks, remade weapon stages, cooling racks, quench trough, process signage/markers.

Each future manifest should name planned meshes, pivots, collision policy, material slots, LOD expectations, planned source/export paths, and Unreal target paths. It should also restate the relevant no-gameplay guardrails.

## Validator Gaps

No new validators are authored by this readiness document. Future implementation lanes should add focused validators only when they own the affected tool paths.

| Future lane | Validator need |
| --- | --- |
| DCC source/export | Confirm centimeter scale, Giant-relative dimensions, source/export paths, FBX names, LOD0-LOD3 sources, material slots, pivots, collision proxy notes, and no micro-detail geometry misuse. |
| Giant scale | Compare dimensions and grip/carry markers against female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5". |
| Weapon import | Confirm Unreal path, grip pivot, display/equipped collision policy, material slots, LODs, texture references, and planned trace marker names without adding combat rules. |
| Bow import | Confirm bow arc, grip pivot, nock markers, string locators, back-carry marker, `back_quiver` clearance, and no projectile logic. |
| Mini-kit import | Confirm per-child mesh names, export rows, pivots, collision policy, material slots, LODs, reuse policy, and no collapsed-kit assumption. |
| Wearable fit | Confirm helm/chest/harness/belt/greave bounds against Giant body, shoulders, pelvis, thighs, knees, ankles, head, and locomotion clearance. |
| Material authoring | Confirm shared parent material, texture references, default no-emissive, red-paint mask limits, roughness/metallic ranges, and `ForgeHeatAmount=0.0` unless approved. |
| Culture separation | Confirm Blood Axe docs do not claim default Giant culture, neutral cave-town identity, blue-gray stoneworker motifs, or civilized Giant materials. |
| Source-storage | Confirm external concept art was not copied, embedded, moved, or committed. |

## No-Build Guardrails

- No DCC source creation.
- No Blender source files.
- No source folders.
- No FBX export.
- No Unreal Content import.
- No material graph, shader, texture, Niagara, Blueprint, runtime source, or startup-scene work.
- No source concept copying, moving, editing, embedding, or committing.
- No final visual approval claim.
- No selection of a first DCC build target.
- No combat traces, damage values, attack timing, projectile behavior, arrow inventory, loot rules, crafting recipes, salvage loops, economy/resource behavior, destructible behavior, pickup behavior, workstation behavior, or vendor data.
- No cloth simulation, physics setup, skeletal fit, or animation timing.
- No promotion of Blood Axe red-black raider language into neutral/civilized Giant culture.

## Approval Gates

- Lead approval is required to select a first DCC build target.
- Visual approval is required before final hero-weapon shape, trophy density, armor silhouette, banner motion language, or material-emissive variants are locked.
- DCC approval is required before creating Blender source, source folders, FBX exports, or proof renders.
- Unreal approval is required before importing Static Meshes, Skeletal Meshes, materials, textures, Blueprints, validators, or startup actors.
- Gameplay approval is required before combat, projectile, crafting, economy, loot, resource, destructible, pickup, equip, interaction, workstation, or vendor behavior.
- Animation approval is required before bow draw timing, release timing, reload timing, Giant melee swings, wearable fit motion, cloth, or physics.
- Source-storage approval is required before any external concept file enters the repository.
- Culture approval is required if Blood Axe visual language starts bleeding into neutral/civilized Giant packages.

## Quality Gate Checklist

- Primary Blood Axe armory child package docs are complete at planning level.
- Giant scale lock is explicit and unchanged.
- Blood Axe remains a hostile Giant sub-faction, not default Giant culture.
- Future DCC candidate ranking is risk guidance only and does not select a build target.
- Remaining implementation gaps are explicit.
- Mini-kit variant manifests are required before source work.
- Validator gaps are documented without creating tools.
- Docs-only no-build guardrails are explicit.
- Source concept remains external.
- No DCC, FBX, Unreal, runtime, material graph, startup, gameplay, economy, crafting, loot, projectile, animation, cloth, physics, or final visual approval work is claimed.
