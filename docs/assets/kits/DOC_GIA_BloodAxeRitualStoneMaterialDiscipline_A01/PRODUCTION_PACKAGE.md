# DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01`
- Asset type: Documentation-only material policy package / ritual-stone material discipline guidance
- Task: `AET-MA-20260629-181`
- Parent kit: `KIT_GIA_BloodAxeRitualStones_A01`
- Parent intake row: `BloodAxeRitualStones_A01#MaterialDiscipline_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Dependency references: `KIT_GIA_BloodAxeRitualStones_A01`, `KIT_GIA_BloodAxeRitualStones_A01/CHILD_ASSET_INTAKE.md`, and the validated `SK_GIA_Base_A01` scale lock
- Status: docs-only material discipline planning; no material instance creation, texture creation, material graph authoring, VFX/audio, DCC, FBX, Unreal Content, startup placement, final color approval, or final visual approval is created or claimed

`DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01` defines the non-implementation material rules for future Blood Axe ritual-stone children: standing-stone rings, altar stones, cairn guideposts, dry ritual channel stones, ritual banner poles, cave approach markers, review rows, and scale rows. The material read should feel like old hostile camp residue and ritual warning territory, not an active magic device or finalized shader pass.

Blood Axe ritual-stone material language must remain a hostile Giant sub-faction treatment. It must not become the default read for Giants as a people, and it must stay separate from neutral/civilized Giant culture. Neutral/civilized Giant culture remains tied to hidden highland settlements, master stonework, blue-gray civic masonry, terraces, waterworks, warm hearth light, restrained blue runes, and orderly stoneworker identity.

This package preserves the no-default-emissive policy. Baseline ritual stones use rough highland stone, soot, ash, mud, scorched timber, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, and dull bone without glow, particles, animated material states, audio, gameplay highlight states, or final color approval.

## Gameplay Purpose

The gameplay purpose is visual planning only. This document gives future package authors a shared material discipline so Blood Axe ritual-stone assets read consistently as static warning, memory, guidepost, and moved-camp remnants.

Allowed planning uses:

- Establish baseline material families and usage ratios for future docs-only ritual-stone child packages.
- Preserve the Blood Axe material identity without overwriting neutral/civilized Giant culture.
- Keep no-emissive baseline materials clear before any separate emissive, VFX, or material-state task is approved.
- Support MMO-distance readability through broad value groups, sparse oxide red accents, and low material-slot pressure.
- Document what should be modeled as broad form versus handled by texture, normal, AO, roughness, or masks in later approved packages.

Out of scope:

- Material instance creation, texture creation, material graph authoring, trim-sheet authoring, shader work, VFX, audio, DCC source, mesh work, UV work, bake work, FBX export, Unreal import, Blueprint work, validators, startup placement, source concept movement, final color approval, final visual approval, final Blood Axe ritual approval, first implementation target selection, gameplay pathing, nav rules, encounter design, interaction behavior, destructible behavior, loot, crafting, economy, pickup behavior, resource behavior, damage/aura behavior, objective markers, quest/UI markers, readable rune text, or active ritual behavior.

## Silhouette Notes

Materials must support the large ritual-stone silhouettes instead of becoming the main read. The first read should remain Giant-scale stones, slabs, cairns, poles, cloth strips, and cave-threshold forms.

Material silhouette support:

- Rough highland stone should read as broad fractured faces, heavy chips, dark grooves, field-boulder mass, and ash-stained bases. Avoid carpets of tiny cracks.
- Soot should sit in low grooves, fire-blackened contact zones, slab undersides, pole bases, and inactive channel recesses without turning every surface black.
- Ash should gather at bases, trampled centers, dry channel seams, and old camp residue zones as soft pale value breaks.
- Mud should ground stones and poles with broad trampled bands, splashes, and foot-worn brown-gray transitions; it must not imply walkable route proof.
- Scorched timber should appear as oversized poles, weight braces, splintered supports, and blackened tips; fine grain stays in texture planning.
- Rope and rawhide should read as big lashings, broad wraps, and functional ties around poles or stones; fine fibers and stitching stay in normal/detail maps.
- Oxide red cloth should appear as sparse torn strips, tied warning knots, faded maroon wraps, and chipped red marks. It must not become a full red environment wash.
- Blackened iron should read as large clamps, rings, straps, blade fragments, or hammered plate repairs only where they strengthen the silhouette.
- Sparse old horn and dull bone should be restrained secondary warning beats, not dense trophy curtains or graphic gore.

Excluded neutral/civilized Giant material silhouettes:

- Refined blue-gray civic masonry, clean cave-town carving, terrace retaining-stone language, waterwork channel marks, polished bridge stone, warm hearth light, peaceful clan wayfinding, civic mason symbols, restrained blue rune inlays, and orderly hidden-settlement finish.

## Scale Notes

Giant scale lock: use female 442 cm and male 470 cm baselines from `SK_GIA_Base_A01`. The approved Giant ranges remain females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm. Author any future source in centimeters with 1 Unreal unit = 1 cm, but this document creates no source or Unreal assets.

Material scale rules:

- Texture strokes, soot bands, ash deposits, mud streaks, cloth tears, rope wraps, rawhide lashings, and iron wear must be readable on Giant-scale ritual stones, not normal humanoid props.
- Stone fracture bands should usually read as broad 40-180 cm visual shapes on monoliths and slabs, with hairline cracks handled as future normal detail.
- Oxide red cloth strips should be large enough to read beside 442 cm and 470 cm Giant references but remain secondary to stone mass.
- Rope and rawhide wraps should feel hand-tied by Giants, using thick broad bands rather than thin decorative string.
- Horn and bone accents should stay sparse and scale-appropriate; they are warning accents, not dense surface patterning.

All scale language here is material readability guidance. It is not a collision guarantee, nav/pathfinding value, interaction distance, encounter spacing, gameplay radius, or implementation requirement.

## Materials and Color Palette

Primary ritual-stone material families:

- Rough highland stone: dark granite, weathered slate, field boulders, fractured slab faces, chipped edges, lichen hints, mineral streaks, soot-dark grooves, and ash dust.
- Soot: matte black-gray residue, cold burn halos, old fire stains, under-slab darkening, channel recess darkening, and pole-base scorch.
- Ash: cold pale-gray dust, settled camp residue, dry channel dust, wind-muted edge deposits, and soft value breakup at stone bases.
- Mud: trampled brown-gray earth, wet dark base stains, dried splatter, boot-worn gradients, cave-mouth grit, and packed highland dirt.
- Scorched timber: split dark posts, charred pole tips, burnt braces, weathered bark, muddy post feet, and rough static support wood.
- Rope and rawhide: thick rope lashings, sinew ties, rawhide strips, rough leather wraps, smoke staining, and muddy contact grime.
- Oxide red cloth: faded maroon warning strips, dull red wraps, chipped red paint, dirty cloth shadows, and controlled Blood Axe identity beats.
- Blackened iron: dull iron clamps, hammered dark steel, soot-stained rings, rough straps, broad edge wear, and crude plate repairs.
- Sparse old horn and dull bone: aged horn caps, dull bone tokens, tusk fragments, old non-graphic warning pieces, and worn ivory/tan accents.

Palette targets:

- Dominant stone and soot: `#17191A`, `#242729`, `#3C3D3A`, `#5A5A53`
- Mud and packed earth: `#2A2119`, `#403126`, `#5C4938`, `#75624E`
- Ash and cold dust: `#6F6D66`, `#8A867B`, `#ADA698`, `#C6BDAA`
- Scorched timber: `#1A110B`, `#352216`, `#58381F`, `#745232`
- Rope, rawhide, and worn leather: `#5B442B`, `#745C3C`, `#9A7A4E`, `#B09361`
- Oxide red and faded maroon: `#5A1412`, `#711B17`, `#84261E`, `#9C3A2D`
- Blackened iron and dull steel: `#101113`, `#222529`, `#3A3F41`, `#626664`
- Old horn and dull bone: `#766A52`, `#927E59`, `#B19A6D`, `#C8B98D`

Excluded neutral/civilized Giant materials:

- Blue-gray civic masonry, precise cave-town stone blocks, refined carved terraces, bridge and waterwork finish, warm hearth light, restrained blue rune accents, polished civic stoneworker marks, peaceful clan banners, orderly highland wayfinding, and clean hidden-settlement material polish.

Baseline emissive policy:

- No default emissive is approved. No ritual glow, torch VFX, signal glow, shamanic glow, forge heat, magic pulse, bloom behavior, animated material state, objective highlight, loot rarity cue, or gameplay-readable glow belongs to the baseline.
- Approval-gated emissive/VFX variants must be separately named, separately scoped, and separately approved before any material, texture, VFX/audio, graph, or Unreal work begins. They must remain sparse and must not replace the no-emissive baseline.

## Concept Image Prompt

Create an original stylized fantasy MMORPG material discipline board of `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01` for the world of Aerathea. The design should emphasize Blood Axe ritual-stone material swatches, rough highland stone, soot, ash, mud, scorched timber, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, dull bone, no-emissive baseline material rules, approval-gated emissive/VFX variant labels, hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and Giant scale readability beside female 442 cm and male 470 cm baselines from `SK_GIA_Base_A01`. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean docs-only material policy sheet with swatches, allowed and excluded material comparisons, future texture-map notes, usage ratios, scale references, and stop-gate labels. Avoid copying any existing franchise, avoid final material instances, avoid texture creation claims, avoid material graph diagrams, avoid VFX/audio cues, avoid DCC or FBX claims, avoid Unreal implementation claims, avoid startup placement, avoid final color approval, avoid final visual approval, avoid graphic gore, avoid readable rune text, avoid neutral Giant civic materials as Blood Axe defaults, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only material policy package. It does not authorize modeling, DCC source, mesh creation, terrain sculpting, retopo, UVs, bakes, proof renders, LOD source, collision proxies, FBX export, Unreal Content assets, material instances, texture assets, material graphs, VFX/audio, validators, runtime source, startup placement, final color approval, final visual approval, or first implementation target selection.

Future mesh packages, if separately approved, should model only large material-defining forms:

- Broad monolith planes, altar slab masses, cairn stack stones, dry channel lips, and major chipped silhouettes for rough highland stone.
- Large soot-darkened recess shapes, ash bases, mud plinths, trampled contact zones, and camp-residue silhouettes where they affect readability.
- Oversized scorched timber poles, braces, weighted bases, and broad static cloth strips.
- Thick rope and rawhide wraps only when they read as major lashings or structural ties.
- Large blackened iron clamps, rings, straps, and plate repairs where they affect silhouette.
- Sparse old horn and dull bone accents only when they create a clear secondary warning beat.

Keep these in future textures, normals, AO, roughness, masks, or shared swatch planning:

- Tiny cracks, soot speckles, ash flecks, mud droplets, wood grain, cloth weave, rope fibers, rawhide pores, stitch rows, small scratches, pitted metal, paint chips, lichen flecks, horn rings, bone pores, and minor dents.

Do not turn this document into a material-authoring ticket, DCC target, mesh target, trim-sheet ticket, shader task, Unreal task, VFX task, or final approval artifact.

## Texture and Material Notes

This document creates no textures, material instances, material functions, parent materials, shader graphs, trim sheets, texture assets, VFX materials, or audio-linked states. Names below are planning language only and require separate approval before authoring.

Standard future map outputs, if a later approved package creates assets:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Optional Emissive (`E`) only for a separately approved ritual, shamanic, torch, signal, forge, or magic variant; it is not part of the baseline

Material-family planning names only:

- `RitualStone_RoughHighlandStone`
- `RitualStone_SootAshMud`
- `RitualStone_ScorchedTimber`
- `RitualStone_RopeRawhide`
- `RitualStone_OxideRedCloth`
- `RitualStone_BlackenedIron`
- `RitualStone_OldHornDullBone`
- `RitualStone_ApprovalGatedEmissiveVariant`

These are not material instances, texture assets, shader graphs, or Unreal assets. They are reserved vocabulary for future package authors so material rules remain consistent.

Future consuming-mesh material slot guidance:

- Stone-only monoliths, altar slabs, cairns, and dry channel stones: 1 material target, 2 maximum if ash/mud or cloth/metal is part of the same approved mesh.
- Banner poles and mixed cave approach markers: 2 material target, 3 maximum for stone/timber, cloth/rawhide, and metal/bone/horn split.
- Review-only material boards, if separately approved: 1 non-shipping utility material, collision disabled, no gameplay function.
- Do not assign unique materials to each crack, cloth strip, rope knot, horn chip, bone token, soot patch, ash deposit, mud fleck, or paint chip.

ORM guidance for future planning:

- Ambient occlusion should emphasize broad overlaps, stone contact shadows, rope and rawhide lashing contacts, under-slab recesses, and ash/mud bases.
- Roughness should stay high for stone, soot, ash, mud, scorched timber, rope, rawhide, cloth, horn, and bone.
- Metallic should be reserved for blackened iron, dark steel, rings, straps, clamps, and crude plate repairs only.

## Triangle Budget

This documentation package creates no mesh and has no runtime triangle budget.

Future consuming packages should own their own budgets, but this material discipline should reduce geometry pressure:

- Rough highland stone: spend triangles on monolith mass, slab thickness, cairn stack read, and broad fractured planes; do not model tiny crack networks.
- Soot, ash, and mud: spend little or no geometry beyond large bases or plinth silhouettes; use future textures, masks, or vertex color planning for residue.
- Scorched timber: reserve geometry for pole mass, braces, split ends, and major broken silhouettes; do not model fine wood grain.
- Rope and rawhide: reserve geometry for major lashings and broad wraps only; do not model every fiber, stitch, or small tie.
- Oxide red cloth: reserve geometry for broad torn strips and large folds that read at MMO camera distance; do not model dense fray.
- Blackened iron: reserve geometry for large clamps, rings, straps, and plates; do not model tiny rivets or small scratches.
- Sparse old horn and dull bone: reserve geometry for a few large warning accents; do not build dense trophy clusters.
- Non-shipping material review boards, if separately approved: 500-3k tris per board, 1 material, collision disabled, not a game asset.

This package does not select a first DCC, Unreal, source asset, material, texture, VFX, or implementation target.

## LOD Plan

This package creates no LOD assets. Future material use must remain readable across LOD0-LOD3 on separately approved consuming meshes.

- LOD0: full broad material contrast, controlled oxide red cloth and paint accents, rough stone fractures, soot and ash grounding, mud contact zones, timber scorch, rope/rawhide wraps, blackened iron wear, and sparse horn/bone accents.
- LOD1: preserve major material zones and Blood Axe red/black read; reduce small cloth tears, secondary lashing loops, small paint chips, minor cracks, and tiny ash or mud flecks.
- LOD2: keep stone versus timber, cloth versus rawhide, iron versus soot, and horn/bone accents readable through broad masks and value grouping; remove most non-silhouette material-driven geometry.
- LOD3: preserve primary Blood Axe ritual-stone read: dark rough stone, soot/ash base value, controlled oxide red beats, major pole or cloth read, and sparse warning accents.

LOD reduction order:

1. Tiny scratches, fine cracks, wood grain, cloth weave, rope fibers, rawhide pores, soot speckles, ash flecks, mud droplets, pitting, small paint chips, lichen flecks, horn rings, and bone pores.
2. Small knots, tiny splinters, little stone chips, secondary cloth cuts, minor hide repairs, and small lashing loops.
3. Small horn or bone tokens, tiny iron nicks, minor straps, and non-silhouette scrap bits.
4. Hidden backside grime, underside detail, interior recess marks, and camera-hidden camp residue.
5. Minor plate bevels, shallow groove subdivisions, small cloth fold geometry, and secondary rock-plane cuts.
6. Only after small detail is removed, simplify the primary material zones that carry the Blood Axe ritual-stone read.

Never remove the no-emissive baseline, hostile Blood Axe material identity, Giant-scale readability, or separation from neutral/civilized Giant materials before reducing small detail.

## Collision Notes

This document defines no collision. It creates no collision proxies, UCX meshes, physics bodies, collision channels, nav blockers, smart links, gameplay volumes, validators, terrain collision, startup actors, or collision correctness claims.

Future collision policy for consuming meshes:

- Materials must not imply collision type, weak points, cover rules, damage zones, aura zones, objective zones, loot pickups, salvage behavior, harvesting nodes, trap behavior, or destructible states.
- Standing-stone, altar, cairn, channel-stone, banner-pole, and cave-marker packages must own their own collision notes in separate production packages.
- Cloth strips, soot, ash, mud, rope fibers, rawhide wraps, horn details, bone tokens, small iron repairs, scratches, chips, and material overlays should not receive per-detail collision.
- Non-shipping swatch or material review boards, if later approved, should have collision disabled by default.

No pathfinding, traversal proof, route validation, patrol marker, spawn space, projectile blocker, damage volume, aura volume, objective trigger, interaction trigger, pickup collision, or gameplay collision is defined here.

## Animation Notes

Baseline material discipline is static.

Allowed planning language:

- Static value variation for rough highland stone, soot, ash, mud, scorched timber, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, and dull bone.
- Static dirt, wear, chipped paint, cold burn marks, ash deposits, broad AO, and material age cues.
- Approval-gated emissive/VFX variants may be documented later only as separately named variants after explicit approval.

Not approved here:

- Animated material states, emissive pulses, ritual glow, shamanic glow, forge heat shimmer, torch flicker, signal fire, smoke, ash particles, cloth simulation, rope physics, destruction, collapse states, audio cues, VFX, Blueprint-driven material changes, gameplay feedback states, loot rarity glows, objective highlights, or magic path markers.

Any moving, glowing, audio-linked, interactive, destructible, or gameplay-readable material state requires a separately named package and explicit approval.

## Unreal Import Notes

No Unreal import is authorized by this package. Do not create Unreal assets, material instances, parent materials, material functions, texture assets, Blueprints, validators, startup actors, review-scene actors, VFX/audio, import scripts, source assets, or folder changes from this document.

Future planning targets, if a later implementation task approves them:

- Planned consuming mesh packages should keep materials with their owning asset packages, not this document.
- Planned material vocabulary should remain under Blood Axe ritual-stone naming and must not use neutral/civilized Giant culture names as defaults.
- `BC` textures should use sRGB enabled if future textures are approved.
- `N`, `ORM`, masks, and any future `E` map should use sRGB disabled if future textures are approved.
- Default texture targets should be 1K-2K for most reusable ritual-stone materials; 4K only for separately approved hero-scale close review.
- Material slots should stay low and reuse shared families instead of unique one-off materials per chip, cloth strip, rope knot, horn token, bone token, soot patch, ash deposit, or mud fleck.
- Default emissive is off and uncreated.

This document must not be treated as material graph authoring, shader approval, texture import approval, VFX approval, audio approval, DCC approval, FBX approval, Unreal import approval, startup placement approval, final color approval, final visual approval, final Blood Axe ritual approval, or first implementation target selection.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01/`
- Package file: `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01/PRODUCTION_PACKAGE.md`
- Asset/document ID: `DOC_GIA_BloodAxeRitualStoneMaterialDiscipline_A01`
- Parent kit: `KIT_GIA_BloodAxeRitualStones_A01`
- Parent intake row: `BloodAxeRitualStones_A01#MaterialDiscipline_A01`

Future planning names only:

- `RitualStone_RoughHighlandStone`
- `RitualStone_SootAshMud`
- `RitualStone_ScorchedTimber`
- `RitualStone_RopeRawhide`
- `RitualStone_OxideRedCloth`
- `RitualStone_BlackenedIron`
- `RitualStone_OldHornDullBone`
- `RitualStone_ApprovalGatedEmissiveVariant`

These names are not material instances, texture assets, shader graphs, VFX assets, audio assets, DCC files, FBX files, Unreal assets, startup actors, or final color approvals. They are reserved planning language only.

Do not create or edit `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, external concept folders, global indexes, task boards, backlog docs, bootstrap docs, unrelated production packages, validators, startup placement files, or any file outside this package path from this task.

## Quality Gate Checklist

- Universal 15-heading production-package format is present and unnumbered.
- Package is docs-only and creates no material instances, textures, material graphs, VFX, audio, DCC source, FBX exports, Unreal Content assets, runtime source, validators, startup placement, source concept movement, final color approval, final visual approval, final Blood Axe ritual approval, or first implementation target selection.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved female range 14-15 ft / 427-457 cm, and approved male range 14'10"-16'0" / 452-488 cm.
- Blood Axe is documented as a hostile Giant sub-faction only.
- Neutral/civilized Giant culture remains separate and is not overwritten by Blood Axe raider language.
- Required material families are covered: rough highland stone, soot, ash, mud, scorched timber, rope, rawhide, oxide red cloth, blackened iron, sparse old horn, and dull bone.
- Excluded neutral/civilized Giant materials are covered: blue-gray civic masonry, refined cave-town stonework, terraces, bridges, waterworks, warm hearth light, restrained blue runes, civic mason marks, peaceful highland wayfinding, and hidden-settlement polish.
- Default emissive, ritual glow, shamanic glow, signal glow, torch VFX, forge heat, animated material states, gameplay VFX, audio cues, objective markers, loot rarity cues, UI-like markers, readable rune text, and magic path markers are absent and approval-gated.
- Approval-gated emissive/VFX variants are documented only as separate future policy lanes; no material instance, texture, material graph, VFX/audio, DCC, FBX, Unreal, startup placement, or final color approval is created.
- Geometry guidance protects performance by modeling only large forms and pushing micro-detail into texture, normal, AO, roughness, and masks in future approved packages.
- Collision, LOD, animation, and import sections explicitly avoid implementation claims.
- The package supports future Blood Axe ritual-stone docs without selecting a first DCC, Unreal, source asset, material, texture, VFX, or implementation target.
