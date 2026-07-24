# Twin Hammer Center-Post And Handle-Shape Drift Recovery A01

- Date: `2026-07-24`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01`
  - `SM_DRW_FoeHammer_Hammer_A01`
- Artifact status: `authoritative recovery record`
- Production state: `Core Recovery; stopped`
- Valid DCC source candidates: `0`
- Step 13 / Step 14 / Unreal authority: `false / false / false`

## Flamestrike Findings

Flamestrike found two visible shape errors in both centered-face
mirror-and-weld review candidates:

1. The head reads as a full extrusion. The source-owned separation around the
   center post at the top of the head is filled.
2. The handle has become square instead of retaining its source-driven
   rotational cross-section.

These are geometry errors, not camera or shading errors.

## Proven Cause

The fresh builder substituted one front-silhouette depth construction for
the approved component-specific surface rules.

In
`Tools/DCC/build_twin_hammer_centered_face_mirror_weld_a01.py`:

- lines `360-361` force every head row to the same
  `COMMON_HALF_DEPTH`;
- lines `636-644` make the Step 06 front mask the construction domain and
  count only front-mask enclosed holes;
- lines `671-717` copy every retained front cell to one front plane and one
  back plane;
- lines `719-747` close exposed mask edges with side walls; and
- line `888` declares protected negative spaces preserved when the count of
  front-mask holes is merely greater than zero.

Consequences:

- The head becomes a closed front-mask slab. Top/bottom C01/C02/C03 ownership
  and their protected center-post gaps do not control its volume.
- For the haft, grip, collars, and pommel, a row radius is used as the
  positive and negative `Y` plane while the same radius controls the `X`
  extent. That creates box-like row sections instead of the approved
  rotational surface.
- The audit can pass manifold, seam, bounds, and identical-geometry checks
  while testing the wrong shape. Its negative-space result does not prove the
  top/bottom separation visible in the source.

## Governing Evidence

- Approved top source:
  `SourceAssets/Concepts/SiegeBreaker/siege_breaker_top_view.png`
  - SHA-256:
    `06d9cc7f78a4fe459a1f620e4787b53bf63399f7215bb9106a4e264749147d1c`
  - It visibly preserves separation around the central head structure and
    labels the handle as a diameter, not a square width.
- Approved front source:
  `SourceAssets/Concepts/SiegeBreaker/siege_breaker_front_view.png`
  - SHA-256:
    `d00bf9ffcfd4862884626fa961c5f6b4fd6cedfdff7936b2210ca2a905e57e95`
- Locked zero-extrusion execution contract:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/A12_R10_R8_PIXEL_EXACT_STEPS01_16_A01_CONTRACT.md`
  - SHA-256:
    `77b0339126388be01f59532cd6b79228450b61e739ebc10c2f849833fd337bd4`
  - Its cylinder rule requires
    `theta(U)=-pi/2+pi*U`,
    `X=r(z)cos(theta)`, and `Y=r(z)sin(theta)`.
- Authoritative zero-extrusion recovery approval:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/steps/A12_R10_R8_ZERO_EXTRUSION_AUTHORITY_RECOVERY_A01_APPROVAL_RECORD.md`
  - SHA-256:
    `76c9b6a1d798780def0662c3a072f76144531f82b3228d7e2ce4adb4ee0d5ee0`
  - It preserves every approved component equation, source owner,
    combined-boundary rule, hidden-closure rule, cylinder-wrap rule, and
    fail-closed gate.
- Zero-extrusion restart instructions:
  `docs/assets/blueprints/SM_DRW_SiegeBreaker_Hammer_A01/handoffs/A12_R10_R8_ZERO_EXTRUSION_RESET_HANDOFF.md`
  - They explicitly forbid copying a 2D face to a second depth and joining it
    as a prism, rectangular cross-sections, slabs, and filled
    source-connected negative spaces.
- Historical Step 11 blueprint:
  `STEP_11_PRODUCTION_GEOMETRY_BLUEPRINT.json`
  - SHA-256:
    `2b598497ba5e61a4352c217f3fb20b3545189c710934f3a21d9b7398ddb472c7`
  - Status: `invalid / quarantined as construction authority`; it is
    `reference only` for showing the component-method clauses that the current
    builder failed to execute.
- Approved shared-depth recovery blueprint:
  `SHARED_DEPTH_RECOVERY_BLUEPRINT_A01.json`
  - SHA-256:
    `efdbd8795dff2031fcde9e734868ff4c617dc37ad1e7b3743c3727daea981d58`
  - Its common depth is an outer bound, not permission to create fill
    geometry.
- Approved face correction record:
  `TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01.json`
  - SHA-256:
    `4e960362ebcf27ffd3c6ed811584679d5f8ca75befcaad8286370224fe9eb3e4`
  - Its face alignment, positive-`X` half, `X=0` mirror, and welded-seam
    requirements remain approved constraints. It did not authorize replacing
    component-specific construction.

## Last Known Core-Valid State

The last valid production authority is the combined pre-geometry evidence and
rules:

- hash-locked source images;
- exact measurements and component ownership through Step `09A`;
- the locked A12 R10 zero-extrusion component, boundary, closure, and
  cylinder-wrap rules;
- the shared twin bounds and identity rules; and
- the approved end-face elevation, positive-`X` half, `X=0` mirror, and
  welded-seam constraints.

No current Blender geometry is a valid DCC source candidate.

## First Drift Action

The first drift action is the construction method in
`build_asset_mesh()` beginning from the front-mask domain at line `636`, then
creating paired front/back cells and closing their perimeter. This replaced
the approved top/bottom owner surfaces, protected gaps, and rotational
component equations.

## Assumption That Caused Drift

The build treated:

- a correct front projection,
- a common outer depth,
- a closed manifold,
- exact twin dimensions, and
- a welded mirror seam

as sufficient proof of the intended three-dimensional shape. Those facts do
not prove component separation or radial cross-sections.

## Affected Outputs And Status

- Both A13 R1 centered-face Blender files: `invalid / quarantined in place`.
- Both A13 R1 review boards and their raw renders:
  `invalid as corrected-candidate review; proof only for showing the defects`.
- `TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_MANIFEST.json`:
  `proof only for what the builder produced`.
- `TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_INDEPENDENT_AUDIT.json`:
  `proof only for manifold, seam, bounds, and twin equality; invalid as
  component-shape or protected-space proof`.
- `Tools/DCC/build_twin_hammer_centered_face_mirror_weld_a01.py`:
  `quarantined; forbidden as future construction input`.
- `Tools/DCC/audit_twin_hammer_centered_face_mirror_weld_a01.py`:
  `reference only; insufficient for the missing shape gates`.
- `Tools/DCC/render_twin_hammer_centered_face_mirror_weld_review_a01.py`:
  `reference only`.
- Earlier failed/quarantined hammer sources remain unchanged and retain their
  existing classifications.

The files remain preserved in place for defect evidence. They may not be
copied forward, repaired, beveled into compliance, or used as coordinate
authority.

## Smallest Sufficient Recovery

Do not repair either current mesh.

Start from the last Core-valid evidence and write a new, narrow correction
contract that:

1. reconstructs C01/C02/C03 from their approved front, top, and bottom
   ownership and boundary rules;
2. proves the center-post separation remains unoccupied in top and bottom
   projection;
3. reconstructs C06-C11 from exact row-radius evidence with
   `P(z,theta)=(r(z)cos(theta),r(z)sin(theta),z)` and the approved exact
   per-source-column cylinder mapping;
4. proves representative handle, grip, collar, and pommel sections are
   radial rather than rectangular;
5. retains the exact approved face elevation
   `+1608625/145631 cm` on `Z`;
6. builds one correct positive-`X` half, mirrors it across `X=0`, and welds
   only coordinate-equal seam vertices;
7. preserves identical twin bounds and shared geometry, with only the
   approved local C04 treatment difference;
8. independently audits source ownership, protected spaces, rotational
   cross-sections, topology, and saved-file equality; and
9. produces one clear top/three-quarter/handle-section review board per
   hammer and opens both visibly.

The new contract requires a separate explicit Flamestrike approval before
code, Blender, geometry, or rendering.

## Save Point

- Pre-record checkpoint:
  `Saved/ProjectRecovery/20260724-151433`
- Governing restart handoff:
  `../handoffs/TWIN_HAMMER_CENTER_POST_AND_HANDLE_RESET_HANDOFF_A01.md`
