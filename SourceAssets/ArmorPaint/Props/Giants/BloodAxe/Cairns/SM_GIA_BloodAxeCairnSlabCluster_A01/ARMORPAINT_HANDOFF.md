# SM_GIA_BloodAxeCairnSlabCluster_A01 ArmorPaint Handoff

## Goal

Paint the cairn to match `A1_ConceptReference.png`, not the current procedural Blender render.

This pass is for visual art-match approval before Unreal import or canon lock.

## Open In ArmorPaint

Paint target mesh:

`SM_GIA_BloodAxeCairnSlabCluster_A01_LOD0_PaintTarget.fbx`

Launcher:

`Tools/DCC/launch_armorpaint_cairn_A01.sh`

If the detached launcher starts a process but does not show a visible paint window, open ArmorPaint from the desktop app menu and load the paint target mesh manually.

Reference:

`A1_ConceptReference.png`

Starter maps:

- `T_GIA_BloodAxeCairnSlabCluster_A01_BC_Starter.png`
- `T_GIA_BloodAxeCairnSlabCluster_A01_N_Starter.png`
- `T_GIA_BloodAxeCairnSlabCluster_A01_ORM_Starter.png`

Painted preview maps:

- `T_GIA_BloodAxeCairnSlabCluster_A01_BC_PaintedPreview.png`
- `T_GIA_BloodAxeCairnSlabCluster_A01_N_PaintedPreview.png`
- `T_GIA_BloodAxeCairnSlabCluster_A01_ORM_PaintedPreview.png`

Preview render:

- `PaintedApprovalReview.png`

## Paint Priorities

1. Darken the stone mass so it reads like charcoal highland stone, not pale concrete.
2. Break the slab faces with broad hand-painted value shifts and chipped edges.
3. Keep red Blood Axe paint weathered, broad, and irregular. It should look painted onto stone, not like a UI symbol or separate red bars.
4. Add ash and mud staining around the base and lower stones.
5. Make rawhide dark, worn, and secondary. It should not read as wood planks.
6. Preserve readable mid-poly silhouettes. Do not add dense micro-scratches or noisy detail.

## Export Targets

Export final maps to:

- `T_GIA_BloodAxeCairnSlabCluster_A01_BC_Painted.png`
- `T_GIA_BloodAxeCairnSlabCluster_A01_N_Painted.png`
- `T_GIA_BloodAxeCairnSlabCluster_A01_ORM_Painted.png`

Recommended size: 2048 x 2048 for paint review, downsample to 1024 x 1024 only after approval if needed.

## Approval Boundary

Do not mark this as final art, approved canon, Unreal import complete, or gameplay-ready collision until Flamestrike approves the painted result and an Unreal import validation pass is run.
