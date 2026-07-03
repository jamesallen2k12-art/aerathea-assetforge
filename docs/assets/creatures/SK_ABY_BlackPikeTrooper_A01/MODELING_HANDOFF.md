# SK_ABY_BlackPikeTrooper_A01 Modeling Handoff

## Approved Direction

Build a standard Abyss BlackPike infantry unit, not a boss or winged elite. Use `AbyssalTroops3.png` as the primary pike-line anchor and `AbyssalTroops8.png` for shield-line armor mass. Treat `AbyssalTroops2.png`, `AbyssalTroops6.png`, `AbyssalTroops10.png`, and `AbyssalDemon2.png` as formation or variant references only.

## Scale And Pivot

- Body height target: 220 cm.
- Body range: 200-230 cm.
- Pike length: 300-340 cm.
- Pivot: ground center between feet.
- Unit scale: centimeters.
- Startup review actor: `AET_PROD_ABY_BlackPikeTrooper_A01`.

## Required Geometry

Model as real geometry:

- Main humanoid body masses.
- Horned helmet and brow/jaw guard.
- Major shoulder plates and shoulder spikes.
- Chest slab, back plate, belt, bracers, greaves, boots.
- Pike shaft, blade, crossbar, and large weapon bevels.
- Readable ash cloth strips.
- Shield-line forearm plate variant.

Fake with textures, normals, or masks:

- Fine pitting and scratches.
- Tiny cracks and runes.
- Cloth weave/fray.
- Small straps.
- Minor chips and dents.

## Silhouette Requirements

The game-camera read must be: horned infantry plus long pike. Do not let internal armor noise, tiny spikes, heavy smoke, or full-body glow overpower the pike, helmet, shoulder width, chest slab, and stance.

## Materials And UV Plan

Final material targets:

- Flesh/charred skin.
- Scorched iron armor.
- Ash cloth.
- Bone horn.
- Black iron pike.
- Violet emissive eyes/weapon edge.
- Ember emissive chest fissure.

Final texture set:

- `T_ABY_BlackPikeTrooper_A01_BC`
- `T_ABY_BlackPikeTrooper_A01_N`
- `T_ABY_BlackPikeTrooper_A01_ORM`
- `T_ABY_BlackPikeTrooper_A01_E`

Use 2K textures for the standard enemy. Reserve 4K only for a hero/officer variant.

## Skeleton And Sockets

The first-pass imported skeleton is `/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01_Skeleton`.

Required sockets:

- `socket_weapon_r`
- `socket_weapon_l`
- `socket_pike_tip`
- `socket_head_vfx`
- `socket_eye_l`
- `socket_eye_r`
- `socket_chest_core`
- `socket_banner_back`
- `socket_ground_rift`
- `socket_hit_trace_pike`

Preserve these names unless the animation/VFX contract is intentionally revised.

## LOD Targets

- LOD0: 22k-28k tris.
- LOD1: 14k-18k tris.
- LOD2: 7k-10k tris.
- LOD3: 2k-4k tris.

Reduce tiny chips, minor straps, small cloth cuts, inner armor gaps, finger/gauntlet detail, and secondary bevels before reducing the pike, horn crest, chest slab, or shoulder silhouette.

## Collision And Physics

Use a humanoid movement capsule in gameplay. Physics asset should cover head, chest, pelvis, limbs, hands, feet, and pike trace proxy. Keep collision simple and animation-friendly.

## Animation Needs

Idle, alert idle, patrol walk, combat walk, turn in place, pike thrust, sweeping pike attack, shield brace variant, hit front, hit side, stagger, death, summon/portal spawn, and formation hold.

## First-Pass Files

- Blender source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01/SK_ABY_BlackPikeTrooper_A01.blend`
- FBX export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01/SK_ABY_BlackPikeTrooper_A01.fbx`
- DCC review render: `Saved/Automation/AbyssBlackPikeReview/SK_ABY_BlackPikeTrooper_A01_DCCReview.png`

## Final Delivery Checklist

- Final sculpt/retopo replaces first-pass block geometry.
- UVs and texture sets authored.
- Runtime material slots reduced where practical.
- LOD0-LOD3 authored and validated.
- Physics asset tuned.
- Socket names preserved and positioned.
- Animation set imported or retargeted.
- Startup/focused validators pass.
- Visual approval capture compares Unreal view against approved concept/DCC proof.
