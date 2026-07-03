# SK_ABY_BlackPikeTrooper_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_BlackPikeTrooper_A01`
- Asset type: Skeletal Mesh creature / enemy infantry
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalTroops3.png`, `AbyssalTroops8.png`, `AbyssalDemon2.png`, `AbyssalTroops2.png`, `AbyssalTroops6.png`, `AbyssalTroops10.png`
- Current status: Approved first Abyss/Anathema DCC child; first-pass Blender source, FBX export, Unreal skeletal import, sockets, LOD0-LOD3, physics asset, ABP placeholder, startup actor, focused validation, and startup validation are complete.

Standard Abyss infantry for readable war-host encounters. The design is disciplined and frightening rather than chaotic: horned helmet or skull crest, long black pike, charred armor plates, torn ash cloth, ember chest fissures, and restrained violet-black weapon and eye glow.

Source interpretation: `AbyssalTroops3.png` is the primary pike-infantry anchor, `AbyssalTroops8.png` provides shield-line armor mass, and `AbyssalTroops2.png`, `AbyssalTroops6.png`, `AbyssalTroops10.png`, and `AbyssalDemon2.png` are variant or formation references only. Do not add wings, boss-scale horns, oversized VFX, or elite caster forms to the base trooper.

## Gameplay Purpose

Baseline melee enemy for Abyss patrols, army lines, fortress assaults, portal waves, and early combat readability tests. It establishes the standard Abyss humanoid scale before elite reavers, casters, hounds, siege brutes, and lords are built.

## Silhouette Notes

Primary read is a tall horned infantry shape with a long vertical pike. Preserve the pike line, horn crest, shoulder spikes, chest armor slab, narrow helm, and compact shield-line variant plate at distance. The base trooper should remain readable as infantry, not an officer, flying demon, or boss.

## Scale Notes

- Body target: 220 cm.
- Approved range: 200-230 cm for standard BlackPike infantry.
- Pike length target: 300-340 cm.
- First-pass Unreal visible bounds: 314.58 cm including the raised pike.
- Pivot: ground center under feet.
- Authoring units: centimeters.

## Materials And Color Palette

First-pass Unreal materials:

- `M_ABY_CharredFlesh_Blockout_A01`
- `M_ABY_ScorchedIron_Blockout_A01`
- `M_ABY_AshCloth_Blockout_A01`
- `M_ABY_BoneHorn_Blockout_A01`
- `M_ABY_PikeBlackIron_Blockout_A01`
- `M_ABY_VoidGlow_Blockout_A01`
- `M_ABY_EmberFissure_Blockout_A01`

Final color language: obsidian black, charred iron, blackened leather, scorched bone horn, ash-gray cloth, ember fissures, and restrained violet glow on the eyes and pike edge.

## Concept Image Prompt

Create an original stylized fantasy MMORPG enemy production sheet of an Abyss Black Pike Trooper for the world of Aerathea. The design should emphasize a tall horned infantry silhouette, long black pike, charred iron armor, scorched bone crest, torn ash cloth, ember fissures, violet abyssal weapon glow, disciplined war-host identity, and standard melee enemy gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive eyes and weapon accents, and MMO-friendly production design. Present it as a turnaround with front, side, back, weapon detail, material swatches, socket callouts, LOD notes, and scale beside a 180 cm humanoid. Avoid copied franchise designs, wings, boss proportions, excessive micro-spikes, gore, unreadable smoke, and full-body glow.

## Modeling Notes

Model the body mass, helmet, horns, shoulder plates, pike shaft/head, large armor slabs, boots, bracers, greaves, and readable cloth strips as geometry. Texture or normal-map fine pitting, cloth fray, tiny scratches, small rune cuts, and minor straps.

The current first-pass DCC source exists at `SourceAssets/Blender/Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01/SK_ABY_BlackPikeTrooper_A01.blend` and exports to `SourceAssets/Exports/Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01/SK_ABY_BlackPikeTrooper_A01.fbx`. It is a scale/silhouette/socket review mesh, not final sculpted or painted art.

## Texture And Material Notes

Final maps:

- `T_ABY_BlackPikeTrooper_A01_BC`
- `T_ABY_BlackPikeTrooper_A01_N`
- `T_ABY_BlackPikeTrooper_A01_ORM`
- `T_ABY_BlackPikeTrooper_A01_E`

Recommended final material slots: body/flesh, armor, cloth, horn, pike, violet emissive, ember emissive. If final texture authoring can merge slots without hurting variation, reduce to 3-4 runtime material slots.

## Triangle Budget

- LOD0: 22k-28k tris.
- LOD1: 14k-18k tris.
- LOD2: 7k-10k tris.
- LOD3: 2k-4k tris.

The first-pass Unreal mesh has generated LOD0-LOD3 for validation only; final LODs need authored reduction after retopo.

## LOD Plan

Preserve the pike, horn crest, shoulder width, helm read, chest slab, and stance first. Reduce cloth cuts, small spikes, strap loops, finger/gauntlet detail, inner armor gaps, horn bevels, and minor pike bevels before changing the primary outline.

## Collision Notes

Use a humanoid movement capsule for gameplay. Use a simple physics asset for head, chest, pelvis, upper/lower arms, hands, upper/lower legs, feet, and a lightweight pike trace proxy. Do not use complex-as-simple collision.

## Animation Notes

Required set: idle, alert idle, patrol walk, combat walk, turn in place, pike thrust, sweeping pike attack, shield brace variant, hit front, hit side, stagger, death, summon/portal spawn, and formation hold.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/`
- Skeletal mesh: `/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01`
- Generated skeleton: `/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/SK_ABY_BlackPikeTrooper_A01_Skeleton`
- Physics asset: `/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/PHYS_ABY_BlackPikeTrooper_A01`
- Animation Blueprint placeholder: `/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/ABP_ABY_Trooper_A01`
- Startup actor: `AET_PROD_ABY_BlackPikeTrooper_A01`
- Startup actor location: `(1040, 220, 0)` with yaw `-42`
- Required sockets: `socket_weapon_r`, `socket_weapon_l`, `socket_pike_tip`, `socket_head_vfx`, `socket_eye_l`, `socket_eye_r`, `socket_chest_core`, `socket_banner_back`, `socket_ground_rift`, `socket_hit_trace_pike`
- Import script: `Tools/Unreal/import_abyss_blackpike_trooper.py`
- Focused validator: `Tools/Unreal/validate_abyss_blackpike_trooper.py`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_BlackPikeTrooper_A01/`
- Build status: `docs/assets/creatures/SK_ABY_BlackPikeTrooper_A01/BUILD_IMPORT_STATUS.md`
- Modeling handoff: `docs/assets/creatures/SK_ABY_BlackPikeTrooper_A01/MODELING_HANDOFF.md`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01/`

## Quality Gate Checklist

- Reads clearly as standard Abyss infantry.
- Pike, horn crest, armor mass, and stance remain readable from game camera.
- Uses shadow/flame materials distinct from Dark Elves.
- Glow is limited to eyes, weapon edge, and small chest fissures.
- Triangle budget, maps, LODs, collision, animation list, sockets, and Unreal path are defined.
- First-pass DCC source, FBX, Unreal import, LOD0-LOD3, physics asset, ABP placeholder, startup actor, focused validator, and startup validator are complete.
- Final sculpt, retopo, authored UVs/textures, tuned physics bodies, final animation, final VFX, and visual approval capture remain pending.
