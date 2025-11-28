## Description

This trigger fires when a skill is aborted.

Fires on:

- [Skills](SKILL "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [character](Characters "wikilink") aborting the skill. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") aborting the skill. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                 |
|--------------|------------|---------------------------------|
| **Argument** | **In/Out** | **Description**                 |
| ARGN1        | I          | The skill number being aborted. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                       |
|------------------|---------------------------------------|
| **Return Value** | **Description**                       |
| 1                | Bypasses normal skill fail behaviour. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
