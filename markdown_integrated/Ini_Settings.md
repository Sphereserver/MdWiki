## Description

This page describes various settings available in the `sphere.ini` configuration file that influence server behavior and scripting.

## Settings

| Setting Name | Description | Default Value | Notes |
|---|---|---|---|
| `MaxLoopTimes` | Controls the maximum number of `TIMERF` executions allowed in a single tick. If exceeded, the loop is aborted, and a warning is issued. A value of 0 removes the limit. | (Varies) | Essential for preventing deadlocks from script errors. |
| `NetworkThreads` | Specifies the number of dedicated network threads the server should use. | (System-dependent) | Influences network performance. |
| `NetworkThreadPriority` | Sets the priority of the dedicated networking threads. | (Normal) | Can be adjusted for performance tuning. |
| `UseAsyncNetwork` | Enables or disables asynchronous packet sending. | (Boolean) | Affects network efficiency and responsiveness. |
| `DistanceTalk` | Sets the maximum distance for audible "talk" speech. Special values: -1 (never heard), 0 (heard if distance <= listener's VisualRange). | (Varies) | Controls speech audibility range. |
| `DistanceWhisper` | Sets the maximum distance for audible "whisper" speech. Special values: -1 (never heard), 0 (heard if distance <= listener's VisualRange). | (Varies) | Controls speech audibility range. |
| `DistanceYell` | Sets the maximum distance for audible "yell" speech. Special values: -1 (never heard), 0 (heard if distance <= listener's VisualRange). | (Varies) | Controls speech audibility range. |
| `FEATURE_EXTRA_ROLEPLAYFACES` | Enables extra roleplay face styles during character creation. | (Boolean) | Affects character customization options. |
| `CombatArcheryMovementDelay` | Sets the delay (in seconds) after which a player can initiate a new ranged combat swing after stopping movement, if `COMBAT_ARCHERYCANMOVE` is not set. | (Varies) | Controls ranged combat timing. |
| `OF_NoPaperdollTradeTitle` | If set, the trade title will not be shown on the paperdoll. | (Boolean) | Affects client UI display. |
| `ItemsMaxAmount` | Sets the upper limit for item stacking. | 65535 | Prevents server hang/crash with too high values. |
| `CombatParryingEra` | Controls parrying behavior with flags: `01` (pre-SE formula), `02` (SE formula), `010` (shield parry), `020` (one-handed parry without shield), `040` (two-handed parry). | (Flags) | Affects combat mechanics. |
| `MaxCharSkill` | Maximum limit of each skill for players and NPCs. | 1200 | Limits individual skill values. |
| `MaxPlayerSkill` | Maximum limit of total skills a player can have. | 7000 | Limits total player skill points. |
| `MaxPetSkill` | Maximum limit of total skills a pet can have. | 8000 | Limits total pet skill points. |
| `SkillCap` | Maximum limit of total skills a player can have (for backwards compatibility). | 7000 | Backwards compatible setting for total player skill points. |
| `COMBAT_ANIM_HIT_SMOOTH` | Enables the old smooth combat. | (Boolean) | Affects combat animation. |
| `COMBAT_SWING_NORANGE` | Allows starting a close-combat swing at a distance; the blow is landed only when entering range. | (Boolean) | Affects combat mechanics. |
| `CONTAINERMAXITEMS` | Maximum number of items inside a container. Higher values (above 125) are not fully supported by Enhanced Clients. | 255 | Affects container capacity and client compatibility. |
| `MAGICF_CASTPARALYZED` | Allows characters to cast spells even when paralyzed. | (Boolean) | Affects spellcasting mechanics. |
| `AutoProcessPriority` | Automatically sets the process priority at startup. | (Varies) | Affects server performance. |
| `OF_NoTargetTurn` | Prevents the character from turning towards the targeted point. | (Boolean) | Affects character targeting behavior. |
| `OF_StatAllowValOverMax` | Allows stat values to be set above their maximum, with @RegenStat decreasing them by 1 at a time when above max. | (Boolean) | Affects stat handling and regeneration. |
| `OF_GuardOutsideGuardedArea` | Allows guards to walk in unguarded areas. | (Boolean) | Affects guard AI behavior. |
| `ManaLossFail` | Character loses part of the mana required to cast the spell if the spell casting fails. | (Varies) | Affects spellcasting mechanics. |
| `OF_OWNoDropCarriedItem` | When overweight, prevents dropping items on the ground when moving them (or using BOUNCE) and checking carry capacity. | (Boolean) | Affects item movement and inventory management. |
| `COMBAT_FIRSTHIT_INSTANT` | Makes the first hit in a combat instant (0 delay). To mimic OSI combat, `COMBAT_PREHIT` and `COMBAT_FIRSTHIT_INSTANT` should be enabled. | (Boolean) | Affects combat mechanics. |
| `EraLimitGear` | Prevents NPCs from creating gear newer than the specified expansion. | (Expansion Value) | Controls NPC gear generation. |
| `EraLimitLoot` | Prevents NPCs from creating loot newer than the specified expansion. | (Expansion Value) | Controls NPC loot generation. |
| `EraLimitProps` | Prevents characters (players and NPCs) from having properties newer than the specified expansion. | (Expansion Value) | Controls character property application. |

[Category: Configuration](./CategoryConfiguration.md)