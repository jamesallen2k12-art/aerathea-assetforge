---
name: aerathea-dcc-modeling-prep
description: Prepare Aerathea DCC and Blender work. Use for Blender blockout scripts, source asset folder creation, FBX export plans, DCC proof renders, scale checks, LOD source planning, collision proxy notes, and DCC-to-Unreal handoff validation.
---

# Aerathea DCC Modeling Prep

## Quick Start

1. Read the production package and modeling handoff before creating geometry.
2. Use existing `Tools/DCC/build_*.py` patterns before inventing new scripts.
3. Keep first-pass geometry mid-poly, readable, and scale-validated.
4. Export to `SourceAssets/Exports/...` and keep Blender sources in `SourceAssets/Blender/...`.
5. Produce a proof render when the asset needs visual review.

## Ownership

Allowed by default:

- `Tools/DCC/`
- `SourceAssets/Blender/`
- `SourceAssets/Exports/`
- DCC proof outputs under `Saved/Automation/`
- asset-specific modeling handoff updates when assigned

Do not edit Unreal binary assets, startup scene validators, or global indexes unless assigned.

## Required Checks

- scale matches approved race/asset anchor
- pivot and snap points are documented
- LOD0-LOD3 plan exists
- collision proxy plan exists
- material slots match the package
- no tiny modeled rivet or micro-detail forests
