# KIT_DKH_FieldGear_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_DKH_FieldGear_A01`
- Asset type: Production kit / multi-asset field gear set
- Source concept: `Drakhar Arms Relics and Field Gear.png`
- Priority children: `SM_DKH_RiversindRecurve_A01`, `KIT_DKH_CurvedDaggers_A01`, `SM_DKH_ReedShellShield_A01`, `KIT_DKH_MagicTrackingCharms_A01`
- Status: Kit production package ready

Field gear for compact Drakhar relic hunters, rangers, rogues, shamans, and wizards. Use the approved A04 bearded-dragon/desert-lizardfolk anchor, females 3'6"-4'2" and males 4'0"-4'6", not the conflicting taller source-sheet scale.

## Gameplay Purpose

Supports exploration, stealth, ranged combat, ritual casting, relic gathering, magic detection, magic-item handling, and Volcreon-linked collector identity.

## Silhouette Notes

Riversind Recurve has a compact crescent recurve profile. Curved daggers read as hooked, crescent, or fang-like. ReedShell shield is light, layered, woven, and rounded. Tracking charms hang as readable bone, ember stone, cord, tooth, and relic clusters.

## Scale Notes

Approved Drakhar scale: females 3'6"-4'2" / 107-127 cm, males 4'0"-4'6" / 122-137 cm. Riversind Recurve: 90-125 cm. Daggers: 25-45 cm. ReedShell shield: 45-75 cm. Charms: 8-25 cm each. Grips and straps fit small clawed hands.

## Materials And Color Palette

Ochre and muted green scales, sun-bleached bone, dark cracked leather, reed, shell, terracotta, basalt, sandstone, dull brass, dark iron, and restrained orange-red ember glow for active relics.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a Drakhar field gear kit for Aerathea. Emphasize compact female 3'6"-4'2" and male 4'0"-4'6" lizardfolk scale, bearded-dragon and desert-lizard identity, recurve bow silhouettes, curved daggers, reed-shell shielding, bone and leather field craft, ember-lit magic tracking charms, relic gathering for Volcreon, and agile ranger/rogue/shaman/wizard gameplay roles. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive ember accents, and MMO-friendly production design. Present it as an armory and field-gear catalog sheet with corrected A04 scale callouts.

## Modeling Notes

Model bow limbs, grip wraps, dagger blades, shield body layers, shell plates, prominent bone pieces, charm stones, beads, and primary talismans as real geometry. Texture reed fibers, scale patterning, small etched markings, stitching, and relic inscriptions.

## Texture And Material Notes

Use `BC`, `N`, `ORM`, and optional `E` only for ember-lit relics or active magic tracking stones. Shared materials: `MI_DKH_ReedBoneLeather_A01`, `MI_DKH_RelicEmber_A01`, `MI_DKH_ScaleShell_A01`, `MI_DKH_SunbakedStone_A01`.

## Triangle Budget

Riversind Recurve: 2k-5k tris. Daggers: 800-2k each. ReedShell shield: 2k-5k. Charms: 500-1.5k each. Charm cluster: 2k-4k. Full field gear display: 8k-14k.

## LOD Plan

LOD0 full silhouette. LOD1 60-70 percent. LOD2 30-40 percent. LOD3 10-20 percent. Remove tiny markings, cords, underside details, secondary cuts, and minor beads before changing bow curve, dagger hook, shield outline, or charm mass.

## Collision Notes

Equipped bow/daggers use collision disabled by default. World weapons use simple box/capsule collision. ReedShell shield uses simple convex collision for pickup/display. Tracking charms use small pickup bounds or overlap sphere if interactive.

## Animation Notes

Static mesh baseline. Bow needs sockets for string alignment, arrow rest, charm attachment, and back carry. Daggers need hand/belt/boot sheath attachments. Tracking charms can later use material pulse and slight Blueprint/skeletal sway.

## Unreal Import Notes

Use centimeter scale and validate against A04 Drakhar female and male markers. Bow/dagger pivots at grip center; shield at forearm strap; charms at top loop. Sockets: `Grip_Main`, `Carry_Back`, `Charm_Attach_A`, `Charm_Attach_B`, `Arrow_Rest`, `Belt_Left`, `Belt_Right`, `Shield_Forearm`, `Relic_Activate`.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_DKH_FieldGear_A01/`
- Weapons: `/Game/Aerathea/Weapons/Drakhar/`
- Props: `/Game/Aerathea/Props/Drakhar/FieldGear/`
- Gear: `/Game/Aerathea/Characters/Drakhar/Gear/`
- Relic Blueprints: `/Game/Aerathea/Blueprints/Props/Drakhar/Relics/`

## Quality Gate Checklist

- Uses approved A04 Drakhar scale despite source conflict.
- Matches bearded-dragon/desert-lizardfolk anchor.
- Magic obsession, relic gathering, and Volcreon influence are clear.
- Ember glow is restrained.
- Budgets, LODs, collision, sockets, Blueprint notes, and Unreal paths are defined.
