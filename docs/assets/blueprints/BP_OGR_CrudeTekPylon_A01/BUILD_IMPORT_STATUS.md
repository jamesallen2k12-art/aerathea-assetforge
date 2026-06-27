# BP_OGR_CrudeTekPylon_A01 Build And Import Status

## Current Status

- Build/import status: native-backed pylon state wrapper implemented; Blueprint asset created, compiled, placed in startup, and wired to the Gnome/Ogre encounter coordinator.
- Unreal state: `/Game/Aerathea/Blueprints/Ogres/BP_OGR_CrudeTekPylon_A01`
- Startup actor: `AET_PROD_OGR_CrudeTekPylon_A01`
- Native class: `AAETCrudeTekPylonActor`
- Review scope: first-pass state control for Idle, Charged, Overload, Damaged, and Destroyed pylon phases using the imported `SM_OGR_CrudeTekPylon_A01` mesh.

## Runtime Contract

- Mesh component: `PylonMesh`
- Marker components: `CoreLocator`, `TopArcLocator`, `GroundSparksLocator`
- Niagara component: `PylonNiagara`
- Material parameters: `PylonState`, `OverloadPercent`, `DamagePercent`, `StateColor`
- Niagara parameters: `User.PylonState`, `User.OverloadPercent`, `User.DamagePercent`, `User.bOverloaded`, `User.bDestroyed`, `User.StateColor`, `User.CoreWorldLocation`, `User.TopArcWorldLocation`

## Validation

- `Tools/Unreal/validate_startup_scene.py` validates the Blueprint asset, startup actor class, static mesh binding, runtime visibility, hidden Niagara placeholder component, and encounter coordinator reference.
- Latest validation result: passing with `125` expected assets, `47` expected actor labels, and `25` ground tiles.

## Remaining To Finalize

1. Author final `NS_OGR_CrudeTekPylon_A01` overload/damage/destroyed Niagara emitters.
2. Replace first-pass pylon geometry with final sculpt/retopo, UVs, BC/N/ORM/E texture set, and tuned collision.
3. Add repair, damage, objective, and quest rules after gameplay phase design is approved.
