# SM_DEL_VeilstriderBow_A01 Production Package

## Art Direction Summary

- Asset name: `SM_DEL_VeilstriderBow_A01`
- Asset type: Static Mesh bow
- Source: `Dark Elven Armory.png#Bow_Veilstrider`
- Parent kit: `KIT_DEL_Armory_A01`
- Status: Production package ready; DCC build not started

Original Dark Elven crescent bow with obsidian limbs, dark silver reinforcement, violet moonlit focus, and sleek spellbow identity.

## Gameplay Purpose

Ranged weapon for Dark Elven spellbows, rogues, sentinels, NPCs, and weapon socket testing.

## Silhouette Notes

Long crescent recurve, sharp but elegant limb tips, small central grip, and restrained negative space. Avoid spiky clutter.

## Scale Notes

135-160 cm tall. Fit tall Elven/Dark Elven proportions.

## Materials And Color Palette

Obsidian, dark silver, black leather, muted violet glow, moonlit blue-gray highlights.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_DEL_VeilstriderBow_A01` for the world of Aerathea. The design should emphasize a sleek crescent bow silhouette, obsidian limbs, dark silver reinforcement, black leather grip, violet lunar Aetherium focus, refined dangerous Dark Elven identity, moonlit stealth mood, and spellbow gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, strung/unstrung callouts, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model limbs, grip, nocks, central focus, and major dark-silver plates. Fake fine crescent lines and obsidian striations in maps.

## Texture And Material Notes

- `T_DEL_VeilstriderBow_A01_BC`
- `T_DEL_VeilstriderBow_A01_N`
- `T_DEL_VeilstriderBow_A01_ORM`
- `T_DEL_VeilstriderBow_A01_E` for violet focus only

## Triangle Budget

LOD0 3k-7k tris, 1 material slot.

## LOD Plan

LOD0 full crescent limbs; LOD1 removes small plates; LOD2 simplifies nocks and focus; LOD3 preserves arc and grip.

## Collision Notes

Equipped collision disabled. Display collision uses simple long box/capsule.

## Animation Notes

Static mesh baseline. Draw/string behavior waits for combat animation systems.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Weapons/DarkElven/SM_DEL_VeilstriderBow_A01`
- Pivot: hand grip center.
- Scale: centimeters.
- Sockets: `socket_arrow_rest`, `socket_string_top`, `socket_string_bottom`, optional `socket_violet_focus`.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_DEL_VeilstriderBow_A01/`
- Source: `SourceAssets/Blender/Kits/DarkElven/Armory/SM_DEL_VeilstriderBow_A01/`
- Export: `SourceAssets/Exports/Kits/DarkElven/Armory/SM_DEL_VeilstriderBow_A01/`
- Unreal: `/Game/Aerathea/Weapons/DarkElven/SM_DEL_VeilstriderBow_A01`

## Quality Gate Checklist

- Crescent bow silhouette is readable.
- Dark Elven material language is consistent.
- Glow is localized.
- Bow sockets are specified.
- LODs preserve the main arc.
