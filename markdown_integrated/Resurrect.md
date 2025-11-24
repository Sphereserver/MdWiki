## Description

This trigger fires when a character is about to be resurrected.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) being resurrected. |
| [SRC](./SRC.md) | The [character](./Characters.md) being resurrected. |
| [ARGO](./ARGO.md) | The corpse (If any is near) (Readable only). |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                   |
|--------------|------------|-----------------------------------|
| **Argument** | **In/Out** | **Description**                   |
| ARGN1        | IO         | Hit point value when resurrected. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                    |
|------------------|------------------------------------|
| **Return Value** | **Description**                    |
| 1                | Stops resurrection from occurring. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
