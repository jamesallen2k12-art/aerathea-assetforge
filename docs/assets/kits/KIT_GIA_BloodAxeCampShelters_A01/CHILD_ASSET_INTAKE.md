# KIT_GIA_BloodAxeCampShelters_A01 Child Asset Intake

## Intake Summary

- Parent package: `KIT_GIA_BloodAxeCampShelters_A01`
- Task: `AET-MA-20260629-095`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Source basis: Aerathea Giant/Blood Axe anchors, Blood Axe armory/banner/material packages, and production backlog direction
- Status: docs-only child intake ready
- Scale dependency: validated `SK_GIA_Base_A01` female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"

This intake splits the Blood Axe camp shelter kit into planning-only child rows. It does not select a first DCC target, create child package files, create source folders, author meshes, export FBX, import Unreal Content, build validators, edit startup scenes, define snapping implementation, create collision proxies, simulate cloth, define destructible behavior, or add shelter interaction.

Blood Axe shelters must remain crude hostile raider camp assets. They should not inherit neutral/civilized Giant cave-town architecture, blue-gray stoneworker materials, warm hearth identity, restrained blue rune language, or refined highland settlement construction.

## Child Intake Table

| Child ID | Type | Proposed asset/package | Status | Scale and material target | Triangle budget target | Collision/LOD planning | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `KIT_GIA_BloodAxeCampShelters_A01#Shelter_HideTent_A01` | Hide tents | `SM_GIA_BloodAxeHideTent_A01` | Package needed; planning only | Giant-scale hide wedge or squat conical tent, 420-620 cm tall, 650-1100 cm long, rough hide/leather, scorched pole frame, red repair cloth, blackened iron stakes | 8k-18k tris | Future simple hulls around frame and blocked walls; no cloth collision; LOD0-LOD3 required | Primary shelter read for Blood Axe camp living zones. Entrance should fit the male 470 cm Giant baseline. Static shaped hide only; no cloth simulation, destructible flaps, interaction, storage, or rest behavior. |
| `KIT_GIA_BloodAxeCampShelters_A01#Shelter_LeanTo_A01` | Lean-tos | `SM_GIA_BloodAxeLeanTo_A01` | Package needed; planning only | Asymmetric sloped shelter, 350-520 cm high side, 550-950 cm wide footprint, rough timber, hide panels, lashings, blackened clamps, muted red warning scraps | 4k-10k tris | Future boxes or low-count hulls around frame; cloth panel collision disabled; LOD0-LOD3 required | Supports camp edge dressing, guard rest zones, and forge-adjacent cover silhouettes. Should look hastily built by raiders, not finely joined Giant craft. |
| `KIT_GIA_BloodAxeCampShelters_A01#Shelter_TrophyPole_A01` | Trophy poles | `SM_GIA_BloodAxeShelterTrophyPole_A01` | Package needed; planning only | 520-760 cm vertical warning pole, dark timber, blackened iron rings, red strips, one to three large bone/horn/armor trophies | 3k-8k tris | Future pole capsule plus optional base hull; no per-trophy collision; LOD0-LOD3 required | Marks hostile shelter territory and separates Blood Axe camp identity from normal Giant settlements. Keep trophies sparse and non-graphic. |
| `KIT_GIA_BloodAxeCampShelters_A01#Shelter_BeddingPallet_A01` | Bedding pallets | `SM_GIA_BloodAxeBeddingPallet_A01` | Package needed; planning only | Oversized 500-650 cm bed pallet, 230-340 cm wide, stacked logs, hide rolls, straw mats, dirty cloth, soot and mud wear | 2k-6k tris | Future low box or convex hull around pallet mass; LOD0-LOD3 required | Communicates Giant scale and camp occupancy. Inert set dressing only; no sleep/rest interaction, inventory, search, or loot logic. |
| `KIT_GIA_BloodAxeCampShelters_A01#Shelter_BarricadeLeaner_A01` | Barricade leaners | `SM_GIA_BloodAxeBarricadeLeaner_A01` | Package needed; planning only | Leaning defensive boards, sharpened logs, broken shield slabs, blackened scrap plates, red cloth tags, 280-520 cm tall | 3k-9k tris | Future one or two simple hulls matching the leaned footprint; no per-spike collision; LOD0-LOD3 required | Adds defensive camp language around shelters. Does not define gameplay cover, destructible barricades, nav blocking, or encounter rules. |
| `KIT_GIA_BloodAxeCampShelters_A01#Shelter_Awning_A01` | Awnings | `SM_GIA_BloodAxeCampAwning_A01` | Package needed; planning only | Broad static hide or torn cloth shade panel spanning 450-900 cm, tied to poles or frames, red/black Blood Axe accents, soot-stained lower edges | 4k-9k tris | Future support pole collision only; no awning cloth collision; LOD0-LOD3 required | Gives camp spaces overhead rhythm and shade. Static mesh baseline only; no wind, vertex sway, cloth sim, collapse state, or interaction. |
| `KIT_GIA_BloodAxeCampShelters_A01#Shelter_SupportFrame_A01` | Support frames | `SM_GIA_BloodAxeShelterSupportFrame_A01` | Package needed; planning only | Reusable A-frames, tripods, ridge poles, cross braces, 20-45 cm log diameters, blackened clamps, lashings, crude red marker cloth | 3k-8k tris | Future capsules/boxes for major poles only; LOD0-LOD3 required | Planning row for reusable shelter construction forms. Modular snapping remains out of scope until a separate implementation task defines pivots, grid, sockets, and validation. |
| `KIT_GIA_BloodAxeCampShelters_A01#Shelter_Clutter_A01` | Shelter clutter | `KIT_GIA_BloodAxeShelterClutter_A01` | Package needed; planning only | Hide rolls, tether stakes, ash buckets, bone hooks, cracked bowls, water skins, stored bundles, boot scrapers, large enough for Giant use | 500-4k tris per prop, 4k-12k per composed clutter group | Future simplified boxes/hulls only for large blocking pieces; tiny clutter collision disabled; LOD0-LOD3 for important children | Practical living clutter, not loot. Avoid inventory, harvest, crafting, economy, pickup, resource-node, or quest-object behavior. |
| `KIT_GIA_BloodAxeCampShelters_A01#Shelter_ComposedCluster_A01` | Composed placement cluster | `SM_GIA_BloodAxeCampShelters_A01` | Optional future package; planning only | Reused tent, lean-to, support frame, awning, pallet, barricade, trophy, and clutter children arranged as one preview/placement cluster | 25k-55k tris using reused child meshes | Future grouped low-count hulls only if approved; LOD0-LOD3 required | Optional level-dressing assembly after children are approved. Do not build as a unique collapsed sculpt. No startup placement or final visual approval in this task. |

## Material and Scale Rules

- Use the female 442 cm and male 470 cm Giant baselines for all shelter dimensions, entrances, awning clearances, bedding, and support frame proportions.
- Use Blood Axe material language: rough hide, scorched leather, dark timber, blackened iron, dark steel, red cloth, soot, ash, mud, grime, and sparse bone/horn trophies.
- Use `MI_GIA_BloodAxeReforgedMetal_A01` for stakes, clamps, scrap plates, hardware, and blackened metal fittings where applicable.
- Do not use neutral/civilized Giant cave-town materials as the default: no blue-gray stoneworker masonry, warm hearth identity, restrained blue rune language, or refined highland construction.
- No default emissive. Ritual, shamanic, forge-heat, or magical variants require separate approval.

## Planning Priorities

This list is scheduling guidance only and does not select or authorize a first DCC target.

1. `SM_GIA_BloodAxeShelterSupportFrame_A01` - establishes reusable Giant-scale frame proportions.
2. `SM_GIA_BloodAxeHideTent_A01` - primary shelter silhouette and entrance scale.
3. `SM_GIA_BloodAxeLeanTo_A01` - lower-risk shelter variant and camp edge dressing.
4. `SM_GIA_BloodAxeBeddingPallet_A01` - direct Giant scale proof for living spaces.
5. `SM_GIA_BloodAxeBarricadeLeaner_A01` - camp defense silhouette without gameplay cover claims.
6. `SM_GIA_BloodAxeCampAwning_A01` - overhead shelter rhythm after static cloth policy is accepted.
7. `SM_GIA_BloodAxeShelterTrophyPole_A01` - faction marker after trophy density is reviewed.
8. `KIT_GIA_BloodAxeShelterClutter_A01` - broad set dressing after large forms are stable.
9. `SM_GIA_BloodAxeCampShelters_A01` - optional composed cluster only after child meshes and placement rules are approved.

## Stop Gates

- Stop before modular snapping implementation, snap sockets, snap grid, placement validators, or source pivots are authored.
- Stop before collision proxy creation, UCX meshes, physics bodies, nav policy, or gameplay cover rules.
- Stop before cloth simulation, vertex sway, wind animation, moving flaps, collapse states, rope physics, or destructible shelter behavior.
- Stop before shelter interaction, sleeping/resting, storage, looting, crafting, resource, search, quest objective, camp alarm, fire spread, or economy behavior.
- Stop before selecting a first DCC target.
- Stop before source folders, DCC, FBX, Unreal Content, runtime source, tools, validators, startup placement, global index edits, task-board edits, or external concept copying.
- Stop if the shelter language starts reading as neutral/civilized Giant cave-town architecture instead of Blood Axe raider camp construction.

## Quality Gate Checklist

- Intake covers hide tents, lean-tos, trophy poles, bedding pallets, barricade leaners, awnings, support frames, shelter clutter, and optional composed cluster planning.
- Every child row is planning-only and does not claim DCC, FBX, Unreal, collision proxy, snapping, cloth, interaction, destructible, startup, validator, or final visual work.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Blood Axe shelter language stays separate from neutral/civilized Giant cave-town culture.
- Materials use rough hide, scorched leather, dark timber, blackened iron, red cloth, soot, ash, mud, grime, and sparse non-graphic trophies.
- Triangle budget, collision planning, LOD requirements, material target, and guardrails are captured for every row.
- Future package work is clear without selecting a first DCC target.
