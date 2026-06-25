# KIT_MIN_Arsenal_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_MIN_Arsenal_A01`
- Asset type: Production kit / multi-asset arsenal set
- Source concept: `Minotaur Arsenal.png`
- Priority children: `SM_MIN_GreatAxe_A01`, `SM_MIN_CrushingMaul_A01`, `KIT_MIN_HideShields_A01`, `KIT_MIN_Helmets_A01`
- Status: Kit production package ready

Oversized brutal practical weapons and defensive gear for 8-9 ft Minotaur plains warriors. Gear should feel heavy, direct, strength-respecting, and battlefield-repaired, using hide, bone, raw iron, fur, leather, rope, horn, and crude bindings.

## Gameplay Purpose

Supports Minotaur barbarians, berserkers, shamans, warriors, elite guards, enemy equipment, display props, loot items, and future character attachment rules.

## Silhouette Notes

Great axes use slab blades, long hafts, blunt hooks, and top-heavy mass. Mauls read as impact weapons first. Hide shields are wide, battered, asymmetrical, and strapped for large forearms. Helmets support horns without hiding the head silhouette.

## Scale Notes

Minotaur reference: 8-9 ft. Great axe: 220-300 cm. Crushing maul: 180-260 cm. Hide shields: 120-170 cm. Helmets include horn clearance, heavy brow guards, cheek plates, leather caps, and raw iron reinforcement.

## Materials And Color Palette

Dark raw iron, sweat-darkened leather, reddish brown hide, coarse fur, aged ivory bone, smoke-stained horn, rope/sinew, red ochre, charcoal, and bone-white paint. No emissive unless a rare anti-magic charm variant is approved.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a Minotaur arsenal kit for Aerathea. Emphasize massive practical silhouettes, raw iron weapon heads, hide shields, horn-compatible helmets, bone and fur accents, brutal lowland warrior culture, magic-resistant strength, and heavy melee gameplay roles. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, restrained material contrast, and MMO-friendly production design. Present it as an armory catalog concept sheet with 8-9 ft Minotaur scale callouts.

## Modeling Notes

Model primary weapon heads, hafts, shield bodies, helmet shells, large bone pieces, spikes, horn guards, raw iron bands, and thick grip wraps as real geometry. Texture small cracks, scratches, hide grain, pores, paint wear, stitching, and binding fibers.

## Texture And Material Notes

Use `BC`, `N`, and packed `ORM`. Shared material families: `MI_MIN_RawIron_A01`, `MI_MIN_HideLeather_A01`, `MI_MIN_BoneHorn_A01`, `MI_MIN_FurRope_A01`. Avoid emissive maps in the baseline kit.

## Triangle Budget

Large weapons: 3k-8k tris. Hero axe/maul: 6k-10k tris. Hide shields: 3k-7k each. Helmets: 2k-6k each. Display rack: 8k-16k tris.

## LOD Plan

LOD0 full silhouette. LOD1 60-70 percent. LOD2 30-40 percent. LOD3 10-20 percent. Remove tiny scratches, small straps, secondary cuts, backside detail, and minor ornaments before altering weapon mass or horn clearance.

## Collision Notes

Equipped weapons use collision disabled by default; combat traces handle hits. World weapons use simple capsules/boxes. Shields use simple convex collision for pickup/display. Helmets use preview bounds only.

## Animation Notes

Static mesh baseline. Weapons need future hand, back carry, rack display, and trace sockets. Shields need forearm/back sockets. Combat animation belongs to character sets.

## Unreal Import Notes

Use centimeter scale and validate against `AET_BOOT_MinotaurScale_270cm`. Weapon pivots at primary grip or display base; shields at forearm strap; helmets at head origin. Sockets: `Grip_Main`, `Grip_Off`, `Carry_Back`, `Trace_Start`, `Trace_End`, `Shield_Forearm`, `Display_Base`.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_MIN_Arsenal_A01/`
- Weapons: `/Game/Aerathea/Weapons/Minotaur/`
- Props: `/Game/Aerathea/Props/Minotaur/Arsenal/`
- Gear: `/Game/Aerathea/Characters/Minotaurs/Gear/`
- Materials: `/Game/Aerathea/Materials/Characters/Minotaur/`

## Quality Gate Checklist

- Matches approved 8-9 ft Minotaur anchor.
- Brutal, practical, simple, and heavy.
- Avoids refined craftsmanship and complex mechanisms.
- Uses hide, bone, raw iron, fur, leather, rope, and horn consistently.
- Budgets, LODs, collision, sockets, and Unreal paths are defined.
