# Static Prop Reference Benchmarks A01

## Purpose

This benchmark records license-clean complete 3D asset packages used to study production packaging, not to define Aerathea visual canon. The downloaded assets are stored under ignored `Saved/AssetForgeResearch/benchmarks/reference_assets/` paths and must not be copied into Aerathea production art.

Use the findings here to improve Aerathea source packages, especially `SM_GIA_BloodAxeCairnTarget_A1_A01`, while keeping Aerathea's approved concept art as the visual source of truth.

## Source Assets

| Reference | Source URL | License evidence | Local research path | Why it was selected |
| --- | --- | --- | --- | --- |
| Kenney Graveyard Kit 5.0 | `https://kenney.nl/assets/graveyard-kit` | Page and local `License.txt` list Creative Commons CC0. | `Saved/AssetForgeResearch/benchmarks/reference_assets/unpacked/kenney_graveyard-kit_5.0/` | Low-poly static prop kit with grave stones, rocks, walls, previews, and multiple interchange formats. |
| Kenney Modular Dungeon Kit 2.1 | `https://kenney.nl/assets/modular-dungeon-kit` | Page and local `License.txt` list Creative Commons CC0. | `Saved/AssetForgeResearch/benchmarks/reference_assets/unpacked/kenney_modular-dungeon-kit_1.0/` | Modular environment kit with repeated parts, previews, and multiple interchange formats. The downloaded zip name is `1.0`, but the local license identifies package version 2.1. |
| Khronos Lantern glTF sample | `https://github.com/KhronosGroup/glTF-Sample-Models/tree/main/2.0/Lantern` | Local `README.md` lists CC0. | `Saved/AssetForgeResearch/benchmarks/reference_assets/unpacked/khronos_lantern_gltf/` | Compact PBR glTF sample with explicit base color, normal, roughness/metallic, and emissive maps. |

## Local Inventory

| Reference | Local package contents |
| --- | --- |
| Kenney Graveyard Kit 5.0 | 91 FBX files, 91 GLB files, 91 OBJ files plus 91 MTL files, 91 preview PNGs, and a shared `colormap.png` per model-format folder. |
| Kenney Modular Dungeon Kit 2.1 | 39 FBX files, 39 GLB files, 39 OBJ files plus 39 MTL files, 39 preview PNGs, and shared texture PNGs. |
| Khronos Lantern glTF sample | `Lantern.gltf`, `Lantern.bin`, `Lantern_baseColor.png`, `Lantern_normal.png`, `Lantern_roughnessMetallic.png`, `Lantern_emissive.png`, and `README.md`. |

## Audit Results

Audit script:

- `Tools/DCC/audit_reference_static_assets.py`

Ignored audit report:

- `Saved/AssetForgeResearch/benchmarks/reference_assets/reports/static_asset_reference_audit.json`

Representative sample stats:

| Sample | Mesh objects | Triangles | Vertices | Materials | Texture/map pattern |
| --- | ---: | ---: | ---: | ---: | --- |
| Kenney `rocks.obj` | 1 | 364 | 204 | 1 | Shared `colormap.png`. |
| Kenney `gravestone-broken.obj` | 1 | 134 | 76 | 1 | Shared `colormap.png`. |
| Kenney `stone-wall-damaged.obj` | 1 | 144 | 80 | 1 | Shared `colormap.png`. |
| Kenney `template-wall.obj` | 1 | 224 | 149 | 1 | Shared `colormap.png`. |
| Kenney `gate.obj` | 1 | 296 | 162 | 1 | Shared `colormap.png`. |
| Khronos `Lantern.gltf` | 3 glTF meshes | 5394 | 4145 | 1 | Base color, roughness/metallic, normal, emissive. |

## What The References Teach

- Complete packages include source-visible licensing, one or more interchange formats, and preview images.
- Simple prop kits often keep each asset to one mesh and one material, using shared textures for many related assets.
- Preview PNGs are valuable. They make browsing and review faster than opening every DCC file.
- File and folder consistency matters as much as mesh quality. Kenney repeats the same names across FBX, GLB, OBJ, MTL, and preview outputs.
- PBR examples make map intent explicit: base color, normal, roughness/metallic, and emissive maps are named and linked in the asset file.
- Interchange formats do not equal Unreal readiness. These references do not provide Aerathea-style LODs, UCX collision, Unreal import paths, gameplay scale checks, or concept-geometry approval sheets.

## What We Should Adopt For Aerathea

- Keep a license/source note for every external reference used in research.
- Keep raw downloaded references under ignored `Saved/AssetForgeResearch/` paths.
- For every Aerathea asset package, keep a production brief, source file, exports, proof renders, and status document together.
- Add a preview PNG or comparison sheet for every candidate, not just final assets.
- Make material-map naming explicit and predictable: `_BC`, `_N`, `_ORM`, optional `_E`.
- Keep static props to low material-slot counts unless the asset genuinely needs more.
- Preserve deterministic build scripts where possible so the package can be rebuilt after a reset.
- Treat missing LOD/collision/Unreal validation as a hard blocker for `Fully game-ready`.

## What We Should Not Adopt Blindly

- Do not copy reference silhouettes, texture art, or theme language.
- Do not use Kenney's very-low-poly style as the visual quality target for Aerathea.
- Do not treat glTF/FBX/OBJ availability as proof that an asset is game-ready.
- Do not skip concept matching. The Blood Axe A1 concept remains the visual target.

## Applied Gate For Blood Axe A1

Before `SM_GIA_BloodAxeCairnTarget_A1_A01` can move from `DCC source candidate` to `DCC game-ready candidate`, it needs:

1. A revised DCC mesh that matches the `BloodAxe A1` concept comparison better.
2. LOD0 geometry with sculpted/chipped slab contours, not blocky placeholder slabs.
3. UV0 verified for all renderable meshes.
4. Texture-map plan or generated candidate maps: base color, normal, ORM, optional emissive only if justified.
5. LOD0-LOD3 exports.
6. Broad UCX collision export.
7. Per-asset proof render and concept comparison sheet.
8. Status document updated with triangle counts, material slots, texture list, collision, and remaining gaps.
9. No Unreal import until the concept comparison passes visual review.

## Current Decision

The benchmark lane is complete enough to inform the next A1 revision. The next production step remains a second geometry pass on `SM_GIA_BloodAxeCairnTarget_A1_A01`, using the benchmark packaging checklist and the BloodAxe A1 concept side-by-side.
