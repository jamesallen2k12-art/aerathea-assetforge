# SK_INF_Base_A01 Production Package

## Art Direction Summary

`SK_INF_Base_A01` defines the adult Infernal race body/style package. Infernals are mortal-descended demonic beings, blessed by Balgoroth after generations of cult devotion to demonic forces and forgotten gods of the Abyss. They are not true Abyss demons. They are a race with bloodlines, courts, cult laws, hunting packs, ritual hierarchies, and personal ambition.

Their bodies must communicate willing transformation: reddish skin, black claws, horns, large leathery wings, a long thick tail, predatory posture, regenerative scars, and eyes or brands that imply invisible sight. They reject mortal weaponry as weakness, so their combat identity is natural weapons, body power, magic, wings, tail, and demonic gifts.

The final adult production art direction is locked in `FINAL_ART_DIRECTION.md`, using body-type bands instead of a strict male/female height split: Compact, Standard, Greater, and Exalted.

All adult Infernal source images must pass through `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md` before they become modeling, texture, VFX, or prompt requirements.

## Gameplay Purpose

The base package supports playable or NPC race development, enemy faction variants, cult leaders, hunters, rogues, mages, and natural-weapon combat. It provides the adult body target that later class packages will build on:

- `SK_INF_Warrior_A01`
- `SK_INF_Rogue_A01`
- `SK_INF_Hunter_A01`
- `SK_INF_Mage_A01`
- `SK_INF_Lesser_A01`
- `KIT_INF_BalgorothCult_A01`

## Silhouette Notes

- Required: horns, large leathery wings, long thick tail, black claws.
- Adult bodies range from 5'0"-9'0" / 152-274 cm.
- First review uses two adult targets: 165 cm compact body and 245 cm tall body.
- Build athletic to powerful humanoid proportions, not hunched monster caricature.
- Wings should read clearly even when folded; spread-wing silhouette must remain production-friendly.
- Tail should be thick enough to matter in profile and animation.
- Hands need visible black claws and natural-weapon readiness.
- Facial read: human-derived but transformed, with strong brow, horn roots, predatory eyes, and controlled rage.

## Scale Notes

- Canon adult range: 5'0"-9'0" / 152-274 cm.
- Production body bands: Compact 5'0"-5'8", Standard 5'8"-6'8", Greater 6'8"-8'0", Exalted 8'0"-9'0".
- First-pass adult review heights:
  - `SK_INF_Base_Compact_A01`: 165 cm.
  - `SK_INF_Base_Tall_A01`: 245 cm.
- Sex-specific variants remain future character-creation work and must stay inside the locked body bands.
- Review should include a 180 cm humanoid marker and Lesser Infernal stage markers.

## Materials And Color Palette

- Skin: ember red, crimson, ash red, dark umber, subtle healed scar variation.
- Horns/claws: black keratin, dark horn tips, worn edges.
- Wings: dark leather membrane, red-brown undertone, thicker leading fingers.
- Ritual material: charcoal leather, ash cloth, bone beads, obsidian ornaments, scorched metal.
- Glow: readable eye glow, chest/forehead/hand brands, mage spell marks, fire/lightning-like abyssal power for caster variants, and invisible-sight accents.

## Concept Image Prompt

Create an original stylized fantasy MMORPG race body/style concept sheet of adult Infernals for the world of Aerathea. The design should emphasize a mortal-descended demonic race blessed by Balgoroth, reddish skin, black claws, required horns, large leathery wings, long thick tail, regenerative scar language, invisible-sight eye glow, natural-weapon combat, contempt for mortal weaponry, predatory upright posture, major skull/bone villain iconography where appropriate, and adult scale range from 5'0" to 9'0". Use hand-painted texture detail, readable MMO shapes, baked-AO-style depth, normal-map-style surface detail, focused emissive accents, and production-friendly forms. Present it as a body/style sheet with compact and tall adult bodies, folded and spread wing views, tail callouts, horn variants, claw detail, material swatches, natural-weapon poses, and a 180 cm humanoid comparison. Clean the design for production readability: full body visible, feet and wings uncropped, readable midtone lighting, clear separation between red skin, black armor, dark wings, and background. If the source is too dark, start from a roughly 30 percent brighter pass. Use A03-style cleanup by default: reduce tiny repeated rivets, random speckle artifacts, malformed micro-spikes, broken micro-chains, torn-strip noise, dense spell clutter that hides anatomy, and photoreal surface garbage. Preserve skulls, bones, flame, lightning, glowing eyes, anger, and villain threat. Avoid copied franchise designs, gore, excessive particles, readable text, watermarks, and weapon-focused designs.

## Modeling Notes

- Author in centimeters at real Unreal scale.
- Build compact and tall adult review bodies first.
- Real geometry: main body forms, horns, claws, wings, tail, major ritual jewelry, large scar ridges if needed.
- Texture/normal detail: skin grain, healed scars, tiny brands, membrane veins, horn striations, small jewelry scratches.
- Wings need a folded state for gameplay navigation and a spread review pose for silhouette approval.
- Tail needs a root, mid, and tip control plan.
- Hands and feet must support claw attacks.

## Texture And Material Notes

- Texture set:
  - `T_INF_Base_A01_BC`
  - `T_INF_Base_A01_N`
  - `T_INF_Base_A01_ORM`
  - `T_INF_Base_A01_E`
- Material slots: skin, horn/claw, wing membrane, ritual wraps/ornaments, emissive.
- Use 2K texture sets by default. Use 4K only for named leaders, Ancient variants, or cinematic closeups.
- Emissive limited to eyes, brands, mage marks, and invisible-sight cues.

## Triangle Budget

- Compact adult LOD0: 28k-40k tris.
- Tall adult LOD0: 32k-48k tris.
- Winged/mage hero variants may reach 55k tris if wing and ritual silhouette requires it.
- Material slot target: 4-5.

## LOD Plan

- LOD0: full body, horns, claws, wings, tail, face, hands, material callouts.
- LOD1: 55-60 percent; reduce small jewelry, minor wing membrane cuts, small scars.
- LOD2: 25-35 percent; simplify fingers, claws, tail taper, wing struts, small brands.
- LOD3: 10-15 percent; preserve horns, wings, tail, claws, body height, red/black color read.

## Collision Notes

- Use humanoid capsule sized to body target.
- Wings should not block default navigation unless a wing-shield ability or boss variant requires it.
- Tail collision should be simplified to 2-4 bodies and enabled only for combat or hit reaction as needed.
- Physics bodies: pelvis, spine, chest, head, upper/lower arms, hands, thighs, calves, feet, tail root/mid/tip, wing upper/lower simplified bodies.

## Animation Notes

- Base: idle, walk, run, turn, jump/land or wing-assisted hop, hit react, death, interact.
- Natural combat: claw combo, bite/snarl, tail sweep, wing buffet, leap, pounce, execute pose.
- Utility: see-invisible focus gesture, regeneration flare, controlled rage idle.
- Wing states: folded idle, flare, short burst, glide test if approved, damaged-fold variant.

## Unreal Import Notes

- Asset type: Skeletal Mesh.
- Primary asset: `SK_INF_Base_A01`.
- First review assets:
  - `SK_INF_Base_Compact_A01`
  - `SK_INF_Base_Tall_A01`
- Folder path: `/Game/Aerathea/Characters/Infernals/Base/`.
- Scale: centimeters, no import scaling after DCC export.
- Pivot: between feet at ground center.
- Sockets: `hand_l_claw`, `hand_r_claw`, `tail_tip`, `wing_l_tip`, `wing_r_tip`, `vfx_eye_l`, `vfx_eye_r`, `vfx_brand_chest`, `vfx_mouth`, `vfx_regen_core`.
- Blueprint behavior belongs in class packages after base body approval.

## Folder And Naming Recommendation

- Package folder: `docs/assets/characters/SK_INF_Base_A01/`.
- Final art direction sheet: `docs/assets/characters/SK_INF_Base_A01/FINAL_ART_DIRECTION.md`.
- Blender source: `SourceAssets/Blender/Characters/Infernals/SK_INF_Base_A01/SK_INF_Base_A01.blend`.
- FBX exports: `SourceAssets/Exports/Characters/Infernals/SK_INF_Base_A01/`.
- Unreal folder: `/Game/Aerathea/Characters/Infernals/Base/`.

## Quality Gate Checklist

- Adult body range remains 5'0"-9'0".
- Infernals read as mortal-descended demonic race, not true Abyss demons.
- Horns, wings, tail, and black claws are mandatory silhouette features.
- Natural-weapon doctrine is respected; no mortal weapon dependency.
- Regeneration and invisible sight have controlled visual hooks.
- Wing/tail/claw rig and collision needs are defined.
- Texture maps, LODs, sockets, Unreal paths, and performance budgets are included.
