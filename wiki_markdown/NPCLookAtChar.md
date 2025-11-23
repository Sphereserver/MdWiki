## Description

This trigger fires when an NPC looks at another character.

Fires on:

- [NPCs](./CharactersNPCs.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [NPC](./CharactersNPCs.md) looking at a character. |
| [SRC](./SRC.md) | The [character](./Characters.md) being looked at. |

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
| 0 | Prevents the NPC from seeing the character, allows it to look at other characters. |
| 1 | Prevents the NPC from seeing the character, does not allow it to look at other characters. |

## Notes
- This trigger now fires more frequently due to NPCs performing AI checks ("look around") while wandering.
- NPCs can now play different sounds depending on their AI choices when looking around.

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
NPCS](./_NPCS.md)
