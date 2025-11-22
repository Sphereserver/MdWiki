## Description

This trigger is fired when the NPC is about to select a
[spell](./SPELL.md) to cast. When assigning spells to a NPC make
sure these spells does not have the SPELLFLAG_PLAYERONLY flag.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The current NPC's target. |
| [I](./I.md) | The NPC caster. |
| [SRC](./SRC.md) | The NPC caster. |
| [REF1](./REF1.md) | The new target, this will override the target set on [ARGO](./ARGO.md). |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | The spell being cast, this can be a spell not found in the NPC's spellbook. |
| ARGN2 | O | If 1 the spell is being cast by a wand. (If the NPC is wielding a wand it has a 50% chance to cast the spell from the wand instead of the spellbook. |
| local.healthreshold | IO | This value determines at what health threshold (in percent) the NPC will successfully select a [spell](./SPELL.md) with the SPELLFLAG_HEAL flag. The value is taken from the [sphere.ini](./sphereini.md) property NPCHealThreshold and the default value is 30. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                 |
|------------------|---------------------------------|
| **Return Value** | **Description**                 |
| 1                | Interrupts the spell selection. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
