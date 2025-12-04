## Description

This trigger fires when a character sees someone Snooping something.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [victim](Characters "wikilink") of the crime. |
| [I](I "wikilink") | The [character](Characters "wikilink") witnessing the crime. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") performing the criminal action. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The skill number that is needed to see the crime. (-1 = seen by all) |
| ARGN2 | I | The [UID](UID "wikilink") of the object related to the action. (e.g. a corpse, if the action is looting) |
| ARGS | I | A description of the criminal action. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | Allows the character to see the crime, with no skill check taking place. |
| 1 | Prevents the character from seeing the crime. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
