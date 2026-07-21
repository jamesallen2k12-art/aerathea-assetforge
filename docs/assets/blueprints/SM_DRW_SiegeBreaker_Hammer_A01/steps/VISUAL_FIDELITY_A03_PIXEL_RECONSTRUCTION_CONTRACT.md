# Siege Breaker Visual Fidelity A03 Pixel Reconstruction Contract

- Contract ID: `SB-VF-A03-PIXEL`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-21
- Approver: Flamestrike
- Approval statement: "I approve everything you have full authority and approval ... make the changes use the pixel perfect method and do whatever you need to do to create this 3d asset."
- Artifact status: `authoritative`

## Decision

Create a fresh, isolated A03 DCC reconstruction whose projected appearance is
measured against the approved concept rather than inferred from dimensions and
feature labels alone. Preserve the exact physical envelope and production
constraints, but replace the quarantined A01/A02 visual solution.

## Core Authority Order

1. Aerathea Core and Flamestrike's explicit A03 authority.
2. Exact numeric envelope and anchors from `asset_spec.json` and `dimensions_cm.csv`.
3. Primary projected visual authority: the large 3/4 concept render in `concept_sheet_style_reference.png`.
4. Secondary projected evidence: front, back, left, right, top, and bottom concept panels, only where internally consistent and compatible with the numeric envelope.
5. Supporting component and material specifications.
6. Bounded documented interpretation for hidden or contradictory surfaces.

The numeric envelope remains exactly `52 x 32 x 170 cm`. Source pixels control
the visible silhouette, component proportions, landmark placement, structural
layering, ornament distribution, and rendered-reference palette inside that
envelope. Conflicting panels are never averaged or silently combined.

## Required Execution Sequence

1. Hash and crop the primary and secondary source panels without modifying source pixels.
2. Record the pixel coordinate frame, silhouette bounds, component landmarks, visible ratios, and rendered-color samples.
3. Audit secondary panels for conflicts and classify each datum as usable, blocked, or reference only.
4. Build A03 from fresh geometry with zero A01/A02 geometry inputs.
5. Lock the comparison camera, crop, scale, orientation, resolution, and color-management transform.
6. Render matched source-view and orthographic evidence.
7. Measure silhouette, landmark, component proportion, and color-distribution error; iterate until the declared gates pass or an evidence block is proven.
8. Produce versioned Blender, UV/PBR, LOD, collision, FBX/GLB, manifests, audits, and review outputs.

## Pixel-Perfect Boundaries

- Source pixels, exact coordinates, exact boundaries, hashes, formulas, ratios, and sampled rendered colors are evidence.
- Concept pixels are rendered-reference colors, not direct Base Color/albedo authority.
- Pixel evidence does not determine invisible depth, backside construction, normals, roughness, metallic response, or lighting independently.
- Hidden construction must be documented as interpretation and must remain compatible with every non-conflicting source view.
- A01/A02 geometry, textures, and rendered forms are quarantined and may not be reused as A03 visual authority.
- General scripts may supply mechanical helpers only; they may not supply A01/A02 geometry decisions.

## Required Visual Gates

- Primary silhouette occupancy and aspect ratios match the measured 3/4 source target.
- Major landmark centers and component spans remain within declared pixel tolerances after registration.
- The head reads as two craggy dark runestone masses around a layered dwarven core.
- Metalwork reads as nested engraved architectural bracing, not a flat X-frame.
- Shaft and grip carry continuous authored engraving and dense leather wrapping.
- Pommel reads as compact, broad, and faceted.
- Rendered stone, bronze, steel, leather, and rune regions match the source palette hierarchy under the locked view transform.
- The exact numeric envelope, LOD, collision, material, texture, and clean-reimport gates pass independently.

## Completion Boundary

A03 may be classified only as a `DCC game-ready candidate` pending Flamestrike
visual approval. This contract does not authorize Unreal import, `Fully
game-ready` classification, or self-approval of final visual quality.
