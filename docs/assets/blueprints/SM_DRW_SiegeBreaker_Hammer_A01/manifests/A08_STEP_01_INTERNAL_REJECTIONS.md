# A08 Step 01 Internal Rejections

## Pommel Attempt A01

- Date: `2026-07-22`
- Contract: `SB-BSR-A08-STEP01-POMMEL`
- Artifact status: `quarantined`
- Source status: unchanged and authoritative
- Historical geometry inputs: `0`
- Generation boundary: Blender only; no TRELLIS or other generative software

### Rejection Reasons

- The comparison camera clipped the candidate and did not present its complete
  silhouette.
- Review labels were outside or obscured by the framing.
- The blue focal rune read as one solid emissive diamond rather than the
  source's restrained outlined rune construction.
- Dark material response obscured the layered bronze and steel hierarchy.

### Preserved Evidence

- Blender source:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A08_BlenderOnly_Pommel_A01/SM_DRW_SiegeBreaker_Hammer_A01_A08_Pommel_A01.blend`
- Review render:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/review/A08_STEP_01_POMMEL_A01_REVIEW.png`
- Validation manifest:
  `manifests/A08_STEP_01_POMMEL_A01_VALIDATION.json`

Attempt A01 is not eligible for Flamestrike approval and may not be repaired
forward as an approved component. Attempt A02 may reuse only the Step 01
contract, immutable source, numeric bounds, and defect lessons; it may not load
the A01 `.blend` or mesh.

## Pommel Attempt A02

- Date: `2026-07-22`
- Contract: `SB-BSR-A08-STEP01-POMMEL`
- Artifact status: `quarantined`
- Source status: unchanged and authoritative
- Historical geometry inputs: `0`
- Generation boundary: Blender only; no TRELLIS or other generative software

### Rejection Reasons

- The outlined rune and material separation corrected their A01 defects.
- Blender's orthographic scale was incorrectly treated as vertical scale; at
  the `16:9` render aspect it controlled horizontal width, clipping the
  candidate vertically and placing all labels beyond the visible frame.
- The incomplete framing still prevents a valid source-versus-candidate
  decision.

### Preserved Evidence

- Blender source:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A08_BlenderOnly_Pommel_A02/SM_DRW_SiegeBreaker_Hammer_A01_A08_Pommel_A02.blend`
- Review render:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/review/A08_STEP_01_POMMEL_A02_REVIEW.png`
- Validation manifest:
  `manifests/A08_STEP_01_POMMEL_A02_VALIDATION.json`

Attempt A03 may change only the review camera scale/center and source display
window needed to show the complete existing candidate. It may not load either
prior `.blend` or change the source, numeric bounds, or component scope.

## Pommel Attempt A03

- Date: `2026-07-22`
- Contract: `SB-BSR-A08-STEP01-POMMEL`
- Artifact status: `quarantined`
- Numeric audit: `18.000 x 11.000 cm` gate passed
- Review-rig audit: complete candidate and labels visible
- Historical geometry inputs: `0`

### Rejection Reasons

- The outer diamond plate occupies too much of the body compared with the
  authoritative source.
- The emissive diamond is oversized and reads as a generic solid motif rather
  than the source's small restrained outlined rune.
- Upper and lower torus bands read as oversized horizontal bars.
- Bright full-body bracing hides the source-owned faceted pommel silhouette.

Attempt A04 may reduce only the visible plate/rune/band/brace proportions and
improve their material hierarchy inside the unchanged `18 x 11 cm` envelope.
It may not load A01-A03 geometry or advance to another component.

### A04 Fail-Closed Pre-Output Correction

The first A04 execution wrote no candidate because the numeric gate measured
`10.162675 cm` width after the oversized bands were reduced. The body profile
still declared an `11 cm` maximum radius pair, but its octagonal phase placed no
vertex on the X extrema. The builder was corrected to place source-visible
faceted-body vertices at exact `X=-5.5` and `X=+5.5`; the rejected bands were
not enlarged to manufacture the measurement pass.

## Pommel Attempt A04

- Date: `2026-07-22`
- Contract: `SB-BSR-A08-STEP01-POMMEL`
- Artifact status: `quarantined`
- Numeric audit: exact `18.000 x 11.000 cm` gate passed
- Historical geometry inputs: `0`

### Rejection Reasons

- The production review render failed to show the authoritative source plane
  and its labels, so no valid comparison decision was possible.
- A Blender-only `/tmp` diagnostic moved the source display closer to the
  camera and proved the source texture, crop, and labels were intact. The
  diagnostic is `proof only` and not a production review artifact.
- The focal rune remained a generic diamond outline instead of the source's
  small upper diamond connected to a lower open loop.

Attempt A05 may move only the review-only source plane/labels toward the camera
and replace the rune with that source-visible motif. It may not load A04
geometry, alter numeric bounds, or advance to another component.

## Pommel Attempt A05

- Date: `2026-07-22`
- Contract: `SB-BSR-A08-STEP01-POMMEL`
- Artifact status: `quarantined`
- Numeric audit: exact `18.000 x 11.000 cm` gate passed
- Review-rig audit: authoritative source and complete candidate visible
- Rune audit: linked upper-diamond/lower-loop motif present
- Historical geometry inputs: `0`

### Rejection Reasons

- The visible side-panel segmentation around the focal shield is absent.
- Source-visible rivets and small forged attachment beats are absent.
- The focal shield's outer frame reads as bright generic bronze rather than the
  source's cooler steel-edged plate over warmer structural metal.

Attempt A06 may add only the visible side-panel frames and rivets and correct
the focal shield's metal hierarchy. It may not change the silhouette, numeric
bounds, rune, source, hidden surfaces, or component scope.
