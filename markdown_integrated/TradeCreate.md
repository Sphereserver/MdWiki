## Description

This trigger fires when one player is going to begin a trade with
another player. The trigger will be fired on both characters.

Fires on:

- [Players](./CharactersPlayers.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [items](./Items.md) that the player is offering. |
| [I](./I.md) | The [player](./CharactersPlayers.md) beggining the trade. |
| [SRC](./SRC.md) | The [player](./CharactersPlayers.md) they try to trading with. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                              |
|------------------|------------------------------|
| **Return Value** | **Description**              |
| 1                | Prevents the trade to begin. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
