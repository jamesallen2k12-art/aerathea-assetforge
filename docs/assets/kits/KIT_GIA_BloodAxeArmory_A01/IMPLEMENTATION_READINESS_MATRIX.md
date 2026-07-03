# KIT_GIA_BloodAxeArmory_A01 Implementation Readiness Matrix

## Scope

- Task: `AET-MA-20260629-056`
- Scope type: docs-only Blood Axe armory implementation readiness matrix.
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Covered child packages: `SM_GIA_BloodAxeDoubleAxe_A01`, `SM_GIA_BloodAxeCrusherHammer_A01`, `SM_GIA_BloodAxeLongbow_A01`, `KIT_GIA_BloodAxeQuivers_A01`, and `MI_GIA_BloodAxeReforgedMetal_A01`.
- Scale dependency: validated `SK_GIA_Base_A01` scale lock, female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft and males 14'10"-16'0".
- Excluded work: no DCC source creation, no source folder creation, no FBX export, no Unreal Content import, no validator authoring, no runtime source, no startup placement, no source concept copying, no final build target selection, no combat rule design, and no final visual approval.

This matrix converts the first Blood Axe armory child packages into an implementation queue. It is a planning artifact only. A later assigned implementation task must choose the build target and own its source/export/Unreal paths before any DCC, FBX, material authoring, Blueprint, startup, or validator work begins.

## Package Inputs

| Asset or package | Package path | Current package status | Readiness note |
| --- | --- | --- | --- |
| `SM_GIA_BloodAxeDoubleAxe_A01` | `docs/assets/props/SM_GIA_BloodAxeDoubleAxe_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started | Primary hero two-handed Blood Axe weapon; strong silhouette target, but final blade/trophy density still needs visual approval before final art. |
| `SM_GIA_BloodAxeCrusherHammer_A01` | `docs/assets/props/SM_GIA_BloodAxeCrusherHammer_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started | Blunt impact counterpart to the double axe; lower silhouette complexity and likely best first static-mesh DCC target after material dependency planning. |
| `SM_GIA_BloodAxeLongbow_A01` | `docs/assets/props/SM_GIA_BloodAxeLongbow_A01/PRODUCTION_PACKAGE.md` | Production package ready; DCC build not started | Bow package is ready for planning, but final socket names, draw envelope, arrow scale, and quiver clearance remain future approval/validation items. |
| `KIT_GIA_BloodAxeQuivers_A01` | `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/PRODUCTION_PACKAGE.md`; `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/CHILD_ASSET_INTAKE.md` | Mini-kit package and child table ready; DCC build not started | Belt, back, rack, arrow, bundle, arrow-head, strap, and trophy-tag children are split; needs a variant export manifest before modeling. |
| `MI_GIA_BloodAxeReforgedMetal_A01` | `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md` | Material package ready; Unreal material authoring not started | Shared material dependency for weapons, quiver hardware, armor plates, and camp hardware; default emissive is locked off. |

## Recommended Build Queue

This queue ranks implementation readiness. It does not select the final build target.

| Queue | Asset or package | Type | Readiness | Why this position | Required gate before build |
| ---: | --- | --- | --- | --- | --- |
| 0 | `MI_GIA_BloodAxeReforgedMetal_A01` | Material dependency | Package ready; Unreal authoring not started | Shared blackened/reforged metal language prevents weapon and hardware packages from drifting. | Assigned material/Unreal task must own shader graph, texture assets, and focused material validation. |
| 1 | `SM_GIA_BloodAxeCrusherHammer_A01` | Static mesh weapon | Ready for first DCC candidate | Simple broad mass, strong impact silhouette, limited trophy density, and clear two-handed grip make it the lowest-risk geometry target. | Lead must approve this as the first DCC build target and confirm grip pivot/impact-marker policy. |
| 2 | `SM_GIA_BloodAxeDoubleAxe_A01` | Static mesh hero weapon | Ready after first weapon pattern exists | Signature Blood Axe hero weapon; benefits from reusing crusher hammer grip, material, LOD, and collision validation patterns. | Visual approval needed before final blade shape, trophy density, and chieftain/boss variants are locked. |
| 3 | `SM_GIA_BloodAxeLongbow_A01` | Static mesh bow | Ready with socket/dependency caution | Bow arc and nock forms are package-ready, but string/nock/draw references and quiver dependency add coordination cost. | Confirm bow socket names, string locators, `back_quiver` clearance, and no projectile/animation timing scope. |
| 4 | `KIT_GIA_BloodAxeQuivers_A01` | Mini-kit | Ready after variant manifest | Child table is complete, but DCC requires per-child names, pivots, export rows, material slots, and collision policy. | Approve variant export manifest before source work. |
| Hold | `SM_GIA_BloodAxeBeltQuiver_A01` and related quiver children | Child static meshes | Package-defined only through mini-kit | Good follow-up after longbow/quiver clearance is tested. | Promote from mini-kit into child-specific task packet. |
| Hold | Future Blood Axe armor modules | Skeletal/static gear | Not covered in this task | Armor fit depends on Giant body, pelvis, shoulder, head, and locomotion clearance. | Create separate armor package and fit-validation lane. |

## Dependency Map

| Dependency | Feeds | Notes |
| --- | --- | --- |
| `SK_GIA_Base_A01` scale lock | All Blood Axe weapons, bows, quivers, armor, racks, and display props | Female baseline 442 cm / 14'6"; male baseline 470 cm / 15'5"; do not resize to normal humanoid scale. |
| `MI_GIA_BloodAxeReforgedMetal_A01` | Double axe, crusher hammer, longbow metal fittings, quiver hardware, future armor plates, scrap piles | Default no-emissive material; forge heat and shamanic glow remain approval-gated variants. |
| `KIT_GIA_BloodAxeQuivers_A01` | Longbow arrow scale, back carry clearance, archer silhouette, rack/camp dressing | Longbow package reserves dependencies, but quiver child variants must define exact carry attachments and arrow proportions. |
| `KIT_GIA_BloodAxeArmory_A01` child intake | Future cleaver, hook spear, knife, armor, banner, scrap pile, bow parts, bowyer tools | Current matrix covers only first package-ready children; remaining child packages need separate docs-only tasks first. |
| Blood Axe culture guardrail | All child packages | Blood Axe remains a hostile Giant sub-faction and must not overwrite neutral/civilized Giant stoneworker culture. |

## Source And Export Path Plan

These paths are planned references only. This matrix does not create source folders, export folders, Blender files, FBX files, Unreal assets, or validators.

| Asset or package | Planned Blender source path | Planned export path | Planned Unreal target path |
| --- | --- | --- | --- |
| `SM_GIA_BloodAxeCrusherHammer_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/SM_GIA_BloodAxeCrusherHammer_A01/` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/SM_GIA_BloodAxeCrusherHammer_A01/` | `/Game/Aerathea/Weapons/Giants/BloodAxe/SM_GIA_BloodAxeCrusherHammer_A01` |
| `SM_GIA_BloodAxeDoubleAxe_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/SM_GIA_BloodAxeDoubleAxe_A01/` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/SM_GIA_BloodAxeDoubleAxe_A01/` | `/Game/Aerathea/Weapons/Giants/BloodAxe/SM_GIA_BloodAxeDoubleAxe_A01` |
| `SM_GIA_BloodAxeLongbow_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/SM_GIA_BloodAxeLongbow_A01/` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/SM_GIA_BloodAxeLongbow_A01/` | `/Game/Aerathea/Weapons/Giants/BloodAxe/SM_GIA_BloodAxeLongbow_A01` |
| `KIT_GIA_BloodAxeQuivers_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/KIT_GIA_BloodAxeQuivers_A01/` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/KIT_GIA_BloodAxeQuivers_A01/` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Quivers/` and `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/Quivers/` |
| `MI_GIA_BloodAxeReforgedMetal_A01` | Not applicable unless a later task creates material preview meshes | Not applicable unless a later task creates material preview exports | `/Game/Aerathea/Materials/Giants/BloodAxe/MI_GIA_BloodAxeReforgedMetal_A01` |

## Planned Variant Export Rows

`KIT_GIA_BloodAxeQuivers_A01` must not enter DCC as a single collapsed mesh. A future variant manifest should include at least:

| Variant | Planned mesh | Pivot | Collision policy | Notes |
| --- | --- | --- | --- | --- |
| Belt quiver | `SM_GIA_BloodAxeBeltQuiver_A01` | Belt attachment point | One simple capsule/box for display; disabled when equipped | Fit `belt_quiver_l`, `belt_quiver_r`, `belt_tool_l`, or `belt_tool_r` references. |
| Back quiver | `SM_GIA_BloodAxeBackQuiver_A01` | Upper-back attachment point | One simple capsule/box for display; disabled when equipped | Must clear `back_large_weapon`, shoulders, spine, and longbow carry. |
| Rack quiver | `SM_GIA_BloodAxeRackQuiver_A01` | Ground center | Grouped boxes or low-count convex hulls | Static camp/armory dressing. |
| Loose arrow | `SM_GIA_BloodAxeArrow_A01` | Shaft midpoint | Simple capsule/box only for display | No projectile behavior in DCC/import task. |
| Arrow bundle | `SM_GIA_BloodAxeArrowBundle_A01` | Bundle center or lower tie point | One simple capsule/box | Use grouped silhouette, not dense individual-arrow collision. |
| Arrow heads display | `SM_GIA_BloodAxeArrowHeadsDisplay_A01` | Board/backing center | One simple box | Keep head variants readable and limited. |
| Strap variants | `SM_GIA_BloodAxeQuiverStrap_A01` or variant set | Attach center | No standalone collision | Reuse materials; avoid one-off material slots. |
| Trophy tag variants | `SM_GIA_BloodAxeTrophyTag_A01` or variant set | Lash point | No standalone collision | Use sparingly to avoid trophy clutter. |

## Material Dependency Matrix

| Asset or package | Material dependency notes | Risk |
| --- | --- | --- |
| `SM_GIA_BloodAxeCrusherHammer_A01` | Use `MI_GIA_BloodAxeReforgedMetal_A01` for blackened head plates, bands, and impact faces; scorched leather/haft material may be in the same atlas or a second slot. | Low geometry risk; medium material risk until shared metal is authored. |
| `SM_GIA_BloodAxeDoubleAxe_A01` | Use the shared reforged metal for blades/head/collars; red paint and trophy accents must stay restrained. | Medium visual risk because it is the hero silhouette and trophy density can overtake readability. |
| `SM_GIA_BloodAxeLongbow_A01` | Use shared metal only for caps, plates, and hardware; primary material remains dark wood, horn, leather, sinew, and red cloth. | Medium dependency risk from bow sockets, string line, and quiver clearance. |
| `KIT_GIA_BloodAxeQuivers_A01` | Use shared metal for rims, buckles, arrowheads, and rack hardware; most surfaces use scorched leather, rough wood, bone/horn, and red cloth. | Medium mini-kit risk until variant manifest locks material slots and child names. |
| Future Blood Axe armory children | Use shared metal when blackened/reforged surfaces are central; avoid applying it to neutral Giant objects unless a stolen/defaced variant is explicitly approved. | Medium culture-separation risk. |

## Risk Ranking

| Rank | Risk | Affected assets | Mitigation |
| ---: | --- | --- | --- |
| 1 | Blood Axe language could overwrite neutral/civilized Giant culture. | All Blood Axe armory packages | Keep `BloodAxe` in names, docs, folders, and material language; never promote red-black raider language as the default Giant identity. |
| 2 | Giant scale or socket drift could break downstream weapons and carry gear. | All children | Validate against female 442 cm / 14'6" and male 470 cm / 15'5"; keep normal humanoid compatibility out of scope unless separately requested. |
| 3 | Quiver mini-kit could collapse into a single mesh. | `KIT_GIA_BloodAxeQuivers_A01` | Require variant export manifest before DCC; keep belt/back/rack/arrows/straps/tags separated. |
| 4 | Bow work could accidentally define gameplay or animation timing. | `SM_GIA_BloodAxeLongbow_A01`, quiver arrows | Keep projectile behavior, draw timing, arrow inventory, damage, and release logic approval-gated. |
| 5 | Hero double axe could become too noisy. | `SM_GIA_BloodAxeDoubleAxe_A01` | Limit trophy accents, red cloth, rivets, and chains; texture small detail instead of modeling it. |
| 6 | Shared material may be overused or become too red. | Material and all consumers | Clamp red paint to accent masks; keep blackened metal and rough leather as primary reads. |
| 7 | Weapon collision could become too complex. | Double axe, crusher hammer, longbow, arrows | Equipped collision disabled; display collision uses simple boxes/capsules/convex hulls; combat traces require later gameplay approval. |
| 8 | Source concept storage could leak into the repo. | All Blood Axe armory packages | Keep `BloodAxeArmory.png` external unless a future source-storage task explicitly approves copying. |

## Validator Gaps And Future Checks

No focused Blood Axe armory DCC, material, or Unreal import validators are created by this task. Future implementation tasks should add focused validators only when they own the relevant tool paths.

| Future lane | Validator requirement |
| --- | --- |
| DCC source/export validation | Confirm source path, export path, FBX name, centimeter scale, primary dimensions, pivot, LOD0-LOD3 sources, material slot count, and no micro-detail geometry misuse. |
| Giant scale validation | Compare dimensions and grip/carry markers against `SK_GIA_Base_A01` female 442 cm / 14'6" and male 470 cm / 15'5" baselines. |
| Weapon import validation | Confirm Unreal path, grip pivot, equipped collision disabled, display collision simple, LODs, material slots, texture references, and planned trace marker names. |
| Bow import validation | Confirm bow arc, grip pivot, nock markers, string locators, `socket_arrow_rest`, `socket_arrow_nock`, `socket_string_top`, `socket_string_bottom`, and no projectile logic. |
| Quiver mini-kit validation | Confirm per-variant mesh names, export rows, pivots, collision policy, material slots, LODs, arrow count limits, and distinct belt/back/rack silhouettes. |
| Material validation | Confirm shared parent material, parameter names, default `ForgeHeatAmount=0.0`, no default emissive, texture references, red-paint mask limits, and roughness/metallic ranges. |
| Culture separation scan | Confirm Blood Axe docs do not claim default Giant culture, cave-town culture, neutral Giant materials, or civilized Giant identity. |
| Matrix maintenance validation | Run package-existence scan, implementation-scope guardrail scan, source-storage guardrail scan, and `git diff --check` after docs edits. |

## Approval Gates

- Lead approval is required to select any final DCC build target from this queue.
- DCC work may start only from an assigned implementation task that owns the relevant `SourceAssets/Blender` and `SourceAssets/Exports` paths.
- Unreal material authoring may start only from an assigned material/Unreal task that owns `/Game/Aerathea/Materials/Giants/BloodAxe/` and its validators.
- Quiver work requires a variant export manifest before modeling starts.
- Longbow work requires bow socket, string locator, arrow scale, and quiver clearance confirmation before final import approval.
- Double axe final art requires visual approval for blade shape, trophy density, red paint placement, and any chieftain/boss variant.
- Gameplay approval is required before combat traces, damage arcs, hit timing, projectile behavior, arrow inventory, loot rules, pickup interactions, or equip behavior.
- Source-storage approval is required before copying or embedding external concept art in the repository.
- Culture approval is required if Blood Axe material or silhouette language starts bleeding into neutral/civilized Giant packages.
- Startup placement and final visual approval are outside this matrix.

## Quality Gate Checklist

- Matrix references only package-ready Blood Axe armory children from `AET-MA-20260629-051` through `AET-MA-20260629-055`.
- DCC queue priority is recorded without choosing a final build target.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", with approved Giant ranges documented.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Source/export paths are plans only; no folders, meshes, FBX files, tools, Unreal assets, runtime source, or startup actors are authored here.
- Material dependencies and default no-emissive policy are explicit.
- Quiver mini-kit variant manifest need is explicit before DCC promotion.
- Bow projectile, animation timing, combat, and inventory behavior are approval-gated.
- Future validator gaps are documented without creating tools.
- Source concept remains external and is not copied, moved, edited, embedded, or committed.
