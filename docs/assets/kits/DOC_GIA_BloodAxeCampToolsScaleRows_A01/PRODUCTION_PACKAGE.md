# DOC_GIA_BloodAxeCampToolsScaleRows_A01 Production Package

## 1. Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeCampToolsScaleRows_A01`
- Asset type: Documentation-only scale row package; non-shipping
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeCamp.png#Review_ScaleRows_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: policy/review planning document; not a mesh, not an Unreal actor, not shipped content

This package defines non-shipping scale row policy for Blood Axe camp tools and utility clusters. It exists to protect the validated Giant scale lock and prevent camp tools from drifting into humanoid prop scale.

Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture. Scale rows should show hostile raider camp utility, not peaceful Giant civic craft or refined highland settlement presentation.

Guardrails: no-DCC, no-Unreal, no-startup, no-nav, no-encounter, no-workstation, no-loot, no-resource, no-material-instance, no-validator, no-capture, no-final-signoff, no-implementation-target.

## 2. Gameplay Purpose

This is a non-shipping scale policy document. It helps later package authors and reviewers compare buckets, rope coils, hooks, wedges, mallets, tie hardware, and utility clusters against Giant baselines.

It does not create gameplay, runtime behavior, nav/pathfinding, encounters, workstations, loot, resources, economy systems, pickups, interactions, startup placement, captures, validators, meshes, materials, or final approval.

## 3. Silhouette Notes

Scale rows should show each tool type with a clean side silhouette and top footprint when relevant. Primary forms must remain readable beside the Giant baselines without relying on tiny texture details.

Policy target: buckets and tubs should read as Giant containers, rope coils as thick labor-scale coils, hooks as heavy blackened hardware, wedges as broad blocks, mallets as oversized tools, and clusters as low camp dressing rather than humanoid clutter.

## 4. Scale Notes

Use the validated Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Scale row policy targets:

- Buckets/tubs: 90-180 cm diameter, 80-160 cm tall.
- Rope coils: 120-260 cm diameter, 25-70 cm coil thickness.
- Hooks: 70-180 cm long.
- Wedges/chocks: 50-140 cm long, 25-70 cm tall.
- Mallets: 140-260 cm long, heads 55-120 cm wide.
- Utility clusters: 250-700 cm wide, 120-420 cm deep, 60-260 cm tall depending on row type.

This document does not change scale lock or approve shipped scale markers.

## 5. Materials and Color Palette

Scale rows should use neutral review lighting and readable material blocks: blackened iron, dark steel, scorched timber, rope, hide, scorched leather, soot, ash, mud, grime, dull red cloth ties, chipped red paint, and sparse non-graphic bone or horn.

Reject polished scale-display materials, bright UI colors, glowing outlines, blue rune markers, neutral/civilized Giant craft palettes, or excessive red coverage.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `DOC_GIA_BloodAxeCampToolsScaleRows_A01` for the world of Aerathea. The design should emphasize non-shipping scale rows for hostile Giant camp tools, female Giant baseline 442 cm / 14'6", male Giant baseline 470 cm / 15'5", oversized buckets, thick rope coils, heavy hooks, broad wedges, massive mallets, utility cluster footprints, clear centimeter callouts, Blood Axe hostile sub-faction identity, blackened iron, dark steel, scorched timber, rope, hide, soot, mud, dull red ties, and policy-only review use. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean non-shipping scale board with front and side rows, top footprints, and explicit non-shipping labels. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## 7. Modeling Notes

No modeling is authorized. This document defines scale policy only and does not create DCC source, meshes, proxies, proof renders, FBX, collision, LOD source, Unreal Content, startup scenes, validators, captures, or implementation targets.

Future visual scale boards, if approved separately, must remain non-shipping and must not change the 442 cm and 470 cm Giant baselines.

## 8. Texture and Material Notes

No texture or material assets are authorized. Scale rows should use simple material swatches only as review language if later visualized.

This package does not create material instances, texture assets, ORM maps, emissive maps, shaders, or material graphs.

## 9. Triangle Budget

No triangle budget applies because this is a non-shipping documentation row package and not a mesh.

Future represented assets must use their own package budgets. This document only records scale ranges and review expectations.

## 10. LOD Plan

No LODs are authored. Scale row policy should require future assets to show readable size and silhouette through LOD0-LOD3 without shrinking or changing the validated Giant scale relationship.

This package does not create LOD meshes, LOD source files, validators, captures, or Unreal assets.

## 11. Collision Notes

No collision is authored. Scale rows are not collision proxies, player blockers, nav markers, encounter markers, pickup volumes, workstation volumes, resource volumes, loot volumes, or startup placement guides.

This package does not create collision proxies or collision validation.

## 12. Animation Notes

No animation is authored. Scale rows are static policy references only and do not define physics, rope simulation, hanging motion, NPC routines, interaction prompts, VFX, audio, material-state timing, or startup behavior.

## 13. Unreal Import Notes

No Unreal import is authorized. This is not a Static Mesh, Blueprint Actor, Material Instance, texture asset, validator, capture setup, startup actor, or shipped scale marker.

Any future in-engine review scene requires a separate approval task and must remain non-shipping until explicitly promoted.

## 14. Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/DOC_GIA_BloodAxeCampToolsScaleRows_A01/`
- Production package: `docs/assets/kits/DOC_GIA_BloodAxeCampToolsScaleRows_A01/PRODUCTION_PACKAGE.md`
- Review document code: `DOC_GIA_BloodAxeCampToolsScaleRows_A01`

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, global indexes, task board updates, material instances, texture assets, startup scene files, or shipping assets from this package.

## 15. Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Is clearly non-shipping and policy-only.
- Remains docs-only with no-DCC/no-Unreal/no-startup/no-nav/no-encounter/no-workstation/no-loot/no-resource/no-material-instance/no-validator/no-capture/no-final-signoff/no-implementation-target guardrails.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Defines scale row policy without changing scale lock or approving shipped markers.
- Does not claim meshes, textures, collisions, LODs, validators, captures, Unreal actors, shipped assets, or final signoff.
