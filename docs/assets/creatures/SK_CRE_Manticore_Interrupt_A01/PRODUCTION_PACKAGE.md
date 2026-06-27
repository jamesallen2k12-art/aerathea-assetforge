# SK_CRE_Manticore_Interrupt_A01 Production Package

## 1. Art Direction Summary

`SK_CRE_Manticore_Interrupt_A01` is an encounter-specific Manticore variant for the Gnome/Ogre rivalry scene. It should read as a wild third-party predator crashing into the battle, not as a Gnome machine, Ogre war beast, or faction pet. The design uses the approved Aerathea Manticore anchor: lion body, bat/draconic wings, scorpion tail, predatory ruin/desert threat language, clear tail stinger, and readable leathery wings.

Use `GnomevsOgreandManticore8.png` for encounter staging and use `Manticore.png` plus `Manticore8.png` as the main anatomy references. `Manticore5.png` can inform stalking posture and forest/overgrown surface variants, but feathered or birdlike wing language from any source should not drive this interrupt package.

## 2. Gameplay Purpose

- Interrupts a Gnome/Ogre battlefield encounter as an uncontrolled roaming elite creature.
- Forces both sides to reposition with wing buffet, leap impact, and scorpion-tail threat zones.
- Adds a temporary third objective or hazard without changing the core rivalry identity.
- Supports quest, world event, ruin ambush, and dungeon-pull variants.
- Establishes production requirements for a future base `SK_CRE_Manticore_A01` skeleton and shared animation set.

## 3. Silhouette Notes

- Large lion torso with heavy shoulders, low predatory stance, clawed paws, mane mass, and compact muscular hindquarters.
- Two large leathery bat/draconic wings with strong finger bones and torn membrane edges.
- High arcing segmented scorpion tail with a large hooked stinger visible above the body from gameplay camera distance.
- Broad mane and horn/spike accents may frame the head, but the face should remain lion-like, not demonic humanoid.
- Avoid saddles, faction armor, Gnome Aetherium hardware, Ogre Teknomancy machinery, and overly ornamental jewelry for the interrupt variant.

## 4. Scale Notes

- Shoulder height target: 230-260 cm.
- Head height target: 300-340 cm in neutral stance.
- Body length target: 520-650 cm, excluding tail arc.
- Tail arc height target: 480-600 cm for readable stinger threat.
- Wing span target: 900-1100 cm when fully extended; folded wings must not hide the tail silhouette.
- The creature should feel threatening beside 10-11 ft Ogres but remain smaller than raid-boss creatures.

## 5. Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Lion hide | tawny gold, sand brown, muted ochre | Body, legs, face |
| Mane | dark umber, charcoal brown, black tips | Head, chest, shoulder framing |
| Wing membrane | dark rust, leathery brown, smoky red underside | Bat/draconic wings |
| Chitin tail | black-brown, burnt bronze, dark horn | Segmented tail plates and stinger |
| Venom accent | muted amber-green, sickly yellow-green | Stinger groove, bite/spit telegraph only |
| Ruin dust | gray stone, ash, desaturated tan | Feet, scars, environmental dirt |

Keep emissive use minimal. Venom glow is allowed only as a restrained telegraph mask on the stinger, eyes, or a status-effect wound.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_CRE_Manticore_Interrupt_A01` for the world of Aerathea. The design should emphasize a powerful lion body, a dark mane, large leathery bat/draconic wings, a high arcing segmented scorpion tail with a clear hooked stinger, tawny hide, dark chitin tail plates, muted venom accents, ruin-stalker predator identity, and the gameplay role of a wild third-party creature interrupting a Gnome heavy Mek versus Ogre battlefield. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a creature concept sheet with front, side, folded-wing, wing-spread, tail-sting pose, scale lineup against a Gnome heavy Mek and an Ogre, material swatches, socket callouts, and attack-state silhouettes on a clean background. Avoid copying any existing franchise, avoid feathered bird wings for this variant, avoid faction armor or machinery, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

- Treat this package as a variant specification until `SK_CRE_Manticore_A01` base body, skeleton, and proportions are approved.
- Model real geometry for the lion body, mane volume, wing arm/finger bones, main membrane shape, tail segments, stinger, paws, claws, ears, and major facial planes.
- Fake fine fur, skin pores, membrane scratches, tiny scars, and small tail-plate wear in texture/normal maps.
- Keep wing membranes broad and readable from above; avoid feather clumps on this interrupt variant.
- Tail segments should deform cleanly through a curved chain and preserve the stinger silhouette in LOD2 and LOD3.
- Build animation-friendly shoulder/wing topology; do not overcut the membrane with tiny holes that will skin poorly.

## 8. Texture And Material Notes

Texture set targets:

- `T_CRE_Manticore_Interrupt_A01_BC`
- `T_CRE_Manticore_Interrupt_A01_N`
- `T_CRE_Manticore_Interrupt_A01_ORM`
- `T_CRE_Manticore_Interrupt_A01_E`

Material slots:

1. `MI_CRE_Manticore_Interrupt_A01_Body`
2. `MI_CRE_Manticore_Interrupt_A01_Wings`
3. `MI_CRE_Manticore_Interrupt_A01_TailClaws`
4. Optional `MI_CRE_Manticore_Interrupt_A01_Venom`

Use a 2K texture set for common world-event use. Use 4K only if this becomes a named elite or cinematic creature. Pack ORM maps and reserve emissive for venom telegraph states.

## 9. Triangle Budget

- LOD0 target: 35k-50k tris.
- Material slots: 3, with 4 allowed only if venom material state requires it.
- Texture set: 2K standard, 4K hero only.
- Wing membranes and tail segments should carry the silhouette budget before mane strand detail or small scars.

## 10. LOD Plan

- LOD0: full lion body, mane mass, wing fingers, membrane shape, tail segments, stinger, claws, teeth, sockets, and attack-state shape keys if needed.
- LOD1: 55-60 percent; simplify mane edge loops, reduce small tail bevels, merge minor wing-finger bevels, keep stinger and folded-wing read.
- LOD2: 25-35 percent; reduce mane clumps, simplify paws/claws, collapse small membrane tears, keep high tail arc and wing silhouette.
- LOD3: 10-15 percent; preserve lion body mass, two-wing profile, scorpion tail arc, stinger tip, and dominant color blocks.

## 11. Collision Notes

- Use skeletal mesh physics bodies for torso, head, neck, shoulders, hips, upper legs, wing roots, tail chain, and stinger.
- Use non-blocking overlap volumes for wing buffet, leap impact, venom spit, tail sweep, and stinger strike.
- Gameplay capsule should cover the body, not the full wing span.
- Tail hit tests should use sockets or simple swept traces, not per-poly collision.

## 12. Animation Notes

Required first set:

- Idle crouch.
- Prowl walk.
- Short charge.
- Leap interrupt landing.
- Wing spread threat.
- Wing buffet.
- Tail sting.
- Tail sweep.
- Bite/claw combo.
- Roar.
- Hit react front/side.
- Wounded retreat.
- Death.

Optional encounter states:

- Background arrival glide.
- Cliff perch idle.
- Venom telegraph.
- Shield-wall impact recoil.

## 13. Unreal Import Notes

- Asset type: Skeletal Mesh creature variant, with future encounter Blueprint dependency.
- Unreal folder: `/Game/Aerathea/Creatures/Manticores/`
- Primary mesh: `SK_CRE_Manticore_Interrupt_A01`
- Skeleton dependency: future `SK_CRE_Manticore_A01_Skeleton`
- Physics asset: `PHYS_CRE_Manticore_Interrupt_A01`
- Animation Blueprint: `ABP_CRE_Manticore_A01`
- Optional encounter Blueprint: `BP_GNM_OGR_ManticoreInterrupt_A01`
- Pivot: ground center between front and rear paws.
- Scale: 1 Unreal unit = 1 cm.
- Sockets:
  - `head_fx`
  - `mouth_fx`
  - `wing_l_root`
  - `wing_r_root`
  - `wing_l_tip`
  - `wing_r_tip`
  - `tail_base`
  - `tail_mid`
  - `tail_stinger`
  - `claw_l`
  - `claw_r`
  - `foot_l`
  - `foot_r`
  - `vfx_venom_drip`
  - `vfx_landing_dust`

Do not import this variant before the base Manticore skeleton and proportion package are approved.

## 14. Folder And Naming Recommendation

- Package folder: `docs/assets/creatures/SK_CRE_Manticore_Interrupt_A01/`
- Source DCC folder: `SourceAssets/Blender/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01/`
- Export folder: `SourceAssets/Exports/Creatures/Manticores/SK_CRE_Manticore_Interrupt_A01/`
- Unreal folder: `/Game/Aerathea/Creatures/Manticores/`
- Mesh: `SK_CRE_Manticore_Interrupt_A01`
- Physics: `PHYS_CRE_Manticore_Interrupt_A01`
- Materials: `MI_CRE_Manticore_Interrupt_A01_*`
- Textures: `T_CRE_Manticore_Interrupt_A01_*`
- Encounter Blueprint: `BP_GNM_OGR_ManticoreInterrupt_A01`

## 15. Quality Gate Checklist

- Reads immediately as lion body, leathery wings, and scorpion tail.
- Tail stinger remains visible in neutral, attack, and distant LOD silhouettes.
- Does not become a dragon, gryphon, hippogryph, demon, or faction machine.
- Does not use feathered wing language for this interrupt variant.
- Supports mid-poly Unreal production with clear material slots and LOD priorities.
- Keeps the Gnome/Ogre rivalry as the core scene while adding a clear interrupt hazard.
- Lists required sockets, collision volumes, animations, and import dependencies.
- Blocks DCC work until base `SK_CRE_Manticore_A01` direction, skeleton, and proportions are approved.
