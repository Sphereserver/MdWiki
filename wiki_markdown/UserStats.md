## Description

This trigger fires when a status update is sent to a player.

Fires on:

- [Clients](./CharactersClients.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [client](./CharactersClients.md) receiving the status update. |
| [SRC](./SRC.md) | The [character](./Characters.md) whose status they are receiving. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN3 | I | If 1, then the client requested the update (i.e. opened their status window) |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                             |
|------------------|---------------------------------------------|
| **Return Value** | **Description**                             |
| 1                | Prevents the status update from being sent. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Players](./_Players.md)
