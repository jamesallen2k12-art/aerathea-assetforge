# KIT_GIA_BloodAxeCairnVariantBatch_A01 Concept Geometry Audit

## Scope

- Audit date: 2026-07-03
- Audit trigger: Flamestrike visual review feedback
- Current asset status: `Unreal import candidate`
- Audit result: requested changes before any final visual, texture/material, library, or gameplay approval
- Approved concept source: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_CandidateBoard.png`
- Approved A1 crop: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- Approved A1 turnaround guide: `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_TurnaroundDraft_A01.png`
- Current Unreal review: `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/BloodAxeCairnVariants_A01_TextureReview_Close_Lit.png`
- Current DCC contact sheet: `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/BloodAxeCairnVariants_A01_DCCReviewContactSheet.png`

## Decision

The current twelve-cairn batch should not proceed as final visual work. It is valid as a technical Unreal import candidate and automation proof, but it has not passed a proper concept-to-geometry match. The batch was generalized from the A1 Blood Axe cairn language and was not individually matched against A2, A3, A4, A5, B1, B2, B3, B4, or B5.

The earlier statement in `UNREAL_VISUAL_REVIEW_STATUS.md` that no geometry rebuild was required is superseded by this audit.

## Main Geometry Mismatches

- The current batch reads as small piles of separated stones on round soil disks. The concept read is stronger cairn objects with authored silhouette, stacked stone intent, and integrated ground.
- The current stones are too simple and too evenly chunked. The concept uses more deliberate slab planes, broken angular faces, leaning forms, and asymmetrical weight.
- The current circular bases make the assets feel like pedestal markers or board-game tokens. The concept grounding reads like ash, mud, debris, and terrain contact, not clean round platforms.
- A1-specific features are underrepresented: dominant broken slab language, rear/side counterweight stones, rawhide/lashing treatment, restrained oxide-red paint placement, and rough Blood Axe hostility.
- The batch does not yet prove 360-degree concept fidelity. It proves import, LOD, material assignment, and rough family style only.
- The batch is not a substitute for the missing concept-specific variants A2-A5 and B1-B5.

## What Worked

- The assets imported to Unreal with one shared material slot, LODs, collision, and batch review placement.
- The broad dark-stone, mud/ash, and restrained oxide-red palette direction is useful.
- The batch has a reusable automation path for Blender source, FBX export, Unreal import, validation, review capture, and status tracking.

## Required Gate Change

Every cairn variant must have a concept target before DCC rebuild or final approval:

| Required Concept Target | Required Action |
| --- | --- |
| `A1` | Rebuild or repair as the primary approved slab-cluster target using the A1 crop and turnaround guide. |
| `A2` | Create a distinct asset only after isolating the A2 concept crop and writing its geometry notes. |
| `A3` | Create a distinct asset only after isolating the A3 concept crop and writing its geometry notes. |
| `A4` | Create a distinct asset only after isolating the A4 concept crop and writing its geometry notes. |
| `A5` | Create a distinct asset only after isolating the A5 concept crop and writing its geometry notes. |
| `B1` | Create a distinct asset only after isolating the B1 concept crop and writing its geometry notes. |
| `B2` | Create a distinct asset only after isolating the B2 concept crop and writing its geometry notes. |
| `B3` | Create a distinct asset only after isolating the B3 concept crop and writing its geometry notes. |
| `B4` | Create a distinct asset only after isolating the B4 concept crop and writing its geometry notes. |
| `B5` | Create a distinct asset only after isolating the B5 concept crop and writing its geometry notes. |

## New Required Workflow

1. Crop and label each concept cairn target from the approved board.
2. Create a one-page geometry brief per target: silhouette, major stone masses, ground contact, cloth/rawhide/paint placement, front/side/back inference, and scale.
3. Build only one or two targets first, not a full batch.
4. Render DCC proof directly beside the exact concept crop.
5. Do not import to Unreal until the DCC proof passes concept-geometry review.
6. Preserve round bases only if the specific concept target needs them; otherwise use irregular terrain-contact geometry.
7. Texture/material polish happens after geometry passes the concept audit.

## Boundary

This audit does not invalidate the technical import automation. It does invalidate using the current twelve-variant batch as final visual evidence. The current batch remains `Unreal import candidate` only and should be treated as requested changes for concept geometry.
