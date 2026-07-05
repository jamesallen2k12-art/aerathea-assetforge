# Blood Axe Cairnstone A002 Core Reconstruction Asset Blueprint

Status: `Core recovery draft; no production output authorized yet`

Blueprint standard: `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
Source template: `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`
Prior contaminated pass: `A001`
Clean restart pass: `A002`

## Core Authority And Asset Intent

This asset blueprint is governed by Aerathea Core Principles and the AetherForge Blueprint.

The goal is to create a measured, rebuildable, game-ready Blood Axe Giant cairnstone asset from approved source evidence using the shortest controlled path that preserves accuracy, component identity, and approval authority.

A001 is treated as drift-contaminated production history.

A001 outputs may be reviewed only for:

- approved source evidence
- approved formulas
- approved measurements
- approved component IDs
- known failure modes
- reusable non-contaminated utility logic
- lessons that improve the clean A002 path

A001 outputs must not be used as geometry, texture, UV, material, assembly, render, Unreal import, or visual approval authority unless Flamestrike explicitly reclassifies a specific artifact.

A002 is the clean restart.

A002 must preserve the approved goal that the cairnstone is made from separate identified components that click together into the assembled asset.

## Flamestrike Review Scope

For this asset type, technical proof renders and proof boards are process/audit artifacts unless they expose a production decision that requires Flamestrike.

Flamestrike's visual attention is reserved for the final assembled asset when it has reached the point of resembling the generated concept art closely enough for subjective and aesthetic judgment.

Codex may use formula proofs, component proofs, marker renders, manifests, and audits as internal technical checkpoints without requesting subjective visual approval from Flamestrike.

Stop for Flamestrike before final assembly/aesthetic approval, or earlier only if:

- the blueprint requires an explicit approval decision
- a technical mismatch requires a direction choice
- a missing authority cannot be resolved from approved records
- a proposed action would change asset intent, component identity, visible silhouette, texture ownership, or production scope

## Approved Source And Authority Hierarchy

A002 must use only approved source evidence and approved written authority.

### Primary Source Authority

1. Approved visual source template:
   `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`

2. Source scanline evidence:
   `docs/assets/reference/bloodaxe_cairnstone_asset/ScanlineCapture/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate_ScanlineManifest.json`

3. Project reconstruction authority:
   `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`

4. Asset-specific modular authority:
   `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_A001_MODULAR_COMPONENT_ASSEMBLY_PLAN.md`

5. Asset-specific geometry authority:
   `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_A001_GEOMETRY_CONSTRUCTION_PLAN.md`

6. Successful process recovery authority:
   `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_TODAYS_SUCCESS_PROCESS_VS_BLUEPRINT.md`

### Reference Only

The following may inform structure, lessons, and remake style, but may not drive A002 production output unless a specific method is reapproved:

- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_3D_GAME_ASSET_BLUEPRINT.md`

### Non-Authority Unless Reclassified

All A001 generated meshes, renders, materials, textures, exports, Unreal imports, packages, and late-pass manifests are non-authority until reviewed and reclassified.

They may not be used as source data for A002.

## Asset Scope And Status Vocabulary

Asset name: `SM_GIA_BloodAxeCairnstone_A002`

Asset type: Static Mesh prop, with approved modular source components and possible Blueprint Actor assembly.

World role: Blood Axe Giant cairnstone / ritual standing-stone cluster.

Culture/faction: Blood Axe Tribe Giant visual language.

Engine target: Unreal Engine.

Current status: `Core recovery draft; no DCC source candidate authorized yet`

Target status path:

1. `Core recovery draft`
2. `A002 source evidence candidate`
3. `A002 measurement formula candidate`
4. `A002 modular DCC source candidate`
5. `A002 modular assembly source candidate`
6. `A002 DCC game-ready candidate`
7. `A002 Unreal import candidate`
8. `Fully game-ready` only after Unreal import, map placement, validation, and Flamestrike approval

A002 must not be called fully game-ready until it has passed Unreal validation and final approval under the project pipeline vocabulary.

## Approved Physical Components

A002 must preserve the approved modular interpretation: the cairnstone is assembled from separate identified physical components.

### `primary_monolith`

- Asset role: vertical main Blood Axe stone.
- Assembly role: seats into the upper socket ring.
- Source authority: approved measured primary footprint and front/back/left/right primary surface evidence.
- Must remain independently identifiable before assembly.
- Must have its own source measurements, formula-owned masks, center, pivot, orientation marks, texture ownership, UV ownership, collision decision, and proof renders.

### `upper_socket_ring`

- Asset role: independent receiver layer between the primary monolith and support base.
- Assembly role: receives the primary monolith above and seats into the support base below.
- Source authority: approved per-view layered contact intervals plus top-view perimeter evidence where separable.
- Must remain independently identifiable before assembly.
- Must have its own source measurements, formula-owned masks or tagged inferred footprint rules, center type, pivot, orientation marks, snap anchors, texture ownership, UV ownership, collision decision, and proof renders.

### `support_base`

- Asset role: lower support and foundation piece.
- Assembly role: receives the upper socket ring and establishes the assembled asset base.
- Source authority: approved measured support/base footprint and ring-bottom contact evidence.
- Must remain independently identifiable before assembly.
- Must have its own source measurements, formula-owned masks, center, pivot, orientation marks, texture ownership, UV ownership, collision decision, and proof renders.

### Assembly

- Assembly ID: `A002_cairnstone_assembly`
- Future DCC assembly asset: `SM_GIA_BloodAxeCairnstone_A002_Assembled_Proof`
- Future Unreal assembly actor, if separate components remain runtime-relevant: `BP_GIA_BloodAxeCairnstone_A002_Assembly`
- Components must assemble by approved source-derived snap anchors, not by manual visual fitting.
- Components may later be combined for runtime performance only if source component lineage is preserved.

## Measurement And Formula Rules

A002 geometry must be driven by scan-verified pixels and declared formulas.

Before any geometry, UV, texture, render, export, or Unreal work:

1. Verify the approved source template scanline evidence.
2. Derive view crops from the approved source layout.
3. Declare pixel convention.
4. Declare coordinate frame.
5. Declare cm-per-pixel calibration per view.
6. Declare component split formulas.
7. Declare component center formulas.
8. Declare contact-position formulas.
9. Declare yaw, pitch, roll, and orientation formulas or zero-rotation proof.
10. Declare exterior seam formulas.
11. Record formula-derived measurement masks.
12. Record which masks are diagnostic only.

Geometry-defining measurements must come from formula-owned source evidence.

Blocked as A002 geometry authority unless explicitly approved as inference:

- threshold cleanup
- largest-blob cleanup
- visual fitting
- averaged contour
- smoothed mask
- generic primitive replacement
- old generator behavior
- prior generated A001 output
- unapproved radial trace
- unapproved bounding-box center
- unapproved full top cap

If a formula is missing, incomplete, or only present inside a script, A002 must stop before geometry.

## Evidence-Bound Decision Rule For A002

Every A002 production decision must be bound to explicit authority.

Valid decision authority includes:

- approved source paths
- scanline manifests
- blueprint sections
- asset-specific plans
- formula records
- measurement contracts
- component IDs
- source-view ownership records
- snap-anchor records
- status labels
- blocked-method lists
- Flamestrike approvals

A002 agents, scripts, audits, and review reports must not replace explicit authority with:

- memory
- visual guessing
- convenience shortcuts
- prior A001 generated output
- old generator behavior
- unapproved inference
- proof-only artifacts

If explicit authority is missing, incomplete, or conflicting, A002 must stop before production continues.

The stop report must identify:

- the missing or conflicting authority
- the affected component, view, formula, contact, texture, UV, or output
- the decision that cannot be made safely
- the smallest sufficient proposed correction

No A002 artifact may advance status unless its report or manifest names the authority used to make the decision.

## Approved Component Interface And Snap Rules

A002 components must connect through source-derived snap anchors and measured contact interfaces.

### Required component pairs

- `primary_monolith` to `upper_socket_ring`
- `upper_socket_ring` to `support_base`

### Required snap-anchor authority

Before modular DCC source generation, A002 must define or verify source-derived snap anchors for:

- primary bottom front/back/left/right contact
- ring top front/back/left/right receiver contact
- ring bottom front/back/left/right contact
- support top front/back/left/right receiver contact
- top-view perimeter checks for each separable component where source evidence supports them

### Contact rules

- Contacts must use measured source pixels, approved formulas, or approved tagged inference.
- Each contact must name both participating components.
- Each contact must record expected position, observed position, gap or overlap, center offset, yaw, pitch, roll, and tolerance.
- Components must snap by anchor ID, not by manual visual fitting.
- Zero translation, zero yaw, zero pitch, and zero roll are required unless a later approved manifest explicitly changes that rule.
- If anchor pairs disagree, stop and apply the AetherForge disagreement rule before moving geometry.

### Blocked contact methods

- inherited taper from adjacent component
- copied contact loops from another component
- visual fitting after component generation
- old shared center as universal authority
- old 35cm contact flattening
- averaged per-view contact positions
- hidden lifts or drops
- stretch strips, cover planes, or seam-hiding geometry

## Visible Data, Hidden Data, And Inferred Fill

A002 must separate visible measured data from hidden or inferred data.

### Visible measured data

Visible surfaces, contours, contacts, seams, texture regions, and UV regions must come from scan-verified source pixels and declared formulas.

Visible measured data may not be replaced by:

- inferred fill
- smoothing
- averaging
- old generated output
- visual fitting
- texture synthesis
- procedural approximation

### Hidden or occluded data

Hidden or occluded areas may use tagged inferred surface fill only when source evidence cannot directly show the area.

Known hidden/inferred candidates for this asset include:

- the void under the removed `primary_monolith` where it seats into `upper_socket_ring`
- the void under the removed `upper_socket_ring` where it seats into `support_base`
- hidden contact faces not visible in the source template

### Inferred fill requirements

Every inferred fill area must record:

- affected component
- affected surface or contact zone
- why direct source data is unavailable
- source sample area used
- fill method
- whether the fill affects geometry, texture, UVs, or material only
- proof that visible measured data was not overwritten
- review output that clearly labels the fill as inferred

Inferred fill may source-match material appearance, but it cannot become visual-canon source data.

If an inferred area would change visible silhouette, contact geometry, or component assembly behavior, stop for Flamestrike approval before implementation.

## Texture, UV, And Material Ownership

Texture, UV, and material work is blocked until modular geometry and assembly source candidates are approved.

Once approved, A002 texture and UV work must follow source ownership:

- visible front-facing surfaces use the front source view
- visible back-facing surfaces use the back source view
- visible left-facing surfaces use the left source view
- visible right-facing surfaces use the right source view
- visible top-facing surfaces use the top source view
- inferred hidden surfaces use only tagged inferred fill

Each component must have its own UV ownership record:

- `primary_monolith`
- `upper_socket_ring`
- `support_base`

Visible source pixels must copy exactly into visible texture outputs.

Blocked for visible source pixels:

- filtered atlas resizing
- color averaging
- lighting-based color approval
- unreported color correction
- wrong-view source sampling
- full source panel stretched across a smaller measured face
- support/base top pixels sampled inside the primary mask
- primary top pixels sampled from the full support/base mask
- A001 generated textures or materials used as source data

Allowed only when tagged and approved by the current step:

- exact-copy atlas placement
- native per-view texture use
- nearest-copy placement
- source-matched inferred fill for hidden or occluded areas
- normal, AO, ORM, and emissive generation from approved visible/inferred texture ownership

No UVs, texture nodes, material instances, FBX exports, or Unreal imports may be generated before the geometry and assembly approval gate authorizes them.

## Proof And Review Gates

A002 must produce review artifacts only when they answer the current production decision.

### Required proof sequence

1. Source evidence proof
   - Confirms approved source and scanline exactness.

2. Measurement/formula proof
   - Confirms view crops, component splits, pixel convention, calibration, centers, contacts, and blocked/diagnostic masks.

3. Individual component geometry proof
   - Confirms `primary_monolith`, `upper_socket_ring`, and `support_base` as separate source candidates.
   - Shows front, back, left, right, top, and angle views for each component.
   - Shows component identity and socket/contact markers.
   - No UVs, textures, exports, or Unreal work.

4. Assembly proof
   - Confirms components click together using approved snap anchors.
   - Shows component colors separately.
   - Shows socket labels or marker pass.
   - Reports seam gaps as measurements, not hidden fixes.
   - Does not merge components into a final static mesh.

5. Texture/UV/material proof
   - Only after geometry and assembly approval.
   - Confirms visible source ownership and inferred-fill boundaries.

6. DCC game-ready proof
   - Confirms source, FBX, UV/texture/material plan, LODs, collision proxy, scale, and proof renders.

7. Unreal import proof
   - Confirms import, material assignment, LODs, collision, scale, placement, and review-map validation.

### Review presentation rule

When a visual review artifact is required, open the actual image file in a visible desktop window.

A proof must be labeled as one of:

- `candidate`
- `proof only`
- `reference only`
- `blocked`
- `invalid`

A proof-of-process artifact may not advance A002 production unless it directly answers the active review gate.

## Blocked Methods And Drift Triggers

The following methods are blocked for A002 unless Flamestrike explicitly approves a documented exception:

### Source and authority drift

- using A001 generated output as source data
- using old generated meshes, renders, textures, materials, exports, or Unreal imports as authority
- using chat memory instead of written blueprint/formula/manifest authority
- treating a proof-only artifact as approval-ready production output
- advancing from a quarantined or invalid artifact

### Geometry drift

- threshold cleanup as geometry authority
- largest-blob cleanup as geometry authority
- visual fitting
- generic primitive replacement
- averaged contours or averaged per-view measurements
- old generator behavior
- unapproved radial trace
- unapproved bounding-box centers
- copied, scaled, projected, or inherited component layers
- one-piece welded final mesh before component proofs
- support/base projection onto the primary monolith
- merging upper socket ring into the primary side shell
- old 35cm contact flattening
- artificial lift/drop/offset

### Texture and UV drift

- filtered atlas resizing for visible source pixels
- wrong-view source sampling
- stretching a full source panel over a smaller measured face
- support/base top UVs inside the primary mask
- primary top UVs from the full support/base mask
- A001 textures or materials as source data
- inferred fill on visible measured surfaces

### Workflow drift

- creating tools, packages, renders, validations, or docs that do not answer the active production decision
- proceeding through missing authority
- continuing after a failed gate without Core Recovery
- repairing forward from drift
- using specialist-agent output before Codex Core review and artifact classification

## A002 Clean Production Path

A002 must follow the shortest controlled path to a valid production asset.

### Phase 0: Core Recovery And Quarantine

- Classify A001 outputs.
- Preserve viable evidence and approved written data.
- Quarantine drifted or non-authority production outputs.
- Record the drift/recovery status in `docs/projects/assetforge/DRIFT_LEDGER.md`.
- Do not use A001 generated output as A002 source authority.

### Phase 1: Source Evidence Lock

- Verify approved source template.
- Verify scanline manifest.
- Confirm source hierarchy.
- Confirm no prior generated output is being used as source data.

Approval decision: source evidence approved, rejected, or blocked.

### Phase 2: Measurement Formula Lock

- Declare pixel convention.
- Declare crop formulas.
- Declare component split formulas.
- Declare component centers.
- Declare contact formulas.
- Declare snap-anchor formulas.
- Declare visible/inferred/diagnostic masks.
- Declare blocked methods.

Approval decision: measurement/formula authority approved, rejected, or blocked.

### Phase 3: Modular Geometry Source Candidates

- Generate `primary_monolith`, `upper_socket_ring`, and `support_base` as separate DCC source candidates.
- Produce individual component proof renders with markers.
- Audit component identity, pivots, centers, dimensions, and source ownership.
- No UVs, textures, FBX export, Unreal import, or final assembly merge.

Approval decision: technical modular DCC source candidate approved, rejected, or blocked. This is not subjective aesthetic approval.

### Phase 4: Snap Assembly Source Candidate

- Assemble approved components using snap anchors.
- Produce assembly proof renders with component colors and socket labels.
- Audit zero translation, yaw, pitch, roll, contact, and seam measurements.
- Do not merge into a final runtime mesh at this stage.

Approval decision: technical modular assembly approved, rejected, or blocked. Flamestrike subjective visual review begins only when the assembled asset is close enough to the generated concept art for aesthetic judgment.

### Phase 5: Texture, UV, Material Candidate

- Create UV ownership records.
- Map visible source pixels by source-view ownership.
- Create tagged source-matched inferred fills only for approved hidden areas.
- Produce color, UV, material, and inferred-fill proof outputs.
- Audit visible pixel exactness and wrong-view sampling.

Approval decision: texture/UV/material candidate approved, rejected, or blocked.

### Phase 6: DCC Game-Ready Candidate

- Create FBX exports.
- Create LOD0-LOD3.
- Create collision proxy.
- Prepare material and texture package.
- Write DCC handoff report and validation manifest.
- Produce final DCC proof renders.

Approval decision: DCC game-ready candidate approved, rejected, or blocked.

### Phase 7: Unreal Import Candidate

- Import into Unreal.
- Assign materials and textures.
- Configure LODs and collision.
- Place in approved review map.
- Validate scale, orientation, material assignment, LOD switching, collision, and performance.
- Capture review images.

Approval decision: Unreal import candidate approved, rejected, or blocked.

### Phase 8: Final Asset Blueprint Archive

- Write final 3D Game Asset Blueprint.
- Archive source hierarchy, formulas, manifests, component records, validation reports, proof renders, known issues, rejected methods, remake instructions, and final approval status.
- Asset may be called `Fully game-ready` only after this archive and Unreal validation are approved.

## Final A002 Standard

A002 must be rebuilt from approved source evidence, approved formulas, approved component identity, and clean generator logic.

The asset is successful only if it is:

- faithful to the approved source template
- measured from scan-verified pixels
- separated into approved reusable source components
- reassembled by source-derived snap anchors
- textured from correct source-view ownership
- explicit about inferred hidden surfaces
- free of A001 drift contamination
- validated before review
- visible in actual review windows when approval is required
- archived so it can be recreated later without memory or chat history

The governing production question is always:

What is the shortest Core-valid step that moves A002 toward a rebuildable, game-ready Aerathea asset while preserving approval authority?
