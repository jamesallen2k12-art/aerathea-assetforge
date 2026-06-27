# Shared Quest Scripting Lua Schema

## Purpose

Define a shared quest content contract that can serve both the Aerathea MMORPG and ARPG while keeping game-specific execution separate. Lua should be used for constrained quest behavior and content hooks, not for core UI framework ownership or trusted client authority.

## Core Rule

- Shared quest packages are data-first.
- Lua hooks are optional, sandboxed, and versioned.
- Unreal owns presentation, replication, save/load integration, combat authority, and UI widgets.
- MMORPG servers must not trust client-side Lua.
- ARPG local builds may run Lua locally, but the same quest package should preserve server-authoritative semantics where possible.

## Folder Pattern

- Shared quest package: `Content/Aerathea/Quests/<Region>/<QuestId>/`
- Source data mirror: `SourceAssets/Quests/<Region>/<QuestId>/`
- Design docs: `docs/systems/quests/<QuestId>.md`
- Lua script: `Content/Aerathea/Quests/<Region>/<QuestId>/QST_<QuestId>.lua`
- Data asset: `/Game/Aerathea/Quests/<Region>/<QuestId>/DA_QST_<QuestId>`

## Quest Package Fields

| Field | Type | Notes |
| --- | --- | --- |
| `quest_id` | string | Stable ID, for example `QST_GNM_OGR_ShieldwallTrial_A01` |
| `title` | localized text key | No hardcoded UI copy in Lua |
| `region` | tag | World region or encounter kit |
| `faction_context` | tag list | Optional race/faction relation hooks |
| `recommended_level` | int/range | Adapter decides exact scaling |
| `prerequisites` | quest/tag list | Shared dependency contract |
| `objectives` | structured array | Kill, collect, interact, escort, defend, discover, craft, talk |
| `stages` | structured array | Stage state machine, not arbitrary script-only state |
| `rewards` | structured array | XP/currency/item/reputation choices |
| `lua_module` | asset path | Optional constrained script |
| `mmorpg_adapter` | asset path/tag | Server-authoritative adapter |
| `arpg_adapter` | asset path/tag | Local/session adapter |

## Allowed Lua Hooks

```lua
function OnQuestAccepted(ctx) end
function OnObjectiveProgress(ctx, objective_id, amount) end
function OnInteract(ctx, actor_tag) end
function OnEnemyDefeated(ctx, enemy_tag) end
function OnItemAcquired(ctx, item_tag, amount) end
function OnStageEntered(ctx, stage_id) end
function CanComplete(ctx) return true end
function OnQuestCompleted(ctx) end
```

## Lua Context Contract

Lua receives a restricted `ctx` object:

- `ctx:GetQuestId()`
- `ctx:GetStage()`
- `ctx:SetStage(stage_id)`
- `ctx:GetObjectiveProgress(objective_id)`
- `ctx:AddObjectiveProgress(objective_id, amount)`
- `ctx:HasTag(tag)`
- `ctx:AddQuestFlag(flag)`
- `ctx:RemoveQuestFlag(flag)`
- `ctx:EmitQuestEvent(event_tag, payload)`
- `ctx:RequestDialogue(dialogue_id)`
- `ctx:RequestEncounter(encounter_id)`
- `ctx:CompleteQuest()`

Lua must not receive direct filesystem, process, network, raw actor spawning, inventory mutation, reward grants, or replication authority.

## MMORPG Adapter

- Executes quest Lua only on authoritative server or trusted quest service.
- Treats client events as requests that must be validated by gameplay systems.
- Writes progress through server save/state systems.
- Uses replicated state snapshots for client UI.
- Limits execution time and memory per hook.

## ARPG Adapter

- Can execute Lua locally in the gameplay runtime.
- Uses the same event names and objective schema as the MMORPG adapter.
- Writes progress through local save slots.
- May allow richer local encounter scripting only behind adapter-specific APIs.

## Example Quest Data

```json
{
  "quest_id": "QST_GNM_OGR_ShieldwallTrial_A01",
  "title": "quest.gnm_ogr.shieldwall_trial.title",
  "region": "kit.gnome_ogre_rivalry",
  "recommended_level": 12,
  "objectives": [
    {"id": "defend_projectors", "type": "defend", "target_tag": "AET_PROD_GNM_HeavyMekShieldwall_A01", "duration": 90},
    {"id": "disable_tek_core", "type": "interact", "target_tag": "ogre.teknomancer.core", "count": 1}
  ],
  "lua_module": "/Game/Aerathea/Quests/GnomeOgre/QST_GNM_OGR_ShieldwallTrial_A01.lua",
  "mmorpg_adapter": "QuestAdapter.Server.Authoritative",
  "arpg_adapter": "QuestAdapter.Local.Session"
}
```

## Example Lua Hook

```lua
function OnEnemyDefeated(ctx, enemy_tag)
    if enemy_tag == "ogre.teknomancer" then
        ctx:AddObjectiveProgress("disable_tek_core", 1)
    end
end

function CanComplete(ctx)
    return ctx:GetObjectiveProgress("defend_projectors") >= 90
       and ctx:GetObjectiveProgress("disable_tek_core") >= 1
end
```

## Production Checklist

- Quest behavior works from structured data without Lua when possible.
- Lua hooks are small, deterministic, and sandboxed.
- MMORPG path remains server-authoritative.
- ARPG path remains compatible with the same quest package.
- UI text and widgets stay Unreal/localization owned.
- Rewards and inventory changes are requested through gameplay systems, not directly granted by Lua.
