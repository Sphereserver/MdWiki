## Description

This trigger fires when a character's fame level is about to change.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [character](Characters "wikilink") whose fame is changing. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") whose fame is changing. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

|              |            |                                                   |
|--------------|------------|---------------------------------------------------|
| **Argument** | **In/Out** | **Description**                                   |
| ARGN1        | IO         | The amount of fame being added (can be negative). |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                   |
|------------------|---------------------------------------------------|
| **Return Value** | **Description**                                   |
| 1                | Prevents the character's fame from being changed. |
| 0                | Applies changes to I.                             |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
