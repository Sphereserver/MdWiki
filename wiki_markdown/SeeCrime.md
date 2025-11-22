## Description

This trigger fires when a character witnesses a crime taking place.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [victim](./Characters.md) of the crime. |
| [I](./I.md) | The [character](./Characters.md) witnessing the crime. |
| [SRC](./SRC.md) | The [character](./Characters.md) performing the criminal action. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | If ARGN1 this character will add MEMORY_SAWCRIME to SRC's memory, so SRC will be flagged as criminal for this character. |
|  |  |  |

## Return Values

There are no return values related to this trigger.

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
