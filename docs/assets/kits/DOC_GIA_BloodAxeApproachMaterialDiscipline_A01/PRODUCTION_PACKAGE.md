## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeApproachMaterialDiscipline_A01`
- Asset type: Documentation-only material discipline package / swatch and usage guidance
- Task: `AET-MA-20260629-164`
- Parent kit: `KIT_GIA_BloodAxeStrongholdApproach_A01`
- Parent intake row: `BloodAxeStronghold.png#MaterialDiscipline`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Dependency references: `KIT_GIA_BloodAxeStrongholdApproach_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`, and the validated `SK_GIA_Base_A01` scale lock
- Status: docs-only production package ready for planning review

`DOC_GIA_BloodAxeApproachMaterialDiscipline_A01` defines the Blood Axe stronghold approach material language so future cliff, path, palisade, marker, barricade, and gate-framing packages stay visually consistent. It is a planning document only. It creates no material instances, textures, material graphs, VFX, audio, DCC source, FBX exports, Unreal Content assets, startup placement, source concept movement, final visual approval, final stronghold approval, or first implementation target selection.

Blood Axe approach materials must read as hostile Giant raider territory: fractured rock, packed earth, raw timber, blackened iron, chained scrap, scorched hide, oxide red cloth, soot, ash, and sparse non-graphic trophies. This language is not neutral or civilized Giant culture. Neutral/civilized Giants remain tied to hidden highland settlements, master stonework, blue-gray masonry, terraces, bridges, waterworks, warm hearth light, restrained blue runes, and civic stoneworker identity.

## Gameplay Purpose

The gameplay purpose is visual planning only. This document helps future environment and prop packages use consistent material signals before any DCC, Unreal, or gameplay implementation is selected.

Allowed planning uses:

- Establish Blood Axe approach swatches and usage ratios for future docs.
- Keep cliff walls, switchback paths, palisades, warning markers, overlook silhouettes, chained barricades, and gate-facing accents in the same hostile material family.
- Preserve readability at MMO camera distance through broad value groups, rough silhouettes, and limited oxide red accents.
- Separate hostile Blood Axe raider materials from neutral/civilized Giant culture.
- Document future texture, material-slot, LOD-read, and import constraints without creating assets.

Out of scope:

- Material instance creation, texture creation, material graph authoring, trim-sheet authoring, shader work, VFX, audio, DCC source, mesh work, terrain sculpting, FBX export, Unreal import, Blueprint work, validators, startup placement, source concept movement, final visual approval, final stronghold approval, first implementation target selection, gameplay pathing, nav rules, encounter design, destructible behavior, loot, crafting, economy, salvage, pickup behavior, or resource behavior.

## Silhouette Notes

Materials should support the large approach silhouettes instead of competing with them. Use surface treatment to make the route feel hostile, weathered, and Giant-built while leaving the primary read to cliff mass, palisade height, path shelves, marker stakes, chained plates, and gate-facing compression.

Material silhouette support:

- Fractured rock should read as broad angular slabs, dark clefts, chipped ledge backs, and heavy shadow bands. Avoid tiny crack carpets.
- Packed earth should read as wide trampled shelves, mud-dark edge bands, ash-stained foot traffic, and large worn path gradients. Avoid noisy pebble fields.
- Raw timber should read as oversized split logs, scorched stakes, heavy braces, and uneven palisade crowns. Fine wood grain stays in textures.
- Blackened iron should read as heavy bands, large clamps, rings, broad blade fragments, and dark plate edges. Avoid fields of tiny rivets.
- Chained scrap should read as major chain arcs, large broken plates, crude lash points, and heavy silhouettes. Do not build per-link curtains unless the chain is a primary shape.
- Scorched hide should read as broad hide panels, lash wraps, rough repairs, and soot-blackened edges. Do not use dense stitching as the main read.
- Oxide red cloth should appear as torn warning strips, large drapes, tied banners, and chipped paint accents in controlled beats. It must not become a full red environment wash.
- Soot and ash should ground bases, shadow recesses, forge-adjacent pieces, and old burn marks without flattening all values.
- Sparse non-graphic trophies should be secondary bone, horn, broken shield, or old weapon tokens. Avoid graphic gore, skull curtains, dense remains, or shock-detail piles.

Excluded neutral/civilized Giant material silhouettes: refined blue-gray masonry blocks, terrace retaining walls, carved civic stone, water channels, warm hearth stonework, clean highland bridge cuts, restrained blue rune inlays, and peaceful clan wayfinding markers.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author any future source in centimeters. 1 Unreal unit = 1 cm.
- This document does not change Giant race scale, skeleton policy, socket policy, capsule expectations, body proportions, or review scale.

Material scale rules:

- Texture strokes, chipped edges, cloth tears, soot stains, and metal wear must be readable on Giant-scale forms, not normal humanoid props.
- Rock fracture bands should often be 60-220 cm visual reads on cliff modules, with small fissures handled by normal detail.
- Packed-earth wear lanes should support 442 cm and 470 cm Giant scale references without defining nav widths or traversal metrics.
- Timber splits, scorch bands, and iron clamps should feel oversized and hand-built by Giants.
- Oxide red cloth strips should be large enough to read against cliffs and palisades but secondary to wall, gate, and cliff silhouettes.
- Bone, horn, and trophy accents should remain sparse and scale-appropriate; they are warning beats, not dense surface patterning.

All measurements are visual planning guidance. They are not nav/pathfinding values, collision guarantees, walkable route proofs, encounter lane dimensions, or implementation requirements.

## Materials and Color Palette

Primary Blood Axe approach material families:

- Fractured rock: dark highland stone, slate gray, blue-black shadow, chipped ledge faces, mineral streaks, soot-dark creases, and ash dust.
- Packed earth: trampled mud, compacted dirt, gravel pressed into path edges, charcoal dust, boot-worn brown-gray gradients, and dry ash overlays.
- Raw timber: split logs, dark bark, scorched post tips, rough braces, muddy post feet, and weathered palisade beams.
- Blackened iron: dull iron bands, hammered dark steel, soot-stained clamps, heavy rings, blade fragments, broad edge wear, and reference alignment with `MI_GIA_BloodAxeReforgedMetal_A01`.
- Chained scrap: oversized chain arcs, broken plates, reforged shield fragments, battered blade-fence pieces, and crude metal repairs.
- Scorched hide: blackened leather edges, rawhide lashings, hide wraps, rough repairs, sinew ties, and smoke staining.
- Oxide red cloth: torn warning strips, faded maroon banners, dull red war paint, chipped red marks, and dirty cloth shadows.
- Soot and ash: matte black-gray residue, burn halos, forge-adjacent dust, recess darkening, and pale ash settled into ground and ledges.
- Sparse non-graphic trophies: aged bone, old horn, tusk fragments, broken shield tokens, and dull weapon remnants used as secondary warning accents only.

Palette targets:

- Dominant rock and soot: `#17191A`, `#25282A`, `#3E3F3C`, `#5E5D56`
- Packed earth and mud: `#2D2118`, `#433226`, `#5E4A36`, `#76624B`
- Raw timber and scorched wood: `#1C120B`, `#392414`, `#5A3A20`, `#7A5634`
- Blackened iron and dark steel: `#101113`, `#232629`, `#3C4143`, `#626765`
- Oxide red and faded maroon: `#5F1513`, `#7A1D18`, `#8B2A21`, `#A24332`
- Hide, rope, and rawhide: `#5B442B`, `#7A6040`, `#A88958`
- Bone, horn, and ash accents: `#85775E`, `#A8946D`, `#C7B98F`, `#8A8275`

Excluded neutral/civilized Giant materials:

- Blue-gray civic masonry, precise stone blocks, refined cave-town carving, polished terrace stone, waterwork channels, warm hearth light, restrained blue rune accents, civic mason marks, clean highland bridge materials, peaceful clan banners, and orderly hidden-settlement finish.

No default emissive is approved. Torchlight, signal fire, forge heat, shamanic glow, ritual glow, magic material states, bloom behavior, or animated material states require separate approval and a different task.

## Concept Image Prompt

Create an original stylized fantasy MMORPG material discipline board of `DOC_GIA_BloodAxeApproachMaterialDiscipline_A01` for the world of Aerathea. The design should emphasize hostile Blood Axe Giant stronghold approach swatches, fractured rock, packed earth, raw timber, blackened iron, chained scrap, scorched hide, oxide red cloth, soot, ash, sparse non-graphic bone and horn trophies, broad MMO-readable material separation, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, and strict separation from neutral/civilized Giant culture. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean docs-only material usage sheet with swatches, usage-ratio callouts, scale references, allowed/excluded material comparisons, future texture-map notes, and stop-gate labels. Avoid copying any existing franchise, avoid creating final material instances, avoid texture creation claims, avoid material graph diagrams, avoid VFX or audio cues, avoid DCC or FBX claims, avoid Unreal implementation claims, avoid source concept embedding, avoid final visual approval, avoid final stronghold approval, avoid first implementation target selection, avoid graphic gore, avoid neutral Giant civic stoneworker materials as Blood Axe defaults, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only material discipline package. It does not authorize modeling, DCC source, terrain sculpt, mesh creation, retopo, UVs, bakes, collision proxies, proof renders, LOD source, FBX export, Unreal Content assets, material graph work, texture creation, VFX/audio, validators, runtime source, startup placement, final visual approval, final stronghold approval, or first implementation target selection.

Future mesh packages, if separately approved, should model only large material-defining forms:

- Broad cliff planes, major ledge breaks, overhang masses, large rubble stones, and dark recess shapes for fractured rock.
- Wide packed-earth shelves, major path lips, mud banks, log edging, and stone-chocked borders for approach paths.
- Large palisade posts, spike crowns, heavy braces, gate-flank returns, and primary raw timber silhouettes.
- Heavy iron bands, large clamps, rings, broad plate scraps, blade-fence inserts, and major chain runs where they affect silhouette.
- Large hide panels, major wraps, big lashings, and readable cloth strips.
- Sparse bone, horn, broken shield, or old weapon tokens only when they create a clear secondary warning beat.

Keep these in textures, normals, AO, masks, or shared trim sheets:

- Tiny cracks, gravel, fine scratches, wood grain, cloth weave, small runes if ever approved elsewhere, rope fibers, stitch rows, soot speckles, ash flecks, pitted metal, paint chips, tiny rivets, hairline burns, minor dents, and dense grime.

Do not turn this planning document into a material instance list, trim-sheet build ticket, DCC target, terrain implementation, or Unreal authoring task.

## Texture and Material Notes

This document creates no textures, material instances, material functions, parent materials, shader graphs, texture assets, VFX materials, or audio-linked states. Names below are future planning references only and require separate approval before authoring.

Standard future map outputs, if later approved:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Optional Emissive (`E`) only for a separately approved torch, forge heat, shamanic, ritual, signal, or magic variant

Future material-family planning names:

- `MI_GIA_BloodAxeApproachFracturedRock_A01`
- `MI_GIA_BloodAxeApproachPackedEarth_A01`
- `MI_GIA_BloodAxeApproachRawTimber_A01`
- `MI_GIA_BloodAxeApproachBlackenedIron_A01`
- `MI_GIA_BloodAxeApproachChainedScrap_A01`
- `MI_GIA_BloodAxeApproachScorchedHide_A01`
- `MI_GIA_BloodAxeApproachOxideRedCloth_A01`
- `MI_GIA_BloodAxeApproachSootAsh_A01`
- `MI_GIA_BloodAxeApproachBoneHornTrophy_A01`
- Existing reference: `MI_GIA_BloodAxeReforgedMetal_A01` for blackened/reforged metal language only

Future texture naming examples:

- `T_GIA_BloodAxeApproachFracturedRock_A01_BC`
- `T_GIA_BloodAxeApproachFracturedRock_A01_N`
- `T_GIA_BloodAxeApproachFracturedRock_A01_ORM`
- `T_GIA_BloodAxeApproachPackedEarth_A01_BC`
- `T_GIA_BloodAxeApproachRawTimber_A01_BC`
- `T_GIA_BloodAxeApproachBlackenedIron_A01_BC`
- `T_GIA_BloodAxeApproachOxideRedCloth_A01_BC`
- `T_GIA_BloodAxeApproachSootAsh_A01_BC`
- `T_GIA_BloodAxeApproachBoneHornTrophy_A01_BC`
- `T_GIA_BloodAxeApproachSignalOrForge_A01_E` only with later emissive approval

Material slot guidance for future consuming meshes:

- Cliff wall and ledge pieces: 1-2 slots, usually rock plus earth/ash blend.
- Packed-earth path pieces: 1-2 slots, earth plus rock/log-edge blend.
- Palisade and gate-flank pieces: 2-4 slots, timber, metal, cloth, and optional hide/bone accent.
- Warning markers: 1-3 slots, depending on timber, cloth, metal, bone, or horn split.
- Chained scrap and barricade accents: 2-3 slots, usually metal, timber, and cloth/hide.
- Review-only swatch or comparison boards: 1 non-shipping material if a future review task approves them.

ORM guidance:

- Ambient occlusion should emphasize broad overlaps, contact shadows, creases, chain undercuts, lashing contacts, and cliff recesses.
- Roughness should stay high for rock, earth, timber, cloth, hide, soot, ash, bone, and horn; blackened iron may have limited worn edge variation.
- Metallic should be reserved for iron, steel, chain, shield rims, blade fragments, and scrap plates only.

## Triangle Budget

This documentation package creates no mesh and has no runtime triangle budget.

Future consuming packages should keep their own budgets, but material discipline should support these planning ranges:

- Cliff-wall material samples on future mesh modules: no added triangles for tiny cracks, pebble fields, mineral streaks, or soot speckles.
- Packed-earth path modules: reserve geometry for shelf shape, path lip, large stones, and log edging; do not model granular dirt.
- Raw-timber palisade modules: reserve geometry for post mass, spike crowns, braces, and large lashings; do not model fine grain or every splinter.
- Blackened-iron and chained-scrap modules: reserve geometry for large plates, broad rings, silhouette chains, and major clamps; do not model tiny rivet carpets.
- Scorched-hide and oxide-red-cloth pieces: reserve geometry for broad cloth/hide silhouette, folds, and tears that read at camera distance; do not model dense stitching or fray.
- Sparse trophy accents: reserve geometry for a few large horn, bone, shield, or weapon-token shapes; do not build dense trophy curtains.
- Non-shipping swatch boards, if separately approved for review only: 500-3k tris per board, 1 material, collision disabled, not a game asset.

The material plan should reduce geometry pressure by pushing micro-detail into texture, normal, AO, and roughness maps. It must not encourage one-off high-poly surfaces for every Blood Axe approach piece.

## LOD Plan

This package creates no LOD assets. Future material usage must remain readable across LOD0-LOD3 on consuming meshes.

- LOD0: full material contrast, broad color zones, readable oxide red cloth/paint accents, soot/ash grounding, rock fractures, timber scorch, metal edge wear, and sparse trophy accents.
- LOD1: preserve major material zones and Blood Axe red/black read; reduce small cloth tears, minor chain subdivisions, small paint chips, fine cracks, and secondary surface cuts.
- LOD2: keep rock versus earth, timber versus metal, cloth versus hide, and trophy accents readable through broad masks and value grouping; remove most non-silhouette material-driven geometry.
- LOD3: preserve primary Blood Axe approach read: dark fractured rock, packed-earth path bands, raw timber masses, blackened metal accents, controlled oxide red beats, and soot/ash value grounding.

LOD reduction order:

1. Tiny scratches, fine cracks, wood grain, cloth weave, stitch rows, soot speckles, ash flecks, pitting, small paint chips, and rope fibers.
2. Small knots, tiny splinters, small stones, little straps, secondary cloth cuts, and minor hide repairs.
3. Small trophy tokens, small chain segments, tiny blade nicks, and non-silhouette scrap bits.
4. Hidden backside grime, underside detail, interior recess marks, and camera-hidden path clutter.
5. Minor plate bevels, small lashing loops, cloth fold geometry, and secondary rock-plane cuts.
6. Only after secondary detail is removed, simplify the primary material zones that carry the Blood Axe approach read.

Never remove the hostile Blood Axe material identity, Giant-scale readability, or separation from neutral/civilized Giant materials before reducing small detail.

## Collision Notes

This document defines no collision. It creates no collision proxies, UCX meshes, physics bodies, collision channels, nav blockers, nav links, gameplay volumes, validators, terrain collision, startup actors, or collision correctness claims.

Future collision policy for consuming meshes:

- Materials must not imply collision type, weak points, cover rules, damage zones, loot pickups, salvage behavior, harvesting nodes, trap behavior, or destructible states.
- Cliff, path, palisade, marker, and barricade packages must own their own collision notes in separate production packages.
- Cloth strips, small chains, soot, ash, trophies, rope, hide wraps, scratches, chips, and material overlays should not receive per-detail collision.
- Non-shipping swatch or review boards, if later approved, should have collision disabled by default.

No pathfinding, traversal proof, slope rule, route validation, patrol marker, spawn space, projectile blocker, damage volume, objective trigger, interaction trigger, pickup collision, or gameplay collision is defined here.

## Animation Notes

Baseline material discipline is static.

Allowed planning language:

- Static value variation for rock, earth, timber, iron, chained scrap, hide, cloth, soot, ash, bone, and horn.
- Static dirt, wear, red cloth age, chipped paint, burn marks, and broad AO/depth cues.

Not approved here:

- Animated material states, emissive pulses, forge heat shimmer, torch flicker, signal fire, smoke, ash particles, cloth simulation, chain physics, destruction, collapse states, audio cues, VFX, Blueprint-driven material changes, gameplay feedback states, loot rarity glows, objective highlights, or magic path markers.

Any moving, glowing, audio-linked, interactive, destructible, or gameplay-readable material state requires a separately named package and explicit approval.

## Unreal Import Notes

No Unreal import is authorized by this package. Do not create Unreal assets, material instances, parent materials, material functions, texture assets, Blueprints, validators, startup actors, review-scene actors, or folder changes from this document.

Future planning targets, if a later implementation task approves them:

- Planned Unreal folder family: `/Game/Aerathea/Materials/Giants/BloodAxe/Approach/`
- Planned material prefix: `MI_GIA_BloodAxeApproach`
- Planned texture prefix: `T_GIA_BloodAxeApproach`
- Planned consuming mesh folders should remain with their owning asset packages, not this document.
- `BC` textures use sRGB enabled.
- `N`, `ORM`, masks, and any future `E` map use sRGB disabled.
- Default texture targets should be 1K-2K for most reusable approach materials; 4K only for separately approved hero-scale close review.
- Material slots should stay low and reuse shared families instead of unique one-off materials per chip, cloth strip, chain, trophy token, or ash patch.
- Default emissive is off and uncreated.

This document must not be treated as material graph authoring, shader approval, texture import approval, VFX approval, audio approval, DCC approval, Unreal import approval, startup placement approval, final visual approval, final stronghold approval, or first implementation target selection.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/DOC_GIA_BloodAxeApproachMaterialDiscipline_A01/`
- Package file: `docs/assets/kits/DOC_GIA_BloodAxeApproachMaterialDiscipline_A01/PRODUCTION_PACKAGE.md`
- Asset/document ID: `DOC_GIA_BloodAxeApproachMaterialDiscipline_A01`
- Parent kit: `KIT_GIA_BloodAxeStrongholdApproach_A01`
- Parent intake row: `BloodAxeStronghold.png#MaterialDiscipline`
- Reference material package: `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md`

Future planning names only:

- `MI_GIA_BloodAxeApproachFracturedRock_A01`
- `MI_GIA_BloodAxeApproachPackedEarth_A01`
- `MI_GIA_BloodAxeApproachRawTimber_A01`
- `MI_GIA_BloodAxeApproachBlackenedIron_A01`
- `MI_GIA_BloodAxeApproachChainedScrap_A01`
- `MI_GIA_BloodAxeApproachScorchedHide_A01`
- `MI_GIA_BloodAxeApproachOxideRedCloth_A01`
- `MI_GIA_BloodAxeApproachSootAsh_A01`
- `MI_GIA_BloodAxeApproachBoneHornTrophy_A01`

These names are not created assets. They are reserved planning language for a future material-authoring task if one is approved.

## Quality Gate Checklist

- Universal 15-heading production-package format is present and unnumbered.
- Package is docs-only and creates no material instances, textures, material graphs, VFX, audio, DCC source, FBX exports, Unreal Content assets, runtime source, validators, startup placement, source concept movement, final visual approval, final stronghold approval, or first implementation target selection.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved female range 14-15 ft / 427-457 cm, and approved male range 14'10"-16'0" / 452-488 cm.
- Blood Axe is documented as a hostile Giant sub-faction only.
- Neutral/civilized Giant culture remains separate and is not overwritten by Blood Axe raider language.
- Required material families are covered: fractured rock, packed earth, raw timber, blackened iron, chained scrap, scorched hide, oxide red cloth, soot, ash, and sparse non-graphic trophies.
- Excluded neutral/civilized Giant materials are covered: blue-gray civic masonry, refined cave-town stonework, terraces, bridges, waterworks, warm hearth light, restrained blue runes, civic mason marks, and peaceful highland settlement cues.
- Default emissive, animated material states, VFX, audio, gameplay glow, objective markers, loot rarity cues, and magic path markers are absent and approval-gated.
- Geometry guidance protects performance by modeling only large forms and pushing micro-detail into texture, normal, AO, roughness, and masks.
- Texture and Unreal names are future planning references only and do not authorize asset creation.
- Collision, LOD, animation, and import sections explicitly avoid implementation claims.
- The package supports future Blood Axe approach docs without selecting a first DCC, Unreal, source asset, material, texture, or implementation target.
