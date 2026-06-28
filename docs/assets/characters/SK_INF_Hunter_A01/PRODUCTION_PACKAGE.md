# SK_INF_Hunter_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SK_INF_Hunter_A01`
- Asset type: Skeletal Mesh class outfit / Infernal pursuit class package
- Parent body: `SK_INF_Base_A01`
- World: Aerathea
- Theme: invisible-sight tracker, winged pursuit predator, natural-weapon hunter
- Primary references: `SK_INF_Base_A01`, `ANIMATION_HANDOFF.md`, `INFERNAL_VISUAL_CLEANSE_STANDARD.md`, `InfernalMaleLit.png`, `InfernalFemaleLit2.png`, Lesser action references
- Current status: production package and modeling handoff ready; DCC build not started

Infernal Hunters are not archers. They hunt by seeing what prey tries to hide, crossing distance with wing-assisted bursts, using tail balance in leaps, and killing with claws, teeth, horns, and body-powered strikes. Their gear should support pursuit and trophy hierarchy without becoming a mortal weapon kit: tracking brands, eye/brow marks, light armor, wing harness straps, claw guards, tail bands, bone markers, and prey-scent ritual charms.

## 2. Gameplay Purpose

- Supports Infernal hunter/scout/tracker identity.
- Provides anti-stealth, pursuit, leap, pounce, target-mark, and ambush-counter gameplay reads.
- Creates a visual class between Rogue and Warrior: more mobile/tracking than Warrior, more direct pursuit than Rogue.
- Reuses `VFX_INF_AbyssalSpellcasting_A01` for invisible-sight reveal and target-mark pulses.

## 3. Silhouette Notes

- Primary read: alert forward posture, eye/brow glow, folded wings ready to burst, tail held for balance, clawed hands open, light pursuit armor.
- Best first body targets: Standard and Greater bands.
- Gear should expose shoulders/arms/hands enough to read claw attacks and tracking gestures.
- Use bone/horn markers as trophies of worthy prey; avoid noisy trophy racks.
- No bows, rifles, spears, or nets as primary identity.

## 4. Scale Notes

- Adult canon range: 5'0"-9'0" / 152-274 cm.
- First class-fit targets: Standard 173-203 cm and Greater 203-244 cm.
- Leap/pounce animations must preserve wing and tail clearance.
- Tracking pose needs readable eye, hand, head, and tail alignment at gameplay camera distance.

## 5. Materials And Color Palette

| Family | Palette | Use |
| --- | --- | --- |
| Skin | ember red, ash red, crimson | exposed face, arms, hands, legs, tail |
| Light armor | blackened iron, obsidian, dark leather | chest straps, thigh plates, shin/forearm guards |
| Tracking marks | ember orange, deep red, focused violet | eyes, brow, forearms, target-mark channels |
| Bone/horn | aged ivory, smoke tan, black keratin | worthy-prey markers, horn trims, small trophies |
| Cloth/leather | charcoal, soot brown, burnt red | pursuit wraps, harness straps |

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_INF_Hunter_A01`, an Infernal Hunter for Aerathea. Emphasize a mortal-descended demonic tracker blessed by Balgoroth, red skin, black claws, required horns, folded leathery wings ready for pursuit bursts, a long thick tail used for balance, glowing invisible-sight eyes and brow marks, light obsidian and blackened-iron pursuit armor, claw guards, wing harness straps, bone/horn worthy-prey markers, target-mark brand channels, and natural-weapon hunting through tracking, pounce, leap, claws, wings, and tail rather than mortal bows or traps. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, focused emissive accents, and MMO-friendly production design. Present front, side, back, tracking pose, pounce pose, wing-burst pose, target-mark callout, material swatches, socket callouts, and scale beside Standard/Greater Infernal bands. Apply A03 cleanup: preserve glowing eyes, menace, skull/bone cues, flame or lightning-like energy, and threat while reducing tiny rivets, speckle artifacts, malformed micro-spikes, broken micro-chains, and noisy texture fragments. Avoid copied franchise designs, gore, readable text, watermarks, bows, rifles, spears, traps, or weapon-dependent silhouettes.

## 7. Modeling Notes

- Build modular hunter gear over `SK_INF_Base_A01`.
- Model real geometry for light armor plates, wing harness straps, claw guards, tail bands, brow/forearm raised mark ridges if approved, and major bone/horn prey markers.
- Keep eyes, brow, hands, wing roots, and tail line unobstructed.
- Use textures/normals for small scars, small brands, leather grain, scratches, and minor trophy wear.
- Avoid dangling trophy clutter that interferes with running, leaping, or wing burst poses.

## 8. Texture And Material Notes

Texture maps:

- `T_INF_Hunter_A01_BC`
- `T_INF_Hunter_A01_N`
- `T_INF_Hunter_A01_ORM`
- `T_INF_Hunter_A01_E`

Material slots:

1. Base Infernal skin/body inherited from `SK_INF_Base_A01`
2. `MI_INF_Hunter_A01_PursuitArmor`
3. `MI_INF_Hunter_A01_HarnessLeather`
4. `MI_INF_Hunter_A01_BoneHorn`
5. Optional `MI_INF_Hunter_A01_SightMarkGlow`

## 9. Triangle Budget

- Class gear LOD0 target: 10k-20k tris.
- Full equipped character with base body: 38k-58k tris.
- Greater elite ceiling: 62k tris if wing harness and trophy markers justify it.
- Material slot target: 4-5.

## 10. LOD Plan

- LOD0: full body, pursuit armor, wing harness, claw guards, tail bands, bone markers, target-mark glow.
- LOD1: reduce strap bevels, minor plates, secondary bone detail.
- LOD2: merge small trophy clusters, simplify harness straps and tail bands.
- LOD3: preserve horn crown, folded wings, tail line, claw hands, eye/brow glow, and broad armor blocks.

## 11. Collision Notes

- Use base Infernal capsule.
- Gear collision disabled by default.
- Wing/tail auxiliary bodies enabled only for authored pounce, wing burst, hit reaction, or boss variants.
- Tracking and target-mark gameplay uses traces and ability volumes, not mesh collision.

## 12. Animation Notes

Use `ANIMATION_HANDOFF.md`. Required hunter overlay:

- alert tracking idle
- invisible-sight target lock
- scent/brand tracking gesture
- wing-assisted pursuit burst
- pounce
- claw takedown
- tail balance turn
- target-mark cast
- anti-stealth reveal
- controlled kill pose

## 13. Unreal Import Notes

- Primary mesh: `SK_INF_Hunter_A01`
- Parent body: `SK_INF_Base_A01`
- Unreal path: `/Game/Aerathea/Characters/Infernals/Hunter/`
- Animation Blueprint: `ABP_INF_Hunter_A01`
- Scale: centimeters.
- Required sockets: base claw/wing/tail/eye sockets plus optional `vfx_target_mark`, `vfx_brow_sight`, and `vfx_pursuit_burst`.

## 14. Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_INF_Hunter_A01/`
- Source: `SourceAssets/Blender/Characters/Infernals/Hunter/SK_INF_Hunter_A01/`
- Export: `SourceAssets/Exports/Characters/Infernals/Hunter/SK_INF_Hunter_A01/`
- Unreal: `/Game/Aerathea/Characters/Infernals/Hunter/`
- Materials: `MI_INF_Hunter_A01_*`
- Textures: `T_INF_Hunter_A01_*`

## 15. Quality Gate Checklist

- Reads as an Infernal hunter without bow/trap/rifle dependency.
- Tracking and invisible-sight identity are readable through eyes, brow, hand, wing, and tail poses.
- Horns, wings, tail, black claws, red skin, and predatory posture remain clear.
- Gear supports fast pursuit and pounce animation.
- Triangle budget, texture maps, material slots, LODs, collision, animation notes, sockets, and Unreal paths are included.
