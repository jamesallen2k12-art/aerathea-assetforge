# KIT_GIA_BloodAxeCaveRemnantCluster_A01 Child Asset Intake

## Source

- Parent backlog row: `Blood Axe Nomad Ritual Stones`
- Grandparent package: `KIT_GIA_BloodAxeRitualStones_A01`
- Parent package: `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- Current package: `KIT_GIA_BloodAxeCaveRemnantCluster_A01`
- Related packages: `SM_GIA_BloodAxeRitualCairnGuidepost_A01` and `SM_GIA_BloodAxeStandingStone_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only planning child breakdown; no row may proceed to DCC, FBX, Unreal, startup placement, runtime work, final approval, or first implementation target selection
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture
- Scale dependency: Giant scale lock from `SK_GIA_Base_A01` uses female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges remain females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: external source concepts remain external. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This intake splits `KIT_GIA_BloodAxeCaveRemnantCluster_A01` into planning-only child rows for cairn, low standing stone, old cloth, ash/mud base, threshold variants, review-only cluster rows, material discipline, and LOD/collision planning.

The kit is static memory dressing only. Rows may describe how an abandoned hostile Giant cave-edge remnant reads visually, but they must not define encounter behavior, spawn marker behavior, damage/aura behavior, route scripting, cave trigger behavior, cave entrance gameplay marker behavior, cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI markers, objective markers, interaction behavior, readable signage, path widths as gameplay values, patrol logic, AI spaces, VFX/audio, DCC, FBX, Unreal, startup placement, final approval, or first implementation target selection.

Blood Axe cave remnant dressing must stay separate from neutral/civilized Giant culture. It may use rough highland stone, soot, ash, trampled mud, cave grit, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, and dull bone. It must not use refined Giant cave-town masonry, blue-gray civic stonework, terrace/waterwork forms, warm hearth identity, peaceful highland wayfinding, carved civic ornament, or restrained blue-rune culture as the default read.

Every row below is marked `package-ready; docs-only` or `reference-only`. No row creates or authorizes source assets, DCC, FBX, Unreal Content, runtime source, tools, validators, material instances, textures, VFX/audio, startup placement, source concept movement, final visual approval, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeCaveRemnantCluster_A01#Cairn_Remnant_A01` | Cairn | `SM_GIA_BloodAxeCaveRemnantCairn_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-329`. Low old cairn made from a few large stones with soot, ash, and optional restrained cloth. Static memory dressing only; no encounter behavior, spawn marker, route scripting, cave trigger, DCC, FBX, Unreal, startup placement, final approval, or first implementation target. |
| `BloodAxeCaveRemnantCluster_A01#Cairn_Collapsed_A01` | Cairn | `SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-339`. Collapsed or slumped cairn with shifted major stones and cold ash contact. Visual abandonment only; no destruction, physics, pickup, interaction, traversal proof, collision correctness, DCC, FBX, Unreal, or startup placement. |
| `BloodAxeCaveRemnantCluster_A01#LowStandingStone_Primary_A01` | Low standing stone | `SM_GIA_BloodAxeLowCaveStandingStone_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-339`. Short fractured standing stone sized below the tall standing-stone prop but still readable against female 442 cm and male 470 cm Giant baselines. Static territory memory only; no objective marker, readable text, damage/aura, route scripting, cave trigger, VFX, DCC, Unreal, or final approval. |
| `BloodAxeCaveRemnantCluster_A01#LowStandingStone_BrokenLean_A01` | Low standing stone | `SM_GIA_BloodAxeBrokenLeaningCaveStone_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-339`. Leaning or half-broken low slab with broad chipped planes and heavy mud contact. Static silhouette only; no destructible state, puzzle state, cave compatibility proof, traversal clearance, interaction behavior, DCC, FBX, Unreal, or startup placement. |
| `BloodAxeCaveRemnantCluster_A01#OldCloth_TiedWrap_A01` | Old cloth | `SM_GIA_BloodAxeOldCaveClothWrap_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-339`. Broad faded oxide red cloth tied around stone or trapped under a cairn rock. Static cloth accent only; no cloth physics, wind animation, UI marker, quest pointer, objective marker, VFX/audio, DCC, FBX, Unreal, or startup placement. |
| `BloodAxeCaveRemnantCluster_A01#OldCloth_DrapedScrap_A01` | Old cloth | `SM_GIA_BloodAxeDrapedCaveClothScrap_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-339`. Fixed old cloth scrap draped over a low stone or ash edge, with broad folds and frayed silhouette. Static cloth only; no simulation, material pulse, interaction affordance, readable signage, objective cue, DCC, Unreal, or final visual approval. |
| `BloodAxeCaveRemnantCluster_A01#AshMudBase_Primary_A01` | Ash/mud base | `SM_GIA_BloodAxeCaveAshMudBase_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-339`. Low irregular base of cold ash, soot, trampled mud, packed earth, and cave grit used to ground the cluster. Ground dressing only; no trigger area, damage field, aura, objective zone, route path, decal gameplay, collision claim, DCC, FBX, Unreal, or startup placement. |
| `BloodAxeCaveRemnantCluster_A01#AshMudBase_ColdFireScar_A01` | Ash/mud base | `SM_GIA_BloodAxeColdCaveFireScar_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-339`. Subtle cold fire-scar and mud-lip variant for an older abandoned remnant. Static visual history only; no active fire, torch state, VFX/audio, damage volume, interaction, resource pickup, DCC, Unreal, or final approval. |
| `BloodAxeCaveRemnantCluster_A01#ThresholdVariant_CairnStoneCloth_A01` | Threshold variants | `KIT_GIA_BloodAxeCaveRemnantThreshold_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-339`. Combined cairn, low stone, cloth, and ash base arranged as a compact cave-edge memory beat. Visual threshold only; no cave entrance gameplay marker, route scripting, nav/pathfinding, encounter lane, spawn marker, cave trigger, collision guarantee, DCC, Unreal, or final approval. |
| `BloodAxeCaveRemnantCluster_A01#ThresholdVariant_BrokenSlabPair_A01` | Threshold variants | `KIT_GIA_BloodAxeCaveBrokenSlabThreshold_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-349`. Pair of low broken slabs with an ash/mud base and restrained cloth. Static abandoned remnant only; no gate behavior, traversal proof, route validation, objective frame, interaction behavior, DCC, FBX, Unreal, or startup placement. |
| `BloodAxeCaveRemnantCluster_A01#ThresholdVariant_HalfBuriedStone_A01` | Threshold variants | `KIT_GIA_BloodAxeHalfBuriedCaveStoneCluster_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-349`. Half-buried marker stones and mud-sunk cloth for older cave-edge residue. Static age/readability beat only; no cave compatibility proof, nav blocker, cover rule, encounter setup, damage/aura, DCC, Unreal, or first implementation target. |
| `BloodAxeCaveRemnantCluster_A01#ReviewOnly_ClusterSilhouetteRows_A01` | Review-only cluster rows | `DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-349`. Non-shipping rows comparing cairn height, low standing-stone height, old cloth density, ash footprint, and cluster silhouette beside Giant baselines. No DCC, Unreal actor, validator, capture, startup placement, final visual approval, or implementation target. |
| `BloodAxeCaveRemnantCluster_A01#ReviewOnly_ScaleRows_A01` | Review-only cluster rows | `DOC_GIA_BloodAxeCaveRemnantClusterScaleRows_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-349`. Non-shipping scale rows showing remnant cluster variants beside female 442 cm and male 470 cm Giant baselines. No scale-lock change, shipped marker approval, DCC, FBX, Unreal, validator, capture, or startup placement. |
| `BloodAxeCaveRemnantCluster_A01#ReviewOnly_MaterialRestraintRows_A01` | Review-only cluster rows | `DOC_GIA_BloodAxeCaveRemnantClusterMaterialRows_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-349`. Non-shipping material restraint rows for rough highland stone, soot, ash, cave grit, trampled mud, oxide red cloth, rope, rawhide, blackened iron, old horn, and dull bone. Excludes neutral/civilized Giant culture, emissive, material instance creation, texture creation, VFX/audio, DCC, FBX, and Unreal. |
| `BloodAxeCaveRemnantCluster_A01#MaterialDiscipline_A01` | Material discipline | `DOC_GIA_BloodAxeCaveRemnantClusterMaterialDiscipline_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-349`. Shared material discipline for the cave-remnant child rows. Docs-only; no material instance, texture asset, material graph, VFX/audio, DCC, FBX, Unreal Content, or implementation target is created. |
| `BloodAxeCaveRemnantCluster_A01#LODCollisionPlanning_A01` | LOD/collision planning | `DOC_GIA_BloodAxeCaveRemnantClusterLODAndCollision_A01` | package-ready; docs-only | Package validated in `AET-MA-20260629-349`. Docs-only LOD0-LOD3 reduction order and disabled/simple collision policy for static remnant modules and review rows. No collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, objective volumes, validators, DCC, FBX, Unreal Content, or runtime implementation. |
| `BloodAxeCaveRemnantCluster_A01#Reference_CairnGuidepostDiscipline_A01` | Material and silhouette reference | `SM_GIA_BloodAxeRitualCairnGuidepost_A01` | reference-only | Use the cairn guidepost package as a restraint reference for few-large-stones construction, oxide red cloth restraint, and static memory read. This row does not create new assets, implementation order, DCC, FBX, Unreal, startup placement, or final approval. |
| `BloodAxeCaveRemnantCluster_A01#Reference_StandingStoneDiscipline_A01` | Material and silhouette reference | `SM_GIA_BloodAxeStandingStone_A01` | reference-only | Use the standing-stone package as a restraint reference for rough slab silhouette, base contact, Giant scale, and Blood Axe/neutral Giant separation. This row does not create new assets, implementation order, DCC, FBX, Unreal, startup placement, or final approval. |

## Dependency Notes

- `SK_GIA_Base_A01` owns Giant scale. This intake repeats the female 442 cm and male 470 cm baselines for marker scale comparison but does not change race scale, sockets, skeleton policy, collision capsules, or character proportions.
- `KIT_GIA_BloodAxeRitualStones_A01` owns the broader ritual-stone planning kit. This cave remnant cluster package is a child lane for static memory dressing only.
- `KIT_GIA_BloodAxeCaveApproachMarkers_A01` owns low threshold cairns, paired standing stones, cave remnant clusters, red cloth threshold markers, review rows, material discipline, and LOD/collision planning. This package narrows the cave remnant cluster row without approving cave gameplay or traversal.
- `SM_GIA_BloodAxeRitualCairnGuidepost_A01` owns single cairn guidepost discipline. Cave remnant cairns should read lower, older, and less waypoint-like.
- `SM_GIA_BloodAxeStandingStone_A01` owns tall standing-stone discipline. Cave remnant low standing stones should read shorter, partly broken, and cluster-bound.
- No row in this table is approved as a first DCC, FBX, Unreal, runtime, source asset, gameplay, final visual, final cave, or implementation target.

## Unordered Future Package Candidates

All cave-remnant child package, review, scale, material, and LOD/collision rows are package-ready at docs-only level. No first DCC target, source asset target, Unreal target, runtime target, gameplay target, or implementation target is selected by this intake.

## Approval Gates

- Stop before DCC source, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content asset, material instance, texture asset, material graph, import script, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, startup placement, or any source asset creation.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before selecting a first DCC, FBX, Unreal, source asset, runtime, gameplay, or implementation target from any row.
- Stop before encounter behavior, spawn marker behavior, patrol logic, AI spaces, damage values, aura behavior, route scripting, cave trigger behavior, cave entrance gameplay marker behavior, cave gameplay, traversal proof, path widths as gameplay values, nav/pathfinding, route validation, quest/UI markers, objective markers, interaction behavior, readable signage, UI arrows, cover rules, trap behavior, destructible behavior, loot, inventory, rewards, crafting, economy, resource behavior, salvage, pickup behavior, VFX, audio, cloth physics, or material-state animation.
- Stop before claiming collision correctness, cave compatibility, terrain integration, runtime performance validation, marker validation, final silhouette approval, final cave approval, final Blood Axe approval, final Giant culture approval, or final visual approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, VFX/audio asset, global index, task board, backlog, bootstrap, or unrelated package file.
- Rows cover cairn, low standing stone, old cloth, ash/mud base, threshold variants, review-only cluster rows, material discipline, and LOD/collision planning.
- Every row is marked `package-ready; docs-only` or `reference-only`; no row claims permission to proceed to DCC, FBX, Unreal, final approval, implementation, or first target selection.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Cave remnant cluster remains static memory dressing only.
- No encounter behavior, spawn marker behavior, damage/aura behavior, route scripting, cave trigger behavior, cave entrance gameplay marker behavior, cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI markers, objective markers, interaction behavior, readable signage, path widths as gameplay values, VFX/audio, DCC, FBX, Unreal, source asset creation, startup placement, or final visual approval is defined.
- Review-only rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, marker validation, camera approval, or final visual signoff.
- Materials use rough highland stone, soot, ash, trampled mud, cave grit, oxide red cloth, rope, rawhide, blackened iron, old horn, and dull bone consistently.
- Default emissive, glow, animated material states, gameplay VFX, UI-like markers, readable text, and neutral/civilized Giant language are absent and approval-gated.
- Tiny stone chips, cloth weave, fray, scratches, pitting, soot speckles, ash flecks, paint chips, horn rings, lichen, mud streaks, and rope fibers are assigned to textures or normals in future packages.
