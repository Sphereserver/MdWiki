## Description

This trigger fires when an attempt to use a skill fails.

Fires on:

- [Skills](./SKILL.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) failing the skill attenot. |
| [SRC](./SRC.md) | The [character](./Characters.md) failing the skill attempt. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                |
|--------------|------------|--------------------------------|
| **Argument** | **In/Out** | **Description**                |
| ARGN1        | I          | The skill number being failed. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                       |
|------------------|---------------------------------------|
| **Return Value** | **Description**                       |
| 1                | Bypasses normal skill fail behaviour. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
