## Description

This trigger fires when a character picks up an item from inside a
container.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](./ACT.md) | The [item](./Items.md) being picked up. |
| [I](./I.md) | The [character](./Characters.md) picking up the item. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                         |
|--------------|------------|-----------------------------------------|
| **Argument** | **In/Out** | **Description**                         |
| ARGN1        | I          | The amount of the item being picked up. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                         |
|------------------|-----------------------------------------|
| **Return Value** | **Description**                         |
| 1                | Prevents the item from being picked up. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
