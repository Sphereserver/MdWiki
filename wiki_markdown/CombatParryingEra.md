## Description

This `ini` flag controls the parrying behavior in combat, offering different formulas and capabilities based on its value.

## Ficha

|              |                     |
|--------------|---------------------|
| **INI Flag** | **CombatParryingEra** |
| **Sphere X** | Yes                 |

## Flags

This flag is a bitmask, and you can combine its values.

-   `01`: Uses the pre-SE parrying chance formula (does not use the Bushido skill). Mutually exclusive with `02` flag.
-   `02`: Uses the SE parrying chance formula (uses the Bushido skill). Mutually exclusive with `01` flag.
-   `010`: Allows parrying with a shield.
-   `020`: Allows parrying with a one-handed weapon without a shield.
-   `040`: Allows parrying with two-handed weapons.
-   `080`: Enables the old AR parrying formula: `Displayed AR = ((Parrying Skill * Base AR of Shield) ÷ 200) + 1`. Maximum AR is `Base AR of Shield / 2`.
    -   Requires `ARMOR` value of shields to be uncommented.
    -   Works only with `Combat Elemental Engine` disabled.
    -   Updates character armor only when `Parrying` skill changes or shield is equipped/unequipped.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Ini Settings](./CategoryIni_Settings.md)