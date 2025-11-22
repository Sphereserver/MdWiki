## Description

This trigger fires when an NPC leaves its owner for one of the following
reasons:

- The owner harmed the NPC.
- The NPC became too hungry.
- The owner hasn't paid the NPC's wages.

Fires on:

- [NPCs](./CharactersNPCs.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [NPC](./CharactersNPCs.md) who is deserting their owner. |
| [SRC](./SRC.md) | The [owner](./Characters.md) of the NPC. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                             |
|------------------|---------------------------------------------|
| **Return Value** | **Description**                             |
| 1                | Prevents the NPC from deserting its master. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
