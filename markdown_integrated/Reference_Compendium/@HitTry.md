## Description

This trigger fires when a character is about to swing their weapon or
fist using a combat skill.

More info on [How_Combat_Works](How_Combat_Works "wikilink")

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [weapon](Items "wikilink") being used (can be nothing, if fists are used). |
| [I](I "wikilink") | The [character](Characters "wikilink") doing the hitting. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") being hit. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | The time, in tenths of a second, until the swing will complete. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                            |
|------------------|----------------------------|
| **Return Value** | **Description**            |
| 1                | Prevents the combat swing. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
