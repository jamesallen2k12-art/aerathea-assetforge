# KIT_GIA_BloodAxeStandingStoneRing_A01 Child Asset Intake

## Source

- Parent package: `KIT_GIA_BloodAxeRitualStones_A01`
- Current package: `KIT_GIA_BloodAxeStandingStoneRing_A01`
- Related docs: `SM_GIA_BloodAxeStandingStone_A01` and `SK_GIA_Base_A01`
- Task: `AET-MA-20260629-178`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only planning child breakdown; no row may proceed to DCC, FBX, Unreal, startup placement, final ring approval, or first implementation target selection
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture
- Scale dependency: Giant scale lock from `SK_GIA_Base_A01` uses female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline; approved Giant ranges remain females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: external source concepts remain external. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This intake splits `KIT_GIA_BloodAxeStandingStoneRing_A01` into planning-only child rows for tall anchor stones, secondary stones, broken/fallen stones, partial ring arcs, ring-gap variants, review rows, material discipline, and LOD/collision planning.

Keep standing-stone rings as inactive warning and memory circles only, not gameplay arenas. These rows are static worldbuilding and visual territory memory, not ritual gameplay. They must not define final ring approval, VFX/audio, objective markers, encounter behavior, aura/damage behavior, quest/UI markers, readable rune text, navigation/pathfinding, collision correctness, interaction behavior, DCC, FBX, Unreal, startup placement, or first implementation target selection.

Blood Axe standing-stone dressing must stay separate from neutral/civilized Giant culture. It may use rough highland stone, soot, ash, trampled mud, rawhide, rope, oxide red cloth, blackened iron, sparse old horn, and dull bone. It must not reuse civilized Giant cave-town masonry, blue-gray civic stonework, terrace/waterwork forms, warm hearth identity, refined stoneworker craft language, peaceful highland wayfinding, or restrained blue-rune culture as the default read.

Every row below is marked `package-needed` or `planned`. No row creates or authorizes DCC source, FBX export, Unreal Content, runtime source, tools, validators, material instances, textures, VFX/audio, startup placement, source concept movement, final visual approval, final ring approval, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeStandingStoneRing_A01#TallAnchorStones_A01` | Tall anchor stones | `SM_GIA_BloodAxeRingAnchorStone_A01` | package-needed | Dominant upright slabs, 420-850 cm high, with fractured crowns, heavy lean, base chock stones, and restrained Blood Axe accents. Static warning and memory circle read only; no ritual gameplay, VFX/audio, objective markers, aura/damage behavior, nav/pathfinding, collision correctness, DCC, FBX, Unreal, startup placement, or final ring approval. |
| `BloodAxeStandingStoneRing_A01#TallAnchorStones_Leaning_A01` | Tall anchor stones | `SM_GIA_BloodAxeRingLeaningAnchorStone_A01` | planned | Leaning anchor variant for irregular ring rhythm and old camp memory. No physics, collapse state, destructible behavior, interaction prompt, pathing proof, DCC, FBX, Unreal, or first implementation target selection. |
| `BloodAxeStandingStoneRing_A01#TallAnchorStones_Bound_A01` | Tall anchor stones | `SM_GIA_BloodAxeRingBoundAnchorStone_A01` | planned | Anchor stone with broad rawhide lashings, one static oxide red cloth strip, and optional blackened iron clamp. No cloth simulation, VFX/audio, readable rune text, quest/UI marker, material instance creation, DCC, FBX, Unreal, or final approval. |
| `BloodAxeStandingStoneRing_A01#SecondaryStones_A01` | Secondary stones | `SM_GIA_BloodAxeRingSecondaryStone_A01` | package-needed | Medium upright stones, 180-460 cm high, for uneven circle rhythm. Static dressing only; no arena boundary, nav blocker, objective area, aura/damage behavior, ritual gameplay, collision correctness, DCC, FBX, Unreal, or startup placement. |
| `BloodAxeStandingStoneRing_A01#SecondaryStones_LowPair_A01` | Secondary stones | `SM_GIA_BloodAxeRingLowStonePair_A01` | planned | Paired low stones that imply a broken ring beat without forming a functional gate. No traversal guarantee, navigation/pathfinding, objective marker, interaction behavior, DCC, FBX, Unreal, or first implementation target selection. |
| `BloodAxeStandingStoneRing_A01#SecondaryStones_ChockBase_A01` | Secondary stones | `SM_GIA_BloodAxeRingChockBaseStone_A01` | planned | Secondary stone with 2-4 large chock stones and embedded mud/ash base. Planning only; no collision proxy, collision correctness, DCC, FBX, Unreal, startup placement, or final visual approval. |
| `BloodAxeStandingStoneRing_A01#BrokenUprightStones_A01` | Broken/fallen stones | `SM_GIA_BloodAxeRingBrokenUprightStone_A01` | package-needed | Snapped standing remnant with chipped crown and soot-stained fractures. Static age and abandonment read only; no destructible state, damage volume, ritual activation, VFX/audio, DCC, FBX, Unreal, or final ring approval. |
| `BloodAxeStandingStoneRing_A01#FallenStones_A01` | Broken/fallen stones | `SM_GIA_BloodAxeRingFallenStone_A01` | package-needed | Heavy fallen slab partly sunk into ash, mud, and dry grass to break ring continuity. No physics fall, collision correctness, path-width proof, gameplay cover rule, interaction behavior, DCC, FBX, Unreal, or startup placement. |
| `BloodAxeStandingStoneRing_A01#CollapsedCluster_A01` | Broken/fallen stones | `KIT_GIA_BloodAxeRingCollapsedStoneCluster_A01` | planned | Small collapsed section with broken upright, fallen slab, and scattered large chock stones. Visual memory only; no nav blocker, objective area, encounter boundary, damage/aura behavior, DCC, FBX, Unreal, or final approval. |
| `BloodAxeStandingStoneRing_A01#PartialArc_ThreeStone_A01` | Partial ring arcs | `KIT_GIA_BloodAxePartialStandingStoneArc_A01` | package-needed | Three-to-five-stone arc module for old warning circle reads without completing a full arena. No ritual gameplay, nav/pathfinding, objective marker, VFX/audio, collision correctness, DCC, FBX, Unreal, startup placement, or first implementation target selection. |
| `BloodAxeStandingStoneRing_A01#PartialArc_Broad_A01` | Partial ring arcs | `KIT_GIA_BloodAxeBroadStandingStoneArc_A01` | planned | Wider 6-9 stone arc for highland camp perimeter memory. Planning only; no combat arena, patrol lane, spawn logic, quest marker, navigation/pathfinding, DCC, FBX, Unreal, or final ring approval. |
| `BloodAxeStandingStoneRing_A01#PartialArc_Asymmetric_A01` | Partial ring arcs | `KIT_GIA_BloodAxeAsymmetricStoneArc_A01` | planned | Asymmetric arc with one tall anchor, several secondary stones, and one fallen slab for MMO camera readability. No VFX/audio, ritual boundary, interaction, objective marker, DCC, FBX, Unreal, or startup placement. |
| `BloodAxeStandingStoneRing_A01#RingGap_OpenBreak_A01` | Ring-gap variants | `KIT_GIA_BloodAxeStandingStoneRingGap_A01` | package-needed | Deliberate open gap that makes the circle read inactive and broken. Visual composition only; no traversal proof, pathfinding guarantee, invisible blocker, objective entry, ritual gameplay, DCC, FBX, Unreal, or final approval. |
| `BloodAxeStandingStoneRing_A01#RingGap_CollapsedBreak_A01` | Ring-gap variants | `KIT_GIA_BloodAxeCollapsedRingGap_A01` | planned | Gap filled by fallen slab and ash/mud berm for abandoned memory. No collision correctness, nav blocker, damage/aura behavior, encounter logic, DCC, FBX, Unreal, startup placement, or first implementation target selection. |
| `BloodAxeStandingStoneRing_A01#RingGap_MissingStones_A01` | Ring-gap variants | `KIT_GIA_BloodAxeMissingStoneRingGap_A01` | planned | Missing-stone gap with disturbed ground contact and no UI-like pointer shape. No quest/UI marker, objective marker, navigation/pathfinding, ritual activation, VFX/audio, DCC, FBX, Unreal, or final ring approval. |
| `BloodAxeStandingStoneRing_A01#ReviewRows_RingRhythm_A01` | Review rows | `DOC_GIA_BloodAxeStandingStoneRingReviewRows_A01` | planned | Non-shipping rows comparing anchor height, secondary stone rhythm, broken/fallen interruption, partial arcs, and ring-gap readability beside female 442 cm and male 470 cm Giant baselines. No Unreal actor, validator, capture, startup placement, final visual approval, or first implementation target selection. |
| `BloodAxeStandingStoneRing_A01#ReviewRows_BloodAxeSeparation_A01` | Review rows | `DOC_GIA_BloodAxeStandingStoneRingCultureSeparationRows_A01` | planned | Non-shipping art-direction rows proving Blood Axe hostile Giant sub-faction language stays separate from neutral/civilized Giant culture. No final culture approval, DCC, FBX, Unreal, global index update, startup placement, or source concept movement. |
| `BloodAxeStandingStoneRing_A01#ReviewRows_ScaleComparison_A01` | Review rows | `DOC_GIA_BloodAxeStandingStoneRingScaleRows_A01` | planned | Non-shipping scale rows for tall anchor, secondary, broken, fallen, arc, and gap variants against the Giant baselines. No scale-lock change, collision correctness, nav/pathfinding, DCC, FBX, Unreal, or final approval. |
| `BloodAxeStandingStoneRing_A01#MaterialDiscipline_A01` | Material discipline | `DOC_GIA_BloodAxeStandingStoneRingMaterialDiscipline_A01` | planned | Shared material discipline for rough highland stone, soot, ash, trampled mud, rawhide, rope, oxide red cloth, blackened iron, sparse old horn, and dull bone. Excludes neutral/civilized Giant culture, default emissive, texture creation, material instance creation, VFX/audio, DCC, FBX, and Unreal. |
| `BloodAxeStandingStoneRing_A01#MaterialDiscipline_NoGlow_A01` | Material discipline | `DOC_GIA_BloodAxeStandingStoneRingNoGlowPolicy_A01` | planned | Non-shipping policy row confirming no ritual glow, shamanic glow, signal glow, animated material state, readable magic diagram, or emissive default. No VFX/audio, material graph authoring, Unreal, DCC, or final visual approval. |
| `BloodAxeStandingStoneRing_A01#LODCollisionPlanning_A01` | LOD/collision planning | `DOC_GIA_BloodAxeStandingStoneRingLODAndCollision_A01` | planned | Docs-only LOD0-LOD3 reduction order and disabled/simple collision policy for future static stone modules and review rows. No collision proxies, nav blockers, gameplay volumes, damage volumes, aura volumes, objective volumes, validators, DCC, FBX, Unreal Content, or runtime implementation. |
| `BloodAxeStandingStoneRing_A01#LODCollisionPlanning_GapPolicy_A01` | LOD/collision planning | `DOC_GIA_BloodAxeStandingStoneRingGapCollisionPolicy_A01` | planned | Policy note that ring gaps are visual breaks, not route proofs, smart links, nav gates, invisible blockers, or objective entrances. No nav/pathfinding, collision correctness, DCC, FBX, Unreal, or startup placement. |

## Dependency Notes

- `KIT_GIA_BloodAxeRitualStones_A01` owns the broader ritual-stone planning split. This standing-stone ring kit only owns inactive warning and memory circle planning.
- `SM_GIA_BloodAxeStandingStone_A01` owns the single standing-stone prop language that future anchor and secondary stones should derive from without claiming implementation.
- `SK_GIA_Base_A01` owns Giant scale. This intake does not change female 442 cm / 14'6" and male 470 cm / 15'5" baselines.
- `KIT_GIA_BloodAxeCairnGuideposts_A01`, `KIT_GIA_BloodAxeRitualBannerPoles_A01`, and future cave approach markers may sit near a ring in later composition planning, but this intake does not approve their placement, behavior, navigation/pathfinding, collision correctness, VFX/audio, DCC, FBX, Unreal, or startup integration.
- No row in this table is approved as a first DCC, Unreal, runtime, source asset, gameplay, final visual, final ring approval, or implementation target.

## Unordered Future Package Candidates

No first DCC target, source asset target, Unreal target, runtime target, or implementation target is selected by this intake. If a later lead-approved package lane is opened, these may be promoted independently:

- `SM_GIA_BloodAxeRingAnchorStone_A01`
- `SM_GIA_BloodAxeRingSecondaryStone_A01`
- `SM_GIA_BloodAxeRingBrokenUprightStone_A01`
- `SM_GIA_BloodAxeRingFallenStone_A01`
- `KIT_GIA_BloodAxePartialStandingStoneArc_A01`
- `KIT_GIA_BloodAxeStandingStoneRingGap_A01`
- `DOC_GIA_BloodAxeStandingStoneRingReviewRows_A01`
- `DOC_GIA_BloodAxeStandingStoneRingCultureSeparationRows_A01`
- `DOC_GIA_BloodAxeStandingStoneRingScaleRows_A01`
- `DOC_GIA_BloodAxeStandingStoneRingMaterialDiscipline_A01`
- `DOC_GIA_BloodAxeStandingStoneRingNoGlowPolicy_A01`
- `DOC_GIA_BloodAxeStandingStoneRingLODAndCollision_A01`

## Approval Gates

- Stop before DCC source, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content asset, material instance, texture asset, material graph, import script, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, startup placement, or any source asset creation.
- Stop before copying, moving, editing, embedding, cropping, renaming, inspecting for final approval, or committing any external source concept.
- Stop before selecting a first DCC, Unreal, source asset, runtime, gameplay, or implementation target from any row.
- Stop before final ring approval, ritual gameplay, arena behavior, offering mechanics, activation states, readable rune text, objective markers, quest/UI symbols, waypoint logic, trail-marker gameplay, navigation/pathfinding, traversal proofs, path widths as gameplay values, encounter design, AI spaces, patrol routes, spawn logic, perception, damage values, aura behavior, aura/damage behavior, projectile behavior, cover rules, trap behavior, destructible behavior, loot, inventory, rewards, crafting, economy, resource behavior, salvage, pickup behavior, VFX/audio, or interaction behavior.
- Stop before claiming collision correctness, terrain integration, cave compatibility, runtime performance validation, marker validation, final silhouette approval, final Blood Axe ritual approval, final visual approval, or final ring approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5", or the approved Giant ranges of females 14-15 ft and males 14'10"-16'0".

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, VFX/audio asset, global index, task board, backlog, bootstrap, or unrelated package file.
- Rows cover tall anchor stones, secondary stones, broken/fallen stones, partial ring arcs, ring-gap variants, review rows, material discipline, and LOD/collision planning.
- Every row is marked `package-needed` or `planned`; no row claims permission to proceed to DCC, FBX, Unreal, final approval, implementation, or first implementation target selection.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Standing-stone rings remain inactive warning and memory circles only, not gameplay arenas.
- No final ring approval, ritual gameplay, VFX/audio, collision correctness, nav/pathfinding, objective markers, aura/damage behavior, quest/UI markers, readable rune text, interaction behavior, pickup/loot behavior, resource/crafting/economy behavior, cloth physics, animation, DCC, FBX, Unreal, source asset creation, startup placement, or final visual approval is defined.
- Review rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, marker validation, camera approval, or final visual signoff.
- Materials use rough highland stone, soot, ash, trampled mud, rawhide, rope, oxide red cloth, blackened iron, sparse old horn, and dull bone consistently.
- Default emissive, ritual glow, shamanic glow, signal glow, animated material states, gameplay VFX, UI-like markers, readable text, and neutral/civilized Giant language are absent and approval-gated.
- Tiny stone chips, cloth weave, fray, scratches, pitting, soot speckles, ash flecks, paint chips, horn rings, lichen, mud streaks, and rope fibers are assigned to textures or normals in future packages.
