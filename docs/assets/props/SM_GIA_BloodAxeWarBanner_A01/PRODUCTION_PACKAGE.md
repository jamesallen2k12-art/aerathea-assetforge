# SM_GIA_BloodAxeWarBanner_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeWarBanner_A01`
- Asset type: Static Mesh production package / hostile camp marker prop
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source child ID: `BloodAxeArmory.png#Banner_WarCamp`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready

`SM_GIA_BloodAxeWarBanner_A01` is a hostile Blood Axe camp marker, warband rally point, and territorial warning prop for Giant raider spaces. It uses torn red cloth, rough pole construction, blackened iron bindings, crude bone or trophy accents, soot, hide ties, and blunt raider geometry to identify a dangerous Blood Axe presence at a distance. It is not a default Giant banner and must stay visually separate from neutral/civilized Giant cave-town, stoneworker, highland nomad, or shamanic culture.

This package is planning only. It does not authorize DCC source creation, FBX export, Unreal Content creation, startup placement, source-concept copying, cloth simulation, faction aura gameplay, final visual approval, or runtime implementation.

## Gameplay Purpose

The banner supports Blood Axe encounter readability by marking hostile camps, armory yards, watch posts, raider gates, arena edges, siege staging areas, and loot/display compositions. Its main gameplay value is quick faction recognition: players should read the red torn banner and brutal Giant-scale pole language before they identify individual weapons or enemies.

Expected use cases:

- Static camp dressing for Blood Axe war camps and armory scenes.
- Territorial marker near Giant raider patrol routes, gates, cages, weapon racks, or command tents.
- Visual anchor for future encounter layouts without adding gameplay logic in this task.
- Optional carried-banner or rally-object variants only after separate approval.

Cloth simulation, wind-driven cloth deformation, destructible cloth, interactive capture mechanics, enemy buffs, player debuffs, faction aura effects, objective logic, VFX pulses, and audio cues are out of scope and approval-gated.

## Silhouette Notes

Primary silhouette must read as a Giant-scale hostile war banner from MMO camera distance:

- Tall rough pole with a heavy base footprint and overbuilt bindings.
- Wide torn red cloth panel or split-tail pennant hanging from a brutal crossbar.
- Large diagonal tears and asymmetric lower cloth points for a raider-camp read.
- Blackened iron clamps, large hide lashings, and a few oversized bone or horn trophies.
- Optional axe-head, spike, or skull-shaped top cap used sparingly as a Blood Axe identifier.
- Strong vertical read for camp navigation and strong red shape language for faction recognition.

Keep detail bold. Model the pole, crossbar, primary cloth planes, large clamps, main lashings, top cap, and one to three major trophies as real geometry. Use textures or normal maps for thread fray, cloth weave, small nail heads, scratches, soot, old stains, leather pores, and fine cracks. Do not fill the banner with dense chains, excessive skull clusters, graphic gore, unreadable runes, or tiny modeled cloth strips.

## Scale Notes

Giant scale lock: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

Author all future source in centimeters. 1 Unreal unit = 1 cm. The banner should feel built and placed by Giants, not resized from a normal humanoid prop.

Recommended static world scale:

- Total height: 620-760 cm from ground to top cap.
- Main pole diameter: 18-32 cm, irregular and rough-hewn.
- Crossbar width: 260-420 cm.
- Cloth drop: 280-440 cm from crossbar to lowest torn point.
- Cloth width: 220-360 cm, depending on variant.
- Base footprint: 90-160 cm wide if using a ground spike, stacked stones, or weighted metal collar.
- Trophy accents: 30-90 cm each, kept large enough to read and sparse enough to avoid clutter.

Suggested variants:

- `A01_StaticCampMarker`: ground-planted camp banner with pole base, crossbar, and torn cloth.
- `A01_GateMarker`: shorter wall/gate-mounted variant using the same cloth and crossbar language.
- `A01_RackMarker`: compact banner tied to an armory rack or weapon pile for set dressing.

Carried-banner scale, skeleton attachment, and locomotion clearance require a separate approval and are not part of this docs-only static package.

## Materials And Color Palette

Primary materials:

- Torn red war cloth with darker maroon shadowing, faded paint, soot, and weather staining.
- Rough dark wood or scorched timber for the pole and crossbar.
- Blackened iron, dark steel, and crude reforged clamps.
- Scorched leather, hide lashings, sinew cord, and rough rope.
- Bone, horn, teeth, or skull trophies used sparingly as large readable accents.
- Ash, soot, mud, and dried grime for lower-edge weathering.

Palette targets:

- Blood Axe red: dominant cloth signal, rough and worn rather than clean ceremonial red.
- Charcoal black and dark iron gray: pole hardware, clamps, and soot.
- Warm dirty leather brown: bindings, lashings, and hide repairs.
- Bone ivory: small accent only, never the dominant shape.
- Muted wood brown: structural pole and crossbar.

Avoid neutral/civilized Giant visual language: no blue-gray stoneworker ornament, warm hearth symbolism, restrained blue runes, monumental masonry pride, or civilized highland clan banners unless a future stolen-object variant is approved. Emissive is not part of the default banner. Any ritual glow, faction aura, or magical marker state requires a separate approval gate.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeWarBanner_A01` for the world of Aerathea. The design should emphasize a towering Giant-scale hostile camp marker silhouette, torn red war cloth, rough-hewn dark timber, blackened iron clamps, crude hide lashings, sparse oversized bone trophies, soot-dark grime, Blood Axe raider sub-faction identity, and the gameplay role of marking dangerous Giant war camps and armory spaces. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a static prop concept sheet with front, side, back, base detail, cloth tear callouts, and scale markers beside a 442 cm female Giant and a 470 cm male Giant on a clean background. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid graphic gore, avoid cloth-simulation claims, avoid faction aura effects, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model the readable production forms first:

- Rough main pole with slight bends, carved flattening, and broad chipped ends.
- Heavy crossbar lashed or clamped to the pole with large, readable bindings.
- Static torn cloth sheet or layered cloth panels with bold silhouette tears.
- Large iron straps, clamp plates, or reinforcement rings at key stress points.
- Ground spike, stone-weighted base, or hammered metal collar for placement variants.
- Sparse trophy accents: one skull, one horn cluster, or two large bone charms at most for the default A01.
- Large stitches, patch plates, and rope wraps only where they affect silhouette.

Texture or normal-map the small details:

- Cloth weave, frayed fibers, pinholes, faded paint edges, old stains, and soot gradients.
- Tiny nails, small scratches, dense wood grain, leather pores, small cracks, and minor chips.
- Small runic-looking marks should be avoided unless approved; if present, they are painted marks, not emissive magic.

The cloth should be authored as static shaped geometry for this package. Do not claim simulated cloth, runtime wind deformation, destructibility, or animation. If a later task approves cloth simulation, create a separate skeletal or cloth-ready variant and validate performance independently.

## Texture And Material Notes

Target material slot count: 2 slots for the default static mesh.

- Slot 0: `MI_GIA_BloodAxeRedCloth_A01`
- Slot 1: `MI_GIA_BloodAxeBannerHardware_A01`

Optional split for hero or close-up variants: 3 slots if separating cloth, wood/leather, and metal/bone improves reuse. Do not create one-off slots for every trophy or binding.

Texture set targets:

- Default prop: 1K-2K texture set.
- Hero camp marker: 2K texture set if placed near player routes or boss staging.
- Far camp silhouette: 512-1K texture set with simplified cloth and hardware.

Required texture maps:

- `T_GIA_BloodAxeWarBanner_A01_BC`
- `T_GIA_BloodAxeWarBanner_A01_N`
- `T_GIA_BloodAxeWarBanner_A01_ORM`

Optional only with later approval:

- `T_GIA_BloodAxeWarBanner_A01_E` for approved ritual, shamanic, or faction-state variants.

Packed ORM guidance:

- Occlusion: bake strong contact under cloth folds, lashings, clamps, and trophies.
- Roughness: high for cloth and weathered wood; varied medium-high for blackened iron.
- Metallic: metal hardware only; cloth, wood, leather, bone, soot, and mud remain non-metallic.

## Triangle Budget

Default static camp marker target:

- LOD0: 3k-7k tris.
- Material slots: 2 target, 3 maximum for hero variant.
- Texture set: 1K-2K.

Variant guidance:

- Compact rack or wall marker: 1.5k-4k tris.
- Hero gate marker with larger base/trophies: 6k-10k tris.
- Set-dressing cluster using repeated banners: keep each banner under 5k tris and instance shared meshes/materials where possible.

Spend geometry on the pole shape, crossbar, cloth outline, large tears, major clamps, and big trophies. Do not spend geometry on tiny fray fibers, many dangling strips, small rivets, dense chains, fine carving, or micro scratches.

## LOD Plan

All important banner variants require LOD0-LOD3.

- LOD0: full silhouette, shaped cloth tears, pole/crossbar bevels, major bindings, large clamps, base, and sparse trophies.
- LOD1: 60-70 percent of LOD0; simplify cloth edge cuts, reduce clamp bevels, merge small lashings, and remove minor trophy undercuts.
- LOD2: 35-45 percent of LOD0; preserve pole, crossbar, red cloth mass, main torn lower edge, and top cap while flattening secondary folds and bindings.
- LOD3: 15-25 percent of LOD0; preserve vertical banner read, red cloth block, and base footprint; remove most small hardware and trophy detail.

Reduction order:

1. Tiny edge nicks, nails, stitches, and fray cuts.
2. Small leather ties and secondary cords.
3. Minor cloth holes and interior tears.
4. Trophy undercuts and back-facing detail.
5. Clamp bevels and pole chip complexity.
6. Base detail not visible from normal camera distance.

Never reduce the tall pole, broad red cloth read, torn lower silhouette, or camp-marker height before removing small surface detail.

## Collision Notes

Default collision should be simple and cheap:

- Static world prop: one capsule or box for the main pole plus one simple box for the base if needed.
- Cloth collision: none by default; cloth is visual geometry and should not block movement.
- Trophy collision: none unless a large trophy protrudes into player traversal; fold into the main simple hull if needed.
- Gate/wall variant: simple box or convex hull matching the mounting bracket, not the cloth.
- Large base variant: simple blocking box or low-count convex hull only if placed where players can walk into it.

Do not add per-strip cloth collision, per-trophy collision, physics bodies, destructible pieces, nav-relevant cloth collision, or combat hit shapes in this package. If the banner becomes an encounter objective, collision and interaction channels must be defined in a separate gameplay task.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh with fixed cloth silhouette.
- Optional material-only painted wear variation in future material instances.
- No runtime motion claim.

Approval-gated future work:

- Cloth simulation.
- Wind animation or vertex shader sway.
- Destructible banner states.
- Carried-banner attachment and character animation support.
- Capture, rally, buff, debuff, faction aura, VFX, audio, or objective behavior.

Any future moving version should be split into a separately named variant so the static camp marker remains lightweight and predictable for set dressing.

## Unreal Import Notes

Planned future import target only:

- Folder: `/Game/Aerathea/Props/Giants/BloodAxeArmory/`
- Mesh: `SM_GIA_BloodAxeWarBanner_A01`
- Default material instances: `MI_GIA_BloodAxeRedCloth_A01`, `MI_GIA_BloodAxeBannerHardware_A01`
- Optional hero material: `MI_GIA_BloodAxeWarBannerHero_A01`
- Pivot: ground-contact center at pole/base, with +Z up.
- Orientation: face the primary cloth read toward +X unless a future project import convention specifies otherwise.
- Scale: centimeter-authored source, import at scale 1.0 after future DCC/export approval.
- Collision: simple custom collision or generated primitive collision as described above.
- LODs: import LOD0-LOD3 if/when mesh work is approved.
- Sockets: none for default static prop.

Potential future sockets if separately approved:

- `banner_top_vfx`
- `banner_base_vfx`
- `banner_carry_grip`
- `banner_cloth_anchor_l`
- `banner_cloth_anchor_r`

These sockets are planning notes only. Do not author sockets, Blueprint behavior, VFX hooks, gameplay aura logic, cloth setup, or startup-scene placement from this package.

## Folder And Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeWarBanner_A01/PRODUCTION_PACKAGE.md`

Planned future source/export paths, pending approval:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/SM_GIA_BloodAxeWarBanner_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/SM_GIA_BloodAxeWarBanner_A01.fbx`
- Unreal: `/Game/Aerathea/Props/Giants/BloodAxeArmory/`

Naming:

- Static mesh: `SM_GIA_BloodAxeWarBanner_A01`
- Compact variant: `SM_GIA_BloodAxeWarBanner_Rack_A01`
- Gate marker variant: `SM_GIA_BloodAxeWarBanner_Gate_A01`
- Material instance cloth: `MI_GIA_BloodAxeRedCloth_A01`
- Material instance hardware: `MI_GIA_BloodAxeBannerHardware_A01`
- Textures: `T_GIA_BloodAxeWarBanner_A01_BC`, `T_GIA_BloodAxeWarBanner_A01_N`, `T_GIA_BloodAxeWarBanner_A01_ORM`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, tools, startup-scene actors, copied source concepts, or global index entries from this task.

## Approval Gates

- Stop before any DCC source, FBX export, Unreal Content asset, runtime source, Blueprint, tool, startup-scene, or validator implementation work.
- Stop before copying, moving, editing, embedding, or committing the external `BloodAxeArmory.png` source concept.
- Stop if the banner starts reading as neutral/civilized Giant culture instead of a hostile Blood Axe sub-faction marker.
- Stop before cloth simulation, vertex wind, destructible cloth, physics bodies, or animated cloth states.
- Stop before faction aura gameplay, rally buffs, debuffs, capture/objective logic, VFX pulses, audio cues, or interactable behavior.
- Stop before adding graphic gore, excessive skull clutter, dense chains, unreadable micro-detail, or a one-note red-only palette.
- Stop if future scale tests conflict with the Giant scale lock or imply normal humanoid compatibility as a requirement.
- Stop before final visual approval claims; this package defines production direction, not approved final art.

## Quality Gate Checklist

- Banner is a hostile Blood Axe camp marker, not a default Giant banner.
- Blood Axe identity remains separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Primary silhouette reads at MMO distance: tall pole, torn red cloth, brutal crossbar, rough base, and sparse trophy accents.
- Materials use red war cloth, blackened iron, dark wood, scorched leather, hide lashings, bone accents, ash, soot, mud, and grime consistently.
- Emissive, ritual glow, faction aura behavior, and gameplay effects are absent by default and approval-gated.
- Cloth simulation, wind animation, physics, destructibility, carried-banner support, and interaction logic are clearly out of scope.
- Triangle budgets, texture maps, material slot targets, LODs, collision, animation notes, and planned Unreal import notes are included.
- Tiny fray, nails, scratches, soot, weave, stains, and small cracks are assigned to textures or normals instead of geometry.
- Package makes no claim of DCC, FBX, Unreal Content, runtime source, source asset copying, global index editing, startup placement, cloth simulation, or final visual approval.
