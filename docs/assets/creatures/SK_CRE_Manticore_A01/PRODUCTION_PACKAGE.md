# SK_CRE_Manticore_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SK_CRE_Manticore_A01`
- Asset type: Skeletal Mesh large creature
- World: Aerathea
- Theme: common dangerous ruin/desert predator
- Source concepts: `Manticore.png`, `Manticore1.png`, `Manticore3.png`, `Manticore4.png`, `Manticore5.png`, `Manticore8.png`, plus variant-only checks from `Manticore2.png`, `Manticore6.png`, `Manticore7.png`, `Manticore9.png`, and `Manticore10.png`
- Source folder: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/`
- Current status: base production direction, skeleton/proportion plan, modeling handoff, and build/import status ready; DCC build not started

`SK_CRE_Manticore_A01` is the shared Aerathea Manticore body and rig target. It establishes the readable base creature before the Gnome/Ogre interrupt variant, future elemental variants, or named elite versions are built. The approved anchor is lion body, bat/draconic wings, and scorpion tail, with a clear tail stinger and leathery wing silhouette.

The base direction uses the dark/tawny ruin predator references. White feathered, frost, moonlit, lava, and tamed/armored readings are future variants and should not change the base silhouette.

## 2. Gameplay Purpose

- Provides a reusable wild predator for ruins, deserts, canyons, low mountain passes, and hostile wilderness zones.
- Establishes the shared Manticore skeleton, physics bodies, sockets, material families, and animation set.
- Unlocks `SK_CRE_Manticore_Interrupt_A01` as a Gnome/Ogre encounter variant.
- Supports future elite, world-event, dungeon, and elemental-skin variants without rebuilding anatomy.
- Gives combat designers a clear creature profile: leap pressure, wing buffet, tail sweep, stinger strike, bite/claw combo, venom telegraph, and short ground charge.

## 3. Silhouette Notes

- Massive lion body with heavy shoulders, lower stalking stance, deep chest, muscular haunches, clawed paws, and a large mane mass.
- Large leathery bat/draconic wings mounted behind the shoulder blades, with strong wing arms, clear finger bones, and broad membrane panels.
- High arcing segmented scorpion tail that reads above the back in idle, prowl, and attack poses.
- Oversized hooked stinger with a simple venom groove and readable attack point.
- Lion-like head and muzzle remain the base identity. Horns, spikes, or armor should be restrained and variant-driven.
- Avoid eagle/gryphon feather language, dragon body anatomy, demon/humanoid facial structure, faction armor, saddle tack, or Teknomancy devices on the base creature.

## 4. Scale Notes

Author in centimeters.

- Shoulder height: 230-260 cm.
- Head height in neutral alert pose: 300-340 cm.
- Body length nose to rump: 520-650 cm.
- Tail arc height: 480-600 cm.
- Tail length along curve: 420-520 cm.
- Wingspan spread: 900-1100 cm.
- Folded wing width should stay within a practical combat footprint and not hide the tail arc.

The creature should feel threatening beside 10-11 ft Ogres, larger than standard humanoid enemies, and smaller than true boss-scale dragons or giants.

## 5. Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Lion hide | tawny gold, sand brown, muted ochre, dirty tan | Body, legs, face |
| Mane | dark umber, charcoal brown, black tips | Head, chest, shoulders, silhouette framing |
| Wing membrane | dark rust, leathery brown, smoky red, gray-brown underside | Main wing panels and tears |
| Wing bones | dark horn, burnt bronze, blackened brown | Wing arms and fingers |
| Tail chitin | black-brown, burnt bronze, dark horn, dull obsidian | Segments, ridges, stinger shell |
| Claws and teeth | dark ivory, bone, black horn | Paws, mouth, stinger tip accents |
| Venom telegraph | muted amber-green, sickly yellow-green | Stinger groove, mouth spit cue, optional status wound |
| Environmental wear | gray dust, ash, stone grit, dried mud | Feet, lower legs, scars, wing edges |

Use emissive sparingly. The base creature can have non-emissive eyes; emissive is allowed only for venom telegraph states or elite variants.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_CRE_Manticore_A01` for the world of Aerathea. The design should emphasize a massive lion body with heavy shoulders and dark mane, large leathery bat/draconic wings with strong finger bones and broad membrane panels, a high arcing segmented scorpion tail with an oversized hooked stinger, tawny ruin-predator hide, black-brown chitin, smoky rust wing membranes, restrained venom accents, dangerous ancient ruin and desert wilderness identity, and a gameplay role as a leap, wing-buffet, and tail-sting predator. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents only for venom telegraphs, and MMO-friendly production design. Present it as a creature production sheet with front, side, back, folded-wing, wing-spread, tail-sting pose, scale lineup against a 180 cm humanoid and an Ogre, skeleton callouts, socket callouts, material swatches, and LOD silhouette notes on a clean background. Avoid copying any existing franchise, avoid feathered bird wings, avoid dragon body anatomy, avoid faction armor or machinery, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

- Model real geometry for body mass, head planes, muzzle, ears, mane silhouette clumps, paws, claws, teeth, wing arms, wing fingers, major membrane panels, tail segments, and stinger.
- Use texture and normal maps for fine fur direction, small scars, membrane scratches, pores, tiny tail chips, dirt, and small venom staining.
- Keep the body anatomy lion-first. Do not elongate the torso into a dragon or shrink the hindquarters until it loses feline power.
- Build wing roots with enough shoulder clearance for folded, spread, buffet, leap, landing, and hit-react poses.
- Build the tail as overlapping segmented plates over a deforming chain. Segments must not clip badly in a tight curl or stinger thrust.
- Keep the mane as broad clumps and silhouette planes, not many small hair strands.
- Preserve the stinger silhouette through LOD2 and LOD3 because it communicates threat and creature identity.

## 8. Texture And Material Notes

Material slot target: 3, maximum 4.

Recommended slots:

1. `MI_CRE_Manticore_A01_Body` - body hide, mane, face, lower dust.
2. `MI_CRE_Manticore_A01_Wings` - membranes, wing arms, tears, edge wear.
3. `MI_CRE_Manticore_A01_TailClaws` - tail chitin, stinger, claws, teeth.
4. Optional `MI_CRE_Manticore_A01_Venom` - venom glow state only if gameplay telegraph needs a separate material.

Texture maps:

- `T_CRE_Manticore_A01_Body_BC`
- `T_CRE_Manticore_A01_Body_N`
- `T_CRE_Manticore_A01_Body_ORM`
- `T_CRE_Manticore_A01_Wings_BC`
- `T_CRE_Manticore_A01_Wings_N`
- `T_CRE_Manticore_A01_Wings_ORM`
- `T_CRE_Manticore_A01_TailClaws_BC`
- `T_CRE_Manticore_A01_TailClaws_N`
- `T_CRE_Manticore_A01_TailClaws_ORM`
- Optional `T_CRE_Manticore_A01_Venom_E`

Use 2K texture sets for normal world use. Use 4K only for a hero/named elite or cinematic review variant.

## 9. Triangle Budget

Large creature target:

- LOD0: 35k-50k tris.
- LOD1: 22k-30k tris.
- LOD2: 10k-16k tris.
- LOD3: 3k-6k tris.

Spend silhouette budget on wings, tail, stinger, paws, head, and mane mass before small scars, tiny membrane holes, or minor tail chips.

## 10. LOD Plan

- LOD0: full lion body, face, mane clumps, paws/claws, wing fingers, major membrane tears, tail segments, stinger, sockets, and gameplay telegraph shapes.
- LOD1: reduce mane clumps, small paw bevels, minor tail-segment bevels, and secondary membrane tears while keeping wing profile and stinger.
- LOD2: merge wing membrane panels, simplify paws, reduce tail rings, collapse small scar geometry, keep two-wing profile, lion body, tail arc, and stinger tip.
- LOD3: preserve broad body mass, wing span/folded profile, dark mane block, scorpion tail curve, and stinger point with large color blocks only.

Never reduce the stinger, tail arc, wing outline, or lion-body mass before small surface decorations.

## 11. Collision Notes

- Use a creature movement capsule/body proxy tuned to torso footprint, not full wing span.
- Physics asset bodies: pelvis, chest, neck, head, jaw, shoulders, upper/lower forelegs, paws, hips, upper/lower hind legs, wing roots, upper/lower wing arms, tail base, tail mid segments, and stinger.
- Use overlap volumes or swept socket traces for wing buffet, tail sweep, tail sting, bite, claw, leap impact, venom spit, and landing dust.
- Do not use per-membrane, per-mane, or per-tail-plate collision.
- Do not use complex-as-simple collision on the skeletal mesh.

## 12. Animation Notes

Base animation list:

- Idle crouch.
- Idle alert.
- Prowl walk.
- Short charge.
- Turn in place.
- Leap start.
- Leap landing.
- Wing spread threat.
- Wing buffet.
- Tail sting.
- Tail sweep.
- Bite.
- Claw swipe left/right.
- Bite/claw combo.
- Roar.
- Venom telegraph.
- Hit react front.
- Hit react side.
- Hit react wing.
- Wounded retreat.
- Death.

Optional future states:

- Cliff perch idle.
- Background arrival glide.
- Takeoff and landing.
- Mounted or controlled guardian poses only after a separate tamed variant is approved.

## 13. Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Manticores/Base/`
- Skeletal mesh: `SK_CRE_Manticore_A01`
- Skeleton: `SKEL_CRE_Manticore_A01`
- Physics asset: `PHYS_CRE_Manticore_A01`
- Animation Blueprint placeholder: `ABP_CRE_Manticore_A01`
- Pivot: ground center under body mass between front and rear paws.
- Scale: 1 Unreal unit = 1 cm.
- Material slots: 3 target, 4 maximum.
- LODs: import or generate LOD0-LOD3 and manually inspect wing, tail, stinger, head, and body silhouettes.

Sockets:

- `socket_head_fx`
- `socket_mouth_fx`
- `socket_bite_trace`
- `socket_claw_l`
- `socket_claw_r`
- `socket_foot_l`
- `socket_foot_r`
- `socket_wing_l_root`
- `socket_wing_r_root`
- `socket_wing_l_tip`
- `socket_wing_r_tip`
- `socket_tail_base`
- `socket_tail_mid`
- `socket_tail_stinger`
- `socket_vfx_venom_drip`
- `socket_vfx_landing_dust`
- `socket_back_variant`

`socket_back_variant` is reserved for future harness, trophy, or tamed-guardian variants and should remain unused on the base wild creature.

## 14. Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_CRE_Manticore_A01/`
- Source: `SourceAssets/Blender/Creatures/Manticores/SK_CRE_Manticore_A01/`
- Export: `SourceAssets/Exports/Creatures/Manticores/SK_CRE_Manticore_A01/`
- Unreal: `/Game/Aerathea/Creatures/Manticores/Base/`
- Mesh: `SK_CRE_Manticore_A01`
- Skeleton: `SKEL_CRE_Manticore_A01`
- Physics: `PHYS_CRE_Manticore_A01`
- Animation Blueprint: `ABP_CRE_Manticore_A01`
- Materials: `MI_CRE_Manticore_A01_*`
- Textures: `T_CRE_Manticore_A01_*`

Variant naming examples:

- `SK_CRE_Manticore_Interrupt_A01`
- `SK_CRE_Manticore_Frost_A01`
- `SK_CRE_Manticore_Volcanic_A01`
- `SK_CRE_Manticore_Guardian_A01`

## 15. Quality Gate Checklist

- Reads immediately as lion body, leathery bat/draconic wings, and scorpion tail.
- Tail stinger is visible in neutral, prowl, attack, and distant LOD silhouettes.
- Wing language is leathery, not feathered.
- Does not become a dragon, gryphon, hippogryph, demon, or faction machine.
- Uses broad, readable mid-poly forms with fine fur, membrane, and chitin detail moved to textures.
- Includes material slots, texture map names, triangle budgets, LOD plan, collision notes, animation list, sockets, and Unreal import path.
- Unlocks `SK_CRE_Manticore_Interrupt_A01` without forcing encounter-specific anatomy into the base creature.
- Keeps white/frost, lava, moonlit, armored, and tamed versions as variants, not base direction.
- Original to Aerathea and buildable as an Unreal skeletal mesh.
