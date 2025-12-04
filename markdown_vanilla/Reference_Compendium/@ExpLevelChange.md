## Description

This trigger fires when a character's experience level is about to change.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [character](Characters "wikilink") whose experience level is about to change. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") whose experience level is about to change. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | The number of experience levels being added (can be negative). |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                   |
|------------------|---------------------------------------------------|
| **Return Value** | **Description**                                   |
| 1                | Prevents the experience level from being changed. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
