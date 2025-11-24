## Description

This trigger fires when a player attempts to use a special move. It also fires when a player presses a 'combat ability' slot on the KR toolbar.

Fires on:

- [Players](./CharactersPlayers.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [player](./CharactersPlayers.md) using the special move. |
| [SRC](./SRC.md) | The [player](./CharactersPlayers.md) using the special move. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                              |
|--------------|------------|------------------------------|
| **Argument** | **In/Out** | **Description**              |
| ARGN1        | I          | The special move being used. |

## Return Values

The following return values are explicitly defined for this trigger:

*No return values are handled for this trigger.*

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Players](./_Players.md)
