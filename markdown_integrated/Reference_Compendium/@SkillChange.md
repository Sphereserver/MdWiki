## Description

This trigger fires when a character's skill level is about to change.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [character](Characters "wikilink") whose skill level is changing. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") whose skill level is changing. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                        |
|--------------|------------|----------------------------------------|
| **Argument** | **In/Out** | **Description**                        |
| ARGN1        | I          | The number of the skill being changed. |
| ARGN2        | IO         | The new value of the skill.            |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                         |
|------------------|-----------------------------------------|
| **Return Value** | **Description**                         |
| 1                | Prevents the skill level being changed. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
