# BP_OGR_CrudeTekPylon_A01 Build And Import Status

## Current Status

- Build/import status: native-backed pylon state wrapper implemented; Blueprint asset created, compiled, placed in startup, and wired to the Gnome/Ogre encounter coordinator.
- Unreal state: `/Game/Aerathea/Blueprints/Ogres/BP_OGR_CrudeTekPylon_A01`
- Startup actor: `AET_PROD_OGR_CrudeTekPylon_A01`
- Native class: `AAETCrudeTekPylonActor`
- Review scope: first-pass state control for Idle, Charged, Overload, Damaged, and Destroyed pylon phases using the imported `SM_OGR_CrudeTekPylon_A01` mesh and assigned `NS_OGR_CrudeTekPylon_A01` Niagara target.

## Runtime Contract

- Mesh component: `PylonMesh`
- Marker components: `CoreLocator`, `TopArcLocator`, `GroundSparksLocator`
- Niagara component: `PylonNiagara`
- Niagara system: `/Game/Aerathea/VFX/Ogres/NS_OGR_CrudeTekPylon_A01`
- Emitter target: `/Game/Aerathea/VFX/Ogres/NE_OGR_CrudeTekPylon_Overload_A01`
- Material parameters: `PylonState`, `OverloadPercent`, `DamagePercent`, `StateColor`
- Niagara parameters: `User.PylonState`, `User.OverloadPercent`, `User.DamagePercent`, `User.bOverloaded`, `User.bDestroyed`, `User.StateColor`, `User.CoreWorldLocation`, `User.TopArcWorldLocation`

## Validation

- `Tools/Unreal/validate_startup_scene.py` validates the Blueprint asset, startup actor class, static mesh binding, Niagara system assignment, runtime visibility, optional Niagara component visibility, and encounter coordinator reference.
- Latest validation result: passing with `127` expected assets, `47` expected actor labels, and `25` ground tiles.

## Remaining To Finalize

1. Polish final `NS_OGR_CrudeTekPylon_A01` overload/damage/destroyed Niagara graph from the template-derived review target.
2. Replace first-pass pylon geometry with final sculpt/retopo, UVs, BC/N/ORM/E texture set, and tuned collision.
3. Add repair, damage, objective, and quest rules after gameplay phase design is approved.
