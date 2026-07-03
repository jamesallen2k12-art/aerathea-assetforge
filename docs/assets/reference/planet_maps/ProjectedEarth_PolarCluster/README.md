# Projected Earth Polar-Cluster Planet Model

This package contains a practical 3D reference model for the hypothetical planet described in the prompt:
Earth-like landmasses remapped around the north pole on a larger rocky planet with an equatorial circumference of **91,600 km**.

## Core scale

- Equatorial circumference: **91,600 km**
- Radius: **14,578.59 km**
- Diameter: **29,157.19 km**
- Width scale vs Earth: **2.2857x**
- Surface area: **2.671 billion km²**
- Same-density mass estimate: **11.94 Earth masses**
- Same-density gravity estimate: **2.29 g** / **22.42 m/s²**

> Note: at the same average density, mass scales with radius³, while surface gravity scales with radius. So this world is about 12x Earth mass, but about 2.3g surface gravity — not 12g.

## Model scale

The OBJ/GLB uses:

**1 model unit = 100 km**

So the planet radius in the model is **145.785928 units** and the diameter is **291.571856 units**.

## Included files

- `ProjectedEarth_PolarCluster_Model.obj` — OBJ model with textured planet surface and raised land overlay.
- `ProjectedEarth_PolarCluster_Model.mtl` — material file for the OBJ.
- `ProjectedEarth_PolarCluster_Texture_4096.png` — 4096×2048 projected color texture.
- `ProjectedEarth_PolarCluster_Model.glb` — GLB version with vertex colors for quick preview/import.
- `ProjectedEarth_PolarCluster_3DPreview.png` — quick 3D preview render.
- `ProjectedEarth_PolarCluster_NorthPolePreview.png` — top-down polar preview.
- `ProjectedEarth_PolarCluster_MapPreview.png` — flattened map preview.
- `ProjectedEarth_PolarCluster_LandMask.png` — land/ocean mask used by the texture.
- `planet_specs.json` — machine-readable scale/projection constants.
- `generate_projected_earth_model.py` — reproducible generator script.

## Projection method

The model uses a polar remap that keeps the old Earth longitude as the azimuth around the new north pole.
Old Earth colatitude is mapped like this:

```text
new_colatitude = old_colatitude / 2.285713
old_colatitude = new_colatitude * 2.285713
```

All original Earth land/ocean features fit into a northern cap ending near **11.25°N** on the larger planet. South of that latitude is open ocean.

## Important accuracy note

The coastline/land mask is based on Basemap/GSHHS coastline data available in this runtime. The relief is procedural visual relief, not a real digital elevation model. Treat this as a planet-scale layout/modeling reference rather than a scientifically exact geological reconstruction.

## Unreal / Codex handoff notes

For Unreal, import the OBJ through Blender or directly into Unreal depending on your preferred workflow. If using Unreal centimeters, avoid importing this at true centimeter scale; keep the mesh as a reference planet, then scale it relative to your gameplay world.

Suggested game workflow:

1. Use this model as the macro world reference.
2. Convert the polar cluster into a playable world map or heightfield in tiles.
3. Use `planet_specs.json` as the source of truth for radius, circumference, gravity, and projection constants.
4. Keep the raised land overlay for visual reference, then replace it with proper terrain tiles when building playable zones.
