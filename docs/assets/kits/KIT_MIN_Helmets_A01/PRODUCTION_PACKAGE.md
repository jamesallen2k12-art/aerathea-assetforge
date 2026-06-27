# KIT_MIN_Helmets_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_MIN_Helmets_A01`
- Asset type: Armor mini-kit
- Source: `Minotaur Arsenal.png#Helmets`
- Parent kit: `KIT_MIN_Arsenal_A01`
- Status: Production package ready; DCC fit blocked on approved Minotaur base body/skeleton

Original Minotaur helmet variants using raw iron, hide, bone, horn guards, and simple brutal profiles.

## Gameplay Purpose

Head armor variants for Minotaur warriors, berserkers, shamans, and NPC rank differentiation.

## Silhouette Notes

Broad head openings, horn clearance, heavy brow plates, cheek guards, and simple brutal forms. Avoid ornate fine craft.

## Scale Notes

Fit future Minotaur head and horn shapes for females 7-8 ft and males 8-9 ft. Do not finalize fit until base body exists.

## Materials And Color Palette

Raw iron, hide, bone, leather, fur, dark wood, simple tribal marks.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_MIN_Helmets_A01` for the world of Aerathea. The design should emphasize broad Minotaur helmet silhouettes, horn clearance, raw iron brow plates, hide and leather straps, bone reinforcement, fur accents, simple tribal markings, ruthless Minotaur warrior culture, and armor gameplay roles for berserkers and warriors. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a helmet mini-catalog with front, side, back, scale, and horn-clearance callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model shells, brow plates, cheek guards, horn guards, and large straps. Fake dents, stitching, hide grain, and small marks in textures.

## Texture And Material Notes

- `T_MIN_Helmets_A01_BC`
- `T_MIN_Helmets_A01_N`
- `T_MIN_Helmets_A01_ORM`
- No emissive texture by default

## Triangle Budget

LOD0 4k-8k tris per helmet variant, 1 material slot.

## LOD Plan

LOD0 full helmet; LOD1 removes small strap bevels; LOD2 simplifies cheek/horn guard detail; LOD3 preserves helmet and horn-clearance silhouette.

## Collision Notes

No gameplay collision while equipped.

## Animation Notes

Armor module follows head/neck bones. Final attachment waits for Minotaur skeleton.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Characters/Minotaur/Armor/KIT_MIN_Helmets_A01`
- Pivot: aligned to future head socket.
- Scale: centimeters.
- Socket target: future `head_helm` or equivalent.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_MIN_Helmets_A01/`
- Source: `SourceAssets/Blender/Kits/Minotaur/Arsenal/KIT_MIN_Helmets_A01/`
- Export: `SourceAssets/Exports/Kits/Minotaur/Arsenal/KIT_MIN_Helmets_A01/`
- Unreal: `/Game/Aerathea/Characters/Minotaur/Armor/`

## Quality Gate Checklist

- Horn clearance is explicit.
- Fit remains gated on approved Minotaur body.
- Brutal simple material language is preserved.
- LODs preserve large helmet forms.
- No unnecessary magic glow is introduced.
