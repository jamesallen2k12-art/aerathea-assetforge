# KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01 Child Asset Intake

## Source

- Parent kit: `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01`
- Parent route: `KIT_GIA_BloodAxeStrongholdApproach_A01#Review_CompositionMarkers`
- Source route reference: `BloodAxeStronghold.png#Review_CompositionMarkers` as split by the existing Blood Axe stronghold approach intake docs
- Related docs: `KIT_GIA_BloodAxeStrongholdApproach_A01`, `KIT_GIA_BloodAxeFormationDressing_A01`, `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeArmory_A01`, `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeTrophyGate_A01`, and `SM_GIA_BloodAxeWatchPlatform_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only child split complete for review composition marker planning; no child build target selected
- Scale dependency: validated `SK_GIA_Base_A01` female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: external source concepts remain in the external concept folder only. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This child intake splits the Blood Axe approach review marker kit into planning-only rows. The rows describe non-shipping review aids for height, scale, silhouette mass, gate framing, ground scale ticks, camera composition notes, material discipline, and future LOD/collision assumptions. They are not final visual approval, final stronghold approval, final gate approval, first DCC targets, first Unreal targets, terrain implementation, nav/pathfinding, encounter routes, AI spaces, destructible assets, gameplay systems, loot/crafting/economy/resource loops, validators, capture automation, startup-scene work, or implementation tickets.

Blood Axe approach marker language must stay separate from neutral/civilized Giant culture. It may reference rough cliffs, raw palisades, blackened iron, dark steel, chained scrap, scorched hide, soot, ash, packed earth, rough timber, oxide red cloth, and sparse non-graphic bone or horn warnings. It must not reuse civilized Giant cave-town, blue-gray masonry, terrace, waterwork, warm hearth, civic stoneworker, or restrained blue-rune language as the default read.

No row below creates or authorizes DCC source, FBX export, Unreal import, Unreal actor creation, validator creation, capture automation, startup scene edits, source asset creation, runtime source, source concept movement, final visual signoff, final stronghold approval, nav/pathfinding, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01#HeightRods_FemaleMaleBaselines` | Height rods | `SM_GIA_BloodAxeApproachHeightRod_A01` | Planning row ready | Non-shipping vertical rods for female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines, with optional range ghost marks for females 14-15 ft and males 14'10"-16'0". Visual scale review only; no shipped asset, collision, skeleton change, capsule change, or scale-lock change. |
| `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01#CliffSilhouetteBlocks` | Cliff silhouette blocks | `SM_GIA_BloodAxeApproachCliffSilhouetteBlock_A01` | Planning row ready | Broad proxy blocks for 1200-2600 cm cliff mass, overhang pressure, ledge steps, and gate-facing compression. Planning only; no terrain sculpt, landscape import, cliff mesh approval, HLOD, collision proxy, DCC, Unreal, or final silhouette approval. |
| `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01#PalisadeSilhouetteBlocks` | Palisade silhouette blocks | `SM_GIA_BloodAxeApproachPalisadeSilhouetteBlock_A01` | Planning row ready | Simplified 700-1100 cm raw-log wall skyline blocks with uneven spike crowns, brace mass, and gate-flank pressure. Visual proxy only; no final palisade mesh, destructible wall, cover rule, nav blocker, DCC, Unreal, or startup placement. |
| `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01#GateFrameThumbnails` | Gate-frame thumbnails | `DOC_GIA_BloodAxeApproachGateFrameThumbnails_A01` | Planning row ready | Docs-only thumbnails showing how cliff mass, palisade blocks, ground ticks, and scale rods frame a future gate. Does not approve final gate art, final stronghold art, entry behavior, interaction, lock, collision, nav link, capture, or review-scene placement. |
| `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01#GroundTicks` | Ground ticks | `SM_GIA_BloodAxeApproachGroundTick_A01` | Planning row ready | Low-profile 100 cm, 250 cm, and 500 cm visual interval ticks for scale readability on approach sheets. Values are visual only and must not become nav spacing, spawn spacing, patrol spacing, combat range, collision, or traversal rules. |
| `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01#ScaleRods` | Scale rods | `SM_GIA_BloodAxeApproachScaleRod_A01` | Planning row ready | Neutral 1 m, 5 m, 10 m, Giant shoulder, Giant head, female baseline, and male baseline rods for production scale comparison. Review-only; no shipped measuring prop, gameplay marker, UI label, world scale change, or capsule/skeleton edit. |
| `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01#CameraCompositionNotes` | Camera-composition notes | `DOC_GIA_BloodAxeApproachCameraComposition_A01` | Planning row ready | Docs-only framing notes for full approach, cliff pressure, palisade skyline, gate-facing compression, and ground tick visibility. No camera actor, camera director change, capture script, startup scene, validation marker pass, screenshot approval, or final visual signoff. |
| `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01#MaterialDisciplineMarkers` | Material discipline markers | `DOC_GIA_BloodAxeApproachMaterialDisciplineMarkers_A01` | Planning row ready | Swatch and marker notes for fractured rock, packed earth, raw timber, blackened iron, dark steel, chained scrap, scorched hide, soot, ash, oxide red cloth, and sparse non-graphic bone/horn warnings. No material instances, texture assets, source concepts, or final shader decisions are created. |
| `KIT_GIA_BloodAxeApproachReviewCompositionMarkers_A01#LODCollisionPlanning` | LOD and collision planning | `DOC_GIA_BloodAxeApproachReviewLODAndCollision_A01` | Planning row ready | Docs-only LOD0-LOD3 planning and collision-disabled policy for future non-shipping rods, blocks, thumbnails, ticks, frames, and cards. No collision proxies, nav blockers, gameplay volumes, validators, runtime checks, Unreal import, or implementation files are created. |

## Dependency Notes

- `SK_GIA_Base_A01` owns Giant scale, skeleton policy, capsule expectations, body proportions, and future character collision assumptions.
- `KIT_GIA_BloodAxeStrongholdApproach_A01` owns the parent approach split and lists this package as the review composition marker row.
- `KIT_GIA_BloodAxeFormationDressing_A01` owns the broader non-gameplay formation marker language: height rods, ground ticks, camera frames, and review composition planning.
- `KIT_GIA_BloodAxeCamp_A01`, `SM_GIA_BloodAxeCampGate_A01`, and `SM_GIA_BloodAxeTrophyGate_A01` own camp and gate planning. This intake only frames future review thumbnails and does not approve gate art or gate behavior.
- `KIT_GIA_BloodAxeArmory_A01` owns Blood Axe weapon, banner, shield, chained scrap, and reforged material language referenced by material discipline markers.
- No row in this table is approved as a first DCC, Unreal, runtime, source asset, gameplay, final visual, final stronghold, validator, capture, startup-scene, or implementation target.

## Immediate Package Priority

The kit-level production package and this child intake are ready for docs-only planning review. No first implementation target is selected by this intake.

Later docs-only lanes, if requested by a new task:

- Expand `#GateFrameThumbnails` into a tighter A/B/C thumbnail planning sheet for cliff, palisade, and gate-facing compression.
- Expand `#MaterialDisciplineMarkers` into a standalone docs-only material discipline packet if Blood Axe approach packages start drifting toward neutral/civilized Giant culture.
- Expand `#LODCollisionPlanning` only as documentation for future review proxies, not as validator, collision, or Unreal work.

## Approval and Stop Gates

- Stop before Unreal actor creation, validator creation, capture automation, startup scene work, final visual signoff, nav/pathfinding, DCC, FBX, Unreal import, source concept movement, final stronghold approval, or first implementation target selection.
- Stop before any DCC source, Blender file, terrain sculpt, mesh, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material instance, texture asset, import script, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, or startup placement work.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before defining nav/pathfinding, traversal proofs, climb logic, path widths as gameplay values, encounter design, AI groups, patrol routes, spawn logic, perception, damage values, projectile behavior, cover rules, gate interaction, destructible behavior, objective logic, loot, inventory, rewards, crafting, economy, resource behavior, salvage, pickup behavior, VFX, audio, or interaction behavior.
- Stop before claiming collision correctness, HLOD implementation, terrain integration, gate compatibility, camera-capture approval, marker validation, runtime performance validation, final silhouette approval, final visual approval, or final stronghold approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Child rows are planning-only and do not define final stronghold approval, final visual approval, final gate approval, implementation targets, terrain work, nav paths, encounter routes, AI spaces, destructible assets, gameplay systems, loot, crafting, economy, resource loops, validators, capture automation, startup scene, or Unreal actors.
- Rows cover height rods, cliff silhouette blocks, palisade silhouette blocks, gate-frame thumbnails, ground ticks, scale rods, camera-composition notes, material discipline markers, and LOD/collision planning rows.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5", with approved Giant ranges of females 14-15 ft and males 14'10"-16'0".
- Blood Axe remains a hostile Giant sub-faction, not default Giant culture.
- No source concept files are copied, moved, edited, embedded, cropped, renamed, inspected for final approval, or committed.
- No DCC, FBX, Unreal Content, runtime source, validators, capture automation, startup placements, global indexes, task-board changes, backlog changes, bootstrap changes, AI, combat stats, abilities, loot, crafting, economy, patrol logic, spawn logic, nav/pathfinding, destructible behavior, final visual approval, final stronghold approval, or first build target is claimed.
- Primary approach review read stays clear at MMO camera distance: validated Giant height rods, cliff mass, rough palisade skyline, gate-frame compression, ground ticks, scale rods, camera note frames, and Blood Axe material discipline.
- Materials use fractured rock, packed earth, raw timber, blackened iron, dark steel, chained scrap, scorched hide, soot, ash, oxide red cloth, and sparse non-graphic bone or horn warnings consistently.
- Default emissive, animated material states, gameplay VFX, UI-like route markers, readable tactical text, final gate approval, and neutral/civilized Giant stoneworker language are absent and approval-gated where applicable.
