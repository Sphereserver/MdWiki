## Description

This trigger fires when an attempt to use skill has succeeded.

Fires on:

- [Skills](./SKILL.md)

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

|                  |                                         |
|------------------|-----------------------------------------|
| **Return Value** | **Description**                         |
| 1                | Aborts the skill attempt.               |
| 0                | Aborts the skill, but grants Skillgain. |
| 2                | Aborts the skill, but grants Skillgain. |
|                  |                                         |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
