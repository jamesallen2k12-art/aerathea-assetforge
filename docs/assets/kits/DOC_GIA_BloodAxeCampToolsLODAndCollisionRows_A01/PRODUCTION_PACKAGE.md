# DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01 Production Package

## 1. Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01`
- Asset type: Documentation-only LOD and collision policy row package; non-shipping
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeCamp.png#Review_LODCollisionRows_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: policy/review planning document; not a mesh, not an Unreal actor, not shipped content

This package defines non-shipping policy rows for LOD and collision expectations across Blood Axe buckets, rope coils, hooks, wedges, mallets, tie hardware, and utility clusters.

Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture. LOD and collision policy must preserve brutal camp readability without turning props into refined Giant civic tools or gameplay systems.

Guardrails: no-DCC, no-Unreal, no-startup, no-nav, no-encounter, no-workstation, no-loot, no-resource, no-material-instance, no-validator, no-capture, no-final-signoff, no-implementation-target.

## 2. Gameplay Purpose

This is a non-shipping LOD/collision policy document. It helps later packages avoid overbuilt collision, per-detail physics, and silhouette-damaging LOD reductions.

It does not create gameplay, runtime behavior, nav/pathfinding, encounters, workstations, loot, resources, economy systems, pickups, interactions, startup placement, captures, validators, meshes, materials, or final approval.

## 3. Silhouette Notes

LOD policy should preserve bucket/tub reads, rope coil masses, hook curves, wedge triangular profiles, mallet heads, and cluster footprints before keeping small cuts, rivets, rope fibers, scratches, or red paint chips.

Collision policy should outline simple display hulls only. It must not imply weapon traces, tripwires, pickup volumes, nav blockers, cover, traps, resource nodes, workstation use, or encounter logic.

## 4. Scale Notes

Use the validated Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

LOD/collision policy should ensure simplified forms remain readable beside the 442 cm and 470 cm baselines. Collision simplification must not become a gameplay scale claim or nav/pathfinding rule.

## 5. Materials and Color Palette

Policy rows should use the same review language as the parent kit: blackened iron, dark steel, scorched timber, thick rope, hide, scorched leather, soot, ash, mud, dull red ties, chipped red paint, and sparse non-graphic bone or horn.

Material color should support LOD readability, but this package does not create material instances or texture assets.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01` for the world of Aerathea. The design should emphasize non-shipping LOD0 through LOD3 and simple display-collision policy rows for hostile Giant camp tools, buckets, rope coils, hooks, wedges, mallets, tie hardware, utility clusters, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", preserved silhouettes, simplified hull callouts, no nav blockers, no gameplay volumes, Blood Axe hostile sub-faction identity, blackened iron, dark steel, scorched timber, rope, hide, soot, mud, dull red ties, and policy-only review use. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean non-shipping review board with LOD rows and collision diagrams clearly labeled as policy only. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## 7. Modeling Notes

No modeling is authorized. This document defines LOD/collision policy only and does not create DCC source, meshes, proxies, proof renders, FBX, collision, LOD source, Unreal Content, startup scenes, validators, captures, or implementation targets.

Future asset packages should use this policy to keep LOD reductions ordered and collision simple, but they must author their own budgets and proxy details under approved implementation tasks.

## 8. Texture and Material Notes

No texture or material assets are authorized. LOD policy should remove tiny texture-level detail before reducing primary silhouettes. Collision policy should not depend on material states.

This package does not create material instances, texture assets, ORM maps, emissive maps, shaders, or material graphs.

## 9. Triangle Budget

No triangle budget applies because this is a non-shipping documentation row package and not a mesh.

Policy target for represented future assets: reduce LODs by preserving silhouette first, then removing minor bevels, duplicate ties, extra coil turns, small chips, tiny rivets, pitting, scratches, and underside detail.

## 10. LOD Plan

Policy rows should require:

- LOD0: complete primary forms and readable Blood Axe material blocks.
- LOD1: 60-70 percent of LOD0; remove minor bevels, extra turns, small cuts, and backside detail.
- LOD2: 35-45 percent of LOD0; simplify interiors, hook bevels, wraps, chips, and underside surfaces.
- LOD3: 15-25 percent of LOD0; preserve primary silhouette, footprint, and broad material read.

No LOD meshes, LOD source files, validators, captures, or Unreal assets are created by this package.

## 11. Collision Notes

Policy rows should require simple display collision only:

- Buckets/tubs: one low-count hull or grouped boxes.
- Rope coils: one cylinder-like hull or simplified convex hull.
- Hooks: one simple box or hull around the set, not per hook point.
- Wedges: one box or wedge-like hull around the set.
- Mallets: one box or capsule around display footprint.
- Clusters: grouped hulls around major forms only.

Reject pickup collision, usable workstation volumes, resource triggers, loot outlines, nav blockers, encounter cover, per-rope collision, per-link collision, damage traces, trap volumes, destructible collision, startup placement collision, and collision proxies in docs-only rows.

## 12. Animation Notes

No animation is authored. LOD/collision rows are static policy references only and do not define physics, rope simulation, hanging motion, NPC routines, interaction prompts, VFX, audio, material-state timing, or startup behavior.

## 13. Unreal Import Notes

No Unreal import is authorized. This is not a Static Mesh, Blueprint Actor, Material Instance, texture asset, validator, capture setup, collision proxy asset, startup actor, or shipped review asset.

Future implementation must create its own LOD and collision assets under a separate approved task. This package only records policy.

## 14. Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01/`
- Production package: `docs/assets/kits/DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01/PRODUCTION_PACKAGE.md`
- Review document code: `DOC_GIA_BloodAxeCampToolsLODAndCollisionRows_A01`

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, global indexes, task board updates, material instances, texture assets, startup scene files, collision proxy files, or shipping assets from this package.

## 15. Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Is clearly non-shipping and policy-only.
- Remains docs-only with no-DCC/no-Unreal/no-startup/no-nav/no-encounter/no-workstation/no-loot/no-resource/no-material-instance/no-validator/no-capture/no-final-signoff/no-implementation-target guardrails.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Defines LOD and collision policy without creating collision proxies, validators, Unreal assets, or shipped content.
- Does not claim meshes, textures, material instances, captures, runtime behavior, final signoff, or first DCC target selection.
