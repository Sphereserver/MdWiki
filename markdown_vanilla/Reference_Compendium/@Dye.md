## Description

This trigger fires when an item is dyed by a dye tub. It is also called
in script color changes, dye tub color changes, @Create color
assignment, and staff .xcolor command.

Fires on:

- [Items](Items "wikilink")
- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [item](Items "wikilink") being dyed. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") dyeing the item. |
| [ARGO](ARGO "wikilink") | The [item](Items "wikilink") originating the dye target. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                              |
|--------------|------------|------------------------------|
| **Argument** | **In/Out** | **Description**              |
| ARGN1        | IO         | The hue value.               |
| ARGN2        | IO         | Sound effect (Default 023E). |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Stop internal dye sound. Hue changes made from script will take place. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
