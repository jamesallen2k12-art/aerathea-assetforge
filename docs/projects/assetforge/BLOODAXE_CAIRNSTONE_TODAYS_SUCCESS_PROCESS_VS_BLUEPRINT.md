# Blood Axe Cairnstone: Today's Successful Process vs Blueprint

Date: 2026-07-04

This sheet reconstructs the process from today's conversation, not from late-pass file names. The goal is to recover the method that got the cairnstone close to pixel-perfect before later contaminated generator changes pushed us away from it.

## The Process That Was Working

1. Start from the approved visual source, not a failed generated output.
   - We rejected showing original/perspective-line images as if they were generated results.
   - We kept returning to the most successful approved visual result before adding new methods.

2. Reject inference that does not visibly improve the image.
   - The inference pass was tried and judged not useful.
   - The lesson was: do not add a technique because it sounds advanced; only keep it if visual evidence proves it helps.

3. Use a telescope/interferometer mindset for structure.
   - Break the image into ordered areas.
   - Analyze local sections.
   - Reassemble edges in the correct grid/order.
   - The important rule was local measurement plus global reassembly, not freeform guessing.

4. Use scanline capture as the detail foundation.
   - Line-by-line pixel color recording and rebuild proved it could recreate the image exactly.
   - The scanline result was identical.
   - This became the strongest proof method because it captured all visible detail.

5. Apply scanline data to the cairnstone source views.
   - Front, back, left, right, and top views should be treated as measured source data.
   - If any view is uncertain, rescan and verify it before geometry.

6. Establish the pixel-to-measurement formula before geometry.
   - Count pixels in the source image.
   - Use printed/known dimensions from the same source image.
   - Convert pixels to centimeters.
   - Convert centimeters to polygon vertex positions.
   - This is the core "pixel-perfect measurement" rule.

7. Separate measured visible data from inferred hidden data.
   - Visible cairnstone surfaces must come from front/back/left/right/top source views.
   - Hidden pedestal/base areas may be inferred only because they are physically occluded.
   - Inference must not overwrite visible measured data.

8. Use sample-based texture synthesis only for missing hidden material.
   - The missing pedestal area can be filled by sampling matching visible pedestal pixels.
   - This is a texture brush / sample-based synthesis rule.
   - It is for hidden or missing material only, not visible canon surfaces.

9. Treat polygons as measured geometry that controls screen pixels.
   - The working idea was: measured source pixels define polygon size, position, and UV/color ownership.
   - Geometry determines which screen pixels are filled; textures determine their color.

10. Build side/corner geometry from exact measurements.
   - Voids at side joins are measurement/alignment failures.
   - The fix is exact sizing, correct edge loops, and exterior-only welding.
   - Do not use strip patches, stretch passes, detached shells, or visual cover-ups as final geometry.

11. Weld only the exterior edge that is actually visible.
   - Interior/contact edges are not exterior seams.
   - Welding the wrong edge creates the exact failure we later saw: pieces look pushed apart or interior edges get joined.

12. Use no averaged measurements.
   - The user rule was clear: clean, specific, pixel-perfect measurements only.
   - If views disagree, report the disagreement and choose a declared rule.
   - Do not average the disagreement away.

13. Check tilt, pitch, yaw, roll, and orientation.
   - Slight inward tilt or wrong yaw can create visible edge mismatch.
   - The base/support is oval, not circular, so orientation and centering matter.
   - Top-down source alignment is the strongest orientation check.

14. Use hidden orientation marks between asset pieces.
   - Orientation marks prevent reassembly drift.
   - They must be non-shipping and hidden from export/review renders.

15. Let the top-down image control registration.
   - The top overlay was judged perfect.
   - That means top-down source measurement is the registration anchor for footprint, orientation, and center.

16. Stop before changing geometry.
   - Changes must be discussed first.
   - If a problem appears, show the evidence, explain the cause, propose the fix, then wait.

17. Start fresh when contamination appears.
   - Fresh start means original source data and clean generator logic.
   - A later failure happened because only the data was fresh while old generator assumptions came forward.
   - A001 must be a true clean slate.

## How This Maps To The Blueprint

| Conversation Process | Blueprint Match | Notes For A001 |
|---|---|---|
| Approved source first | Matches Source Hierarchy | Original source template only. No old generated image as source. |
| Full scanline capture | Matches Lossless Scanline Capture | Full image scan first, then crops. `changed_pixels=0`, `max_rgb_delta=0`. |
| Pixel-to-measurement formula | Needs to be treated as a hard geometry rule | Formula-derived crops, masks, component splits, scale, center, and contact positions. |
| Multiview source data | Matches Source Decomposition | Front/back/left/right/top each own the surfaces they show. |
| Visible measured vs hidden inferred | Matches Inferred Surface Fill | Inference only for hidden/missing areas. |
| Texture brush for pedestal | Matches sample-based texture synthesis | Only hidden pedestal/base material, never visible source surfaces. |
| Pixel-to-polygon geometry | Matches Geometry Construction | Polygon vertices must be derived from measured source pixels or declared formula constraints. |
| Exterior seam welding | Matches Exterior Edge Weld | Weld exterior perimeter only. Do not weld/contact-bridge interior edges. |
| No averaged measurements | Matches Disagreement Rule | If views disagree, stop and declare source priority/envelope/override. |
| Pitch/yaw/roll checks | Matches Component Alignment | Must be validated before render. |
| Hidden orientation marks | Matches Component Alignment and Visual Review Orientation | Required for separable components. |
| Top-down registration | Matches Coordinate Frame and Component Alignment | Top view owns footprint/orientation unless a stricter source says otherwise. |
| Discuss fixes first | Matches Change Declaration Rule | No silent geometry/contact/UV/material changes. |
| Fresh clean slate | Now covered by Fresh Pass Rule | Do not copy prior failed asset-specific generator logic. |

## What The Blueprint Adds

1. The hard validation gate records failures formally.
2. Review presentation requires actual images to be opened.
3. UV/atlas ownership is explicit.
4. Component lineage is explicit.
5. Unreal handoff status vocabulary is explicit.

## What The Blueprint Must Preserve From Today's Winning Method

1. Scanline exactness is the first proof, not a later audit.
2. Pixel-perfect measurement formula controls geometry.
3. Diagnostic masks do not own geometry.
4. Formula-derived component masks own geometry.
5. Printed dimensions from the source drive cm-per-pixel scale.
6. Top-down source owns footprint, centering, and orientation.
7. Side views own visible side profiles and texture ownership.
8. Missing hidden areas use tagged sample-based texture synthesis only.
9. Exterior seams are solved by measured alignment and correct welding.
10. No averaging, stretching, patching, hidden drops, or inherited fixes.

## A001 Working Foundation

A001 should not recreate the late broken generator. It should recreate the successful method:

1. Full scan the original source.
2. Verify exact scanline rebuild.
3. Derive view crops from measured source layout.
4. Derive geometry masks from pixel-to-cm formulas.
5. Record component measurement contracts.
6. Build support and primary object from separate formula-owned measurements.
7. Map visible textures from exact source pixels.
8. Fill only hidden missing areas with tagged sampled texture.
9. Validate orientation marks, center, yaw, pitch, roll, contact, and exterior welds.
10. Render all angles.
11. Run visual coherence check.
12. Open the review image for evaluation.

## Bottom Line

The Blueprint is close to the method that worked, but the method from today's conversation makes one point sharper:

Geometry must be owned by pixel-perfect measurement formulas, not by threshold cleanup, old generator behavior, or visual guesswork.

That is the foundation A001 needs.
