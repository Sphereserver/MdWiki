## Description

This trigger fires when two players have accepted a trade agreement. The
trigger will be fired on both characters.

Fires on:

- [Players](./CharactersPlayers.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [player](./CharactersPlayers.md) accepting the trade. |
| [I](./I.md) | The [player](./CharactersPlayers.md) accepting the trade. |
| [REF](./REF.md)1 to [REF](./REF.md)\<ARGN1\> | The [items](./Items.md) that the player is receiving. |
| [SRC](./SRC.md) | The [player](./CharactersPlayers.md) they are trading with. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The number of items that the player is receiving. |
| ARGN2 | I | The number of items that the other player is receiving. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                         |
|------------------|-----------------------------------------|
| **Return Value** | **Description**                         |
| 1                | Prevents the transaction to take place. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Players](./_Players.md)
