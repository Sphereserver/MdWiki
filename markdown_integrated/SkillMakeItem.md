## Description

This trigger fires when a character successfully crafts an item.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](./ACT.md) | The [item](./Items.md) that was crafted. |
| [ARGO](./ARGO.md) | The [item](./Items.md) that the item was crafted from. |
| [I](./I.md) | The [character](./Characters.md) who crafted the item. |
| [SRC](./SRC.md) | The [character](./Characters.md) who crafted the item. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                             |
|--------------|------------|---------------------------------------------|
| **Argument** | **In/Out** | **Description**                             |
| ARGN1        | I          | The amount of skill used to craft the item. |
| ARGN2        | I          | The quality of the crafted item.            |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | Proceeds with rewarding experience (if enabled) and placing the crafting item into the character's backpack, but does not play any potion sounds or display quality messages. |
| 1 | Prevents any further action taking place for the skill. The crafted item will also be deleted. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
