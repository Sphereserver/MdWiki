## Description

This trigger fires when a character is about to miss a combat swing.

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
| [SRC](./SRC.md) | The [character](./Characters.md) who was missed. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| LOCAL.ARROWHANDLED | IO | if set to !=0, you can do whatever you want with local.arrow |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                           |
|------------------|---------------------------|
| **Return Value** | **Description**           |
| 1                | Cancels the attack swing. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
