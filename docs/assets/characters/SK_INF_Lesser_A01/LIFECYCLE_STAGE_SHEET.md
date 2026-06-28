# SK_INF_Lesser_A01 Lifecycle Stage Sheet

## Art Direction Summary

`SK_INF_Lesser_A01` defines the production lifecycle sheet for Lesser Infernals: the demon/mortal hybrid children of the Infernal bloodline. They are born fully autonomous, violently aggressive, and shaped by early survival trials. Their first year is unnaturally fast, with growth fed by the slain; after the first birthday they slow to one visible year for every decade until extreme old age.

The approved stage names are `Spawn`, `1st Kill`, `Blooded`, `Elder`, and `Ancient`. These are social and production stages, not ordinary human ages.

## Gameplay Purpose

The lifecycle sheet supports cult den encounters, early Infernal threats, bloodline trials, named Ancient NPCs, tutorial/lore art, and future spawn-to-adult animation planning. Each stage should be readable in gameplay without relying on gore.

## Source Concept Routing

The 2026-06-27 source addendum supplies dedicated Lesser Infernal and child references beyond the first-pass scale proxies. These images route into the lifecycle matrix, not into a separate ordinary child race package.

All source concepts in this routing pass through `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md` before they become production requirements. Use the images for stage language, posture, wing/tail/claw development, and encounter mood, then reduce noisy micro-detail, excessive VFX, crop-heavy framing, and mortal-weapon emphasis.

| Source group | Routed use |
| --- | --- |
| `Infernal Children.png`, `InfernalClutch.png` | Spawn/1st Kill group staging, clutch behavior, den population, and trial-space scale references |
| `InfernalBoy*.png`, `INfernalBoy*.png` | Male-presenting Spawn, 1st Kill, and Blooded posture, horn, claw, wing-bud, and tail development references |
| `InfernalGirl*.png`, `InfernalGirls5.png` | Female-presenting Spawn, 1st Kill, Blooded, and Elder-bridge silhouette references |
| `LesserInfernal*.png`, `Lesser Infernal15.png` | General Lesser stage variants across Blooded, Elder, and Ancient body language |
| `LesserInfernalFemale.png`, `LesserInfernalMale.png` | Sex-variant checks inside the approved lifecycle stages without changing the locked stage names |

## Stage Progression

| Stage | Production height band | Lore/read | Silhouette priority |
| --- | ---: | --- | --- |
| Spawn | 70-90 cm | newly born autonomous predator | compact body, horn buds, small black claws, short tail, folded wing ridges |
| 1st Kill | 105-125 cm | first proven predator | sharper posture, stronger claws, longer tail, first membrane growth, first hunt scars |
| Blooded | 140-160 cm | young trained survivor | obvious horns, partial wings, active culling temper, quick ambush body language |
| Elder | 198-244 cm | mature full-power Infernal | full horns, full wings, thick tail, controlled predatory stance |
| Ancient | 230-274 cm | 900+ year survivor showing age again | heavy horns, scarred wings, weathered planes, ritual authority, restrained brutality |

First-pass review heights remain valid for current DCC proxies: 80 cm, 115 cm, 150 cm, 220 cm, and 250 cm.

## Silhouette Notes

- Spawn must not look helpless. It is small, alert, and dangerous.
- 1st Kill should show the first clear transition from offspring to hunter.
- Blooded should be the most visibly aggressive young stage.
- Elder should read as the mature adult body bridge into `SK_INF_Base_A01`.
- Ancient should look older through planes, scars, horn mass, wing damage, and restraint, not through frailty.
- Horn, wing, tail, claw, and eye development must be visible across the lineup.
- Stage posture is part of the read: young stages are tense and forward; older stages are controlled and certain.

## Materials And Color Palette

| Stage | Skin | Horn/claw | Wings/tail | Glow and markings |
| --- | --- | --- | --- | --- |
| Spawn | warm ember red, softer dark joints | glossy black claw tips, tiny horn buds | short tail, dark folded ridges | tiny eye glow, faint chest mark |
| 1st Kill | red with fresh darker scar islands | sharper black claws, horn nubs | lengthened tail, first membrane | first brand pulse, small eye flare |
| Blooded | deeper crimson and ash red | clear horn hooks, worn claws | partial functional wings | stronger brand, focused rage glow |
| Elder | rich ember/umber variation | mature horn mass, black claws | full folded wings, thick tail | controlled eye/brand glow |
| Ancient | ash red, dark umber, pale healed scars | heavy worn horns, cracked black keratin | scarred membrane, heavy tail | ritual marks, violet/ember restraint |

## Concept Image Prompt

Create an original stylized fantasy MMORPG lifecycle production sheet of Lesser Infernals for the world of Aerathea. The design should emphasize the approved stages Spawn, 1st Kill, Blooded, Elder, and Ancient; demon/mortal hybrid birth; fully autonomous newborn behavior; aggressive culling temper; rapid first-year growth by feeding on the slain; slowed aging after the first year; Ancient 900+ year age signs; reddish skin; black claws; visible horn, wing, tail, eye, posture, scar, and brand progression; cult upbringing; skull/bone villain language where age-appropriate; and production-friendly MMO silhouettes. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, focused emissive eye and brand accents, and MMO-safe production design. Present it as a clean lifecycle/body-stage sheet with front/side/back stage views, scale callouts, material swatches, folded and open wing notes, tail callouts, claw detail, and a 180 cm humanoid comparison. Clean the design for production readability: full body visible, feet and wings uncropped, readable midtone lighting, clear separation between red skin, black armor, dark wings, and background. If the source is too dark, start from a roughly 30 percent brighter pass. Preserve horns, leathery wings, thick tail, black claws, glowing eyes, skulls, bones, flame, lightning-like abyssal energy, anger, and Balgoroth brand identity where appropriate for the stage. Use A03-style cleanup by default: reduce tiny repeated rivets, random speckle artifacts, malformed micro-spikes, broken micro-chains, torn-strip noise, dense spell clutter that hides anatomy, crop-heavy action framing, and photoreal surface garbage. Avoid copied franchise designs, gore, excessive particles, readable text, watermarks, and weapon-focused designs.

## Modeling Notes

- Build all stages from a shared design language so they read as one bloodline.
- Model real geometry for horns, claws, wings, tails, major body forms, and large ritual marks.
- Keep fine scars, skin pore stylization, membrane veins, and minor brands in texture/normal maps.
- Spawn and 1st Kill need strong face/eye read despite small scale.
- Blooded needs the clearest young-combat pose language.
- Elder and Ancient should reuse adult rig logic where practical, but avoid forcing one skeleton if scale and wing/tail proportions make deformation poor.

## Texture And Material Notes

Final lifecycle texture set:

- `T_INF_Lesser_A01_BC`
- `T_INF_Lesser_A01_N`
- `T_INF_Lesser_A01_ORM`
- `T_INF_Lesser_A01_E`

Use a shared base material family with per-stage material instances:

- `MI_INF_Lesser_Spawn_A01`
- `MI_INF_Lesser_1stKill_A01`
- `MI_INF_Lesser_Blooded_A01`
- `MI_INF_Lesser_Elder_A01`
- `MI_INF_Lesser_Ancient_A01`

Default texture target is 2K for the shared lifecycle sheet. Ancient hero variants may justify 4K if used for close cinematic or boss presentation.

## Triangle Budget

- Spawn LOD0: 12k-16k tris.
- 1st Kill LOD0: 14k-20k tris.
- Blooded LOD0: 18k-28k tris.
- Elder LOD0: 25k-40k tris.
- Ancient LOD0: 30k-45k tris.
- Ancient named boss can reach 50k tris only if wing damage, horn mass, and ritual silhouette require it.

## LOD Plan

- LOD0: full stage silhouette, face, horns, claws, wings, tail, major marks.
- LOD1: 55-60 percent; reduce minor scars, claw bevels, small wing membrane folds, small ornaments.
- LOD2: 25-35 percent; simplify fingers, tail taper, membrane edge, horn bevels.
- LOD3: 10-15 percent; preserve height, posture, horns, wings, tail, red/black color read, and glow block.

## Collision Notes

- Spawn and 1st Kill use compact movement capsules and minimal auxiliary physics.
- Blooded uses small humanoid capsule, tail simplified to 1-2 optional bodies.
- Elder and Ancient use adult capsule logic with simplified wing and tail bodies.
- Wings remain non-blocking by default. Tail collision is enabled only for attacks, hit reaction, or staged encounters.

## Animation Notes

- Spawn: skitter, alert idle, sudden pounce, small claw rake, bite, recoil, hide.
- 1st Kill: lunge, ambush, feeding crouch without gore emphasis, rage idle, short climb.
- Blooded: stalk, leap, two-hit claw combo, tail balance, short wing burst.
- Elder: controlled idle, wing flare, claw strike, tail sweep, see-invisible focus, brand pulse.
- Ancient: slow predatory turn, ritual authority gesture, wing mantle, regeneration flare, rejection/worthiness judgment pose.

## Unreal Import Notes

- Asset type: Skeletal Mesh lifecycle set.
- Folder path: `/Game/Aerathea/Characters/Infernals/Lesser/`.
- Scale: centimeters, no import scaling.
- Pivot: ground center between feet.
- Required sockets: `vfx_eye_l`, `vfx_eye_r`, `vfx_brand_chest`, `vfx_mouth`, `vfx_regen_core`, `claw_l`, `claw_r`, `tail_tip`, `wing_l_tip`, `wing_r_tip`.
- Suggested ABP path: `/Game/Aerathea/Characters/Infernals/Lesser/ABP_INF_Lesser_Base_A01` with stage overrides.

## Folder And Naming Recommendation

- Lifecycle sheet: `docs/assets/characters/SK_INF_Lesser_A01/LIFECYCLE_STAGE_SHEET.md`
- Blender source: `SourceAssets/Blender/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_A01.blend`
- FBX exports: `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/`
- Unreal folder: `/Game/Aerathea/Characters/Infernals/Lesser/`

## Quality Gate Checklist

- Uses approved stage names exactly: Spawn, 1st Kill, Blooded, Elder, Ancient.
- Growth and aging rules match the Infernal lore.
- Each stage is readable by height, posture, horns, wings, tail, claws, and marks.
- Young stages are aggressive without gore.
- Ancient shows age and authority without becoming weak.
- LOD, collision, sockets, materials, textures, and Unreal paths are defined.
