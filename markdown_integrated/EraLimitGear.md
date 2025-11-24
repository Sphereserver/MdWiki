## Description

This property prevents NPCs from creating gear newer than the items from the expansion specified by its value.

## Ficha

|              |                    |
|--------------|--------------------|
| **Property** | **EraLimitGear**   |
| **Type**     | Character / ITEMDEF / CHARDEF |
| **Access**   | Read/Write         |
| **Sphere X** | Yes                |

## Notes
- Can be overridden by individual character properties.
- Setting `EraLimitGear` on a `CHARDEF` will prevent NPCs of that `CHARDEF` from creating gear newer than the specified expansion.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)