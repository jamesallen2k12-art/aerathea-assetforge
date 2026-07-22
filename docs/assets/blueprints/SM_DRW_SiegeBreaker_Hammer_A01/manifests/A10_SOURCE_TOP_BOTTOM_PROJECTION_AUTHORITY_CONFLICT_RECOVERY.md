# A10 Source Top/Bottom Projection-Authority Conflict Recovery

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-22
- Recovery status: `Blueprint block: source authority missing`
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

No other original-source axial top/bottom images exist under
`SourceAssets/Concepts/SiegeBreaker/`. Files named `top.png` and `bottom.png`
under the verified package's `generated/orthographic_true/` directory are old
DCC outputs classified `proof only`; they are not source authority and cannot
replace missing source evidence.

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

No option is selected by this recovery record.
