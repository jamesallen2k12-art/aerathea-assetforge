# SM_GIA_BloodAxeCairnstone_A002 Phase 2A Measurement Formula Inventory

Status: `A002 measurement formula inventory complete; formula lock not yet approved`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_1_SOURCE_EVIDENCE_LOCK.md`
- `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_A001_CORE_RECOVERY_AND_QUARANTINE_STATUS.md`

## Phase Goal

Inventory the retained A001 pre-geometry formula evidence and determine what can be carried into A002 only after revalidation from the approved A002 source evidence.

This record is not a geometry authorization and not a final A002 formula lock.

## Evidence Reviewed

Candidate evidence reviewed from quarantined A001:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001MeasurementFormulaManifest.json`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001FormulaAuthorityManifest.json`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001PixelCountCenterManifest.json`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001SnapAnchorManifest.json`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001LayeredContactFormulaApprovalManifest.json`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001OvalFootprintApprovalManifest.json`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001PreGeometryHardAuditManifest.json`

These records are retained evidence only until rebound and revalidated under A002.

## Candidate Values To Revalidate

### Pixel Convention

Candidate convention:

- Source origin: top-left pixel of full scan image.
- Point marks: integer coordinates identify pixel centers.
- Box convention: half-open rectangles `[left, top, right, bottom)`.
- Span formula: `span_px = right - left` or `bottom - top`.
- Dimension style: edge-to-edge pixel span for calibration; centerline pixels recorded separately.

Required A002 action: re-declare this convention in the A002 formula lock.

### Coordinate Frame

Candidate frame:

- World units: centimeters.
- Unreal scale: `1 Unreal unit = 1 cm`.
- World up: `+Z`.
- Front: `-Y`.
- Back: `+Y`.
- Right: `+X`.
- Left: `-X`.
- Component yaw/pitch/roll: `0/0/0` unless source orientation formula proves otherwise.

Required A002 action: re-declare this coordinate frame and bind it to A002 source evidence.

### Source Dimensions

Candidate dimensions:

- Overall height: `220.0 cm`
- Support width: `140.0 cm`
- Support depth: `110.0 cm`
- Support height: `35.0 cm` as authored/global calibration only
- Primary width: `120.0 cm`
- Primary depth: `90.0 cm`
- Primary height: `185.0 cm`

Required A002 action: use these as source-dimension candidates, with the old `35 cm` support height demoted for visible contacts according to the layered contact evidence.

### Approved Footprint Candidates

Candidate footprint authorities:

- `primary_monolith`: approved `120 cm x 90 cm` measured oval/envelope candidate.
- `support_base`: approved `140 cm x 110 cm` measured oval/envelope candidate.
- `upper_socket_ring`: diagnostic shared/occluded top envelope only until a separate footprint formula is declared.

Required A002 action: retain oval footprint logic because the pedestal/base forms are oval, but do not treat the upper socket top footprint as independent geometry until A002 has a separate approved formula.

### Candidate Component Centers

Candidate centers from source-owned top-view pixel counts:

- `primary_monolith`: rounded pixel-count center `[541, 1222]`
- `upper_socket_ring`: rounded pixel-count center `[528, 1223]`
- `support_base`: rounded pixel-count center `[528, 1223]`
- `full_top_assembly_footprint`: rounded center `[528, 1223]`, review only

Required A002 action: revalidate centers from the approved source template before using them for origin, pivot, snap, or assembly.

### Candidate Layered Contacts

The retained layered contact formula demotes the old single `35 cm` support contact to calibration/disagreement evidence and records per-view contact intervals with no averaging.

Candidate contact intervals:

| View | Primary to ring top | Ring to support bottom | Ring interval |
| --- | --- | --- | --- |
| front | `43.7811 cm` | `22.9851 cm` | `20.796 cm` |
| back | `50.3268 cm` | `27.3203 cm` | `23.0065 cm` |
| left | `35.528 cm` | `19.1304 cm` | `16.3976 cm` |
| right | `37.561 cm` | `20.122 cm` | `17.439 cm` |

Required A002 action: carry forward the no-average rule and revalidate per-view contacts from the approved source template before geometry.

### Candidate Snap Anchor Evidence

Candidate snap-anchor status:

- Total anchors: `35`
- Paired anchors: `32`
- Unpaired review-only anchors: `3`
- Blocked review markers: `16`
- Pair validation: all pairs resolve.
- Translation tolerance: zero.
- Yaw/pitch/roll tolerance: zero.

Required A002 action: rebind source paths and scanline manifests to A002, then verify required component pairs:

- `primary_monolith` to `upper_socket_ring`
- `upper_socket_ring` to `support_base`

## A002 Formula Lock Blockers

The following must be resolved before Phase 2 can be marked locked:

- Rebind all source scanline references away from A001 restart manifests to the approved A002 Phase 1 source scanline manifest.
- Re-declare crop boxes and component split formulas under A002.
- Revalidate component centers from the approved source template.
- Revalidate layered contact formulas and snap anchors from the approved source template.
- Declare visible, inferred, and diagnostic masks for A002.
- Keep the `upper_socket_ring` top footprint diagnostic/shared/occluded until a separate A002 formula is approved.
- Keep the old `35 cm` support height as calibration/disagreement evidence only for visible contacts.
- Confirm radial traces remain diagnostic history only, not footprint-shape authority.
- Confirm no A001 generated mesh, render, texture, material, export, or Unreal output is used.

## Phase 2A Decision

Decision: `inventory complete`

A002 has sufficient candidate pre-geometry evidence to draft a Measurement Formula Lock, but the formula lock is not complete until the blockers above are resolved in an A002-owned record.

## Next Core-Valid Step

Begin A002 Phase 2B: Measurement Formula Lock Draft.

The next task is to write the A002-owned formula lock record using the approved source template, Phase 1 scanline manifest, retained written constraints, and revalidated candidate values listed here.
