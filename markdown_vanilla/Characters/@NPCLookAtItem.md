## Description

This trigger fires when an NPC looks at an item.

Fires on:

- [NPCs](Characters#NPCs "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [item](Items "wikilink") being looked at. |
| [I](I "wikilink") | The [NPC](Characters#NPCs "wikilink") looking at the item. |
| [SRC](SRC "wikilink") | The [NPC](Characters#NPCs "wikilink") looking at the item. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The distance between the NPC and the item. |
| ARGN2 | IO | How much the NPC wants the item, as a percentage (0 - 100). |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | Prevents the NPC from seeing the item, allows it to look at other items instead. |
| 1 | Prevents the NPC from seeing the item, does not allow it to look at other items. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink") [Category: Characters](Category:_Characters "wikilink") [Category: NPCS](Category:_NPCS "wikilink")
