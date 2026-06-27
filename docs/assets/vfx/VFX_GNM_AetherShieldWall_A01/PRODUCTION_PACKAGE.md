# VFX_GNM_AetherShieldWall_A01 Production Package

## Art Direction Summary

`VFX_GNM_AetherShieldWall_A01` defines the Gnome/Mekgineer Aether shield-wall effect for the Gnome-vs-Ogre rivalry kit. The current review implementation uses static helper panels and material-state instances. The final authored Niagara art pass should replace or supplement the helper panels with a clean, blue, segmented, defensive, and precise effect that contrasts clearly against Ogre forge-orange and necromantic green effects.

Current status: first-pass helper/VFX contract implemented; final authored Niagara art-pass handoff ready; empty Unreal Niagara target `NS_GNM_AetherShieldWall_A01` exists; final emitter art pass pending.

## Gameplay Purpose

- Provides the visual shield field used by `BP_GNM_HeavyMekShieldwall_A01`.
- Supports idle/braced, impact, overload, failing, and shutdown states.
- Gives encounter designers a readable defensive volume before final heavy Mek animation exists.

## Silhouette Notes

- Shield should read as connected crescent segments, not a flat full-screen wall.
- Blue edge bands and lower/mid pulse lines should remain readable from MMO camera distance.
- Impact feedback should localize near the hit point and nearest projector.

## Scale Notes

- Default review width: 700 cm across a three-projector wall.
- Default arc height: 340 cm.
- Must defend Gnome heavy Mek frames while allowing 10-11 ft Ogres to remain readable above or behind the field.

## Materials And Color Palette

- Blue, cyan, and blue-white Aetherium glow.
- Slight transparent blue body fill.
- No forge orange, no necromantic green, no heavy white bloom.

## Concept Image Prompt

Create an original stylized fantasy MMORPG VFX state sheet of `VFX_GNM_AetherShieldWall_A01` for the world of Aerathea. The design should emphasize precise Gnome/Mekgineer blue Aetherium shield arcs, segmented crescent wall geometry, restrained transparent blue fill, bright edge bands, localized impact ripples, overload flicker, failing broken segments, and readable defensive gameplay states. Use hand-painted texture detail, clean MMO-readable shapes, sparing emissive accents, and production-friendly VFX density. Present it as a clean VFX board with inactive, booting, braced, impact, overload, failing, and shutdown frames plus projector socket callouts. Avoid copied franchise designs, excessive particles, full-screen bloom, unreadable clutter, text, and watermarks.

## Modeling Notes

- First-pass review uses `SM_GNM_AetherShieldWall_A01` as a low-poly helper mesh with segmented panes, edge rails, pulse lanes, projector nodes, impact focus, and failure-crack accents.
- Final VFX should move to Niagara or equivalent VFX assets while keeping the helper mesh as optional LOD support.
- VFX attaches to projector sockets and Blueprint state.
- The native shieldwall actor now provides the VFX contract: `ShieldState`, `ImpactIntensity`, `OverloadPercent`, `ImpactLocationNormalized`, `ImpactLocator`, and idle/impact/failing material bindings.
- Final Niagara requires an implementation hook because `AAETHeavyMekShieldwallActor` currently pushes scalar parameters to materials and positions `ImpactLocator`, but does not own a Niagara component.

## Texture And Material Notes

- `T_GNM_AetherShieldWall_A01_E`
- Optional ripple/edge mask texture for final art.
- Review material: `M_GNM_AetherShieldWall_Review_A01`
- State instances: `MI_GNM_AetherShieldWall_A01_Idle`, `MI_GNM_AetherShieldWall_A01_Impact`, `MI_GNM_AetherShieldWall_A01_Failing`
- Runtime scalar parameters: `ImpactIntensity`, `OverloadPercent`, `ImpactLocationNormalized`

Final Niagara assets:

- `NS_GNM_AetherShieldWall_A01`
- `NE_GNM_ShieldEdgeBands_A01`
- `NE_GNM_ShieldSurfacePulse_A01`
- `NE_GNM_ShieldImpactRipple_A01`
- `NE_GNM_ShieldOverloadSparks_A01`
- `NE_GNM_ShieldFailingFragments_A01`

Niagara user parameters:

- `User.ShieldState`
- `User.ShieldWidthCm`
- `User.ArcHeightCm`
- `User.ProjectorCount`
- `User.ImpactIntensity`
- `User.OverloadPercent`
- `User.ImpactLocationNormalized`
- `User.ImpactWorldLocation`
- `User.EdgeColor`
- `User.FillColor`
- `User.bFailing`

## Triangle Budget

- Helper mesh: under 500 tris for the full first-pass review helper; final particle/ribbon implementation should stay cheaper at distance.
- Final VFX should keep overdraw modest and reduce ripple density at distance.

## LOD Plan

- LOD0: full segmented shield surface, edge bands, pulse lines, impact focus.
- LOD1: reduce pulse lines and ripple density.
- LOD2: keep edge bands and broad transparent fill only.
- LOD3: disable particles and preserve minimal core/edge glow on projectors.
- Niagara scalability: cap active particles and ribbons by distance, disable overload sparks first, disable surface fill second, keep edge bands last.

## Collision Notes

- VFX has no collision by default.
- Gameplay blocking belongs to `BP_GNM_HeavyMekShieldwall_A01` and its `ShieldCollision` component.

## Animation Notes

- `Inactive`: panels hidden, cores dark.
- `Booting`: core brightens and arc connects.
- `Braced`: low-frequency stable pulse.
- `Impact`: localized ripple from hit point.
- `Overload`: stronger edge flicker.
- `Failing`: broken shield segment visibility and pulse loss.
- `Shutdown`: collapse toward projectors.

## Unreal Import Notes

- VFX placeholder asset: `/Game/Aerathea/VFX/GnomeOgre/VFX_GNM_AetherShieldWall_A01`
- Final Niagara system target: `/Game/Aerathea/VFX/GnomeOgre/NS_GNM_AetherShieldWall_A01`
- Helper mesh: `/Game/Aerathea/VFX/GnomeOgre/SM_GNM_AetherShieldWall_A01`
- Material: `/Game/Aerathea/Materials/M_GNM_AetherShieldWall_Review_A01`
- Blueprint consumer: `/Game/Aerathea/Blueprints/GnomeOgre/BP_GNM_HeavyMekShieldwall_A01`
- Native handoff: `AAETHeavyMekShieldwallActor` controls state materials, impact location, and scalar parameters until authored Niagara replaces or supplements the helper mesh.

## Folder And Naming Recommendation

- Package folder: `docs/assets/vfx/VFX_GNM_AetherShieldWall_A01/`
- Unreal VFX folder: `/Game/Aerathea/VFX/GnomeOgre/`
- Niagara art-pass handoff: `docs/assets/vfx/VFX_GNM_AetherShieldWall_A01/NIAGARA_ART_PASS_HANDOFF.md`
- Build/import status: `docs/assets/vfx/VFX_GNM_AetherShieldWall_A01/BUILD_IMPORT_STATUS.md`
- Material instances: `/Game/Aerathea/Materials/Instances/MI_GNM_AetherShieldWall_A01_*`

## Quality Gate Checklist

- Gnome blue Aetherium shield language is readable.
- VFX does not overwhelm silhouettes or camera.
- State names match the Blueprint handoff.
- Helper mesh, materials, LOD behavior, collision ownership, and Unreal paths are defined.
- Final Niagara consumes the existing native state and parameter contract instead of duplicating gameplay state.
- Final Niagara asset is not marked complete until `NS_GNM_AetherShieldWall_A01` exists in Unreal and is bound to the shieldwall actor or Blueprint.
