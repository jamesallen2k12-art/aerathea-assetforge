        # BloodAxe Cairnstone A001 Geometry Construction Plan

        Status: `A001 geometry construction plan candidate recorded; no mesh generated`

        This is a planning artifact only. No mesh, UVs, textures, movement, rotation, centering, assembly, render, or export has been generated.

        ## Approved Inputs

        - Pre-geometry audit: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001PreGeometryHardAuditManifest.json`
        - Formula authority: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001FormulaAuthorityManifest.json`
        - Surface marker approval: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001SurfaceEdgeMarkerApprovalManifest.json`
        - Surface marker manifest: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001SurfaceEdgeMarkerManifest.json`
        - Oval footprint approval: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001OvalFootprintApprovalManifest.json`
        - Layered contact approval: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001LayeredContactFormulaApprovalManifest.json`
        - Radial decision: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A001/SM_GIA_BloodAxeCairnstone_A001_A001RadialTraceReviewDecision.json`

        ## Plan Scope

        - Allowed now: geometry construction planning only.
        - Mesh generation allowed now: `false`.
        - Render/export allowed now: `false`.
        - Approval required before mesh candidate generation: `true`.

        ## Global Construction Rules

        - Build primary, upper socket/ring, and support/base independently before attachment.
- Use approved per-view station values; do not average contact disagreement away.
- Use exact source-derived markers for side edge correspondence and normal ownership.
- Preserve component lineage even if a later runtime mesh is combined.
- Texture and UV generation remain blocked until geometry proof passes.

        ## Components

        ## primary_monolith

Export role: reusable source component; later may be combined into final static mesh after lineage is preserved

Geometry source: approved 120cm x 90cm measured oval top footprint plus front/back/left/right side markers

Top footprint: `[120.0, 90.0]`

Construction:
- Generate a separate primary side shell from view-owned exterior edge markers.
- Use the approved oval formula only for the top footprint envelope; do not use the rejected radial pass.
- Use the approved per-view primary-to-ring contact stations for the bottom loop; do not flatten to 35cm.
- Keep top cap UVs inside the primary top mask only.

Blocked:
- support/base projection onto primary
- old radial trace as footprint authority
- old 35cm contact flattening
- cross-view averaging

## upper_socket_ring

Export role: reusable source component and contact layer between primary and support

Geometry source: approved per-view layered contact intervals plus surface-edge markers

Top footprint: `diagnostic shared/occluded top envelope only until separate footprint formula is approved`

Construction:
- Generate the ring/socket as an independent interval component.
- Use per-view top and bottom contact stations exactly as recorded; no global average.
- Do not inherit taper, normals, UVs, or side shell from the primary object.
- Hidden/occluded contact surfaces remain tagged and cannot override visible source data.

Blocked:
- merging ring into primary side shell
- copying/scaling support ring
- same-plane annulus bridge as exterior fix
- unapproved full top cap

## support_base

Export role: reusable source component; base/support layer

Geometry source: approved 140cm x 110cm measured oval footprint plus approved ring-bottom contact stations

Top footprint: `[140.0, 110.0]`

Construction:
- Generate the support/base as its own component from the approved 140x110cm oval footprint.
- Use approved upper-ring-to-support contact stations for the top contact loop.
- Support visible top/annulus must stay outside the primary component mask.
- Do not copy, resize, or project support/base pixels into the primary component.

Blocked:
- full top cap sampling under primary
- base layer copied onto primary
- old A02/A23/A26 generator logic
- stretch patches or detached shells


        ## Blocked Methods

        - old contaminated generator logic
- radial trace as footprint-shape authority
- single 35cm support height as visible contact authority
- copied/resized support-base layer
- primary/support full top cap mixing
- stretch strip, detached shell, cover-up plane, or visual patch
- global averaging of per-view contact stations

        ## Mesh Candidate Validation Targets

        - geometry proof render with markers
- top/front/back/left/right orientation proof
- edge-loop gap report for exterior seams
- component lineage proof
- no UV/texture approval until geometry proof passes

        ## Constraints To Carry Forward

        - upper socket/ring top footprint remains diagnostic/shared/occluded until a separate footprint formula is approved
- old 35cm support height is calibration/disagreement evidence only for visible contacts
- approved geometry plan must use per-view layered contact intervals with no averaging
- radial trace is diagnostic history only, not footprint-shape authority
