# SM_GIA_BloodAxeCairnstone_A002 Phase 2C Pre-Geometry Formula Audit

Status: `passed for A002 measurement formula lock candidate; geometry not authorized`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_1_SOURCE_EVIDENCE_LOCK.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2A_MEASUREMENT_FORMULA_INVENTORY.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md`

## Audit Scope

Audit the A002 Phase 2B formula lock draft as a written measurement authority candidate.

This audit does not authorize geometry, UVs, textures, renders, exports, Unreal imports, or use of A001 generated output as source data.

## Audit Results

| Check | Result | Evidence |
| --- | --- | --- |
| Approved source template is named | pass | Phase 2B lists `REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png` with SHA256. |
| Phase 1 scanline evidence is named | pass | Phase 2B lists the approved scanline manifest and `pixel_exact=true`, `changed_pixels=0`, `max_rgb_delta=0`. |
| A001 generated output blocked as source | pass | Phase 2B states no A001 generated output is source authority. |
| Pixel convention declared | pass | Half-open `[left, top, right, bottom)` convention and pixel-center mark meaning are declared. |
| Coordinate frame declared | pass | `+Z` up, `-Y` front, `+Y` back, `+X` right, `-X` left, centimeters, zero-rotation policy. |
| Source dimensions declared | pass | Overall, support/base, and primary dimensions are listed. |
| Crop boxes declared | pass | Front, back, left, right, and top crop boxes are listed. |
| Component split formulas declared | pass | Side and top split formulas are listed. |
| Component centers declared | pass with candidate status | Primary, upper socket ring, support base, and review-only full assembly centers are listed and marked for revalidation. |
| Footprint authority separated by component | pass | Primary/support oval candidates are separated; upper socket ring top footprint remains diagnostic/shared/occluded. |
| Layered contact formula blocks old support-height flattening | pass | Old single `35 cm` support contact is demoted; per-view layered contacts are listed with no averaging. |
| Snap anchor requirements declared | pass with candidate status | Required component pairs and zero-tolerance policy are listed. |
| Visible/inferred/diagnostic categories declared | pass | Visible data, two hidden/inferred void candidates, and diagnostic-only data are separated. |
| Blocked methods declared | pass | A001 generated source use, threshold/blob authority, averaging, visual fitting, old generator behavior, single-zone void fill, and other drift methods are blocked. |
| Geometry remains blocked | pass | Draft status and next-step language explicitly do not authorize geometry generation. |

## Remaining Constraints

The following constraints must carry into Phase 3:

- A002 geometry may not start from A001 generated meshes, renders, textures, materials, exports, or Unreal assets.
- The Phase 2B record is written authority for formulas only after this audit; it is not visual approval.
- The upper socket ring top footprint remains diagnostic/shared/occluded until a separate A002 formula is declared.
- The old `35 cm` support height remains calibration/disagreement evidence only for visible contacts.
- Radial trace history remains diagnostic only.
- Pixel centers, crop boxes, contacts, and snap anchors must be used as formula-owned A002 candidates and audited again after any DCC source candidate is generated.

## Phase 2C Decision

Decision: `passed_for_measurement_formula_lock_candidate`

A002 Phase 2 is sufficient to proceed to the next controlled stage: modular DCC source candidate planning.

Geometry generation is still blocked until the Phase 3 action is explicitly stated and remains limited to the approved modular source candidate scope.

## Next Core-Valid Step

Begin A002 Phase 3A: Modular DCC Source Candidate Plan.

The next task is to state the exact generation plan for `primary_monolith`, `upper_socket_ring`, and `support_base` as separate DCC source candidates before running Blender or creating geometry.
