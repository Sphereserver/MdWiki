## Description

This trigger fires when a character drops an item on to the ground. The trigger now fires *before* the item's new position (`P`) is set.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](./ACT.md) | The [item](./Items.md) being dropped. |
| [I](./I.md) | The [character](./Characters.md) dropping the item. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                              |
|--------------|------------|----------------------------------------------|
| **Argument** | **In/Out** | **Description**                              |
| ARGN1        | IO         | The decay time, in tenths of a second, that will be set on the item. |
| ARGN2        | I          | Set to `1` if the trigger is called during a BOUNCE check (e.g., an overloaded character dropping the item). |
| ARGS         | I          | The location ([P](./P.md)) that the item will be dropped at. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the item from being deleted if dropped on water. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
