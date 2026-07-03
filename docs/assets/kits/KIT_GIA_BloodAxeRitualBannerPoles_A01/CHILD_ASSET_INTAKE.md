# KIT_GIA_BloodAxeRitualBannerPoles_A01 Child Asset Intake

## Source

- Parent planning context: future Blood Axe ritual-stone and camp-edge dressing split, with visual dependencies on `KIT_GIA_BloodAxeBannerLine_A01`, `KIT_GIA_BloodAxePathMarkers_A01`, `SM_GIA_BloodAxeBoneHornMarker_A01`, and `SK_GIA_Base_A01`.
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only.
- Intake status: docs-only planning child breakdown.
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep this hostile sub-faction separate from neutral/civilized Giant culture.
- Scale dependency: validated `SK_GIA_Base_A01` female `442 cm` and male `470 cm` baselines.
- Source-storage guardrail: source concepts remain external. Do not copy, move, edit, embed, inspect for visual review, or commit source images for this docs-only package.

## Notes

This intake splits the ritual banner-pole kit into planning-only child rows. The rows cover tall poles, tied cloth strips, rope lashings, stone weights, sparse horn markers, review rows, material discipline, and LOD/collision planning.

The kit is static warning and memory dressing only. It does not define cloth physics, animation, faction buff behavior, morale/AI behavior, aura/VFX, interaction behavior, quest marker behavior, DCC, FBX, Unreal, startup placement, or first implementation target selection.

Blood Axe ritual banner poles may use rough timber, tied oxide red cloth, thick rope, hide lashings, blackened iron, crude stone weights, soot, ash, mud, and sparse non-graphic horn markers. They must not use neutral Giant cave-town masonry, refined highland clan banners, warm hearth settlement ornament, terrace or waterwork motifs, civic stoneworker symbols, restrained blue runes, or polished neutral/civilized Giant culture.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- |
| `BloodAxeRitualStones.png#RitualBannerPole_Tall_A01` | Tall poles | `SM_GIA_BloodAxeRitualBannerPole_Tall_A01` | Package needed; planning only | Giant-scale rough pole, 520-780 cm above ground, split top, fixed red cloth, rope lashing, and weighted base. Static warning and memory dressing only; no cloth physics, animation, aura/VFX, interaction, quest marker, or startup placement. |
| `BloodAxeRitualStones.png#RitualBannerPole_Secondary_A01` | Tall poles | `SM_GIA_BloodAxeRitualBannerPole_Secondary_A01` | Package needed; planning only | Shorter 320-520 cm pole variant for background rhythm and abandoned camp traces. Keep silhouette rough and Blood Axe-specific; do not reuse neutral/civilized Giant culture markings. |
| `BloodAxeRitualStones.png#RitualPole_Pair_A01` | Paired poles | `SM_GIA_BloodAxeRitualPolePair_A01` | Package needed; planning only | Two uneven poles with a static tied cloth band and stone weights. Visual threshold only; no gate behavior, nav blocker, objective logic, interaction behavior, or first implementation target selection. |
| `BloodAxeRitualStones.png#RitualPole_Cluster_A01` | Pole cluster | `SM_GIA_BloodAxeRitualPoleCluster_A01` | Package needed; planning only | Three to five varied poles for ritual-stone approach composition and memory dressing. Use sparse horns and broad cloth strips; avoid dense trophy walls, graphic gore, spell-device reads, or aura/VFX. |
| `BloodAxeRitualStones.png#TiedCloth_Strips_A01` | Tied cloth strips | `SM_GIA_BloodAxeRitualClothStripSet_A01` | Package needed; planning only | Static oxide red cloth-strip set with broad readable torn shapes, soot-dark lower edges, and hide ties. No cloth physics, vertex wind, banner animation, destructible cloth, runtime material state, or faction buff behavior. |
| `BloodAxeRitualStones.png#TiedCloth_KnotWraps_A01` | Tied cloth strips | `SM_GIA_BloodAxeRitualClothKnotWraps_A01` | Package needed; planning only | Reusable cloth knots and wrap shapes for pole bases and cross ties. Keep cloth strips large and count-controlled; texture tiny fray and weave instead of modeling micro-detail. |
| `BloodAxeRitualStones.png#RopeLashing_Set_A01` | Rope lashings | `SM_GIA_BloodAxeRitualRopeLashingSet_A01` | Package needed; planning only | Thick rope, hide cord, and major knot modules for tying poles, stones, and horn markers. No simulated rope, dangling physics, interaction, trap behavior, or collision beyond future simple pole/base collision. |
| `BloodAxeRitualStones.png#StoneWeights_A01` | Stone weights | `SM_GIA_BloodAxeRitualStoneWeight_A01` | Package needed; planning only | Crude heavy stones, mud-packed anchors, and rope-tied base weights sized for Giant handling. Visual anchoring only; no pickup, loot, resource, crafting, damage, destructible, or nav behavior. |
| `BloodAxeRitualStones.png#SparseHornMarkers_A01` | Sparse horn markers | `SM_GIA_BloodAxeRitualHornMarker_A01` | Package needed; planning only | Sparse horn markers tied near pole tops or stone bases as silhouette punctuation. Keep non-graphic and low density; no gore escalation, collectible behavior, ritual gameplay, aura/VFX, or magic state. |
| `BloodAxeRitualStones.png#BlackenedIron_TieHardware_A01` | Hardware accents | `SM_GIA_BloodAxeRitualTieHardware_A01` | Package needed; planning only | Crude blackened iron rings, collars, nails, and scrap hooks used sparingly on major ties. Do not create dense rivet detail or unique material slots for every small piece. |
| `BloodAxeRitualStones.png#Review_ScaleRows_A01` | Review rows | `SM_GIA_BloodAxeRitualPoleScaleRow_A01` | Planning row only | Non-shipping scale rows showing female `442 cm` and male `470 cm` Giant baselines beside tall poles, cloth strips, rope lashings, stone weights, and sparse horn markers. No shipped marker status, Unreal actor, startup placement, or scale-lock change. |
| `BloodAxeRitualStones.png#Review_CompositionRows_A01` | Review rows | `DOC_GIA_BloodAxeRitualPoleReviewRows_A01` | Planning row only | Docs-only rows for single-pole, paired-pole, cluster, and ritual approach spacing. No validator, capture automation, startup scene work, visual review claim, DCC, FBX, or Unreal work. |
| `BloodAxeRitualStones.png#MaterialDiscipline_A01` | Material discipline | `DOC_GIA_BloodAxeRitualPoleMaterialDiscipline_A01` | Planning row only | Locks rough timber, oxide red cloth, rope, hide, stone, blackened iron, soot, ash, mud, and sparse horn materials. Excludes default emissive, blue runes, polished civic Giant material language, and neutral/civilized Giant culture. |
| `BloodAxeRitualStones.png#LODAndCollision_A01` | LOD/collision planning | `DOC_GIA_BloodAxeRitualPoleLODAndCollision_A01` | Planning row only | Docs-only LOD0-LOD3 and collision policy for poles, cloth strips, rope lashings, stone weights, horn markers, and review rows. No collision proxies, cloth collision, trigger volumes, nav blockers, gameplay volumes, DCC, FBX, Unreal, or startup placement. |

## Dependency Notes

- `KIT_GIA_BloodAxeBannerLine_A01` owns repeated perimeter banner-line language. Ritual banner poles should be more isolated, vertical, and memory-focused.
- `SM_GIA_BloodAxeWarBanner_A01` owns larger camp-marker banner identity. Ritual banner poles should not compete with hero war banners.
- `KIT_GIA_BloodAxePathMarkers_A01` owns general route markers. Ritual banner poles may overlap visually through cloth and horn language, but must remain static dressing and not become waypoint or quest marker behavior.
- `SM_GIA_BloodAxeBoneHornMarker_A01` owns standalone bone/horn territory-marker planning. This kit uses sparse horn markers only as restrained accents.
- `SK_GIA_Base_A01` owns the Giant scale lock: female `442 cm` and male `470 cm` baselines.

## Unordered Future Package Candidates

No first DCC target, source asset target, Unreal target, runtime target, or implementation target is selected by this intake. If a later lead-scoped docs or production lane is opened, these may be promoted independently:

- `SM_GIA_BloodAxeRitualBannerPole_Tall_A01`
- `SM_GIA_BloodAxeRitualBannerPole_Secondary_A01`
- `SM_GIA_BloodAxeRitualPolePair_A01`
- `SM_GIA_BloodAxeRitualPoleCluster_A01`
- `SM_GIA_BloodAxeRitualClothStripSet_A01`
- `SM_GIA_BloodAxeRitualClothKnotWraps_A01`
- `SM_GIA_BloodAxeRitualRopeLashingSet_A01`
- `SM_GIA_BloodAxeRitualStoneWeight_A01`
- `SM_GIA_BloodAxeRitualHornMarker_A01`
- `SM_GIA_BloodAxeRitualTieHardware_A01`
- `SM_GIA_BloodAxeRitualPoleScaleRow_A01`
- `DOC_GIA_BloodAxeRitualPoleReviewRows_A01`
- `DOC_GIA_BloodAxeRitualPoleMaterialDiscipline_A01`
- `DOC_GIA_BloodAxeRitualPoleLODAndCollision_A01`

## Guardrails

- Do not create DCC source, FBX exports, Unreal Content, runtime source, tools, validators, startup actors, material instances, textures, source folders, or external source concept changes from this intake.
- Do not define cloth physics, animation, faction buff behavior, morale/AI behavior, aura/VFX, interaction behavior, quest marker behavior, objective logic, encounter scripting, nav/pathfinding, trigger volumes, loot, resource, crafting, economy, damage, destructible, pickup, or audio behavior.
- Do not change the `SK_GIA_Base_A01` female `442 cm` and male `470 cm` scale baselines.
- Do not let Blood Axe ritual dressing become neutral/civilized Giant culture.

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, or bootstrap file.
- Child rows cover tall poles, tied cloth strips, rope lashings, stone weights, sparse horn markers, review rows, material discipline, and LOD/collision planning.
- Ritual banner poles are static warning and memory dressing only.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: `SK_GIA_Base_A01` female `442 cm` and male `470 cm` baselines.
- Rows are useful for future package planning without selecting a first implementation target.
- No cloth physics, animation, faction buff behavior, morale/AI behavior, aura/VFX, interaction behavior, quest marker behavior, DCC, FBX, Unreal, startup placement, or runtime gameplay is defined.
- Review rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, or visual review claims.
- Materials use rough timber, rope, hide, stone, blackened iron, soot, ash, mud, oxide red cloth, and sparse non-graphic horn consistently.
- Default emissive, ritual glow, shamanic glow, signal glow, animated material states, gameplay VFX, UI-like markers, readable text, and neutral/civilized Giant language are absent.
