## Description

This trigger fires when a character's karma level is about to change.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) whose karma is changing. |
| [SRC](./SRC.md) | The [character](./Characters.md) whose karma is changing. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                                    |
|--------------|------------|----------------------------------------------------|
| **Argument** | **In/Out** | **Description**                                    |
| ARGN1        | IO         | The amount of karma being added (can be negative). |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                    |
|------------------|----------------------------------------------------|
| **Return Value** | **Description**                                    |
| 1                | Prevents the character's karma from being changed. |
| 0                | Applies changes to ARGN1.                          |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
