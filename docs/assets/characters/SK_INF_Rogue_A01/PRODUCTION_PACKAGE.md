# SK_INF_Rogue_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SK_INF_Rogue_A01`
- Asset type: Skeletal Mesh class outfit / Infernal stealth class package
- Parent body: `SK_INF_Base_A01`
- World: Aerathea
- Theme: winged predator, invisible-sight ambusher, claw-and-tail assassin
- Primary references: `SK_INF_Base_A01`, `ANIMATION_HANDOFF.md`, `INFERNAL_VISUAL_CLEANSE_STANDARD.md`, `InfernalMaleLit.png`, `InfernalFemaleLit2.png`, Lesser Infernal action references
- Current status: production package and modeling handoff ready; DCC build not started

Infernal Rogues do not need daggers to feel dangerous. Their stealth identity comes from folded wings, low predatory posture, black claws, tail counterbalance, see-invisible focus, sudden pounce, short aerial repositioning, and tight brand glow. Gear should be close-fit and quiet: ash-black wraps, obsidian plates, minimal bone trophies, claw guards, wing straps, and tail-root armor.

## 2. Gameplay Purpose

- Supports Infernal rogue player/NPC identity.
- Provides stealth, ambush, scouting, assassination, and anti-stealth reads.
- Establishes animation hooks for stalk, crouch, pounce, rake, wing-assisted reposition, invisible-sight reveal, and vanish/reappear VFX.
- Creates a contrast against the heavier Warrior and brighter Mage class packages.

## 3. Silhouette Notes

- Primary read: compact folded wings, low stalking posture, swept horns, long tail counterbalance, open black claws, close-fit wraps.
- Best first body target: Compact and Standard bands, with Greater assassin variants later.
- Keep armor minimal and shape-driven; do not bury the body in cloth.
- Use small but readable skull/bone marks, not trophy clutter.
- Tail should actively balance crouch and leap poses.

## 4. Scale Notes

- Adult canon range: 5'0"-9'0" / 152-274 cm.
- First class-fit targets: Compact 152-173 cm and Standard 173-203 cm.
- Wings must fold tighter than Warrior/Mage defaults.
- Crouch height, wing clearance, and tail length must be tested for navigation readability.

## 5. Materials And Color Palette

| Family | Palette | Use |
| --- | --- | --- |
| Skin | ember red, ash red, muted crimson | exposed face, arms, legs, tail |
| Wraps | ash black, soot gray, burnt red | stealth cloth, bindings, thigh/forearm wraps |
| Armor | obsidian, blackened iron, dark leather | light plates, claw guards, shin guards |
| Bone/horn | smoke tan, aged ivory, black keratin | small hierarchy marks, horn trims |
| Glow | dim ember, deep red, focused violet | eyes, see-invisible, brief ambush marks |

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_INF_Rogue_A01`, an Infernal Rogue for Aerathea. Emphasize a mortal-descended demonic ambusher with compact folded leathery wings, red skin, black claws, required swept horns, long thick tail used for balance, low stalking posture, close-fit ash-black wraps, obsidian light armor, small skull/bone villain marks, focused violet-red invisible-sight eye glow, and natural-weapon stealth combat through claws, pounce, tail, and wing-assisted repositioning instead of mortal daggers. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, focused emissive accents, and MMO-friendly production design. Present front, side, back, crouch, pounce, claw-rake, wing-fold, tail-balance, material swatches, socket callouts, and scale beside Compact/Standard Infernal bands. Apply A03 cleanup: preserve glowing eyes, menace, skull/bone cues, and threat while reducing tiny rivets, speckle artifacts, malformed micro-spikes, broken micro-chains, and noisy texture fragments. Avoid copied franchise designs, gore, readable text, watermarks, daggers, swords, or weapon-dependent silhouettes.

## 7. Modeling Notes

- Build modular rogue gear over `SK_INF_Base_A01`.
- Model real geometry for close-fit plates, claw guards, shin guards, wing strap anchors, tail-root guard, hood/collar if used, and major wraps.
- Keep wings folded and readable; do not hide wing roots under cloth.
- Use texture/normal maps for cloth weave, small stitches, scratches, scar lines, tiny brands, and small bone wear.
- Avoid dangling cloth strips that interfere with crouch, pounce, and tail motion.

## 8. Texture And Material Notes

Texture maps:

- `T_INF_Rogue_A01_BC`
- `T_INF_Rogue_A01_N`
- `T_INF_Rogue_A01_ORM`
- `T_INF_Rogue_A01_E`

Material slots:

1. Base Infernal skin/body inherited from `SK_INF_Base_A01`
2. `MI_INF_Rogue_A01_Wraps`
3. `MI_INF_Rogue_A01_LightArmor`
4. `MI_INF_Rogue_A01_BoneHorn`
5. Optional `MI_INF_Rogue_A01_SightGlow`

## 9. Triangle Budget

- Class gear LOD0 target: 8k-18k tris.
- Full equipped character with base body: 36k-54k tris.
- Material slot target: 3-5.

## 10. LOD Plan

- LOD0: full body, wraps, light plates, claw guards, wing straps, tail-root guard, socket markers.
- LOD1: reduce wrap bevels, small plate cuts, tiny bone marks.
- LOD2: merge wrap clusters, simplify collar/hood if used, reduce strap geometry.
- LOD3: preserve folded wings, tail line, claw hands, swept horns, dark wrap blocks, and eye/brand glow.

## 11. Collision Notes

- Use base Infernal capsule.
- Outfit collision disabled by default.
- Tail and wings remain non-blocking except for authored attack or hit reaction windows.
- Stealth/ambush gameplay uses ability volumes and traces, not outfit collision.

## 12. Animation Notes

Use `ANIMATION_HANDOFF.md`. Required rogue overlay:

- low stalk idle
- crouch turn
- silent step
- pounce
- two-hit claw rake
- short wing-assisted reposition
- tail counterbalance
- invisible-sight reveal
- ambush strike
- controlled retreat

## 13. Unreal Import Notes

- Primary mesh: `SK_INF_Rogue_A01`
- Parent body: `SK_INF_Base_A01`
- Unreal path: `/Game/Aerathea/Characters/Infernals/Rogue/`
- Animation Blueprint: `ABP_INF_Rogue_A01`
- Scale: centimeters.
- Required sockets: base claw/wing/tail/eye sockets plus optional `vfx_ambush_mark`.

## 14. Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_INF_Rogue_A01/`
- Source: `SourceAssets/Blender/Characters/Infernals/Rogue/SK_INF_Rogue_A01/`
- Export: `SourceAssets/Exports/Characters/Infernals/Rogue/SK_INF_Rogue_A01/`
- Unreal: `/Game/Aerathea/Characters/Infernals/Rogue/`
- Materials: `MI_INF_Rogue_A01_*`
- Textures: `T_INF_Rogue_A01_*`

## 15. Quality Gate Checklist

- Reads as a stealth Infernal without daggers or mortal weapon dependency.
- Folded wings, tail balance, black claws, red skin, horns, and predatory posture remain clear.
- Invisible-sight glow is focused and readable.
- Gear is animation-safe for crouch, pounce, rake, and tail motion.
- Triangle budget, texture maps, material slots, LODs, collision, animation notes, sockets, and Unreal paths are included.
