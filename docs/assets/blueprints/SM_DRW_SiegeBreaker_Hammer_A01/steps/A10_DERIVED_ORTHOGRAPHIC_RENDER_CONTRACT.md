# A10 Derived Orthographic Render Contract

- Contract ID: `SB-ORTHO-A10-DERIVED-A01`
- Asset: `SM_DRW_SiegeBreaker_Hammer_A01`
- Date: 2026-07-22
- Status: `approved by Flamestrike direction to proceed`

## Exact Authorized Step

Open the approved A09 Blender source read-only, render front, back, left,
right, top, and bottom orthographic views at one common metric scale, package
the six unchanged Blender renders into one review board, validate the source
identity and outputs, checkpoint, and open the exact board visibly.

## Sole 3D Authority

- local-only A09 Blender source:
  `SourceAssets/Blender/Weapons/Dwarven/SM_DRW_SiegeBreaker_Hammer_A01/A09_PixelHalfMirror_VisualMatch_A01/SM_DRW_SiegeBreaker_Hammer_A01_A09_PixelHalfMirror_VisualMatch_A01.blend`
- required SHA-256:
  `06ffb121d00cddb7b9e30a60067a5036a851d285f15daca3bffe3a663fd6d78f`
- required object:
  `SM_DRW_SiegeBreaker_Hammer_A01_A09_CompleteMirroredModel`
- approved envelope:
  `75.130516 x 32.957619 x 170.000000 cm`

## Camera and Output Rules

- camera type: true Blender orthographic;
- views: `front`, `back`, `left`, `right`, `top`, `bottom`;
- all views use one `190 cm` orthographic scale and `1200 x 1600` frame;
- all cameras target the evaluated bounds center;
- source colors and materials remain unchanged;
- the `.blend` must not be saved or altered;
- the `.blend` hash must match before and after rendering;
- each render and the combined board must be hash-locked.

## Required Outputs

- six individual Blender orthographic PNGs;
- one labeled six-view review board;
- one validation manifest;
- one output record;
- one visible Flamestrike decision gate.

## Prohibited

- mesh, material, UV, transform, scale, or source-file edits;
- reconstruction or hidden-surface invention;
- generated imagery, TRELLIS, diffusion, or image-to-3D;
- FBX/GLB export, retopology, LODs, collision, Unreal, or game-ready claims;
- advancing after visible review without a new explicit decision.

## Decision

This step produces one Flamestrike classification for the six derived views:
`approved`, `revise`, `rejected`, or `blocked`.
