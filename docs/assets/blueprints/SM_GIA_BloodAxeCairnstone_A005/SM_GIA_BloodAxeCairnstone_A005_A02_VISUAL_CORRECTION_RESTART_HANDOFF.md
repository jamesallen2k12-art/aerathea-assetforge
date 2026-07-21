# SM_GIA_BloodAxeCairnstone_A005 A02 Visual-Correction Restart Handoff

Status: authorized restart boundary; no A02 production action performed

Artifact classification: `authoritative restart handoff`

Date: 2026-07-20

## Flamestrike Decision

Flamestrike rejected the A01 final review image and requested a recovery point
followed by a fresh-context pass.

Authoritative visual findings:

- The bottom base layer appears cut off.
- The base must read distinctly as the plinth, the ring it sits on, and the
  lower ring surrounded by debris.
- The rendered pixel color is off relative to the approved source.
- Only the next final corrected 3D image should be opened for review; do not
  open intermediate images.

## Source And Blueprint Authority

- Visual source:
  `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`
- Source SHA-256:
  `4b953abb87f5f254a5f51c6214e76d3f72c4fc55bc2fa4e4d605b2440d6e53c2`
- Authoritative geometry plan:
  `manifests/STEP_11_CONSTRUCTION_BLUEPRINT.json`
- Authoritative UV/material ownership plan:
  `manifests/STEP_14_UV_OWNERSHIP_PLAN.json`
- Required bounds: `140 x 110 x 220 cm`; base height `35 cm`; pivot bottom
  center at `[0,0,0]`.
- Step 11 visible base spans: C002 upper tier `23-35 cm`; C003 lower tier
  `10-23 cm`; C004 rubble apron `0-10 cm`.
- Steps 01-11 remain authoritative. Unreal/Step 17 remains unauthorized.

## A01 State And Classification

- A01 source commit: `1768a43f58d604d556a57e32c41f7b2dbee46a0e`.
- A01 Blender, FBX, textures, and final review image: `quarantined` as visual
  candidates.
- A01 independent audit `20/20` and clean FBX imports `4/4`: `proof only`;
  they prove technical packaging, not source equivalence.
- A01 final image:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/Production/VisualFidelityRecovery_A01/SM_GIA_BloodAxeCairnstone_A005_FINAL_GAME_READY_ASSET.png`
- A01 final-image SHA-256:
  `56666489f3b5420ad7a4d5206f96e0631147df936eece147780a2263d4d3c05b`.
- A01 builder:
  `Tools/DCC/build_bloodaxe_cairnstone_a005_visual_fidelity_recovery.py`.
- A01 renderer:
  `Tools/DCC/render_bloodaxe_cairnstone_a005_visual_fidelity_final.py`.
- A01 auditor:
  `Tools/DCC/audit_bloodaxe_cairnstone_a005_visual_fidelity_recovery.py`.

## Proven Evidence Versus Open Diagnosis

Proven:

- Flamestrike's three visual findings above.
- The source and Step 11 require three separately readable base bands over
  `0-35 cm`.
- A01 construction contains four technical shells and passes its numeric
  audit, but the final rendered read does not satisfy the source.
- A01's source-owned Base Color audit proves atlas texel preservation only; it
  does not prove final rendered-color equivalence.

Open diagnosis; do not treat as fact until audited:

- The A01 apron may read cut off because its `0-10.5 cm` shell collapses into
  a thin reflective rim in the final presentation even though it exists
  numerically.
- Base-tier UV routing may sample or stretch the wrong source band.
- The material node's Base Color gamma transform (`0.58`), ORM response, and
  the renderer's `Standard` transform at exposure `1.80` with mixed warm/cool
  lights may be shifting the displayed color.
- Camera pitch/target and ground intersection may be weakening the bottom
  silhouette.

## Authorized A02 Scope

1. Re-run the resume handshake and read this handoff, the latest checkpoint,
   git status, Step 11, Step 14, A01 builder/renderer/auditor, and the two
   images named above.
2. Audit the three base spans in geometry and in the final camera projection.
3. Audit Base Color sampling and rendered output through the full shader,
   lighting, color-management, and camera chain.
4. Make the smallest A005-only change that produces a distinct plinth,
   seated ring, and lower debris-surrounded ring while preserving the locked
   dimensions, four primary shells, one material, LODs, collision, and source
   authority.
5. Match source color in the final displayed pixels; do not substitute a
   subjective recolor for measured source comparison.
6. Create A02-suffixed Blender, FBX, texture/manifest, audit, and final-image
   outputs. Preserve A01 without overwrite.
7. Rerun all dependent technical gates plus explicit base-band visibility and
   final rendered-color gates.
8. Open only the final accepted A02 3D image for Flamestrike.

Forbidden: deleting A01, changing the source, using A001-A004 production
geometry as authority, opening intermediate renders, Unreal work, or claiming
`Fully game-ready`.

## Restart Recovery Point

- Manual checkpoint: `Saved/ProjectRecovery/20260720-202843/`
- Checkpoint note: `A005 A01 visual rejection recorded; A02 base-stack and
  source-color restart handoff ready`.
- The checkpoint was created after this handoff and the linked status records
  were written, so it contains the exact state required by the next agent.
