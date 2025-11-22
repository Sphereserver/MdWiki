## Description

This trigger fires when an item is dyed by a dye tub. It is also called
in script color changes, dye tub color changes, @Create color
assignment, and staff .xcolor command.

Fires on:

- [Items](./Items.md)
- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [item](./Items.md) being dyed. |
| [SRC](./SRC.md) | The [character](./Characters.md) dyeing the item. |
| [ARGO](./ARGO.md) | The [item](./Items.md) originating the dye target. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                              |
|--------------|------------|------------------------------|
| **Argument** | **In/Out** | **Description**              |
| ARGN1        | IO         | The hue value.               |
| ARGN2        | IO         | Sound effect (Default 023E). |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Stop internal dye sound. Hue changes made from script will take place. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
