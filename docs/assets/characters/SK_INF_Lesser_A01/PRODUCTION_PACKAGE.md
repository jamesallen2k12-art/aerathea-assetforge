# SK_INF_Lesser_A01 Production Package

## Art Direction Summary

`SK_INF_Lesser_A01` defines the lifecycle/body-stage sheet for Lesser Infernals, the demon/mortal hybrid children of the Infernal bloodline. They are fully autonomous at birth, violently aggressive from a very young age, and shaped by the approved culling temper. Their development is not ordinary childhood: they grow through predation, feeding on the slain, healing, adapting, and surviving early trials that Infernal culture treats as necessary weakness-culling.

The approved lifecycle stages are Spawn, 1st Kill, Blooded, Elder, and Ancient. The sheet must show how horns, wings, tails, claws, posture, eye glow, skin tone, scars, and restraint change across the stages without turning the race into random Abyss creatures. Lesser Infernals are still mortal-descended, socially legible, and tied to Balgoroth's cult laws.

## Gameplay Purpose

This package supports juvenile Infernal NPCs, lifecycle lore art, stealth/ambush encounters, cult den encounters, bloodline growth events, and future adult Infernal body planning. It establishes the stage names and body language needed before creating `SK_INF_Base_A01` final body variants or Infernal class packages.

Gameplay hooks:

- Spawn: dangerous autonomous newborn or hidden cult-cell threat.
- 1st Kill: first proven predator, fast and unstable.
- Blooded: young trained Infernal, suitable for low-to-mid encounter roles.
- Elder: mature full-power Infernal body target and social authority.
- Ancient: 900+ year survivor with visible age, ritual authority, and controlled brutality.

## Silhouette Notes

- Spawn: small but not helpless; horn buds, small black claws, tail nub or short tail, folded wing ridges.
- 1st Kill: leaner, longer claws, sharper posture, tail lengthening, wing membrane emerging.
- Blooded: adolescent/young combat silhouette with obvious horns, working tail, partial wings, aggressive crouch or stalking posture.
- Elder: full Infernal read, large wings, thick tail, developed horns, controlled predatory stance.
- Ancient: similar base silhouette to Elder but with sharper restraint, heavier horn mass, weathered skin planes, scarred wings, and ritual markings.

## Scale Notes

First-pass review heights for `SK_INF_Lesser_A01`:

| Stage | First-pass review height | Notes |
| --- | ---: | --- |
| Spawn | 80 cm | Autonomous but compact, below gnome scale. |
| 1st Kill | 115 cm | Near small gnome scale, fast predatory read. |
| Blooded | 150 cm | Near dwarf/short humanoid scale; roughly first-birthday-to-youth visual target. |
| Elder | 220 cm | Mature Infernal review target, within adult 5'0"-9'0" range. |
| Ancient | 250 cm | Older powerful body, still below 9'0" adult maximum. |

These are blockout review heights, not final canon splits. The adult race anchor remains 5'0"-9'0" / 152-274 cm until a sex/body-type split is approved.

## Materials And Color Palette

- Skin: ember red, ash red, crimson, dark umber, or muted infernal red.
- Claws/horns: black keratin, dark horn tips, subtle worn edges.
- Wings: dark leathery membrane with red-brown undertone.
- Eyes/marks: restrained abyssal red-orange or violet eye glow.
- Ritual elements: charcoal leather, blood-dark wraps, bone/obsidian beads, ash markings, Balgoroth brand marks.

## Concept Image Prompt

Create an original stylized fantasy MMORPG lifecycle concept sheet of Lesser Infernals for the world of Aerathea. The design should emphasize the approved stages Spawn, 1st Kill, Blooded, Elder, and Ancient; demon/mortal hybrid birth; fully autonomous newborn behavior; violent culling temper; rapid first-year growth by feeding on the slain; reddish skin; black claws; horn, wing, tail, eye, posture, and skin development; cult upbringing; and production-friendly MMO silhouettes. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive eye and brand accents, and MMO-safe production design. Present it as a clean lifecycle/body-stage sheet with scale callouts, material swatches, folded and open wing notes, tail callouts, claw detail, and a 180 cm humanoid comparison. Avoid copied franchise designs, gore, excessive particles, readable text, watermarks, and weapon-focused designs.

## Modeling Notes

- Build first review as five stage meshes in a shared file for scale and silhouette approval.
- Model real geometry for horns, claws, wing masses, tails, hands, feet, and major body forms.
- Keep fine skin texture, scars, membrane grain, tiny brands, and minor scratches as texture/normal detail.
- Do not over-detail juvenile bodies; readability and stage progression matter more than surface noise.
- Keep posture clearly more aggressive in Spawn, 1st Kill, and Blooded stages.
- Elder and Ancient should read more controlled and dangerous than simply larger.

## Texture And Material Notes

- First review uses blockout materials only.
- Final package target:
  - `T_INF_Lesser_A01_BC`
  - `T_INF_Lesser_A01_N`
  - `T_INF_Lesser_A01_ORM`
  - `T_INF_Lesser_A01_E` for eyes, brands, and restrained magic only.
- Material slots: skin, horn/claw, wing membrane, ritual wraps/brands, emissive.
- Use 2K shared texture set for lifecycle sheet; 4K only for hero Ancient or cinematic use.

## Triangle Budget

- Spawn/1st Kill LOD0: 12k-20k tris per stage.
- Blooded LOD0: 18k-28k tris.
- Elder/Ancient LOD0: 25k-40k tris.
- Lifecycle concept-review blockout may be lower; final sculpt targets should stay within normal humanoid to large creature budgets depending stage.

## LOD Plan

- LOD0: full stage silhouette, horns, claws, wings, tail, face, hands, posture.
- LOD1: 55-60 percent; reduce small claw bevels, minor membrane folds, small brands.
- LOD2: 25-35 percent; simplify fingers, tail taper detail, wing membrane edge cuts.
- LOD3: 10-15 percent; preserve height, horns, wings, tail, red/black color read, and posture.

## Collision Notes

- Spawn/1st Kill: small character capsule and simplified physics bodies.
- Blooded: standard small humanoid capsule.
- Elder/Ancient: adult humanoid capsule, wing collision disabled or simplified unless gameplay requires wing blocking.
- Tails and wings should use simplified auxiliary physics bodies only for hit reaction, cloth/physics review, or gameplay collision.

## Animation Notes

- Spawn: skitter, pounce, bite/claw, recoil, sudden hide.
- 1st Kill: lunge, ambush, feeding crouch, rage idle.
- Blooded: stalk, leap, claw combo, short wing burst, tail balance.
- Elder: controlled idle, wing flare, claw strike, tail sweep, cast/see-invisible gesture.
- Ancient: restrained idle, slow predatory turn, authority gesture, wing mantle, ritual mark activation.

## Unreal Import Notes

- Asset type: Skeletal Mesh review set.
- Primary asset name: `SK_INF_Lesser_A01`.
- First review assets:
  - `SK_INF_Lesser_Spawn_A01`
  - `SK_INF_Lesser_1stKill_A01`
  - `SK_INF_Lesser_Blooded_A01`
  - `SK_INF_Lesser_Elder_A01`
  - `SK_INF_Lesser_Ancient_A01`
- Folder path: `/Game/Aerathea/Characters/Infernals/Lesser/`.
- Scale: Unreal centimeters, no import scaling after DCC export.
- Pivot: between feet at ground center.
- Sockets: `vfx_eye_l`, `vfx_eye_r`, `vfx_brand_chest`, `tail_tip`, `wing_l_tip`, `wing_r_tip`, `claw_l`, `claw_r`.

## Folder And Naming Recommendation

- Package folder: `docs/assets/characters/SK_INF_Lesser_A01/`.
- Blender source: `SourceAssets/Blender/Characters/Infernals/SK_INF_Lesser_A01/SK_INF_Lesser_A01.blend`.
- FBX exports: `SourceAssets/Exports/Characters/Infernals/SK_INF_Lesser_A01/`.
- Unreal folder: `/Game/Aerathea/Characters/Infernals/Lesser/`.

## Quality Gate Checklist

- Uses approved stage names: Spawn, 1st Kill, Blooded, Elder, Ancient.
- Shows culling temper through posture and behavior, not gore.
- Reads as Infernal bloodline, not true Abyss demon.
- Horns, wings, tail, and black claws are visible by appropriate stages.
- Growth and aging rules match lore.
- Materials match Infernal red/black/ash/abyssal-glow language.
- LOD, collision, sockets, texture maps, and Unreal paths are defined.
