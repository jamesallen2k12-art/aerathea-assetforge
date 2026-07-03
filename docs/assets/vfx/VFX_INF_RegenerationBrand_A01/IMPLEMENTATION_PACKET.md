# VFX_INF_RegenerationBrand_A01 Pre-Implementation Packet

## Task Scope

- Task: `AET-MA-20260629-045`
- Build scope: docs-only pre-implementation packet.
- Result target: define the future Niagara/VFX contract for restrained Infernal brand regeneration using the expected `SM_INF_BrandingStone_A01` socket contract.
- Not included: Niagara graph authoring, emitter creation, helper material authoring, helper mesh creation, texture authoring, Unreal content import, runtime regeneration logic, gameplay healing values, animation binding, startup scene placement, or final visual approval.

This packet prepares the effect for a later VFX build lane. It does not approve or start Niagara implementation.

## Dependency Evidence

| Dependency | Evidence | Status |
| --- | --- | --- |
| `VFX_INF_RegenerationBrand_A01` package | `docs/assets/vfx/VFX_INF_RegenerationBrand_A01/PRODUCTION_PACKAGE.md` | Production package ready for pre-implementation planning. |
| `SM_INF_BrandingStone_A01` socket contract | `docs/assets/props/SM_INF_BrandingStone_A01/IMPLEMENTATION_PACKET.md` | Expected only. BrandingStone DCC, Unreal mesh, sockets, and validator evidence are pending. |
| `MI_INF_BrandGlowStates_A01` | `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md` and `BUILD_IMPORT_STATUS.md` | First-pass material-state assets are reported complete and focused validation passed. RegenerationBrand must reuse this state language without redefining it. |

## Visual Role

- Primary read: ember-red scar lines waking up, a short red-orange transfer arc from BrandingStone to body brand, a restrained pulse, and low-density ash motes.
- Gameplay role: future visual response for brand initiation, regeneration, worthiness aftermath, Lesser lifecycle rites, and Balgoroth ritual staging.
- Readability rule: frame the brand and body plane without hiding horns, hands, wings, tails, weapon silhouettes, or the target body mass.
- Palette rule: ember red and orange only for accepted/regeneration states; violet-red only for brief rejection or curse contamination.

## State List

Future Niagara or material-driven states:

| State | Purpose | Visual behavior |
| --- | --- | --- |
| `Inactive` | No active ritual event | No particles; body brand material remains inactive or very low scar color. |
| `Smolder` | Idle preparation | Low ember at stone core or target brand, no room-filling bloom. |
| `BrandPrepare` | Stone wakes before contact | Short core pulse at `vfx_brand_core`; sparse ash lift. |
| `BrandContact` | Target mark responds | Body brand mask brightens through BrandGlow state parameters. |
| `TransferStart` | Stone transfers energy to target | Short red-orange arc from `vfx_brand_transfer` to target brand location. |
| `RegenerationPulse` | Regrowth or brand consolidation | One expanding pulse around the body mark, then narrowing back to the scar. |
| `AcceptedConsolidate` | Successful outcome | Warm ember settles into accepted brand lines, then fades to smolder. |
| `RejectedSnap` | Failed or corrupted outcome | Brief violet-red snap from `vfx_rejected_snap`; event-based only. |
| `Cooldown` | Return to idle | Ash motes fade, emissive intensity returns to low or inactive. |

## Expected BrandingStone Socket Mapping

All BrandingStone socket consumption is expected and pending until a future `SM_INF_BrandingStone_A01` build validates sockets in Unreal.

| Expected socket | Consumer | Pending use |
| --- | --- | --- |
| `vfx_brand_core` | `BrandPrepare`, `Smolder`, `Cooldown` | Prop-side core pulse origin in the brand groove. |
| `vfx_brand_transfer` | `TransferStart`, `RegenerationPulse` | Prop-side origin for transfer arc toward body brand target. |
| `vfx_rejected_snap` | `RejectedSnap` | Brief violet-red rejection burst origin. |
| `interact_brand_side` | Future gameplay or presentation code | Not consumed by this VFX packet; listed as adjacent expected dependency. |
| `snap_floor_center` | Future placement tooling | Not consumed by this VFX packet. |

No BrandingStone socket has been validated for RegenerationBrand use in this task.

## Target Attachment Mapping

Future runtime or animation systems should supply target positions instead of hardcoding body locations in Niagara:

- Forearm brand: compact body mark, primary transfer target for initiation.
- Chest or sternum brand: stronger accepted/regeneration pulse target.
- Shoulder or wing-root brand: optional adult/Greater variant, must not clip wing silhouettes.
- Tail-base or spine brand: optional boss or Exalted variant, density must remain capped.

The VFX system should not define gameplay healing authority, body-part eligibility, or regeneration values.

## User Parameter Contract

Required future `User.*` parameters:

| Parameter | Type intent | Use |
| --- | --- | --- |
| `User.State` | Enum or integer state | Selects inactive, smolder, transfer, pulse, accepted, rejected, or cooldown behavior. |
| `User.SourceWorldLocation` | Vector | Generic source fallback when no BrandingStone socket binding exists. |
| `User.TargetWorldLocation` | Vector | Target body brand or presentation point. |
| `User.BrandCoreWorldLocation` | Vector | World-space value from expected `vfx_brand_core`. |
| `User.BrandTransferWorldLocation` | Vector | World-space value from expected `vfx_brand_transfer`. |
| `User.RejectedSnapWorldLocation` | Vector | World-space value from expected `vfx_rejected_snap`. |
| `User.BodyBandScale` | Float | Scales pulse radius across Lesser, compact adult, standard adult, Greater, and Exalted targets. |
| `User.EmissiveIntensity` | Float | Drives restrained material/VFX brightness. |
| `User.PulseDuration` | Float | Controls one-shot pulse timing. |
| `User.ArcDensity` | Float | Caps transfer arc particle or ribbon density. |
| `User.AshDensity` | Float | Caps ash motes and cooldown residue. |
| `User.VioletMix` | Float | Adds brief rejection contamination only. |
| `User.AcceptedFocus` | Float | Tightens accepted-state glow around the final brand. |
| `User.RejectedSnap` | Float or bool | Triggers brief snap event without persistent aura. |

Parameter ranges must be validated in the future VFX lane before visual signoff.

## Material Dependencies

Primary material-state dependency:

- `/Game/Aerathea/Materials/Infernals/M_INF_BrandGlow_Master_A01`
- `/Game/Aerathea/Materials/Infernals/MF_INF_BrandGlowStates_A01`
- `MI_INF_BrandGlowStates_A01_Inactive`
- `MI_INF_BrandGlowStates_A01_Smolder`
- `MI_INF_BrandGlowStates_A01_TrialActive`
- `MI_INF_BrandGlowStates_A01_Accepted`
- `MI_INF_BrandGlowStates_A01_Rejected`
- `MI_INF_BrandGlowStates_A01_SorcererFocus`

Future RegenerationBrand helper targets, not authored by this packet:

- `M_INF_RegenerationBrand_Arc_A01`
- `M_INF_RegenerationBrand_Pulse_A01`
- `M_INF_RegenerationBrand_Ash_A01`
- `MI_INF_RegenerationBrand_Arc_A01`
- `MI_INF_RegenerationBrand_Pulse_A01`
- `MI_INF_RegenerationBrand_Ash_A01`

Material rules:

- Reuse BrandGlow state color language.
- Keep accepted/regeneration glow warm ember, not holy white or blue Aetherium.
- Keep violet-red short and event-based.
- Avoid constant full-body fire, dense sparks, smoke walls, or bloom-heavy idle states.

## Future Niagara Targets

Future systems:

- `NS_INF_RegenerationBrand_Inactive_A01`
- `NS_INF_RegenerationBrand_Smolder_A01`
- `NS_INF_RegenerationBrand_Transfer_A01`
- `NS_INF_RegenerationBrand_Pulse_A01`
- `NS_INF_RegenerationBrand_Accepted_A01`
- `NS_INF_RegenerationBrand_Rejected_A01`
- `NS_INF_RegenerationBrand_Cooldown_A01`

Future emitters:

- `NE_INF_RegenerationBrand_Arc_A01`
- `NE_INF_RegenerationBrand_Pulse_A01`
- `NE_INF_RegenerationBrand_Ash_A01`
- `NE_INF_RegenerationBrand_Snap_A01`

These are target names only. No Niagara assets are authored by this packet.

## Bounds And LOD Density Limits

Fixed bounds guidance for future implementation:

- Prop-attached bounds: cover expected `vfx_brand_core`, `vfx_brand_transfer`, `vfx_rejected_snap`, and the hand/forearm presentation groove without covering the full room.
- Character-attached bounds: scale from Lesser 70-90 cm targets through 274 cm Greater/Exalted targets without clipping active body-brand masks.
- Transfer arc length: 30-180 cm by default.
- Brand pulse radius: 20-45 cm by default.
- Boss or Exalted pulse radius: up to 1.25-1.5 scale only if density stays capped.

LOD density plan:

- VFX LOD0: transfer arc, brand pulse, restrained ash, short edge sparks, material-mask pulse.
- VFX LOD1: reduce ash and sparks by at least 50 percent; keep transfer arc and brand pulse.
- VFX LOD2: remove sparks and most ash; preserve brand color block and one arc or pulse.
- VFX LOD3: disable particles; keep only material-mask glow if gameplay readability requires it.

Particle density should reduce before primary brand readability is removed.

## Helper Mesh And Texture Limits

Future helper budgets:

- Arc ribbon helper: under 150 tris.
- Brand pulse helper: under 100 tris.
- Ash mote card: under 20 tris.
- Total helper mesh budget per system: under 500 tris.

Future texture targets:

- `T_INF_RegenerationBrand_Arc_A01_E`
- `T_INF_RegenerationBrand_Pulse_A01_E`
- `T_INF_RegenerationBrand_Ash_A01_BC`
- `T_INF_RegenerationBrand_Mask_A01_E`

No helper meshes, textures, or materials are created by this packet.

## Future Validator Plan

Focused validator path for a later VFX build lane:

- `Tools/Unreal/validate_infernal_regeneration_brand_vfx.py`

Validator should check:

- Expected Niagara systems and emitters exist only after an approved VFX build task.
- `User.*` parameters exist and expose sane ranges.
- BrandingStone socket bindings are present only after `SM_INF_BrandingStone_A01` has validated Unreal sockets.
- Fixed bounds are compact enough for ritual-room placement and large enough for target masks.
- LODs reduce ash, sparks, and density before removing core brand readability.
- Material references use BrandGlow state language and approved RegenerationBrand helpers.
- Violet use is restricted to `RejectedSnap` or curse contamination.
- Startup scene is unchanged unless a placement task explicitly owns it.
- No gameplay healing values, runtime authority, or animation timing is introduced by the VFX lane.

## Approval Gates And Stop Conditions

Stop and return to lead/user approval before:

- Authoring Niagara systems, emitters, modules, helper materials, helper textures, or helper meshes.
- Binding to runtime regeneration, healing, damage, quest, backend, or gameplay ability logic.
- Binding animation notifies or final timing curves.
- Claiming BrandingStone socket consumption as validated before a future BrandingStone validator proves the sockets exist.
- Adding constant bloom, full-body flame shells, dense sparks, smoke walls, holy-white healing language, blue Aetherium, or Ogre green-black necromancy.
- Editing startup maps, Unreal content, source assets, tools, global indexes, or unrelated package docs.

## Acceptance Checklist

- Packet is docs-only and touches no implementation files.
- State list, expected socket mapping, target attachment mapping, `User.*` parameters, material dependencies, bounds, LOD density limits, future validator plan, and stop conditions are explicit.
- BrandingStone socket consumption is marked expected/pending, not validated.
- BrandGlow material-state language is reused without redefining it.
- No Niagara graph art, helper materials, runtime regeneration values, animation binding, or final visual approval is claimed.
- The next production step is an approval-gated BrandingStone validation or VFX build task.
