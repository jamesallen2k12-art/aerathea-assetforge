# KIT_INF_BalgorothCult_A01 Remaining Child Package Intake

## Scope

- Task: `AET-MA-20260628-006`
- Scope type: docs-only child package intake
- Write scope: `docs/assets/kits/KIT_INF_BalgorothCult_A01/`
- Source image policy: source concepts remain read-only; this intake classifies routing and approval needs only.

This intake starts the remaining Balgoroth cult child package lane after the first-pass floor, arch, altar, BrandGlow, WorthinessJudgment, and ritual altar Blueprint work. It does not approve new DCC, Unreal, source asset, Content, Tool, or global index changes.

## Sources Read

- `AGENTS.md`
- `docs/assets/kits/KIT_INF_BalgorothCult_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_INF_BalgorothCult_A01/VISUAL_KIT_BREAKDOWN.md`
- `docs/assets/ASSET_CONCEPTS_MANIFEST.md`, Infernal and Gnome/Ogre intake delta section
- `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`
- `docs/assets/characters/SK_INF_Lesser_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_INF_CullingTrialFloor_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_INF_HornWingArch_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_INF_WorthinessAltar_A01/PRODUCTION_PACKAGE.md`

## Current Coverage

The existing kit now has enough validated first-pass coverage for ritual layout, threshold scale, altar state sockets, shared brand states, and WorthinessJudgment VFX contracts. Remaining work should avoid duplicating those packages.

| Child | Classification | Current routing |
| --- | --- | --- |
| `SM_INF_CullingTrialFloor_A01` | Covered | Production package, DCC/Unreal first pass, sockets, material channels, and startup placement exist. Final art and expanded floor-state behavior remain later work, not a new package. |
| `SM_INF_HornWingArch_A01` | Covered | Approved first cult prop after the floor. Production package, DCC/Unreal first pass, collision, sockets, LODs, and startup placement exist. Final VFX/BP behavior is later work. |
| `SM_INF_WorthinessAltar_A01` | Covered | Production package, DCC/Unreal first pass, sockets, collision, startup placement, and `BP_INF_RitualAltar_A01` binding exist. Final art and tuned collision remain later work. |
| `MI_INF_BrandGlowStates_A01` | Covered | Shared material-state package and first-pass Unreal assets exist. Final masks, shader polish, and gameplay/animation binding remain later work. |
| `VFX_INF_WorthinessJudgment_A01` | Covered | Production package, first-pass material/Niagara assets, altar assignment, timing/trace validation, and scalar polish contract exist. Bespoke Niagara graph polish remains later work. |
| `BP_INF_RitualAltar_A01` | Covered | Native-backed first-pass ritual altar state wrapper exists. Quest, audio, UI, and combat binding remain later work outside this intake. |
| `SK_INF_Lesser_A01` | Covered external dependency | Lifecycle stages, scale bands, first-pass DCC/Unreal review, and source routing exist. Child/clutch images should inform cult den scale and staging, not create duplicate character packages here. |
| `SK_INF_Base_A01`, starter classes | Covered external dependencies | Adult body and Mage, Warrior, Rogue, Hunter class lanes cover adult character imagery. Cult props should consume their scale, socket, and material needs. |

## Remaining Package Priority

| Priority | Child package | Classification | Why next |
| ---: | --- | --- | --- |
| 1 | `MI_INF_CultStone_Set_A01` | Production package ready | Highest leverage final-art dependency for floor, arch, altar, sigils, basins, chains, banners, and den dressing. Locks basalt, scorched stone, obsidian, ash wear, and emissive channel material rules before more prop packages multiply variants. |
| 2 | `SM_INF_BalgorothSigil_A01` | Production package ready | Locks the horned crown, split wing, hooked tail crescent, claw slash, ember eye, and broken-circle symbols as reusable mesh/decal/relief standards before banner, branding stone, gate, and floor variants diverge. |
| 3 | `SM_INF_BrandingStone_A01` | Production package ready | Connects Lesser lifecycle, adult brand states, WorthinessJudgment, and regeneration hooks through one readable body-brand source prop. Defines `vfx_brand_core`, `vfx_brand_transfer`, presentation groove, and safe interaction side before regeneration VFX package work. |
| 4 | `VFX_INF_RegenerationBrand_A01` | Production package ready | Reuses BrandGlow and AbyssalSpellcasting language for restrained healing/regrowth feedback. Consumes the BrandingStone socket/material-mask contract without becoming generic fire or full-body bloom. |
| 5 | `SM_INF_AshBasin_A01` | Production package ready | Adds low-cost cult dressing and smoke/ember VFX hooks for trial rooms, den interiors, altar sides, and regeneration staging; no VFX or Unreal implementation authored yet. |
| 6 | `SM_INF_WitnessChains_A01` | Production package ready | Adds non-blocking witness/restraint dressing for worthiness scenes and cult dens. Chain density, collision, and physics limits are documented; no DCC/Unreal implementation authored yet. |
| 7 | `SM_INF_TrialBanner_A01` | Production package ready | Adds faction-readable vertical dressing after symbol and material rules are locked. Static-first banner variants are defined; cloth animation remains approval-gated future work. |
| 8 | `KIT_INF_LesserTrialDen_A01` | Package needed after approval | Proposed environment mini-kit for Spawn-scale props, clutch sightlines, low ledges, witness positions, and culling trial staging. Requires user approval because it expands beyond the current child list. |
| 9 | `BP_INF_CultGate_A01` | Package needed after approval | `Infernals Guarding a Gate2.png` can support locked/active/passive gate behavior, but the visual gate is already covered by `SM_INF_HornWingArch_A01`. Needs explicit behavior approval before package work. |

## Child Asset Classification

| Child asset or route | Type | Classification | Notes |
| --- | --- | --- | --- |
| `MI_INF_CultStone_Set_A01` | Material set | Production package ready | Reusable material instances, texture targets, roughness/metallic economy, emissive channel limits, and LOD/material fallback rules are now defined. |
| `SM_INF_BalgorothSigil_A01` | Static mesh/decal kit | Production package ready | Large wall relief, floor insert, altar inset, banner print/reference variants, sockets, LODs, and material rules are now defined without readable text dependency. |
| `SM_INF_BrandingStone_A01` | Static mesh/VFX anchor | Production package ready | Defines `vfx_brand_core`, `vfx_brand_transfer`, hand/forearm presentation groove, `interact_brand_side`, material states, collision, and Unreal import naming without starting DCC or Unreal work. |
| `VFX_INF_RegenerationBrand_A01` | VFX | Production package ready | Socket and material-mask driven; uses ember red/orange with very restrained violet only for curse/rejection moments; no Niagara assets authored yet. |
| `SM_INF_AshBasin_A01` | Static mesh/VFX hook | Production package ready | Small/large/wall variants share one package. VFX sockets are documented for restrained smoke, ember motes, and ash lift only; no implementation authored yet. |
| `SM_INF_WitnessChains_A01` | Static mesh | Production package ready | Mostly non-blocking dressing. Wall, floor, hanging, broken-chain, and anchor-plate variants are defined in one package; no implementation authored yet. |
| `SM_INF_TrialBanner_A01` | Static mesh or skeletal optional | Production package ready | Static wall, pole, pennant, and torn-marker variants are defined. Skeletal/cloth variants remain future approval-gated work. |
| `SM_INF_CullingTrialFloor_A01` | Static mesh modular floor | Covered | Do not create a duplicate floor package. Track final art and expanded behavior in the existing package lane. |
| `SM_INF_HornWingArch_A01` | Static mesh threshold | Covered | Do not create a duplicate gate visual package. Gate behavior can become `BP_INF_CultGate_A01` if approved. |
| `SM_INF_WorthinessAltar_A01` | Static mesh altar | Covered | Do not create `SM_INF_BalgorothAltar_A01` as a duplicate unless a distinct non-worthiness altar role is approved. |
| `MI_INF_BrandGlowStates_A01` | Material state set | Covered | Material-state package already handles body brands and ritual states; future work is mask/shader polish and binding. |
| `VFX_INF_WorthinessJudgment_A01` | VFX | Covered | Bespoke graph polish continues in the existing VFX package; no new ritual judgment VFX package needed. |
| `BP_INF_RitualAltar_A01` | Blueprint Actor | Covered | Future quest/audio/UI/combat binding belongs to the Blueprint lane, not this kit intake. |
| `BP_INF_CultGate_A01` | Blueprint Actor | Package needed after approval | Use only for behavior states on the existing arch: inactive, guarded, locked, trial-open, rejected snap. |
| `KIT_INF_LesserTrialDen_A01` | Environment mini-kit | Package needed after approval | Proposed to collect Spawn-scale den props and clutch staging from child references without duplicating `SK_INF_Lesser_A01`. |

## Manifest Source Routing

| Source group | Classification | Routing |
| --- | --- | --- |
| `InfernalFemale*.png`, `Infernalfemale3.png`, `InfernalMale*.png` | Reference only | Adult body and sex-variant references are covered by `SK_INF_Base_A01` and starter class packages. For this kit, use them only for scale, posture, material, and silhouette checks. |
| `Infernals.png` | Reference only | Group hierarchy and population density source. It informs staging, not a standalone cult child package. |
| `InfernalFemaleLit*.png`, `InfernalMaleLit.png`, `InfernalMaleSorcererLit.png` | Reference only | Lit-brand references are covered by `MI_INF_BrandGlowStates_A01`, `VFX_INF_AbyssalSpellcasting_A01`, and class packages. Use for material masks and glow constraints. |
| `InfernalMaleSorcerer2.png`, `InfernalMaleSorcerer3.png` | Variant | Sorcerer action and power-pose variants route to Mage, AbyssalSpellcasting, BrandGlow, and animation overlay work. Preserve skulls, flame, lightning, anger, and hands; remove rivet/speckle noise before package use. |
| `Infernals Guarding a Gate.png` | Covered | Visual threshold and guard spacing are covered by `SM_INF_HornWingArch_A01`. |
| `Infernals Guarding a Gate2.png` | Covered plus package needed after approval | Visual threshold is covered by `SM_INF_HornWingArch_A01`; future behavior may become `BP_INF_CultGate_A01` only after approval. |
| `InfernalClutch.png`, `Infernal Children.png`, `InfernalGirls5.png` | Reference only | Character lifecycle is covered by `SK_INF_Lesser_A01`. These inform scale, staging, low sightlines, and the proposed `KIT_INF_LesserTrialDen_A01`, not separate character packages. |
| `INfernalBoy*.png`, `InfernalGirl*.png`, `LesserInfernalFemale.png`, `LesserInfernalMale.png` | Variant | Route to `SK_INF_Lesser_A01` Spawn, 1st Kill, Blooded, Elder bridge, and sex-variant matrices. Use as child-stage variants, not new cult prop packages. |
| `Lesser Infernal15.png`, `LesserInfernal*.png` except `LesserInfernal20.png` | Variant | Route to `SK_INF_Lesser_A01`, action/animation references, and cult den encounter staging. `LesserInfernal24.png` remains the clean action anchor. |
| `LesserInfernal20.png` | Reference only | Brightness target for preventing over-dark Infernal renders; do not convert into a standalone package. |

## Visual Cleanse Constraints

Apply these constraints to every remaining child package before DCC or Unreal work:

- Use the Infernal clean anchors first: `InfernalMaleLit.png`, `InfernalFemaleLit2.png`, `InfernalMaleSorcererLit.png`, and `LesserInfernal24.png`.
- For darker sources, start from a roughly 30 percent brighter pass before cleanup, then keep the brightness only if it improves skin, armor, wing, tail, and prop readability.
- Default to A03-style cleanup: remove artifact speckles, tiny repeated rivets, malformed micro-spikes, broken micro-chains, torn-strip clutter, and photoreal surface garbage while preserving glow, skulls, flame, lightning, anger, and menace.
- Use A04-style cleanup only if A03 still leaves the source unreadable.
- Preserve large readable forms: horned crowns, split wings, hooked tail crescents, claw slashes, ember eyes, large skull/bone motifs, stone masses, chains, basins, banners, brands, horns, wings, tails, claws, and hand poses.
- Reduce dense particle fields, glow fuzz, oversized spell circles, and background clutter when they hide anatomy, symbols, sockets, or silhouettes.
- Model major forms as geometry. Push tiny cracks, ash smears, scratches, membrane veins, minor brand lines, small rivets, and chain wear into Base Color, Normal, AO, ORM, and Emissive maps.
- Keep glow sparing and state-driven: eyes, brands, altar cores, ritual channels, rejection snaps, regeneration pulses, and sorcerer focus only.
- Do not use gore, readable text glyphs, watermarks, copied franchise symbols, universal portal styling, or mortal weapons as the primary Infernal read.

## Approval Gates

| Gate | Requirement |
| --- | --- |
| Package selection | User approves the next package from the priority table before DCC or Unreal work starts. |
| Source routing | Lead confirms primary anchors, secondary references, rejected traits, and package boundaries. |
| Production package | Package follows the Aerathea universal format: art direction, gameplay purpose, silhouette, scale, materials, prompt, modeling notes, texture/material notes, triangle budget, LOD, collision, animation, Unreal import, naming, and quality gate. |
| Visual cleanse | Package includes A03/A04 cleanup language, 30 percent brightness rule for dark sources, and micro-detail reduction rules. |
| DCC handoff | DCC starts only after package approval and must preserve silhouette, scale, material slots, LOD0-LOD3, collision, sockets, and Unreal naming. |
| Unreal handoff | Unreal work starts only after DCC proof or material/VFX package approval. Startup or focused validators must be named before review. |
| Visual review | Any Unreal visual approval must compare source or DCC proof orientation, camera pitch/yaw, framing, and scale before presentation. |

## Immediate Next Task Recommendation

Next, run QA over the package-ready Balgoroth cult child assets and the new implementation readiness matrix. `MI_INF_CultStone_Set_A01`, `SM_INF_BalgorothSigil_A01`, `SM_INF_BrandingStone_A01`, `VFX_INF_RegenerationBrand_A01`, `SM_INF_AshBasin_A01`, `SM_INF_WitnessChains_A01`, and `SM_INF_TrialBanner_A01` are now package-ready, which reduces visual drift for later gate, den, and implementation tasks.

## Checks For This Intake

- Docs-only scope respected.
- No source concepts copied, edited, renamed, or moved.
- No global indexes edited.
- Covered work is not duplicated as new packages.
- Remaining children are classified as package needed, covered, variant, or reference-only routing.
- Approval gates are explicit before any DCC, Unreal, Tools, Content, Source, SourceAssets, or global index work.
