# A005 Visual Correction A05 Measurement Gate

Status: `authoritative measurement record ready for A05 contract`

Artifact classification: `authoritative`

Date: 2026-07-21

## Decision

`authoritative measurement record ready for A05 contract`

The source supports a bounded A05 replacement-base contract without creating
or presenting candidate geometry in this gate. The exact A04 plinth remains
the visual reference to preserve; the A04 base remains invalid as A05
construction authority.

## Controlling Measurements

- C002 upper course: `119.097222 x 77.647059 cm`
  from same-view ratios to the approved `140 x 110 cm` C004 anchors.
- C003 lower course: `134.652778 x 96.561086 cm`.
- A04 depth excess: C002
  `15.909091%`;
  C003 `7.703843%`.
- Exact top contact point deltas: CL002
  `[167, 183] px`; CL003
  `[188, 207] px`.
- Same-row exact top stations narrow away from their widest recorded rows;
  rectangular C002/C003 footprints are not source-authorized.
- Two-view course-height evidence intervals: C002
  `[8.235294, 11.666667]` cm, C003 `[14.583333, 15.235294]` cm,
  and C004 `[8.75, 11.529412]` cm. These are measurement bounds, not
  source-exact individual course heights.

## Color Correspondence

The exact top contact witnesses provide 96 byte-checked component-local RGB
samples with `0` mismatch. Step 14's exact RGB transfer rule remains in force.
A05 must correct component-local geometry and face ownership before UV
placement is evaluated; no source recoloring or compensating grade is
authorized.

## Preserved Blocks

- Fully closed source-owned C002/C003 contours.
- Source-authored centers and hidden contact closures.
- A unified cross-view pixel scale.
- Source-exact individual course heights.
- Physical cross-panel pixel identity.

These blocks do not prevent a later A05 construction contract from using the
approved production pivot, a clearly classified oval interpretation bounded
by the exact stations, and a 35 cm course allocation selected inside the
recorded two-view intervals.

## Evidence

- Manifest: `manifests/VISUAL_CORRECTION_A05_MEASUREMENT_AUDIT.json`
- Measurement-only review board:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualCorrection_A05_Measurement/SM_GIA_BloodAxeCairnstone_A005_A05_MEASUREMENT_ONLY_REVIEW.png`
- Board SHA-256: `e7275844c9ecda918a1838c2b1a164ba42133b29600fae0ec8e1117f80f218cb`

No geometry, candidate fill, inferred contour overlay, smoothing envelope, or
Unreal output was created.
