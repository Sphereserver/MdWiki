## Description

This trigger fires when an NPC looks at an item.

Fires on:

- [NPCs](./CharactersNPCs.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [item](./Items.md) being looked at. |
| [I](./I.md) | The [NPC](./CharactersNPCs.md) looking at the item. |
| [SRC](./SRC.md) | The [NPC](./CharactersNPCs.md) looking at the item. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The distance between the NPC and the item. |
| ARGN2 | IO | How much the NPC wants the item, as a percentage (0 - 100). |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | Prevents the NPC from seeing the item, allows it to look at other items instead. |
| 1 | Prevents the NPC from seeing the item, does not allow it to look at other items. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
NPCS](./_NPCS.md)
