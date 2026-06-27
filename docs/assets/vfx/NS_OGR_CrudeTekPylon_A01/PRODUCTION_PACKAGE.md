# NS_OGR_CrudeTekPylon_A01 Production Package

## 1. Art Direction Summary

`NS_OGR_CrudeTekPylon_A01` is the Ogre Teknomancy overload effect for the crude battlefield pylon. It should read as unstable forge-orange magic-tech with blackened-iron heat shimmer, rough blue-white anti-Mek discharge accents, and a violent but controlled battlefield-objective silhouette.

Current status: template-derived first-pass Niagara system and emitter target exist in Unreal and are assigned to `BP_OGR_CrudeTekPylon_A01`. Bespoke emitter graph polish remains pending.

## 2. Gameplay Purpose

The effect communicates that the pylon is powering Ogre siege pressure, disrupting Gnome Mek defenses, or entering an overload objective state. Players should understand idle, charged, overload, damaged, and destroyed states at a glance.

## 3. Silhouette Notes

- Primary read: vertical core energy column rising from the pylon body.
- Secondary read: rough conductor arcs from core to top fork.
- Tertiary read: ground sparks around the lower cairn base.
- Avoid clean gnomish precision, perfect circles, or elegant wizard geometry.

## 4. Scale Notes

- VFX is attached to `BP_OGR_CrudeTekPylon_A01`.
- Local core height should fit the pylon body, not exceed Ogre character scale.
- Ground sparks should stay within the pylon objective footprint.

## 5. Materials and Color Palette

- Forge orange and furnace yellow for crude Tek heat.
- Soot-black smoke flecks used sparingly.
- Blue-white discharge only as anti-Mek contrast.
- No necromantic green unless a future necromancer variant is explicitly created.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG VFX concept sheet of `NS_OGR_CrudeTekPylon_A01` for the world of Aerathea. The design should emphasize a rough Ogre Teknomancy pylon overload, furnace-orange core surges, blackened-iron heat distortion, crude conductor arcs, ground sparks, unstable anti-Mek blue-white discharge, and a gameplay role as a battlefield objective powering Ogre siege pressure. Use readable shapes, hand-painted texture language, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly VFX density. Present it as a VFX state board with idle, charged, overload, damaged, and destroyed frames plus socket callouts. Avoid copied franchise designs, clean gnome precision, excessive particle storms, and full-screen bloom.

## 7. Modeling Notes

No new mesh is required for the first VFX pass. Use sockets and locators from `SM_OGR_CrudeTekPylon_A01` and `AAETCrudeTekPylonActor`: `CoreLocator`, `TopArcLocator`, and `GroundSparksLocator`.

## 8. Texture and Material Notes

- Use low-overdraw sprite/ribbon materials.
- Suggested future textures: `T_OGR_CrudeTekPylon_VFX_Noise_A01`, `T_OGR_CrudeTekPylon_VFX_Spark_A01`, `T_OGR_CrudeTekPylon_VFX_ArcMask_A01`.
- Material blend should stay additive/translucent only where needed.
- No dynamic lights by default.

## 9. Triangle Budget

Niagara sprite/ribbon effect only. Mesh particles are not planned for the first polished pass. If mesh particles are added later, keep them under 500 tris total near-camera.

## 10. LOD Plan

- LOD0: core pulse, conductor arcs, ground sparks, overload burst.
- LOD1: core pulse, reduced conductor arcs, sparse sparks.
- LOD2: core pulse and occasional arc only.
- LOD3: material glow on the pylon mesh only; Niagara can cull.

## 11. Collision Notes

No VFX collision. Gameplay collision remains on the pylon mesh and encounter trigger volumes.

## 12. Animation Notes

Driven by pylon state and scalar parameters:

- `User.PylonState`
- `User.OverloadPercent`
- `User.DamagePercent`
- `User.DamageWindowAlpha`
- `User.RepairWindowAlpha`
- `User.DamageTraceRadius`
- `User.RepairTraceRadius`
- `User.bOverloaded`
- `User.bDestroyed`
- `User.bDamageWindowActive`
- `User.bRepairWindowActive`
- `User.StateColor`
- `User.CoreWorldLocation`
- `User.TopArcWorldLocation`
- `User.GroundSparksWorldLocation`

## 13. Unreal Import Notes

- Asset type: Niagara System.
- System path: `/Game/Aerathea/VFX/Ogres/NS_OGR_CrudeTekPylon_A01`
- Emitter target: `/Game/Aerathea/VFX/Ogres/NE_OGR_CrudeTekPylon_Overload_A01`
- Native consumer: `AAETCrudeTekPylonActor`
- Blueprint consumer: `/Game/Aerathea/Blueprints/Ogres/BP_OGR_CrudeTekPylon_A01`
- Component: `PylonNiagara`
- Validation: `Tools/Unreal/validate_startup_scene.py`, `Tools/Unreal/validate_gnome_ogre_gameplay_timing_traces.py`

## 14. Folder and Naming Recommendation

- Package folder: `docs/assets/vfx/NS_OGR_CrudeTekPylon_A01/`
- Unreal folder: `/Game/Aerathea/VFX/Ogres/`
- System: `NS_OGR_CrudeTekPylon_A01`
- Emitter: `NE_OGR_CrudeTekPylon_Overload_A01`

## 15. Quality Gate Checklist

- Reads as Ogre Teknomancy, not Gnome Aetherium.
- Overload state is clear at gameplay camera distance.
- Uses the native pylon `User.*` contract.
- Does not obscure the pylon mesh silhouette.
- Keeps emissive intensity restrained.
- Has distance scalability and culling behavior.
- Avoids dynamic lights and heavy overdraw.
- Startup validation passes before visual approval.
