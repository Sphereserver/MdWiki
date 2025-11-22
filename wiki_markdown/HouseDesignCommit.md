## Description

This trigger fires when a player attempts to commit a new house design.

Fires on:

- [Players](./CharactersPlayers.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [custom multi](./Special_ItemsCustomizable_Multis.md) being designed. |
| [I](./I.md) | The [player](./CharactersPlayers.md) committing the design. |
| [SRC](./SRC.md) | The [player](./CharactersPlayers.md) committing the design. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The total number of components in the current house design. |
| ARGN2 | I | The total number of components in the house design being committed. |
| ARGN3 | I | The revision number of the house design being committed. |
| LOCAL.FIXTURES.NEW | I | The total number of fixtures in the house design being committed. |
| LOCAL.FIXTURES.OLD | I | The total number of fixtures in the current house design. |
| LOCAL.MAXZ | I | The value of the top placed item |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                 |
|------------------|-------------------------------------------------|
| **Return Value** | **Description**                                 |
| 1                | Prevents the house design from being committed. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
