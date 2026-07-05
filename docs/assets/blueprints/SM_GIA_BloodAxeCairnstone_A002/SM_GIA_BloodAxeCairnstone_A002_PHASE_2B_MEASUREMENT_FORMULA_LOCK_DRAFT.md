# SM_GIA_BloodAxeCairnstone_A002 Phase 2B Measurement Formula Lock Draft

Status: `A002 measurement formula lock draft; geometry not authorized`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_1_SOURCE_EVIDENCE_LOCK.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2A_MEASUREMENT_FORMULA_INVENTORY.md`

## Purpose

Declare the A002-owned measurement formula draft before any geometry, UV, texture, render, export, or Unreal work.

This record rebases retained candidate values onto A002 authority. It does not authorize geometry generation.

## Source Authority

Approved source:

- `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`
- PNG image data, `1055 x 1491`, 8-bit RGB, non-interlaced
- File SHA256: `4b953abb87f5f254a5f51c6214e76d3f72c4fc55bc2fa4e4d605b2440d6e53c2`

Approved scanline evidence:

- `docs/assets/reference/bloodaxe_cairnstone_asset/ScanlineCapture/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate_ScanlineManifest.json`
- Pixel SHA256: `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- `pixel_exact`: `true`
- `changed_pixels`: `0`
- `max_rgb_delta`: `0`

No A001 generated output is source authority for this draft.

## Pixel Convention

- Source origin: top-left pixel of full scan image.
- Point marks: integer coordinates identify pixel centers.
- Box convention: half-open rectangles `[left, top, right, bottom)`.
- Span formula: `span_px = right - left` or `bottom - top`.
- Dimension style: edge-to-edge pixel span for calibration; centerline pixels are recorded separately.

## Coordinate Frame

- World units: centimeters.
- Unreal scale: `1 Unreal unit = 1 cm`.
- World up: `+Z`.
- Front: `-Y`.
- Back: `+Y`.
- Right: `+X`.
- Left: `-X`.
- Top: `+Z`.
- Component yaw/pitch/roll: `0/0/0` unless source orientation formula proves otherwise.
- Origin policy: component origins are not final until pixel-count centers and snap anchors pass A002 pre-geometry audit.

## Source Dimensions

| Dimension | Candidate value | A002 use |
| --- | ---: | --- |
| Overall height | `220.0 cm` | calibration |
| Support/base width | `140.0 cm` | support footprint candidate |
| Support/base depth | `110.0 cm` | support footprint candidate |
| Primary width | `120.0 cm` | primary footprint candidate |
| Primary depth | `90.0 cm` | primary footprint candidate |
| Primary height | `185.0 cm` | primary height candidate |
| Authored support height | `35.0 cm` | calibration/disagreement evidence only for visible contacts |

## Crop And Calibration Candidates

All boxes are full-source pixel coordinates using half-open `[left, top, right, bottom)` convention.

| View | Object box px | Component boxes px | cm per px |
| --- | --- | --- | --- |
| front | `[648, 156, 946, 558]` | support `[648, 494, 946, 558]`; primary `[666, 156, 922, 494]` | `[0.4697986577, 0.5472636816]` |
| back | `[142, 684, 422, 990]` | support `[142, 941, 422, 990]`; primary `[162, 684, 402, 941]` | `[0.5, 0.7189542484]` |
| left | `[674, 680, 888, 1002]` | support `[674, 951, 888, 1002]`; primary `[692, 680, 868, 951]` | `[0.5140186916, 0.6832298137]` |
| right | `[70, 1090, 314, 1418]` | support `[70, 1366, 314, 1418]`; primary `[93, 1090, 293, 1366]` | `[0.4508196721, 0.6707317073]` |
| top | `[414, 1108, 685, 1367]` | support `[414, 1108, 685, 1367]`; primary `[434, 1132, 666, 1344]` | `[0.5166051661, 0.4247104247]` |

Crop boxes are candidates until an A002 pre-geometry audit confirms they are still valid under the approved source template and Phase 1 scanline evidence.

## Component Split Formula Draft

For front/back/left/right views:

- `primary_width_or_depth_px = full_object_width_px * primary_component_cm / support_component_cm`, centered on the recorded source orientation centerline.
- `support_height_px = full_object_height_px * 35cm / 220cm` remains calibration/disagreement evidence only.
- Visible contact geometry must use the layered contact formula, not the old single support-height formula.

For top view:

- `primary_width_px = support_width_px * 120cm / 140cm`, centered on the top component center after center validation.
- `primary_depth_px = support_depth_px * 90cm / 110cm`, centered on the top component center after center validation.
- `support_visible_mask = support_object_formula_box - primary_object_formula_box`.

## Component Center Formula Draft

Candidate source-owned top-view centers:

| Component | Center type | Rounded center px | A002 status |
| --- | --- | --- | --- |
| `primary_monolith` | reviewed source-owned perimeter filled footprint center | `[541, 1222]` | candidate; revalidate |
| `upper_socket_ring` | seed-connected filled row-span footprint center | `[528, 1223]` | candidate; revalidate; footprint still diagnostic/shared where occluded |
| `support_base` | seed-connected filled row-span footprint center | `[528, 1223]` | candidate; revalidate |
| `full_top_assembly_footprint` | filled footprint center | `[528, 1223]` | review only, not a separate export component |

Bounding-box centers, raw visible color-density centers, and old shared centers are not A002 alignment authority.

## Footprint Authority Draft

- `primary_monolith`: formula-derived `120 cm x 90 cm` oval/envelope candidate.
- `support_base`: formula-derived `140 cm x 110 cm` oval/envelope candidate.
- `upper_socket_ring`: diagnostic/shared/occluded top envelope only until A002 declares a separate footprint formula.

Oval footprint logic remains valid because the pedestal/base forms are oval. A rectangle is calibration only.

## Layered Contact Formula Draft

The old single `35 cm` support-height contact is demoted to calibration/disagreement evidence.

Per-view layered contact candidates:

| View | Primary to ring top | Ring to support bottom | Ring interval | Rule |
| --- | ---: | ---: | ---: | --- |
| front | `43.7811 cm` | `22.9851 cm` | `20.796 cm` | no average |
| back | `50.3268 cm` | `27.3203 cm` | `23.0065 cm` | no average |
| left | `35.528 cm` | `19.1304 cm` | `16.3976 cm` | no average |
| right | `37.561 cm` | `20.122 cm` | `17.439 cm` | no average |

These contact values are candidates until revalidated in an A002 pre-geometry audit.

## Snap Anchor Formula Draft

Required component pairs:

- `primary_monolith` to `upper_socket_ring`
- `upper_socket_ring` to `support_base`

Candidate snap-anchor inventory:

- Total anchors: `35`
- Paired anchors: `32`
- Unpaired review-only anchors: `3`
- Blocked review markers: `16`
- Translation tolerance: `0`
- Yaw tolerance: `0`
- Pitch tolerance: `0`
- Roll tolerance: `0`

Snap anchors must be rebound to A002 source evidence before use. They control assembly and validation only; they may not deform, stretch, or visually fit components.

## Visible, Inferred, And Diagnostic Data

Visible measured data:

- Formula-owned source pixels and formulas only.
- View-owned source surfaces only.
- No A001 generated output.

Known inferred/hidden candidates:

- void under removed `primary_monolith` where it seats into `upper_socket_ring`
- void under removed `upper_socket_ring` where it seats into `support_base`
- hidden contact faces not visible in the source template

Diagnostic only:

- radial traces
- upper socket shared/occluded top envelope until separately approved
- full top assembly center
- old `35 cm` support-height contact
- A001 pre-geometry masks until revalidated

## Blocked Methods

- A001 generated meshes, renders, textures, materials, exports, or Unreal assets as source data.
- Threshold cleanup as geometry authority.
- Largest-blob cleanup as geometry authority.
- Averaged measurements.
- Visual fitting.
- Old generator behavior.
- Copied/scaled/projected component layers.
- Upper socket ring merged into primary side shell.
- Support/base projected onto primary.
- Old `35 cm` contact flattening as visible contact authority.
- Unapproved radial trace as footprint-shape authority.
- Unapproved bounding-box center.
- Single-zone void fill.
- Inferred fill on visible measured surfaces.

## Remaining Lock Requirements

Before A002 Phase 2 can be considered locked:

- A002 must run or record a pre-geometry audit against this draft.
- Crop boxes must be confirmed against the approved source template.
- Pixel centers must be revalidated from the approved source template.
- Layered contacts must be revalidated from the approved source template.
- Snap anchors must be rebound and pair-checked under A002.
- Diagnostic/inferred masks must be clearly separated from geometry masks.
- The upper socket ring top footprint must remain blocked unless a separate A002 formula is declared.

## Phase 2B Decision

Decision: `draft complete`

This record is sufficient for A002 pre-geometry audit preparation, but it does not authorize geometry generation.

## Next Core-Valid Step

Begin A002 Phase 2C: Pre-Geometry Formula Audit.

The next task is to validate this draft against Core, AetherForge, the approved source template, and the retained candidate evidence before Phase 3 modular geometry source candidates can be considered.
