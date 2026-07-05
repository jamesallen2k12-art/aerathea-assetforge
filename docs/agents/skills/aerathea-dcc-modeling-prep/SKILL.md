---
name: aerathea-dcc-modeling-prep
description: Prepare Aerathea DCC and Blender work. Use for Blender blockout scripts, image-to-geometry intake, scanline image capture, source asset folder creation, FBX export plans, DCC proof renders, scale checks, LOD source planning, collision proxy notes, and DCC-to-Unreal handoff validation.
---

# Aerathea DCC Modeling Prep

## Quick Start

1. Read the production package and modeling handoff before creating geometry.
2. For image-derived geometry, first create a lossless scanline capture with `Tools/DCC/scanline_image_capture.py` and confirm `pixel_exact=true`.
3. Use existing `Tools/DCC/build_*.py` patterns before inventing new scripts.
4. Keep first-pass geometry mid-poly, readable, and scale-validated.
5. Export to `SourceAssets/Exports/...` and keep Blender sources in `SourceAssets/Blender/...`.
6. Produce a proof render when the asset needs visual review.
7. For pixel-measured assets, run the strict pixel asset gate before presenting proof renders for approval.

## Scanline Intake Rule

Before deriving geometry, silhouettes, contours, measurements, masks, or texture guides from a raster reference:

```bash
python3 Tools/DCC/scanline_image_capture.py \
  --input path/to/reference.png \
  --out-dir path/to/asset/ScanlineCapture \
  --asset-id STABLE_ASSET_OR_REFERENCE_ID
```

Require `max_rgb_delta=0`, `changed_pixels=0`, matching target/rebuild pixel hashes, and `pixel_exact=true` in the manifest before treating scan-derived data as a production input. Keep the `.rgbscan.gz`, rebuilt PNG, difference PNG, and JSON manifest with the asset or reference package.

## Strict Pixel Asset Gate

When a DCC asset is built from calibrated scanline pixels or multi-view measured source images, do not present it as review-ready until an asset-specific geometry/color audit passes through:

```bash
python3 Tools/DCC/strict_pixel_asset_gate.py \
  --audit path/to/ASSET_GeometryColorGuidanceAudit.json \
  --generator path/to/build_asset.py \
  --out path/to/ASSET_StrictPixelGate.json
```

The gate must pass before opening or presenting proof renders for approval. If it fails, stop and fix the data path first. Treat these as blocking failures:

- source scanline evidence is not pixel exact
- visible source pixels differ from exported texture pixels
- atlas or material path resamples visible canon color
- contact gaps or unapproved center offsets exist between assembled pieces
- visible measured geometry is replaced by analytic approximations
- nearby-row search, fallback clamps, or averaging are used on visible measured geometry

Hidden or missing surfaces may use tagged inference or sample synthesis, but visible canon surfaces must remain exact unless Flamestrike explicitly approves a tolerance.

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
- scanline capture proof exists for image-derived geometry
- strict pixel asset gate passes for pixel-measured assets before visual approval
