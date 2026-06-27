# NS_CRE_Manticore_Impact_A01 Production Package

## 1. Art Direction Summary

`NS_CRE_Manticore_Impact_A01` is the Manticore interrupt impact effect for the Gnome-vs-Ogre encounter. It should read as a sudden predator landing: dust, claw impact, wing buffet, and a small venom-green sting accent without turning the creature into a magical caster.

Current status: template-derived first-pass Niagara system and emitter target exist in Unreal and are assigned to `BP_CRE_ManticoreInterrupt_A01`. Bespoke emitter graph polish remains pending.

## 2. Gameplay Purpose

The effect signals the Manticore interrupt moment: the creature lands, breaks player attention, and creates a short danger beat. It supports Telegraph, LeapImpact, ThreatHold, and Retreat states.

## 3. Silhouette Notes

- Primary read: low ground impact burst at the landing point.
- Secondary read: outward dust ring and wing-buffet streaks.
- Tertiary read: short venom-green glint near the stinger or impact focus.
- Avoid large magical circles, constant glow, or effects that hide the Manticore body.

## 4. Scale Notes

- VFX attaches to `BP_CRE_ManticoreInterrupt_A01`.
- Impact should fit under and around the Manticore feet/claws.
- Dust should stay inside the encounter interrupt area.

## 5. Materials and Color Palette

- Packed-earth tan and muted gray dust.
- Bone/claw off-white flecks sparingly.
- Venom green accent only at the sting/impact highlight.
- No blue Aetherium and no Ogre forge-orange as the primary read.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG VFX concept sheet of `NS_CRE_Manticore_Impact_A01` for the world of Aerathea. The design should emphasize a sudden Manticore leap impact, ground dust burst, claw gouge streaks, wing-buffet motion, short venom-green sting accent, predator interruption timing, and MMO-readable combat telegraphing. Use readable shapes, hand-painted texture language, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and production-friendly VFX density. Present it as a VFX state board with telegraph, leap impact, threat hold, and retreat frames plus socket and impact locator callouts. Avoid copied franchise designs, large spell circles, excessive particle storms, and effects that hide the creature silhouette.

## 7. Modeling Notes

No new mesh is required for the first VFX pass. Use `ImpactMarker` from `AAETManticoreInterruptActor` and future skeletal sockets from `SK_CRE_Manticore_Interrupt_A01` for claw/stinger polish.

## 8. Texture and Material Notes

- Use soft dust sprites and short-lived streaks.
- Suggested future textures: `T_CRE_Manticore_Impact_Dust_A01`, `T_CRE_Manticore_Impact_ClawStreak_A01`, `T_CRE_Manticore_Impact_VenomSpark_A01`.
- Keep translucent overdraw low and lifetimes short.
- No dynamic lights by default.

## 9. Triangle Budget

Niagara sprite/ribbon effect only. Mesh particles are not planned for the first polished pass. If debris mesh particles are added later, keep them under 300 tris total near-camera.

## 10. LOD Plan

- LOD0: dust burst, wing-buffet streaks, claw gouges, venom spark.
- LOD1: dust burst, reduced streaks, venom spark.
- LOD2: dust puff only.
- LOD3: cull Niagara; rely on animation silhouette.

## 11. Collision Notes

No VFX collision. Gameplay hit traces and trigger volumes remain separate from the Niagara system.

## 12. Animation Notes

Driven by interrupt state and sequence parameters:

- `User.InterruptState`
- `User.SequenceProgress`
- `User.bImpact`
- `User.ImpactColor`

## 13. Unreal Import Notes

- Asset type: Niagara System.
- System path: `/Game/Aerathea/VFX/Creatures/NS_CRE_Manticore_Impact_A01`
- Emitter target: `/Game/Aerathea/VFX/Creatures/NE_CRE_Manticore_Impact_A01`
- Native consumer: `AAETManticoreInterruptActor`
- Blueprint consumer: `/Game/Aerathea/Blueprints/Creatures/BP_CRE_ManticoreInterrupt_A01`
- Component: `ImpactNiagara`
- Validation: `Tools/Unreal/validate_startup_scene.py`

## 14. Folder and Naming Recommendation

- Package folder: `docs/assets/vfx/NS_CRE_Manticore_Impact_A01/`
- Unreal folder: `/Game/Aerathea/VFX/Creatures/`
- System: `NS_CRE_Manticore_Impact_A01`
- Emitter: `NE_CRE_Manticore_Impact_A01`

## 15. Quality Gate Checklist

- Reads as Manticore impact, not a mage spell.
- Impact state is clear at gameplay camera distance.
- Uses the native interrupt `User.*` contract.
- Does not hide the Manticore silhouette.
- Keeps venom green as an accent only.
- Has distance scalability and culling behavior.
- Avoids dynamic lights and heavy overdraw.
- Startup validation passes before visual approval.
