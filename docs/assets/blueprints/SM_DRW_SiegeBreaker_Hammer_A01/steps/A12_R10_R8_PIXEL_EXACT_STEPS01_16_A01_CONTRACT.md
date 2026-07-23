# A12 R10 R8 Pixel-Exact Steps 01-16 A01 Contract

- Date: `2026-07-23`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract ID: `SB-CR-STEPS01-16-R8-PIXEL-EXACT-A01`
- Process authority:
  `SB-CR-STEPS01-16-A06-POC`
- Status: `authorized by Flamestrike`
- Required sequence:
  `01 -> 02 -> 03 -> 04 -> 05 -> 06 -> 07 -> 08 -> 09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16`
- Maximum result:
  `DCC game-ready candidate pending Flamestrike final visual approval`
- Unreal / Fully game-ready authority:
  `false / false`

## Flamestrike Direction

Flamestrike rejected the preceding correct-axis two-hammer package because its
images were stretched. Flamestrike explicitly directed Codex to:

1. take the new orthographic images;
2. complete a scanline pixel-for-pixel scan of the hammer from every side;
3. derive the dimensions from that new image evidence;
4. take the new dataset through yesterday's documented sixteen-step process
   exactly;
5. substitute only the new image data for the old data; and
6. present the completed final image for approval.

This is the one end-to-end execution authority permitted by the authoritative
sixteen-step plan. Routine intermediate approval is not required when every
deterministic gate passes and no uncovered authority conflict occurs.

## Governing Truths

- The six new R8 orthographic PNGs are the immutable metric and color-pixel
  sources for this run.
- The registered perspective concept remains style reference only and cannot
  override a new orthographic pixel.
- Overall length `170 cm` is the approved external scale anchor.
- Every other overall or component dimension is an observed consequence of
  the new pixels and declared uniform transforms.
- Printed dimension annotations are evidence text, not permission to move,
  stretch, compress, or resample the depicted hammer pixels.
- Exact full-image scanlines and exact selected-object scanlines must preserve
  every source RGB value and location.
- The right-image rotational center is the proven diamond-center edge
  `x=557`.

## Mandatory No-Stretch Invariant

For each complete source view there is exactly one uniform pixel-to-world
scale. Within a view:

`scale_x = scale_y`.

The following are forbidden:

- forcing unequal source halves into one equal target half-depth;
- separate scale factors for rune-side and metal-center-piece halves;
- separate scale factors for head, coupler, shaft, ferrule, grip, collar,
  pommel, or terminal-cap image regions;
- resampling a source crop as construction input;
- fixed-segment nearest-pixel sampling that skips or repeats source pixels;
- changing source aspect ratio;
- using target bounds to replace an observed result;
- smoothing or visually fitting a measured contour.

If the two right-image halves contain different pixel spans, their completed
rotated candidates must retain different observed depths. They may not be
normalized to equal depth.

## Cylinder-Wrapping Rule

The handle uses the previously approved half-cylinder mapping:

`theta(U)=-pi/2+pi*U`, `U in [0,1]`

`X=r(z)cos(theta)`

`Y=r(z)sin(theta)`.

Each retained source-pixel column owns its exact proportional `U` interval.
The flat-diameter-to-half-circumference factor is exactly `pi/2`. The wrap may
change planar distance into cylindrical arc distance only through that
declared formula; it may not discard, duplicate, or independently normalize
source columns.

## New Source Set

Source root:

`Saved/AssetForgeResearch/SiegeBreaker/A12_R8_SixViewGeneration/VisualReference_A01/`

- Front SHA-256:
  `9a34588afd4fef32001cd9cb2115699e7506ef1e90331c19f4d32483c60aab8c`
- Back SHA-256:
  `f09dd1ad3978f39e10ecee8ea7efa84336520f0cea4921fe3c410dfd04019694`
- Left SHA-256:
  `7215495802065bb1907ec67f46e6f7c622b9beaf768eb710a5fc12880a6b1cc5`
- Right SHA-256:
  `58f3199babbcf9323751d04f0ffafa4316048243cf2f39992cdb6b04176306e8`
- Top SHA-256:
  `be3e0b70de7a6e4fad025315f22feb21dc948ea9c3e7efb0adb63a983f190f9c`
- Bottom SHA-256:
  `d2a32732fd480a0556e882e304bcfbff1dd82d0a913ad4c36117109406de988e`

## Step Substitution Boundary

The process, gates, authority order, state transitions, evidence separation,
artistic-soul checks, DCC requirements, material requirements, LOD/collision
requirements, clean reimport, reproducibility tests, and final decision remain
those of `SB-CR-STEPS01-16-A06-POC`.

Only these data fields may change:

- source paths and hashes;
- decoded pixels and scanline records;
- exact object rectangles and memberships;
- centers, stations, contours, intervals, component observations, and colors
  directly measured from the new sources;
- dimensions and ratios calculated from those observations;
- geometry, UV, texture, material, LOD, collision, and render outputs
  deterministically generated from the new approved records.

Old construction geometry, transformed crops, masks, UVs, textures, and
rendered candidates are forbidden inputs.

## Candidate Boundary

The prior explicit two-hammer comparison remains in scope:

1. rune-side right-image half `[557,668)`;
2. metal-center-piece right-image half `[418,557)`.

Each candidate uses its own observed source span, one common right-view scale,
and exactly one:

`Rz(180 degrees): (X,Y,Z)->(-X,-Y,Z)`.

Run A and Run B reproducibility tests apply separately to each candidate; they
are clean repeats, not names for the two source-half variants.

## Mandatory Audits

- six full-image RGB scanline round trips:
  `changed_pixels=0`, `max_rgb_delta=0`;
- six complete-hammer selected-pixel/color scanline round trips:
  exact membership and RGB equality;
- exact source rectangles, centers, transitions, and component stations;
- one uniform scale per complete view;
- scale-X equals scale-Y inside every view;
- no candidate-specific pixel scale;
- source-pixel coverage with no omitted or multiply owned construction pixel;
- exact `x=557` right-image bisection;
- one Rz180 completion;
- exact `pi/2` handle wrap;
- direct saved-file geometry, UV, texture, material, LOD, collision, export,
  reimport, render, and reproducibility validation;
- independent validator may not trust builder booleans or expected values.

## Stop

After both Step 16 candidate variants independently pass and the final
comparison image is opened visibly, stop for Flamestrike:

`approve / select / revise / reject / blocked`.
