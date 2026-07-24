# Twin Hammer Centered-Face Mirror-and-Weld Fresh Build A01 Output Record

- Date: `2026-07-24`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Build: `TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01`
- Artifact status: `authoritative status record backed by proof-only audits`
- Current decision: `technical PASS; Flamestrike visual decision pending`
- Step 13 complete: `false`
- Step 14 authority: `false`
- Unreal authority: `false`

## Plain-English Result

Both failed hammers were left byte-for-byte unchanged.

Two new hammers were built from the hash-locked measurements and approved
source-pixel ownership. Each new hammer uses one positive-`X` half, an exact
mirror across `X=0`, and a welded center seam. No whole-hammer 180-degree
copy was used.

The end-face treatment was raised by the exact approved amount:

`+1608625/145631 cm = +11.045896821419 cm on Z`

The treatment is contained by a continuous welded strike-face perimeter.
Siege Breaker keeps the double-rune-sided identity; Foe Hammer keeps the
double-metal-center-piece-sided identity.

## Accepted DCC Source Candidates

### Siege Breaker

- Status: `DCC source candidate; pending Flamestrike visual decision`
- Source:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A13_R1_CenteredFaceMirrorWeld_DCCSource_A01/SM_DRW_SiegeBreaker_Hammer_A01_DCCSource_CenteredFaceMirrorWeld_A01.blend`
- SHA-256:
  `9808a58a57d8c9f55e9c7083bd8596f9085d59f60cc1ae27e26dd90a43e50f31`

### Foe Hammer

- Status: `DCC source candidate; pending Flamestrike visual decision`
- Source:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_FoeHammer_Hammer_A01/A13_R1_CenteredFaceMirrorWeld_DCCSource_A01/SM_DRW_FoeHammer_Hammer_A01_DCCSource_CenteredFaceMirrorWeld_A01.blend`
- SHA-256:
  `bb5337f7a40b0e10ba1b29772c00177bc597fe70e36393ed0704b26054f4ff70`

## Mandatory Technical Result

Each source was reopened directly by the independent auditor. Both returned:

- open boundary edges: `0`
- edges used by more than two faces: `0`
- winding mismatches: `0`
- loose edges: `0`
- zero-area faces: `0`
- duplicate faces: `0`
- unwelded center-seam vertices: `0`
- missing mirrored vertices: `0`
- signed volume: `positive`
- protected source negative spaces: `PASS`
- declared contacts: `PASS`

Both saved files also have:

- identical dimensions:
  `97.97442626953125 × 44.29917526245117 × 170.0 cm`
- identical saved geometry SHA-256:
  `a7076cfb62eb229e3e996f37144517adbbdc81d594a22d1c14397828d16566ad`
- identical topology counts:
  `924152 vertices / 1637566 edges / 713042 faces`

Build manifest:

- Path:
  `../manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_MANIFEST.json`
- SHA-256:
  `2668d03fb868f989f1a4fd95c0f84cb9b772984d04a4cf72f253c636ec07192f`
- Result: `PRE_SAVE_PASS`

Independent saved-file audit:

- Path:
  `../manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_INDEPENDENT_AUDIT.json`
- SHA-256:
  `416ea044a2f28ca009423a3780302621b0e31c49cb9c9eec3dfe896e9b9da3bf`
- Result: `PASS`

## Review Boards

### Siege Breaker

- Status: `proof only; pending Flamestrike visual review`
- Path:
  `../review/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01/SM_DRW_SiegeBreaker_Hammer_A01_CENTERED_FACE_MIRROR_WELD_REVIEW_A01.png`
- SHA-256:
  `963b48ad87f4d1beb1368c1db23aa5588dc2d8c780fbbca1828aa2a47243b72a`
- Size: `3100 × 1760`

### Foe Hammer

- Status: `proof only; pending Flamestrike visual review`
- Path:
  `../review/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01/SM_DRW_FoeHammer_Hammer_A01_CENTERED_FACE_MIRROR_WELD_REVIEW_A01.png`
- SHA-256:
  `7c4a29f6ced322339354dbd36bb86e2946740e908daabbfafec0f93d72a61dc4`
- Size: `3100 × 1760`

Each board contains:

1. the full fresh DCC source candidate;
2. a direct positive-`X` strike-face view with the complete head transition;
3. the same direct camera with a temporary topology-partition palette; and
4. the independent saved-file topology results.

Render manifest:

- Path:
  `../manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_REVIEW_RENDER_A01_MANIFEST.json`
- SHA-256:
  `957cb2551c3486494b2d589be86af42709759f523f5545314ca05918e4236052`
- Result: `PASS`

Both final boards were opened in two visible desktop Image Viewer windows.

## Controlled Rejections

The mandatory gates rejected four pre-save topology attempts, one pair that
passed individually but failed the paired geometry-identity audit, and one
internal camera framing pass.

Rejected-attempt record:

- Path:
  `../manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_FRESH_BUILD_A01_REJECTED_ATTEMPTS.json`
- SHA-256:
  `a81e29458043485aaf3fa20fdc7ac7b5b34edf09ad8bc5118ef2421a9cdb3923`
- Status: `reference only`

No rejected attempt has Step 13-pass or downstream authority.

## Source Integrity

The quarantined failed sources remain unchanged:

- Siege Breaker:
  `c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537`
- Foe Hammer:
  `67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4`

The builder, auditor, and renderer invoked no save operation against either
failed source and read no geometry from them.

## Tool Records

- Builder:
  `Tools/DCC/build_twin_hammer_centered_face_mirror_weld_a01.py`
  - SHA-256:
    `e58e9084b6b6cd55ccb4716a670e1733173d6b5c72c8606982fff35aab064081`
- Independent auditor:
  `Tools/DCC/audit_twin_hammer_centered_face_mirror_weld_a01.py`
  - SHA-256:
    `075e33edf41699934943e24df721c2b0a070dc0c6a8df5283ef2d24a5f2f9f2e`
- Review renderer:
  `Tools/DCC/render_twin_hammer_centered_face_mirror_weld_review_a01.py`
  - SHA-256:
    `2f921ed99157a7c9463a9715ca4b23b2c924c7628f8f66bada7adad195266059`

## Stop Gate

Stop here for Flamestrike's visual decision.

No UV, texture, LOD, collision, export, Unreal, Step 14, DCC game-ready, or
Fully game-ready authority is granted by this record.
