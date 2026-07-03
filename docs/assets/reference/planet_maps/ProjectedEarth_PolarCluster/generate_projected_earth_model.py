import json
import math
import os
import zipfile
from pathlib import Path

import numpy as np
from PIL import Image
from mpl_toolkits.basemap import maskoceans

try:
    import trimesh
except Exception:
    trimesh = None

OUT = Path('/mnt/data/projected_earth_model')
OUT.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Planet constants
# -----------------------------
EARTH_EQUATORIAL_CIRCUMFERENCE_KM = 40075.017
EARTH_EQUATORIAL_RADIUS_KM = EARTH_EQUATORIAL_CIRCUMFERENCE_KM / (2 * math.pi)
TARGET_EQUATORIAL_CIRCUMFERENCE_KM = 91600.0
TARGET_RADIUS_KM = TARGET_EQUATORIAL_CIRCUMFERENCE_KM / (2 * math.pi)
TARGET_DIAMETER_KM = TARGET_RADIUS_KM * 2
SCALE_VS_EARTH = TARGET_EQUATORIAL_CIRCUMFERENCE_KM / EARTH_EQUATORIAL_CIRCUMFERENCE_KM
SURFACE_AREA_KM2 = 4 * math.pi * TARGET_RADIUS_KM**2
EARTH_SURFACE_AREA_KM2 = 4 * math.pi * EARTH_EQUATORIAL_RADIUS_KM**2
SURFACE_AREA_RATIO = SURFACE_AREA_KM2 / EARTH_SURFACE_AREA_KM2
MASS_RATIO_SAME_DENSITY = SCALE_VS_EARTH**3
GRAVITY_RATIO_SAME_DENSITY = SCALE_VS_EARTH

# Model units: 1 OBJ/GLB unit = 100 km. This keeps the model at a reasonable DCC size.
KM_PER_MODEL_UNIT = 100.0
TARGET_RADIUS_UNITS = TARGET_RADIUS_KM / KM_PER_MODEL_UNIT

# Polar remapping: preserve old Earth meridional distances by shrinking angular distance from the north pole
# by the scale factor. All original Earth latitudes fit in a new north-polar cap down to this latitude.
POLAR_CAP_EDGE_LAT_DEG = 90.0 - 180.0 / SCALE_VS_EARTH

# -----------------------------
# Original Earth land mask from Basemap/GSHHS coastline data.
# -----------------------------
print('Building original Earth land/ocean mask...')
ORIG_W, ORIG_H = 2048, 1024
orig_lons = np.linspace(-180, 180, ORIG_W, endpoint=False)
orig_lats = np.linspace(-90, 90, ORIG_H)
lon2, lat2 = np.meshgrid(orig_lons, orig_lats)
masked = maskoceans(lon2, lat2, np.ones_like(lon2), resolution='i', grid=1.25)
orig_land = ~np.ma.getmaskarray(masked)


def sample_orig_land(lon_deg, lat_deg):
    """Vectorized nearest-neighbor sample of the original Earth land mask."""
    lon_norm = (lon_deg + 180.0) % 360.0
    col = np.floor(lon_norm / 360.0 * ORIG_W).astype(np.int64)
    col = np.clip(col, 0, ORIG_W - 1)
    row = np.floor((lat_deg + 90.0) / 180.0 * (ORIG_H - 1)).astype(np.int64)
    row = np.clip(row, 0, ORIG_H - 1)
    return orig_land[row, col]


def map_new_to_old_lat(new_lat_deg):
    """Polar remap: new colatitude * scale => old colatitude."""
    theta_new = 90.0 - new_lat_deg
    theta_old = theta_new * SCALE_VS_EARTH
    old_lat = 90.0 - theta_old
    inside = theta_old <= 180.0
    return old_lat, inside


def pseudo_noise(lon_deg, lat_deg):
    lon = np.radians(lon_deg)
    lat = np.radians(lat_deg)
    n = (
        0.45 * np.sin(2.9 * lon + 1.7 * lat) +
        0.30 * np.sin(6.3 * lon - 2.1 * lat + 1.2) +
        0.20 * np.sin(13.7 * lon + 4.8 * lat + 2.4) +
        0.10 * np.cos(19.0 * lon - 8.0 * lat)
    )
    return np.clip((n + 1.05) / 2.1, 0, 1)

# -----------------------------
# Build equirectangular texture for the new larger planet.
# -----------------------------
print('Building projected polar-cluster texture...')
TEX_W, TEX_H = 4096, 2048
new_lons = np.linspace(-180, 180, TEX_W, endpoint=False)
new_lats = np.linspace(90, -90, TEX_H)
tex_lon, tex_lat = np.meshgrid(new_lons, new_lats)
old_lat, inside = map_new_to_old_lat(tex_lat)
land = inside & sample_orig_land(tex_lon, old_lat)

# Ocean background with subtle latitude/depth variation.
lat_factor = (np.sin(np.radians(tex_lat)) + 1) / 2
water_noise = pseudo_noise(tex_lon * 0.7, tex_lat * 0.9)
img = np.zeros((TEX_H, TEX_W, 3), dtype=np.uint8)
# Deep ocean -> slightly lighter polar water.
img[..., 0] = (8 + 10 * lat_factor + 5 * water_noise).astype(np.uint8)
img[..., 1] = (35 + 25 * lat_factor + 6 * water_noise).astype(np.uint8)
img[..., 2] = (83 + 45 * lat_factor + 10 * water_noise).astype(np.uint8)

# Land coloring: biome-ish green/tan/mountain/ice based on original latitude and procedural highlands.
n = pseudo_noise(tex_lon, old_lat)
abs_old_lat = np.abs(old_lat)
desert_band = np.exp(-((abs_old_lat - 24.0) / 12.0) ** 2)
highland = np.clip((n - 0.55) / 0.45, 0, 1)

base_green = np.array([70, 126, 58], dtype=float)
forest = np.array([35, 98, 47], dtype=float)
tan = np.array([173, 143, 82], dtype=float)
rock = np.array([137, 122, 96], dtype=float)
snow = np.array([222, 230, 229], dtype=float)

land_color = base_green[None, None, :] * (1 - n[..., None]) + forest[None, None, :] * n[..., None]
land_color = land_color * (1 - 0.55 * desert_band[..., None]) + tan[None, None, :] * (0.55 * desert_band[..., None])
land_color = land_color * (1 - 0.55 * highland[..., None]) + rock[None, None, :] * (0.55 * highland[..., None])

ice = land & ((old_lat < -62) | (old_lat > 72))
mountain_snow = land & (highland > 0.86) & (abs_old_lat > 35)
land_color[ice | mountain_snow] = snow
img[land] = np.clip(land_color[land], 0, 255).astype(np.uint8)

# Add a fine equator / cap edge guide as subtle cyan line in texture for model orientation.
# The exact cap edge is where the remapped old south pole reaches the new sphere.
edge_rows = np.where(np.abs(tex_lat[:, 0] - POLAR_CAP_EDGE_LAT_DEG) < (180 / TEX_H) * 0.8)[0]
for r in edge_rows:
    # make it subtle, only on ocean/near edge
    img[r:r+1, :, :] = (0.7 * img[r:r+1, :, :] + np.array([50, 105, 120]) * 0.3).astype(np.uint8)

texture_path = OUT / 'ProjectedEarth_PolarCluster_Texture_4096.png'
Image.fromarray(img).save(texture_path)

# Smaller land mask map for documentation.
mask_preview = np.zeros((TEX_H, TEX_W, 3), dtype=np.uint8)
mask_preview[..., :] = np.array([12, 40, 90], dtype=np.uint8)
mask_preview[land] = np.array([70, 145, 55], dtype=np.uint8)
mask_preview[ice] = np.array([235, 240, 240], dtype=np.uint8)
Image.fromarray(mask_preview).save(OUT / 'ProjectedEarth_PolarCluster_LandMask.png')

# -----------------------------
# Mesh builders
# -----------------------------
def sph_to_cart(radius_units, lon_deg, lat_deg):
    lon = math.radians(float(lon_deg))
    lat = math.radians(float(lat_deg))
    x = radius_units * math.cos(lat) * math.cos(lon)
    y = radius_units * math.cos(lat) * math.sin(lon)
    z = radius_units * math.sin(lat)
    return x, y, z


def land_height_units(lon_deg, new_lat_deg):
    old_lat_val, inside_val = map_new_to_old_lat(np.array(new_lat_deg))
    if not bool(inside_val):
        return 0.0
    n_val = float(pseudo_noise(np.array(lon_deg), np.array(old_lat_val)))
    # Real-scale relief + tiny offset above ocean: 1 unit = 100 km.
    # 0.025 units = 2.5 km base relief, up to ~9 km highland. Good for visible but still near real scale.
    return 0.025 + 0.065 * max(0.0, n_val - 0.25) / 0.75


def is_projected_land(lon_deg, new_lat_deg):
    old_lat_val, inside_val = map_new_to_old_lat(np.array(new_lat_deg))
    if not bool(inside_val):
        return False, float(old_lat_val)
    return bool(sample_orig_land(np.array(lon_deg), np.array(old_lat_val))), float(old_lat_val)

print('Writing OBJ/MTL mesh...')
obj_path = OUT / 'ProjectedEarth_PolarCluster_Model.obj'
mtl_path = OUT / 'ProjectedEarth_PolarCluster_Model.mtl'

mtl_text = f"""# Materials for ProjectedEarth_PolarCluster_Model.obj
# 1 model unit = {KM_PER_MODEL_UNIT:g} km
newmtl PlanetTexture
Ka 1.000 1.000 1.000
Kd 1.000 1.000 1.000
Ks 0.150 0.150 0.150
Ns 64.000
map_Kd {texture_path.name}

newmtl RaisedLand
Ka 0.090 0.190 0.070
Kd 0.190 0.560 0.180
Ks 0.080 0.080 0.060
Ns 24.000

newmtl IceLand
Ka 0.700 0.730 0.730
Kd 0.880 0.920 0.920
Ks 0.250 0.250 0.250
Ns 48.000
"""
mtl_path.write_text(mtl_text)

with obj_path.open('w') as f:
    f.write('# Projected Earth polar-cluster planet model\n')
    f.write(f'# Target equatorial circumference: {TARGET_EQUATORIAL_CIRCUMFERENCE_KM:,.3f} km\n')
    f.write(f'# Target radius: {TARGET_RADIUS_KM:,.3f} km\n')
    f.write(f'# Model scale: 1 OBJ unit = {KM_PER_MODEL_UNIT:g} km; radius = {TARGET_RADIUS_UNITS:.6f} units\n')
    f.write(f'mtllib {mtl_path.name}\n\n')

    # Textured full sphere.
    lat_div = 128
    lon_div = 256
    f.write('o Textured_Project_Earth_Surface\n')
    f.write('usemtl PlanetTexture\n')
    vert_start = 1
    uv_start = 1
    vertices = []
    uvs = []
    for i in range(lat_div + 1):
        lat = -90.0 + 180.0 * i / lat_div
        for j in range(lon_div + 1):
            lon = -180.0 + 360.0 * j / lon_div
            vertices.append(sph_to_cart(TARGET_RADIUS_UNITS, lon, lat))
            uvs.append((j / lon_div, i / lat_div))
    for v in vertices:
        f.write(f'v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n')
    for uv in uvs:
        f.write(f'vt {uv[0]:.6f} {uv[1]:.6f}\n')
    def idx(i, j):
        return vert_start + i * (lon_div + 1) + j
    def tidx(i, j):
        return uv_start + i * (lon_div + 1) + j
    for i in range(lat_div):
        for j in range(lon_div):
            a, b, c, d = idx(i,j), idx(i,j+1), idx(i+1,j+1), idx(i+1,j)
            ta, tb, tc, td = tidx(i,j), tidx(i,j+1), tidx(i+1,j+1), tidx(i+1,j)
            f.write(f'f {a}/{ta} {b}/{tb} {c}/{tc} {d}/{td}\n')
    current_vert = vert_start + len(vertices)

    # Raised land cells; group by material for manageable material switches.
    land_lon_div = 360
    land_lat_div = 180
    cells_land = []
    cells_ice = []
    for i in range(land_lat_div):
        lat0 = -90.0 + 180.0 * i / land_lat_div
        lat1 = -90.0 + 180.0 * (i + 1) / land_lat_div
        latc = (lat0 + lat1) / 2.0
        # skip southern ocean below cap edge quickly
        if lat1 < POLAR_CAP_EDGE_LAT_DEG - 1.5:
            continue
        for j in range(land_lon_div):
            lon0 = -180.0 + 360.0 * j / land_lon_div
            lon1 = -180.0 + 360.0 * (j + 1) / land_lon_div
            lonc = (lon0 + lon1) / 2.0
            hit, oldlat_c = is_projected_land(lonc, latc)
            if not hit:
                continue
            is_ice = (oldlat_c < -62.0) or (oldlat_c > 72.0)
            (cells_ice if is_ice else cells_land).append((lon0, lon1, lat0, lat1))

    def write_cells(name, material, cells):
        nonlocal_current = None
        f.write(f'\no {name}\n')
        f.write(f'usemtl {material}\n')
        base = write_cells.current_vert
        local_v_count = 0
        for lon0, lon1, lat0, lat1 in cells:
            corners = [(lon0, lat0), (lon1, lat0), (lon1, lat1), (lon0, lat1)]
            inds = []
            for lon, lat in corners:
                h = land_height_units(lon, lat)
                v = sph_to_cart(TARGET_RADIUS_UNITS + h, lon, lat)
                f.write(f'v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n')
                local_v_count += 1
                inds.append(base + local_v_count - 1)
            f.write(f'f {inds[0]} {inds[1]} {inds[2]} {inds[3]}\n')
        write_cells.current_vert = base + local_v_count
    write_cells.current_vert = current_vert
    write_cells('Raised_Project_Earth_Land', 'RaisedLand', cells_land)
    write_cells('Raised_Project_Earth_Ice_Land', 'IceLand', cells_ice)

# -----------------------------
# Optional GLB export using vertex colors.
# -----------------------------
print('Writing GLB mesh...')
glb_path = OUT / 'ProjectedEarth_PolarCluster_Model.glb'
if trimesh is not None:
    # Build a moderately detailed vertex-colored sphere and land overlay.
    lat_div = 96
    lon_div = 192
    verts = []
    faces = []
    colors = []
    for i in range(lat_div + 1):
        lat = -90.0 + 180.0 * i / lat_div
        for j in range(lon_div):
            lon = -180.0 + 360.0 * j / lon_div
            verts.append(sph_to_cart(TARGET_RADIUS_UNITS, lon, lat))
            # sample texture colors using same map, but directly compute land/water to avoid reading image.
            oldlat_v, inside_v = map_new_to_old_lat(np.array(lat))
            is_land = bool(inside_v) and bool(sample_orig_land(np.array(lon), np.array(oldlat_v)))
            if is_land:
                if oldlat_v < -62 or oldlat_v > 72:
                    colors.append([220, 230, 230, 255])
                else:
                    nv = float(pseudo_noise(np.array(lon), np.array(oldlat_v)))
                    colors.append([int(40 + 70*nv), int(100 + 60*nv), int(35 + 45*nv), 255])
            else:
                colors.append([12, 48, 105, 255])
    def vi(i, j):
        return i * lon_div + (j % lon_div)
    for i in range(lat_div):
        for j in range(lon_div):
            faces.append([vi(i, j), vi(i, j+1), vi(i+1, j+1)])
            faces.append([vi(i, j), vi(i+1, j+1), vi(i+1, j)])
    sphere_mesh = trimesh.Trimesh(vertices=np.array(verts), faces=np.array(faces), process=False)
    sphere_mesh.visual.vertex_colors = np.array(colors, dtype=np.uint8)

    # Land overlay in GLB with vertex colors.
    lv = []
    lf = []
    lc = []
    land_lon_div = 240
    land_lat_div = 120
    for i in range(land_lat_div):
        lat0 = -90.0 + 180.0 * i / land_lat_div
        lat1 = -90.0 + 180.0 * (i + 1) / land_lat_div
        latc = (lat0 + lat1) / 2
        if lat1 < POLAR_CAP_EDGE_LAT_DEG - 1.5:
            continue
        for j in range(land_lon_div):
            lon0 = -180.0 + 360.0 * j / land_lon_div
            lon1 = -180.0 + 360.0 * (j + 1) / land_lon_div
            lonc = (lon0 + lon1) / 2
            hit, oldlat_c = is_projected_land(lonc, latc)
            if not hit:
                continue
            start = len(lv)
            is_ice_cell = (oldlat_c < -62.0) or (oldlat_c > 72.0)
            rgba = [225, 235, 235, 255] if is_ice_cell else [55, 150, 50, 255]
            for lon, lat in [(lon0,lat0),(lon1,lat0),(lon1,lat1),(lon0,lat1)]:
                h = land_height_units(lon, lat) + 0.015
                lv.append(sph_to_cart(TARGET_RADIUS_UNITS + h, lon, lat))
                lc.append(rgba)
            lf.append([start, start+1, start+2])
            lf.append([start, start+2, start+3])
    if lv:
        land_mesh = trimesh.Trimesh(vertices=np.array(lv), faces=np.array(lf), process=False)
        land_mesh.visual.vertex_colors = np.array(lc, dtype=np.uint8)
        scene = trimesh.Scene({'textured_surface_vertex_color': sphere_mesh, 'raised_land': land_mesh})
    else:
        scene = trimesh.Scene({'textured_surface_vertex_color': sphere_mesh})
    scene.export(glb_path)
else:
    glb_path = None

# -----------------------------
# Previews
# -----------------------------
print('Writing preview images...')
# Downscaled map preview
map_preview_path = OUT / 'ProjectedEarth_PolarCluster_MapPreview.png'
Image.fromarray(img).resize((1600, 800), Image.Resampling.LANCZOS).save(map_preview_path)

# 3D-ish preview rendered with matplotlib
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

    img_small = np.asarray(Image.fromarray(img).resize((384, 192), Image.Resampling.BILINEAR)) / 255.0
    lon_grid = np.linspace(-math.pi, math.pi, 384)
    lat_grid = np.linspace(math.pi/2, -math.pi/2, 192)
    lonm, latm = np.meshgrid(lon_grid, lat_grid)
    # Use normalized radius for preview.
    x = np.cos(latm) * np.cos(lonm)
    y = np.cos(latm) * np.sin(lonm)
    z = np.sin(latm)
    fig = plt.figure(figsize=(8, 8), dpi=180)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=2, cstride=2, facecolors=img_small, linewidth=0, antialiased=False, shade=False)
    ax.set_box_aspect([1,1,1])
    ax.view_init(elev=22, azim=-50)
    ax.set_axis_off()
    ax.set_title('Projected Earth: 91,600 km circumference, polar landmass cluster', pad=20)
    preview_path = OUT / 'ProjectedEarth_PolarCluster_3DPreview.png'
    plt.savefig(preview_path, bbox_inches='tight', pad_inches=0.1, transparent=False)
    plt.close(fig)

    # North pole view preview
    fig = plt.figure(figsize=(8, 8), dpi=180)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=2, cstride=2, facecolors=img_small, linewidth=0, antialiased=False, shade=False)
    ax.set_box_aspect([1,1,1])
    ax.view_init(elev=90, azim=-90)
    ax.set_axis_off()
    ax.set_title('North pole cluster view', pad=20)
    preview_north_path = OUT / 'ProjectedEarth_PolarCluster_NorthPolePreview.png'
    plt.savefig(preview_north_path, bbox_inches='tight', pad_inches=0.1, transparent=False)
    plt.close(fig)
except Exception as e:
    print('Preview render failed:', e)

# -----------------------------
# Specs and README
# -----------------------------
spec = {
    "name": "ProjectedEarth_PolarCluster",
    "description": "Hypothetical Earth landmasses remapped into a northern polar cap on a 91,600 km circumference rocky planet.",
    "source_assumption": "Land/ocean outlines use bundled Basemap/GSHHS coastline mask; elevations are procedural visual relief, not real Earth DEM data.",
    "target_equatorial_circumference_km": TARGET_EQUATORIAL_CIRCUMFERENCE_KM,
    "target_radius_km": TARGET_RADIUS_KM,
    "target_diameter_km": TARGET_DIAMETER_KM,
    "scale_vs_earth_equatorial_circumference": SCALE_VS_EARTH,
    "surface_area_km2": SURFACE_AREA_KM2,
    "surface_area_ratio_vs_earth": SURFACE_AREA_RATIO,
    "same_density_mass_ratio_vs_earth": MASS_RATIO_SAME_DENSITY,
    "same_density_surface_gravity_ratio_vs_earth": GRAVITY_RATIO_SAME_DENSITY,
    "same_density_surface_gravity_m_s2": GRAVITY_RATIO_SAME_DENSITY * 9.80665,
    "model_units": {
        "km_per_model_unit": KM_PER_MODEL_UNIT,
        "radius_model_units": TARGET_RADIUS_UNITS,
        "diameter_model_units": TARGET_RADIUS_UNITS * 2
    },
    "polar_projection": {
        "method": "azimuthal-equidistant-style remap from old Earth north pole",
        "new_colatitude_degrees": "old_colatitude_degrees / scale_vs_earth",
        "old_colatitude_degrees": "new_colatitude_degrees * scale_vs_earth",
        "projected_cap_edge_latitude_degrees_north": POLAR_CAP_EDGE_LAT_DEG
    },
    "files": {
        "obj": obj_path.name,
        "mtl": mtl_path.name,
        "glb": glb_path.name if glb_path else None,
        "texture": texture_path.name,
        "map_preview": map_preview_path.name,
        "land_mask": "ProjectedEarth_PolarCluster_LandMask.png"
    }
}
(OUT / 'planet_specs.json').write_text(json.dumps(spec, indent=2))

readme = f"""# Projected Earth Polar-Cluster Planet Model

This package contains a practical 3D reference model for the hypothetical planet described in the prompt:
Earth-like landmasses remapped around the north pole on a larger rocky planet with an equatorial circumference of **{TARGET_EQUATORIAL_CIRCUMFERENCE_KM:,.0f} km**.

## Core scale

- Equatorial circumference: **{TARGET_EQUATORIAL_CIRCUMFERENCE_KM:,.0f} km**
- Radius: **{TARGET_RADIUS_KM:,.2f} km**
- Diameter: **{TARGET_DIAMETER_KM:,.2f} km**
- Width scale vs Earth: **{SCALE_VS_EARTH:.4f}x**
- Surface area: **{SURFACE_AREA_KM2/1e9:.3f} billion km²**
- Same-density mass estimate: **{MASS_RATIO_SAME_DENSITY:.2f} Earth masses**
- Same-density gravity estimate: **{GRAVITY_RATIO_SAME_DENSITY:.2f} g** / **{GRAVITY_RATIO_SAME_DENSITY*9.80665:.2f} m/s²**

> Note: at the same average density, mass scales with radius³, while surface gravity scales with radius. So this world is about 12x Earth mass, but about 2.3g surface gravity — not 12g.

## Model scale

The OBJ/GLB uses:

**1 model unit = {KM_PER_MODEL_UNIT:g} km**

So the planet radius in the model is **{TARGET_RADIUS_UNITS:.6f} units** and the diameter is **{TARGET_RADIUS_UNITS*2:.6f} units**.

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
new_colatitude = old_colatitude / {SCALE_VS_EARTH:.6f}
old_colatitude = new_colatitude * {SCALE_VS_EARTH:.6f}
```

All original Earth land/ocean features fit into a northern cap ending near **{POLAR_CAP_EDGE_LAT_DEG:.2f}°N** on the larger planet. South of that latitude is open ocean.

## Important accuracy note

The coastline/land mask is based on Basemap/GSHHS coastline data available in this runtime. The relief is procedural visual relief, not a real digital elevation model. Treat this as a planet-scale layout/modeling reference rather than a scientifically exact geological reconstruction.

## Unreal / Codex handoff notes

For Unreal, import the OBJ through Blender or directly into Unreal depending on your preferred workflow. If using Unreal centimeters, avoid importing this at true centimeter scale; keep the mesh as a reference planet, then scale it relative to your gameplay world.

Suggested game workflow:

1. Use this model as the macro world reference.
2. Convert the polar cluster into a playable world map or heightfield in tiles.
3. Use `planet_specs.json` as the source of truth for radius, circumference, gravity, and projection constants.
4. Keep the raised land overlay for visual reference, then replace it with proper terrain tiles when building playable zones.
"""
(OUT / 'README.md').write_text(readme)

# Copy generator script into package.
this_script = Path('/mnt/data/build_projected_earth_model.py')
if this_script.exists():
    (OUT / 'generate_projected_earth_model.py').write_text(this_script.read_text())

# Zip package
zip_path = Path('/mnt/data/ProjectedEarth_PolarCluster_Model_Package.zip')
if zip_path.exists():
    zip_path.unlink()
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(OUT.iterdir()):
        z.write(p, arcname=p.name)

print('DONE')
print(zip_path)
print('Files:')
for p in sorted(OUT.iterdir()):
    print(p.name, p.stat().st_size)
