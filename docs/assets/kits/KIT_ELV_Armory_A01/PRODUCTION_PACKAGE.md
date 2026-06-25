# KIT_ELV_Armory_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_ELV_Armory_A01`
- Asset type: Production kit / multi-asset armory set
- Source concept: `Elven Armory.png`
- Priority children: `SM_ELV_Moonblade_A01`, `SM_ELV_SilverleafRecurve_A01`, `SM_ELV_MoonwardBuckler_A01`, `SM_ELV_AetheriumLantern_A01`
- Status: Kit production package ready

Graceful ancient Elven armory kit built around moonlight, living craft, silverleaf, and refined magical utility. Forms should feel elegant and celestial without becoming fragile or over-decorated.

## Gameplay Purpose

Supports Elven rangers, wardens, runesingers, sentinels, quest rewards, settlement props, inventory icons, and future weapon/light socket testing.

## Silhouette Notes

Use long arcs, crescent shapes, leaf-like negative space, refined tapering forms, and clear moonstone focal points. Preserve the bow curve, Moonblade crescent edge, buckler outline, and lantern frame.

## Scale Notes

Moonblade length: 90-105 cm. Recurve bow height: 145-165 cm. Buckler diameter: 35-45 cm. Lantern height: 35-50 cm. Author to tall graceful Elven proportions in centimeters.

## Materials And Color Palette

Polished silver, moonstone, pale silverleaf, living whitewood, soft blue-white Aetherium, muted midnight-blue wraps, pearl highlights, and desaturated green leaf tones.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of an Elven moon-warden armory kit for Aerathea. Emphasize graceful crescent silhouettes, polished silver, moonstone, silverleaf, living whitewood, blue-white Aetherium glow, ancient nature-and-star culture, serene moonlit mood, and agile ranger/warden gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as an armory catalog asset board with Moonblade, Silverleaf Recurve bow, Moonward buckler, and Aetherium lantern.

## Modeling Notes

Model blade, guard, bow limbs, buckler rim, lantern frame, handle, and moonstone/Aetherium cores as real geometry. Texture fine leaf veins, star etching, wood grain, silver filigree, and cloth weave.

## Texture And Material Notes

Required maps: `BC`, `N`, `ORM`, and `E` for lantern core, blade runes, bow inlays, and buckler moon mark. Use shared silver, living wood, moonstone, and blue-white Aetherium material instances.

## Triangle Budget

Moonblade LOD0: 2.5k-4k tris. Bow LOD0: 3.5k-6k tris. Buckler LOD0: 2k-3.5k tris. Lantern LOD0: 3k-5k tris. Full display under 18k tris.

## LOD Plan

LOD0 full curves and frames. LOD1 60-70 percent. LOD2 35-45 percent. LOD3 15-25 percent. Remove secondary leaf cuts, inner lantern supports, buckler back detail, and small filigree before reducing the main arcs.

## Collision Notes

Equipped items use minimal attachment collision. Pickup/display versions use simple convex hulls. Lantern collision should be a capsule or box around the frame, not separate small bars.

## Animation Notes

Static mesh baseline. Bow may need future string/socket support. Lantern can use Blueprint-driven soft glow and optional low-radius light disabled by default.

## Unreal Import Notes

Use centimeter scale. Pivots at hand grip for blade/bow, forearm center for buckler, handle top or base center for lantern. Sockets: `Grip_R`, `Grip_L`, `Arrow_Nock`, `Buckler_Forearm`, `Lantern_Handle`, `Aetherium_Core`.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_ELV_Armory_A01/`
- Unreal weapons: `/Game/Aerathea/Weapons/Elven/`
- Unreal props: `/Game/Aerathea/Props/Elven/Armory/`
- Unreal gear: `/Game/Aerathea/Characters/Elves/Gear/`
- Materials: `/Game/Aerathea/Materials/Elven/Armory/`

## Quality Gate Checklist

- Original Aerathea Elven identity.
- Moon, star, leaf, silver, and living-wood language reads clearly.
- Priority children are named and production-ready for child packages.
- Fine decoration stays in texture/normal maps.
- Texture maps, LODs, collision, sockets, and Unreal paths are defined.
- Glow is soft, useful, and restrained.
