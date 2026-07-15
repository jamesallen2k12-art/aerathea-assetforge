# SM_GIA_BloodAxeCairnstone_A005 Source Authority Lock

Status: approved Step 02 source authority lock

Artifact classification: `authoritative`

Date: 2026-07-15

## Approved Decision

The confirmed A02 source and its exact scanline record passed fresh,
non-mutating verification. Flamestrike approved the Step 02 output package on
2026-07-15. They are the sole authoritative asset-specific source evidence for
the A005 fresh-start project.

This record does not authorize panel extraction, measurement, interpretation,
geometry, texture, export, Unreal work, or Step 03.

## Authoritative Source

Source:

`docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`

- File SHA256:
  `4b953abb87f5f254a5f51c6214e76d3f72c4fc55bc2fa4e4d605b2440d6e53c2`
- Decoded RGB pixel SHA256:
  `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- Width: `1055` pixels
- Height: `1491` pixels
- Format: non-interlaced PNG
- Pixel format: 8-bit RGB

## Authoritative Scanline Evidence

Manifest:

`docs/assets/reference/bloodaxe_cairnstone_asset/ScanlineCapture/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate_ScanlineManifest.json`

- Manifest file SHA256:
  `ec544f80b969f53eb9729910d4eebc28a0fd0bfbc9c2d1be35d2aa7de0806dbc`
- Format signature: `AET_RGB_SCANLINE_V1`
- Metadata: `1055 1491 3 RGB`
- Scanlines: `1491`
- Decoded RGB bytes: `4719015`
- Scan RGB SHA256:
  `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- Target RGB pixel SHA256:
  `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- Rebuilt RGB pixel SHA256:
  `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- Fresh in-memory rebuild RGB pixel SHA256:
  `65b69c9674d6644fcae6795df01bdab55e59fc0c493a501ed7ed1baa966a3a72`
- Changed pixels: `0`
- Maximum RGB delta: `0`
- Mean grayscale delta: `0.0`
- Difference image: all RGB values are zero
- Pixel exact: `true`

## Referenced Proof File Hashes

- Target PNG:
  `64dd5c613cf294c146fa03238b1429062c2e5d7de3e472f8dd204fdd3e1576e7`
- Gzip scan record:
  `0be64c62d497f8bf062954e1c16661a954442f6eb2a540a43cdb57650e37040b`
- Rebuilt PNG:
  `64dd5c613cf294c146fa03238b1429062c2e5d7de3e472f8dd204fdd3e1576e7`
- Difference PNG:
  `7a57ebc0b89e6e1535aadd2c81793bc46baef18b30db6dd9c729bd83a231d8b5`

Every manifest-referenced proof path resolved to a regular, non-symlink file
inside the manifest's exact `ScanlineCapture` directory.

## Fresh Verification Method

The verifier read the two declared scan-record header lines, then audited all
`1491` rows. Each row contained a four-byte big-endian row index equal to its
zero-based row number followed by `1055 * 3 = 3165` RGB bytes. Concatenating
the validated row payloads produced exactly `4719015` RGB bytes.

The concatenated scan payload was rebuilt in memory as an RGB image and
compared byte-for-byte with the decoded source, target, and stored rebuilt
image. All four RGB byte streams were identical.

## Evidence Boundary

This lock proves only source identity and exact scanline reproduction. It does
not establish panel bounds, component identities, measurements, formulas,
cross-view correspondence, hidden surfaces, topology, or any production
solution.

## Access Declaration

- No A001-A004 asset-specific artifact was opened or read.
- No source or scanline proof file was modified, copied, or regenerated.
- No crop, mask, transformed image, interpretation, or production artifact was
  created.
- No A005 production root was created.

## Approval Record

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Decision: this record, the A02 source, and its exact scanline evidence are
  `authoritative` for A005
- Exclusion: panel decomposition, measurement, interpretation, production
  work, and Step 03 remain unauthorized
