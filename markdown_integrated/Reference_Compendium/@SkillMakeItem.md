## Description

This trigger fires when a character successfully crafts an item.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](ACT "wikilink") | The [item](Items "wikilink") that was crafted. |
| [ARGO](ARGO "wikilink") | The [item](Items "wikilink") that the item was crafted from. |
| [I](I "wikilink") | The [character](Characters "wikilink") who crafted the item. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") who crafted the item. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

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

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
