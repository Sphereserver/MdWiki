## Description

This trigger fires when a character witnesses a crime taking place.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [victim](Characters "wikilink") of the crime. |
| [I](I "wikilink") | The [character](Characters "wikilink") witnessing the crime. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") performing the criminal action. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | If ARGN1 this character will add MEMORY_SAWCRIME to SRC's memory, so SRC will be flagged as criminal for this character. |
|  |  |  |

## Return Values

There are no return values related to this trigger.

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
