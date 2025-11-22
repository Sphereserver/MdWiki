## Description

This trigger fires when a character receives damage.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) being damaged. |
| [SRC](./SRC.md) | The [character](./Characters.md) responsible for the damage. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |  |
|----|----|----|----|
| **Argument** | **In/Out** | **Description** | **Sphere X only?** |
| ARGN1 | IO | The amount of damage being applied. (Before Slayer calulation if applicable) |  |
| ARGN2 | IO | The type of damage being applied. |  |
| ARGN3 | IO | Hits will be fixed to this amount after the hit if the value is greater than it, default = maxhits. |  |
| LOCAL.ITEMDAMAGECHANCE | IO | Sets the chance for the hitted part of the body (Armor or shield, if any) to be damaged (Default: 40% in Sphere D, 25% in Sphere X). |  |
| LOCAL.DAMAGEPERCENTPHYSICAL | I | The amount in % of the physical damage received, only set if Elemental Engine is enabled. | X |
| LOCAL.DAMAGEPERCENTFIRE | I | The amount in % of the fire damage received, only set if Elemental Engine is enabled. | X |
| LOCAL.DAMAGEPERCENTCOLD | I | The amount in % of the cold damage received, only set if Elemental Engine is enabled. | X |
| LOCAL.DAMAGEPERCENTPOISON | I | The amount in % of the poison damage received, only set if Elemental Engine is enabled. | X |
| LOCAL.DAMAGEPERCENTENERGY | I | The amount in % of the energy damage received, only set if Elemental Engine is enabled. | X |
| LOCAL.SPELL | I | Display the spell number that damaged the character. | X |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                     |
|------------------|-------------------------------------|
| **Return Value** | **Description**                     |
| 1                | Prevents damage from being applied. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
