## Description

This trigger fires when a character steps on an item. After being stepped on, this trigger will periodically fire until the character steps off the item.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](ACT "wikilink") | The [item](Items "wikilink") being stepped on. |
| [I](I "wikilink") | The [character](Characters "wikilink") stepping on the item. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

|              |            |                                                    |
|--------------|------------|----------------------------------------------------|
| **Argument** | **In/Out** | **Description**                                    |
| ARGN1        | I          | If 1, the character is standing still on the item. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                          |
|------------------|------------------------------------------|
| **Return Value** | **Description**                          |
| 1                | Prevents the item from being stepped on. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
