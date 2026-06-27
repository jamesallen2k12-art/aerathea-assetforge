# SM_GNM_AetherShieldProjector_A01 Production Package

## Art Direction Summary

`SM_GNM_AetherShieldProjector_A01` is the reusable Gnome/Mekgineer shield projector for `BP_GNM_HeavyMekShieldwall_A01`. It should read as compact, precise, and engineered: squat dark-iron feet, brass service frames, readable blue Aetherium reactor core, paired shield emitter vanes, and small gnome-scale controls.

## Gameplay Purpose

- Provides the physical anchor for Gnome defensive shield-wall encounters.
- Supports standalone field placement and later heavy Mek socket attachment.
- Supplies VFX sockets for shield arcs, impacts, damage sparks, and core pulses.

## Silhouette Notes

- Squat and stable, wider than it is tall.
- Paired side vanes should clearly imply a projected shield field.
- Operator-side handles must keep the object visibly gnome-scaled.
- Avoid Ogre-style crude bulk, forge-orange power, or necromantic green.

## Scale Notes

- Review mesh target: roughly 140 cm wide by 140 cm deep by 120 cm tall.
- Authored in centimeters with origin at ground center.
- +X is the shield-emitter side; -X is the operator side.

## Materials And Color Palette

- Dark iron feet, base, and internal housing.
- Brass/copper frames, collars, clamps, and service plates.
- Blue/cyan Aetherium reactor and emitter crystals.
- Dark leather may be added in final art for handles or padded controls.

## Concept Image Prompt

Create an original stylized fantasy MMORPG prop concept sheet of `SM_GNM_AetherShieldProjector_A01` for the world of Aerathea. The design should emphasize a compact Gnome/Mekgineer shield projector, squat stabilizer feet, brass and dark-iron engineered construction, blue Aetherium reactor core, paired shield emitter vanes, small gnome-scale controls, precise defensive technology, and MMO-friendly production design. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and production-friendly geometry. Present it as a clean prop sheet with front, side, top, socket callouts, material swatches, and scale beside a 110 cm gnome. Avoid copied franchise designs, excessive micro-detail, unreadable clutter, text, and watermarks.

## Modeling Notes

- Model real geometry for feet, base slab, core housing, collars, vanes, handles, and emitter crystals.
- Fake small rivets, gauge ticks, scratches, and tiny seams in normal/texture maps.
- Keep side vanes broad enough to read from gameplay distance.
- Required sockets: `vfx_core`, `vfx_shield_emit_l`, `vfx_shield_emit_r`, `attach_mek_l`, `attach_mek_r`, `damage_spark`.

## Texture And Material Notes

- `T_GNM_AetherShieldProjector_A01_BC`
- `T_GNM_AetherShieldProjector_A01_N`
- `T_GNM_AetherShieldProjector_A01_ORM`
- `T_GNM_AetherShieldProjector_A01_E`
- Material instances: brass, dark iron, leather/dark grip if added, and Aetherium core.

## Triangle Budget

- LOD0 target: 3k-8k tris.
- Material slots: 1-2 final target, review import may use shared blockout material instances.

## LOD Plan

- LOD0: full base, vanes, core, collars, handles, and major clamps.
- LOD1: reduce bevels and minor brackets.
- LOD2: simplify vanes, core frame, and service plates.
- LOD3: preserve squat base, blue core, and paired emitter silhouette.

## Collision Notes

- Simple box/convex collision around base and body.
- Emitter crystals, handles, small cables, and micro detail remain non-blocking.

## Animation Notes

- No skeletal animation required.
- Future Blueprint may pulse core emissive, rotate vanes slightly, or spark at `damage_spark`.

## Unreal Import Notes

- Asset type: Static Mesh.
- Unreal path: `/Game/Aerathea/Props/Gnomes/Mekgineer/SM_GNM_AetherShieldProjector_A01`.
- Source path: `SourceAssets/Blender/Kits/GnomeOgre/RivalryEncounter/BP_GNM_HeavyMekShieldwall_A01/SM_GNM_AetherShieldProjector_A01/`.
- Export path: `SourceAssets/Exports/Kits/GnomeOgre/RivalryEncounter/BP_GNM_HeavyMekShieldwall_A01/SM_GNM_AetherShieldProjector_A01/`.
- Pivot: ground center.
- LOD0-LOD3 required.

## Folder And Naming Recommendation

- Package folder: `docs/assets/props/SM_GNM_AetherShieldProjector_A01/`.
- Material instances: `/Game/Aerathea/Materials/Instances/MI_GNM_AetherShieldProjector_A01_*`.
- Blueprint consumer: `/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_HeavyMekShieldwall_A01`.

## Quality Gate Checklist

- Reads as Gnome/Mekgineer precision technology.
- Blue Aetherium is the only active power color.
- Sockets exist and match the Shieldwall Blueprint contract.
- LODs, material slots, collision, pivot, scale, and Unreal path are defined.
