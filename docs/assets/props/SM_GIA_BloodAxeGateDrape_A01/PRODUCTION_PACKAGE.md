# SM_GIA_BloodAxeGateDrape_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeGateDrape_A01`
- Asset type: Static Mesh production package / Giant-scale static gate cloth panel
- Task: `AET-MA-20260629-130`
- Parent kit: `KIT_GIA_BloodAxeCamp_A01`
- Source child ID: `BloodAxeGate.png#Banner_GateDrape`
- Related packages: `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeTrophyGate_A01`, `KIT_GIA_BloodAxeBannerLine_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only static visual production package ready for planning review
- Source-storage guardrail: source concepts remain external through existing intake records. Do not copy, move, crop, edit, embed, inspect for final approval, or commit source images for this task.

`SM_GIA_BloodAxeGateDrape_A01` defines a large torn red cloth panel tied to Blood Axe gate compositions. It should read as a brutal warning mark fastened to a Giant-scale camp gate, palisade threshold, or trophy-gate frame through a broad red cloth block, heavy lashing, soot-dark weathering, and crude blackened hardware.

This is a static readable cloth panel tied to gate composition, not a simulated banner or interactive gate object. Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture. Blood Axe visual language must stay separate from neutral/civilized Giant culture and must not become the default banner, civic marker, cave-town cloth, or highland clan symbol set for all Giants.

This package is planning only. It does not authorize DCC source creation, source-folder creation, FBX export, Unreal Content creation, material graph authoring, collision proxy creation, cloth/physics setup, banner animation, gate interaction, destructible behavior, runtime source, startup placement, final visual approval, first DCC target selection, global documentation edits, or source concept movement.

## Gameplay Purpose

The gameplay purpose is visual readability only. The drape helps players identify a Blood Axe gate or threshold as hostile Giant territory before reading smaller props, sentries, path markers, or barricades.

Allowed planning purpose:

- Static visual faction marker for Blood Axe camp gates, trophy gates, palisade gaps, stronghold approaches, and gate-review compositions.
- Red cloth mass that helps distinguish Blood Axe camp entrances from neutral/civilized Giant cave-town gates or nomad markers.
- Gate-composition dressing that can be paired visually with `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeTrophyGate_A01`, and banner-line modules.
- Scale reference for Giant-built camp cloth, lashings, and gate hardware using the validated Giant baselines.

Out of scope:

- Cloth simulation, wind motion, vertex sway, banner physics, rope physics, gate opening, gate closing, lock/key behavior, triggers, interaction prompts, capture/objective behavior, destructible cloth, damage states, fire spread, VFX, audio, morale/faction aura behavior, AI behavior, nav behavior, encounter scripting, loot, resource, crafting, economy, startup placement, final visual approval, or first build target selection.

## Silhouette Notes

Primary silhouette: one broad torn cloth panel or paired overlapping panels hanging from a heavy gate crossbeam, side post, or trophy-gate frame. The shape should be readable at MMO camera distance as a crude Blood Axe warning drape: broad red mass first, ragged lower edge second, then heavy ties and dark hardware.

Key visual reads:

- Large oxide-red cloth field with a blunt top attachment line and a torn lower edge.
- One dominant center panel for the default `A01` read, with optional shorter side flap planning if a later visual composition needs asymmetry.
- Broad triangular tears, split tails, and missing corner chunks that read from distance without becoming many thin strips.
- Thick rope, rawhide lashing, blackened iron rings, clamp plates, or crude hooks along the top edge.
- Dark soot, mud stains, faded black paint, and worn red patching to keep it brutal and camp-made.
- Optional abstract Blood Axe warning mark as painted slash, broad axe-like smear, or black hand-applied symbol. Avoid readable text, modern icons, or UI marker shapes.
- Optional sparse horn, bone, or broken shield tokens near the top corners only if they remain secondary to the cloth panel.
- Gate context should be implied through attachment placement and scale, not by turning this asset into a full gate.

Model as real geometry when promoted later:

- Main cloth panel shape, broad torn silhouette, rolled or folded top hem, large lower tears, thick edge folds, major knots, top rope or rod, big rings, clamp plates, and large patches that affect the silhouette.

Keep in textures or normal maps:

- Cloth weave, tiny fray threads, stitch holes, small scratches, soot speckles, mud flecks, paint flakes, light wrinkles, small punctures, rope fibers, leather pores, metal pitting, and minor edge wear.

Avoid:

- Neutral/civilized Giant blue-gray stoneworker motifs, warm hearth symbols, refined highland clan cloth, restrained blue runes, civic cave-town banners, many tiny strips, dense skull strings, graphic gore, fresh remains, glowing quest-marker shapes, readable text, or one-note red-only material treatment.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author all future source in centimeters. 1 Unreal unit = 1 cm.

Recommended static drape dimensions:

- Default center drape width: 300-560 cm.
- Default center drape drop: 260-430 cm.
- Optional side flap width: 120-240 cm per flap.
- Optional side flap drop: 180-340 cm.
- Cloth thickness: 2-6 cm as a shaped static shell or doubled panel edge, not a physical cloth asset.
- Top hem, rope, or rod diameter: 12-35 cm.
- Large rings or clamp plates: 25-70 cm across, sized for Giant-scale hardware.
- Main patch shapes: 60-180 cm across, used sparingly.
- Major tear cuts: 40-180 cm tall or wide, kept bold and readable.
- Planned gate attachment height: usually 700-920 cm above ground on a Giant gate crossbeam or high post, depending on the parent gate frame.
- Lowest hanging edge: usually 280-520 cm above ground when over a passage, or lower if mounted to the side of a closed/static visual gate. This does not define nav clearance or gate behavior.

The drape should feel oversized for normal humanoids and appropriate for the 470 cm male Giant baseline. It should never shrink into a human-scale banner, tavern sign, UI marker, or ordinary settlement pennant.

## Materials and Color Palette

Primary materials:

- Torn oxide-red war cloth, faded maroon canvas, dirty red patch cloth, and soot-dark lower edges.
- Thick rope, rawhide cord, sinew ties, scorched leather straps, and hide wrap reinforcement.
- Blackened iron, dark steel rings, crude hooks, clamp plates, and old gate hardware.
- Packed mud, ash, soot, charcoal, and grime collected along lower folds.
- Sparse aged bone, horn, broken shield, or dull metal warning tokens only if needed for Blood Axe context.

Palette targets:

- Blood Axe red cloth and paint: `#5F1513` to `#8B211B`
- Dull maroon shadows: `#35100E` to `#4B1714`
- Charcoal soot and blackened iron: `#111214` to `#2A2C2E`
- Rope, rawhide, and scorched leather: `#5C422A` to `#A17B4E`
- Mud and ash: `#1B1712` to `#403025`
- Aged bone or horn accents: `#9E8C6B` to `#CDB78A`

Material identity:

- Red cloth should be the dominant read, but value variation, soot, mud, blackened hardware, rope, and rawhide must prevent a flat red rectangle.
- No default emissive is approved.
- Any ritual glow, shamanic mark, torch response, signal flare, animated material, faction aura, capture marker, or VFX state requires a separate approval-gated package.
- Avoid neutral/civilized Giant material language: carved blue-gray masonry, warm hearth light, civic stoneworker patterns, clean highland clan cloth, terrace/waterwork symbols, restrained blue runes, or peaceful settlement ornament.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeGateDrape_A01` for the world of Aerathea. The design should emphasize a static Giant-scale Blood Axe gate drape, one broad torn oxide-red cloth panel tied to a rough gate crossbeam, heavy rope and rawhide lashings, blackened iron rings and clamp plates, faded black warning paint, soot, mud, ash, scorched leather reinforcement, large readable lower tears, hostile Giant sub-faction identity, clear separation from neutral/civilized Giant culture, and the gameplay role of non-interactive gate-threshold readability. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh production sheet with front view, rear view, side thickness view, top attachment detail, material swatches, LOD and collision planning callouts, and scale markers beside a 442 cm female Giant and a 470 cm male Giant, with a simple ghosted gate frame only for context. Avoid copying any existing franchise, avoid making Blood Axe visual language the default Giant culture, avoid neutral Giant cave-town or highland civic symbols, avoid cloth simulation diagrams, avoid banner animation, avoid gate interaction, avoid destructible behavior, avoid objective/capture UI shapes, avoid readable text, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Source reference note: use `BloodAxeGate.png#Banner_GateDrape` only as an intake route reference. This docs-only package does not copy, move, crop, inspect for final approval, embed, edit, or commit external source concept imagery.

## Modeling Notes

This is a docs-only modeling plan. No Blender file, sculpt, retopo, UV, bake, proof render, collision proxy, LOD source, FBX, Unreal asset, material graph, validator, source asset, or startup placement is created or approved by this package.

Future modeling should prioritize these readable forms:

- One main static cloth mesh with a broad rectangular or shield-like red mass and a ragged lower silhouette.
- A thick top hem, folded sleeve, rope wrap, or beam-tied edge that explains how the drape is attached.
- Large torn cuts and missing corner chunks as modeled silhouette geometry.
- A few broad folds or weighted vertical sag lines sculpted into the static mesh, not generated by cloth simulation.
- Thick rope knots, rawhide bands, blackened rings, clamp plates, and crude hooks at major attachment points.
- Optional secondary side flap or patch layer if it improves asymmetry without turning the asset into a full banner-line kit.
- Optional sparse horn, bone, or broken shield token at top corners only if the final drape still reads primarily as cloth.
- Back side should be simpler but believable, with seam, fold, and tie indications because the gate may be viewed from either side.

Use textures, normals, and masks for:

- Cloth weave, fine wrinkles, fray fibers, stitch holes, faded red dye, mud stains, soot gradients, ash flecks, paint chips, rope fibers, leather pores, small scratches, metal pitting, tiny nail heads, and small punctures.

Simplification rules:

- Keep the red cloth block and torn bottom silhouette readable before adding small surface detail.
- Keep edge cuts large and few. Do not fill the bottom with dozens of tiny strips.
- Keep hardware chunky and sparse. Do not model every ring, knot, stitch, rivet, or fray strand.
- Do not include parent gate posts, full crossbeams, doors, hinges, collision blockers, trigger markers, nav markers, or gameplay affordances in this mesh.
- Do not select a mesh split, source folder, or first DCC target from this package.

## Texture and Material Notes

Target material slot count:

- Preferred: 2 material slots.
- Maximum: 3 material slots if hardware or token accents require a separate shared material.

Suggested future slots:

- Slot 0: `MI_GIA_BloodAxeRedCloth_A01` for red cloth, faded paint, dirt masks, patch cloth, and cloth wear.
- Slot 1: `MI_GIA_BloodAxeRopeHide_A01` or `MI_GIA_BloodAxeBannerLineHardware_A01` for rope, rawhide, leather, rings, hooks, and clamps.
- Optional slot 2: `MI_GIA_BloodAxeBlackenedIron_A01` or `MI_GIA_BloodAxeBoneTrophy_A01` only if hardware or sparse tokens cannot be handled through shared atlases.

Required future texture maps:

- `T_GIA_BloodAxeGateDrape_A01_BC`
- `T_GIA_BloodAxeGateDrape_A01_N`
- `T_GIA_BloodAxeGateDrape_A01_ORM`

Optional future texture maps only after separate approval:

- `T_GIA_BloodAxeGateDrape_A01_E` for a separately approved ritual, shamanic, torch-lit, or signal variant. The baseline gate drape has no emissive.
- `T_GIA_BloodAxeGateDrape_A01_Mask` if future material variation needs controlled soot, mud, faded paint, or edge-wear blending.

Texture resolution targets:

- Default gate drape: 1K-2K texture set.
- Close hero threshold variant: 2K, only if explicitly approved with a hero gate composition.
- Far camp silhouette or repeated drape variant: 512-1K shared atlas.

Packed ORM guidance:

- R: Ambient occlusion under top folds, attachment wraps, rings, patches, knots, tear overlaps, and heavy lower folds.
- G: High roughness for cloth, rope, leather, soot, mud, and bone; medium-high varied roughness for blackened iron.
- B: Metallic only for iron rings, hooks, clamp plates, and other metal hardware.

Do not create unique material slots for every patch, tear, ring, knot, stain, paint mark, or token.

## Triangle Budget

`SM_GIA_BloodAxeGateDrape_A01` is a large static gate-dressing prop. It should stay cheaper than a full gate while retaining a strong cloth silhouette.

Targets:

- LOD0 target: 3k-6k tris.
- LOD0 hard cap: 8k tris.
- Material slots: 2 target, 3 maximum.
- Texture set: 1K-2K standard; 2K only for close gate review or hero threshold approval.

Suggested LOD0 allocation:

- Main cloth panel, broad folds, large torn silhouette, thickened edges, and top hem: 55-65 percent.
- Rope, rawhide, knots, rings, hooks, and clamp hardware: 18-25 percent.
- Patch shapes, large painted-symbol geometry if needed, and optional side flap: 8-12 percent.
- Sparse horn, bone, broken shield, or token accents: 0-8 percent.
- Minor bevels and backside support only after primary cloth and attachment reads are clear.

Do not spend geometry on tiny fray fibers, stitch rows, cloth weave, small holes, many dangling strips, tiny rivets, dense chain links, small scratches, soot speckles, or mud flecks.

## LOD Plan

All future approved mesh work should include LOD0-LOD3.

- LOD0: 3k-6k tris target, 8k hard cap. Full static cloth silhouette, thick top hem, broad torn lower edge, large folds, major patches, main lashing, rings, clamps, hooks, and sparse token accents.
- LOD1: 60-70 percent of LOD0. Reduce secondary cloth fold loops, minor edge cuts, knot bevels, backside folds, small patch bevels, and hardware subdivisions.
- LOD2: 35-45 percent of LOD0. Preserve the main red cloth block, top attachment line, lower torn read, and major dark hardware shapes while flattening folds and removing secondary tokens.
- LOD3: 15-25 percent of LOD0. Preserve the overall red silhouette, ragged bottom contour, and top attachment bar or rope. Remove most hardware, backside detail, small patches, and minor tear cuts.

Reduction order:

1. Tiny fray cuts, stitch holes, small punctures, soot chips, and minor paint chips.
2. Small patch bevels, secondary fold loops, backside seam details, and minor wrinkles.
3. Secondary knots, small rings, small hooks, and thin lashings.
4. Optional horn, bone, shield, or token accents.
5. Top hardware bevels, cloth thickness subdivisions, and lower tear subdivisions.
6. Only then simplify the main cloth outline, top attachment read, and Blood Axe red mass.

Never reduce the primary red drape silhouette, top attachment read, or hostile Blood Axe gate identity before removing small detail.

## Collision Notes

Collision is planning only. Do not create collision proxies, UCX meshes, physics bodies, runtime collision channels, nav links, nav blockers, damage volumes, interaction volumes, cloth collision, or validation scripts from this task.

Future static collision intent:

- Default collision: disabled.
- Main cloth panel: no player collision, no camera collision, no cloth collision, and no per-tear collision.
- Rope, rings, hooks, clamps, tokens, and patches: no individual collision.
- If a future map needs selection or broad editor bounds, use generated bounds or a simple non-blocking editor-only selection shape.
- If the drape is composed directly onto a blocking gate, collision belongs to the parent gate or approved gate mesh, not this drape package.

This package does not define navmesh behavior, AI routes, patrol points, cover tags, door states, interaction channels, objective volumes, destruction, damage, traversal policy, or gate passability.

## Animation Notes

Baseline asset is static.

Approved at planning level:

- Static Mesh gate drape with fixed cloth silhouette, fixed top ties, fixed hardware, fixed patches, and fixed warning paint.
- Optional future material wear variations for soot, mud, faded dye, or paint damage, without runtime behavior claims.

Not approved here:

- Cloth simulation, vertex wind, cloth bones, banner waving, rope physics, hanging prop sway, physics bodies, wind response, destructible cloth, tear propagation, burn states, collapse states, gate opening, gate closing, interaction prompts, capture behavior, faction aura behavior, AI behavior, VFX, audio, or animated material state logic.

Any moving, simulated, interactive, or destructible version must be split into a separately approved variant or implementation task.

## Unreal Import Notes

No Unreal import is authorized by this docs-only package. The following notes are future planning only.

Planned future Unreal asset:

- Asset name: `SM_GIA_BloodAxeGateDrape_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/Gates/`
- Alternate prop folder if separated from gate structures: `/Game/Aerathea/Props/Giants/BloodAxeCamp/GateDrapes/`
- Materials folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures folder: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/Gates/`
- Import scale: centimeter-authored source, Unreal import scale 1.0 after future DCC/export validation.
- Pivot: top center on the attachment line for placement against a parent gate crossbeam. If later composed into a full gate mesh, the parent gate keeps its own ground-centered pivot.
- Forward orientation: primary cloth read faces +X unless a later project import convention overrides it.
- Bounds: include full static cloth, top rope or hardware, lower torn edge, and optional side flap.
- Collision type: collision disabled by default.
- LODs: LOD0, LOD1, LOD2, LOD3 required before any production import approval.
- Material slot count: 2 target, 3 maximum.
- Texture list: `T_GIA_BloodAxeGateDrape_A01_BC`, `T_GIA_BloodAxeGateDrape_A01_N`, `T_GIA_BloodAxeGateDrape_A01_ORM`.
- Optional texture: `T_GIA_BloodAxeGateDrape_A01_E` only for a separately approved emissive variant.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: favor shared Blood Axe cloth, rope, and hardware materials; reduce tear, fold, knot, and hardware detail before reducing the broad red cloth silhouette.

Candidate future parent-gate attachment markers, if separately approved:

- `gate_drape_socket`
- `gate_drape_socket_l`
- `gate_drape_socket_r`

These are planning notes only. Do not author sockets, transforms, attachment Blueprints, gate behavior, VFX hooks, gameplay links, or startup placement from this package.

## Folder and Naming Recommendation

Docs:

- Package folder: `docs/assets/props/SM_GIA_BloodAxeGateDrape_A01/`
- Package file: `docs/assets/props/SM_GIA_BloodAxeGateDrape_A01/PRODUCTION_PACKAGE.md`

Related docs:

- Parent camp child intake: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md`
- Related main gate package: `docs/assets/props/SM_GIA_BloodAxeCampGate_A01/PRODUCTION_PACKAGE.md`
- Related trophy gate package: `docs/assets/props/SM_GIA_BloodAxeTrophyGate_A01/PRODUCTION_PACKAGE.md`
- Related banner-line kit package: `docs/assets/kits/KIT_GIA_BloodAxeBannerLine_A01/PRODUCTION_PACKAGE.md`

Future source/export paths, pending separate approval only:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeGateDrape_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeGateDrape_A01.fbx`
- Unreal: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/Gates/`

Naming:

- Static mesh: `SM_GIA_BloodAxeGateDrape_A01`
- Optional shorter side variant: `SM_GIA_BloodAxeGateDrape_Side_A01`, approval-gated
- Optional torn lower variant: `SM_GIA_BloodAxeGateDrape_Torn_A01`, approval-gated
- Material instances: `MI_GIA_BloodAxeRedCloth_A01`, `MI_GIA_BloodAxeRopeHide_A01`, optional `MI_GIA_BloodAxeBlackenedIron_A01`
- Texture maps: `T_GIA_BloodAxeGateDrape_A01_BC`, `T_GIA_BloodAxeGateDrape_A01_N`, `T_GIA_BloodAxeGateDrape_A01_ORM`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, UV files, bake outputs, collision proxy files, FBX exports, Unreal Content assets, material graphs, runtime source, tools, validators, startup-scene actors, copied source concepts, embedded concept images, global index entries, task-board edits, backlog edits, bootstrap edits, final approval captures, or external concept-folder edits from this task.

## Approval Gates and Stop Points

- Stop before creating DCC source, source folders, Blender files, proof renders, LOD source meshes, collision proxy meshes, FBX exports, Unreal imports, material graphs, material instances, texture assets, Blueprints, runtime source, tools, validators, startup placements, or global documentation updates.
- Stop before copying, moving, cropping, editing, embedding, inspecting for final approval, or committing external source concept images.
- Stop before selecting this drape as a first DCC build target or final visual approval target.
- Stop before defining cloth simulation, cloth/physics setup, vertex wind, banner animation, rope physics, hanging prop sway, destructible behavior, tear propagation, burn states, collapse states, VFX, audio, animated material behavior, or faction aura behavior.
- Stop before defining gate opening behavior, hinge behavior, portcullis behavior, lock/key logic, interaction prompts, usable doors, objective capture, damage behavior, repair states, navmesh links, nav blockers, AI cover, patrol behavior, spawn rules, encounter layout, combat timing, trigger volumes, or gameplay collision channels.
- Stop if the design starts using neutral/civilized Giant culture as the primary identity: blue-gray carved masonry, cave-town civic pride, warm hearth halls, restrained blue runes, refined stonework, terrace/waterwork motifs, or peaceful highland clan banners.
- Stop if the drape appears to require changing the validated Giant scale lock: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved range females 14-15 ft and males 14'10"-16'0".
- Stop if material count exceeds 3 slots or LOD0 exceeds 8k tris without explicit hero-threshold approval.

## Quality Gate Checklist

- Blood Axe is clearly a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Blood Axe visual language must stay separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Asset is a static readable cloth panel tied to gate composition, not a simulated banner or interactive gate object.
- Silhouette reads at MMO camera distance: broad oxide-red cloth, top attachment line, large lower tears, heavy rope/rawhide ties, and sparse blackened hardware.
- Materials use Blood Axe red cloth, soot, mud, ash, rope, rawhide, scorched leather, blackened iron, and optional sparse aged bone or horn consistently.
- Neutral/civilized Giant cave-town stonework, civic highland banner language, warm hearth identity, terrace/waterwork motifs, clean blue-gray masonry, and restrained blue runes are excluded from the baseline.
- Emissive, ritual glow, signal glow, faction aura, animated material states, and gameplay VFX are absent and approval-gated for separate variants.
- Tiny fray, cloth weave, stitch holes, scratches, soot speckles, mud flecks, paint chips, rope fibers, leather pores, and metal pitting are assigned to textures or normals instead of geometry.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision planning, animation limits, Unreal import planning, folder naming, approval gates, and explicit stop points are included.
- Collision defaults to disabled and does not claim collision proxy creation, per-cloth collision, nav behavior, interaction behavior, damage behavior, or gate passability.
- Package remains docs-only static visual planning and makes no DCC, FBX, Unreal Content, SourceAssets, material graph, collision proxy, runtime source, validator, startup placement, interaction, gate behavior, destructible behavior, AI, nav, first build target, final approval, global docs edit, or source concept movement claim.
