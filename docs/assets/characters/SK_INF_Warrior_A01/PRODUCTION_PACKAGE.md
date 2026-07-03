# SK_INF_Warrior_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SK_INF_Warrior_A01`
- Asset type: Skeletal Mesh class outfit / Infernal melee class package
- Parent body: `SK_INF_Base_A01`
- World: Aerathea
- Theme: Balgoroth-chosen natural-weapon shock fighter
- Primary references: `SK_INF_Base_A01`, `INFERNAL_VISUAL_CLEANSE_STANDARD.md`, `ANIMATION_HANDOFF.md`, `InfernalMaleLit.png`, `InfernalFemaleLit2.png`, `Infernals.png`
- Current status: approved by Flamestrike on 2026-06-28 as part of the Infernal starter class set; first-pass DCC/Unreal review implementation complete; final sculpt, retopo, UVs, textures, tuned physics, final VFX binding, and animation remain pending

Infernal Warriors are not sword-and-shield soldiers. They are armored natural-weapon combatants who prove strength through claws, horns, tail sweeps, wing pressure, brutal pounces, regeneration, and controlled rage. Armor should amplify their demonic gifts rather than replace them: heavy bracers around clawed hands, wing-root guards, skull/bone hierarchy belts, obsidian chest plates, and reinforced tail-root armor.

## Implementation Status - 2026-06-28

- DCC build script: `Tools/DCC/build_infernal_warrior.py`
- Unreal import script: `Tools/Unreal/import_infernal_warrior.py`
- Focused validator: `Tools/Unreal/validate_infernal_warrior.py`
- Blender source: `SourceAssets/Blender/Characters/Infernals/Warrior/SK_INF_Warrior_A01/SK_INF_Warrior_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Infernals/Warrior/SK_INF_Warrior_A01/SK_INF_Warrior_A01.fbx`
- DCC review image: `Saved/Automation/InfernalWarriorReview/SK_INF_Warrior_A01_DCCReview.png`
- Unreal mesh: `/Game/Aerathea/Characters/Infernals/Warrior/SK_INF_Warrior_A01`
- Shared skeleton: `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton`
- Review actor: `AET_PROD_INF_Warrior_A01`
- Validation: focused Warrior validator passed with visible height 248.71 cm, bounds radius 213.18 cm, and 23 sockets; startup validator passed with 177 assets, 52 expected actors, and 25 ground tiles.

## 2. Gameplay Purpose

- Provides the first Infernal melee class package.
- Supports player/NPC warrior identity, elite cult guards, arena champions, and Balgoroth enforcers.
- Establishes animation and socket needs for claw combos, wing-guard posture, tail sweep, rage surge, regeneration flare, and execute poses.
- Reuses `SK_INF_Base_A01` and `ANIMATION_HANDOFF.md`.

## 3. Silhouette Notes

- Primary read: broad chest, horn crown, folded wing mass, thick tail, heavy claw bracers, skull/bone belt, and forward predatory stance.
- Greater and Exalted bodies are the best first targets; Standard is the common gameplay fit.
- Keep hands free and visibly clawed.
- Use armor as impact framing, not full coverage that hides red skin, claws, wings, or tail.
- Major skull/bone ornaments are allowed; tiny trophy clutter is not.

## 4. Scale Notes

- Adult canon range: 5'0"-9'0" / 152-274 cm.
- First class-fit targets: Standard 190-203 cm, Greater 230-244 cm, Exalted 260-274 cm.
- Tail sweep and wing buffet animation space must be tested against the movement capsule.
- Armor must clear folded wings and tail base deformation.

## 5. Materials And Color Palette

| Family | Palette | Use |
| --- | --- | --- |
| Skin | ember red, ash red, crimson | exposed torso, arms, face, tail |
| Armor | obsidian, blackened iron, scorched bronze | chest, bracers, greaves, wing-root guards |
| Bone/horn | aged ivory, smoke tan, black keratin | skull belt, trophies, horn trims |
| Cloth/leather | ash black, burnt red, charcoal leather | wraps, loin panels, straps |
| Glow | ember orange, deep red, focused violet | eyes, rage brands, regeneration, execute state |

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_INF_Warrior_A01`, an Infernal Warrior for Aerathea. Emphasize a mortal-descended demonic melee fighter blessed by Balgoroth, red skin, black claws, required horns, large folded leathery wings, long thick tail, heavy claw bracers, obsidian armor plates, skull/bone hierarchy belt, wing-root guards, controlled rage, regeneration marks, and natural-weapon combat through claws, horns, wings, and tail rather than mortal weapons. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, focused emissive accents, and MMO-friendly production design. Present front, side, back, three-quarter view, claw combo pose, tail sweep pose, wing-guard pose, material swatches, socket callouts, and scale beside Standard/Greater/Exalted Infernal bands. Apply A03 cleanup: preserve skulls, flame, glowing eyes, anger, and threat while reducing tiny rivets, speckle artifacts, malformed micro-spikes, broken micro-chains, and noisy texture fragments. Avoid copied franchise designs, gore, readable text, watermarks, swords, shields, axes, or weapon-dependent silhouettes.

## 7. Modeling Notes

- Build modular warrior gear over `SK_INF_Base_A01`.
- Model real geometry for chest armor, bracers, greaves, wing-root guards, tail-root armor, skull/bone belt, large shoulder plates, and major claw caps if used.
- Keep claw fingers, wing fold, and tail base visible.
- Use textures/normals for small scratches, tiny rivets, scars, leather grain, cloth weave, and minor bone wear.
- Avoid many small hanging trophies that will skin poorly.

## 8. Texture And Material Notes

Texture maps:

- `T_INF_Warrior_A01_BC`
- `T_INF_Warrior_A01_N`
- `T_INF_Warrior_A01_ORM`
- `T_INF_Warrior_A01_E`

Material slots:

1. Base Infernal skin/body inherited from `SK_INF_Base_A01`
2. `MI_INF_Warrior_A01_Armor`
3. `MI_INF_Warrior_A01_BoneHorn`
4. `MI_INF_Warrior_A01_RitualCloth`
5. Optional `MI_INF_Warrior_A01_RageGlow`

## 9. Triangle Budget

- Class gear LOD0 target: 14k-26k tris.
- Full equipped character with base body: 44k-64k tris.
- Exalted elite ceiling: 68k tris if armor and wing guards justify it.
- Material slot target: 4-5.

## 10. LOD Plan

- LOD0: full body, armor, bracers, wing guards, skull belt, tail armor, socket markers.
- LOD1: reduce bevels, small armor cuts, secondary skull detail.
- LOD2: merge trophy clusters, reduce bracer/greave cuts, simplify straps.
- LOD3: preserve horn crown, wing mass, tail line, claw hands, armor blocks, skull belt, and glow blocks.

## 11. Collision Notes

- Use base Infernal capsule.
- Gear collision disabled by default.
- Tail/wing auxiliary collision only for specific attacks, hit reaction, or boss variants.
- Claw and tail attacks use socket-driven traces and gameplay volumes.

## 12. Animation Notes

Use `ANIMATION_HANDOFF.md`. Required warrior overlay:

- idle controlled rage
- wing-guard posture
- three-hit claw combo
- horn/body check
- tail sweep
- wing buffet
- pounce
- execute pose
- regeneration flare
- rage surge

## 13. Unreal Import Notes

- Primary mesh: `SK_INF_Warrior_A01`
- Parent body: `SK_INF_Base_A01`
- Unreal path: `/Game/Aerathea/Characters/Infernals/Warrior/`
- Animation Blueprint: `ABP_INF_Warrior_A01`
- Pivot: inherited from base body at ground center.
- Scale: centimeters.
- Required sockets: base claw, wing, tail, eye, chest brand, regeneration, forearm brand, rage core, tail-sweep trace, wing-buffet trace, and body-check trace sockets.

## 14. Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_INF_Warrior_A01/`
- Source: `SourceAssets/Blender/Characters/Infernals/Warrior/SK_INF_Warrior_A01/`
- Export: `SourceAssets/Exports/Characters/Infernals/Warrior/SK_INF_Warrior_A01/`
- Unreal: `/Game/Aerathea/Characters/Infernals/Warrior/`
- Materials: `MI_INF_Warrior_A01_*`
- Textures: `T_INF_Warrior_A01_*`

## 15. Quality Gate Checklist

- Reads as an Infernal warrior without mortal weapon dependency.
- Horns, wings, tail, black claws, red skin, and predatory posture remain clear.
- Armor supports natural weapons and does not hide race traits.
- Major forms are geometry; tiny noise stays in maps.
- Triangle budget, texture maps, material slots, LODs, collision, animation notes, sockets, and Unreal paths are included.
