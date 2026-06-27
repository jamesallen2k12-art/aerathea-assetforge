# BP_GNM_HeavyMekShieldwall_A01 Production Package

## Art Direction Summary

`BP_GNM_HeavyMekShieldwall_A01` is the first child package from `KIT_GNM_OGR_RivalryEncounter_A01`. It defines a reusable Gnome/Mekgineer defensive shield-wall assembly for encounters where compact gnome pilots and heavy Mek frames hold a line against huge Ogre warriors and crude Teknomancers.

The visual read should be tactical, compact, and engineered: brass-and-dark-iron projector hardware, blue Aetherium shield arcs, short squat field braces, small gnome pilot access points, and a clean defensive crescent that contrasts with Ogre mass and forward pressure.

## Gameplay Purpose

- Establishes the Gnome side of the Gnome-vs-Ogre battlefield identity.
- Supports defensive event scripting, encounter staging, dungeon pulls, quest scenes, and startup review placement later.
- Gives designers a reusable shield volume, impact VFX anchor, and Mek attachment target before full heavy Mek animation is complete.
- Creates a production dependency path for `SM_GNM_AetherShieldProjector_A01`, `VFX_GNM_AetherShieldWall_A01`, and future heavy Mek sockets.

## Silhouette Notes

- Shield wall must read as a crescent or segmented barricade, not a flat glowing sheet.
- Use three to five squat projector units with heavy feet, side vanes, coil braces, and blue Aetherium cores.
- Blue shield arcs should connect between projectors and lean slightly toward the Ogre threat side.
- The hardware should feel precise and compact, unlike Ogre crude Teknomancy.
- Keep gnome scale visible through small handles, access hatches, cockpit-like controls, or operator platforms.

## Scale Notes

- Individual projector: 90-140 cm tall, 100-160 cm wide, 80-140 cm deep.
- Shield wall segment: 500-900 cm wide depending on number of projector units.
- VFX height: 260-420 cm so it can defend heavy Mek frames while still showing 10-11 ft Ogres above or behind it when needed.
- Blueprint pivot: ground center of the shield-wall arc.
- Projector sockets should align to heavy Mek `vfx_shield_l`, `vfx_shield_r`, or standalone ground placement.

## Materials And Color Palette

- Gnome hardware: warm brass, copper, dark iron, charcoal plates, leather grip wraps.
- Aetherium: blue, cyan, blue-white core highlights.
- Ground contact: dark iron stabilizers and small dust/debris decals only.
- Shield VFX: translucent blue edge bands, low-frequency pulse, impact ripples, restrained sparks.
- Avoid Ogre forge orange or necromantic green in the Gnome shield-wall asset.

## Concept Image Prompt

Create an original stylized fantasy MMORPG Blueprint/encounter asset sheet of `BP_GNM_HeavyMekShieldwall_A01` for the world of Aerathea. The design should emphasize compact Gnome/Mekgineer shield projectors, brass and dark-iron engineered hardware, blue Aetherium reactor cores, a segmented crescent shield wall, readable gnome-scale controls, tactical defensive posture against huge Ogre pressure, and MMO-friendly production design. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and production-friendly geometry. Present it as a clean Blueprint kit sheet with projector front/side views, shield arc layout, socket callouts, VFX states, scale beside a 110 cm gnome and 335 cm Ogre, and collision volume notes. Avoid copied franchise designs, excessive particles, unreadable clutter, text, watermarks, and photoreal micro-detail.

## Modeling Notes

- Build projector bodies as real geometry: base feet, coil housings, vane arms, core frames, shield emitters, and large bolts or clamps.
- Fake tiny rivets, gauge ticks, scratches, soot, and micro-gear detail in texture/normal maps.
- Keep VFX planes, Niagara systems, and collision volumes Blueprint-driven rather than baked into static mesh geometry.
- Use modular projector pieces so the Blueprint can assemble 3-unit, 5-unit, and curved-line variants.
- Maintain separate visual language from Ogre Teknomancy by using cleaner proportions and blue Aetherium logic.

## Texture And Material Notes

Texture targets:

- `T_GNM_AetherShieldProjector_A01_BC`
- `T_GNM_AetherShieldProjector_A01_N`
- `T_GNM_AetherShieldProjector_A01_ORM`
- `T_GNM_AetherShieldProjector_A01_E`
- `T_GNM_AetherShieldWall_A01_E`

Material instances:

- `MI_GNM_AetherShieldProjector_A01_Brass`
- `MI_GNM_AetherShieldProjector_A01_DarkIron`
- `MI_GNM_AetherShieldProjector_A01_AetheriumCore`
- `MI_GNM_AetherShieldWall_A01_Idle`
- `MI_GNM_AetherShieldWall_A01_Impact`
- `MI_GNM_AetherShieldWall_A01_Failing`

Runtime material parameters:

- `ImpactIntensity`
- `OverloadPercent`
- `ImpactLocationNormalized`

## Triangle Budget

- Projector static mesh LOD0: 3k-8k tris, 1-2 material slots.
- Full 3-projector shield-wall Blueprint visible LOD0: 9k-24k tris plus VFX.
- Full 5-projector hero variant: 15k-40k tris plus VFX.
- Keep VFX overdraw modest; shield should be readable but not a constant full-screen translucent wall.

## LOD Plan

- LOD0: full projector silhouettes, vane arms, core frames, major braces, shield anchor points.
- LOD1: 55-60 percent; reduce bevels, minor brackets, small coil supports.
- LOD2: 25-35 percent; simplify projector bodies and side vanes, reduce core frame geometry.
- LOD3: 10-15 percent; preserve squat projector silhouette, blue core read, and shield arc anchors.
- VFX LOD: reduce ripple count and impact sprite density at distance before removing the primary arc.

## Collision Notes

- Blueprint uses a simple shield gameplay volume only when mechanics require blocking or damage mitigation.
- Projector meshes use simple box/convex collision for world placement.
- Shield VFX should not block camera or player movement unless explicitly enabled by encounter logic.
- Small cables, coil handles, and indicator lights are non-blocking.

## Animation Notes

- Blueprint states: inactive, booting, braced, absorbing impact, overload warning, failing, shutdown.
- Projector animation may use small hinge rotation or emissive pulse only; avoid expensive moving part clusters.
- Impact VFX should pulse from the hit point to the nearest projector sockets.
- Audio hooks: boot hum, shield hum, impact thump, overload crackle, shutdown whine.

## Unreal Import Notes

- Asset type: Blueprint Actor with Static Mesh, Material Instance, Niagara/VFX, and collision dependencies.
- Blueprint path: `/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_HeavyMekShieldwall_A01`
- Projector mesh path: `/Game/Aerathea/Props/Gnomes/Mekgineer/SM_GNM_AetherShieldProjector_A01`
- VFX path: `/Game/Aerathea/VFX/GnomeOgre/VFX_GNM_AetherShieldWall_A01`
- Pivot: ground center of shield-wall arc.
- Required sockets on projector mesh: `vfx_core`, `vfx_shield_emit_l`, `vfx_shield_emit_r`, `attach_mek_l`, `attach_mek_r`, `damage_spark`.
- Blueprint variables: `ShieldState`, `ShieldWidthCm`, `ProjectorCount`, `ArcHeightCm`, `bBlocksProjectiles`, `bBlocksPawns`, `ImpactIntensity`, `OverloadPercent`, `ImpactLocationNormalized`, `ShieldIdleMaterial`, `ShieldImpactMaterial`, `ShieldFailingMaterial`.
- Blueprint functions: `SetShieldState`, `SetImpactIntensity`, `SetOverloadPercent`, `SetImpactLocationNormalized`, `TriggerImpact`, `ConfigureShieldwall`.
- Current native polish: state-driven material switching, scalar parameter propagation, and assignment to empty target `NS_GNM_AetherShieldWall_A01` are implemented; final Niagara emitter art-pass handoff is ready in `docs/assets/vfx/VFX_GNM_AetherShieldWall_A01/NIAGARA_ART_PASS_HANDOFF.md`.

## Folder And Naming Recommendation

- Package folder: `docs/assets/blueprints/BP_GNM_HeavyMekShieldwall_A01/`
- Implementation handoff: `docs/assets/blueprints/BP_GNM_HeavyMekShieldwall_A01/IMPLEMENTATION_HANDOFF.md`
- Source DCC: `SourceAssets/Blender/Kits/GnomeOgre/RivalryEncounter/BP_GNM_HeavyMekShieldwall_A01/`
- Export root: `SourceAssets/Exports/Kits/GnomeOgre/RivalryEncounter/BP_GNM_HeavyMekShieldwall_A01/`
- Unreal Blueprint: `/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_HeavyMekShieldwall_A01`

## Quality Gate Checklist

- Gnome/Mekgineer shield identity is readable without a full Mek body.
- Scale contrast supports 110 cm gnomes, heavy Mek frames, and 10-11 ft Ogres.
- Blue Aetherium shield language stays distinct from Ogre Teknomancy.
- Projector geometry is buildable as mid-poly Unreal content.
- VFX is restrained, state-driven, and not constant heavy overdraw.
- Collision, LODs, sockets, Blueprint variables, texture maps, and Unreal paths are defined.
- Native Blueprint/VFX contract exposes state materials, impact location, impact intensity, and overload parameters for final Niagara or material-driven effects.
