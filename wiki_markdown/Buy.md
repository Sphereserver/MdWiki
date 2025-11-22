## Description

This trigger fires when an item is bought from a vendor. The trigger
fires on each item that is bought in the transaction.

Fires on:

- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [vendor](./CharactersNPCs.md) the item is being bought from. |
| [I](./I.md) | The [item](./Items.md) being bought. |
| [SRC](./SRC.md) | The [character](./Characters.md) buying the item. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The amount of the item being bought. |
| ARGN2 | I | The final cost of the item (amount \* value). |
| LOCAL.TOTALCOST | I | The total cost for the whole transaction ( the sum of the final prizes of all items ). |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the character from buying the item (blocks the entire transaction). |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
