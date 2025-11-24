## Description

This trigger fires when a character hits someone using a combat skill.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [weapon](./Items.md) being used (can be nothing, if fists are used). |
| [I](./I.md) | The [character](./Characters.md) doing the hitting. |
| [SRC](./SRC.md) | The [character](./Characters.md) being hit. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | The amount of damage being dealt. |
| ARGN2 | IO | The type(s) of damage. |
| LOCAL.ARROW | I | UID of the arrow used (Archery only) |
| LOCAL.ARROWHANDLED | IO | if set to !=0, you can do whatever you want with local.arrow |
| LOCAL.ITEMDAMAGECHANCE | IO | Sets the chance for the weapon to be damaged (Default: 25). |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                           |
|------------------|---------------------------|
| **Return Value** | **Description**           |
| 1                | Cancels the combat swing. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
