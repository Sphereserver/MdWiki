## Description

This trigger fires for each item committed during the house design process. It provides granular control over individual components of a custom house.

## Ficha

|              |                       |
|--------------|-----------------------|
| **Trigger**  | **@HouseDesignCommitItem** |
| **Fires on** | Multis (t_multi_custom) |
| **Sphere X** | Yes                   |

## Arguments

-   `local.id`: ID of the item being committed.
-   `local.p.x`: X location of the item.
-   `local.p.y`: Y location of the item.
-   `local.p.z`: Z location of the item.
-   `local.visible`: 0 or 1 (0 for non-visible items like doors and signs).

## Return Values

-   `return false`: Removes this item from the commit.
-   If not `return false`, `local.MaxZ` will check the `P.Z` value of the item and update it if it's higher than the old one.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Triggers](./CategoryTriggers.md)