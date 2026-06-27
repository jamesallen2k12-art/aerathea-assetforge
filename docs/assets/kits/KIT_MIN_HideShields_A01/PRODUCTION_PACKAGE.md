# KIT_MIN_HideShields_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_MIN_HideShields_A01`
- Asset type: Shield mini-kit
- Source: `Minotaur Arsenal.png#HideShields`
- Parent kit: `KIT_MIN_Arsenal_A01`
- Status: Production package ready; DCC build not started

Original Minotaur hide shield variants built from thick hide, raw iron plates, bone reinforcements, leather lashing, and simple tribal marking.

## Gameplay Purpose

Large shield props for Minotaur warriors, camps, NPC equipment, and display scenes.

## Silhouette Notes

Large hide shields with simple oval, rectangular, and tusk-framed variants. Avoid refined metalwork or ornate heraldry.

## Scale Notes

95-140 cm tall. Fit approved Minotaur body scale: females 7-8 ft, males 8-9 ft.

## Materials And Color Palette

Thick hide, raw iron, bone, leather, fur, dark wood, simple paint markings.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_MIN_HideShields_A01` for the world of Aerathea. The design should emphasize large simple hide-shield silhouettes, raw iron plates, bone reinforcement, leather lashing, dark wood support, fur accents, tribal markings, ruthless Minotaur strength culture, and defensive warrior gameplay roles. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a shield mini-catalog with three variants, front/back views, scale callouts, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model shield slab, major ribs, plates, straps, and bone frames. Fake stitching, hide grain, scratches, and paint wear in maps.

## Texture And Material Notes

- `T_MIN_HideShields_A01_BC`
- `T_MIN_HideShields_A01_N`
- `T_MIN_HideShields_A01_ORM`
- No emissive texture by default

## Triangle Budget

LOD0 3k-7k tris per shield, 1 material slot.

## LOD Plan

LOD0 full shield; LOD1 removes small strap bevels; LOD2 simplifies bones/plates; LOD3 preserves shield outline and major ribs.

## Collision Notes

Equipped collision disabled. World placement uses simple convex or box bounds.

## Animation Notes

Static mesh variants. Blocking and bash motion belong to character animation.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Shields/Minotaur/KIT_MIN_HideShields_A01`
- Pivot: back grip or forearm strap center per variant.
- Scale: centimeters.
- Sockets: none by default.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_MIN_HideShields_A01/`
- Source: `SourceAssets/Blender/Kits/Minotaur/Arsenal/KIT_MIN_HideShields_A01/`
- Export: `SourceAssets/Exports/Kits/Minotaur/Arsenal/KIT_MIN_HideShields_A01/`
- Unreal: `/Game/Aerathea/Shields/Minotaur/`

## Quality Gate Checklist

- Shields read as simple and brutal.
- No refined magical craftsmanship.
- Hide/bone/raw iron language is consistent.
- Pivots and collision are equipment-safe.
- LODs preserve shield mass.
