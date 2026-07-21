# Siege Breaker Orthographic Render Requirements

The authoritative set must be generated from one unchanged Blender collection named `SB_ASSET`.

- resolution: 2048 × 2048 PNG for every view
- identical orthographic scale for all six views
- white or transparent background
- no perspective
- no object rotation between the six fixed-object renders
- manifest records pixels-per-centimeter

True top and bottom views look along the hammer's Z axis and therefore do **not** show the full 170 cm length. That is correct. Optional rotated full-length top/bottom presentation views must be stored separately and marked non-authoritative.
