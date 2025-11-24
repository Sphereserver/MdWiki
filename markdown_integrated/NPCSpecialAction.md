## Description

This trigger fires when an NPC is about to perform a special action.
This can be used to script new actions or to intercept the following
actions:

- Fire elementals dropping fire.
- Spiders dropping spider webs.

Fires on:

- [NPCs](./CharactersNPCs.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [NPC](./CharactersNPCs.md) performing the action. |
| [SRC](./SRC.md) | The [NPC](./CharactersNPCs.md) performing the action. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the NPC from performing its hardcoded special action. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
NPCS](./_NPCS.md)
