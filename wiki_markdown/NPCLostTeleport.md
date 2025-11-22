## Description

This trigger fires when an NPC gets lost and is about to be teleported
back to its [HOME](./HOME.md) location. The LOSTNPCTELEPORT
setting in Sphere.ini controls how far an NPC can wander from its home
location before it is considered to be lost.

Fires on:

- [NPCs](./CharactersNPCs.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [NPC](./CharactersNPCs.md) who has gotten lost. |
| [SRC](./SRC.md) | The [NPC](./CharactersNPCs.md) who has gotten lost. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The distance between the NPC and its home location. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                   |
|------------------|---------------------------------------------------|
| **Return Value** | **Description**                                   |
| 1                | Prevents the NPC from being teleported back home. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
NPCS](./_NPCS.md)
