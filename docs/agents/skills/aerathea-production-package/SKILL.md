---
name: aerathea-production-package
description: Convert approved Aerathea concepts into build-ready production packages. Use for asset briefs, scanline-backed image reference intake, modeling handoffs, LOD plans, collision notes, texture/material plans, Unreal import specs, folder naming, and quality gates before DCC or Unreal implementation.
---

# Aerathea Production Package

## Quick Start

1. Read `AGENTS.md`.
2. Check `docs/assets/ASSET_INDEX.md` before creating a package.
3. If the source is a collage, split it into child assets before writing packages.
4. If production will derive geometry or texture evidence from a raster image, require a lossless scanline proof from `Tools/DCC/scanline_image_capture.py`.
5. For pixel-perfect or pixel-measured assets, require the DCC handoff to run `Tools/DCC/strict_pixel_asset_gate.py` before visual approval.
6. Follow the universal Aerathea output format.
7. Do not write DCC, Unreal, or final-art implementation as part of this role unless the task packet explicitly expands ownership.

## Required Sections

Every package or handoff must include:

- art direction summary
- gameplay purpose
- silhouette and scale notes
- materials and color palette
- concept prompt or source reference
- scanline capture manifest for image-derived geometry or texture references
- modeling notes
- texture and material notes
- triangle budget
- LOD plan
- collision notes
- animation notes
- Unreal import notes
- folder and naming recommendation
- quality gate checklist

## Handoff Rule

Write handoffs so a DCC or Unreal agent can execute without reinterpreting the source concept.

For raster-driven assets, include the scanline target image, `.rgbscan.gz` record, rebuilt image, difference image, and manifest path. The handoff should state whether the image is `pixel_exact=true`; do not ask DCC to infer geometry from a lossy or unverified reference.

For pixel-measured assets, the handoff must also state that proof renders are not review-ready until the DCC geometry/color audit passes `Tools/DCC/strict_pixel_asset_gate.py`. Blocking issues include visible texture color drift, filtered atlas resampling, contact gaps, unapproved offsets, analytic replacement of measured contours, fallback clamps, averaging, or stretch-strip seam fixes on visible canon surfaces.
