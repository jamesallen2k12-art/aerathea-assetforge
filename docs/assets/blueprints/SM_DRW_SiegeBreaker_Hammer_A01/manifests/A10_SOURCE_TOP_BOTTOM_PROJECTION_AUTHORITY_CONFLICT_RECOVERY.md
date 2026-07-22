# A10 Source Top/Bottom Projection-Authority Conflict Recovery

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-22
- Recovery status: `source identity resolved by A11 intake; pixel reconciliation block remains`
- Detected by: Flamestrike visual review

## Conflict

The following files carry `Top View` and `Bottom View` titles but are not axial
top/bottom orthographic projections under the established A09 frame, where the
hammer's `170 cm` length is the `Z` axis:

- `SourceAssets/Concepts/SiegeBreaker/siege_breaker_top_view.png`
  - SHA-256:
    `06d9cc7f78a4fe459a1f620e4787b53bf63399f7215bb9106a4e264749147d1c`
- `SourceAssets/Concepts/SiegeBreaker/siege_breaker_bottom_view.png`
  - SHA-256:
    `634dcf706a95a7f967b0c73d3c28fff318e3f91b2866e790369a57fa3b6e8d91`

Both sheets display the full `170 cm` longitudinal elevation and `52 cm` head
span. A true `+Z` or `-Z` axial projection cannot display the full shaft length.
Their titles and filenames therefore conflict with their visible projection.

## Repository Audit

At the time of the audit, no other original-source axial top/bottom images
existed under `SourceAssets/Concepts/SiegeBreaker/`. Files named `top.png` and
`bottom.png` under the verified package's `generated/orthographic_true/`
directory are old DCC outputs classified `proof only`; they are not source
authority and cannot replace source evidence.

## First Drift Action

Codex trusted the filenames and embedded titles, called the two sheets original
top/bottom views, and opened them in a temporary side-by-side viewer without
first verifying the projection against the established object axes.

## Affected Outputs and Classification

- temporary `/tmp/siegebreaker_source_top_bottom_review.html` viewer:
  `invalid`; its window was closed;
- the two source PNGs: preserved unchanged; `reference only for their visible
  full-length elevation content` and `invalid as axial top/bottom authority`;
- A06 Step 08 top/bottom measurement contracts, boards, and their downstream
  top/bottom authority claims: `invalid as axial top/bottom evidence`; retained
  as `proof only` for historical scan mechanics;
- A09 approved Blender source: `unaffected`; its recorded construction inputs
  were front, back, left, and concept sources, not these two sheets;
- A10 derived orthographic renders: `candidate / proof of the unchanged A09
  model only`; their `+Z/-Z` images are genuine Blender axial projections but
  are not source-matched top/bottom evidence.

## Last Known Core-Valid State

The exact hash-locked A09 Blender source remains approved for the visual result
Flamestrike reviewed. The exact A10 renders remain valid views of that unchanged
model. No source evidence currently authorizes the unseen axial end surfaces.

## Recovery Decision

Do not repair geometry or reinterpret the mislabeled sheets. Stop before
game-ready work. The block may be resolved only by one of these explicit
authorities:

1. Flamestrike supplies genuine axial top and bottom source views; or
2. Flamestrike reviews the A10 `+Z/-Z` derived views and explicitly approves
   those model-derived end surfaces as interpretation.

No option was selected by this original recovery record.

## A11 Recovery Update — Supplied Axial Sources

Flamestrike subsequently supplied two `1254 x 1254` PNGs and explicitly
declared Image 1 the top view and Image 2 the bottom view. They are preserved
under unambiguous filenames:

- `SourceAssets/Concepts/SiegeBreaker/siege_breaker_true_axial_top_view.png`
  — SHA-256 `aee612d9bed74e4f861576f926fe9d75de00f80dc416e3a6ba66a75247c00e98`;
- `SourceAssets/Concepts/SiegeBreaker/siege_breaker_true_axial_bottom_view.png`
  — SHA-256 `874a9e7c7713c7edbcf1030486d3988a54e8499ee697e316ec82a013fdb9d746`.

Flamestrike further directed: `use pixel measurements`. Therefore the printed
`52 x 32 cm` labels are preserved as `reference only` and do not control
geometry.

The established adaptive-luma greatest non-edge connected-component scan
measured these exact half-open object rectangles:

- top `[94, 330, 1106, 921]` = `1012 x 591 px`;
- bottom `[93, 330, 1106, 933]` = `1013 x 603 px`.

The source-identity block is resolved. A new fail-closed conflict remains:
registering either axial sheet to the approved A09 front-pixel head width
produces `43.875625705 cm` top depth or `44.722309348 cm` bottom depth, while
the approved A09 left-view pixel proportion produces `32.957619477 cm` depth.
Top and bottom also disagree by `12 px` in depth. No averaging, cropping, or
owner choice is authorized. Blender geometry remains stopped pending an
explicit pixel ownership or reconciliation rule from Flamestrike.

Evidence:
`A11_TRUE_AXIAL_TOP_BOTTOM_PIXEL_MEASUREMENT.json`; independent audit `19/19`
pass. No image generation, TRELLIS, image-to-3D, or Blender geometry change
occurred.
