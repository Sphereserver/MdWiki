## Description

`TDATA4` is a property used to store various data in items. For containers, it specifically stores the maximum X and Y coordinates for items placed inside.

## Ficha

|              |             |
|--------------|-------------|
| **Property** | **TDATA4**  |
| **Type**     | Item        |
| **Access**   | Read/Write  |
| **Sphere X** | Yes         |

## Notes
- For items of type `t_container`, `TDATA4` stores the maximum X (first 16 bits) and maximum Y (last 16 bits) of an object placed inside.
- For `t_spellbook` items, `TDATA4` is now used to store the maximum spells.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)