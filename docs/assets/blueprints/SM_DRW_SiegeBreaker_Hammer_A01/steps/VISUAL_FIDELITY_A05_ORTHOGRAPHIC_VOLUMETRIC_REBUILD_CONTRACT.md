# Siege Breaker A05 Orthographic Volumetric Rebuild Contract

- Contract ID: `SB-VF-A05-ORTHOGRAPHIC-VOLUMETRIC`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-21
- Approver: Flamestrike
- Approval: full authority to reset, rebuild the 3D asset from the supplied
  orthographic data under Core, complete the DCC package, and present only the
  final completed image.
- Artifact status: `authoritative`
- Execution state: `approved for the first post-reset agent`

## One Decision

Can the supplied detailed orthographic views, exact numeric anchors, and
corrected canonical blockout produce one genuinely volumetric, aligned,
source-faithful `DCC game-ready candidate` without any A03/A04 geometry,
facade/card construction, nonuniform component scaling, background
contamination, or asserted validation?

## Core Truths

1. The project goal is a true 2D-orthographic-to-3D production asset, not a
   camera-specific illusion.
2. Flamestrike has explicitly stated that the supplied orthographic dataset is
   the intended construction data.
3. `asset_spec.json`, `dimensions_cm.csv`, and the corrected canonical blockout
   own the world frame, bounds, pivot, centerline, and anchor intervals.
4. The detailed front/back/left/right/top/bottom views own visible shape and
   surface evidence after complete-view registration to the numeric frame.
5. The three-quarter render owns style, material character, and final beauty
   comparison only. It is not a geometry coordinate system.
6. A03/A04 production outputs are quarantined and may not be read as A05
   construction inputs.
7. Intermediate images remain internal. Flamestrike sees only the final
   completed A05 image unless a genuine evidence block prevents completion.

## Exact Authority Inputs

- `AGENTS.md` Core Principles.
- `manifests/VISUAL_FIDELITY_A04_DRIFT_RECOVERY_A05_RESTART.json`.
- `manifests/SOURCE_AUTHORITY_A05_ORTHOGRAPHIC.json`.
- Final-package `asset_spec.json`, `dimensions_cm.csv`,
  `component_breakdown.json`, `modeling_notes.md`, and `material_spec.json`.
- Corrected `SiegeBreaker_Blockout.blend` and its numeric manifest.
- Unchanged detailed orthographic source sheet.
- Final-package deterministic camera/render rules.

## Forbidden Inputs And Methods

- Any A03/A04 Hammer mesh, curve, contour, mask, texture, UV, component center,
  source-to-world scale, camera, backing block, export, or derived geometry.
- The A03 perspective-primary authority rule and cross-view conflict decision.
- Independent component scaling or recentering.
- Perspective-render tracing as the construction frame.
- Image planes, billboards, facade slabs, detached projection shells, or
  view-dependent cards used to create apparent geometry.
- Raw concept-sheet background, labels, arrows, paper, or shadows in shipping
  textures.
- Hard-coded gate results or validation values copied from design targets.
- Repairing forward after a failed method gate.

## Required Sequence

### Step 0 — Resume And Recovery Lock

1. Read `AGENTS.md`, the latest recovery journal entry, reset state, A04 drift
   recovery manifest, A05 source authority, this contract, approval log, and
   artifact index.
2. Report the resume summary required by Core.
3. Confirm A03/A04 construction input count is zero.
4. Run a manual checkpoint before the first long DCC operation.

Pass decision: the next agent can state the exact authority, quarantine
boundary, final review behavior, and prohibited methods without ambiguity.

### Step 1 — Fresh Orthographic Intake

1. Hash the unchanged source sheet and every authoritative numeric file.
2. Extract fresh front, back, left, right, top, and bottom panels directly from
   the source. Do not reuse A03/A04 crops or masks.
3. Build clean semantic masks that contain only weapon pixels. Explicitly
   exclude paper, border, labels, dimension text, arrows, extension lines,
   shadows, and background.
4. Record uncertain or occluded pixels as unknown rather than filling them.
5. Internally inspect the masks before any geometry.

Fail closed if any component silhouette cannot be separated from annotation or
background with defensible evidence.

### Step 2 — One Registered World Frame

1. Register each complete orthographic view to its printed dimension endpoints
   and declared axes with one uniform transform for that complete view.
2. Lock world origin at bottom-center of the pommel and the shared assembly axis
   at `X=0,Y=0`.
3. Lock stations `Z=0,14,18,60,132,170 cm`.
4. Lock overall bounds `52 x 32 x 170 cm`, head envelope `52 x 32 x 38 cm`,
   structural shaft `Z=14..132 cm`, grip `Z=18..60 cm`, pommel `Z=0..18 cm`,
   handle diameter `5 cm`, and shaft/pommel overlap `4 cm`.
5. Identify the head socket, shaft center, grip center, and pommel socket in every
   view. All attachment landmarks must resolve to the same world axis.
6. Produce an internal pregeometry registration report with formulas, observed
   values, and residual errors computed from the source—not design values copied
   into observed fields.

Blocked interpretation: different panel crop/zoom is a camera-registration
problem, not permission to scale individual components. A raw bounding-box
ratio alone cannot invalidate an annotated orthographic view.

### Step 3 — Pregeometry Gate

Before mesh creation, independently verify:

- six clean object-only masks;
- complete-view registration and camera transforms;
- one shared centerline and attachment axis;
- all required dimension anchors and intervals;
- front/back, left/right, and top/bottom paired landmark correspondence;
- zero per-component scale transforms;
- zero A03/A04 construction inputs.

If this gate fails, stop with `Blueprint block: source authority missing` or
`Blueprint block: rule missing`. Do not begin geometry.

### Step 4 — Genuine Volumetric Blockout

1. Duplicate the corrected canonical blockout into a fresh A05 path; do not
   modify or overwrite the authoritative blockout.
2. Construct the pommel, shaft, grip, head core, left stone mass, and right
   stone mass in the approved construction order.
3. Use intersecting orthographic silhouettes and cross-sections to form actual
   three-dimensional volumes. Every visible surface must remain valid between
   the source cameras.
4. Build explicit shaft-to-head and shaft-to-pommel sockets on the shared axis.
5. Preserve component separation while ensuring declared physical contact.
6. Render internal six-view blockout overlays plus a rotating parallax check.

Mandatory method gate: no production object may be a camera-facing card,
facade slab, detached projection shell, or texture-only substitute for the
primary silhouette.

### Step 5 — Alignment And Proportion Gate

Measure the evaluated mesh, not metadata:

- head socket center versus shaft center in X/Y;
- shaft center versus grip center in X/Y;
- grip center versus pommel socket center in X/Y;
- visible and structural Z contacts;
- handle diameter at multiple clear stations;
- head width/depth/height and overall length;
- component proportions against every registered orthographic view.

Required interface center delta: `<=0.05 cm` in X and Y. Required dimensional
tolerance: `<=0.02 cm` unless a stricter source record applies. Any failure
returns to Step 4; do not add detail to a misaligned blockout.

### Step 6 — Source-Faithful Detailed Modeling

1. Model craggy stone silhouette changes, layered core plates, major braces,
   collars, shaft profile, grip wrap, pommel facets, and major rune insets.
2. Keep large shape changes as geometry; reserve micro-cracks, fine engraving,
   leather grain, and scratches for bake/texture detail.
3. Recheck the six orthographic silhouettes after every major component family.
4. Use the three-quarter render only to judge shape character, material
   hierarchy, and depth—not to move the assembly axis or rescale components.

### Step 7 — UV And PBR Construction

1. Create genuine UV unwraps for the volumetric mesh with declared texel density
   and seam placement.
2. Project or transfer only clean, semantically owned source detail onto the
   corresponding real surface, then resolve occlusion, seam, and lighting
   contamination deliberately.
3. Create five production material families: stone, bronze, steel, leather, and
   restrained rune emissive.
4. Produce Base Color, Normal, ORM, and Emissive maps as applicable.
5. Reject any texture containing source paper, gray shadow halos, labels,
   dimension marks, borders, or camera-card padding.

The source render is appearance evidence, not permission to bake its background
or directional lighting into a camera-facing shipping surface.

### Step 8 — Production Package

1. Create LOD0-LOD3 while preserving the primary silhouette first.
2. Create three custom collision proxies for head, shaft, and pommel.
3. Apply transforms; keep pivot at `Z=0`; validate normals, manifold closure,
   material slots, and UVs.
4. Export four FBXs and one GLB into a fresh A05 directory.
5. Clean-reimport every export and recompute dimensions, triangle counts,
   material slots, UV presence, and collision scope.

### Step 9 — Independent Fail-Closed Validation

The validator must independently compute:

- actual bounds and anchor intervals;
- actual interface-center deltas from evaluated vertices/sockets;
- actual handle diameters and component extents;
- source-versus-render silhouettes for all six registered views;
- landmark positions and component ordering;
- clean texture ownership and absence of background contamination;
- topology, UVs, materials, LODs, collision, and clean imports;
- absence of forbidden facade/card/billboard construction;
- multi-angle parallax proving real volume.

No gate may pass from a literal `true`, expected value, custom property, or
generator declaration without independently observing the finished artifact.

### Step 10 — Internal Final Rejection Gate

Before presentation, reject the package internally if any of the following is
visible:

- head, shaft, grip, or pommel are not on one axis;
- handle reads too long or too thin against the registered orthographic set;
- any head surface reads as a pasted image;
- gray/white source-background pixels remain;
- backing blocks, facade edges, view cards, or projection seams are visible;
- the object loses coherent form between orthographic cameras;
- the beauty render hides a defect exposed by an orthographic or turntable view.

An internal rejection returns to the last passing step and is recorded. It is
not presented to Flamestrike.

### Step 11 — Final Review Image Only

After all gates pass, create one final completed review board containing:

- authoritative detailed orthographic references;
- final front, back, left, right, top, and bottom fixed-object renders;
- one final three-quarter beauty render;
- one concise parallax/turntable proof strip;
- exact bounds, alignment deltas, handle diameter, LOD counts, materials,
  textures, collision, exports, and audit result;
- explicit status `DCC game-ready candidate pending Flamestrike visual approval`.

Open that final image automatically in a visible desktop window. Do not present
intermediate images. Flamestrike's valid decisions are `approved`, `rejected`,
or `blocked`.

## Completion Boundary

A05 ends with a technically validated, genuinely volumetric `DCC game-ready
candidate` and one visible final review image. Unreal import and `Fully
game-ready` status remain unauthorized and false.
