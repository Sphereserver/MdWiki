## Description

This trigger fires when an NPC is about to accept an item that another
character is giving them.

Fires on:

- [NPCs](./CharactersNPCs.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [item](./Items.md) the NPC is accepting. |
| [I](./I.md) | The [NPC](./CharactersNPCs.md) accepting the item. |
| [SRC](./SRC.md) | The [character](./Characters.md) giving the item away. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                          |
|------------------|--------------------------|
| **Return Value** | **Description**          |
| 1                | Returns the item to SRC. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
NPCS](./_NPCS.md)
