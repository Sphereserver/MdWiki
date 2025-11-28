## Description

This trigger fires when the gathering proccess is going to finish.

Fires on:

- [Region Resources](REGIONRESOURCE "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [worldgem bit](Items "wikilink") that represents the resource in the world. |
| [I](I "wikilink") | The [region resource](REGIONRESOURCE "wikilink") being gathered. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") gathering the resource. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| Local.ResourceID | IO | The id of the item being gathered. |
| ARGN1 | IO | The amount of the resource being gathered at this time. |
|  |  |  |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the resource from being gathered, showing up the related messages. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
