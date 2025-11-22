## Description

This trigger fires when a character drops an item inside another item
(e.g. a backpack).

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](./ACT.md) | The [item](./Items.md) that is being dropped on to. |
| [ARGO](./ARGO.md) | The [item](./Items.md) being dropped on to the item. |
| [I](./I.md) | The [character](./Characters.md) dropping the item. |

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
| 1 | Prevents the item from being dropped on to the item. If no CONT is set, item will drop on ground. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
