# A12 R6 A04 Front-Half Depth-Mirror A01 Output Record

- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Contract: `SB-AXIAL-A12-R6-A04-FRONT-HALF-DEPTH-MIRROR`
- Attempt: `A12_R6_A04_FrontHalfDepthMirror_A01`
- Date: `2026-07-22`
- Artifact status: `invalid / quarantined after Flamestrike visual revision`
- Independent audit: `not run; visual gate failed first`
- Unreal authority: `false`
- Fully game-ready: `false`

## Outcome

The proper-axis construction passed its narrow mechanical gates but failed the
visible haft/collar ownership gate. Flamestrike identified disconnected-looking
haft cylinders, vertical misregistration, and missing/incorrect pixel ownership
on the collar below the head.

The saved mesh is one closed connected component: all `1,210,410` vertices are
linked, all `2,420,816` edges have two incident faces, internal `Y=0` faces are
zero, duplicate faces are zero, missing depth-mirrored vertices are zero, and
signed volume is positive. These checks are `proof only`; they do not validate
the colored result.

## Root Cause

`assign_static_uvs` routed every +X face to the right source and every -X face
to the left source, including the haft and upper collar. The haft therefore
mixed `95,664` front-, `36,766` left-, and `36,766` right-owned faces. The upper
collar mixed `6,592` front with `2,176` left and `2,176` right. Their vertical
features do not form one cylindrical registration.

This violated the component-specific cylindrical-UV requirement. The complete
colored candidate and validation implication are invalid. Connectivity,
depth-mirror, closed-topology, and normal results remain proof only.

## Preserved Evidence

- Local blend SHA:
  `386a532b3fd400ea22b793f6b61ae6133ce7742667e09c2b7da3ac913c68bff3`.
- Validation SHA:
  `d09f202c9880a44f99454bc426c562543edb7907b8a79cf16212e574bad3bf63`.
- Review-board SHA:
  `f173c834e51d47728494fa25ffbd3f933070dea2f57cbf60576e51dd82dab6fa`.
- Colored three-quarter SHA:
  `3c10027e66aa29e5c3043ca9bbab6d403f721b2270ac6a270992f9d3b8aa918a`.

## Recovery Gate

Do not repair the saved blend or run the independent candidate audit. A fresh
source rebuild requires approval of the draft A05 haft/collar cylindrical-UV
recovery contract. No export or Unreal work is authorized.
