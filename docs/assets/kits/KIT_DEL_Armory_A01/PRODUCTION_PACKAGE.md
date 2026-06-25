# KIT_DEL_Armory_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_DEL_Armory_A01`
- Asset type: Production kit / multi-asset armory set
- Source concept: `Dark Elven Armory.png`
- Priority children: `SM_DEL_DuskspiteBlade_A01`, `SM_DEL_VeilstriderBow_A01`, `SM_DEL_AegisOfEternalDusk_A01`, `MI_DEL_ShadowArmory_Set_A01`
- Status: Kit production package ready

Elegant shadowed Dark Elven armory language for moonlit weapons, shields, accessories, and shared materials. Designs should feel refined, dangerous, oath-bound, and original to Aerathea.

## Gameplay Purpose

Supports Dark Elf shadowblades, spellbows, sentinels, priestesses, rogues, arcane defenders, loot models, inventory sources, display props, and reusable material language.

## Silhouette Notes

Use long crescent arcs, narrow points, swept guards, moon-disc shields, veil-like negative space, and elegant asymmetry. Avoid bulky savage shapes, generic black spikes, and unreadable micro-ornament.

## Scale Notes

Scale for tall graceful humanoids. Blades: 85-110 cm. Bows: 150-175 cm. Shields: 65-85 cm. Small jewelry and focus props must remain readable in inventory preview.

## Materials And Color Palette

Dark silver, obsidian steel, star-iron, shadow leather, void silk, moonbone, lunar crystal, and restrained violet Aetherium glow. Palette: charcoal, cold silver, deep violet, moon white, and small luminous accents.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a Dark Elven armory kit for Aerathea. Emphasize elegant crescent weapon silhouettes, dark silver and obsidian materials, violet lunar glow accents, refined oath-bound Dark Elven identity, moonlit danger, and combat roles for shadowblades, spellbows, and sentinels. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as an armory catalog asset board featuring Duskspite blade, Veilstrider bow, Aegis of Eternal Dusk shield, and Shadow Armory material swatches.

## Modeling Notes

Model primary blades, bow limbs, shield body, guards, grips, large gems, crescent plates, and major sockets as real geometry. Texture fine filigree, tiny runes, scratches, leather grain, cloth weave, and oath marks.

## Texture And Material Notes

Use `BC`, `N`, `ORM`, and optional `E`. Shared material families: `MI_DEL_ShadowArmory_Set_A01`, `MI_DEL_ObsidianSteel_A01`, `MI_DEL_ShadowLeather_A01`, `MI_DEL_VoidSilk_A01`, `MI_DEL_LunarCrystal_A01`.

## Triangle Budget

Accessories: 500-2k tris. Blades: 1.5k-4k tris. Veilstrider bow: 3k-7k tris. Aegis shield: 3k-8k tris. Armor modules or cloaks: 2k-8k per piece. Full display cluster under 35k tris.

## LOD Plan

LOD0-LOD3 for important meshes. LOD1 60-70 percent. LOD2 35-45 percent. LOD3 15-25 percent. Remove tiny etching, underside detail, small hanging ornaments, and minor gem cuts before changing crescents, bow curve, or shield outline.

## Collision Notes

Equipped weapons and shields use attachment collision disabled by default. World pickups use simple capsule or box bounds. Display props use simple custom collision. Avoid complex-as-simple for runtime equipment.

## Animation Notes

Static mesh baseline. Bows need later string/socket support. Cloaks wait for cloth or skeletal attachment direction. Emissive materials may use subtle idle pulse parameters.

## Unreal Import Notes

Use centimeter scale. Weapon pivots at grip center, shield at hand mount, display props at base/center. Sockets: `Socket_Grip_R`, `Socket_Grip_L`, `Socket_Back`, `Socket_Shield`, `Socket_Gem`.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_DEL_Armory_A01/`
- Weapons: `/Game/Aerathea/Weapons/DarkElven/`
- Props: `/Game/Aerathea/Props/DarkElven/Armory/`
- Gear: `/Game/Aerathea/Characters/DarkElves/Gear/`
- Materials: `/Game/Aerathea/Materials/DarkElven/Armory/`

## Quality Gate Checklist

- Original Aerathea Dark Elven identity.
- Elegant, shadowed, moonlit, oath-bound anchor is clear.
- Duskspite, Veilstrider, Aegis, and material set are represented.
- Silhouettes read at MMO camera distance.
- Glow is restrained and purposeful.
- Budgets, LODs, collision, sockets, and texture maps are defined.
