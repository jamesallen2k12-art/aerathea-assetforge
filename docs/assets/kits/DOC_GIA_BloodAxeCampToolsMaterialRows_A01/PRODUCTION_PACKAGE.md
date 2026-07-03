# DOC_GIA_BloodAxeCampToolsMaterialRows_A01 Production Package

## 1. Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeCampToolsMaterialRows_A01`
- Asset type: Documentation-only material policy row package; non-shipping
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeCamp.png#Review_MaterialDisciplineRows_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: policy/review planning document; not a mesh, not a material instance, not an Unreal actor, not shipped content

This package defines non-shipping material-discipline policy rows for Blood Axe camp tools. It protects the material language of blackened iron, dark steel, scorched timber, thick rope, hide, leather, soot, ash, mud, dull red ties, chipped red paint, and sparse non-graphic bone or horn.

Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture. Material rows must reject blue-gray cave-town masonry, refined stoneworker craft, warm hearth presentation, restrained blue runes, peaceful highland civic identity, and neutral Giant culture as the baseline read.

Guardrails: no-DCC, no-Unreal, no-startup, no-nav, no-encounter, no-workstation, no-loot, no-resource, no-material-instance, no-validator, no-capture, no-final-signoff, no-implementation-target.

## 2. Gameplay Purpose

This is a non-shipping material policy document. It helps later reviewers prevent material drift, emissive creep, overuse of red, polished finish creep, and culture drift across Blood Axe camp tools.

It does not create gameplay, runtime behavior, nav/pathfinding, encounters, workstations, loot, resources, economy systems, pickups, interactions, startup placement, captures, validators, meshes, material instances, texture assets, or final approval.

## 3. Silhouette Notes

Material rows should support silhouette readability by keeping broad value separation between dark metal, scorched wood, rope/hide, mud/ash, and dull red ties. Materials must reinforce primary forms instead of covering them with tiny high-contrast noise.

Policy target: broad hand-painted wear, strong baked-AO style depth, and restrained faction accents. Reject noisy micro-scratches, dense rivet fields, glowing outlines, UI-like red marks, or material patterns that obscure bucket, coil, hook, wedge, mallet, and cluster silhouettes.

## 4. Scale Notes

Use the validated Giant scale lock for material review boards:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Material rows are policy-only and do not change scale lock. Any future material review board should show material swatches on forms sized for the 442 cm and 470 cm Giant baselines, not humanoid props.

## 5. Materials and Color Palette

Approved Blood Axe camp-tools material language:

- Blackened iron and dark steel for hooks, rims, rings, wedge faces, bands, and chain accents.
- Scorched timber and rough boards for buckets, handles, mallets, and chocks.
- Thick rope, hide lashings, scorched leather, dirty cloth ties, and sinew wraps.
- Soot, ash, mud, oil-dark stains, grime, broad hand-painted wear, and chipped red paint.
- Dull Blood Axe red as restrained ties, warning marks, or chipped paint only.
- Sparse non-graphic bone or horn as secondary hostile accent only.

Rejected baseline language: default emissive, blue runes, bright magic, polished civic metal, warm hearth craft, blue-gray civilized Giant stone, refined stoneworker tools, clean highland materials, high-saturation red coverage, readable text labels, loot shine, and UI marker colors.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `DOC_GIA_BloodAxeCampToolsMaterialRows_A01` for the world of Aerathea. The design should emphasize non-shipping material discipline rows for hostile Giant camp tools, blackened iron, dark steel, scorched timber, thick rope, hide lashings, scorched leather, soot, ash, mud, grime, dull Blood Axe red ties, chipped red paint, sparse non-graphic bone or horn, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", no default emissive, no blue runes, no neutral/civilized Giant cave-town materials, and policy-only review use. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, and MMO-friendly production design. Present it as a clean non-shipping material board with approved and rejected swatches, broad-value examples, and micro-detail limits. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## 7. Modeling Notes

No modeling is authorized. This document defines material policy only and does not create DCC source, meshes, proxies, proof renders, FBX, collision, LOD source, Unreal Content, startup scenes, validators, captures, material instances, texture assets, or implementation targets.

Future assets should model primary forms and use material/texture work for tiny rivets, scratches, rope fibers, cloth weave, stitching, pitting, soot speckles, ash flecks, mud flecks, wood grain, and chipped paint.

## 8. Texture and Material Notes

No texture or material assets are authorized by this package. It defines future review policy for:

- Base Color / Albedo readability.
- Normal-map restraint for rope, wood, leather, metal pitting, and chipped paint.
- Packed ORM discipline for rough blackened metal, mud, leather, rope, and dull cloth.
- No baseline emissive map.
- No material instance creation in this task.

Future texture sets should keep Blood Axe red sparse and avoid turning every prop into a red faction icon.

## 9. Triangle Budget

No triangle budget applies because this is a non-shipping documentation row package and not a mesh.

Policy note: material detail should reduce the need for modeled micro-detail. Tiny rivets, scratches, fibers, stitch lines, pitting, soot, ash, and chipped paint belong in texture/normal work, not triangle-heavy geometry.

## 10. LOD Plan

No LODs are authored. Material policy should require broad material blocks to remain readable at LOD3 while tiny texture details are allowed to fade.

Future assets should preserve dark metal, scorched wood, rope/hide, mud/ash, and dull red accent separation through LOD0-LOD3. This package does not create LOD meshes, validators, captures, or Unreal assets.

## 11. Collision Notes

No collision is authored. Material rows do not define pickup collision, workstation volumes, resource triggers, loot outlines, nav blockers, encounter cover, damage traces, trap volumes, destructible collision, collision proxies, or startup placement collision.

Material variation must not imply gameplay states without a separate approval-gated task.

## 12. Animation Notes

No animation is authored. Material rows do not define animated emissive states, heat pulses, VFX, audio, material-state timing, physics, rope simulation, NPC routines, interaction prompts, loot states, workstation states, or startup behavior.

## 13. Unreal Import Notes

No Unreal import is authorized. This is not a Static Mesh, Blueprint Actor, Material Instance, texture asset, material graph, validator, capture setup, startup actor, or shipped review asset.

Any future material instance or texture asset requires a separate implementation task. This package only records policy.

## 14. Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/DOC_GIA_BloodAxeCampToolsMaterialRows_A01/`
- Production package: `docs/assets/kits/DOC_GIA_BloodAxeCampToolsMaterialRows_A01/PRODUCTION_PACKAGE.md`
- Review document code: `DOC_GIA_BloodAxeCampToolsMaterialRows_A01`

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, global indexes, task board updates, material instances, texture assets, material graphs, startup scene files, or shipping assets from this package.

## 15. Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Is clearly non-shipping and policy-only.
- Remains docs-only with no-DCC/no-Unreal/no-startup/no-nav/no-encounter/no-workstation/no-loot/no-resource/no-material-instance/no-validator/no-capture/no-final-signoff/no-implementation-target guardrails.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Defines material policy without creating material instances, texture assets, material graphs, validators, captures, Unreal actors, or shipped assets.
- Does not claim final visual approval, implementation readiness, runtime behavior, material implementation, or first DCC target selection.
