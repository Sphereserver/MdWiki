## Description

This trigger fires when a character's experience level is changed.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [character](./Characters.md) that was killed, if the experience change originated from a kill, |
| [I](./I.md) | The [character](./Characters.md) whose experience is being changed. |
| [SRC](./SRC.md) | The [character](./Characters.md) whose experience is being changed. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | The amount of experience being added (can be negative). |
| ARGN2 | IO | If non-zero, a message will be displayed to the client to inform them of the change. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the character's experience level from being changed. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
