# AetherForge Blueprints

Strict source-to-asset reconstruction standards for Aerathea.

Last updated: 2026-07-04

## Purpose

The AetherForge Blueprints define the start-to-finish process for turning approved visual sources into measured, auditable, game-ready DCC candidates.

This document exists to prevent silent corrections, hidden averaging, color drift, orientation drift, contact gaps, and other "almost right" failures. It converts the lessons from the Blood Axe cairnstone work into a reusable standard for any future object, prop, building piece, weapon, modular component, creature part, or environment asset.

Use this document with:

- `docs/assets/CONCEPT_ART_TO_GAME_READY_ASSET_PIPELINE.md`
- asset-specific production packages
- scanline evidence manifests
- DCC generator scripts
- strict validation gate reports

## File Format Rule

The canonical AetherForge Blueprints live as Markdown.

Markdown is the master format because it is readable, reviewable, version controlled, and easy to diff. If needed, this Markdown source can later generate:

- PDF review handbooks
- JSON validation schemas
- CSV measurement sheets
- proof boards
- Unreal import checklists

Do not make PDF, image, or spreadsheet versions the source of truth. They are exports only.

## Core Principle

Measure first. Declare the method. Build to the method. Validate before review.

The hard validation gate should almost always pass because every possible failure has already been addressed as a rule from the beginning. If the gate fails, the build violated a known standard or encountered a new condition that must be documented before continuing.

## Blueprint Authority Rule

For strict reconstruction work, the Blueprint is the authority.

Do not add non-Blueprint methods, hidden fixes, automatic substitutions, extra helpers, or "improvements" during a build. If the build encounters a problem not covered by the Blueprint, stop and report:

- the observed problem
- the exact evidence
- the affected rule or missing rule
- the proposed rule change
- the proposed implementation change

Only after the rule and implementation change are approved should the build continue.

## Change Declaration Rule

Before changing geometry, contact, orientation, color, texture, UVs, lighting, scale, source priority, inference, or validation logic, state the change in plain English.

Every change must include:

- what is changing
- why it is changing
- source evidence
- expected measurement or visual result
- tolerance
- validation check
- whether the change affects visible canon geometry or inferred/hidden data

No silent changes are allowed.

## Source Hierarchy

Use this hierarchy unless a production package defines a stricter one:

1. Approved scanline source image or template
2. Approved top-down or orientation source
3. Approved front, back, left, right, side, or detail views
4. Declared source-priority or envelope rule for conflicting measurements
5. Tagged inferred fill for missing or hidden areas
6. Prior generated outputs for review history only

Prior failed generations, procedural fixes, review renders, and visual patches are not source data.

## Fresh Pass Rule

A fresh pass is a clean slate for both data and generator logic.

Required:

- use approved original source images only
- create new scanline evidence, masks, measurements, manifests, and output folders
- write or assemble the build from neutral, asset-agnostic utilities only
- declare any reused utility before using it
- prove reused utilities do not carry prior asset-pass assumptions

Forbidden:

- copying a prior failed asset-specific generator as the build base
- inheriting prior pass contact fixes, support layers, annulus tricks, stretch passes, seam patches, hidden offsets, or tuned constants
- treating an old review render, old generated texture, old mesh, or old manifest as source data
- silently preserving behavior from a previous pass because it appears useful

Prior passes may be reviewed only for lessons learned and known failure modes. If a fresh pass encounters a problem, stop, show the evidence, propose the fix, and get approval before implementation.

## Pixel-Perfect Measurement Rule

All geometry-defining crops, masks, component splits, scale, alignment, orientation, contact positions, and seam positions must be derived from scan-verified pixels using declared pixel-to-world formulas.

Required:

- full source scanline capture before any crop, mask, measurement, texture, or geometry step
- declared pixel convention before measurement
- declared crop-boundary formula
- declared centimeters-per-pixel or world-units-per-pixel formula
- declared component-split formula
- declared center/origin formula
- declared yaw/pitch/roll/orientation formula
- declared contact-position formula
- declared exterior seam-position formula

Geometry ownership masks must be formula-derived measurement masks. Texture/material masks may help extract visible pixels, create overlays, or diagnose object boundaries, but they do not define geometry unless explicitly approved as inferred geometry.

Blocked as geometry authority unless explicitly approved as inference:

- threshold cleanup
- largest-blob cleanup
- smoothed masks
- hand-traced correction
- visual fit
- averaged contour
- procedural replacement
- old generator behavior

If formula-derived measurement and visible source pixels disagree, stop and apply the disagreement rule before modeling.

## Formula Archive Rule

Every strict reconstruction pass must record the exact formulas needed to recreate the asset.

The formula record must be stored in:

- the asset's measurement formula manifest during the build
- the asset's final 3D Game Asset Blueprint after approval

Required formula fields:

- source image path and source hash
- source scanline manifest
- pixel convention
- coordinate frame
- orientation-pixel manifest
- crop-boundary formula for every source view
- component-split formula for every separable component
- calibration formula for every view
- center/origin formula
- yaw/pitch/roll formula or zero-rotation proof
- contact-position formula
- exterior seam-position formula
- formula-derived measurement mask paths
- proof that diagnostic masks do not own geometry
- blocked methods for that pass

If the formula record is missing or incomplete, the build is not recreateable and must not proceed to geometry.

## Pixel-Count Center Rule

For any component footprint, alignment center, orientation center, contact center, or reassembly center, the center must be calculated from actual source-owned pixel counts inside the measured component footprint.

Do not assume the center from a rectangular bounding box unless the source component is truly rectangular and that rectangular shape is source-approved.

Required:

- count actual source-owned pixels for the component
- record the pixel-count method
- record the total counted pixels
- compute the component center from those counted pixels
- record the resulting pixel coordinate
- compare the pixel-count center against orientation marks, printed guides, and calibration boxes
- if centers disagree beyond tolerance, stop and apply the disagreement rule

Bounding boxes may be used for calibration, crop framing, or review overlays. They must not define the final component center for oval, circular, irregular, broken, organic, tapered, or non-rectangular components.

For top-down footprints, the support/base footprint must use the actual measured footprint shape, such as an oval, ring, irregular contour, or source-owned pixel perimeter. A rectangle around that footprint is a calibration frame only.

For textured, cracked, highlighted, engraved, broken, ring-shaped, or partially occluded components, raw visible color-density centers are diagnostic only unless explicitly approved as the alignment method. Raw visible pixels can overweight dark cracks, painted symbols, shadows, labels, and annotation marks.

Required center authority for a physical footprint:

- isolate object pixels from source-sheet text, arrows, dimension lines, labels, and background
- record the exclusion method for non-object annotation pixels
- record the raw visible-pixel center as diagnostic evidence
- derive the alignment center from the measured footprint contour, filled source-owned footprint, annulus formula, or perimeter formula
- record which center is the authority for alignment, attachment, origin, or scale
- compare raw visible-pixel center, footprint center, orientation marks, and calibration guides
- if labels, dimensions, background, or unrelated artwork enter the counted mask, fail the center pass and revise before geometry

For rings, collars, sockets, bases, and other layered components, record the center type being used:

- outer footprint center
- inner contact perimeter center
- visible annulus center
- filled footprint center
- assembled-footprint review center
- shared stacked-layer envelope center

Do not substitute one center type for another without declaring the reason, tolerance, and affected attachment interface.

When a source sheet includes labels, arrows, dimension lines, grid marks, borders, or other nearby non-object pixels, the center pass must use a method that proves those pixels cannot affect the component center.

Approved methods include:

- explicit annotation-exclusion mask
- seed-connected source component mask
- reviewed source-owned contour/perimeter mask

For a seed-connected center pass, record:

- declared object-only source window
- source-owned seed pixel
- connectivity rule
- background rejection rule
- raw source-owned pixel count
- connected source-owned pixel count
- excluded annotation or detached-pixel count
- filled-footprint or contour-center formula
- resulting center coordinate
- proof that no geometry, movement, rotation, centering, assembly, or source-pixel modification occurred

Seed-connected centers are especially useful when detached annotation pixels sit near the object. Detached pixels must not be allowed to stretch a row span or bias the center.

Seed-connected masks are not automatically approved geometry authority. If source lighting, highlights, pale edge pixels, compression artifacts, labels, guide marks, or annotation fragments cause the seed-connected mask to visibly clip the true object edge or include non-object fragments, the mask is diagnostic only.

When a seed-connected mask visibly disagrees with the source silhouette, switch to a reviewed source-owned contour or perimeter-point method before geometry. Record:

- the rejected seed-connected mask path
- the visual disagreement
- the affected edge or surface
- reviewed perimeter points or source-owned contour mask
- the replacement contour formula
- why the replacement better matches the source

A measured component center may differ from a printed guide center or shared review center when the source footprint is asymmetric. Do not recenter an asymmetric component to a printed guide unless the source evidence proves the guide is the intended alignment authority.

If a top-down view cannot visually separate stacked vertical layers, do not pretend that one top contour independently proves every layer.

Required classification for top-view contours in stacked components:

- independent component footprint
- shared stacked-layer envelope
- visible annulus or exposed contact surface
- occluded footprint requiring tagged inference
- review-only assembled footprint

A shared stacked-layer envelope can validate the assembled outer size, but it cannot by itself prove the separate geometry of multiple layers. The separate layer geometry must then use:

- side/front/back component-isolated profiles
- clean measured level/contact lines
- paired snap/contact anchors
- source-priority or envelope rules for hidden overlap
- tagged inferred footprint fill where the source is occluded

Do not duplicate the same top contour into multiple independent reusable components unless it is explicitly tagged as a shared envelope or source evidence proves those components have the same footprint.

## Shared-Origin Radial Perimeter Trace Rule

When stacked or nested components share an assembly origin, a radial perimeter trace may be used to derive top-view contours more cleanly than color thresholding or rectangular boxes.

This method starts from an approved shared assembly origin and samples outward in many directions until each ray reaches the visible perimeter of the target component.

Required:

- approved shared origin point
- proof that the origin is an assembly/reference origin, not a forced recentering of asymmetric components
- target component or layer name
- ray count or angle step
- source view and source crop
- perimeter stop rule
- perimeter point list
- filled contour mask
- pixel area count
- calculated footprint center
- center delta from shared origin
- source-pixel scale for each axis when X and Y pixels do not represent the same world distance
- measured width/depth ratio in world units for oval or elliptical footprints
- source-pixel preview and centimeter-normalized preview when the source-pixel view can visually hide the oval ratio
- visible, occluded, and inferred angular sectors
- comparison against prior center/contour evidence
- proof that no source pixels, components, geometry, UVs, or assembly transforms were modified

Allowed perimeter stop rules:

- reviewed source-owned edge pixel
- strongest reviewed silhouette edge along the ray
- declared contact/envelope boundary
- tagged inferred boundary for an occluded sector

Blocked:

- assuming a perfect circle when the source footprint is oval, irregular, broken, or asymmetric
- using only left/right radius to define a circular component
- approving a near-circular source-pixel preview without checking the measured world-space width/depth ratio
- letting cracks, symbols, labels, arrows, gridlines, or dimension text become perimeter stops
- using a shared origin to overwrite a component's measured asymmetric footprint center
- silently filling occluded sectors as measured visible data

The radial trace can produce a better filled contour and pixel count, but the resulting calculated footprint center must still be recorded separately. The shared origin can remain the snap/assembly axis while the component's true footprint center remains asymmetric.

If the source image uses different centimeter-per-pixel values on X and Y, a true oval can appear almost circular in raw pixel space. In that case the review must show a centimeter-normalized footprint next to the raw source-pixel overlay. The hard gate uses the measured world-unit ratio, not the visual roundness of the pixel preview.

When the source explicitly provides width and depth for a footprint and the visible top pixels are occluded or visually misleading, a measured oval or ellipse envelope may be used as a diagnostic or candidate footprint authority only if it is tagged as formula-derived, lists its exact width/depth ratio, and remains blocked until review approval. Do not replace irregular visible geometry with smoothing unless that replacement is explicitly approved.

## Source-Derived Snap Anchor Rule

Before component reconstruction or assembly, create source-derived snap anchors for every separable physical component and every measured attachment interface.

Snap anchors are named attachment points, lines, or perimeter IDs that allow components to reconnect by formula instead of visual fitting.

Required:

- create anchors from scan-verified source pixels
- record the source view and pixel coordinate or pixel line/perimeter
- record the physical layer/component that owns the anchor
- record the paired anchor ID on the adjacent component
- record the snap role: center, front, back, left, right, top, bottom, corner, edge, perimeter, or contact
- record the world-space meaning
- record allowed translation tolerance
- record allowed yaw, pitch, and roll tolerance
- record whether the anchor controls position, orientation, scale, or contact only
- record whether the anchor is overlay-only, hidden non-shipping, or source-authored
- prove anchors are excluded from texture, mesh, render, and export unless explicitly source-authored

Blocked:

- manually moving components after reconstruction to make anchors appear to fit
- creating anchors from old renders, old meshes, old generator data, or visual memory
- using bounding-box centers as snap anchors for non-rectangular components
- using one component's anchors to deform, stretch, taper, or reorient another component

During assembly, paired anchors must snap together within tolerance. If anchor pairs disagree, stop and apply the disagreement rule before moving geometry.

For non-rectangular, ring-shaped, irregular, broken, organic, tapered, or visibly asymmetric components, snap-anchor passes must reference the approved pixel-count center manifest before declaring center anchors.

Printed guide centers, shared review centers, and bounding-box centers are comparison evidence only unless explicitly approved as the center authority.

## Reusable Source Component Rule

When a source contains separable physical pieces, each piece must be treated as a reusable source component before final assembly.

A source component is a measured, named, remakeable piece of an asset. It may later be reused by itself, used in a modular set, or assembled into a larger final asset.

Required for each reusable source component:

- stable component name
- source view ownership
- scanline proof
- crop-boundary formula
- component mask or contour formula
- pixel-count center
- orientation marks
- snap anchors or contact markers, if it attaches to another component
- material and texture source ownership
- UV ownership rule
- collision rule, if reusable in game
- Unreal naming recommendation, if exported separately
- final role: standalone mesh, mesh section, Blueprint child component, or archived construction component

The final game asset may be exported as:

- separate reusable Static Mesh components assembled in a Blueprint Actor
- a combined performance mesh created from preserved source components
- both, when reuse and runtime performance both matter

If components are combined for runtime, the original separated component blueprints, formulas, masks, centers, anchors, and source ownership records must still be preserved. Combining for performance must not erase component lineage.

Do not merge, weld, rename, or discard separated source components in a way that prevents future reuse or forensic review.

## Start-To-Finish Process

### 1. Approved Source Intake

Start with approved visual source files only.

Record:

- source file path
- source role
- approval status
- whether it is visual canon, reference, template, or inferred support
- whether the source contains multiple separate physical pieces

If the asset has multiple pieces, identify them before any geometry work. Use generic names such as:

- primary object
- support object
- separate component
- attachment piece
- occluded interface area
- trim or socket piece

Do not use asset-specific language such as "axe stone" in reusable rules.

### 2. Lossless Scanline Capture

Before deriving geometry, silhouettes, contours, measurements, masks, or texture guides from a raster image, create a scanline capture.

Required proof:

- `max_rgb_delta=0`
- `changed_pixels=0`
- target and rebuilt pixel hashes match
- `pixel_exact=true`

If scanline proof fails, stop. Do not model from that source.

### 3. Source Decomposition

If the source is a collage, template, turnaround sheet, contact sheet, or board, split it into individual views and components.

Separate visible physical layers before assembly, even if they come from one source image.

If the source shows distinct stacked or touching layers, each layer must become its own measured component at a clean measured level line or contact line before geometry construction. Examples include:

- lower base or support footprint
- upper ring, collar, plinth, cap, socket, or contact layer
- primary object
- rubble, debris, trim, skirt, or scatter layer

Do not let one component inherit another component's taper, side profile, normals, UVs, center, contact line, or orientation. A ring/collar/support layer under a primary object must not be treated as part of the primary object's side geometry unless source evidence proves it is the same physical piece.

For each extracted view, record:

- source crop box
- crop-boundary formula or source landmark proof
- object mask path
- geometry measurement mask path
- whether the geometry measurement mask is formula-derived or inferred
- visible pixel crop path
- view name
- view role
- component ownership
- physical layer identity
- clean measured level/contact line, if the component is stacked or touching another component
- reusable source component ID
- intended reuse role: standalone, modular, assembly-only, collision-only, or archived construction component
- final assembly relationship to adjacent components
- whether the crop is exact source data or inferred

Texture/material masks and diagnostic object masks must be labeled as diagnostic unless they are explicitly approved as geometry inference. A diagnostic mask cannot own visible geometry.

### 4. Pixel Convention

Declare the pixel measurement convention before calibration.

Required decision:

- inclusive pixel span
- exclusive pixel span
- center-to-center pixel distance
- edge-to-edge pixel distance

Do not mix conventions in the same pass. One-pixel differences can produce scale and alignment errors.

### 5. Coordinate Frame

Every asset must declare a coordinate frame before modeling.

Record:

- world up axis
- forward axis
- front direction
- back direction
- left direction
- right direction
- top direction
- origin
- pivot
- centerline
- per-component yaw, pitch, and roll

Do not rotate or shift components to make the render look right unless source evidence proves the rotation or shift.

### 6. Registration Marks

Every separate physical component should have orientation identity.

Before any component is moved, cropped for geometry, rotated, centered, rebuilt, or assembled, mark and record source orientation pixels from the scan-verified source.

For production templates, add hidden, review-only, or non-shipping registration marks before scan capture when possible. If the source already exists and cannot be altered, create a separate orientation-pixel manifest and overlay from the scan-verified source without modifying the source image.

Required marks:

- front
- back
- left
- right
- top
- component center
- source-view centerline
- component-to-component contact relationship
- surface/facet angle identity
- exterior edge correspondence
- corner seam correspondence
- height station correspondence
- per-surface normal owner
- intended yaw offset, if any
- component identity
- exterior seam correspondence marks or edge-loop IDs when separate pieces will meet visibly

For any build that assembles multiple source views into one 3D object, add a surface-angle and edge-correspondence marker layer before geometry construction or reassembly.

Required surface-angle and edge-correspondence marks:

- front-left seam ID
- front-right seam ID
- back-left seam ID
- back-right seam ID
- top-front edge ID
- top-back edge ID
- top-left edge ID
- top-right edge ID
- support/contact perimeter IDs where components meet
- height station markers including `0 cm`, contact/support height, key mid-height rows, and maximum height
- per-surface normal owner, such as front `-Y`, back `+Y`, left `-X`, right `+X`, and top `+Z`

For stacked physical layers, also mark:

- lower-layer top contact line
- upper-layer bottom contact line
- upper-layer top contact line
- primary-object bottom contact line
- visible ring/collar inner perimeter
- visible ring/collar outer perimeter
- layer-specific pixel-count center
- layer-specific front/back/left/right direction pixels
- layer-specific yaw/pitch/roll reference pixels
- layer-to-layer contact perimeter IDs
- layer-to-layer no-inheritance proof, confirming the upper layer does not inherit the primary object's taper, normals, UVs, center, or side shell
- source-derived snap anchor IDs for each layer and paired adjacent layer

Required orientation-pixel record fields:

- source file
- source scanline manifest
- component name
- source view
- orientation pixel label
- pixel coordinate
- world meaning
- whether the mark is source-authored, overlay-only, or hidden non-shipping
- whether the mark is excluded from texture, mesh, render, and export
- edge/seam ID, if the mark is used for reassembly
- height station, if applicable
- normal owner, if applicable
- physical layer name, if applicable
- contact line name, if applicable
- paired marker ID on the adjacent component or view, if applicable
- inheritance rule, if the marker prevents one component from inheriting another component's geometry
- snap anchor ID and paired snap anchor ID, if applicable
- snap role, if applicable
- allowed translation and rotation tolerance, if applicable

Orientation marks are measurement evidence, not visible asset detail. They must not alter source pixels, visible textures, generated mesh, review renders, or exported game assets unless explicitly approved as source-authored visible marks.

If registration marks are missing, cross-piece orientation, offsets, and hidden contact geometry are inferred until approved.

### 7. Calibration

Convert pixels to real measurements per source view.

Record:

- source view
- pixel span
- real span
- centimeters per pixel
- formula used to convert pixels to centimeters
- formula used to convert centimeters to polygon vertices
- pixel convention
- calibration confidence

Do not reuse calibration from a different view unless explicitly documented.

Calibration boxes do not automatically define component centers. Component centers must be derived using the Pixel-Count Center Rule unless the component is truly rectangular and approved as such.

### 8. Measurement Contract

Every visible geometry feature must have a measurement contract.

Required fields:

- feature name
- component name
- source view
- source pixels
- pixel-to-world formula
- pixel-count center formula, if the feature is used for alignment, contact, origin, or reassembly
- center authority type, such as raw visible-pixel, filled footprint, outer contour, inner contact perimeter, visible annulus, or review-only assembled center
- top-contour classification, such as independent footprint, shared stacked-layer envelope, visible annulus, occluded inferred footprint, or review-only assembled footprint
- annotation/background exclusion method, if the source view includes labels, arrows, dimensions, gridlines, borders, or guide marks near the component
- seed pixel and connectivity rule, if a seed-connected center or contour is used
- radial trace origin, angle step, perimeter stop rule, visible/occluded/inferred angular sectors, and filled contour path, if a radial perimeter trace is used
- formula-derived measurement mask, if a mask defines geometry ownership
- pixel measurement
- centimeter measurement
- expected value
- observed generated value
- error
- tolerance
- selection method
- visible or inferred

If a visible feature has no measurement contract, it is not ready for modeling.

The measurement contract must reference the formula record that created it. Measurements without a formula link are diagnostic only and cannot drive visible geometry.

### 9. Accuracy Measurement Rule

Visible geometry must be driven by accuracy measurement, not by average-based compromise.

For every generated visible feature:

```text
error = absolute difference between source-expected measurement and generated-observed measurement
```

The feature passes only if:

```text
error <= declared tolerance
```

This rule applies to all geometry types:

- stones
- bases
- panels
- walls
- roofs
- weapons
- armor plates
- creature parts
- modular building pieces
- props
- terrain cuts
- attachment sockets

### 10. No Hidden Averaging

Visible geometry must not use averaged measurements to hide disagreement.

Blocked methods for visible geometry:

- average
- mean
- smoothed average
- blended average
- visually adjusted midpoint
- unreported interpolation
- "looks right" correction

Allowed methods for visible geometry:

- exact source measurement
- source-priority measurement
- outer envelope
- inner envelope
- direct constraint

If views disagree, report the disagreement. Do not silently solve it.

### 11. Source Ownership

Each visible surface or edge needs a source owner.

For multi-component assets, the source owner must include the specific component. A measurement for one component must not be taken from a crop, mask, row span, contour, or silhouette that includes another component.

Component source lineage must also be explicit. A support, base, pedestal, socket, trim, or contact-mount component must not be copied, resized, projected, or inherited into a primary component unless the source proves it is the same physical piece. If a new layer or subcomponent exists, it needs its own source owner and measurement contract.

Examples:

- top view owns XY footprint
- front view owns front silhouette
- side view owns depth profile
- back view owns rear silhouette
- detail view owns local ornament placement

For stacked or touching components:

- top-down component footprint owns maximum XY size for that component
- component-isolated front/back masks own that component's width-by-height profile
- component-isolated left/right masks own that component's depth-by-height profile
- each distinct physical layer has its own source owner, measurement contract, center, contact line, and normal ownership
- full-object masks may validate the assembled object only, not an individual component
- base, support, pedestal, socket, trim, or contact-mount pixels must never validate the primary object dimensions
- base, support, pedestal, socket, trim, or contact-mount layers must never be copied, resized, or projected onto/into the primary object

If two views claim the same edge and disagree, apply the disagreement rule.

### 12. Disagreement Rule

When source views disagree:

1. Stop and report the conflicting measurements.
2. Identify the affected feature.
3. Choose one declared method:
   - source priority
   - outer envelope
   - inner envelope
   - exact source override
   - approved inference
4. Record why the method is correct.
5. Validate the generated measurement against that declared method.

Do not average the disagreement away.

### 13. Geometry Construction

Visible geometry must come from measured source pixels, measured contours, measured profiles, or declared constraints.

Component geometry must be generated from component-specific measurements.

Build distinct physical layers independently before attachment. A lower base, upper ring/collar/support layer, primary object, rubble skirt, or other visible layer must be generated from its own formula-owned measurements and then attached by a measured contact interface. Do not merge a ring/collar/support layer into the primary object's side shell during reconstruction.

Preserve each independently built physical layer as a reusable source component record even if the review or runtime asset later uses a combined mesh. Component reuse records must include formulas, centers, masks, anchors, material ownership, UV ownership, and final assembly relationship.

Do not create a new visible component layer by copying and scaling another component's ring, contour, mesh, UV island, or texture layer. A copied/resized component layer is treated as contaminated geometry unless it is explicitly measured as its own source component.

Do not use one full top cap to texture a multi-component contact surface when a primary component sits on a support/base component. Any visible support/base top surface must be generated from its own formula-derived source ownership and must stay outside the primary component measurement mask. Do not create annulus, bridge, hidden-drop, or contact-fix geometry unless the Blueprint rule and implementation change are approved first.

Required for stacked or touching objects:

- top contour for that component's XY footprint
- front/back profile from masks that isolate that component
- left/right profile from masks that isolate that component
- formula-derived component masks for geometry ownership
- clean measured level/contact line separating each physical layer
- exact component placement
- orientation mark alignment
- component lineage proof showing the component was not copied or resized from another component
- support/base top-surface proof showing visible support pixels stay outside the primary component mask
- reusable source component record for each separated piece

If a side/front mask includes support/base pixels, it cannot be used as the primary object's width or depth.

Do not replace visible measured geometry with:

- ellipse
- superellipse
- arbitrary smoothing
- procedural approximation
- generic primitive fitting
- stretch patch
- detached projection shell
- manually tuned visual fit

These can be used only as temporary diagnostics or explicitly approved inferred geometry.

### 14. Component Alignment

Before assembly, verify each component:

- orientation
- centerline
- pixel-count center
- contact edge
- surface/facet angle markers
- exterior edge correspondence markers
- corner seam correspondence markers
- height station correspondence markers
- per-surface normal owner
- scale
- yaw
- pitch
- roll
- source owner
- expected relationship to adjacent components

Component alignment must be measured, not eyeballed.

For non-rectangular components, use the pixel-count center as the primary alignment center. Bounding-box center is allowed only as a comparison or calibration reference.

Do not assemble multi-view surfaces until edge and angle correspondence is declared. If a surface changes direction, tapers, slopes, or meets another view-derived surface, its seam IDs and normal owner must be recorded before the mesh is generated.

Do not assemble stacked physical layers until layer separation markers are declared. Each layer must have its own:

- clean measured top and bottom contact line
- pixel-count center
- orientation pixels
- seam/edge correspondence IDs
- contact perimeter IDs
- source-derived snap anchors
- normal owner
- no-inheritance proof

Layer attachment must use those markers and the contact interface. It must not use inherited taper, inherited side normals, copied UVs, copied contours, or visual fit.

### 15. Contact And Attachment Interface

Where one component attaches to another, define a contact or attachment interface.

Required fields:

- primary object
- support object
- physical layer names on both sides of the contact
- clean measured level/contact line
- paired contact marker IDs
- paired snap anchor IDs
- pixel-count center for each contacting layer
- contact perimeter IDs
- no-inheritance proof for each layer
- contact surface source
- expected contact height
- observed contact height
- gap or overlap
- tolerance
- center offset
- yaw/pitch/roll relationship
- visible or occluded

No artificial lift, hidden gap, visual patch, or unreported offset is allowed.

If visible source evidence shows more than one stacked contact level, preserve those contacts as separate measured layer intervals. Do not collapse a primary object, ring/collar/socket, and support object into one support-height contact formula.

Required for multi-level visible contacts:

- top contact line for each intermediate layer
- bottom contact line for each intermediate layer
- per-view contact height in pixels and world units
- per-view layer thickness in pixels and world units
- proof that each interval is measured, not averaged
- declaration of whether the interval is geometry authority, texture/visible-profile authority, or diagnostic only

If a printed/global height guide disagrees with visible contact lines, stop and record the disagreement. The global height guide may remain calibration evidence, but it must not overwrite source-visible contact intervals unless Flamestrike approves that correction.

For visible contact interfaces:

- gaps fail
- unapproved center offsets fail
- unapproved rotation offsets fail
- stretch fixes fail

For hidden contact interfaces:

- inference is allowed only when tagged
- the inferred area must not override visible source data

### 16. Exterior Edge Weld

Zero-gap contact is not proof of welded exterior geometry.

If two pieces, panels, shells, planes, or view-derived surfaces meet on a visible outside edge, that seam must be classified and validated before review.

Required seam classifications:

- visible exterior seam
- interior seam
- occluded contact seam
- inferred hidden seam

Required fields for each visible exterior seam:

- seam name
- edge role: `exterior_perimeter`, `interior_edge`, `contact_mount`, `occluded_edge`, or `inferred_hidden_edge`
- weld scope: `exterior_only`, `contact_alignment_only`, or `no_weld`
- participating components or surfaces
- source owner for each side
- source seam marker IDs for each side
- normal owner for each participating surface
- height station IDs where applicable
- expected edge-loop pixels or measured boundary
- observed generated edge-loop vertices
- maximum exterior edge gap
- welded or shared vertex count
- expected welded or shared vertex count
- unwelded exterior edge count
- seam bridge status, if a bridge is used
- UV edge source, including whether it samples visible source pixels or tagged inferred padding
- tolerance
- pass or fail

For visible exterior seams:

- outer edge loops must align to the same measured boundary
- only edges with `edge_role=exterior_perimeter` may be welded as visible exterior seams
- the seam must use shared vertices or a documented perimeter-only seam bridge that is part of the unified exterior mesh
- if the visual issue looks like two pieces need to be pushed together, push/align the measured exterior perimeter edges and validate contact; do not create an interior bridge
- zero gap, coplanar overlap, or visual closeness alone fails
- same-plane annulus bridges, concentric-loop bridges, contact-mount bridges, or interior-wall bridges fail as exterior weld fixes
- detached strips, patch shells, stretch fixes, or cover-up planes fail
- visible UVs must not sample source-crop background or untagged padding

For interior, hidden, or occluded seams:

- do not weld, stretch, or deform inner edges unless the contact interface requires it
- do not bridge across interior/contact space to make an exterior seam appear closed
- preserve component meaning when it affects later editing, collision, sockets, or animation
- tag any inferred hidden fill separately from measured visible data

### 17. Inferred Surface Fill

When source data is missing because an area is hidden, occluded, cropped, damaged, or not provided, the area may be filled only as a tagged inferred surface.

Preferred methods:

- sample matching visible areas from the same material or object
- copy related pixel color
- copy texture density
- copy grain, cracks, wear, edge darkness, and pattern scale
- use sample-based texture synthesis
- use texture brushing
- use patch-based inpainting

Hard limits:

- do not use inferred fill on visible measured canon surfaces
- do not let inferred fill change measured geometry
- label the area as `inferred_surface_fill`
- record the source sample area used
- show inferred areas separately if they affect approval

### 18. Texture And Color

Visible source pixels must copy exactly into visible texture outputs.

Blocked for visible canon pixels:

- Lanczos filtering
- bilinear filtering
- bicubic filtering
- color averaging
- unreported alpha bleed
- lighting-based color approval
- color correction without approval

Allowed:

- exact RGB copy
- nearest-copy placement when resolution changes are explicitly required
- native per-view texture
- exact-copy atlas placement
- tagged inferred texture synthesis for missing hidden areas

### 19. UV And Atlas

If an atlas is used, visible source pixels must remain exact.

Atlas packing must record:

- source texture
- atlas region
- whether pixels were copied exactly
- whether any filtering was used
- whether the region is visible or inferred

If atlas packing changes visible color, do not use that atlas for approval. Use native textures or exact-copy atlas placement instead.

### 20. View-Owned Surface Mapping

Every visible surface must use the source view that owns that surface.

Required ownership rule:

- front-facing surfaces use the front source view
- back-facing surfaces use the back source view
- left-facing surfaces use the left source view
- right-facing surfaces use the right source view
- top-facing surfaces use the top source view
- inferred hidden surfaces use only tagged inferred fill

Required UV scale rule:

- a visible face may not stretch a full source panel across a smaller measured face
- a visible face may not sample another side's source view
- a visible side face must sample inside that source view's measured visible row span at the matching height
- a visible top face must sample inside the measured top footprint
- edge padding may be used only when tagged and only where the measured visible source does not exist

Required all-angle review rule:

- front, front-right, right, back-right, back, back-left, left, front-left, top, and beauty renders must be generated for visual review when a multi-view asset is assembled
- the verifier must check that each visible face's UVs land in the atlas region owned by its outward surface direction
- the verifier must fail if a back-facing surface samples the front view, a side-facing surface samples the wrong side, or any visible side face samples outside its measured row span

### 21. Seam Resolution

Seams must be solved by measurement, orientation, contact, or UV correction.

Stretch strips, seam patches, detached shells, or visual cover-ups are diagnostic only. They cannot be final fixes for visible seams.

### 22. Proof Renders

Produce separate proof outputs for separate questions.

Required proof types:

- color proof: unlit, exact texture check
- geometry proof: measurement, edge, and contact check
- orientation proof: top/front/side registration check
- beauty proof: aesthetic review only

Do not use a lit beauty render to approve exact pixel color.

### 23. Pre-Render Audit

Before rendering for review, verify:

- scanline source is exact
- source orientation pixels were marked before crop-for-geometry, movement, rotation, centering, rebuilding, or assembly
- orientation-pixel manifest and overlay exist for every separable component
- surface-angle and edge-correspondence markers exist before multi-view reassembly
- every exterior seam has source seam IDs, normal owners, and height station correspondence where applicable
- measurement formula manifest exists and contains every required Formula Archive Rule field
- non-rectangular component centers are pixel-count centers, not bounding-box assumptions
- footprint-center authority is declared for textured, cracked, highlighted, ring-shaped, or partially occluded components
- raw visible-pixel centers are not used for alignment unless approved as the declared center authority
- center masks exclude source-sheet labels, arrows, dimension marks, borders, gridlines, and unrelated artwork
- seed-connected center manifests record source window, seed pixel, connectivity rule, excluded detached-pixel count, and no-geometry proof when used
- seed-connected masks are visually compared against the source silhouette before becoming geometry authority
- visible edge clipping or non-object fragments in a seed-connected mask force reviewed-contour replacement before geometry
- snap-anchor center marks reference the approved pixel-count center manifest, not an old shared or printed guide center
- stacked top-view contours are classified as independent, shared envelope, visible annulus, occluded inferred footprint, or review-only assembled footprint
- no shared stacked-layer envelope is reused as independent geometry proof for multiple layers
- radial perimeter traces declare origin, ray count/angle step, stop rule, angular sector classification, filled contour, and center delta before becoming contour authority
- radial perimeter traces do not assume perfect circles unless the source explicitly proves a circular footprint
- distinct visible physical layers are separated at clean measured level/contact lines before assembly
- stacked-layer marker manifest exists when the source contains stacked layers
- each physical layer has top/bottom contact markers, pixel-count center, contact perimeter IDs, normal owner, and no-inheritance proof
- each attachment interface has source-derived paired snap anchors with declared translation and rotation tolerance
- geometry-defining crops, masks, component splits, scale, alignment, orientation, contacts, and seams are formula-derived
- texture/material masks are not used as geometry authority unless approved as inference
- calibration exists
- measurement contracts exist
- no visible averaging is used
- no unapproved inference touches visible canon geometry
- contact interfaces have no unapproved gaps
- every seam is classified as exterior, interior, occluded, or inferred hidden
- every visible exterior weld declares `edge_role=exterior_perimeter` and `weld_scope=exterior_only`
- visible exterior seams have welded/shared vertices or a documented unified seam bridge
- visible exterior seams have zero unwelded exterior edge count within tolerance
- visible exterior seam UVs do not sample crop background or untagged padding
- contact, interior, occluded, and inferred-hidden seams have no same-plane annulus bridge, concentric-loop bridge, or interior bridge used as an exterior fix
- component centers and rotations match declared source evidence
- component source lineage proves no support/base layer was copied, resized, projected, or inherited into the primary component
- every separated physical component has a reusable source component record before final assembly
- combined runtime meshes preserve links back to their source component records
- visible texture pixels remain exact
- visible surfaces use their owned source view
- primary component top UVs stay inside the primary component top mask, not the full support/base top mask
- support/base top UVs stay outside the primary component top mask
- tapered or sloped side faces use actual generated polygon normals for source-view ownership, not vertical-wall assumptions
- visible side-surface UVs stay inside the source view's measured visible row span
- all required cardinal, diagonal, top, and beauty review angles exist
- inferred areas are tagged

If any item fails, do not render for approval.

### 24. Hard Validation Gate

The hard validation gate confirms the rules above. It should not be where the process first discovers known problems.

The gate must fail on:

- non-exact scanline evidence
- missing orientation-pixel manifest before geometry decomposition or assembly
- component moved, cropped for geometry, rotated, centered, rebuilt, or assembled before orientation pixels were recorded
- missing surface-angle or edge-correspondence markers before multi-view geometry assembly
- visible exterior seam without source seam IDs, normal owners, or required height station correspondence
- missing or incomplete measurement formula manifest
- visible geometry measurement without a formula-record link
- non-rectangular component aligned from bounding-box center instead of pixel-count center
- raw visible-pixel color-density center used for alignment on a textured, cracked, highlighted, ring-shaped, or partially occluded component without approval
- center mask includes source-sheet labels, arrows, dimension marks, borders, gridlines, background, or unrelated artwork
- center authority type missing for a component used in alignment, contact, origin, scale, or reassembly
- seed-connected center pass missing declared source window, seed pixel, connectivity rule, or excluded detached-pixel count
- seed-connected mask used as geometry authority after visibly clipping a true object edge or including annotation fragments
- reviewed source-owned contour missing after seed-connected mask disagreement
- snap-anchor center mark uses a printed/shared guide center when a pixel-count center manifest exists
- asymmetric component recentered by eye to a printed guide without source proof
- top-view stacked-layer contour reused as independent geometry authority for multiple layers without shared-envelope classification
- top view cannot separate vertical layers, but side/front/back component profiles and tagged inferred hidden footprints are missing
- radial trace used without declared origin, angle step, perimeter stop rule, angular sector classification, filled contour, or center delta
- circular radius used for an oval, irregular, broken, asymmetric, or unproven footprint
- radial trace uses source-sheet labels, arrows, gridlines, dimension marks, or unrelated artwork as perimeter stops
- top-down oval, circular, ring, irregular, broken, organic, or tapered footprint treated as a rectangle for final center or geometry ownership
- distinct visible physical layer merged into the wrong component
- ring, collar, plinth, socket, cap, or support layer treated as primary-object side geometry without source proof
- missing clean measured level/contact line between stacked physical layers
- missing stacked-layer marker manifest when stacked layers exist
- physical layer without pixel-count center, contact perimeter IDs, normal owner, or no-inheritance proof
- layer attachment driven by inherited taper, inherited normals, copied UVs, copied contours, or visual fit
- separated physical component missing a reusable source component record
- combined runtime mesh missing lineage back to separated source components
- component reconstruction or assembly attempted before source-derived paired snap anchors exist for measured attachment interfaces
- snap anchor derived from a bounding-box center for a non-rectangular component
- paired snap anchors disagree beyond tolerance without applying the disagreement rule
- geometry-defining crop, mask, split, scale, alignment, orientation, contact, or seam without a declared pixel-to-world formula
- diagnostic/threshold/blob mask used as visible geometry authority without approved inference
- missing measurement contracts
- visible geometry without source ownership
- component measurement missing component ownership
- primary component measurement taken from full-object/base/support/pedestal mask
- copied, resized, projected, or inherited support/base layer inside the primary component
- primary component top UV sampling outside the primary component top mask
- support/base top UV sampling inside the primary component top mask
- sloped/tapered side faces classified with stale vertical-wall source-view logic
- visible geometry using blocked averaging methods
- observed measurement error greater than tolerance
- unapproved contact gaps
- unapproved center offsets
- unapproved yaw, pitch, or roll offsets
- missing seam classification
- visible exterior weld missing `edge_role=exterior_perimeter`
- visible exterior weld missing `weld_scope=exterior_only`
- zero-gap contact used as proof of a welded visible exterior seam
- same-plane annulus bridge, concentric-loop bridge, contact-mount bridge, or interior bridge used as a visible exterior seam fix
- visible exterior seam max gap greater than tolerance
- visible exterior seam with unwelded exterior edges
- detached seam strip, patch shell, cover-up plane, or stretch pass used as final visible geometry
- visible seam UV sampling crop background or untagged padding
- visible surface sampling the wrong source view
- back-facing surface sampling front-view pixels, or any cardinal side sampling another side's pixels
- visible side-surface UV outside the measured visible row span for that source view
- missing all-angle review coverage
- inner, hidden, or occluded edge welded or deformed without a declared contact requirement
- visible texture color drift
- filtered visible atlas pixels
- inferred data used on visible canon surfaces
- stretch strips or patch shells used as final visible seam fixes

If the gate fails, stop and fix the data path first.

### 25. Review Presentation

Only after the hard gate passes should the review image be presented as approval-ready.

When a visual is requested, open the actual image file for review. Do not merely describe it.

Show:

- color proof
- geometry proof
- orientation proof
- beauty render
- validation report

### 26. Unreal Handoff

A DCC candidate is not fully game-ready until Unreal import and validation are complete.

Unreal handoff must include:

- asset name
- folder path
- FBX path
- texture paths
- material plan
- LOD plan
- collision plan
- pivot
- scale
- orientation
- validation reports
- inferred-area notes
- approval status

Use the project status vocabulary:

- `DCC source candidate`
- `DCC game-ready candidate`
- `Unreal import candidate`
- `Gameplay validated asset`
- `Approved library asset`

### 27. 3D Game Asset Blueprint Archive

Once an asset is successfully created, store a reusable 3D Game Asset Blueprint for that asset.

The blueprint is the permanent reconstruction and problem-solving record. It must make the asset remakeable without relying on memory, chat history, or prior generated images.

Store the blueprint in git with the project documentation.

Recommended path:

```text
docs/assets/blueprints/[asset_type_or_family]/[ASSET_NAME]_3D_GAME_ASSET_BLUEPRINT.md
```

Each blueprint must include:

- asset name
- asset type or family
- approved source images
- scanline proof paths
- source hierarchy
- measurement contracts
- coordinate frame
- component list
- reusable source component records
- registration marks
- contact and attachment interfaces
- seam classifications
- exterior edge weld measurements
- welded/shared vertex proof
- seam UV edge proof
- inferred surface areas
- texture and material source rules
- UV and atlas rules
- LOD plan
- collision plan
- Unreal import settings
- validation reports
- proof render paths
- final approval status
- known issues encountered
- solutions that worked
- solutions rejected and why
- remake instructions

Reusable source component records must include:

- stable component ID
- source files and scanline proofs
- formulas, masks, contours, and pixel-count centers
- orientation marks and snap/contact anchors
- material, texture, UV, collision, and scale ownership
- whether it can be exported as a standalone mesh
- whether it is used only as an archived construction component
- final assembly relationship to parent or adjacent components
- combined runtime mesh lineage, if applicable

The blueprint must also include an asset-type lessons section so future assets can reuse the solution. If a problem recurs on another asset, check the relevant 3D Game Asset Blueprints before inventing a new fix.

An asset is not considered complete until its 3D Game Asset Blueprint has been written and committed to git.

## Known Failure Response Table

| Failure | Likely Cause | Required Response |
| --- | --- | --- |
| Pixel color is off | Atlas filtering, material color management, lighting, color correction, alpha bleed | Check visible texture exactness, atlas regions, shader mode, and unlit color proof. Use exact copy or native textures. |
| Geometry crop or mask is not pixel-perfect | Crop/mask was made by threshold cleanup, largest-blob cleanup, visual fitting, or remembered constants instead of a declared pixel-to-world formula | Stop before modeling. Recreate the crop/mask from full scanline evidence using a declared formula, or document the mask as diagnostic only. |
| Oval or irregular base is centered wrong | Bounding-box center was used instead of actual source-owned pixel-count center | Recompute center from the counted footprint pixels. Treat bounding box as calibration only. |
| Pixel-count center is pulled toward cracks, symbols, highlights, or shadows | Raw visible color-density center was used as alignment authority for a textured or broken footprint | Treat raw visible-pixel center as diagnostic. Derive alignment from the measured footprint contour, filled source-owned footprint, annulus formula, or perimeter formula. |
| Pixel-count center includes labels or dimension marks | Count window or object mask included source-sheet annotations, arrows, borders, guide lines, or text | Reject the pass. Tighten the object window, add an annotation exclusion mask, or use a source-owned contour before any geometry or snap anchor authority. |
| Detached annotation pixels stretch the footprint mask | Row-span or threshold method connected unrelated label/dimension pixels to the object | Use a seed-connected object mask or explicit annotation-exclusion mask. Record the seed pixel, connectivity rule, excluded detached-pixel count, and filled-footprint/contour formula. |
| Seed-connected mask clips a true edge | Light object-edge pixels, highlights, compression, or source artifacts failed the object-pixel test | Reject the seed mask as geometry authority. Replace it with reviewed source-owned contour/perimeter points and record the rejected mask plus replacement formula. |
| Ring or socket center is ambiguous | Outer footprint, inner contact perimeter, visible annulus, and filled footprint centers were not separated | Record each center type separately and declare which one controls each attachment interface. Do not substitute center types silently. |
| Component looks off-center against a printed guide | The physical source footprint is asymmetric, or the guide is only a review/calibration mark | Compare the pixel-count footprint center, printed guide center, and orientation marks. If the component is genuinely asymmetric, keep the measured source center and do not recenter by eye. |
| Stacked layers have nearly identical top contours | Top view shows a shared outer envelope and cannot independently separate upper/lower vertical layers | Mark the contour as a shared stacked-layer envelope. Use side/front/back profiles, contact lines, and snap anchors to separate layers; tag occluded footprints as inferred instead of duplicating the contour as independent proof. |
| Radial contour becomes too circular | A left/right radius or single radius was used instead of source-owned perimeter points around the full footprint | Reject the pass. Resample the perimeter at many angles from the shared origin and classify visible/occluded/inferred sectors. Do not assume a circle unless the source proves one. |
| Oval footprint appears circular in source pixels | X and Y pixel scales differ, so raw pixel-space preview hides the world-space width/depth ratio | Do not judge the footprint by raw pixel appearance alone. Show the raw source-pixel overlay and the centimeter-normalized footprint side by side, then validate against the measured world-unit width/depth ratio. |
| Radial trace hits labels or dimension marks | The ray stop rule accepted source-sheet annotation instead of object perimeter | Add annotation exclusion or reviewed perimeter stops. Labels, arrows, gridlines, borders, and dimensions cannot own geometry. |
| Shared origin erases asymmetric component center | Assembly origin was confused with the component's true footprint center | Keep both values. Use shared origin for snapping only when approved; record the radial contour's calculated footprint center and delta. |
| Top footprint treated as a rectangle | The support/base/object footprint was boxed instead of measured as its true oval, ring, or irregular contour | Stop before geometry. Derive the footprint contour and center from source-owned pixels. |
| Upper ring/collar tips inward with the primary object | The ring/collar/support layer was treated as part of the primary object's side shell and inherited its taper or normals | Separate the ring/collar/support layer at a clean measured level/contact line. Build it as its own component, then attach it by measured contact. |
| Distinct stacked layers deform each other | Lower base, upper ring/collar, primary object, or rubble/debris were merged before measurement | Decompose into physical layers first. Each layer needs its own formula-owned measurements, center, source owner, and contact interface. |
| Multiple visible contact levels are collapsed into one height | The build forced a single support-height formula even though the source shows separate primary-to-ring and ring-to-support levels | Stop before geometry. Record each visible contact as its own measured interval per view. Do not average or overwrite the source-visible interval with a global guide unless approved. |
| A separated piece cannot be reused later | The piece was merged into the final mesh without a reusable source component record | Recreate or recover the source component record before final approval. Preserve formulas, masks, centers, anchors, UV ownership, material ownership, and final assembly relationship. |
| Combined runtime mesh cannot be audited | Component lineage was lost during weld/combine/export | Fail the asset. The combined mesh must reference the preserved source component records used to create it. |
| Components do not reconnect cleanly after independent reconstruction | No source-derived snap anchors existed, or paired anchors were not validated before assembly | Create paired snap anchors from source pixels before reconstruction. Snap by anchor ID and validate translation/yaw/pitch/roll tolerance before attachment. |
| Component orientation drifts after clean scan | Orientation pixels were not marked before crop, movement, rotation, centering, rebuild, or assembly | Stop. Create an orientation-pixel manifest and overlay from the scan-verified source before continuing. |
| Surface angles drift during reassembly | The build had global orientation markers but no surface-angle, edge-correspondence, normal-owner, or height-station marker layer | Stop before geometry. Add surface-angle and edge-correspondence markers, then declare the reassembly formula. |
| Diagnostic mask starts driving geometry | Texture/material/object detection was treated as measurement authority | Reject the pass. Geometry ownership must use formula-derived measurement masks unless inference is approved first. |
| Build cannot be recreated from documentation | Formula record is missing, incomplete, or stored only in a script/chat memory | Stop. Write the formula archive into the measurement manifest and final asset blueprint before proceeding. |
| A fresh pass reproduces old failures | Prior asset-specific generator logic, hidden constants, contact tricks, or old assumptions were copied forward | Delete the contaminated pass and restart from original source evidence plus neutral utilities only. Prior pass logic may inform rules, not implementation. |
| Black line near contact | Contact gap, duplicate shell, shadow, detached patch, z-fighting | Measure contact interface, check z gap, check duplicate geometry, render geometry proof. |
| Component appears twisted | Wrong orientation, missing registration marks, top-down mismatch, yaw drift | Recheck coordinate frame, top source, piece marks, yaw/pitch/roll, and centerline. |
| Base/support object looks wrong | Support contour replaced by approximation, scaled after capture, wrong source ownership | Rebuild from measured top contour or declared source owner. Do not post-scale without measurement report. |
| Primary object too large for base/support | Primary object was measured from a full-object mask that included base/support/pedestal pixels | Rebuild with component-isolated masks. Top-down component footprint controls maximum XY size; side/front views control taper only after the component is isolated. |
| Base/support appears copied onto the primary object | Support/base layer was duplicated, scaled, projected, or inherited into the primary component; primary top UVs sampled the full top mask instead of the primary component mask | Remove the copied layer. Rebuild with one independently measured support and one independently measured primary component. Validate component source lineage and primary-top-mask UV ownership. |
| Base/support top texture looks corrupted | Full top cap UVs smeared mixed support/primary pixels across one surface, or support top UVs sampled inside the primary mask | Replace the full cap with source-owned support top geometry, such as a measured annulus outside the primary component mask. Validate support top UVs never enter the primary component mask. |
| Sloped/tapered side faces show wrong source panels | UV ownership was classified with a vertical-wall shortcut instead of the generated polygon normal | Rebuild side UVs from actual generated polygon normals and validate all side faces against their owned source view. |
| Primary object does not sit correctly | Contact interface changed, artificial lift, center offset, wrong support orientation | Revalidate attachment interface and zero/unapproved gap. |
| Side seams do not meet | Edge measurements disagree, UV mismatch, orientation error | Use source-priority or envelope rule. Do not stretch-patch final seam. |
| Pieces touch but still look separated | Zero gap was validated but the visible exterior edge loops were not welded or bridged | Run exterior edge weld validation. Rebuild with shared exterior vertices or a unified measured seam bridge. |
| Pieces look pushed apart | Exterior perimeter edges are offset, but the fix was attempted with an interior/contact bridge | Push/align the measured exterior perimeter edges. Weld only `edge_role=exterior_perimeter`; do not bridge annulus/contact/interior loops. |
| Interior stepped bands appear | Same-plane annulus, concentric-loop, contact-mount, or interior edges were bridged as if they were exterior seams | Remove the interior bridge. Preserve interior/contact surfaces and validate exterior perimeter alignment instead. |
| White or empty strip appears on an exterior seam | UVs are sampling crop background, untagged padding, or a detached patch edge | Rebuild the seam UVs from visible edge pixels or tagged nearest-copy inferred padding. Validate edge source ownership. |
| Back, side, or diagonal view shows the wrong face image | Visible surface UVs are sampling the wrong source-view atlas panel, or a full source panel is stretched over a smaller measured face | Rebuild UVs with view-owned surface mapping. Classify faces by outward normal, sample only the owned source view, and validate UVs stay inside that view's measured visible row span. |
| Image scale looks wrong from an angle | Geometry may be correct but texture projection is not view-owned or is sampling outside the measured row span | Run the all-angle surface ownership verifier before changing geometry scale. Fix UV ownership/row-span mapping first. |
| Top surface warps | Wrong top contour, wrong source owner, post-fit deformation | Use top source contour and compare observed-vs-expected XY measurements. |
| Missing hidden area | Occluded or unavailable source data | Use tagged inferred surface fill from matching visible pixels. |
| Shape seems close but not exact | Procedural approximation replaced measured contour | Require measurement contract and source-derived contour/profile. |
| Gate fails late | Starting rules were not followed | Update the pre-render audit and process rule so it fails earlier next time. |

## Rule Origins From The Cairnstone Pass

These are the specific lessons that produced the current rules.

### Scanline Reconstruction

Finding: pixel-perfect scanline capture correctly rebuilt the source image.

Rule created: scanline proof is mandatory before raster-derived geometry or texture work.

### Pixel-To-Measurement Conversion

Finding: pixel data can define scale, edge length, color, and silhouette, but only when pixel convention and calibration are explicit.

Rule created: declare calibration and pixel convention before modeling.

### Pixel-Perfect Measurement Formula

Finding: the strongest method came from scanning the source exactly, then using source dimensions and pixel counts to define crops, component masks, scale, centers, orientation, contacts, and seams.

Rule created: all geometry-defining measurements must come from declared pixel-to-world formulas. Diagnostic masks can inspect texture pixels but cannot own visible geometry.

### Pixel-Count Centers

Finding: oval, ring, irregular, broken, tapered, or organic footprints can be miscentered if the build uses a rectangular bounding box center.

Rule created: alignment centers must come from actual counted source-owned pixels for the component footprint. Bounding boxes are calibration frames only unless the component is truly rectangular and approved as such.

Finding: raw visible color-density centers can be pulled away from the physical center by cracks, symbols, shadows, highlights, missing pixels, labels, and dimension marks.

Rule created: raw visible-pixel centers are diagnostic unless approved as the alignment authority. Physical alignment uses a declared footprint center type, such as filled footprint, outer contour, inner contact perimeter, or visible annulus, and the source count must exclude annotations and unrelated sheet marks.

Finding: detached source-sheet annotations can enter a row-span or threshold mask and silently bias the center, while a printed guide center can make a genuinely asymmetric footprint appear wrong.

Rule created: center passes near annotations must use seed-connected source pixels, explicit annotation exclusion, or reviewed source-owned contours. The pass must record the seed/window/connectivity/excluded-pixel evidence, and asymmetric measured centers must not be corrected to printed guides without source proof.

Finding: seed-connected masks can still fail when the true object edge is very light or interrupted by source artifacts.

Rule created: visually compare seed-connected masks against the source silhouette before geometry authority. If the mask clips a true edge or includes non-object fragments, reject it and use reviewed source-owned contour/perimeter points with an explicit replacement formula.

Finding: a top view can prove the assembled outer footprint while still failing to distinguish stacked vertical layers that overlap in that view.

Rule created: classify top contours as independent footprints, shared stacked-layer envelopes, visible annuli, occluded inferred footprints, or review-only assembled footprints. Do not reuse one shared envelope as independent proof for multiple components; separate stacked layers with side/front/back profiles, contact lines, snap anchors, and tagged inference for hidden areas.

### Shared-Origin Radial Perimeter Trace

Finding: a shared assembly origin can simplify top-view contour extraction when stacked components are oval, irregular, asymmetric, or hard to threshold by color.

Rule created: use the approved shared origin to cast many rays to source-owned perimeter points, fill the traced outline, and count the resulting pixels. The shared origin remains an assembly reference; the traced component still records its own calculated footprint center and delta. Perfect-circle assumptions, annotation hits, and untagged occluded sectors fail.

### Formula Archive

Finding: a working formula is only reusable if it is recorded outside the implementation script and can be reviewed, remade, and audited.

Rule created: every strict reconstruction pass must archive the exact measurement formulas in the build manifest and final 3D Game Asset Blueprint.

### Fresh Pass Clean Slate

Finding: a pass can use fresh source data and still fail if old asset-specific generator logic is copied forward.

Rule created: a fresh pass means fresh source evidence and clean generator logic. Prior failed passes may provide lessons and failure modes, not implementation bases.

### No Averaged Measurements

Finding: averaged measurements can hide view disagreement and produce geometry that matches no source.

Rule created: visible geometry cannot use averaging. Use exact source, source priority, or envelope.

### Orientation And Registration

Finding: separate components can look wrong when their source orientation is not locked before assembly.

Rule created: components need orientation identity and registration marks.

### Orientation Pixels Before Movement

Finding: once pieces are cropped, shifted, rotated, centered, or assembled, it becomes difficult to prove whether later alignment is source-correct or an accidental visual fit.

Rule created: mark and record orientation pixels from the scan-verified source before any geometry crop, movement, rotation, centering, rebuild, or assembly.

### Surface-Angle And Edge-Correspondence Markers

Finding: global front/back/left/right/top markers preserve overall orientation, but they do not prove that individual sloped surfaces, corners, seams, or edge loops reassemble at the correct angles.

Rule created: before multi-view geometry assembly, add surface-angle, edge-correspondence, corner seam, height-station, and per-surface-normal-owner markers. Geometry cannot be assembled until those markers are recorded and tied to the reassembly formula.

### Physical Layer Separation

Finding: stacked layers can deform or misalign when a ring, collar, support, base, or debris layer is treated as part of another component's side geometry.

Rule created: separate visible physical layers at clean measured level/contact lines before assembly. Each layer gets its own source owner, formula-owned measurement, center, orientation, contact interface, and normal ownership.

### Source-Derived Snap Anchors

Finding: independent components can be measured correctly and still reassemble incorrectly if there are no named attachment points proving where and how they snap together.

Rule created: create paired snap anchors from scan-verified source pixels before component reconstruction or assembly. Components attach by matching anchor IDs within declared translation and rotation tolerances, not by eyeballing or post-build visual fitting.

### Reusable Source Components

Finding: once a separated physical piece is welded or merged into a final asset without its own record, it becomes difficult to reuse, remake, audit, or repair without rebuilding the whole object.

Rule created: every separated physical piece must receive a reusable source component record before final assembly. The final runtime asset may be a Blueprint Actor, a combined mesh, or both, but the original component formulas, masks, centers, anchors, material ownership, UV ownership, and assembly relationship must remain archived.

### Contact Interface

Finding: a small artificial lift or offset can create visible lines, shadows, or mounting errors.

Rule created: contact interfaces need explicit expected and observed gap/offset checks.

### Exterior Edge Weld

Finding: separate pieces can have zero contact gap and still look visibly separated when the outside edge loops are not welded, shared, or bridged as one measured exterior mesh.

Rule created: visible exterior seams require seam classification, edge-loop correspondence, welded/shared vertex proof, and UV edge proof. Zero gap alone is not enough.

### Exterior-Only Weld Scope

Finding: welding or bridging an interior/contact annulus can pass a closed-mesh check while visibly creating stepped internal bands and leaving the exterior pieces looking pushed apart.

Rule created: exterior welds are allowed only on `edge_role=exterior_perimeter` with `weld_scope=exterior_only`. Contact, annulus, concentric-loop, occluded, and interior edges must not be used as exterior seam fixes.

### View-Owned Surface Mapping

Finding: a render angle can look like incorrect geometry scale when the copied texture pixels are exact but the visible face is sampling the wrong source-view panel or stretching outside that source view's measured row span.

Rule created: visible faces must be classified by outward surface direction and may sample only their owned source view. Cardinal, diagonal, top, and beauty review angles are required, and the verifier must fail wrong-view UVs or visible row-span violations before approval.

### Contour Preservation

Finding: replacing measured contours with analytic shapes can make the model look plausible but wrong.

Rule created: visible contours must come from source pixels or declared constraints, not generic fitted shapes.

### Texture Color Drift

Finding: filtered atlas resizing changed visible pixel color even when source crops were exact.

Rule created: visible texture pixels must remain exact through texture, atlas, and material proof paths.

### Inferred Surface Fill

Finding: missing hidden areas can be filled convincingly by sampling related visible material pixels.

Rule created: inferred fill is allowed only on tagged hidden/missing surfaces and must not override measured data.

### Proof Separation

Finding: beauty lighting can obscure color or geometry accuracy.

Rule created: color proof, geometry proof, orientation proof, and beauty proof are separate outputs.

### Hard Gate

Finding: validation discovered issues after visual review had already started.

Rule created: the hard gate is a confirmation step. The same checks must exist as start-of-process rules.

## Required Manifest Fields

Every strict pixel asset pass must output a manifest with:

- asset name
- source files
- source hierarchy
- scanline proof paths
- view crops
- masks
- calibration data
- pixel convention
- coordinate frame
- component list
- source ownership map
- measurement contracts
- selection methods
- inferred surfaces
- texture copy proof
- atlas region proof
- contact interface measurements
- seam classifications
- exterior edge weld measurements
- welded/shared vertex proof
- seam UV edge proof
- exterior-only weld scope proof
- orientation measurements
- validation report paths
- proof render paths
- approval status

## Measurement Contract Template

```json
{
  "feature": "primary_object_front_width_at_z_120cm",
  "component": "primary_object",
  "source_view": "front",
  "source_pixels": [42, 173, 188, 173],
  "pixel_measurement": 147,
  "cm_measurement": 76.42,
  "expected": 76.42,
  "observed": 76.421,
  "error": 0.001,
  "tolerance": 0.001,
  "selection_method": "exact",
  "visible": true
}
```

## Change Declaration Template

```text
Change:
Reason:
Source evidence:
Affected component:
Visible or inferred:
Expected measurement:
Tolerance:
Validation check:
Approval needed:
```

## Final Standard

The AetherForge process is evidence-driven, not experimental.

If a change is based on evidence, record the evidence.

If a surface is inferred, tag it.

If a measurement disagrees, report it.

If color changes, prove why.

If geometry moves, measure the move.

If the gate fails, the process must be improved so the same failure is prevented earlier next time.
