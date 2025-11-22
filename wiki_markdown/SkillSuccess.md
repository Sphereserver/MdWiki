## Description

This trigger fires when a character succeeds at an attempt to use a
skill.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) succeeding the skill attempt. |
| [SRC](./SRC.md) | The [character](./Characters.md) succeeding the skill attempt. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                      |
|--------------|------------|--------------------------------------|
| **Argument** | **In/Out** | **Description**                      |
| ARGN1        | I          | The skill number that has succeeded. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                           |
|------------------|---------------------------|
| **Return Value** | **Description**           |
| 1                | Aborts the skill attempt. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
