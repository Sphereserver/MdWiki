## Description

This property prevents characters (players and NPCs) from having properties newer than the ones from the expansion specified by its value.

## Ficha

|              |                    |
|--------------|--------------------|
| **Property** | **EraLimitProps**  |
| **Type**     | Character / ITEMDEF / CHARDEF |
| **Access**   | Read/Write         |
| **Sphere X** | Yes                |

## Notes
- Can be overridden by individual character properties.
- Setting `EraLimitProps` on a `CHARDEF` will prevent NPCs of that `CHARDEF` from having properties newer than the specified expansion.
- If you create characters with a low `EraLimitProps` and then change it to a higher value, you may need to recreate the characters to make them load the matching properties.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)