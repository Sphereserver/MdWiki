## Description

This trigger fires when a character pays to train, buy something, or
hire them.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) paying for the service. |
| [SRC](./SRC.md) | The [character](./Characters.md) receiving the gold.. |
| [ARGO](./ARGO.md) | The stack of gold used to pay (if any) (ie training). |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | Gold to pay. |
| ARGN2 | IO | Payment type ( 0 = training, 1 = buying something, 2 = hiring the NPC) |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                   |
|------------------|-----------------------------------|
| **Return Value** | **Description**                   |
| 1                | Stops the payment from occurring. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
