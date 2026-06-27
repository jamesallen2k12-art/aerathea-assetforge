# SK_CRE_Manticore_Interrupt_A01 Modeling Handoff

## Handoff Status

- Current state: production planning and modeling handoff ready.
- DCC state: blocked until base `SK_CRE_Manticore_A01` body, skeleton, and proportion direction are approved.
- Intended use: encounter-specific variant for the Gnome/Ogre rivalry interrupt source.

## Source References

| Source | Use |
| --- | --- |
| `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/GnomevsOgreandManticore8.png` | Encounter staging: Manticore arrives as third-party pressure between heavy Mek and Ogre force |
| `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Manticore.png` | Primary anatomy reference: lion body, leathery bat/draconic wings, scorpion tail |
| `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Manticore8.png` | Ruin-stalker mood, tail arc, wing membrane, forward threat posture |
| `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Manticore5.png` | Optional stalking posture and overgrown/forest variant cues; do not copy feathered wing language |

## Approved Shape Language

- Lion body with muscular shoulders, strong forelegs, lower stalking posture, and large mane.
- Leathery bat/draconic wings, not feathered bird wings.
- High scorpion tail arc with heavy segmented chitin and an oversized hooked stinger.
- Wild predator surface language: scars, dust, torn membrane, dark claws, tail venom accents.
- No Gnome Aetherium hardware, no Ogre Teknomancy devices, no saddles, and no faction banners.

## Blockout Requirements

1. Build body mass first from simple proportional primitives.
2. Establish shoulder height at 230-260 cm and wing span at 900-1100 cm.
3. Add folded-wing silhouette and a separate wing-spread pose check.
4. Add tail segment chain with enough joints for sting, sweep, and idle curl poses.
5. Place the stinger so it remains visible above the body in gameplay camera angles.
6. Confirm scale against `SK_GNM_HeavyMek_Rivalry_A01`, `SK_OGR_Warrior_Rival_A01`, and `SM_OGR_CairnBattleGate_A01`.

## Geometry Priorities

Model as geometry:

- Main lion body, head, muzzle, ears, paws, claws, teeth, and mane silhouette clumps.
- Wing arm bones, wing fingers, major membrane panels, and torn membrane outline.
- Tail segments, stinger shell, venom groove, and main chitin ridges.
- Major scar plates, horn/spike accents if approved, and thick claw forms.

Use textures/normal maps for:

- Fine fur direction.
- Small scars and scratches.
- Membrane wrinkles.
- Tiny chips on tail plates.
- Small venom stains.
- Dirt, dust, and dried blood.

## Topology Notes

- Preserve clean deformation loops around shoulders, hips, wing roots, elbows, paws, tail base, and tail segment pivots.
- Avoid dense mane strand geometry; use large clump shapes and texture detail.
- Use membrane topology that can fold without collapsing into long skinny triangles.
- Tail segments should overlap like armor plates without clipping badly during tight curls.
- Keep stinger topology simple enough for LOD reduction and hit trace readability.

## Socket Plan

Required sockets:

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

## Material Slots

1. Body and mane.
2. Wings and membrane.
3. Tail, claws, teeth, and stinger.
4. Optional venom telegraph material.

Do not exceed 4 material slots.

## LOD And Collision Targets

| LOD | Target | Notes |
| --- | --- | --- |
| LOD0 | 35k-50k tris | Full silhouette, wings, tail chain, stinger, mane mass |
| LOD1 | 55-60 percent | Reduce mane clumps, small bevels, minor membrane tears |
| LOD2 | 25-35 percent | Preserve body, wing profile, high tail arc, and stinger |
| LOD3 | 10-15 percent | Large color blocks and readable creature type only |

Collision:

- Main capsule or body-blocking shape around torso.
- Physics bodies for torso, head, wing roots, legs, tail chain, and stinger.
- Gameplay overlaps for wing buffet, tail sting, tail sweep, venom spit, and landing dust.

## Animation Planning Notes

The interrupt set must support:

- Arrival glide or leap into battle.
- Stalking idle and short charge.
- Wing spread threat and wing buffet.
- Tail sting and tail sweep.
- Bite/claw combo.
- Roar and hit reactions.
- Wounded retreat and death.

The base Manticore animation set should own locomotion and idle behavior; this package adds encounter-specific interrupt poses and VFX timing.

## Review Checklist

- Lion, wing, and scorpion-tail silhouette reads from top-down and third-person gameplay cameras.
- Wing membrane is leathery and bat/draconic.
- Tail stinger remains visible when folded, prowling, or attacking.
- The creature looks wild and independent from both battlefield factions.
- The mesh can share a future base Manticore skeleton and animation set.
- Mid-poly budget, materials, LODs, sockets, collision, and Unreal paths match the production package.
