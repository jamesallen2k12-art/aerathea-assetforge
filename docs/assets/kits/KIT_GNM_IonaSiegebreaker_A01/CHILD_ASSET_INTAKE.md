# KIT_GNM_IonaSiegebreaker_A01 Child Asset Intake

## Source

- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Iona.png`
- Related source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Gnome Mek fighting Demon.png`
- Added heavy Mek variant references: `GnomeFemaleHeavyMek.png`, `GnomeFemaleHeavyMek0.png`, `GnomeFemaleHeavyMek8.png`, `GnomeFemaleHeavyMek10.png`
- Faction/theme: Gnome/Mekgineer versus Abyss
- Intake status: visual classification complete; child packages proposed; approval pending before DCC build

## Notes

`Iona.png` shows a named gnome hero-pilot in a large combat Mek, with crowds of gnomes behind her and an Abyss demon in front. Treat the image as a named hero/vehicle/encounter kit, not a single character portrait.

`Gnome Mek fighting Demon.png` is a related encounter reference with another heavy Mek fighting a winged demon. It should inform weapon sockets, demon scale, and siege-defense mood, but it should not replace Iona's named hero package.

The four added `GnomeFemaleHeavyMek*` references are not Iona replacements. Use them to broaden the heavy Mek variant matrix and share compatible mechanical language with `KIT_GNM_OGR_RivalryEncounter_A01`.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Status | Notes |
| --- | --- | --- | --- | --- |
| `Iona.png#Pilot_Iona` | Named gnome hero | `SK_GNM_IonaPilot_A01` | Package needed after approval | Compact gnome pilot with goggles, bright hair, expressive face, gloves, harness |
| `Iona.png#Mek_Siegebreaker` | Heavy Mek skeletal mesh | `SK_GNM_IonaSiegebreakerMek_A01` | Package needed after approval | Large dark-iron/brass Mek frame with fists, boots, cockpit/harness, core |
| `Iona.png#Weapon_TwinArcCannons` | Weapon assembly | `SM_GNM_IonaArcCannon_A01` | Package needed after approval | Twin back/shoulder arc cannon assemblies with blue Aetherium muzzle glow |
| `Iona.png#Blueprint_AssembledHero` | Blueprint actor | `BP_GNM_IonaSiegebreaker_A01` | Package needed after pilot/Mek approval | Assembled pilot, Mek, weapon sockets, VFX, and animation state routing |
| `Iona.png#Crowd_GnomeMilitia` | Encounter/NPC crowd reference | `KIT_GNM_CogspireMilitia_A01` | Reference only | Use for later gnome civilian/militia crowd package |
| `Iona.png#Abyss_DemonOpponent` | Encounter reference | `SK_ABY_WingedRavager_A01` or `SK_ABY_CinderLord_A01` | Reference only | Use Abyss hierarchy packages for actual demon production |
| `Iona.png#RuinedCityDefense` | Environment reference | `KIT_AET_SiegeDefenseDressing_A01` | Reference only | Burning city/ruins/dust/smoke mood, not immediate asset scope |
| `Gnome Mek fighting Demon.png#HeavyMekVariant` | Heavy Mek variant | `SK_GNM_SiegeMekVariant_A01` | Package needed later | Alternate heavy Mek silhouette with seated pilot and arm cannons |
| `Gnome Mek fighting Demon.png#WingedDemonOpponent` | Encounter reference | `SK_ABY_WingedRavager_A01` | Reference only | Use as flying Abyss enemy scale and targeting reference |
| `GnomeFemaleHeavyMek*.png#HeavyMekVariantMatrix` | Heavy Mek variant set | `SK_GNM_SiegeMekVariant_A01` or `SK_GNM_HeavyMek_Rivalry_A01` | Package needed later | Additional female pilot/heavy Mek shapes; keep named Iona silhouette distinct |

## Immediate Next Action

If approved later, start with `SK_GNM_IonaSiegebreakerMek_A01` as a hero Mek production package, then split `SK_GNM_IonaPilot_A01` and `SM_GNM_IonaArcCannon_A01`. Do not build a procedural placeholder for this image.
