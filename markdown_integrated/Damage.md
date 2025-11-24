## Description

This trigger fires when an item receives damage.

Fires on:

- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [item](./Items.md) taking damage. |
| [SRC](./SRC.md) | The [character](./Characters.md) responsible for the damage, in the case of a weapon, it's the [character](./Characters.md) that receive the hit. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                     |
|--------------|------------|-------------------------------------|
| **Argument** | **In/Out** | **Description**                     |
| ARGN1        | I          | The amount of damage being applied. |
| ARGN2        | I          | The damage attributes.              |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                       |
|------------------|---------------------------------------|
| **Return Value** | **Description**                       |
| 1                | Prevents the item from being damaged. |

## Notes

Damage function in items doesn't mean the amount of hitpoints receiving
but a chance to receive 1 point of damage, so by default Sphere is using
this formula to calc the chace of receive damage:

<spherescript>local.success = \<eval <MaxHits>\*16\> if
(\<r\<local.success\>\> \> damage)

`return 1// and block the damage`

endif</spherescript>

So if a random number between 1 and MaxHits\*16 is higher than the
damage dealt, there's no damage.

In a PickAxe with 45 Hits it will mean that a number higher than 720
(45\*16) have to be given to force one point of damage.

Here's a damage formula to force damage: <spherescript> damage=\<eval
<maxhits>\*16\>,<src>,dam_physical </spherescript>


## Damage Flags

For a comprehensive list and descriptions of all available damage flags, see [Damage Flags](./Damage_Flags.md).

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)