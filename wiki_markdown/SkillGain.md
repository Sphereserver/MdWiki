## Description

This trigger fires when a character receives an opportunity to gain in
skill.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) trying to gain skill. |
| [SRC](./SRC.md) | The [character](./Characters.md) trying to gain skill. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The skill number being gained. |
| ARGN2 | IO | The chance to gain skill. (1 - 1000) |
| ARGN3 | IO | The maximum skill level that the character can gain to. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                            |
|------------------|--------------------------------------------|
| **Return Value** | **Description**                            |
| 1                | Prevents the character from gaining skill. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
