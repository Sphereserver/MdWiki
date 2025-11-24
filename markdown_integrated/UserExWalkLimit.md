## Description

This trigger fires when a player exceeds the walking limit defined by
the WALKBUFFER and WALKREGEN settings in Sphere.ini. This could indicate
that the player is using a cheat to run faster than they should (i.e.
speedhacking) or it could be a result of a poor connection between the
server and client.

Fires on:

- [Players](./CharactersPlayers.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [player](./CharactersPlayers.md) exceeding the walk limit. |
| [SRC](./SRC.md) | The [player](./CharactersPlayers.md) exceeding the walk limit. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Allows the player to continue moving without being restricted. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Players](./_Players.md)
