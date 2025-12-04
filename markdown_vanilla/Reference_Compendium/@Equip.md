## Description

This trigger fires when an item is equipped.

Fires on:

- [Items](Items "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [item](Items "wikilink") being equipped. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") equipping the item. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

| **Return Value** | **Description** |
| --- | --- |
| 1 | Treats the item as failed to equip. **Note:** This trigger is not reliable for blocking the equipping of an item. Use the [@EquipTest](@EquipTest) trigger instead which is designed for blocking the equip action. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
