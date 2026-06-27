# ACIQ-P02_01 Giant Blood Axe Slate

## Source

- Visual inspection date: 2026-06-25
- Source folder: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS`
- Temporary contact sheet reviewed: `/tmp/aerathea_giant_bloodaxe_contact.jpg`; late-added `BloodAxeArmory.png` inspected separately.
- Source count: 48 concepts, split into 26 Giant concepts and 22 Blood Axe Tribe concepts.
- Intake state: source-level visual intake complete; `SK_GIA_Base_A01` scale, visual direction, and first-pass DCC scale/proportion pass are approved after height verification, with approval image, production package, modeling handoff, DCC source, male/female FBX exports, review render, staged Unreal import, generated sockets/physics/ABP placeholders, startup actors, and validation passing. Unreal close-up visual approval is pending. Child expansion is still required for Blood Axe armory, warband, camp, ritual stones, and Giant environment kits before those assets move to DCC or Unreal work.

## Visual Direction Read

Civilized Giants read as remote mountain people with enormous scale, hidden cliff settlements, pale stone masonry, carved halls, bridge networks, hearth-lit interiors, and architecture that disappears into natural rock. Their strongest production direction is a mountain cave-town kit with disguised entrances, terraces, monumental stairs, visitor-scale side paths, workshops, halls, waterworks, and warm interior lighting against cold stone.

Blood Axe Tribe sources must stay separate from general Giant culture. They use red banners, skull and horn markers, rough hide shelters, dark timber, smoky fires, blood ritual spaces, brutal weapons, warbands, and harsher camp silhouettes. These should become a hostile sub-faction kit and warband hierarchy, not the default Giant look.

The images are moodier and more realistic than the final Aerathea target. Production translation should keep the silhouette, scale, stonecraft, red-banner language, and faction split, then simplify into stylized MMO-safe forms with readable mid-poly geometry, hand-painted texture detail, baked AO, limited material slots, and restrained glow.

## Proposed Parent Packages

| Package | Purpose | First dependency |
| --- | --- | --- |
| `SK_GIA_Base_A01` | Giant body/style anchor covering male, female, scale, rig notes, starter clothing, and neutral/civilized material language | Approved scale, concept direction, and first-pass DCC scale/proportion pass; male/female FBXs imported to Unreal and validator-clean; close-up visual approval pending |
| `KIT_GIA_MountainCaveTown_A01` | Civilized hidden mountain cave-town environment kit: gates, terraces, halls, bridge spans, stairs, homes, forge/workshop pieces, visitor paths, and lighting props | Giant scale sheet and settlement direction approval |
| `KIT_GIA_BloodAxeCamp_A01` | Blood Axe nomad/raider camp kit: shelters, forge, gate, banners, bone markers, defensive stakes, camp props, and stronghold approach modules | Blood Axe sub-faction direction approval |
| `KIT_GIA_BloodAxeRitualStones_A01` | Ritual stones and warning markers: standing-stone rings, altars, cairns, guideposts, ritual channels, skull/horn poles, and territory markers | Blood Axe ritual-stone direction approval |
| `KIT_GIA_BloodAxeWarband_A01` | Blood Axe NPC hierarchy: hunting party, army formation, chieftain, leader, shaman, male/female body variants, armor, weapons, and banner carriers | `SK_GIA_Base_A01` body scale and skeleton policy |
| `KIT_GIA_BloodAxeArmory_A01` | Blood Axe armory and bowyer kit: double axes, cleavers, hammers, spears, knives, giant bows, quivers, arrows, bow staves, bowyer tools, trophy armor, and reforged-metal process reference | Giant hand scale, Blood Axe warband hierarchy, and armory child intake |
| `SK_GIA_Yiva_A01` | Named Giant character candidate from `Yiva.png` | Giant base body/style approval and named NPC role approval |

## Source Routing

| Source concept | Category | Route | Status / next action |
| --- | --- | --- | --- |
| `Blood Axe Fist Hunting Party.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Package needed after Giant scale and Blood Axe hierarchy |
| `BloodAxe Village.png` | Building/settlement/environment | `KIT_GIA_BloodAxeCamp_A01` | Package needed; split shelters, banners, ritual markers, camp props |
| `BloodAxeArmory.png` | Armory/weapons/gear | `KIT_GIA_BloodAxeArmory_A01` | Collage-heavy source; split giant weapons, bows, quivers, bowyer tools, armor trophies, and reforged-metal process into child IDs |
| `BloodAxeCamp.png` | Building/settlement/environment | `KIT_GIA_BloodAxeCamp_A01` | Package needed; compare with `BloodAxecamp.png` for duplicate or variant status |
| `BloodAxeChieftan.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Package needed; chieftain and throne-hall dressing must be split |
| `BloodAxeForge.png` | Building/settlement/environment | `KIT_GIA_BloodAxeCamp_A01` | Package needed; forge module and brutal camp-crafting props |
| `BloodAxeGate.png` | Building/settlement/environment | `KIT_GIA_BloodAxeCamp_A01` | Package needed; defensive gate, banner, skull/horn markers |
| `BloodAxeGiantMale.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Variant source after base Giant body approval |
| `BloodAxeGiantMale2.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Variant source after base Giant body approval |
| `BloodAxeLeaderMale.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Package candidate after chieftain/leader hierarchy is approved |
| `BloodAxeRitual.png` | Building/settlement/environment | `KIT_GIA_BloodAxeRitualStones_A01` | Package needed; key source for altars and standing-stone formations |
| `BloodAxeShamanHut.png` | Building/settlement/environment | `KIT_GIA_BloodAxeCamp_A01` | Package needed; split hut shell, ritual poles, fire, banners |
| `BloodAxeShelter.png` | Building/settlement/environment | `KIT_GIA_BloodAxeCamp_A01` | Package needed; nomad shelter module and dressing props |
| `BloodAxeStronghold.png` | Building/settlement/environment | `KIT_GIA_BloodAxeCamp_A01` | Package needed; hostile stronghold approach and vertical camp layout |
| `BloodAxecamp.png` | Building/settlement/environment | `KIT_GIA_BloodAxeCamp_A01` | Compare with `BloodAxeCamp.png`; likely variant rather than duplicate |
| `Bloodaxe Army.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Reference for formation scale, banner read, and troop hierarchy |
| `Giant Fortress Entrance.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Package needed; disguised mountain gate and giant-scale doorway |
| `Giant Settlement.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Package needed; cave interior, bridges, terraces, warm light |
| `Giant Settlement1.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Package needed; cliff-facing settlement facade and monumental stairs |
| `Giant.png` | Character/NPC/class | `SK_GIA_Base_A01` | Body/style source; separate neutral Giant identity from Blood Axe tribe |
| `Giant1.png` | Character/NPC/class | `SK_GIA_Base_A01` | Body/style variant source |
| `Giant2.png` | Character/NPC/class | `SK_GIA_Base_A01` | Body/style and weapon-scale variant source |
| `GiantBloodAxeHuntersMale.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Hunting-party hierarchy source |
| `GiantBloodAxeMale3.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Male Blood Axe variant source |
| `GiantBloodAxeMale4.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Male Blood Axe champion variant source |
| `GiantBloodAxeMaleShaman.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Shaman/cult leader package candidate |
| `GiantBloodAxeMaleandFemale.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Male/female comparison source for Blood Axe outfits and scale |
| `GiantFemale.png` | Character/NPC/class | `SK_GIA_Base_A01` | Female Giant body/style source |
| `GiantFemale1.png` | Character/NPC/class | `SK_GIA_Base_A01` | Female Giant warrior variant source |
| `GiantFemale3.png` | Character/NPC/class | `SK_GIA_Base_A01` | Female Giant battlefield variant source |
| `GiantFemale4.png` | Character/NPC/class | `SK_GIA_Base_A01` | Female Giant hunter/warrior variant source |
| `GiantFemale5.png` | Character/NPC/class | `SK_GIA_Base_A01` | Female Giant body/outfit variant source |
| `GiantFemaleBloodAxe1.png` | Character/NPC/class | `KIT_GIA_BloodAxeWarband_A01` | Female Blood Axe variant source |
| `GiantFemaleShaman.png` | Character/NPC/class | `SK_GIA_Base_A01` | Neutral/civilized shaman variant unless later assigned to Blood Axe |
| `GiantMale1.png` | Character/NPC/class | `SK_GIA_Base_A01` | Male Giant body/style source |
| `GiantMale2.png` | Character/NPC/class | `SK_GIA_Base_A01` | Male Giant hammer/weapon-scale variant |
| `GiantMale3.png` | Character/NPC/class | `SK_GIA_Base_A01` | Male Giant magic/hero variant; keep glow restrained |
| `GiantMale4.png` | Character/NPC/class | `SK_GIA_Base_A01` | Male Giant heavy hammer and stoneworker silhouette source |
| `GiantMaleandFemale.png` | Character/NPC/class | `SK_GIA_Base_A01` | Male/female proportion and scale comparison source |
| `GiantMaleandFemale3.png` | Character/NPC/class | `SK_GIA_Base_A01` | Male/female combat-scale comparison source |
| `GiantSettlement3.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Cave hall/bridge module source |
| `GiantSettlement4.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Snow cliff hidden settlement and exterior camouflage source |
| `GiantSettlement5.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Giant workshop/forge and inhabited cave module source |
| `GiantSettlement6.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Mountain gate and defensive facade source |
| `GiantSettlement7.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Terraced hidden-city layout source |
| `GiantSettlement8.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Interior hall, stairs, and visitor route source |
| `GiantSettlement9.png` | Building/settlement/environment | `KIT_GIA_MountainCaveTown_A01` | Deep cave district and bridge lighting source |
| `Yiva.png` | Character/NPC/class | `SK_GIA_Yiva_A01` | Named Giant character candidate; package only after named role approval |

## Production Constraints

- Giant scale must be established before armor, weapons, interiors, doors, stair heights, beds, tables, and player traversal paths are authored.
- Civilized Giant stonework and Blood Axe ritual/camp work must be separate material and module sets.
- Blood Axe brutality should read through props, banners, silhouettes, and ritual markers, not excessive gore or unbuildable detail.
- Use real geometry for giant-scale doors, stairs, bridge spans, pillars, major weapons, shields, banners, standing stones, altars, and large horn/skull markers.
- Use textures and normals for fine cracks, scratches, fur texture, stitching, small symbols, dirt, smoke staining, and rough chisel marks.
- Environment kit targets should stay modular with LOD0-LOD3, simplified collision, 2-5 material slots depending on kit size, and impostors for distant cliff-city reads.
- `BloodAxeArmory.png` includes readable text and gore-heavy trophy treatment; production packages should translate the useful silhouettes and material story into readable, non-text-dependent, MMO-safe assets.

## Next Action

1. Review the staged `SK_GIA_Base_A01` Unreal close-up capture and either approve it as the Giant hand/body scale lock or request scale/proportion changes.
2. Approve whether `KIT_GIA_MountainCaveTown_A01` or `KIT_GIA_BloodAxeRitualStones_A01` should be the first environment production package.
3. Split `KIT_GIA_BloodAxeArmory_A01` into weapon, bow, armor, trophy, tool, quiver, arrow, and process-reference child IDs before individual Blood Axe gear packages.
4. Split `KIT_GIA_BloodAxeWarband_A01` into chieftain, shaman, hunter, troop, and male/female body variant children only after the base Giant body scale is fixed.
