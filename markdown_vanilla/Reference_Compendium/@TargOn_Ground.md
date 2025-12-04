## Description

This trigger fires when the ground is targeted with an item.

Fires on:

- [Items](Items "wikilink")

## References

The following object references are explicitly available for this trigger:

| **Name** | **Description** |
| --- | --- |
| [I](I) | The [item](Items) that the target cursor originated from. |
| [SRC](SRC) | The [player](Characters#Players) targeting the ground. **Note:** The [TARGP](TARGP) property on the player can be used to acquire the target coordinates. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

|              |            |                                                    |
|--------------|------------|----------------------------------------------------|
| **Argument** | **In/Out** | **Description**                                    |
| ARGN1        | I          | If a static item was targeted, the ID of the item. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents Sphere from processing the default target behaviour. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
