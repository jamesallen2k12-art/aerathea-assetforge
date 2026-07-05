# SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21 3D Game Asset Blueprint

Status: DCC game-ready candidate  
Blueprint standard: `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`  
Last updated: 2026-07-04

## Asset Summary

- Asset name: `SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21`
- Asset type: Static Mesh prop
- World role: Blood Axe Giant cairnstone / ritual standing-stone cluster
- Culture/faction: Blood Axe Tribe Giant visual language
- Engine target: Unreal Engine
- Current status: DCC game-ready candidate, pending Flamestrike visual approval and Unreal import validation

## Source Hierarchy

1. Approved original source template: `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`
2. Fresh scanline-verified view crops from A21 evidence
3. Top view owns XY footprint, orientation, and component registration
4. Front/back/left/right views own primary-object width/depth profiles by height
5. Tagged inferred fill is allowed only for occluded or hidden surfaces
6. Prior generated outputs are review history only and were not used as source data

## Source Evidence

- Build manifest: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_3DBuildManifest.json`
- Evidence manifest: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/FreshEvidence/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_FreshCalibrationManifest.json`
- Geometry/color audit: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_GeometryColorAccuracyAudit.json`
- Strict gate report: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_StrictPixelGate.json`
- Review board: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_3DReviewBoard.png`
- Beauty review: `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_BeautyReview.png`

## DCC Outputs

- Blender source: `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21.blend`
- FBX: `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21.fbx`
- LOD exports:
  - `SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_LOD0.fbx`
  - `SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_LOD1.fbx`
  - `SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_LOD2.fbx`
  - `SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_LOD3.fbx`
- Collision export: `SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_UCX.fbx`

## Coordinate Frame

- Up axis: `Z`
- Forward/front direction: `-Y`
- Right direction: `+X`
- Pivot: bottom center of support object at world origin
- Primary/support alignment: all visible contact centers validated at `[0.0, 0.0]`
- Base/support yaw: `0.0 deg`
- Primary object relative yaw: `0.0 deg`

## Pixel Convention

- Calibration span: inclusive object crop pixel span
- Mesh contours: source mask boundary points recentered to declared component origin
- Visible texture color: exact RGB copy from source crop into per-view texture and atlas source region
- Prior outputs used as source data: `false`

## Component List

- Lower support object: source-derived top footprint contour, closed mesh
- Upper support object: source-priority scaled support contour, closed mesh
- Primary object: top-contour shape fitted to front/back/left/right outer-envelope width/depth profiles by height
- Hidden orientation markers: non-shipping geometry stored in Blender source and excluded from render/export
- Collision proxies: two simple UCX boxes

## Registration Marks

Hidden non-shipping registration markers are stored in the Blender source:

- `AET_ORIENT_SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_BaseFro`
- `AET_ORIENT_SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_StoneFr`

These identify front-facing assembly orientation. They are hidden and not exported as shipping render geometry.

## Contact And Attachment Interfaces

Validated contact results:

- Lower support to upper support Z gap: `0.0 cm`
- Upper support to primary object Z gap: `0.0 cm`
- Lower/upper center delta: `[0.0, 0.0] cm`
- Upper/primary center delta: `[0.0, 0.0] cm`
- Primary bottom Z: `35.0 cm`

No artificial lift, hidden gap, stretch strip, or unapproved offset is present in A21.

## Measurement Contracts

Selection methods:

- Support XY contour: `exact`
- Upper support XY contour: `source_priority`
- Primary object XY contour: `source_priority`
- Primary object width/depth by height: `outer_envelope`
- Visible texture color: `exact`
- Occluded surface fill: `inferred_surface_fill`

Strict audit measurements passed:

- Support declared width: expected `140.0 cm`, observed `139.388641 cm`, tolerance `1.0 cm`
- Support declared depth: expected `110.0 cm`, observed `109.535866 cm`, tolerance `1.0 cm`
- Primary width/depth at sampled heights: all errors `<= 0.01 cm`
- Contact and center alignment: all errors `<= 0.001 cm`

The support width/depth difference is the declared pixel-boundary convention result from source-contour construction, not a post-build scale drift.

## Texture And Material Rules

Visible texture rule: exact RGB copy only.

Textures:

- Front: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_Front_BC.png`
- Back: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_Back_BC.png`
- Left: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_Left_BC.png`
- Right: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_Right_BC.png`
- Top: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_Top_BC.png`
- Hidden fill: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_HiddenSampleFill_BC.png`
- Atlas: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_Atlas_BC.png`
- Normal: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_N.png`
- ORM: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_ORM.png`
- Emissive: `T_GIA_BloodAxeCairnstone_A02_StrictPixelA21_E.png`

Atlas source regions are exact source-size copies. The strict audit reported zero changed pixels for all visible atlas regions.

## Inferred Surface Areas

Allowed inferred areas:

- occluded/hidden support contact texture fill
- simple collision proxy approximation

Inference rules:

- inferred fill is tagged
- inferred fill uses same-source visible pixel sampling
- inferred fill does not override visible source geometry
- inferred fill is not treated as visual canon source data

## LOD Plan

Generated LOD triangle counts:

- LOD0: `13300`
- LOD1: `4628`
- LOD2: `1812`
- LOD3: `716`

LOD reduction keeps the primary silhouette before reducing smaller contour/detail density.

## Collision Plan

Collision type: simple UCX proxy boxes.

Collision proxies:

- `UCX_SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_00`
- `UCX_SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_01`

Unreal validation still required.

## Unreal Import Notes

- Target path: `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21`
- Asset type: Static Mesh
- Unit scale: centimeters
- Import LOD0-LOD3
- Import/assign UCX collision
- Material slot target: one primary material
- Use base color, normal, ORM, and emissive maps
- Validate scale, collision, LOD switching, material assignment, and review-map placement

## Validation Results

Strict gate: `PASS`

Passed checks include:

- source scanline exact
- visible per-view pixels exact
- visible atlas source regions exact
- no visible atlas filtered resize
- no explicit primary/support Z gap
- no measured visible geometry replaced by superellipse
- no nearby-row search tolerance for visible measurements
- contact gaps zero
- center offsets zero
- rotations zeroed
- meshes closed with no boundary/non-manifold edges
- generic accuracy measurements present
- no visible averaged measurements

## Known Issues Encountered

Issues from earlier passes:

- visible color drift from filtered atlas resizing
- contact line from artificial primary/support lift
- support object orientation/registration uncertainty
- seam mismatch from trying to visually patch or stretch
- analytic shape replacement causing plausible but non-source geometry
- missing explicit measurement contracts

## Solutions That Worked

- Fresh source-only rebuild from the approved A02 template
- Exact scanline capture and verification
- Hidden non-shipping orientation markers
- Source hierarchy and coordinate frame declared before build
- Zero-gap contact interface
- Exact RGB per-view texture copies
- Exact-copy atlas source regions
- Outer-envelope selection for conflicting front/back and left/right profile measurements
- Generic accuracy measurements written into the audit
- Strict validation gate before visual review

## Solutions Rejected

- Averaging front/back or left/right measurements
- Stretch strips as final seam fixes
- Detached shell patches as final fixes
- Filtered atlas resizing for visible source pixels
- Superellipse replacement for visible primary geometry
- Artificial primary/support lift
- Unreported contact or center offsets
- Using prior generated candidates as source data

## Remake Instructions

1. Read `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`.
2. Use only `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png` as source input.
3. Run:

```bash
blender --background --python Tools/DCC/build_bloodaxe_cairnstone_a02_strict_pixel_a21_3d.py
```

4. Audit:

```bash
blender --background SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21.blend --python Tools/DCC/audit_bloodaxe_cairnstone_a02_strict_pixel_a21.py
```

5. Validate:

```bash
python3 Tools/DCC/strict_pixel_asset_gate.py \
  --audit Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_GeometryColorAccuracyAudit.json \
  --generator Tools/DCC/build_bloodaxe_cairnstone_a02_strict_pixel_a21_3d.py \
  --out Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_StrictPixelGate.json
```

6. Present review images only if the strict gate passes.

## Asset-Type Lessons

For future multi-view static prop reconstruction:

- define source hierarchy before geometry
- never use prior failed assets as source data
- make the coordinate frame explicit
- validate contact interfaces before rendering
- solve seams by measurement, not visual stretching
- use exact-copy visible texture paths
- use inferred fill only for hidden/missing surfaces
- report accuracy as expected/observed/error/tolerance
- make the gate a confirmation step, not the first place errors are discovered

## Approval Status

- Technical strict gate: passed
- DCC candidate generated: yes
- Review images opened for Flamestrike: yes
- Flamestrike final visual approval: pending
- Unreal import validation: pending
- Approved library asset: no
