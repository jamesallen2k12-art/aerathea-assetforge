# SM_DKH_ReedShellShield_A01 Production Package

## Art Direction Summary

- Asset name: `SM_DKH_ReedShellShield_A01`
- Asset type: Static Mesh shield
- Source: `Drakhar Arms Relics and Field Gear.png#Shield_ReedShell`
- Parent kit: `KIT_DKH_FieldGear_A01`
- Status: Production package ready; DCC build not started

Original Drakhar light shield made from layered reed, shell, bone edging, leather straps, and small ember relic tie-offs.

## Gameplay Purpose

Light shield for Drakhar rangers/rogues/shamans, field gear displays, NPC equipment, and defensive socket tests.

## Silhouette Notes

Rounded layered reed-shell profile with bone edge and visible strap silhouette. Avoid heavy metal shield mass.

## Scale Notes

45-75 cm diameter or height, corrected to A04 Drakhar scale: females 3'6"-4'2", males 4'0"-4'6".

## Materials And Color Palette

Reed, shell, bone, leather, sun-baked cord, muted desert cloth, ember relic accents.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_DKH_ReedShellShield_A01` for the world of Aerathea. The design should emphasize a light rounded reed-shell shield silhouette, layered woven reeds, shell plates, bone edging, leather straps, ember relic tie-offs, corrected A04 Drakhar scale, desert-lizard field-craft identity, magic-seeking culture, and agile defensive gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, back, side, scale callout, and material callouts on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

Model shield body, rim, large layered shell/reed plates, straps, and major tie-offs. Fake weave, shell striations, and small glyphs in maps.

## Texture And Material Notes

- `T_DKH_ReedShellShield_A01_BC`
- `T_DKH_ReedShellShield_A01_N`
- `T_DKH_ReedShellShield_A01_ORM`
- `T_DKH_ReedShellShield_A01_E` for ember tie-offs only

## Triangle Budget

LOD0 2k-5k tris, 1 material slot.

## LOD Plan

LOD0 full layered shell; LOD1 removes tiny tie details; LOD2 simplifies weave and straps; LOD3 preserves shield outline and rim.

## Collision Notes

Equipped collision disabled. World display uses simple convex or box collision.

## Animation Notes

Static mesh. Block/parry animations belong to character systems.

## Unreal Import Notes

- Unreal path: `/Game/Aerathea/Shields/Drakhar/SM_DKH_ReedShellShield_A01`
- Pivot: back grip center.
- Scale: centimeters.
- Sockets: optional `socket_relic_tie`.

## Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_DKH_ReedShellShield_A01/`
- Source: `SourceAssets/Blender/Kits/Drakhar/FieldGear/SM_DKH_ReedShellShield_A01/`
- Export: `SourceAssets/Exports/Kits/Drakhar/FieldGear/SM_DKH_ReedShellShield_A01/`
- Unreal: `/Game/Aerathea/Shields/Drakhar/SM_DKH_ReedShellShield_A01`

## Quality Gate Checklist

- Light field shield read is clear.
- Correct A04 Drakhar scale is used.
- Reed/shell/bone material language is consistent.
- Glow is sparing.
- LOD and collision plans are defined.
