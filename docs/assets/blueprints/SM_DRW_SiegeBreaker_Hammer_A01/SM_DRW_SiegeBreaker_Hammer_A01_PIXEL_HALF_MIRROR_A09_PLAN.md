# Siege Breaker Pixel-Half Mirror Visual-Match A09 Plan

- Plan ID: `SB-PHM-A09`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date approved: `2026-07-22`
- Status: `authoritative execution plan`
- Artifact target: `DCC source candidate`
- Unreal authority: `false`
- Fully game-ready authority: `false`

## Flamestrike Direction

Flamestrike selected `Visual Match`: build one complete physical half from
source-pixel measurements, mirror it across the center plane, and show the
completed Blender image. Blender is the only permitted visual or geometry
application. TRELLIS, image generation, generated views, and image-to-3D are
forbidden.

## Source Authority

1. The unchanged front source controls the visible front silhouette, component
   placement, and source-facing color:
   `SourceAssets/Concepts/SiegeBreaker/siege_breaker_front_view.png`.
2. The unchanged left source controls the depth profile.
3. The unchanged back source controls rear-facing visible color.
4. The unchanged concept source controls the three-quarter character check.
5. The original source pixels remain unchanged and are never replaced by a
   generated image.

## Visual-Match Scale Rule

The source pixel coordinate system is uniform in X and Z. Overall length is the
single physical scale anchor:

`source_scale = 170 cm / 1111 front-object pixels`

The resulting pixel-proportion envelope is:

- X width: `491 * 170 / 1111 = 75.130513051 cm`;
- Z height: `170 cm`;
- Y depth from the left crop: `215 * 170 / 1109 = 32.957619477 cm`.

The printed `52 cm` head-width label conflicts with the source image by
`44.481756%` and is superseded for A09 visual-match construction. It remains
preserved source evidence, not A09 geometry authority.

## Construction Rule

- Recompute masks directly from immutable sources.
- Build only the `X >= 0` half.
- Derive front/back surface positions from the left-view scanline depth profile.
- Preserve source-connected negative space where detected.
- Use source luminance only for bounded inward surface relief; relief may not
  extend the measured envelope.
- Mirror the source half in Blender at `X=0` with merge enabled.
- Do not load or consume any prior Siege Breaker candidate mesh or `.blend`.

## Proof Separation

The review package must contain both:

1. an untextured three-quarter geometry proof, where source projection cannot
   disguise incorrect volume or mirroring; and
2. a colored front visual-match render using unchanged source pixels on the
   source-facing surface.

The colored render cannot independently approve geometry. Technical audit
cannot grant visual approval.

## Stop Gate

Stop after opening the completed A09 review image for Flamestrike. Do not
export, create LODs/collision, enter Unreal, or classify the asset above
`DCC source candidate`.
