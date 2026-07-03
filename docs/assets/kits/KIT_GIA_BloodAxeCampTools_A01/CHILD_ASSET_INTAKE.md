# KIT_GIA_BloodAxeCampTools_A01 Child Asset Intake

## Source

- Parent planning row: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md` entry `BloodAxeCamp.png#Clutter_ToolBucketRopeCoils`
- Source references recorded in existing camp intake docs: `BloodAxeCamp.png`, `BloodAxecamp.png`, `Blood Axe Village.png`, `BloodAxeGate.png`, `BloodAxeForge.png`, `BloodAxeShelter.png`, `BloodAxeShamanHut.png`, and `BloodAxeStronghold.png`
- Related package: `KIT_GIA_BloodAxeBowyerTools_A01`, for specialized bowyer workshop tools
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only planning child breakdown ready
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture
- Scale dependency: validated `SK_GIA_Base_A01` female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: source concepts remain in the external concept folder only. Do not copy, move, edit, embed, inspect for visual approval, or commit source images for this docs-only package.

## Notes

This intake splits Blood Axe camp tools into planning-only child rows. The rows cover tool buckets, rope coils, hooks, wedges, mallets, tie hardware, camp utility clusters, and review composition rows so later workers can create child packages without treating the camp clutter board as one final asset.

Blood Axe camp-tool dressing must stay separate from neutral/civilized Giant culture. It may use rough timber, thick rope, blackened iron, dark steel, hide lashings, scorched leather, soot, ash, mud, grime, dull red cloth ties, chipped red paint, and sparse non-graphic bone or horn. It must not use civilized Giant cave-town masonry, blue-gray stoneworker craft, warm hearth presentation, refined highland tools, peaceful terrace language, restrained blue runes, or neutral Giant civic identity as the default read.

This intake does not select a first DCC target, approve final visual art, create source folders, create FBX exports, create Unreal Content, place startup actors, define usable workstation behavior, define tool pickup behavior, define crafting/resource/economy behavior, define interaction behavior, define NPC work loops, define nav/pathfinding behavior, or define runtime gameplay.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeCamp.png#CampTools_ToolBucket_Open_A01` | Tool buckets | `SM_GIA_BloodAxeToolBucket_A01` | Package-ready; docs-only | Oversized open bucket or battered carry tub, 90-180 cm diameter, with thick rim, crude handle, soot-stained boards or blackened metal panels, and a few large visible tool handles. Static display only; no inventory, pickup, loot, workstation, or interaction behavior. |
| `BloodAxecamp.png#CampTools_ToolBucket_IronRim_A01` | Tool buckets | `SM_GIA_BloodAxeIronRimToolBucket_A01` | Package-ready; docs-only | Heavier bucket variant with dark iron rim, hide handle wrap, red cloth tie, and sparse dents for gate, shelter, or forge support dressing. No storage contents, vendor use, resource data, or economy data. |
| `BloodAxeForge.png#CampTools_CarryTub_A01` | Tool buckets | `SM_GIA_BloodAxeCarryTub_A01` | Package-ready; docs-only | Low rectangular or oval carry tub for wedges, rope, and hooks, scaled for female 442 cm and male 470 cm Giants. Visual clutter only; not a resource crate or usable container. |
| `BloodAxeCamp.png#CampTools_RopeCoil_Large_A01` | Rope coils | `SM_GIA_BloodAxeRopeCoil_A01` | Package-ready; docs-only | Thick 120-260 cm diameter coil with broad rope turns, large knot, muddy underside, and hide tie. Static mesh only; no rope physics, tripwire, climbing, pickup, or nav behavior. |
| `BloodAxeGate.png#CampTools_RopeCoil_TieDown_A01` | Rope coils | `SM_GIA_BloodAxeTieDownRopeCoil_A01` | Package-ready; docs-only | Rope coil with heavy tie loop, ring, or stake anchor for gates, shelters, and banner lines. Visual tie-down language only; no interaction, trap, pathfinding, or gate behavior. |
| `Blood Axe Village.png#CampTools_RopeBundle_Spare_A01` | Rope coils | `KIT_GIA_BloodAxeRopeBundleSet_A01` | Package-ready; docs-only | Small set of spare coils, tied lengths, and thick knots for repeated camp dressing. Texture fibers and fray; do not model dense micro-strands. |
| `BloodAxeCamp.png#CampTools_HeavyHookSet_A01` | Hooks | `SM_GIA_BloodAxeHeavyHookSet_A01` | Package-ready; docs-only | Large blackened iron S-hooks, wall hooks, and loose tie-down hooks, 70-180 cm long, with strong curved silhouettes and restrained red cloth tags. No tool pickup, weapon use, trap use, or interaction volume. |
| `BloodAxeGate.png#CampTools_StakeHook_A01` | Hooks | `SM_GIA_BloodAxeStakeHook_A01` | Package-ready; docs-only | Ground or wall stake hook with crude mounting plate, hammered ring, and mud-dark base for gate or shelter utility dressing. Static display only; no collision gameplay or nav blocker definition. |
| `BloodAxeShelter.png#CampTools_HangingHookRail_A01` | Hooks | `SM_GIA_BloodAxeHangingHookRail_A01` | Package-ready; docs-only | Short rail with sparse oversized hooks for shelter-edge dressing. Related to camp tools, not bowyer tool racks; no hanging physics, usable rack, pickup, or workstation behavior. |
| `BloodAxeCamp.png#CampTools_WedgeSet_A01` | Wedges | `SM_GIA_BloodAxeWedgeSet_A01` | Package-ready; docs-only | Blunt splitting wedges and chock blocks, 50-140 cm long, with broad triangular profiles, chipped edges, and stacked or loose variants. No harvest node, crafting ingredient, or destructible setup. |
| `BloodAxeForge.png#CampTools_IronWedgeStack_A01` | Wedges | `SM_GIA_BloodAxeIronWedgeStack_A01` | Package-ready; docs-only | Dark metal wedge stack with soot, ash, chipped red paint, and broad readable forms for forge-adjacent utility. Static dressing only; no resource behavior, salvage behavior, or economy behavior. |
| `BloodAxeStronghold.png#CampTools_ChockBlocks_A01` | Wedges | `SM_GIA_BloodAxeChockBlockSet_A01` | Package-ready; docs-only | Heavy wood or metal chock blocks for barricade, wagon, or gate dressing. Visual support props only; no physics constraint, gate logic, or destructible behavior. |
| `BloodAxeCamp.png#CampTools_Mallet_Heavy_A01` | Mallets | `SM_GIA_BloodAxeMallet_A01` | Package-ready; docs-only | Giant-scale mallet, 140-260 cm long, with heavy wood or iron-banded head, long handle, hide wrap, and soot grime. Display prop only; no weapon trace, pickup, tool use, crafting loop, or animation behavior. |
| `BloodAxeForge.png#CampTools_Mallet_Sledge_A01` | Mallets | `SM_GIA_BloodAxeSledgeMallet_A01` | Package-ready; docs-only | Heavier forge-adjacent mallet with rectangular head, dark bands, and worn handle. Related to camp utility, not a usable forge station or combat weapon. |
| `BloodAxeShelter.png#CampTools_MalletPair_A01` | Mallets | `SM_GIA_BloodAxeMalletPair_A01` | Package-ready; docs-only | Two mallets crossed or leaned against a bucket or wall, kept sparse for shelter-edge dressing. No skeletal attachment, pickup behavior, or NPC work loop. |
| `BloodAxeCamp.png#CampTools_TieHardware_A01` | Tie hardware | `KIT_GIA_BloodAxeTieHardware_A01` | Package-ready; docs-only | Oversized rings, pegs, short chain lengths, latch plates, and hide ties that support buckets, rope coils, hooks, and clusters. Secondary detail only; no per-link collision or interaction behavior. |
| `BloodAxeGate.png#CampTools_RingPegSet_A01` | Tie hardware | `SM_GIA_BloodAxeRingPegSet_A01` | Package-ready; docs-only | Ground pegs and ring anchors for camp perimeter visual dressing. Static mesh only; no rope simulation, physics constraint, nav blocker, trap, or objective logic. |
| `BloodAxeCamp.png#CampTools_UtilityCluster_Small_A01` | Camp utility clusters | `SM_GIA_BloodAxeCampUtilityCluster_A01` | Package-ready; docs-only | Low 250-600 cm wide cluster combining one bucket, one rope coil, two or three wedges, one mallet, and sparse hooks with clear spacing. Non-interactive set dressing only. |
| `Blood Axe Village.png#CampTools_UtilityCluster_PathEdge_A01` | Camp utility clusters | `SM_GIA_BloodAxePathEdgeUtilityCluster_A01` | Package-ready; docs-only | Path-edge clutter cluster with low profile, mud-dark base, rope, wedges, and red cloth tie, designed to preserve Giant-scale visual lanes. No nav/pathfinding, collision-proxy, startup placement, or encounter behavior. |
| `BloodAxeForge.png#CampTools_UtilityCluster_ForgeSupport_A01` | Camp utility clusters | `SM_GIA_BloodAxeForgeSupportUtilityCluster_A01` | Package-ready; docs-only | Forge support cluster using bucket, iron wedges, mallet, hooks, and ring pegs. Visual only; no heat gameplay, crafting/resource/economy behavior, VFX, material graph, or usable workstation behavior. |
| `BloodAxeShelter.png#CampTools_UtilityCluster_ShelterEdge_A01` | Camp utility clusters | `SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01` | Package-ready; docs-only | Shelter-edge cluster with rope coil, hanging hook rail, bucket, and mallet pair. No shelter interaction, NPC routine, pickup behavior, cloth physics, or startup actor. |
| `BloodAxeCamp.png#Review_CompositionRows_A01` | Review composition rows | `DOC_GIA_BloodAxeCampToolsReviewRows_A01` | Package-ready; docs-only | Docs-only row describing bucket/coil/hook/wedge/mallet spacing, silhouette density, cluster rhythm, and MMO camera readability. No Unreal actor, validator, capture automation, startup placement, or final visual signoff. |
| `BloodAxeCamp.png#Review_ScaleRows_A01` | Review composition rows | `DOC_GIA_BloodAxeCampToolsScaleRows_A01` | Package-ready; docs-only | Non-shipping scale rows for female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines beside buckets, coils, hooks, wedges, mallets, and clusters. No scale-lock change or shipped marker approval. |
| `BloodAxeCamp.png#Review_LODCollisionRows_A01` | Review composition rows | `DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01` | Package-ready; docs-only | Docs-only LOD0-LOD3 and collision-limit rows for buckets, coils, hooks, wedges, mallets, tie hardware, and utility clusters. No collision proxies, validators, nav blockers, gameplay volumes, or startup work are created. |
| `BloodAxeCamp.png#Review_MaterialDisciplineRows_A01` | Review composition rows | `DOC_GIA_BloodAxeCampToolsMaterialRows_A01` | Package-ready; docs-only | Shared material discipline row for blackened iron, dark steel, scorched timber, rope, hide, leather, soot, ash, mud, dull red ties, and sparse non-graphic bone or horn. Explicitly excludes neutral/civilized Giant cave-town materials and default emissive. |

## Dependency Notes

- `KIT_GIA_BloodAxeBowyerTools_A01` owns specialized bow-making and repair equipment such as clamps, draw knives, stringing frame, glue pot, measuring jig, rasp, blade scraper, tool rack, and repair bench pieces. This camp-tools intake owns general camp utility clutter only.
- `KIT_GIA_BloodAxeBannerLine_A01` may use related rope and tie language, but this intake does not define banner animation, cloth simulation, faction buff behavior, morale behavior, or AI behavior.
- `KIT_GIA_BloodAxeForgeScrapSorting_A01` and `SM_GIA_BloodAxeAnvilQuench_A01` own forge sorting and forge station dressing. This intake can provide small support clusters but does not define heat, crafting, resource, economy, workstation, material graph, or interaction behavior.
- `KIT_GIA_BloodAxePathMarkers_A01` owns route-marker language. Camp tools may sit near paths, but they do not define waypoints, objective logic, nav/pathfinding behavior, pickup behavior, loot behavior, or startup placement.

## Immediate Package Priority

The kit-level package and all child package rows are package-ready at docs-only level after `AET-MA-20260629-439` validation. They are not implementation approvals.

No first DCC target is selected by this intake.

## Approval Gates

- Stop before any DCC source, sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material instance, texture asset, validator, runtime source, Blueprint, socket authoring, physics setup, animation asset, VFX, audio, or startup placement work.
- Stop before copying, moving, editing, embedding, inspecting for visual approval, or committing external source concepts.
- Stop before final camp-tools visual approval or first playable visual approval.
- Stop before selecting a first DCC target.
- Stop before usable workstation behavior, tool pickup behavior, crafting behavior, resource behavior, economy behavior, salvage behavior, vendor behavior, inventory behavior, loot behavior, interaction behavior, quest behavior, NPC work loops, nav/pathfinding behavior, encounter behavior, cover behavior, damage behavior, destructible behavior, objective logic, rope physics, cloth physics, or hanging secondary motion.
- Stop if Blood Axe visual language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock or socket assumptions from `SK_GIA_Base_A01`.

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, or bootstrap file.
- Child rows cover tool buckets, rope coils, hooks, wedges, mallets, tie hardware, camp utility clusters, and review composition rows.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Rows are useful for future package planning without selecting a first DCC target.
- No usable workstation behavior, tool pickup behavior, crafting/resource/economy behavior, interaction behavior, nav/pathfinding behavior, startup placement, or runtime gameplay is defined.
- Review composition rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, collision proxies, or final visual signoff.
- Materials use blackened iron, dark steel, rough timber, thick rope, hide, scorched leather, soot, ash, mud, dull red cloth ties, chipped red paint, and sparse non-graphic bone or horn consistently.
- Default emissive, forge glow, ritual glow, magic glow, UI-like markers, quest markers, loot beams, readable text, and neutral/civilized Giant language are absent and approval-gated.
- Tiny rope fibers, cloth weave, fray, stitches, rivets, scratches, pitting, soot speckles, ash flecks, paint chips, wood grain, mud flecks, and leather stitching are assigned to textures or normals in future packages.
