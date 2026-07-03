# SK_GIA_Base_A01 Production Package

## Art Direction Summary

- Asset name: `SK_GIA_Base_A01`
- Asset type: Skeletal Mesh base race body / character production package
- Source concepts: `Giant.png`, `Giant1.png`, `Giant2.png`, `GiantMale1.png`, `GiantMale2.png`, `GiantMale3.png`, `GiantMale4.png`, `GiantFemale.png`, `GiantFemale1.png`, `GiantFemale3.png`, `GiantFemale4.png`, `GiantFemale5.png`, `GiantFemaleShaman.png`, `GiantMaleandFemale.png`, `GiantMaleandFemale3.png`
- Faction/theme: Giant
- Approval image: `docs/assets/characters/SK_GIA_Base_A01/SK_GIA_Base_A01_ApprovalConcept.png`
- Status: Concept direction approved; 2026-06-28 rebuild/rescale completed to A04 baselines: female 442 cm and male 470 cm; current staged import is validated for first-pass scale, sockets, physics, LODs, and startup placement, but remains review-only for final sculpt/retopo/UV/texture quality

Build status:

- DCC builder: `Tools/DCC/build_giant_base.py`
- Unreal importer: `Tools/Unreal/import_giant_base.py`
- Blender source: `SourceAssets/Blender/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_A01.blend`
- Male FBX export: `SourceAssets/Exports/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_Male_A01.fbx`
- Female FBX export: `SourceAssets/Exports/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_Female_A01.fbx`
- DCC review render: `Saved/Automation/GiantBaseReview/SK_GIA_Base_A01_DCCReview.png`
- Unreal close-up capture: `Saved/Automation/StartupReview/AeratheaStartupReview_GiantBase_Closeup_v2.png`
- Unreal import: regenerated male/female FBX exports imported, placed in startup scene, sockets generated, physics assets assigned, animation Blueprint placeholders created, focused scale validation passing via `Tools/Unreal/validate_giant_base_scale.py`, and startup validation passing via `Tools/Unreal/validate_startup_scene.py`
- Scale validation result: male review mesh visible bounds height 464.26 cm for the approved 470 cm baseline; female review mesh visible bounds height 429.35 cm for the approved 442 cm baseline
- Rebuild/rescale plan: `docs/assets/characters/SK_GIA_Base_A01/REBUILD_RESCALE_PLAN.md`

Approved Giant base direction for Aerathea. Giants are remote mountain people, not oversized humans: massive, weathered, broad-framed, highland-adapted, and strongly tied to stonecraft, isolated cave towns, and nomadic mountain life. The neutral base package must preserve civilized Giant identity and not let Blood Axe brutality become the default Giant culture. The approval concept is the visual target for the first DCC scale/body pass; the current DCC output is a review blockout for scale, proportion, skeleton, and sockets only.

## Gameplay Purpose

Establishes the body scale, silhouette language, rig assumptions, clothing fit, hand scale, collision envelope, animation range, and Unreal import rules for all future Giant work. Blood Axe warbands, Giant armory assets, cave-town interiors, door heights, stairs, beds, tables, settlement props, and named Giant NPCs all depend on this base package.

## Silhouette Notes

Readable MMO-distance silhouette: towering height, broad shoulders, long powerful arms, heavy hands, thick neck, sturdy legs, large feet, weathered face planes, heavy brow, highland hair/braids, fur or hide starter clothing, and stoneworker posture. Giants should feel ancient, physical, and practical rather than cartoonish. Avoid simply scaling a normal human skeleton.

Neutral/civilized variants should emphasize stoneworker mass, carved ornament, blue-gray tattoo or paint motifs, rough leather, fur, and monumental tool/weapon scale. Blood Axe-specific red banners, skull trophies, gore, and brutal raider markings are excluded from the base body and handled in later sub-faction packages.

## Scale Notes

Approved scale:

- Female Giants: 14-15 ft tall, approximately 427-457 cm.
- Male Giants: 14'10"-16'0" tall, approximately 452-488 cm.
- Recommended first production baselines: female 442 cm / 14'6", male 470 cm / 15'5".
- Author in centimeters. 1 Unreal unit = 1 cm.
- Feet at world origin, facing +X unless import tests establish another project convention.

Scale dependencies:

- Giant doors should start around 600-700 cm clear height for primary entries.
- Giant stair risers must be split from small-folk traversal routes. Add side paths, ramps, or separate steps for normal player navigation.
- Giant hand sockets must drive Blood Axe armory scale before any weapon DCC work starts.
- Interior camera and collision review must include both Giant and normal humanoid traversal.

## Materials And Color Palette

Base palette: weathered skin tones, cool mountain-gray body paint, blue-gray tattoo marks, rough leather, dark iron, fur, hide, braided cord, bone/stone beads used sparingly, carved slate, and muted warm hearth accents.

Civilized Giant stoneworker accent palette: blue-gray stone, aged iron, worn brass, pale carved stone, warm lantern/hearth light, and restrained blue rune or storm glow only for shamanic/mystic variants.

Blood Axe materials are not part of the base: red banners, blood paint, excessive trophy elements, and heavy skull language belong in Blood Axe packages.

## Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_GIA_Base_A01` for the world of Aerathea. The design should emphasize a 14-15 ft female and 14'10"-16'0" male Giant scale range, towering mountain-forged silhouettes, broad shoulders, powerful hands, sturdy legs, highland weathering, rough leather and fur starter clothing, blue-gray stoneworker body paint, carved stone and dark iron accents, remote Giant cave-town culture, and a neutral/civilized identity separate from the Blood Axe Tribe. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing rune or storm-glow accents only where justified, and MMO-friendly production design. Present it as a character production sheet with male/female front, side, back, three-quarter views, scale comparison beside a 180 cm human and current A04 gnome/minotaur markers, hand/foot callouts, clothing material callouts, and socket landmarks on a clean background. Avoid copying any existing franchise, avoid gore, avoid readable text, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model the primary body forms as real geometry: head, brow, nose, jaw, torso, shoulders, arms, hands, fingers, legs, feet, starter clothing masses, belts, large braids/hair clumps, fur mantle blocks, and major stone/iron ornaments. Do not model every hair strand, stitch, crack, bead, tattoo edge, or tiny carving.

The base body should be neutral and modular:

- Keep Blood Axe armor, trophy belts, red war banners, and raider paint separate.
- Keep starter clothing as removable or replaceable modules where practical.
- Use clean edge flow for extreme height, heavy shoulders, elbows, knees, wrists, fingers, ankles, neck, jaw, and facial expression range.
- Build male and female proportion variants from shared skeleton assumptions if possible, but allow separate body meshes if scale/proportion differences require it.
- Preserve hand scale for future giant weapons, bows, masonry tools, shields, and ritual props.

## Texture And Material Notes

Texture deliverables:

- `T_GIA_Base_A01_Body_BC`
- `T_GIA_Base_A01_Body_N`
- `T_GIA_Base_A01_Body_ORM`
- `T_GIA_Base_A01_Eyes_BC`
- `T_GIA_StarterOutfit_A01_BC`
- `T_GIA_StarterOutfit_A01_N`
- `T_GIA_StarterOutfit_A01_ORM`
- `T_GIA_Base_A01_Rune_E` only for shamanic or mystic variants

Material slot target:

- Body/head/skin
- Eyes
- Hair/fur
- Starter outfit/leather/iron/stone ornaments

Use 2K texture sets for normal NPC use. Use 4K only for named hero or boss-scale Giant variants. Paint tattoos and weathering in BC/ORM/normal detail, not dense geometry. Use emissive only for restrained rune, storm, or shamanic accents.

## Triangle Budget

- LOD0 base body target: 35k-55k tris per adult Giant body.
- Starter clothing, hair, fur, belts, and simple ornaments: 8k-18k tris depending on variant complexity.
- First production review target: under 70k tris total for one fully dressed Giant.
- Named hero or boss variant: 70k-90k tris only when justified and with aggressive LODs.

## LOD Plan

- LOD0: full body, face planes, hands, feet, hair/fur clumps, starter clothing, major belts and ornaments.
- LOD1: 60-70 percent of LOD0; reduce small straps, hair subdivisions, fur clump cuts, and minor belt details.
- LOD2: 35-45 percent of LOD0; simplify fingers, inner clothing folds, ornament bevels, and hair/fur silhouettes while preserving the large read.
- LOD3: 15-25 percent of LOD0; preserve head, shoulders, hands, weapon sockets, posture, and overall height.

Never reduce the towering shoulder line, large hands, heavy stance, or primary head silhouette before removing small trims and secondary clothing cuts.

## Collision Notes

Use a Giant-tuned movement capsule per variant:

- Female baseline capsule: roughly 442 cm height, 95-115 cm radius.
- Male baseline capsule: roughly 470 cm height, 100-125 cm radius.
- Maximum male variants may need up to 490 cm capsule height and nav-agent review.

Physics asset should include pelvis, spine, chest, head, upper/lower arms, hands, major fingers as simplified groups, thighs, calves, feet, and optional hair/fur secondary bodies only if animation needs them. Equipped giant weapons and armor should usually rely on character collision unless a specific boss mechanic requires separate hit shapes.

## Animation Notes

Baseline animation list:

- Idle neutral
- Idle heavy breathing
- Walk
- Run/jog
- Turn in place
- Step up/down
- Jump or heavy vault, if playable movement requires it
- Interact / reach down to small-folk scale
- One-handed heavy attack
- Two-handed heavy attack
- Shield brace
- Bow draw placeholder for future Giant bows
- Mason/tool work loop
- Shaman cast/channel placeholder
- Stomp or ground impact
- Hit reactions
- Stagger
- Death / collapse

Animation style should sell mass: slower acceleration, clear weight shift, footfall timing, broad arcs, and readable telegraphs for combat. Do not use normal human timing at giant scale.

## Unreal Import Notes

- Folder: `/Game/Aerathea/Characters/Giants/Base/`
- Current staged skeletal meshes: `SK_GIA_Base_Male_A01`, `SK_GIA_Base_Female_A01`
- Current staged skeletons: `SK_GIA_Base_Male_A01_Skeleton`, `SK_GIA_Base_Female_A01_Skeleton`
- Current staged physics assets: `PHYS_GIA_Base_Male_A01`, `PHYS_GIA_Base_Female_A01`
- Current staged animation Blueprint placeholders: `ABP_GIA_Base_Male_A01`, `ABP_GIA_Base_Female_A01`
- Startup review actors: `AET_PROD_GiantMaleBase_A01`, `AET_PROD_GiantFemaleBase_A01`
- Pivot: feet at world origin
- Scale: DCC authored to centimeter baselines; import script applies the project FBX uniform scale and keeps startup actors at scale 1,1,1
- Material slots: body/head, eyes, hair/fur, starter outfit/gear
- Sockets:
  - `hand_r_weapon`
  - `hand_l_offhand`
  - `hand_r_twohand_grip`
  - `hand_l_twohand_grip`
  - `back_large_weapon`
  - `back_shield`
  - `belt_tool_l`
  - `belt_tool_r`
  - `head_hair_ornament`
  - `chest_talisman`
  - `vfx_rune_hand_l`
  - `vfx_rune_hand_r`
  - `vfx_stomp_ground`

Validate beside a 180 cm humanoid reference, the 110 cm gnome reference, a 270 cm minotaur reference, and future Giant door/stair blockouts.

## Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_GIA_Base_A01/`
- Modeling handoff: `docs/assets/characters/SK_GIA_Base_A01/MODELING_HANDOFF.md`
- Approval concept: `docs/assets/characters/SK_GIA_Base_A01/SK_GIA_Base_A01_ApprovalConcept.png`
- Source: `SourceAssets/Blender/Characters/Giants/SK_GIA_Base_A01/`
- Exports: `SourceAssets/Exports/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_Male_A01.fbx`, `SourceAssets/Exports/Characters/Giants/SK_GIA_Base_A01/SK_GIA_Base_Female_A01.fbx`
- DCC review render: `Saved/Automation/GiantBaseReview/SK_GIA_Base_A01_DCCReview.png`
- Unreal: `/Game/Aerathea/Characters/Giants/Base/`

## Quality Gate Checklist

- Female Giant scale is 14-15 ft; male Giant scale is 14'10"-16'0".
- Approved A04 rebuild baselines are female 442 cm and male 470 cm; current first-pass DCC/Unreal import has been regenerated and validated before Blood Axe, cave-town, armory, or named Giant production.
- Giant base reads as a remote mountain race, not a scaled normal human.
- Civilized/neutral Giant identity is separate from Blood Axe Tribe visual language.
- Primary silhouette remains readable at MMO distance.
- Giant hand, foot, door, stair, weapon, and interior scale dependencies are documented.
- Materials support skin, fur, rough leather, iron, stone, and restrained shamanic/rune accents.
- Triangle budgets, texture maps, LODs, collision, sockets, animation notes, and Unreal paths are included.
- Build does not copy existing franchise Giant designs and does not use unbuildable gore or micro-detail.
