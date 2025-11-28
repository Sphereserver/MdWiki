## Description

This trigger fires when a character is under effect of a periodic spell
(like Poison spell).

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|                       |                                                   |
|-----------------------|---------------------------------------------------|
| **Name**              | **Description**                                   |
| [I](I "wikilink")     | The object that is going to be affected.          |
| [SRC](SRC "wikilink") | The object that is going to be affected.          |
| ARGO                  | The spell memory.(Argo.link holds the caster UID) |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | Spell Id |
| ARGN2 | IO | Spell Level |
| LOCAL.CHARGES | IO | How many charges are left on the spell memory, this will be automatically decreased by 1 at the end of the method execution. Default value is 1. |
| LOCAL.DELAY | IO | How many seconds until the next spell effect tick. Default value is 5 seconds. |
| LOCAL.EFFECT | IO | The effect value of the spell, harmful or beneficial (if SPELLFLAG_HEAL is enabled). |
| LOCAL.DAMAGETYPE | IO | The damage type of the spell, if you are making a custom spell you must set a value otherwise the spell will not cause damage. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Destroy the spell memory and block the spell execution. |
| 0 | If the spell has the flag SPELLFLAG_SCRIPTED blocks the spell execution |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
