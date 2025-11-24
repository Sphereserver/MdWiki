## Description

This trigger fires when an item is sold to a vendor. The trigger fires
on each item that is sold in the transaction.

Fires on:

- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [vendor](./CharactersNPCs.md) the item is being sold to. |
| [I](./I.md) | The [item](./Items.md) being sold. |
| [SRC](./SRC.md) | The [character](./Characters.md) selling the item. |

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

## Notes
- Vendors can now re-sell items previously bought from players.
