## Description

This trigger fires when a character moves whilst hidden. Any one of the following flags being set on the character will cause the trigger to be fired:

- statf_invisible
- statf_hidden
- statf_sleeping

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this trigger:

|                       |                                                   |
|-----------------------|---------------------------------------------------|
| **Name**              | **Description**                                   |
| [I](I "wikilink")     | The [character](Characters "wikilink") who moved. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") who moved. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | If non-zero, the character will be revealed. Replaced by STEPSTEALTH property since 27/08/2015 |

## Return Values

The following return values are explicitly defined for this trigger:

*No return values are handled by this trigger.*

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
