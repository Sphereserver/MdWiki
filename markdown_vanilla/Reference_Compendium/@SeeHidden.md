## Description

This trigger fires when character is going to see a hidden character so
it can control whether to see it or not.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|                       |                                                 |
|-----------------------|-------------------------------------------------|
| **Name**              | **Description**                                 |
| [I](I "wikilink")     | The [character](Characters "wikilink") viewing. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") hidden.  |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | 0 will remain invisible for the viewer/ 1 the viewer will see this character grayed (like an Admin sees an invisible GM). |

## Notes

This trigger is being fired a lot, keep it clean.

## Return Values

The following return values are explicitly defined for this trigger:

*This trigger doesn't have return values, characters must be send
always.*

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
