# Twin Hammer Centered-Face Mirror-and-Weld Fresh Build A01 Approval Record

- Date: `2026-07-24`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01`
  - `SM_DRW_FoeHammer_Hammer_A01`
- Decision authority: `Flamestrike`
- Decision: `approved`
- Artifact status: `authoritative approval record`

## Approval Evidence

After the exact face misalignment and the required perimeter correction were
explained, Flamestrike stated:

`I approve the fix ... make it happen.`

This approves the correction direction that had just been stated:

- raise and correctly align both end faces;
- correct their perimeter shape;
- weld each end face into its adjoining hammer body; and
- build one correct half and mirror it instead of copying and rotating the
  faulty half.

## Locked Recovery Amendment

- Amendment:
  `../manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01.json`
- Amendment SHA-256:
  `4e960362ebcf27ffd3c6ed811584679d5f8ca75befcaad8286370224fe9eb3e4`
- Validation:
  `../manifests/TWIN_HAMMER_CENTERED_FACE_MIRROR_WELD_RECOVERY_A01_VALIDATION.json`
- Validation SHA-256:
  `8f6cfa57c8044c93e671a0d4270ef801df311f8cfa7428eaa17f19003837bb07`
- Validation result: `PASS 51/51`
- Validation artifact status: `proof only`

## Exact Approved Build Step

Create a fresh builder and an independent saved-file auditor under new
filenames. The builder must:

1. read only the hash-locked measurement, ownership, source-image, approved
   mirror-appearance, and recovery-amendment records;
2. read no geometry or coordinates from either failed Blender source;
3. construct one fresh positive-`X` half with its strike end face integrated
   into the head solid;
4. use the exact centered face-treatment translation
   `+1608625/145631 cm` on `Z`, with no local-treatment scaling;
5. let the welded shared-body perimeter control the end-face boundary;
6. reflect the sealed half across `X=0` using
   `(X,Y,Z)->(-X,Y,Z)`;
7. merge and weld the center seam;
8. use no whole-asset `Rz180`;
9. preserve the exact shared output dimensions
   `50719500/517681 × 6644212/149985 × 170/1 cm`;
10. preserve the correct double-rune-sided versus
    double-metal-center-piece-sided identity;
11. stop before saving if any pre-save topology or source-integrity gate
    fails;
12. repeat every topology and source-integrity gate independently against
    each saved file;
13. produce one corrected review board per hammer; and
14. open both boards visibly, then stop for Flamestrike's review.

## Mandatory Technical Result

Each candidate must independently prove:

- `0` open boundary edges;
- `0` edges used by more than two faces;
- `0` face-winding mismatches;
- `0` loose edges;
- `0` zero-area faces;
- `0` duplicate faces;
- `0` unwelded center-seam vertices;
- `PASS` declared contacts;
- `PASS` protected negative spaces;
- unchanged source hashes; and
- exactly matching twin XYZ bounds.

Any failed gate stops the build. A failed output remains `invalid` or
`quarantined`; it cannot be rendered or presented as a corrected candidate.

## Source Protection

The following failed sources remain immutable and quarantined as Step 13-pass
or downstream authority:

- Siege Breaker:
  `c69b415ac3429091c6aa77d24ffcd6d88bbd0f9fc711e3862c2c7e7b51034537`
- Foe Hammer:
  `67737a3c561cd6462af3657ea93488af76f32a5815ee0b4d5887182d14c761d4`

They may be hash-checked but may not be opened as geometry input, resaved,
modified, copied forward, or repaired.

## Explicit Exclusions

This approval does not authorize:

- modifying either failed source;
- repair-forward of the failed surface-patch assembly;
- whole-asset `Rz180`;
- stretching or normalizing the local C04 treatment;
- UV or texture production;
- LODs or collision;
- FBX or other export;
- Unreal work;
- Step 14 advancement;
- `DCC game-ready candidate`; or
- `Fully game-ready`.

The approved decision output is exactly two audited fresh
`DCC source candidate` files and two visible corrected review boards.
