## Description

This trigger fires to check various conditions before a combat hit is processed. It allows for modification of combat behavior, such as disabling `Swing_NoRange` or continuing default combat code.

## Ficha

|              |             |
|--------------|-------------|
| **Trigger**  | **@HitCheck** |
| **Fires on** | Characters  |
| **Sphere X** | Yes         |

## Arguments

-   `LOCAL.Swing_NoRange`:
    -   `-1`: Force disables the `Swing_NoRange` behavior for the current hit.
    -   `0`: Leaves `Swing_NoRange` dependent on the `COMBAT_SWING_NORANGE` ini CombatFlag.
    -   `1`: Force enables the `Swing_NoRange` behavior.

## Return Values

-   `RETURN -2`: Continues the execution of the default combat code. Useful for modifying `LOCAL.Swing_NoRange` without altering other combat logic.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Triggers](./CategoryTriggers.md)