# KIT_GIA_BloodAxeBannerLine_A01 Child Asset Intake

## Source

- Parent planning row: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md` entry `Blood Axe Village.png#Banner_LineMarkers`
- Source references recorded in existing camp intake docs: `Blood Axe Village.png`, `BloodAxeCamp.png`, `BloodAxecamp.png`, `BloodAxeGate.png`, and `BloodAxeStronghold.png`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only planning child breakdown ready
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in names to keep the hostile sub-faction separate from neutral/civilized Giant culture
- Scale dependency: validated `SK_GIA_Base_A01` female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: source concepts remain in the external concept folder only. Do not copy, move, edit, embed, inspect for visual approval, or commit source images for this docs-only package.

## Notes

This intake splits the Blood Axe banner-line kit into planning-only child rows. The rows describe tall poles, rope-line variants, tattered cloth banners, warning pennants, camp-threshold markers, material discipline, LOD/collision assumptions, and review composition rows for later visual planning.

Blood Axe banner-line dressing must stay separate from neutral/civilized Giant culture. It may use rough timber, thick rope, red warning cloth, blackened iron, scorched leather, soot, ash, mud, broken scrap, and sparse non-graphic horn or bone markers. It must not reuse civilized Giant cave-town, blue-gray masonry, terrace, warm hearth, civic stoneworker, refined highland clan banner, or restrained blue-rune language as the default read.

This intake does not select a first DCC target, approve final visual art, create source folders, create FBX exports, create Unreal Content, place startup actors, define cloth/physics setup, define banner animation, define faction buff behavior, define morale/AI behavior, or define runtime gameplay.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- |
| `Blood Axe Village.png#BannerLine_TallPole_A01` | Tall poles | `SM_GIA_BloodAxeBannerLineTallPole_A01` | Package needed; planning only | Giant-scale rough timber pole, 420-620 cm tall, blackened iron collar, hide lashings, red cloth wrap, optional stone or scrap base. Static boundary vertical only; no cloth physics, socket, interaction, or startup placement. |
| `BloodAxeCamp.png#BannerLine_TallPoleCluster_A01` | Tall pole cluster | `KIT_GIA_BloodAxeBannerLineTallPoleCluster_A01` | Package needed; planning only | Two to five varied tall poles for camp-edge rhythm, with staggered heights against the 442 cm and 470 cm Giant baselines. Visual composition only; no faction aura, morale effect, AI marker, or spawn lane. |
| `Blood Axe Village.png#BannerLine_RopeLineLow_A01` | Rope-line variants | `SM_GIA_BloodAxeBannerLineRopeSpan_Low_A01` | Package needed; planning only | Low sagging rope between short stakes, 140-220 cm rope height, thick knots, mud-dark bases, and small cloth ties. Boundary dressing only; no collision rope, tripwire, trap, pathfinding, or damage behavior. |
| `Blood Axe Village.png#BannerLine_RopeLineHigh_A01` | Rope-line variants | `SM_GIA_BloodAxeBannerLineRopeSpan_High_A01` | Package needed; planning only | Higher rope span between Giant-built poles, 240-360 cm rope height, larger knots and red cloth strips for camp perimeter readability. Static visual line only; no banner animation, rope physics, nav blocker, or gameplay marker. |
| `BloodAxeGate.png#BannerLine_RopeTieKnotSet_A01` | Rope and knot set | `KIT_GIA_BloodAxeBannerLineRopeKnots_A01` | Package needed; planning only | Reusable thick knots, rope coils, hide ties, and iron tie rings for future banner-line modules. Texture rope fibers and tiny fray; no simulated rope or dynamic secondary motion. |
| `BloodAxeCamp.png#BannerLine_TatteredClothBanner_A01` | Tattered cloth banners | `SM_GIA_BloodAxeTatteredBannerLine_A01` | Package needed; planning only | Broad torn oxide red cloth panel tied to a rope line or short crossbar, 120-260 cm wide and 120-320 cm drop. Static shaped cloth geometry only; no cloth simulation, wind animation, destructibility, or faction-state material behavior. |
| `Blood Axe Village.png#BannerLine_SplitTailBanner_A01` | Tattered cloth banners | `SM_GIA_BloodAxeSplitTailBannerLine_A01` | Package needed; planning only | Split-tail red banner variant with two or three large readable tails, soot-dark lower edges, and sparse hide patches. Keep tears large; avoid dense micro-strips, readable text, and graphic gore. |
| `BloodAxeStronghold.png#BannerLine_WarningPennants_A01` | Warning pennants | `SM_GIA_BloodAxeWarningPennantLine_A01` | Package needed; planning only | Small repeated red warning pennants, 70-180 cm long, used sparingly along paths and perimeter edges. Visual warning rhythm only; no UI arrow, waypoint, quest marker, aura, buff, debuff, or AI behavior. |
| `BloodAxeCamp.png#BannerLine_PennantBundle_A01` | Warning pennants | `KIT_GIA_BloodAxePennantBundle_A01` | Package needed; planning only | Bundle of short red pennants, hide strips, and blackened rings for quick repeated camp dressing. Do not make a dense bunting curtain; preserve mid-poly readability and low material count. |
| `Blood Axe Village.png#BannerLine_CampThresholdPair_A01` | Camp-threshold markers | `SM_GIA_BloodAxeCampThresholdMarker_A01` | Package needed; planning only | Pair of taller poles with rope, tattered cloth, and heavy bases framing a camp threshold span of roughly 500-1000 cm. Visual threshold only; no gate behavior, nav path, capture mechanic, objective volume, or startup placement. |
| `BloodAxeGate.png#BannerLine_ThresholdDrape_A01` | Camp-threshold markers | `SM_GIA_BloodAxeThresholdDrape_A01` | Package needed; planning only | Static torn drape or cloth hang for a rough entry compression beat, related to future gate drapes but kept smaller than a gate package. No cloth setup, interaction, destructible state, or final gate approval. |
| `BloodAxeStronghold.png#BannerLine_CairnClothStake_A01` | Camp-threshold markers | `SM_GIA_BloodAxeCairnClothMarker_A01` | Package needed; planning only | Crude cairn, cloth stake, horn token, and ash-stained base for route or perimeter edge marking. Visual warning only; no waypoint logic, trail-marker gameplay, loot, pickup, or source concept embedding. |
| `BloodAxeCamp.png#BannerLine_BrokenShieldMarker_A01` | Warning marker | `SM_GIA_BloodAxeBrokenShieldMarker_A01` | Package needed; planning only | Broken shield, scrap plate, red paint smear, and rope-tied stake used as sparse hostile warning dressing. Keep non-graphic; no loot, destructible behavior, inventory pickup, or combat cover definition. |
| `Blood Axe Village.png#Review_CompositionRows_A01` | Review composition rows | `DOC_GIA_BloodAxeBannerLineReviewRows_A01` | Planning row ready | Docs-only review composition rows showing line rhythm, pole height alternation, rope sag silhouettes, threshold framing, and camera read. No Unreal actor, validator, capture automation, startup scene placement, or final visual signoff. |
| `Blood Axe Village.png#Review_ScaleRows_A01` | Review composition rows | `SM_GIA_BloodAxeBannerLineScaleRow_A01` | Planning row ready | Non-shipping scale rows for female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines beside tall poles, rope spans, pennants, and threshold markers. No scale-lock change or shipped marker approval. |
| `Blood Axe Village.png#Review_LODCollisionRows_A01` | LOD and collision review rows | `DOC_GIA_BloodAxeBannerLineLODAndCollision_A01` | Planning row ready | Docs-only LOD0-LOD3 and collision-limit rows for static poles, rope lines, cloth panels, pennants, threshold pairs, and review markers. No collision proxies, nav blockers, cloth collision, gameplay volumes, or validator files are created. |
| `Blood Axe Village.png#MaterialDiscipline_A01` | Material discipline row | `DOC_GIA_BloodAxeBannerLineMaterialDiscipline_A01` | Planning row ready | Shared material discipline for rough timber, rope, hide, scorched leather, blackened iron, soot, mud, oxide red cloth, and sparse non-graphic bone/horn. Explicitly excludes neutral/civilized Giant cave-town materials and default emissive. |

## Dependency Notes

- `SM_GIA_BloodAxeWarBanner_A01` owns the larger static camp-marker banner language. Banner-line modules should be smaller, more repeatable, and cheaper.
- `SK_GIA_BloodAxeBannerBearer_A01` owns character banner-carry planning. This intake does not define carried-banner sockets, harness fit, animation timing, cloth simulation, or character attachment behavior.
- `KIT_GIA_BloodAxeFormationDressing_A01` owns broader non-gameplay formation composition. This kit can provide banner-line rhythm references but must not define combat ranks, waves, AI groups, or spawn spacing.
- `KIT_GIA_BloodAxeStrongholdApproach_A01` owns stronghold approach cliffs, palisades, and gate-facing compression. This kit can provide warning cloth and threshold-line modules only as visual dressing.

## Suggested Future Package Order

No first DCC target is selected by this intake. If a later lead-approved package lane is opened, the lowest-risk planning order is:

1. `SM_GIA_BloodAxeBannerLineTallPole_A01`
2. `SM_GIA_BloodAxeBannerLineRopeSpan_Low_A01`
3. `SM_GIA_BloodAxeTatteredBannerLine_A01`
4. `SM_GIA_BloodAxeWarningPennantLine_A01`
5. `SM_GIA_BloodAxeCampThresholdMarker_A01`
6. Review composition rows only when a later visual review task explicitly needs them

## Approval Gates

- Stop before any DCC source, sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material instance, texture asset, validator, runtime source, Blueprint, socket authoring, cloth setup, physics setup, animation asset, or startup placement work.
- Stop before copying, moving, editing, embedding, inspecting for visual approval, or committing external source concepts.
- Stop before cloth simulation, vertex wind, rope physics, pennant flutter, banner animation, destructible cloth, collapse states, physics bodies, or dangling secondary motion.
- Stop before faction buff behavior, morale behavior, AI behavior, patrol/spawn logic, encounter scripting, objective logic, capture mechanics, aura volumes, UI markers, loot, resource, crafting, economy, interaction behavior, VFX pulses, or audio cues.
- Stop before selecting a first DCC target.
- Stop before final visual approval claims.
- Stop if Blood Axe banner-line dressing starts replacing neutral/civilized Giant culture.
- Stop if any row requires changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5".

## Quality Gate Checklist

- Intake is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, or bootstrap file.
- Child rows include tall poles, rope-line variants, tattered cloth banners, warning pennants, camp-threshold markers, and review composition rows.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Rows are useful for future package planning without selecting a first DCC target.
- No cloth/physics setup, banner animation, faction buff behavior, morale/AI behavior, encounter behavior, nav behavior, interaction behavior, loot, resource, crafting, economy, VFX, audio, or objective logic is defined.
- Review composition rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, or final visual signoff.
- Materials use rough timber, rope, hide, scorched leather, blackened iron, soot, ash, mud, oxide red cloth, and sparse non-graphic bone or horn consistently.
- Default emissive, ritual glow, shamanic glow, signal glow, animated material states, gameplay VFX, UI-like markers, readable text, and neutral/civilized Giant language are absent and approval-gated.
- Tiny rope fibers, cloth weave, fray, stitches, rivets, scratches, pitting, soot speckles, ash flecks, paint chips, and wood grain are assigned to textures or normals in future packages.
