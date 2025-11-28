## Description

This trigger fires when a spell memory item is going to be removed from
the character.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |  |  |
|----|----|----|----|
| **Name** | **Description** | [I](I "wikilink") | The target of the spell. |
| [SRC](SRC "wikilink") | The caster of the spell. |  |  |
| [ARGO](ARGO "wikilink") | The spell item. |  |  |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                   |
|--------------|------------|-------------------|
| **Argument** | **In/Out** | **Description**   |
| ARGN1        | IO         | The spell number. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | Remove the spell memory item but don't execute the default spell behaviour when the spell item is removed. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
