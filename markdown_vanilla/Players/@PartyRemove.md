## Description

This trigger fires when a character is about to be removed from a party
by it's party master.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [character](Characters "wikilink") being removed from the party. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") removing another from the party (master). |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | when argn1=1, means informative remove when a @PartyDisband has been fired before and is in proccess now. In this case, no return can stop this action. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                     |
|------------------|---------------------|
| **Return Value** | **Description**     |
| 1                | Cancels the action. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Players](Category:_Players "wikilink")
