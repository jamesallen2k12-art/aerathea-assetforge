# Aerathea Visual Canon Workflow

Last updated: 2026-06-30

## Purpose

Aerathea visual production now uses concept approval before DCC or Unreal implementation for subjective visual work. Concept art, source references, and generated exploration boards define the look. Blender and Unreal production must then match the approved visual target rather than inventing the final aesthetic during implementation.

## Core Rule

Approved concept images become visual canon.

An approved image can be a user-provided source concept, a selected variant from a generated exploration board, a cleaned reference, or a concept composite. Once Flamestrike approves it, the image must be registered in `docs/assets/VISUAL_CANON_REGISTRY.md` with a stable canon ID, scope, keeper features, cleanup requirements, and affected assets or kits.

## Required Flow

1. Gather relevant source concepts from `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`.
2. Inspect the source concepts visually before writing prompts, packages, or DCC instructions.
3. Create a grouped concept board when a look is not already locked.
4. Ask Flamestrike to approve, reject, or combine specific variants.
5. Register approved selections as canon anchors or canon variants.
6. Convert the canon selection into production package constraints.
7. Build DCC sources to match the canon target.
8. Compare DCC proof and Unreal capture against the canon image before presenting visual approval.
9. Move approved implementations through `docs/assets/CONCEPT_ART_TO_GAME_READY_ASSET_PIPELINE.md` before marking them fully game-ready.

## Batch Sizes

| Work type | Recommended batch size | Approval behavior |
| --- | ---: | --- |
| New visual language exploration | 8-12 concepts | Stop for Flamestrike selection |
| Small prop family variants | 6-10 concepts | Flamestrike selects favorites and requested combinations |
| Character/race/faction anchors | 4-8 concepts | Stop before locking silhouette, color, or identity |
| DCC implementation from approved canon | 1-3 assets | Technical work may proceed inside the canon target |
| Unreal review captures | 1-3 assets | Stop before final visual approval |

## Canon Statuses

- `candidate`: an image or variant is available for review but not approved.
- `approved anchor`: primary visual source for a race, faction, kit, or hero asset.
- `approved variant`: accepted variation that can produce child assets.
- `reference only`: useful for mood, material, scale, silhouette, or setting but not binding by itself.
- `needs cleanup`: potentially useful but too noisy, over-detailed, unclear, or off-style for direct production.
- `rejected`: explicitly not part of Aerathea visual canon.
- `superseded`: replaced by a newer approved canon entry.

## Production Requirements

Every package or implementation task that uses visual canon must record:

- Canon ID.
- Source image or generated board path.
- Approved variant labels or grid positions.
- Keeper features.
- Required cleanup or simplification.
- Disallowed features.
- Affected packages, meshes, materials, VFX, or review captures.

## Approval Gates

Stop for Flamestrike before:

- Marking a candidate image as an approved anchor or approved variant.
- Combining multiple variants into one final target.
- Changing final silhouette, color language, faction identity, race identity, or hero art direction.
- Continuing DCC/Unreal implementation when the current result no longer matches the canon target.
- Accepting inferred side/back design from a single source image as final visual lock.

## Current Blood Axe Correction

The current `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` implementation pass is blocked from further visual signoff until a Blood Axe cairn concept board is approved. The earlier Unreal capture read as an unpainted rock pile and is not visual canon.
