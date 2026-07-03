# DOC_GIA_BloodAxeStorageMaterialDiscipline_A01 Production Package

Docs-only material-discipline package for Blood Axe Giant storage clutter. This package creates no material instances, no texture assets, no material graphs, no VFX/audio, no DCC source, no Unreal Content, no startup placement, no final color approval, no final visual approval, no source concept movement, no Hermes work, and no implementation target.

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeStorageMaterialDiscipline_A01`
- Asset type: Docs-only material policy package
- Parent kit: `KIT_GIA_BloodAxeCratesSacksBaskets_A01`
- Source planning row: `Blood Axe Village.png#MaterialDiscipline_Storage_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only material discipline ready

This document locks the shared material language for Blood Axe storage clutter: rough timber, blackened iron, rope, rawhide, dirty sackcloth, thick basket weave, patched hide covers, soot, ash, mud, and restrained oxide red accents. It explicitly separates hostile Blood Axe raider storage from neutral/civilized Giant culture.

## Gameplay Purpose

The material policy keeps future storage assets visually consistent and prevents accidental gameplay signaling through glow, UI colors, readable labels, resource colors, vendor display polish, or interaction highlights.

Out of scope: material instance creation, texture asset creation, material graph authoring, VFX/audio, emissive behavior, animated material states, DCC, Unreal Content, startup placement, final color approval, final visual approval, implementation target selection, loot, pickup, inventory, resource, vendor, crafting, economy, interaction, cover, nav/pathfinding, destructible, and runtime behavior.

## Silhouette Notes

Material treatment must support silhouette rather than hide it:

- Dark timber and blackened iron should clarify crate block forms.
- Dirty sackcloth and hide should keep sack/bundle masses broad.
- Rope and rawhide should emphasize large lashings and knots.
- Basket weave should read as thick bands, not fine fiber noise.
- Oxide red should be a restrained identity accent, not a route marker or UI color.

Avoid high-contrast labels, glowing marks, tiny pattern noise, shiny treasure treatment, clean vendor polish, and civilized Giant craft symbols.

## Scale Notes

- Giant scale lock: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Materials must support Giant-scale forms with broad readable zones; do not use human-scale textile or basket detail density as the dominant read.

## Materials and Color Palette

Primary material families:

- Rough timber and scorched boards.
- Blackened iron and dull dark-steel straps.
- Heavy rope, rawhide lashings, sinew ties, and dirty leather.
- Dirty sackcloth, burlap, smoke-gray canvas, patched hide, and old tarp cloth.
- Thick basket weave using reeds, split timber, rawhide bands, and rope ribs.
- Soot, ash, dried mud, grease, charcoal dust, and ground-contact grime.
- Restrained oxide red cloth or paint for Blood Axe identity.

Palette targets:

- Rough timber: `#2A1A10` to `#5C3A22`
- Blackened iron: `#121315` to `#333538`
- Rope/rawhide: `#6B5435` to `#A98B5B`
- Sackcloth/canvas: `#6A604E` to `#A39370`
- Hide/leather: `#2F1D14` to `#77543A`
- Basket weave: `#5A4128` to `#9A7A4C`
- Soot/ash/mud: `#0B0A09` to `#4B4032`
- Blood Axe red: `#5F1513` to `#8B211B`

Do not use neutral/civilized Giant blue-gray masonry, polished stoneworker craft, warm hearth market supplies, restrained blue runes, default emissive, or clean highland civic material language.

## Concept Image Prompt

Create an original stylized fantasy MMORPG material discipline board of `DOC_GIA_BloodAxeStorageMaterialDiscipline_A01` for the world of Aerathea. The design should emphasize Blood Axe Giant storage material swatches for rough timber, scorched wood, blackened iron, heavy rope, rawhide, dirty sackcloth, thick basket weave, patched hide covers, soot, ash, mud, restrained oxide red accents, validated Giant scale context with female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in references, hostile Giant sub-faction identity, and separation from neutral/civilized Giant culture. Use hand-painted texture detail, readable material zones, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production discipline. Present it as a clean docs-only material board with swatches, allowed/blocked examples, texture-map notes, roughness/metallic notes, and no-build guardrails. Avoid copying any existing franchise, avoid material instance claims, avoid texture asset claims, avoid shader graph diagrams, avoid VFX/audio, avoid UI-colored markers, avoid readable labels, avoid neutral Giant cave-town language, and avoid excessive micro-detail.

## Modeling Notes

Material discipline affects future modeling by keeping large material zones readable. Future meshes should not model tiny grain, fibers, weave, fray, scratches, soot flecks, and paint chips as geometry. This document creates no meshes, material slots, source folders, or implementation targets.

## Texture and Material Notes

Future texture plan only:

- Base Color for broad timber, cloth, hide, rope, basket, iron, mud, ash, and red accents.
- Normal for grain, weave, fibers, stitching, folds, scratches, chips, soot, and pitting.
- ORM with high roughness for timber, cloth, hide, rope, basket, soot, ash, and mud; metallic only for blackened iron.

No emissive map is planned. Do not create material instances, material functions, texture assets, shader graphs, VFX, audio, or material-state behavior from this policy.

## Triangle Budget

No triangle budget is assigned to the material policy itself. Future material discipline should reduce geometry pressure by moving micro-detail into texture/normal maps. Shipping mesh budgets remain owned by individual child packages.

## LOD Plan

Material readability must survive LOD reduction. LODs should keep broad timber/cloth/rope/basket/iron/red accent zones while removing small dirt, weave, and scratch detail first. This document does not author LODs.

## Collision Notes

No collision is created or approved. Material choices must not imply damage fields, hot surfaces, pickup zones, resource nodes, interaction highlights, cover markers, nav/pathfinding aids, or gameplay volumes.

## Animation Notes

No animation is planned. No emissive pulse, heat shimmer, material-state swap, VFX, audio cue, cloth motion, rope motion, or gameplay feedback is authorized.

## Unreal Import Notes

Future Unreal material work, if separately approved, should use shared material instances under `/Game/Aerathea/Materials/Giants/BloodAxe/` and must preserve no-baseline-emissive policy. This document creates no Unreal Content, material instances, texture assets, material functions, Blueprints, validators, review actors, startup actors, or map edits.

## Folder and Naming Recommendation

- Package: `docs/assets/kits/DOC_GIA_BloodAxeStorageMaterialDiscipline_A01/PRODUCTION_PACKAGE.md`
- Policy ID: `DOC_GIA_BloodAxeStorageMaterialDiscipline_A01`
- Possible future material root: `/Game/Aerathea/Materials/Giants/BloodAxe/Storage/`
- No source, texture, material, export, or Unreal folder is selected.

## Quality Gate Checklist

- [x] Docs-only material policy package.
- [x] Includes all universal Aerathea package sections.
- [x] Uses female 442 cm and male 470 cm Giant scale lock.
- [x] Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- [x] Blocks material instances, texture assets, material graphs, VFX/audio, DCC, Unreal Content, startup placement, final color approval, final visual approval, and implementation target selection.
- [x] Uses rough timber, blackened iron, rope, rawhide, dirty sackcloth, basket weave, hide covers, soot, ash, mud, and restrained oxide red accents consistently.
- [x] Excludes default emissive, readable labels, UI colors, vendor polish, resource cues, and neutral/civilized Giant cave-town materials.
