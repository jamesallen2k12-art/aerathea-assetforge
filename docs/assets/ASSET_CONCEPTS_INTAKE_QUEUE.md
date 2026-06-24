# Asset Concepts Intake Queue

## Purpose

This queue schedules category-level intake for the 289 PNG source concepts listed in `docs/assets/ASSET_CONCEPTS_MANIFEST.md`. It does not replace the manifest, production backlog, or asset index. Its job is to define the order, batching rules, expected batch artifacts, and collage-expansion rules before more production packages are created.

Source concepts remain in `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`. A source PNG is not complete until it has been visually inspected, expanded into child items when needed, and assigned a package, variant, reference-only, covered, or retired status.

## Intake Principles

- Treat the source-file count as the floor, not the final asset count.
- Create kit-level or category-level breakdowns before individual production packages.
- Keep race body/style decisions ahead of armor, clothing, Mek attachment, and portrait finalization.
- Keep building shell kits ahead of interior kits when an interior depends on the same architectural language.
- Use cross-category faction passes for Anubisath/Sutekh and Valar so their visual systems stay coherent across characters, armory, structures, interiors, and UI.
- Do not turn any source concept or collage child directly into a mesh, Blueprint, UI icon, or material without the Aerathea production pipeline.

## Batch Size And Method

Use small, reviewable batches rather than one broad manifest pass.

| Batch type | Normal size | Method | Batch output artifact |
| --- | ---: | --- | --- |
| Single collage-heavy source | 1 source PNG | Inspect visually, split all buildable children, group by child type, assign proposed names and statuses | `CHILD_ASSET_INTAKE.md` under the future kit/package folder |
| Category intake slice | 3-8 source PNGs | Group related sources by category, faction/theme, and production dependency | Category intake brief, usually `docs/assets/intake/<BatchID>_<Category>_INTAKE.md` when intake artifacts are created |
| Faction/theme vertical slice | 6-15 source PNGs | Pull matching sources across armory, race/NPC, building, interior, UI, and world-reference categories | Faction intake slate, usually `docs/assets/intake/<BatchID>_<Faction>_SLATE.md` when intake artifacts are created |
| Variant family | 5-12 source PNGs | Compare variants, pick base silhouette/material rules, then classify child variants | Family package plus variant matrix |
| Pipeline/reference pass | 3-6 source PNGs | Classify as project rule, style anchor, production checklist, or reference-only source | Rule/reference classification brief |

Batch IDs should use `ACIQ-P##_NN`, where `P##` matches the priority row below and `NN` is the local batch number. Example: `ACIQ-P01_01_MKG_ARMORY_CHILDREN`.

## Priority Order

| Priority | Queue area | Scope from manifest/backlog | First scheduling target | Output artifact per batch | Dependency notes |
| ---: | --- | --- | --- | --- | --- |
| 1 | Armory and gear | 13 armory/gear source concepts, including faction armories, arsenals, relic gear, and workshop gear | Continue from existing `KIT_MKG_Armory_A01`; then schedule Dwarven, Elven, Dark Elven, Orc, Minotaur, Drakhar, Anubisath/Sutekh, Valar, and Common kits | Kit-level production package plus `CHILD_ASSET_INTAKE.md` for each collage-heavy armory sheet | Gnome armory is already seeded; individual armor modules wait for race body fit rules |
| 2 | Race body/style | 57 character/NPC/class sources plus approved race anchors | Start with gnome base body/style because startup scale and Mekgineer gear already exist; then Dwarves, Elves, Dark Elves, Orcs, Minotaurs, Drakhar, Valar, and Anubisath/Sutekh bodies/NPCs | Race body/style sheet package with proportions, material language, starter outfit rules, rig notes, and Unreal import plan | Required before wearable armor, portrait finalization, and Mek pilot fit |
| 3 | Settlement/building | 66 building, settlement, and environment concepts | Start with `SM_AET_Palisade_A01` or `SM_AET_House_A01`; then common settlement anchors before faction buildings | Modular building kit intake brief or production package with child module list | Exterior shell and material rules should precede matching interiors |
| 4 | Creature/mount | 45 creature/mount concepts | Start with `SK_CRE_Gryphon_A01`; then Hippogryph, Manticore, Dragon variants, and Dwarf riding yak | Creature family intake package with base anatomy, variant matrix, animation list, collision, LOD, and material plan | Dragon and raid-boss variants wait until family rules and aggressive LOD policy are approved |
| 5 | Mek suits/companions | 43 Gnome/Mekgineer Mek suit and companion sources | Group light, medium, heavy, weapon-specific, companion, and rift-touched sources into Mek class batches | Mek class kit with skeletal/static mesh split, sockets, attachment rules, child intake, material plan, and VFX socket notes | Depends on gnome body scale, Mekgineer material language, and armory socket policy |
| 6 | Interiors | 36 interior/environment set concepts | Start with common house/interior and meeting hall sources; then faction halls and Sutekh temple interiors | Interior kit intake with room modules, hero props, lighting/material notes, collision, and LOD guidance | Match exterior faction material rules where available |
| 7 | UI and portraits | 7 portrait icon sheets | Batch all `Portrait Icons for Mobs*.png` sheets by icon rows/panels | UI portrait atlas intake with one child ID per icon, crop/export rules, naming plan, and status table | Final portrait naming should align with race, creature, and NPC package names where known |
| 8 | Anubisath/Sutekh vertical slice | 47 Anubisath/Sutekh sources across armory, character, buildings, interiors, and world references | Consolidate armaments, minions/NPCs, pyramid/necropolis structures, barge concepts, temple interiors, and Sutekh reference sources | Faction slate that maps all Anubisath/Sutekh sources to package needs, variants, reference-only items, and dependency order | Cross-cutting pass prevents contradictory seal, necropolis, sand, soulforge, and enemy-faction material language |
| 9 | Valar vertical slice | 16 Valar sources across armory, character, buildings, interiors, and world references | Consolidate Valar body/style, nobility, paladin/priest, ranger/warden, armory, halls, barracks/training yard, and spire sources | Faction slate that defines Valar silhouette, material, oath/warden motifs, package needs, and child expansion | Should follow or run alongside race body/style so Valar body proportions and gear fit are consistent |
| 10 | Common/world references | 16 general world references plus 6 pipeline/reference boards | Classify lore/world references, target dummy/common prop references, magecraft/rune references, and pipeline boards | Rule/reference classification brief, with production package links only when a buildable asset is identified | Reference boards become style rules, checklists, or package constraints, not meshes by themselves |

## Category Batch Notes

### Armory And Gear

- Start each armory sheet as a kit, not as isolated weapons.
- Group children into weapons, shields, armor pieces, tools, backpacks, relics, power cores, displays, and outfit configurations.
- Use `KIT_<Faction>_Armory_A##` for kit-level documentation where an established faction code exists.
- Create child packages only after the kit breakdown, material set, scale rules, sockets, and attachment rules are recorded.
- Existing seed: `docs/assets/kits/KIT_MKG_Armory_A01/` covers `Gnome Armory.png` at kit and child-intake level; schedule its child packages before duplicating the same work elsewhere.

### Race Body And Style

- Build body/style packages before armor, portrait finalization, or skeletal gear fitting.
- Every race batch needs a base body proportion sheet, starter outfit direction, material language, rig assumptions, animation notes, and import naming.
- Approved anchors in `AGENTS.md` control silhouettes and culture; do not re-interpret races from a single source image.
- Character/NPC/class sheets that are not base bodies should be classified as starter outfit, class kit, hero NPC, enemy NPC, or reference variant.

### Creature And Mount

- Batch by creature family before variant production.
- Separate base anatomy, mount/ride assumptions, combat animation needs, wing/tail collision, physics constraints, and LOD budgets.
- Variant sheets should produce a variant matrix first, then individual packages only for approved gameplay roles.
- Creature sheets with many variants must use child IDs for each distinct variant, pose, or body-part reference.

### Settlement And Building

- Batch common settlement shells before faction settlement expansions where possible.
- Split boards into modular walls, doors, windows, roofs, pillars, props, lamps, banners, signs, terrain pieces, and material sets.
- Every building batch should specify pivot policy, snap dimensions, collision type, material slot limits, LOD targets, and Unreal folder naming.
- Boards that include multiple views or districts should become kit/module lists before any individual building package is marked ready.

### Interiors

- Split each room board into structural modules, large furniture, small props, lighting fixtures, banners/signage, material sets, and dressing-only references.
- Interior kits should include camera/player scale notes, collision simplification, light/VFX restraint, and reused exterior material links.
- Do not create dense prop lists from interior boards until hero props and reusable modules are separated from dressing clutter.

### UI And Portraits

- Treat every portrait icon as a child item.
- Use child IDs such as `Portrait Icons for Mobs.png#Icon_01`.
- Record intended use before production: player race portrait, mob portrait, boss icon, quest portrait, vendor/trainer portrait, or placeholder/reference.
- Batch output must include crop/export rules, target sizes, alpha/background policy, naming, and package links to matching character or creature assets when known.

### Mek Suits And Companions

- Group Mek sources by light, medium, heavy, weapon-specific, pet/companion, and rift-touched classes.
- Each Mek batch needs pilot fit assumptions, skeletal/static mesh split, socket plan, attachment rules, material slot budget, emissive limits, animation states, and collision notes.
- Mechanical companions should be split from wearable suits so pet rigs, locomotion, scale, and gameplay collision stay separate.
- Weapon-specific Meks should not define base Mek proportions until the class kit establishes shared silhouette rules.

### Anubisath/Sutekh

- Run as a vertical slice after initial category rules exist, or earlier if an enemy-faction milestone needs it.
- Consolidate armaments, minions, named enemies, pyramid fortresses, necropolis structures, barges, quarry/soulforge, portal pyramids, halls, temple interiors, and Sutekh lore references.
- Separate buildable assets from lore/style references such as `Sutekh Breaker of Seals.png`.
- Ensure seal, necropolis, soulforge, sand, stone, gold, obsidian, and glow language is consistent across all subcategories.

### Valar

- Run as a vertical slice tied to race body/style and armory planning.
- Consolidate approved male/female body sources, nobility, paladin/priest, ranger, wardens, armory, halls, meadhall, barracks/training yard, watchtower, spire, and world reference.
- Separate body proportion rules from class outfit rules and faction architecture rules.
- Keep oath/warden motifs, noble silhouettes, material palette, and UI portrait language consistent.

### Common And World References

- Classify each common/world source as buildable package, style anchor, lore reference, pipeline rule, checklist source, or reference-only item.
- `Target Dummy.png` should be checked against existing `SM_AET_TargetDummy_A01` before creating any new package.
- Pipeline boards should update process/checklist artifacts in a future task, not produce meshes.
- Magecraft, rune, sealing, and culture references should be linked to packages as constraints instead of duplicated into every package.

## Collage Child Expansion Rules

1. Visually inspect the source image before assigning child count or status.
2. Use a parent kit or batch brief when a source contains multiple related child assets.
3. Create stable child IDs in the form `Source File.png#Group_ChildName`.
4. Assign every child one status: `Package needed`, `Covered by existing package`, `Variant of existing package`, `Reference only`, or `Rejected or retired by Flamestrike`.
5. Give every buildable child a proposed asset or package name before production work starts.
6. Split children by production type: static mesh, skeletal mesh, Blueprint actor, material, UI, VFX, animation, or reference.
7. Mark scale dependencies explicitly, especially for race armor, Mek suits, mounts, and oversized enemy units.
8. Do not close a parent source as complete until every child row has a status and next action.
9. If a child is only useful as material, color, silhouette, lore, or mood reference, mark it `Reference only` and link it to the package it constrains.
10. If a child is already covered, record the existing package path or asset name rather than creating duplicate work.
11. For variant sheets, define the base variant first, then record later variants as biome, role, threat, class, material, or silhouette variants.
12. For UI sheets, one visible portrait/icon equals one child unless Flamestrike explicitly retires a row or panel.

## Batch Definition Of Done

A batch is complete only when it records:

- Source PNG list and manifest category/faction.
- Visual inspection date or note.
- Parent kit/package name when applicable.
- Child IDs for every buildable child in collage-heavy sources.
- Classification status for every child or source.
- Proposed package or asset names for buildable entries.
- Dependency notes for body scale, sockets, material sets, exterior/interior pairing, animation, collision, and Unreal import.
- Next action: production package, modeling handoff, variant pass, reference linkage, or retirement request.
