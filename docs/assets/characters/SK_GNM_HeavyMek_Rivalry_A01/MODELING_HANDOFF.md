# SK_GNM_HeavyMek_Rivalry_A01 Modeling Handoff

## Purpose

Create the first-pass Gnome heavy Mek review mesh for the Gnome-vs-Ogre rivalry kit. This pass validates silhouette, scale, sockets, Unreal import path, startup review placement, and relationship to the existing shield wall. It is not final sculpted, retopologized, textured, or animated production art.

## Source References

- `docs/assets/characters/SK_GNM_HeavyMek_Rivalry_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/CHILD_ASSET_INTAKE.md`
- `GnomeFemaleHeavyMek.png`
- `GnomeFemaleHeavyMek0.png`
- `GnomeFemaleHeavyMek8.png`
- `GnomeFemaleHeavyMek10.png`
- `GnomevsOgre*.png` encounter references

## Production Target

- Asset: `SK_GNM_HeavyMek_Rivalry_A01`
- Type: Skeletal Mesh review asset.
- Height target: approximately 360 cm including shoulder mass, with reactor stacks allowed slightly above.
- Pilot target: visible gnome bust near 110 cm scale.
- Unreal path: `/Game/Aerathea/Characters/Gnomes/Meks/`

## Modeling Constraints

- Use real geometry for the cockpit ring, chest core, shoulder shells, limbs, boots, cannon barrel, hammer/tool head, reactor stacks, and large blue armor panels.
- Use texture and normal maps later for tiny rivets, scratches, panel etching, hair strands, cable detail, and gauge ticks.
- Keep material slots focused: dark iron, brass/copper, blue panel, Aetherium glow, pilot skin/workwear, leather.
- Preserve arm and leg volume for later deformation and physics bodies.
- Do not make this the named Iona hero Mek; keep it generic for encounter reuse.

## Blender Setup

- Build script: `Tools/DCC/build_gnome_heavy_mek.py`
- Blender source output: `SourceAssets/Blender/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01/SK_GNM_HeavyMek_Rivalry_A01.blend`
- FBX export output: `SourceAssets/Exports/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01/SK_GNM_HeavyMek_Rivalry_A01.fbx`
- DCC review output: `Saved/Automation/GnomeHeavyMekReview/SK_GNM_HeavyMek_Rivalry_A01_DCCReview.png`

## Modeling Sequence

1. Block the skeletal proportions first: root, torso, cockpit, reactor, arms, legs, feet, cannon, and hammer/tool arm.
2. Add chest reactor, cockpit ring, pilot bust, goggles, shoulder shells, and blue armor panels.
3. Add left cannon/shield emitter arm and right hammer/tool arm.
4. Add back reactor stacks and Aetherium glow markers.
5. Add sockets and export the review FBX.
6. Import, assign materials, generate LOD0-LOD3, create physics/ABP placeholders, and place the startup actor.

## Triangle Budget

- First-pass blockout: under 25k tris.
- Final common encounter variant: 28k-45k tris.
- Final hero variant: 45k-70k tris only if upgraded to named hero status.

## Texture Deliverables

- `T_GNM_HeavyMek_Rivalry_A01_BC`
- `T_GNM_HeavyMek_Rivalry_A01_N`
- `T_GNM_HeavyMek_Rivalry_A01_ORM`
- `T_GNM_HeavyMek_Rivalry_A01_E`
- Pilot BC/N/ORM set if the pilot remains embedded in the mesh.

## Collision Deliverables

- Generated review physics asset for first pass.
- Final pass should replace generated bodies with a simplified capsule plus major body/limb bodies.
- Weapon and VFX behavior should use sockets, not collision-heavy mesh detail.

## Export Targets

- `/Game/Aerathea/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01`
- `/Game/Aerathea/Characters/Gnomes/Meks/SK_GNM_HeavyMek_Rivalry_A01_Skeleton`
- `/Game/Aerathea/Characters/Gnomes/Meks/PHYS_GNM_HeavyMek_Rivalry_A01`
- `/Game/Aerathea/Characters/Gnomes/Meks/ABP_GNM_HeavyMek_Rivalry_A01`

## Unreal Validation

- Mesh imports and loads.
- Material instances assigned.
- LOD0-LOD3 generated.
- Physics asset assigned.
- Sockets exist: `vfx_reactor_core`, `vfx_shield_l`, `vfx_shield_r`, `weapon_cannon_muzzle`, `pilot_hatch`, `foot_l`, `foot_r`, `vfx_stomp_l`, `vfx_stomp_r`, `weapon_hammer_socket`, `vfx_chest_core`.
- Startup actor `AET_PROD_GNM_HeavyMek_Rivalry_A01` is visible and passes bounds validation.

## Acceptance Checklist

- Heavy Mek silhouette reads clearly as Gnome/Mekgineer.
- Gnome pilot is visibly smaller than the Mek frame.
- Chest core, cannon arm, hammer/tool arm, and shield sockets are readable.
- Asset remains mid-poly and performance-conscious.
- Unreal import path, materials, LODs, sockets, physics, and startup placement validate.
