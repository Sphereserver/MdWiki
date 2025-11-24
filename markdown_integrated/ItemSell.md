## Description

This trigger fires when a character sells an item to a vendor. The
trigger fires for each item that is sold in the transaction. Gold received from sales is added to existing gold piles in the character's pack, rather than creating new piles for each transaction.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](./ACT.md) | The [item](./Items.md) being sold. |
| [ARGO](./ARGO.md) | The [vendor](./CharactersNPCs.md) the item is being sold to. |
| [I](./I.md) | The [character](./Characters.md) selling the item. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                                 |
|--------------|------------|-------------------------------------------------|
| **Argument** | **In/Out** | **Description**                                 |
| ARGN1        | I          | The amount of items sold.                       |
| ARGN2        | I          | The price of the items sold after vendermarkup. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the character from selling the item (blocks the entire transaction). |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
