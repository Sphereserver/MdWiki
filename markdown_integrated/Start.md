## Description

This trigger fires when an attempt to use skill has started.

Fires on:

- [Skills](./SKILL.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) starting to use the skill. |
| [SRC](./SRC.md) | The [character](./Characters.md) starting to use the skill. |
| [ACT](./ACT.md) | The [backpack](./Backpack.md) trying to peek for snooping. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The skill number that has started. |
| LOCAL.CRAFTAMOUNT | IO | For crafting skills, the amount of the item that will be created. |
| LOCAL.CRAFTITEMDEF | IO | For crafting skills, the item [BASEID](./BASEID.md) that will be created. |
| LOCAL.CRAFTSTROKECNT | IO | For crafting skills, the number of 'strokes' until the skill completes. |
| local.GatherStrokeCnt | IO | For gathering skills, the number of 'strokes' until the skill completes. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                           |
|------------------|---------------------------|
| **Return Value** | **Description**           |
| 1                | Aborts the skill attempt. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
