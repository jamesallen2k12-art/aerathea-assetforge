# SM_OGR_CairnBattleGate_A01 Modeling Handoff

## Purpose

Create a first-pass Ogre cairn battle-gate review mesh for the Gnome/Ogre rivalry kit. This validates gate scale, fortress silhouette, material slots, static mesh sockets, simple collision, LODs, startup placement, and relationship to the Ogre Warrior/Teknomancer and Gnome Heavy Mek scene.

## Source References

- `docs/assets/props/SM_OGR_CairnBattleGate_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/PRODUCTION_PACKAGE.md`
- `OgreGate.png`
- `OgreFortress.png`
- `Ogres3.png`
- `Ogres7.png`
- `Ogres8 .png`

## Production Target

- Asset: `SM_OGR_CairnBattleGate_A01`
- Type: Static Mesh review module.
- Unreal path: `/Game/Aerathea/Props/Ogres/CairnFortifications/`
- Startup actor: `AET_PROD_OGR_CairnBattleGate_A01`
- Pivot: ground center of the gate opening.

## Modeling Constraints

- Use a single combined static mesh for first-pass review.
- Prioritize chunky silhouette over tiny stone detail.
- Model large forms: towers, wall blocks, arch, gate bars, doors, skull crest, large spikes, banners, braziers, and major chains.
- Keep tiny cracks, chipped edges, micro rivets, small runes, and chain texture for later normal/albedo work.
- Include simple collision proxy objects or collision-ready geometry.
- Add DCC locator equivalents for snap, VFX, banner, portcullis, and defender positions.

## Blender Setup

- Build script: `Tools/DCC/build_ogre_cairn_gate.py`
- Blender source output: `SourceAssets/Blender/Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01/SM_OGR_CairnBattleGate_A01.blend`
- FBX export output: `SourceAssets/Exports/Props/Ogres/CairnFortifications/SM_OGR_CairnBattleGate_A01/SM_OGR_CairnBattleGate_A01.fbx`
- DCC review output: `Saved/Automation/OgreCairnGateReview/SM_OGR_CairnBattleGate_A01_DCCReview.png`

## Modeling Sequence

1. Build the base plinth and left/right cairn wall masses.
2. Add two side tower masses with large stacked block shapes.
3. Add central gate doors, portcullis bars, iron braces, and top beam.
4. Add skull crest, large horns/spikes, banner drops, chain hints, and brazier bowls.
5. Add simple UCX collision blocks for walls, towers, arch, and closed gate.
6. Export the first-pass FBX.
7. Import, assign material instances, generate LOD0-LOD3, add sockets, and place the startup review actor.

## Material Slots

- `M_OGR_CairnStone_Blockout_A01`
- `M_OGR_Iron_Blockout_A01`
- `M_AET_Timber_Handpainted_A01`
- `M_OGR_Bone_Blockout_A01`
- `M_OGR_Warpaint_Blockout_A01`
- `M_OGR_TekGlow_Blockout_A01`
- `M_OGR_Brass_Blockout_A01`

## Collision Notes

- `UCX_SM_OGR_CairnBattleGate_A01_00`: left tower/wall blocker.
- `UCX_SM_OGR_CairnBattleGate_A01_01`: right tower/wall blocker.
- `UCX_SM_OGR_CairnBattleGate_A01_02`: central arch/top blocker.
- `UCX_SM_OGR_CairnBattleGate_A01_03`: closed gate blocker.
- Banners, chains, skulls, and spikes are visual only.

## Socket Checklist

- `snap_wall_l`
- `snap_wall_r`
- `gate_center`
- `portcullis_top`
- `portcullis_bottom`
- `vfx_brazier_l`
- `vfx_brazier_r`
- `vfx_gate_forge`
- `vfx_skull_crest`
- `socket_banner_l`
- `socket_banner_r`
- `ai_gate_defender_l`
- `ai_gate_defender_r`

## Acceptance Checklist

- The module reads as a brutal Ogre cairn gate at startup-camera distance.
- Gate clearance is visibly Ogre-scale.
- Skull crest, red banners, barred gate, and tower masses are clear.
- Material slots, LODs, collision, sockets, source paths, and Unreal path are ready.
- Final sculpt, authored UVs/textures, tuned collision, and Blueprint gate behavior remain explicitly pending.
