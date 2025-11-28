## Description

This trigger fires when a character attempts to mount a rideable
creature.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [creature](Characters "wikilink") being mounted. |
| [I](I "wikilink") | The [character](Characters "wikilink") attempting to mount the creature. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") attempting to mount the creature. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | The itemID of the item containing the animation use when moounting.(Anim \# is in tiledata of this item) \[Sphere X\] |
|  |  |  |

`   NOTE: When mounting a pet you'll read a non sense random value in ARGN1 but you can replace it by an ITEMID to force anim`  
`   EX: 03ea6 for Llama anim or 03e9f for gray horse anim. Yes 03ea6 is a ship part but in tiledata it link to anim 828`

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                    |
|------------------|----------------------------------------------------|
| **Return Value** | **Description**                                    |
| 1                | Prevents the character from mounting the creature. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
