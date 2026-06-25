# KIT_ORC_Arsenal_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_ORC_Arsenal_A01`
- Asset type: Production kit / multi-asset arsenal set
- Source concept: `Orc Arsenal.png`
- Priority children: `SM_ORC_GreatAxe_A01`, `KIT_ORC_Shields_A01`, `KIT_ORC_ShamanicTalismans_A01`, `MI_ORC_RunicAffinities_A01`
- Status: Kit production package ready

Noble upright Orc arsenal language for powerful clan warriors, rangers, wardens, and shamanic defenders. Designs should feel honorable, disciplined, spiritual, and battle-ready without reducing Orcs to savage caricature.

## Gameplay Purpose

Supports Orc warriors, rangers, shamans, mages, clan champions, loot models, armory dressing, crafting references, runic material variants, and socket standards.

## Silhouette Notes

Use disciplined weight: broad axe heads, thick hafts, slab shields, layered leather, clan-bound charms, feather and bone accents, rune-cut metal plates. Shields are ceremonial and protective, not crude.

## Scale Notes

Scale for large powerful upright humanoids around 220-230 cm where needed. Great axes: 150-190 cm. Heavy blades: 110-145 cm. Shields: 85-120 cm. Talismans: 10-35 cm.

## Materials And Color Palette

Raw and worked iron, dark steel, bronze, aged copper, carved bone, horn, leather, fur, woven cords, spirit stone, muted clan cloth, and restrained blue-green rune glow.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of an Orc arsenal kit for Aerathea. Emphasize broad disciplined weapon silhouettes, iron, bronze, bone, leather, fur, spirit-stone materials, muted clan colors, blue-green rune accents, noble upright Orc identity, honorable shamanic spirituality, and gameplay roles for warriors, wardens, rangers, and shamans. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as an arsenal catalog board featuring GreatAxe A01, shield variants, shamanic talismans, and runic affinity material swatches.

## Modeling Notes

Model axe heads, shield plates, hafts, grips, large rivets, bone charms, totem forms, major rune stones, feathers, and horn pieces as real geometry. Texture fine scratches, leather pores, woven fiber, small rune cuts, stitching, hammered metal grain, and tiny bindings.

## Texture And Material Notes

Use `BC`, `N`, `ORM`, and optional `E`. Shared materials: `MI_ORC_ArsenalMaterials_A01`, `MI_ORC_RunicAffinities_A01`, `MI_ORC_WorkedIron_A01`, `MI_ORC_ClanLeather_A01`, `MI_ORC_SpiritStone_A01`. Affinities cover strength, protection, ancestry, spirit, and balance.

## Triangle Budget

Talismans: 500-2k tris. Great axes/heavy blades: 2k-6k tris. Shields: 3k-8k tris. Totems/foci: 1.5k-5k tris. Armor modules: 3k-8k per piece. Full arsenal display under 40k tris.

## LOD Plan

LOD0-LOD3 for important meshes. LOD1 60-70 percent. LOD2 35-45 percent. LOD3 15-25 percent. Remove small bindings, feather cuts, minor chips, inner shield detail, and small charms before changing axe mass, shield outline, or talisman silhouette.

## Collision Notes

Equipped weapons and shields use attachment collision disabled by default. World pickups use simple capsule or box bounds. Display shields use convex hulls. Totems use simple cylinder or box collision when world-placed.

## Animation Notes

Static mesh baseline. Great axes, shields, and talismans need socket alignment. Talismans may use later secondary motion through character attachments. Runic affinities use material parameters.

## Unreal Import Notes

Use centimeter scale. Weapon pivots at grip center. Shields pivot at hand strap or forearm mount. Talismans pivot at attachment loop. Sockets: `Socket_Grip_R`, `Socket_Grip_L`, `Socket_Back`, `Socket_Shield`, `Socket_BeltCharm`, `Socket_NeckCharm`, `Socket_Totem`.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_ORC_Arsenal_A01/`
- Weapons: `/Game/Aerathea/Weapons/Orc/`
- Props: `/Game/Aerathea/Props/Orc/Arsenal/`
- Gear: `/Game/Aerathea/Characters/Orcs/Gear/`
- Materials: `/Game/Aerathea/Materials/Orc/Arsenal/`

## Quality Gate Checklist

- Original Aerathea Orc identity.
- Noble, upright, powerful, honorable clan culture is clear.
- GreatAxe, shields, talismans, and runic affinities are represented.
- Avoids savage caricature and copied franchise language.
- Budgets, LODs, collision, sockets, and texture maps are defined.
- Glow is restrained and spiritual.
