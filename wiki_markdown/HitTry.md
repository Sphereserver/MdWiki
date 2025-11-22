## Description

This trigger fires when a character is about to swing their weapon or
fist using a combat skill.

More info on [How_Combat_Works](./How_Combat_Works.md)

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
| ARGN1 | IO | The time, in tenths of a second, until the swing will complete. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                            |
|------------------|----------------------------|
| **Return Value** | **Description**            |
| 1                | Prevents the combat swing. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
