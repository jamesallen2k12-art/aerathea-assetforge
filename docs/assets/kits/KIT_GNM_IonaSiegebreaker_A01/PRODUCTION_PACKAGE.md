# KIT_GNM_IonaSiegebreaker_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GNM_IonaSiegebreaker_A01`
- Asset type: Production kit / hero character, heavy Mek, and encounter reference
- Source concept: `Iona.png`
- Related source concept: `Gnome Mek fighting Demon.png`
- Related heavy Mek variants: `GnomeFemaleHeavyMek.png`, `GnomeFemaleHeavyMek0.png`, `GnomeFemaleHeavyMek8.png`, `GnomeFemaleHeavyMek10.png`
- Faction/theme: Gnome/Mekgineer versus Abyss
- Current status: Visual intake complete; first child approved by Flamestrike on 2026-06-28 as `SK_GNM_IonaSiegebreakerMek_A01`; first-pass DCC/Unreal review implementation is imported and validated

Iona is a named gnome/Mekgineer hero-pilot shown in a heavy combat Mek during an Abyss assault. The image is not a generic Aerathea/Common portrait. It should seed a named hero package, a heavy Mek package, and a cross-faction encounter reference.

The added female heavy Mek references support alternate heavy Mek body and armor solutions, but they should not overwrite Iona's named hero silhouette. Shared mechanical language can be reused by `KIT_GNM_OGR_RivalryEncounter_A01`.

First child package:

- `docs/assets/characters/SK_GNM_IonaSiegebreakerMek_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_GNM_IonaSiegebreakerMek_A01/MODELING_HANDOFF.md`
- `docs/assets/characters/SK_GNM_IonaSiegebreakerMek_A01/BUILD_IMPORT_STATUS.md`

First-pass validation locks the Mek foundation at `419.61 cm` visible height with `16` required sockets and startup-scene validation passing. Split `SK_GNM_IonaPilot_A01` and `SM_GNM_IonaArcCannon_A01` after this cockpit and cannon socket contract is accepted for the next asset lane.

## Gameplay Purpose

Supports named NPC planning, Mekgineer hero identity, siege-defense encounter design, gnome crowd scale, heavy Mek locomotion planning, twin arc-cannon weapon sockets, and Abyss invasion narrative beats.

## Silhouette Notes

Primary kit read is a compact gnome pilot inside an oversized heavy Mek frame with huge armored limbs, shoulder/back arc cannons, goggles, exposed face, brass/dark iron plating, blue Aetherium power, and aggressive forward motion.

Preserve gnome readability. The pilot should still be visibly compact, expressive, and gnomish, not hidden inside an anonymous war machine.

## Scale Notes

- Iona pilot: 100-120 cm tall, consistent with approved gnome scale.
- Heavy Mek frame standing height: 320-450 cm depending final locomotion needs.
- Arm cannons: 160-240 cm long.
- Scene demon: reference only for scale; use Abyss packages for actual demon production.

Author in centimeters. Pivot for final Mek should sit at ground center under the Mek body mass. Pilot socket should align to a seated/standing harness origin.

## Materials And Color Palette

Gnome side: dark iron, blackened steel, aged brass, copper trims, leather harnessing, glass goggles, blue Aetherium cores, smoke grime, and warm orange muzzle flare.

Abyss side: charred demon flesh, ember cracks, black flame, and violet/blue impact light. Keep Gnome blue Aetherium visually cleaner and engineered; keep Abyss energy rough, smoky, and entropic.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept sheet of Iona, a gnome Mekgineer hero-pilot from Aerathea, operating a heavy siegebreaker Mek against an Abyss demon invasion. The design should emphasize a compact expressive gnome with goggles and pink or bright hair, a massive brass and dark-iron combat Mek frame, oversized armored fists, twin arc cannons, blue Aetherium power cores, leather harnesses, smoke-grimed plating, heroic battlefield urgency, and siege-defense gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing blue emissive Aetherium accents, and MMO-friendly production design. Present it as a production board with pilot turnaround, Mek front/side/back, cockpit/harness callout, weapon sockets, scale beside a 110 cm gnome and 180 cm humanoid, material swatches, and encounter inset versus an Abyss demon.

## Modeling Notes

Split production into child assets before DCC:

- Iona pilot body/outfit, face, hair, goggles, gloves, and harness.
- Heavy Mek frame with torso cage, oversized limbs, pistons, boots, fists, back/shoulder weapon arms, and Aetherium core.
- Twin arc cannon assembly with muzzle, feed cables, recoil housing, and VFX sockets.
- Encounter dressing reference for ruined wall/city defense, not immediate mesh work.

Model major plates, fists, cannon housings, goggle rims, harness, boots, core housings, and large cables. Texture tiny rivets, scratches, gauge marks, cloth weave, soot, and small bolts.

## Texture And Material Notes

Shared gnome/Mekgineer material language should align with `KIT_MKG_Armory_A01` and existing gnome props: dark iron, brass, copper, leather, and blue Aetherium.

Required map families:

- `T_GNM_IonaPilot_A01_BC/N/ORM`
- `T_GNM_IonaHair_A01_BC/N/ORM`
- `T_GNM_IonaMek_A01_BC/N/ORM/E`
- `T_GNM_IonaArcCannons_A01_BC/N/ORM/E`

Use emissive only for Aetherium cores, goggles if needed, muzzle charge, and small status lamps.

## Triangle Budget

- Iona pilot LOD0: 18k-25k tris.
- Heavy Mek frame LOD0: 45k-70k tris.
- Arc cannon assemblies included in frame budget unless detached.
- Combined hero review target: under 90k tris visible at once.

Use 2K texture sets for pilot and 2K-4K for Mek depending hero/cinematic priority.

## LOD Plan

LOD0: full pilot face/hair/goggles, cockpit/harness, major Mek plates, fists, cannons, cables, and Aetherium cores.

LOD1: reduce small plate bevels, minor cables, interior cockpit parts, hair strand cards, and cannon housing cuts.

LOD2: merge armor groups, simplify pistons, reduce hand/finger detail, simplify goggles and hair mass.

LOD3: preserve gnome head/read, Mek torso, fists, cannon silhouette, and blue core glow.

## Collision Notes

Pilot collision follows character capsule if separated. Mek requires a custom movement capsule or vehicle/creature collision profile after gameplay rules are approved. Weapon fire uses muzzle sockets and projectile traces, not mesh collision.

## Animation Notes

Pilot: idle in harness, command gestures, hit reaction, victory/taunt, emergency eject only if gameplay requires it.

Mek: idle engine rumble, heavy walk, turn, brace, fist punch, cannon aim, cannon fire, recoil, overheat vent, hit reaction, shutdown/kneel, death or disabled state.

## Unreal Import Notes

- Suggested Unreal root: `/Game/Aerathea/Characters/Gnomes/Iona/`
- Pilot skeletal mesh: `SK_GNM_IonaPilot_A01`
- Mek skeletal mesh: `SK_GNM_IonaSiegebreakerMek_A01`
- Optional assembled Blueprint: `BP_GNM_IonaSiegebreaker_A01`
- Materials: `/Game/Aerathea/Materials/Gnome/Iona/`
- VFX: `/Game/Aerathea/VFX/Gnome/AetheriumArc/`
- Sockets: `socket_pilot_harness`, `socket_cannon_l_muzzle`, `socket_cannon_r_muzzle`, `socket_core_chest`, `socket_core_back`, `socket_hand_l`, `socket_hand_r`, `socket_vent_l`, `socket_vent_r`

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_GNM_IonaSiegebreaker_A01/`
- Source: `SourceAssets/Blender/Characters/Gnomes/Iona/`
- Export: `SourceAssets/Exports/Characters/Gnomes/Iona/`

Child package order:

1. `SK_GNM_IonaSiegebreakerMek_A01` - approved first child; first-pass DCC/Unreal review implementation imported and validated.
2. `SK_GNM_IonaPilot_A01` - split after Mek cockpit/harness scale lock.
3. `SM_GNM_IonaArcCannon_A01` - split after Mek cannon socket lock.
4. `BP_GNM_IonaSiegebreaker_A01` - assemble after pilot, Mek, and cannon packages are stable.

## Quality Gate Checklist

- Iona reads as a compact Aerathea gnome, not a short human.
- Heavy Mek uses established Mekgineer brass/dark iron/leather/blue Aetherium language.
- Demon content remains reference only unless promoted through Abyss packages.
- Main forms are modeled; tiny bolts, scratches, and gauge marks are textured.
- LODs, collision, sockets, animation list, maps, and Unreal paths are defined.
- First child direction is approved for `SK_GNM_IonaSiegebreakerMek_A01`; first-pass implementation is validated, while final art-model sculpt/UV/texture/animation work remains pending.
