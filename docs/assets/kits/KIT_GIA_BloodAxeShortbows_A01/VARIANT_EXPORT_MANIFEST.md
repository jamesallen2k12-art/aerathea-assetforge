# KIT_GIA_BloodAxeShortbows_A01 Variant Export Manifest

## Scope

- Task: `AET-MA-20260629-083`
- Scope type: docs-only variant/export manifest for future DCC planning
- Parent kit: `KIT_GIA_BloodAxeShortbows_A01`
- Parent source: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#Bow_Shortbow_Set`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: path and export planning only; no build target selected

This manifest names planned child meshes, source path plans, export path plans, Unreal path plans, pivots, scale notes, material slot limits, LOD expectations, collision policy, and blockers for the Giant-scaled Blood Axe shortbow mini-kit. It does not create folders, source files, FBX files, Unreal assets, tools, validators, runtime source, material assets, startup-scene placements, or final visual approval.

## Dependencies

- `docs/assets/kits/KIT_GIA_BloodAxeShortbows_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeShortbows_A01/CHILD_ASSET_INTAKE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeLongbow_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeLongbow_A02/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeLongbow_A03/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`
- Future Giant base attachment and scale validation against `SK_GIA_Base_A01`
- Future quiver, arrow, socket, animation, and projectile approvals before any gameplay-facing bow work

## Giant Scale Lock

- Female Giants: 14-15 ft / 427-457 cm.
- Male Giants: 14'10"-16'0" / 452-488 cm.
- Validated baseline references inherited from `SK_GIA_Base_A01`: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5".
- Author future DCC in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.
- Shortbows are compact only relative to Blood Axe Giant longbows; they must not shrink into normal humanoid bow proportions.

## Source-Storage Guardrail

The source concept remains in the external concept folder only. This docs-only manifest does not copy, move, edit, embed, crop, commit, or otherwise store `BloodAxeArmory.png` or any derivative source concept inside the repository. All paths below are planned storage paths only and do not imply the folders or files currently exist.

## Culture Separation

Blood Axe is a hostile Giant sub-faction only. This manifest must not redefine neutral or civilized Giant culture. Blood Axe red-black raider materials, crude bowyer repairs, dark highland wood, scorched leather, blackened iron, horn, bone, soot, grime, and dull red cloth stay separate from neutral Giant cave-town, blue-gray stoneworker, warm hearth, monumental masonry, restrained blue rune, and civilized highland craft language.

## Docs-Only and No-Build Guardrails

- No DCC source creation.
- No Blender source folders or `.blend` files.
- No FBX export.
- No Unreal Content assets, imports, materials, textures, Blueprints, startup actors, or validators.
- No runtime source edits.
- No global index, task board, backlog, bootstrap, or external concept folder edits.
- No copied source concept or embedded source image.
- No final visual approval or approval capture.
- No first DCC target selection; lead approval is still required before choosing any build target.
- No projectile behavior, projectile collision, arrow flight, hit logic, damage volume, combat trace, combat stat, range value, rarity value, loot rule, pickup rule, inventory rule, arrow inventory, ammunition count, bow draw distance, draw timing, release timing, reload timing, montage timing, repair interaction timing, cloth simulation, physics simulation, or runtime equip behavior.

## Variant Export Table

All planned paths are path plans only. Do not create these folders or files from this manifest task.

| Variant | Planned mesh name | Planned Blender source path | Planned export path | Planned Unreal path | Pivot | Scale notes | Material slots | LOD expectations | Collision policy | Implementation blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hunter shortbow | `SM_GIA_BloodAxeHunterShortbow_A01` | Planned only: `SourceAssets/Blender/Weapons/Giants/BloodAxe/Shortbows/SM_GIA_BloodAxeHunterShortbow_A01/SM_GIA_BloodAxeHunterShortbow_A01.blend` | Planned only: `SourceAssets/Exports/Weapons/Giants/BloodAxe/Shortbows/SM_GIA_BloodAxeHunterShortbow_A01/SM_GIA_BloodAxeHunterShortbow_A01.fbx` | Planned only: `/Game/Aerathea/Weapons/Giants/BloodAxe/Shortbows/SM_GIA_BloodAxeHunterShortbow_A01` | Center of main grip | 300-335 cm unstrung height; 11-19 cm stave thickness; 34-48 cm grip height; sized to Giant hunter hands and not normal humanoids | 1 target, 2 max if string/leather must separate from stave/metal | LOD0 3.5k-6.5k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve arc, grip, nocks, string, and red marker | Equipped collision disabled; display may use one long capsule or narrow box plus optional small grip box only by later pickup/display approval; no projectile collision | Blocked until lead selects a DCC target and separate DCC/export/Unreal tasks approve folder creation, FBX export, import, socket review, quiver clearance, animation boundaries, and final visual review |
| Scout compact bow | `SM_GIA_BloodAxeScoutShortbow_A01` | Planned only: `SourceAssets/Blender/Weapons/Giants/BloodAxe/Shortbows/SM_GIA_BloodAxeScoutShortbow_A01/SM_GIA_BloodAxeScoutShortbow_A01.blend` | Planned only: `SourceAssets/Exports/Weapons/Giants/BloodAxe/Shortbows/SM_GIA_BloodAxeScoutShortbow_A01/SM_GIA_BloodAxeScoutShortbow_A01.fbx` | Planned only: `/Game/Aerathea/Weapons/Giants/BloodAxe/Shortbows/SM_GIA_BloodAxeScoutShortbow_A01` | Center of main grip | 240-290 cm unstrung height; 10-17 cm stave thickness; 30-44 cm grip height; compact only relative to Giant longbows; keep clearance for scout carry | 1 target, 2 max | LOD0 2.8k-5.5k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve tight C arc, grip, nocks, string, and carry silhouette | Equipped collision disabled; display uses one narrow capsule or box if approved; no per-string, per-wrap, projectile, or combat collision | Blocked until lead-selected DCC target, Giant carry clearance, back/side socket policy, quiver dependency, DCC source approval, export approval, Unreal import approval, and visual approval are assigned |
| Camp rack bow | `SM_GIA_BloodAxeCampRackShortbow_A01` | Planned only: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Shortbows/SM_GIA_BloodAxeCampRackShortbow_A01/SM_GIA_BloodAxeCampRackShortbow_A01.blend` | Planned only: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Shortbows/SM_GIA_BloodAxeCampRackShortbow_A01/SM_GIA_BloodAxeCampRackShortbow_A01.fbx` | Planned only: `/Game/Aerathea/Props/Giants/BloodAxeArmory/Shortbows/SM_GIA_BloodAxeCampRackShortbow_A01` | Center of main grip; optional display duplicate may use rack-contact or ground pivot only by future approval | 265-325 cm unstrung height; flatter rack-facing presentation; stable display contact points; static Giant camp dressing scale | 1 target, 2 max | LOD0 2.5k-5k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve rack-facing bow arc and contact silhouette | Display-only one long capsule or box if needed; no equip, pickup, projectile, per-string, or combat collision in this manifest | Blocked until DCC target selection, static display placement rules, collision proxy approval, source/export creation approval, Unreal import approval, and final visual review |
| Repaired spare bow | `SM_GIA_BloodAxeRepairedShortbow_A01` | Planned only: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Shortbows/SM_GIA_BloodAxeRepairedShortbow_A01/SM_GIA_BloodAxeRepairedShortbow_A01.blend` | Planned only: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Shortbows/SM_GIA_BloodAxeRepairedShortbow_A01/SM_GIA_BloodAxeRepairedShortbow_A01.fbx` | Planned only: `/Game/Aerathea/Props/Giants/BloodAxeArmory/Shortbows/SM_GIA_BloodAxeRepairedShortbow_A01` | Center of main grip unless later promoted to display-only lean variant | 250-315 cm unstrung height; large splints and patch plates must not overpower the primary bow arc; Giant repair handling scale | 1 target, 2 max | LOD0 3.5k-7k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve arc, grip, replacement nock, primary repair mass, and red faction block | One display capsule or box; no per-splint, per-lashing, per-patch, projectile, or combat collision | Blocked until repaired-bow visual density review, DCC target selection, source/export approval, import approval, collision proxy approval, and no-gameplay boundaries are assigned |
| String coil | `SM_GIA_BloodAxeShortbowStringCoil_A01` | Planned only: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowStringCoil_A01/SM_GIA_BloodAxeShortbowStringCoil_A01.blend` | Planned only: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowStringCoil_A01/SM_GIA_BloodAxeShortbowStringCoil_A01.fbx` | Planned only: `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowStringCoil_A01` | Center of coil mass | 36-70 cm coil diameter; 6-13 cm cord thickness; spare sinew/rawhide shortbow string scale for Giant bowyer shelves | 1 target | LOD0 350-1.1k tris per coil/folded string; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve coil mass and cord read | One simple box or capsule only if world placed; no string deformation, tension, projectile, equip, or per-fiber collision | Blocked until DCC target selection, support-piece atlas/material plan, source/export approval, import approval, and display placement approval |
| String rack | `SM_GIA_BloodAxeShortbowStringRack_A01` | Planned only: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowStringRack_A01/SM_GIA_BloodAxeShortbowStringRack_A01.blend` | Planned only: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowStringRack_A01/SM_GIA_BloodAxeShortbowStringRack_A01.fbx` | Planned only: `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowStringRack_A01` | Ground center for floor rack, or back-plane center for wall variant only if later approved | 220-330 cm stretched string length; sized to shortbow strings, not longbow staves; Giant workshop support scale | 1 target, 2 max for wood/leather plus metal/bone accents | LOD0 1.8k-4.5k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve support frame, stretched string read, and footprint | Grouped boxes or low-count convex hulls for feet, uprights, crossbars, and major shelf/support forms; no per-string collision | Blocked until floor-vs-wall variant decision, DCC target selection, source/export approval, Unreal import approval, collision proxy approval, and no simulation policy are assigned |
| Nock parts | `SM_GIA_BloodAxeShortbowNockParts_A01` | Planned only: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowNockParts_A01/SM_GIA_BloodAxeShortbowNockParts_A01.blend` | Planned only: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowNockParts_A01/SM_GIA_BloodAxeShortbowNockParts_A01.fbx` | Planned only: `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowNockParts_A01` | Grouped display center | 18-38 cm long horn, bone, or iron nock pieces; readable grooves; shortbow-proportioned and Giant-hand repair scale | 1 target | LOD0 800-2.8k tris per grouped display set; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve grouped nock silhouettes and groove read | One grouped box if placed; no per-nock, per-groove, projectile, draw-mechanic, or combat collision | Blocked until grouped display composition approval, DCC target selection, source/export approval, import approval, and no draw/release behavior gate are assigned |
| Grip-wrap bundle | `SM_GIA_BloodAxeShortbowGripWrapBundle_A01` | Planned only: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowGripWrapBundle_A01/SM_GIA_BloodAxeShortbowGripWrapBundle_A01.blend` | Planned only: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowGripWrapBundle_A01/SM_GIA_BloodAxeShortbowGripWrapBundle_A01.fbx` | Planned only: `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowGripWrapBundle_A01` | Bundle center or coil mass center | 20-75 cm roll diameter; 8-16 cm strip width; broad Giant-scale leather/rawhide/red-cloth repair stock | 1 target | LOD0 600-2k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve roll/bundle mass and red cloth identifiers | One grouped box or capsule if world placed; no per-strip, per-stitch, equip, repair interaction, projectile, or combat collision | Blocked until atlas/material reuse plan, DCC target selection, source/export approval, import approval, and static display approval |
| Repair pieces | `SM_GIA_BloodAxeShortbowRepairPieces_A01` | Planned only: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowRepairPieces_A01/SM_GIA_BloodAxeShortbowRepairPieces_A01.blend` | Planned only: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowRepairPieces_A01/SM_GIA_BloodAxeShortbowRepairPieces_A01.fbx` | Planned only: `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeShortbowRepairPieces_A01` | Grouped display center | 28-90 cm splints/support blocks plus patch plates, clamp blocks, wedges, and resin pot; Giant repair-bench scale | 1 target, 2 max if wood/leather separates from metal/resin | LOD0 1.2k-4.5k tris per grouped repair set; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve major splints, patch plates, and grouped mass | One grouped box or capsule; no per-small-piece, per-wedge, per-splint, repair interaction, projectile, or combat collision | Blocked until grouping density review, DCC target selection, source/export approval, Unreal import approval, collision proxy approval, and no crafting/repair gameplay approval |
| Rack support | `SM_GIA_BloodAxeShortbowRackSupport_A01` | Planned only: `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Shortbows/SM_GIA_BloodAxeShortbowRackSupport_A01/SM_GIA_BloodAxeShortbowRackSupport_A01.blend` | Planned only: `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Shortbows/SM_GIA_BloodAxeShortbowRackSupport_A01/SM_GIA_BloodAxeShortbowRackSupport_A01.fbx` | Planned only: `/Game/Aerathea/Props/Giants/BloodAxeArmory/Shortbows/SM_GIA_BloodAxeShortbowRackSupport_A01` | Ground center of rack footprint | 180-285 cm tall; 120-260 cm wide; broad feet, simple crossbars, low cradle options, and Giant camp footprint | 1 target, 2 max for wood/leather plus metal/bone accents | LOD0 3k-7k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve footprint, uprights, crossbars, bow contact silhouette, and red faction blocks | Grouped boxes or low-count convex hulls for feet, uprights, crossbars, and shelves; no dense per-part collision | Blocked until rack layout approval, DCC target selection, source/export approval, Unreal import approval, collision proxy approval, environment placement review, and final visual approval |

## Shared Material and Texture Plan

- Baseline map set for future texture work: Base Color / Albedo (`BC`), Normal (`N`), and packed Occlusion/Roughness/Metallic (`ORM`).
- No baseline emissive map is planned.
- Shared material targets remain planning names only: `MI_GIA_BloodAxeBowWood_A01`, `MI_GIA_BloodAxeBowString_A01`, `MI_GIA_BloodAxeScorchedLeather_A01`, `MI_GIA_BloodAxeBlackenedIron_A01`, `MI_GIA_BloodAxeBoneHorn_A01`, `MI_GIA_BloodAxeRedCloth_A01`, and `MI_GIA_BloodAxeSootResin_A01`.
- Do not create unique material slots per string, nock cap, lashing, splint, stitch, cloth tie, repair patch, or small support part.

## Shared LOD and Collision Rules

- All important child meshes require LOD0, LOD1, LOD2, and LOD3.
- LOD reductions must remove tiny fibers, stitch marks, pitting, scratches, small knots, tiny rivets, small nails, minor wedges, secondary bindings, tiny nock bevels, secondary repair patch bevels, and secondary rack braces before reducing the primary bow arc, grip, nocks, string line, rack footprint, or Giant-scale mass.
- Collision remains simple and display-focused. Equipped bows should have collision disabled by default. World display pieces may use one capsule, one box, grouped boxes, or low-count convex hulls only where later implementation work approves them.
- No projectile collision, damage collision, combat trace collision, inventory pickup collision, or interactive repair collision is defined by this manifest.

## Approval Gates Before Implementation

- Lead approval is required before selecting the first DCC target.
- DCC approval is required before creating Blender source folders, `.blend` files, source meshes, LOD source files, proof renders, or FBX exports.
- Unreal approval is required before creating or importing Static Meshes, materials, textures, Content assets, Blueprints, validators, or startup actors.
- Animation approval is required before bow draw timing, release timing, reload timing, string deformation, carry animation, socket ownership, montage timing, cloth, physics, or equip behavior.
- Gameplay approval is required before projectile behavior, arrow inventory, ammunition counts, combat stats, hit logic, damage values, range values, pickup behavior, loot rules, repair interaction, crafting, economy, or encounter use.
- Visual approval is required before final shape language, damage density, repair density, trophy density, red cloth placement, and Blood Axe/neutral Giant culture separation are locked.
- Source-storage approval is required before any external concept source enters the repository.

## Quality Gate Checklist

- Giant scale lock is explicit and unchanged.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- The manifest covers hunter shortbow, scout compact bow, camp rack bow, repaired spare bow, string coil, string rack, nock parts, grip-wrap bundle, repair pieces, and rack support.
- Planned Blender source paths, planned export paths, and planned Unreal paths are included as plans only.
- No folders, DCC source, FBX exports, Unreal assets, tools, runtime files, startup placements, validators, global indexes, external concepts, or final visual approvals are created or claimed.
- Projectile behavior, projectile collision, combat stats, arrow inventory, draw timing, release timing, reload timing, DCC/FBX/Unreal work, final visual approval, and first DCC target selection are explicitly blocked.
