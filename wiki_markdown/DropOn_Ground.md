## Description

This trigger fires when an item is dropped on to the ground.

Fires on:

- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [item](./Items.md) being dropped. |
| [SRC](./SRC.md) | The [character](./Characters.md) dropping the item. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                              |
|--------------|------------|----------------------------------------------|
| **Argument** | **In/Out** | **Description**                              |
| ARGN1        | IO         | The decay time that will be set on the item. |
| ARGS         | I          | The location that the item was dropped at.   |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the item from being deleted if dropped on water. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
