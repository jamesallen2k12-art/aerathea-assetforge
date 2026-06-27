# SK_DWR_Helm_Stonebound_A01 Production Package

## Art Direction Summary

- Asset name: `SK_DWR_Helm_Stonebound_A01`
- Asset type: Skeletal Mesh armor module or Static Mesh helm, final type depends on character attachment workflow
- Source: `Dwarven Armory.png#Helm_Stonebound`
- Parent kit: `KIT_DWR_Armory_A01`
- Status: Production package ready; DCC fit blocked on approved Dwarven base body/skeleton

Original Dwarven full helm with broad brow, cheek guards, stone-and-steel mass, brass runic trim, and compact mountain-forged proportions.

## Gameplay Purpose

Guardian/runesmith head armor module for Dwarven player characters, NPC variants, and armory display.

## Silhouette Notes

Broad brow, low crown, sturdy cheek plates, short neck guard, and frontal rune plate. Avoid tall fragile crests.

## Scale Notes

Fit future Dwarven head proportions. Do not model to human proportions until Dwarven base body is approved.

## Materials And Color Palette

Dark steel, slate stone plates, aged brass trim, leather lining, blue rune accents.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SK_DWR_Helm_Stonebound_A01` for the world of Aerathea. The design should emphasize a broad low Dwarven helm silhouette, heavy steel and stone plates, aged brass runic trim, dark leather lining, sparing blue rune glow, mountain-forged guardian identity, and defensive armor gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production armor sheet with front, side, back, three-quarter view, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model the main shell, brow, cheek plates, neck guard, and major trim. Fake tiny etched runes, scratches, rivets, and leather texture in maps.

## Texture And Material Notes

- `T_DWR_Helm_Stonebound_A01_BC`
- `T_DWR_Helm_Stonebound_A01_N`
- `T_DWR_Helm_Stonebound_A01_ORM`
- `T_DWR_Helm_Stonebound_A01_E` for rune glow only

## Triangle Budget

LOD0 3k-7k tris, 1-2 material slots.

## LOD Plan

LOD0 full helm; LOD1 removes minor trim bevels; LOD2 simplifies cheek and neck plates; LOD3 preserves brow and head outline.

## Collision Notes

No gameplay collision while equipped. Use capsule/head overlap only if a future interaction requires it.

## Animation Notes

Armor module follows head bone. Facial/helmet clipping checks wait for approved Dwarven rig.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Characters/Dwarves/Armor/SK_DWR_Helm_Stonebound_A01`
- Pivot: aligned to future Dwarven head socket.
- Scale: centimeters.
- Socket target: future `head_helm` or equivalent.

## Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_DWR_Helm_Stonebound_A01/`
- Source: `SourceAssets/Blender/Kits/Dwarven/Armory/SK_DWR_Helm_Stonebound_A01/`
- Export: `SourceAssets/Exports/Kits/Dwarven/Armory/SK_DWR_Helm_Stonebound_A01/`
- Unreal: `/Game/Aerathea/Characters/Dwarves/Armor/SK_DWR_Helm_Stonebound_A01`

## Quality Gate Checklist

- Dwarven broad-head proportions are preserved.
- Fit waits for approved Dwarven base body.
- Glow is limited to rune accents.
- Major plates are geometry; micro marks are texture.
- LODs and attachment plan are defined.
