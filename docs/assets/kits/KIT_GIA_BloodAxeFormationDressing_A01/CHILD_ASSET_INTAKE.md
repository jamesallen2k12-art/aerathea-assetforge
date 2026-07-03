# KIT_GIA_BloodAxeFormationDressing_A01 Child Asset Intake

## Source

- Parent kit: `KIT_GIA_BloodAxeFormationDressing_A01`
- Parent route: `KIT_GIA_BloodAxeWarband_A01#FormationDressing`
- Source route references: `Bloodaxe Army.png`, `Blood Axe Fist Hunting Party.png`, `BloodAxeStronghold.png`, and `BloodAxeCamp.png` as listed by existing Blood Axe intake docs
- Related docs: `KIT_GIA_BloodAxeWarband_A01`, `KIT_GIA_BloodAxeArmory_A01`, `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeCampShelters_A01`, `SK_GIA_BloodAxeBannerBearer_A01`, `SK_GIA_BloodAxeShieldCarrier_A01`, `SK_GIA_BloodAxeTrophyCarrier_A01`, `SK_GIA_BloodAxeRaider_A01`, `SK_GIA_BloodAxeCampSentry_A01`, and `SK_GIA_BloodAxeForgeGuard_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Intake status: docs-only child split complete for visual composition planning; no child build target selected
- Scale dependency: validated `SK_GIA_Base_A01` female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5"; approved Giant ranges females 14-15 ft and males 14'10"-16'0"
- Source-storage guardrail: external source concepts remain in the external concept folder only. Do not copy, move, edit, embed, crop, rename, inspect for final visual approval, or commit source images for this docs-only package.

## Notes

This child intake splits formation dressing into planning-only visual rows. The rows describe composition, scale readability, material discipline, camera framing, and future static-dressing requirements. They are not final asset approvals, encounter roles, combat ranks, waves, AI groups, spawn sets, nav markers, patrol paths, or implementation tickets.

Blood Axe formation dressing must stay separate from neutral/civilized Giant culture. It may use red banners, blackened iron, dark steel, scorched leather, rough hide, soot, ash, packed earth, rough timber, broken scrap, and sparse non-graphic trophies. It must not reuse civilized Giant cave-town, blue-gray masonry, terrace, warm hearth, civic stoneworker, or restrained blue-rune language as the default read.

No row below creates or authorizes DCC source, FBX export, Unreal import, source asset creation, runtime source, validators, startup placement, source concept movement, final visual approval, or first implementation target selection.

## Child Asset Table

| Child ID | Planning type | Proposed future package or asset | Status | Notes |
| --- | --- | --- | --- | --- |
| `KIT_GIA_BloodAxeFormationDressing_A01#LineSilhouettes` | Grouped line silhouettes | `KIT_GIA_BloodAxeFormationLineSilhouettes_A01` | Planning row ready | Front/three-quarter/side silhouette bands for Blood Axe Giants using 442 cm female and 470 cm male scale anchors. Visual line only, not combat ranks, troop classes, waves, or encounter lanes. |
| `KIT_GIA_BloodAxeFormationDressing_A01#SpacingReferences` | Visual spacing references | `SM_GIA_BloodAxeFormationSpacingStrip_A01` | Planning row ready | Ground spacing, depth offsets, and negative-space gutters for review composition. Values support camera readability only and must not become nav spacing, spawn spacing, patrol spacing, or collision blocking rules. |
| `KIT_GIA_BloodAxeFormationDressing_A01#BannerRhythm` | Banner rhythm and vertical beats | `SM_GIA_BloodAxeBannerRhythmMarker_A01` | Planning row ready | Repeated torn red banner poles, banner top-line comparison, cloth block rhythm, and pole/head tangent checks. No faction aura, capture mechanic, buff, debuff, objective, cloth simulation, or banner AI behavior. |
| `KIT_GIA_BloodAxeFormationDressing_A01#WeaponHeightMarkers` | Weapon height markers | `SM_GIA_BloodAxeWeaponHeightMarker_A01` | Planning row ready | Simplified height references for double axe, crusher hammer, hook spear, cleaver, longbow, and carried banner reads against Giant baselines. Not attack reach, trace length, damage arc, or combat-role definition. |
| `KIT_GIA_BloodAxeFormationDressing_A01#ShieldWallVisualDressing` | Shield wall visual dressing | `SM_GIA_BloodAxeShieldWallDressing_A01` | Planning row ready | Broad shield blocks and foreground silhouette tests using Blood Axe shield-carrier language. Visual dressing only; no block volumes, cover behavior, stamina rules, weak points, nav blockers, or shield mechanics. |
| `KIT_GIA_BloodAxeFormationDressing_A01#TrophyBackdropDressing` | Trophy backdrop dressing | `SM_GIA_BloodAxeTrophyBackdrop_A01` | Planning row ready | Sparse dry trophy markers, horn/bone shapes, broken shield tokens, and trophy-carrier silhouette support. Keep non-graphic and readable; no loot, collection, inventory, dismemberment, or reward behavior. |
| `KIT_GIA_BloodAxeFormationDressing_A01#ForgeBackdropDressing` | Forge backdrop dressing | `SM_GIA_BloodAxeForgeBackdrop_A01` | Planning row ready | Soot-dark forge rack, scrap, slag, quench, tool, and guard-adjacent shapes for background depth. No crafting, economy, heat hazard, resource, salvage, workstation, material graph, VFX, or interaction behavior. |
| `KIT_GIA_BloodAxeFormationDressing_A01#CampBackdropDressing` | Camp backdrop dressing | `SM_GIA_BloodAxeCampBackdrop_A01` | Planning row ready | Raw-log gate, shelter edge, warning cloth, packed-earth path, barricade, and camp post reads borrowed from camp planning. No final camp visual approval, nav mesh, gate behavior, patrol path, or startup placement. |
| `KIT_GIA_BloodAxeFormationDressing_A01#ReviewCompositionMarkers` | Review composition markers | `KIT_GIA_BloodAxeReviewCompositionMarkers_A01` | Planning row ready | Non-shipping height rods, ground ticks, camera frame references, and marker positions for A/B comparison planning. No Unreal actor creation, validator update, capture approval, or final review-scene signoff. |
| `KIT_GIA_BloodAxeFormationDressing_A01#CameraReadabilityFrames` | Camera readability frames | `DOC_GIA_BloodAxeFormationCameraFrames_A01` | Planning row ready | Thumbnail-style framing notes for full group, banner top-line, shield foreground, and camp backdrop readability. Docs-only camera planning; no camera actor, capture script, startup scene, or visual approval claim. |
| `KIT_GIA_BloodAxeFormationDressing_A01#MaterialDisciplineSwatches` | Material discipline planning | `DOC_GIA_BloodAxeFormationMaterialDiscipline_A01` | Planning row ready | Swatch and usage guidance for blackened iron, dark steel, scorched leather, rough hide, soot, ash, oxide red cloth, packed earth, timber, and sparse trophies. No new material instances are created. |
| `KIT_GIA_BloodAxeFormationDressing_A01#LODAndCollisionStaticDressing` | Future static dressing LOD/collision planning | `DOC_GIA_BloodAxeFormationLODAndCollision_A01` | Planning row ready | LOD0-LOD3 and disabled/simple collision policy for future review markers or static dressing. No collision proxies, nav blockers, gameplay volumes, or implementation files are created. |

## Dependency Notes

- `SK_GIA_Base_A01` owns Giant scale, skeleton policy, capsule expectations, body proportions, and future character collision assumptions.
- `KIT_GIA_BloodAxeWarband_A01` owns the broader visual hierarchy and confirms this row as non-gameplay formation dressing.
- `KIT_GIA_BloodAxeArmory_A01` owns Blood Axe weapons, banners, shields, trophy gear, reforged metal, quivers, bows, and material language.
- `KIT_GIA_BloodAxeCamp_A01` and `KIT_GIA_BloodAxeCampShelters_A01` own camp gates, shelters, watch points, forge/cooking/dressing zones, paths, barricades, and camp clutter.
- Character role packages own their own future fit, scale, socket, animation, and gear-read concerns. This intake only references their silhouettes for composition.
- No row in this table is approved as a first DCC, Unreal, runtime, source asset, gameplay, or visual approval target.

## Immediate Package Priority

The kit-level production package and this child intake are ready for docs-only planning review. Later work should choose one planning lane only after lead approval and should remain docs-only unless a new task explicitly expands ownership.

Recommended next planning lane, if requested later:

- Expand `#ReviewCompositionMarkers` into a docs-only review layout packet with camera thumbnails, scale rods, and non-shipping marker descriptions.
- Expand `#BannerRhythm` or `#WeaponHeightMarkers` only if the art direction team needs tighter top-line comparison before DCC work.

No first implementation target is selected by this intake.

## Approval and Stop Gates

- Stop before any DCC source, Blender file, sculpt, retopo, UV, bake, collision proxy, proof render, FBX export, Unreal Content asset, material instance, texture asset, validator, runtime source, Blueprint, socket authoring, animation asset, review-scene actor, or startup placement work.
- Stop before copying, moving, editing, embedding, cropping, renaming, or committing any external source concept.
- Stop before final Blood Axe formation visual approval, hero screenshot approval, or first playable visual approval.
- Stop before selecting a first DCC, Unreal, source asset, or implementation target from any row.
- Stop before defining encounter design, AI groups, waves, ranks, combat roles, squad logic, patrol routes, spawn logic, nav behavior, aggro logic, perception, damage values, projectile behavior, shield mechanics, aura effects, objective logic, loot, inventory, rewards, crafting, economy, destructible behavior, pickup behavior, or interaction behavior.
- Stop before claiming character fit, socket compatibility, final pose clearance, cloth simulation, physics setup, collision correctness, or camera-capture approval.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any row appears to require changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5".

## Quality Gate Checklist

- Child rows are planning-only and do not define final gameplay troop roles, combat ranks, waves, AI groups, patrol paths, nav behavior, or spawn logic.
- Rows cover line silhouettes, spacing references, banner rhythm, weapon height markers, shield wall visual dressing, trophy backdrop dressing, forge backdrop dressing, camp backdrop dressing, review composition markers, camera readability frames, material discipline, and LOD/collision static-dressing planning.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5", with approved Giant ranges of females 14-15 ft and males 14'10"-16'0".
- Blood Axe remains a hostile Giant sub-faction, not default Giant culture.
- No source concept files are copied, moved, edited, embedded, cropped, renamed, inspected for final approval, or committed.
- No DCC, FBX, Unreal Content, runtime source, validators, startup placements, global indexes, task-board changes, backlog changes, bootstrap changes, AI, combat stats, abilities, loot, crafting, economy, patrol logic, spawn logic, final visual approval, or first build target is claimed.
