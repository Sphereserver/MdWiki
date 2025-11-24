## Description

This trigger fires when a character begins to cast a spell.

Fires on:

- [Spells](./SPELL.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [item](./Items.md) being used to cast the spell (e.g. a wand or scroll). |
| [I](./I.md) | The [character](./Characters.md) casting the spell. |
| [SRC](./SRC.md) | The [character](./Characters.md) casting the spell. |
| [ACT](./ACT.md) | The [character](./Characters.md) or [item](./Items.md) being hit by the spell. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | The spell number being cast. |
| ARGN2 | IO | The difficulty of the spell. |
| ARGN3 | IO | The length of time it will take to cast the spell, in tenths of a second. |
| local.WOP | IO | Enables/Disables the WOP for this character and spell. |
| local.WOPColor | IO | Sets the color of WOP. |
| local.WOPFont | IO | Sets the font of WOP. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                     |
|------------------|-------------------------------------|
| **Return Value** | **Description**                     |
| 1                | Prevents the spell from being cast. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
