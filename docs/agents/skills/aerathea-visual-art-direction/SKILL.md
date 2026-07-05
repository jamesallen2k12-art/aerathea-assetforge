---
name: aerathea-visual-art-direction
description: Cleanse Aerathea visual references and lock readable art direction. Use for noisy concept review, scanline-backed raster reference intake, rivet or micro-detail reduction, silhouette cleanup, prompt rewriting, faction visual standards, approval folders, or visual direction gates before production packages or DCC work.
---

# Aerathea Visual Art Direction

## Quick Start

1. Read `AGENTS.md` and the relevant race, creature, kit, or prop docs.
2. Inspect the source image before judging it.
3. For raster references that may drive geometry, masks, contours, or texture evidence, require a lossless scanline capture and pixel-exact rebuild proof.
4. Classify the reference as `approved anchor`, `variant`, `reference only`, `needs cleanup`, or `rejected`.
5. Protect Aerathea's style: strong silhouette, hand-painted surface detail, mid-poly readability, restrained emissive accents.
6. Remove or reduce visual noise before production: tiny rivets, excessive scratches, overglow, unreadable particles, dense spikes, and photoreal clutter.

## Scanline Reference Rule

Use `Tools/DCC/scanline_image_capture.py` for important raster references before treating pixel data as authoritative. Record the scanline manifest path and only call the reference pixel-authoritative when the manifest reports `pixel_exact=true`, `max_rgb_delta=0`, and `changed_pixels=0`.

## Output Contract

For each visual pass provide:

- art direction summary
- keeper features
- cleanup requirements
- silhouette/scale notes
- material/color notes
- approval question if the direction changes the asset identity
- production prompt or reference note
- scanline manifest path when pixel data drives later production

## Approval Gates

Stop for user approval when changing:

- race or faction identity
- final silhouette
- color language
- major VFX behavior
- final art direction for a hero asset
