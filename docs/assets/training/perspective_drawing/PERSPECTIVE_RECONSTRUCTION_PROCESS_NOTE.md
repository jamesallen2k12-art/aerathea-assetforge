# Perspective Reconstruction Process Note

Date: 2026-07-04

Purpose: preserve the working lessons from the P12-P17 perspective reconstruction experiments so the next session resumes from the actual process state, not from memory.

## Current Status

- `P12` fixed the high-resolution overlay ratio issue for multi-reference perspective boards.
- `P13` applied the ratio-safe high-resolution X/Y/Z method to the LACMA Gothic Cathedral reference.
- `P14` separated global and local crop measurements, but still looked too much like a measurement-overlay board.
- `P15` tested roughly 10x measurement/reference density. It added some clarity but not enough to prove raw density is the right solution.
- `P16` is rejected. It jumped from evidence into hand-curated semantic scaffold geometry and produced fake structure disconnected from the source.
- `P17` is the current unreviewed WIP correction. It is evidence-locked: visible strokes must come from detected source segments, equation extensions, endpoint dots, or X/Z line intersections.

## Process Lessons

1. Raw reference count helps only slightly.
   - Increasing Hough lines, VP candidates, and visible references can reveal more source evidence.
   - It does not automatically fill missing structure or produce a clean reconstruction.

2. Ratio discipline is mandatory.
   - Every detected endpoint must be normalized against the exact processing width/height used during extraction.
   - Do not draw overlays with a default processing size after increasing extraction resolution.

3. Do not invent semantic structure too early.
   - Do not hand-draw arches, curves, columns, or floor grids unless they are traceable to measured source evidence or explicitly marked as inference.
   - P16 failed because it looked like a guessed diagram, not a reconstruction.

4. Evidence layer must come before semantic labels.
   - First produce a source-derived evidence layer.
   - Then label or simplify the approved evidence layer into semantic scaffold form.

5. Local crops are useful, but only if they produce source-derived features.
   - Crop panels should isolate floor grid, columns, arches, arcade, and vault ribs.
   - Crop panels should not become decorative zooms or guessed layouts.

## Required Workflow Going Forward

Use this sequence for the next perspective reconstruction attempt:

1. Review `P17`.
   - Open `docs/assets/training/perspective_drawing/P17_LACMAGothicCathedralEvidenceLockedReconstructionBoard.png`.
   - Judge whether the evidence-locked layer is clearer than P15.

2. If P17 is rejected:
   - Do not increase density again by default.
   - Improve line classification, confidence filtering, and crop layout.
   - Keep all drawn strokes evidence-locked.

3. If P17 is acceptable:
   - Build `P18` as the first labeled semantic pass.
   - P18 may label floor grid, column families, arch families, bay spacing, and vault ribs.
   - P18 must trace from P17 evidence, not from hand-guessed geometry.

4. Only after P18 is approved:
   - Apply the evidence-locked plus semantic-label process to simpler primitives.
   - Then return to Blood Axe cairn stones using the primitive-to-cairn ladder.

## Hard Rules

- Do not promote rejected boards as baseline.
- Do not treat a dense overlay as a clean reconstruction.
- Do not treat a clean diagram as valid unless each structural stroke can be traced back to source evidence or explicitly marked as inference.
- Do not modify Codex skills yet. This is project process knowledge, not a general reusable skill, until the process proves itself on at least one approved reconstruction.

## Morning Resume Step

Open and review:

`docs/assets/training/perspective_drawing/P17_LACMAGothicCathedralEvidenceLockedReconstructionBoard.png`

Then decide:

- Accept P17 as evidence layer and build P18 labeled semantic pass.
- Or reject P17 and refine evidence extraction/filtering before any semantic redraw.
