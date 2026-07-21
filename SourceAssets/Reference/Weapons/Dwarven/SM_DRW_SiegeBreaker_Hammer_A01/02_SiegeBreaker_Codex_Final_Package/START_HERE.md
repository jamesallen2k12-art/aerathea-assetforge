# Siege Breaker — Codex Final Package

This package is designed to let Codex create an exact blockout first and a detailed game asset second.

## Authoritative files
1. `asset_spec.json`
2. `dimensions_cm.csv`
3. `blender/build_siege_breaker_blockout.py`
4. deterministic renders created by `blender/render_six_orthographic_views.py`

The included AI concept sheet is a **style reference only**. It is not accepted as mathematically authoritative because independently illustrated panels can drift.

## Resolved length relationship
The dimensions originally appear to total 174 cm if simply added:

- head height: 38 cm
- structural shaft: 118 cm
- pommel: 18 cm

The package resolves this with a documented **4 cm structural shaft insertion into the pommel**:

- head spans Z = 132–170 cm
- shaft spans Z = 14–132 cm, length 118 cm
- pommel spans Z = 0–18 cm, length 18 cm
- shaft and pommel overlap from Z = 14–18 cm
- overall asset spans Z = 0–170 cm

This overlap is authoritative unless deliberately revised and recorded.
