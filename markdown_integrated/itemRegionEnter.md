## Description

This trigger is a homologue to `@RegionEnter`, specifically designed for ships. It fires when a ship enters a region.

## Ficha

|              |                    |
|--------------|--------------------|
| **Trigger**  | **@itemRegionEnter** |
| **Fires on** | Ships              |
| **Sphere X** | Yes                |

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [region](./Regions.md) being entered. |
| [I](./I.md) | The [ship](./Ship.md) entering the region. |
| [SRC](./SRC.md) | The [ship](./Ship.md) entering the region. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                 |
|------------------|-------------------------------------------------|
| **Return Value** | **Description**                                 |
| 1                | Prevents the ship from entering the region.     |

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Triggers](./CategoryTriggers.md)