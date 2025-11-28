## Description

This trigger fires when someone is being added to my attacker list.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | Myself, someone is being entering in combat with me (or I am entering in combat with |
| [SRC](SRC "wikilink") | The character entering in my list. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|          |                                                                 |
|----------|-----------------------------------------------------------------|
| **Name** | **Description**                                                 |
| ARGN1    | Threat set to this SRC, if enabled on ini and I'm not a player. |
| ARGN2    | Sets wether to add SRC as ignored or not.                       |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents src of being added to my list, however I will try to add him each time I can. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Combat](Category:_Combat "wikilink")
