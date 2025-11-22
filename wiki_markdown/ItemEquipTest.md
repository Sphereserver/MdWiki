## Description

This trigger fires when a character equips an item and Sphere is
deciding whether or not the character is allowed to equip it.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](./ACT.md) | The [item](./Items.md) being equipped. |
| [I](./I.md) | The [character](./Characters.md) equipping the item. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                        |
|------------------|----------------------------------------|
| **Return Value** | **Description**                        |
| 1                | Prevents the item from being equipped. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
