## Description

This trigger fires when a player exits house design mode.

Fires on:

- [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [Customizable Multis\|custom multi](Special_Items "wikilink") being designed. |
| [I](I "wikilink") | The [player](Characters#Players "wikilink") designing the multi. |
| [SRC](SRC "wikilink") | The [player](Characters#Players "wikilink") designing the multi. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | Indicates whether or not the player is being forced out of design mode (e.g. due to logout) |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the player from leaving design mode, if ARGN1 is 0. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
