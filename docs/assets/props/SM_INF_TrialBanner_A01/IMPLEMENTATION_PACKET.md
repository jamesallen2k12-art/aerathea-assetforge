# SM_INF_TrialBanner_A01 Implementation Packet

## Task Scope

- Task: `AET-MA-20260629-044`
- Build scope: docs-only implementation packet.
- Result target: prepare static mesh banner and marker variants for a future DCC and Unreal build lane.
- Not included: Blender source creation, FBX export, Unreal import, runtime interaction behavior, startup scene placement, cloth simulation, skeletal cloth setup, animation authoring, final texture authoring, or final banner symbol redesign.

This packet promotes the production package into an implementation-ready task contract. It does not approve or start asset construction.

## Dependency Evidence

| Dependency | Evidence | Status |
| --- | --- | --- |
| `SM_INF_TrialBanner_A01` package | `docs/assets/props/SM_INF_TrialBanner_A01/PRODUCTION_PACKAGE.md` | Production package ready for static-first implementation planning. |
| `SM_INF_BalgorothSigil_A01` | `docs/assets/props/SM_INF_BalgorothSigil_A01/BUILD_IMPORT_STATUS.md` | First-pass Unreal static mesh import, material assignment, LODs, and sockets validated. Final sculpt, UVs, authored textures, tuned collision, and startup placement remain open. |
| `MI_INF_CultStone_Set_A01` | Referenced by the TrialBanner and BalgorothSigil packages | Approved material language for basalt, scorched red, obsidian, black iron, bone/horn, ash cloth, and restrained emissive channels. |

## Selected Variant Family

- Variant family: `A01` Balgoroth cult trial banner set.
- Primary read: ash-black vertical cloth, blood-dark red trim, one large Balgoroth symbol, heavy top rod or pole support, scorched lower tear shape, and sparse ember stitch accents.
- Gameplay role: faction-readable ritual dressing for trial rooms, altar walls, gate approaches, Lesser dens, witness areas, and den staging.
- Safety/readability rule: read as an Infernal trial marker, not a generic medieval banner, gore trophy, text placard, or all-over glowing cloth sheet.

## Static Mesh Variant Contract

Future DCC lane may build these variants from one shared cloth silhouette family:

| Mesh | Purpose | Approximate scale | Pivot |
| --- | --- | --- | --- |
| `SM_INF_TrialBanner_Wall_A01` | Wall-hung vertical banner for altar walls and gate approaches | 90-140 cm wide x 220-360 cm tall | Top-center hanging point |
| `SM_INF_TrialBanner_Pole_A01` | Freestanding room marker or entry marker | 70-110 cm wide x 260-420 cm tall including pole | Pole base center |
| `SM_INF_TrialBanner_Pennant_A01` | Short altar-side or witness-side pennant | 40-70 cm wide x 90-160 cm tall | Top-center hanging point |
| `SM_INF_TrialBanner_TornMarker_A01` | Narrow torn trial strip for den corners and Lesser staging | 30-60 cm wide x 100-220 cm tall | Center top |

Required shared features:

- Simple static cloth sheet with broad folded planes and large tear shapes.
- Large Balgoroth symbol based on validated horned crown, split wing, claw slash, ember eye, or broken-circle language.
- Heavy blackened iron, smoke-stained bone, or horn rod/pole supports.
- Major rod caps, pole base, banner holes, and broad tears as geometry.
- Cloth weave, soot, ash wear, frayed fibers, tiny stitches, and minor scorch marks reserved for texture and normal maps.

## DCC Build Contract

Future DCC lane may create:

- `Tools/DCC/build_infernal_trial_banner.py`
- `SourceAssets/Blender/Props/Infernals/BalgorothCult/SM_INF_TrialBanner_A01/SM_INF_TrialBanner_A01.blend`
- `SourceAssets/Exports/Props/Infernals/BalgorothCult/SM_INF_TrialBanner_A01/SM_INF_TrialBanner_A01.fbx`
- `Saved/Automation/InfernalTrialBannerReview/SM_INF_TrialBanner_A01_DCCReview.png`

Required DCC checks:

- Centimeter scale, 1 Unreal unit = 1 cm.
- Static mesh geometry only.
- Wall, pole, pennant, and torn-marker variants share a symbol and material language.
- Cloth planes use broad folds that hold silhouette at distance.
- No dense fringe, tiny glyph fields, unreadable script, random micro-spikes, excessive dangling charms, gore, or thousands of small stitches.
- Cloth motion is not authored in this lane.

## Unreal Import Contract

Future Unreal lane may create:

- `Tools/Unreal/import_infernal_trial_banner.py`
- `Tools/Unreal/validate_infernal_trial_banner.py`
- `/Game/Aerathea/Props/Infernals/BalgorothCult/TrialBanner/`

Import requirements:

- Asset type: Static Mesh set.
- Unreal folder: `/Game/Aerathea/Props/Infernals/BalgorothCult/TrialBanner/`
- Scale: centimeters.
- LODs: LOD0-LOD3 required for each placed variant.
- Material slots: 2-4 maximum per variant.
- Collision: none for wall cloth, simple pole/base collision only for freestanding variants.
- Startup scene: out of scope unless a later placement task explicitly assigns it.

## Material Slot Plan

Target material lanes:

1. `MI_INF_CultStone_AshCloth_A01` or future `MI_INF_TrialBanner_A01_AshCloth`
2. `MI_INF_CultStone_BlackIron_A01` or `MI_INF_CultStone_BoneHorn_A01`
3. `MI_INF_TrialBanner_A01_SigilPrint`
4. `MI_INF_TrialBanner_A01_Emissive`

Texture targets for future final art:

- `T_INF_TrialBanner_A01_BC`
- `T_INF_TrialBanner_A01_N`
- `T_INF_TrialBanner_A01_ORM`
- `T_INF_TrialBanner_A01_E`

Material rules:

- Use one large symbol per banner face.
- Keep emissive stitches and symbol pips sparse.
- Violet-red is limited to future rejection state use and must not become a constant aura.
- Do not create a duplicate faction symbol style outside the validated Balgoroth sigil language.

## Socket And Snap Contract

Expected sockets for future mesh variants:

| Socket | Applies to | Purpose |
| --- | --- | --- |
| `snap_wall_hanger` | Wall, pennant, torn marker | Aligns top hanger to wall hooks, rods, or ritual-room dressing points. |
| `snap_pole_base` | Pole | Aligns freestanding pole base to floor or platform markers. |
| `vfx_sigil_ember` | All symbol-bearing variants | Optional future low-intensity ember pulse from the main symbol. |
| `vfx_rejected_thread` | Broken-circle or torn-marker variants | Optional future rejection thread effect, event-based only. |

Socket names are part of the future contract only. No sockets are authored by this packet.

## Triangle And LOD Budget

| Variant | LOD0 target | LOD1 | LOD2 | LOD3 |
| --- | --- | --- | --- | --- |
| Wall banner | 800-2k tris | 55-60 percent | 25-35 percent | 10-15 percent |
| Pole banner | 1.2k-3k tris | 55-60 percent | 25-35 percent | 10-15 percent |
| Pennant | 500-1.2k tris | 50-60 percent | 25-35 percent | 10-15 percent |
| Torn marker | 400-1k tris | 50-60 percent | 25-35 percent | 10-15 percent |

LOD reduction order:

1. Remove tiny stitch, fray, soot, and scorch detail from geometry if any slipped into LOD0.
2. Reduce fold loops and small tear bevels.
3. Simplify rod caps, pole caps, and secondary hanging loops.
4. Flatten minor cloth waves.
5. Preserve the vertical banner block, lower tear silhouette, pole read, and one broad Balgoroth symbol color block.

## Collision Plan

- Wall banner: no collision.
- Pennant: no collision.
- Torn marker: no collision.
- Pole banner: one simple capsule or box for the pole plus optional low box for the base.
- Do not add collision to cloth sheets.
- Collision must not snag player capsules, Infernal wings, tails, large horns, or camera movement.

## Animation And Cloth Notes

- Static mesh by default.
- Cloth simulation, skeletal cloth setup, wind sway, tear animation, material-state animation, and runtime interaction are approval-gated future tasks.
- If a future material pulse is approved, it should be scalar-driven and restrained through `vfx_sigil_ember` or `vfx_rejected_thread`, not an always-on cloth glow.

## Future Validator Plan

Focused validator path for a later build lane:

- `Tools/Unreal/validate_infernal_trial_banner.py`

Validator should check:

- Expected static mesh names exist under `/Game/Aerathea/Props/Infernals/BalgorothCult/TrialBanner/`.
- LOD0-LOD3 are present for each future-authored variant.
- Material slot count stays within 2-4.
- Material references use approved TrialBanner and CultStone lanes.
- Expected sockets exist on variants that consume them.
- Wall, pennant, and torn-marker variants do not use blocking cloth collision.
- Pole collision is simple and restricted to pole/base.
- Startup scene is unchanged unless a placement task explicitly owns it.
- No cloth simulation, skeletal mesh asset, or runtime behavior is introduced by the static mesh lane.

## Stop Conditions

Stop and return to lead/user approval before:

- Creating DCC source, FBX export, Unreal content, import scripts, validator scripts, or startup placement.
- Changing the Balgoroth symbol language beyond the validated sigil direction.
- Authoring cloth simulation, skeletal cloth, wind animation, or dynamic tearing.
- Creating runtime interaction, gameplay state logic, quest logic, or encounter behavior.
- Adding constant full-cloth glow, dense particle attachments, gore, readable text, or copied symbols.
- Editing global indexes or unrelated kit/package docs.

## Acceptance Checklist

- Packet is docs-only and touches no implementation files.
- Static wall, pole, pennant, and torn-marker variants are defined.
- Balgoroth sigil use is locked to validated symbol language.
- Material lanes, texture targets, pivots, sockets, collision, LODs, validator gaps, and approval gates are explicit.
- Cloth motion remains future work.
- The next production step is an approval-gated DCC or Unreal build task.
