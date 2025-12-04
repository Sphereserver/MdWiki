## Description

This trigger fires when an NPC attempts to move closer to or further away from another character.

Fires on:

- [NPCs](Characters#NPCs "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [NPC](Characters#NPCs "wikilink") doing the following. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") the NPC is trying to get closer to or further from. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | If non-zero, the NPC is attempting to flee from the target. |
| ARGN2 | IO | The distance between the NPC and target that it is trying to achieve. |
| ARGN3 | IO | If non-zero and the NPC is trying to move closer, then the NPC will move further away from the target if they are closer than the distance they were trying to achieve. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | Prevents any movement from taking place, and aborts further attempts to follow the target. |
| 1 | Prevents any movement from taking place, and allows the NPC to make further attempts to follow the target. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink") [Category: Characters](Category:_Characters "wikilink") [Category: NPCS](Category:_NPCS "wikilink")
