# Concept Art to Game-Ready Asset Pipeline

Last updated: 2026-07-04

Source intake: `/home/Flamestrike/Downloads/CONCEPT_ART_TO_GAME_READY_ASSET_PIPELINE.md`

## Purpose

This is the formal Aerathea pipeline for turning approved 2D concept art into functional Unreal Engine assets.

Core rule:

```text
Visual idea -> approved visual target -> production spec -> 3D form -> functional game object
```

A concept image is the visual target. It is not a game asset by itself.

## Status Vocabulary

Use these terms consistently in task packets, build status docs, and final reports.

| Status | Meaning |
| --- | --- |
| Concept candidate | Source image or generated variant exists but is not approved. |
| Visual canon | Flamestrike approved the concept, variant, or source image as a binding visual target and it is recorded in `docs/assets/VISUAL_CANON_REGISTRY.md`. |
| Production package ready | Asset brief, world role, scale, silhouette, material plan, triangle budget, LOD plan, collision plan, and Unreal notes exist. |
| DCC source candidate | Blender or other DCC source exists for review, but UVs, final textures, LODs, collision, or exports may still be incomplete. |
| DCC game-ready candidate | DCC source, FBX, UV/textures/material plan, LODs, collision proxy, scale, and proof renders exist. It is ready for Unreal import testing but not fully game-ready yet. |
| Unreal import candidate | Asset is imported into Unreal with materials, textures, LODs, collision, and review placement configured. |
| Gameplay validated asset | Asset has been tested in an Unreal gameplay or review map for scale, lighting, collision, LODs, materials, and expected behavior. |
| Approved library asset | Asset passed technical validation and Flamestrike aesthetic approval for its intended use. |

Do not call an asset fully game-ready just because it visually resembles the concept. Full game-ready status requires Unreal import, gameplay-map testing, validation, and approval.

## Required Pipeline

Every buildable race, creature, character, prop, building, weapon, armor piece, UI item, VFX item, or environment asset follows this order unless a task packet explicitly narrows scope.

1. Study the concept art.
2. Create or confirm the asset brief.
3. Define gameplay purpose and world role.
4. Define silhouette, scale, materials, colors, culture, and mood.
5. Create or infer front, side, back, and top design information.
6. Register approved concept selections as visual canon when Flamestrike approves them.
7. Convert the visual target into a production package.
8. Build a rough 3D blockout or DCC source candidate.
9. Test scale and silhouette early.
10. Create the detailed model or controlled mid-poly model.
11. Create the optimized low-poly game mesh.
12. Retopologize when needed.
13. UV unwrap.
14. Bake maps when useful.
15. Texture the asset.
16. Create or assign Unreal materials and material instances.
17. Rig if needed.
18. Animate if needed.
19. Add collision.
20. Create LOD0, LOD1, LOD2, and LOD3.
21. Export source meshes and textures.
22. Import into Unreal.
23. Build Blueprint or prefab setup if needed.
24. Test in the gameplay or review map.
25. Optimize.
26. Validate technically.
27. Stop for Flamestrike aesthetic approval when subjective visual quality is being locked.

## Single-Image Rule

One 2D concept image does not contain complete 360-degree geometry.

When only one view exists:

- Preserve the visible silhouette, proportions, color identity, signature details, and material language.
- Infer missing front, side, back, and top information in the production package.
- Treat side and back geometry as an art-direction interpretation until approved.
- Prefer generating or drawing turnaround views before final DCC work for hero assets, characters, creatures, buildings, and complex mechanical assets.
- Use camera projection only as a source-view fidelity tool, not as a substitute for full 3D design.

For simple static props, a single-image concept can produce a DCC game-ready candidate, but Unreal import and side/back approval are still required before full game-ready status.

## Pixel-Measured Mesh Rule

When an asset is built from calibrated scanline pixels or multi-view measured reference images, do not average panel measurements to hide disagreement between views.

- Convert each source edge from pixels to centimeters using that view's calibration.
- Preserve explicit source measurements for visible panels wherever a source view owns that edge.
- When adjacent views disagree at a shared corner, use a documented selection rule such as the outer measured min/max envelope, an approved source-priority edge, or a tagged inferred hidden-contact fill.
- Do not use cross-panel averaged width/depth profiles, smoothing, stretch strips, or detached projection shells as a final fix for visible seams.
- Record any selected edge rule in the build manifest and keep hidden or missing geometry tagged as inferred.

## Strict Pixel-Perfect Gate Rule

When a pass is intended to be pixel-perfect, validation is mandatory before visual approval.

Run an asset-specific geometry/color audit, then run:

```bash
python3 Tools/DCC/strict_pixel_asset_gate.py \
  --audit path/to/ASSET_GeometryColorGuidanceAudit.json \
  --generator path/to/build_asset.py \
  --out path/to/ASSET_StrictPixelGate.json
```

If the gate fails, the pass is not review-ready. Do not present proof renders as approval images until the blocking checks are fixed.

The gate must fail on:

- non-exact scanline evidence;
- visible source pixels that do not match exported visible texture pixels;
- Lanczos, bicubic, bilinear, or other filtered resampling on visible canon pixels;
- lit/material preview color drift when the task is color proofing;
- visible contact gaps, unapproved center offsets, or unapproved yaw/pitch/roll offsets between assembled pieces;
- measured contours replaced by analytic approximations such as ellipses or superellipses;
- fallback clamps, nearby-row search, smoothing, or averaging on visible measured geometry;
- stretch strips or detached shells used as final visible seam fixes.

Hidden-contact geometry, occluded faces, and missing pedestal fill may use tagged inference or sample-based synthesis, but those surfaces must be named in the manifest and kept separate from visible canon measurements.

## Multi-Part Registration Mark Rule

When a source template contains multiple physical asset pieces that must be reassembled into one 3D asset, add hidden, review-only, or non-shipping registration marks before scan capture.

- Give each physical piece its own registration identity, such as base, central stone, top plate, trim ring, cloth wrap, socketed prop, or hidden contact patch.
- Include orientation marks for front, back, left, right, top, and any intended yaw offset between pieces.
- Place marks where they can be read by the reconstruction workflow but removed, masked, or assigned to a non-rendering helper layer before final art.
- Use the marks to verify piece-to-piece orientation before welding, boolean joining, texture baking, or atlas packing.
- If registration marks are missing, treat cross-piece yaw, offsets, and hidden contact geometry as inferred until Flamestrike approves the assembly.

## Required Asset Brief

Every buildable asset must define:

- Asset name.
- Asset type.
- Game use.
- Engine target.
- Target style.
- Target scale.
- Target triangle count.
- Texture resolution.
- Material count target.
- Rigging requirement.
- Animation requirement.
- Collision type.
- LOD count.
- Required sockets.
- Required VFX.
- Required audio.
- Gameplay systems used.
- Notes and approval gates.

## Technical Requirements

Before an asset can be marked as a DCC game-ready candidate, it must have:

- Correct scale in centimeters.
- Ground or socket pivot appropriate to asset type.
- Optimized low-poly or mid-poly mesh.
- UVs suitable for the texture plan.
- Base Color, Normal, and ORM texture plan or maps.
- Emissive only when justified by magic, Aetherium, runes, eyes, lamps, portals, cores, or special effects.
- LOD0-LOD3 source or export plan.
- Simple collision proxy or collision plan.
- Correct naming and folder path.
- Proof render or review capture.
- Build/status documentation.

Before an asset can be marked as fully game-ready, it must also have:

- Unreal import completed.
- Materials and textures assigned.
- LODs assigned and checked.
- Collision validated.
- Scale validated against the intended character or environment.
- Runtime or review-map placement.
- Gameplay behavior, Blueprint, sockets, rig, animation, VFX, and audio validated when applicable.
- Performance checked for triangle count, material count, texture size, shader cost, and draw calls.
- Flamestrike aesthetic approval if final visual quality is being locked.

## Asset-Type Variants

Static prop:

```text
Concept -> package -> blockout/model -> UV -> texture -> collision -> LODs -> export -> Unreal import -> test -> approve
```

Weapon:

```text
Concept -> package -> model -> UV -> texture -> sockets -> traces/collision policy -> VFX/audio -> Unreal import -> combat test -> approve
```

Character:

```text
Concept -> turnaround -> sculpt/detail model -> retopo -> UV -> bake -> texture -> rig -> animate -> Unreal import -> gameplay test -> approve
```

Creature or mount:

```text
Concept -> anatomy study -> sculpt/detail model -> retopo -> rig -> animation set -> AI/collision setup -> Unreal import -> gameplay test -> approve
```

Building:

```text
Concept -> modular breakdown -> blockout -> kit pieces -> materials -> collision -> lighting -> navmesh test -> approve
```

Mek suit or vehicle:

```text
Concept -> mechanical breakdown -> blockout -> hard-surface model -> rig moving parts -> sockets -> VFX/audio -> gameplay test -> approve
```

## Validation Checklist

An asset is not approved for the asset library until these checks pass where applicable:

- Matches approved Aerathea visual style.
- Preserves the concept's core silhouette and material language.
- Uses approved visual canon or records why it is still a candidate.
- Scale is correct.
- Pivot is correct.
- Orientation is correct.
- Naming convention is correct.
- Folder path is correct.
- Textures are assigned.
- Materials are instanced where appropriate.
- Collision works.
- LODs work.
- No missing references.
- No broken normals.
- No flipped faces.
- No extreme texture sizes.
- No unnecessary material slots.
- Animation works if applicable.
- Rig deformation works if applicable.
- Sockets work if applicable.
- VFX attach correctly if applicable.
- Audio attaches correctly if applicable.
- Blueprint or prefab works if applicable.
- Gameplay interaction works if applicable.
- Performance is acceptable.
- Tested in gameplay or approved review map.
- Flamestrike approval recorded for subjective final visual quality.

## Approval Boundaries

Standing technical pipeline approval covers scoped implementation work when a task packet names ownership, allowed files, blocked files, dependencies, validators, and expected outputs.

Flamestrike approval is still required before:

- selecting or locking concept images as visual canon;
- changing final silhouette, color language, faction identity, race identity, or hero art direction;
- accepting inferred side/back design as final;
- final aesthetic approval;
- final combat feel, playstyle, encounter feel, economy, reward, or backend direction;
- marking a DCC candidate as a fully approved library asset.
