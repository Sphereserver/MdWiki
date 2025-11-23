\_\_FORCETOC\_\_

## Description

This trigger fires when an item is being equipped and Sphere is deciding
whether or not the character is allowed to equip it.

Fires on:

- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [item](./Items.md) being equipped. |
| [SRC](./SRC.md) | The [character](./Characters.md) equipping the item. |

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

## Notes
- This trigger is now called only when trying to equip equippable items. Previously, it was also called when dropping or creating an item to be equipped or bounced to an NPC's pack.

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
