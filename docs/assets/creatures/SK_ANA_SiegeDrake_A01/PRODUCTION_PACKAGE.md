# SK_ANA_SiegeDrake_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ANA_SiegeDrake_A01`
- Asset type: Skeletal Mesh creature / Anathema siege construct
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `Anathema4.png`, `Anathema1.png`, `Anathema2.png`, `Anathema3.png`
- Current status: Concept direction proposed; approval pending before DCC build

Bound Anathema siege drake with armored draconic mass, mechanical cannon arrays, dark brass/black iron plating, torn wings, and blue-white bound-core energy. It should feel like a forbidden abyssal war construct, not a friendly Mekgineer invention.

## Gameplay Purpose

Raid, world-event, or siege encounter creature. Provides long-range artillery, anti-fortification pressure, mechanical weak points, wing/cannon target zones, and large-creature animation planning.

## Silhouette Notes

Primary read is a huge armored drake with cannon spines over the back, heavy forelegs, broad wings, long tail, horned head, and blue core nodes. Preserve cannon array, drake body, wing outline, and head silhouette.

## Scale Notes

Length: 900-1600 cm. Shoulder height: 450-700 cm. Wingspan: 1200-2200 cm. Author in centimeters with pivot under body mass. Requires encounter-scale review before DCC build.

## Materials And Color Palette

Blackened iron, dark brass, scorched plate, charred wing membrane, ember mouth glow, blue-white bound cores, violet containment arcs. Blue is bound stolen power, not safe Aetherium.

## Concept Image Prompt

Create an original stylized fantasy MMORPG raid creature production sheet of an Anathema Siege Drake for Aerathea. The design should emphasize a huge armored draconic siege construct silhouette, cannon arrays mounted along the back, heavy clawed forelegs, broad torn wings, long tail, horned head, blackened iron, dark brass, scorched plates, blue-white bound-core energy, violet containment arcs, forbidden war-construct mood, and siege artillery gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive cores and cannon muzzles, and MMO-friendly production design. Present it as a creature turnaround with side scale, cannon detail, weak-point callouts, material swatches, collision zones, and LOD callout.

## Modeling Notes

Model drake body, head, horns, wings, tail, main armor plates, cannon barrels, core housings, claws, and large mechanical joints as geometry. Texture small rivets, plate scratches, internal gears, scales, wing veins, and fine scorch marks.

## Texture And Material Notes

Material slots target: 4, maximum 5. Body/scale, armor/brass, wing membrane, cannon/core, emissive. Maps: `T_ANA_SiegeDrake_A01_Body_BC`, `T_ANA_SiegeDrake_A01_Body_N`, `T_ANA_SiegeDrake_A01_Body_ORM`, `T_ANA_SiegeDrake_A01_Armor_BC`, `T_ANA_SiegeDrake_A01_Armor_N`, `T_ANA_SiegeDrake_A01_Armor_ORM`, `T_ANA_SiegeDrake_A01_E`.

## Triangle Budget

LOD0: 80k-100k tris. LOD1: 50k-65k. LOD2: 24k-34k. LOD3: 8k-14k. Use 4K only for hero review or raid boss final; otherwise split into 2K material sets.

## LOD Plan

Preserve drake body, cannon array, wings, horned head, tail, and core glow. Reduce small rivets, minor gears, plate seams, tiny spikes, wing tears, and secondary cannon bevels first.

## Collision Notes

Use large creature movement collision plus physics bodies for head, neck, chest, pelvis, limbs, wings, tail, cannon array, and core weak points. Cannon/projectile collision belongs to gameplay projectiles. No per-rivet or complex-as-simple collision.

## Animation Notes

Idle heavy, wing flex, walk, turn, roar, cannon charge, cannon fire, tail sweep, claw slam, wing buffet, damaged-core reaction, stagger phase, collapse/banish death.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Anathema/SiegeDrake/`
- Skeletal mesh: `SK_ANA_SiegeDrake_A01`
- Skeleton: `SKEL_ANA_SiegeDrake_A01`
- Physics asset: `PHYS_ANA_SiegeDrake_A01`
- Animation Blueprint: `ABP_ANA_SiegeDrake_A01`
- Sockets: `socket_head_vfx`, `socket_mouth_vfx`, `socket_cannon_l`, `socket_cannon_r`, `socket_cannon_center`, `socket_core_chest`, `socket_core_back`, `socket_wing_l_vfx`, `socket_wing_r_vfx`, `socket_tail`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ANA_SiegeDrake_A01/`
- Source: `SourceAssets/Blender/Creatures/Anathema/SK_ANA_SiegeDrake_A01/`
- Export: `SourceAssets/Exports/Creatures/Anathema/SK_ANA_SiegeDrake_A01/`

## Quality Gate Checklist

- Reads as Anathema siege construct, not friendly gnome machinery.
- Cannon array, drake body, wings, and bound cores remain clear through LODs.
- Blue core glow is restrained and framed as bound/stolen power.
- Boss-scale collision and weak-point sockets are defined.
- Triangle budget, maps, LODs, collision, animations, sockets, and Unreal path are defined.
- Not approved for DCC build until Flamestrike selects it.
