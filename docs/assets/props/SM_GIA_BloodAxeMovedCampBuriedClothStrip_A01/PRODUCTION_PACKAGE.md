## Art Direction Summary

`SM_GIA_BloodAxeMovedCampBuriedClothStrip_A01` is a docs-only production package for a weathered oxide-red cloth strip partially buried in cold ash and trampled mud. It belongs to the moved-camp cairn-line dressing set and should read as old Blood Axe residue left behind by a hostile Giant sub-faction, not as an active camp sign, fresh marker, usable clue, or functional route element.

The cloth is small, low, dirty, and nearly swallowed by ground residue. It may carry faded Blood Axe color language through dull oxide red, black soot, and mud staining, but it must not become a banner, ritual focus, breadcrumb, clickable object, pickup, objective marker, or readable navigation signal. Blood Axe raider language must remain separate from neutral/civilized Giant culture: do not use blue-gray civic masonry, refined cave-town carving, terrace or waterwork motifs, warm hearth settlement language, restrained blue runes, peaceful highland markers, or default neutral Giant material identity.

This file is documentation only. It does not authorize DCC work, sculpting, retopo, UVs, bake work, FBX export, Unreal content creation, startup placement, source concept copying or movement, Hermes file edits, validators, runtime files, final visual approval, or implementation target selection.

## Gameplay Purpose

This prop is passive environmental history. Its only purpose is to support the impression that a Blood Axe camp once occupied or crossed the area and later moved on, leaving minor cloth residue mixed into ash and mud.

It must not define a trail, route, navigation aid, waypoint, breadcrumb behavior, tracking mechanic, UI path, encounter lane, patrol guide, spawn guide, objective line, quest clue, lootable item, pickup, clickable object, interact prompt, resource node, faction buff, ritual state, or camp-route approval. It is static visual dressing only for a future authorized art pass.

## Silhouette Notes

The silhouette should be a flat, ground-hugging torn strip with uneven frayed ends and one or two partially buried edges. At normal MMO camera distance it should read as a broken, dirty red-brown streak caught in ash, not as a bright flag, arrow, ribbon trail, active signal, or player-facing marker.

Recommended shape language for a future mesh:

- Long, irregular strip with a slight twist, sag, or fold, never upright.
- One end partly covered by ash or mud so the full outline is interrupted.
- Torn triangular bites and frayed edge points kept broad enough to model cleanly.
- Optional shallow mud lip or ash crust overlapping the cloth, kept low and non-directional.
- No post, stake, banner pole, readable symbol, glowing rune, knot language, or route-point shape.

## Scale Notes

Use the validated Giant scale lock as the production reference: female Giant baseline 442 cm / 14 ft 6 in and male Giant baseline 470 cm / 15 ft 5 in. The broader approved Giant range remains females 14-15 ft and males 14 ft 10 in-16 ft 0 in. This package must not alter Giant scale.

Future size target:

- Length: 60-110 cm.
- Width: 12-24 cm.
- Raised thickness: 1-4 cm where folded or mud-caked.
- Ground height: keep most visible cloth within 0-6 cm of the terrain.

The strip should feel minor beside Giant-scale camp debris: large enough to read at close camera range, but too small and buried to imply an intentional marker for a 442 cm or 470 cm Giant.

## Materials and Color Palette

Primary materials are faded woven cloth, cold ash, wet and dried mud, soot, and small embedded grit. Keep the palette dull and aged:

- Cloth: faded oxide red, dried maroon, dirty rust, desaturated crimson-brown.
- Ash: charcoal gray, cold black, pale gray dust, soot smears.
- Mud: dark umber, wet brown, dried tan-gray edge crusts.
- Wear: sun-bleached thread, muddy abrasion, ash caking, torn fiber highlights.

Do not use fresh blood, graphic gore, bright red signal color, blue Aetherium, blue runes, active emissive accents, metallic faction plates, readable text, refined civic Giant ornament, or neutral/civilized Giant hearth language. Any Blood Axe identity should come from restrained old cloth color and hostile raider context only.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a weathered Blood Axe Giant cloth strip partially buried in ash and mud for the world of Aerathea. The design should emphasize a low ground-hugging torn silhouette, faded oxide-red woven cloth, cold ash, trampled dark mud, hostile Blood Axe Giant residue kept separate from neutral/civilized Giant culture, abandoned moved-camp mood, and passive environmental history only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a small prop concept sheet with top view, three-quarter ground view, and scale callout beside female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in Giant baselines on a clean neutral background. Avoid copying any existing franchise, avoid excessive micro-detail that would not translate to a mid-poly Unreal asset, and avoid making it look like a breadcrumb, clickable object, pickup, objective marker, route marker, banner, or active signal.

## Modeling Notes

These are future DCC handoff notes only; this task does not authorize DCC creation.

If separately approved for modeling, build the cloth as a thin, low-poly torn strip with broad silhouette cuts and shallow folded thickness. Model only the main cloth body, a few large frayed edge shapes, and one or two low ash or mud overlaps where needed for the partially buried read. Fake fine weave, thread fibers, soot speckles, ash dust, tiny mud cracks, and small fray strands with texture and normal detail.

Recommended future modeling constraints:

- Keep the underside minimal because the prop sits against terrain.
- Avoid cloth simulation, wind deformation setup, physics cloth, dangling threads, or loose animated strips.
- Use cut geometry or a conservative opacity mask for torn edges; do not rely on dense hair-like alpha fibers.
- Keep all forms non-directional so the asset cannot read as an arrow or trail marker.
- Place the future pivot at the center of the ground contact area for easy terrain dressing, if an implementation task later approves the mesh.

## Texture and Material Notes

Use a single future material slot. The material should be matte, dirty, and non-emissive, with hand-painted color variation and baked ambient occlusion around folds and buried edges.

Future texture set recommendation:

- `T_GIA_BloodAxeMovedCampBuriedClothStrip_A01_BC`: faded cloth color, ash, mud stains, optional opacity mask in alpha only if later approved.
- `T_GIA_BloodAxeMovedCampBuriedClothStrip_A01_N`: shallow cloth weave, broad wrinkles, buried-edge compression, mud crusts.
- `T_GIA_BloodAxeMovedCampBuriedClothStrip_A01_ORM`: occlusion in folds and mud overlap, high roughness, no metallic.

Do not create an emissive map. Do not add readable runes, UI-like color coding, bright objective contrast, or polished neutral/civilized Giant ornament. Tiny cloth weave, ash flecks, soot speckles, mud cracks, and thread frays belong in texture and normal detail rather than modeled geometry.

## Triangle Budget

Target this as a minor small prop if a future implementation task approves it:

- LOD0: 300-700 tris, hard cap 900 tris.
- Material slots: 1.
- Texture size: 512 px target; 1K only if the asset is later grouped into a larger shared cloth-remnant atlas.

The budget is intentionally below normal hero-prop density because the asset is flat, non-interactive, and partially buried. Spend geometry on the broad torn outline and fold readability, not on individual fibers, tiny ash clumps, or thread-level frays.

## LOD Plan

Future LODs should preserve the low red-brown cloth streak and buried silhouette while removing small edge complexity first:

- LOD0: Full torn outline, shallow folds, broad buried edges, and low mud or ash overlap.
- LOD1: Reduce frayed edge vertices and simplify folds; keep the interrupted strip shape.
- LOD2: Simplify to a flatter irregular strip with texture-driven fray and ash coverage.
- LOD3: Very low flat remnant or terrain-flush card; keep only the main broken color mass or allow distance culling if approved by a later environment pass.

Remove tiny fray cuts, small mud bumps, minor ash scallops, and secondary fold notches before changing the primary low silhouette. No LOD should become a clear arrow, path segment, marker plate, or objective ring.

## Collision Notes

No gameplay collision is required or authorized by this documentation. If the prop is ever implemented, it should default to no collision and must not create a navigation blocker, cover point, click target, pickup volume, resource volume, damage volume, aura volume, objective trigger, or interaction volume.

Do not claim collision correctness in this package. Any future collision choice must be validated in a separate authorized implementation task.

## Animation Notes

No animation is required. Do not use cloth simulation, wind animation, physics collapse, material pulsing, VFX, audio, idle movement, or interactive state changes.

The strip should remain inert and half-buried, reinforcing that the Blood Axe camp residue is old and abandoned rather than active or signaling.

## Unreal Import Notes

This package is docs-only and does not authorize Unreal import. Do not create or modify `Content/Aerathea/`, FBX files, textures, material instances, Blueprints, validators, runtime source, startup placement, capture setups, or final approval artifacts for this task.

Future import recommendation only, if a separate task later authorizes implementation:

- Asset name: `SM_GIA_BloodAxeMovedCampBuriedClothStrip_A01`.
- Asset type: Static Mesh.
- Suggested folder: `/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/ClothRemnants/`.
- Scale: 1 Unreal unit = 1 cm; preserve the 60-110 cm cloth length target.
- Pivot: center of ground contact area.
- Collision: none by default.
- Material slot count: 1.
- Material instance: `MI_GIA_BloodAxeMovedCampBuriedClothStrip_A01`.
- Textures: `T_GIA_BloodAxeMovedCampBuriedClothStrip_A01_BC`, `T_GIA_BloodAxeMovedCampBuriedClothStrip_A01_N`, `T_GIA_BloodAxeMovedCampBuriedClothStrip_A01_ORM`.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: non-interactive static dressing only; no runtime logic, VFX, audio, overlap events, navigation behavior, or marker validation.

## Folder and Naming Recommendation

Current authorized documentation path:

- `docs/assets/props/SM_GIA_BloodAxeMovedCampBuriedClothStrip_A01/PRODUCTION_PACKAGE.md`

Future naming recommendations only:

- Static mesh: `SM_GIA_BloodAxeMovedCampBuriedClothStrip_A01`.
- Material instance: `MI_GIA_BloodAxeMovedCampBuriedClothStrip_A01`.
- Base color texture: `T_GIA_BloodAxeMovedCampBuriedClothStrip_A01_BC`.
- Normal texture: `T_GIA_BloodAxeMovedCampBuriedClothStrip_A01_N`.
- Packed ORM texture: `T_GIA_BloodAxeMovedCampBuriedClothStrip_A01_ORM`.

Do not create source folders, move source concepts, create DCC files, export FBX, create Unreal folders, edit Hermes files or config, update global indexes, modify task boards, touch backlog/bootstrap files, or select this as a first implementation target under this task.

## Quality Gate Checklist

- Package uses exactly the assigned asset: `SM_GIA_BloodAxeMovedCampBuriedClothStrip_A01`.
- Package remains docs-only and does not authorize DCC, FBX, Unreal content, startup placement, source movement, Hermes edits, runtime work, validators, final visual approval, or implementation target selection.
- The asset reads as a weathered cloth strip partially buried in ash and mud.
- Blood Axe is identified only as a hostile Giant sub-faction.
- Blood Axe hostile raider residue remains separate from neutral/civilized Giant culture, civic masonry, refined cave-town carving, terrace or waterwork motifs, warm hearth settlement language, and peaceful highland markers.
- Giant scale is explicit: female Giant baseline 442 cm / 14 ft 6 in and male Giant baseline 470 cm / 15 ft 5 in.
- The strip is not a breadcrumb, clickable object, pickup, objective marker, waypoint, route guide, tracking mark, UI path, quest clue, encounter lane, spawn guide, or patrol guide.
- Materials stay on faded oxide-red cloth, cold ash, soot, mud, and embedded grit with no default emissive.
- Fine weave, ash flecks, soot speckles, mud cracks, and small frays are reserved for texture or normal detail.
- Triangle budget, LOD plan, collision limits, animation limits, future import notes, and naming recommendations are included without claiming implementation.
