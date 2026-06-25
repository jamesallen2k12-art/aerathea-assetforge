# KIT_DWR_Armory_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_DWR_Armory_A01`
- Asset type: Production kit / multi-asset armory set
- Source concept: `Dwarven Armory.png`
- Priority children: `SM_DWR_OathkeeperHammer_A01`, `SM_DWR_StonewallShield_A01`, `SK_DWR_Helm_Stonebound_A01`, `MI_DWR_RunicGlowStates_A01`
- Status: Kit production package ready

Broad mountain-forged Dwarven guardian gear built around oath, endurance, stone craft, and blue runic defense. Forms should feel dense, practical, ceremonial, and original to Aerathea.

## Gameplay Purpose

Supports Dwarven warriors, runesmiths, guardians, NPC armories, loot previews, display props, and future shield/hammer socket testing.

## Silhouette Notes

Use squat powerful proportions, thick bevels, large stone-and-steel masses, heavy brows, compact shields, and clear rune plates. Preserve the hammer head, shield slab, and helm brow as the main read.

## Scale Notes

Hammer length: 105-120 cm. Shield height: 85-100 cm. Helm sized for broad dwarf heads with male beard clearance and female non-bearded variants. Author in centimeters.

## Materials And Color Palette

Dark forged steel, slate stone, aged brass, worn brown leather, muted fur, and sparing blue Aetherium rune glow. Palette stays grounded in charcoal, iron gray, stone blue, brass gold, and leather brown.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a Dwarven guardian armory kit for Aerathea. Emphasize broad mountain-forged silhouettes, dark steel, slate stone, aged brass, leather, fur padding, blue runic Aetherium glow, Dwarven runesmith identity, solemn guardian mood, and tank-focused gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as an armory catalog asset board with Oathkeeper hammer, Stonewall shield, Stonebound helm, and rune glow state strip.

## Modeling Notes

Model hammer head, haft, shield slab, shield rim, helm plates, cheek guards, and large rune insets as real geometry. Texture fine rune etching, stone grain, leather stitching, hammer marks, and scratches.

## Texture And Material Notes

Use shared Dwarf armory material instances where practical. Required maps: `BC`, `N`, `ORM`, and `E` for rune-bearing items. Use masks for dormant, awakened, oathbound, ancestral, and disabled rune states.

## Triangle Budget

Hammer LOD0: 4k-6k tris. Shield LOD0: 3k-5k tris. Helm LOD0: 3k-5k tris. Full kit display target: under 18k tris visible at once.

## LOD Plan

LOD0 full silhouette and large bevels. LOD1 60-70 percent. LOD2 35-45 percent. LOD3 15-25 percent. Remove small straps, small cuts, inner helm forms, shield back detail, and minor rune bevels before changing the primary silhouette.

## Collision Notes

Equipped items use no blocking collision by default. World pickups and display props use simple convex collision. Hammer collision can separate handle and head only for physics pickup.

## Animation Notes

Static meshes baseline. Rune state changes are material or Blueprint parameters. Optional future effects: hammer rune flare, shield block flash, helm rune glint.

## Unreal Import Notes

Use centimeter scale. Hammer pivot at grip center; shield at forearm mount; helm at head attachment origin. Sockets: `Grip_R`, `Grip_L`, `Shield_Forearm`, `Rune_Core`, `Display_Mount`.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_DWR_Armory_A01/`
- Unreal weapons: `/Game/Aerathea/Weapons/Dwarven/`
- Unreal props: `/Game/Aerathea/Props/Dwarven/Armory/`
- Unreal gear: `/Game/Aerathea/Characters/Dwarves/Gear/`
- Materials: `/Game/Aerathea/Materials/Dwarven/Armory/`

## Quality Gate Checklist

- Original Aerathea Dwarven identity.
- Broad, dense, mountain-forged silhouette.
- Stone, steel, brass, leather, fur, and blue runes match the Dwarven anchor.
- Priority children and rune states are named.
- Texture maps, LODs, collision, sockets, and Unreal paths are defined.
- Glow is functional and restrained.
