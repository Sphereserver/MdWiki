## Description

`TDATA3` is a property used to store various data in items. For containers, it specifically stores the minimum X and Y coordinates for items placed inside.

## Ficha

|              |             |
|--------------|-------------|
| **Property** | **TDATA3**  |
| **Type**     | Item        |
| **Access**   | Read/Write  |
| **Sphere X** | Yes         |

## Notes
- For items of type `t_container`, `TDATA3` stores the minimum X (first 16 bits) and minimum Y (last 16 bits) of an object placed inside.
- For `t_spellbook` items, `TDATA3` is now used to store the spell offset.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)