## Description

This property prevents NPCs from creating loot newer than the items from the expansion specified by its value.

## Ficha

|              |                    |
|--------------|--------------------|
| **Property** | **EraLimitLoot**   |
| **Type**     | Character / ITEMDEF / CHARDEF |
| **Access**   | Read/Write         |
| **Sphere X** | Yes                |

## Notes
- Can be overridden by individual character properties.
- Setting `EraLimitLoot` on a `CHARDEF` will prevent NPCs of that `CHARDEF` from creating loot newer than the specified expansion.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)