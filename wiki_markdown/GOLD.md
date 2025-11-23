## Description

This property gets or sets the amount of gold a character has.

## Ficha

|              |             |
|--------------|-------------|
| **Property** | **GOLD**    |
| **Type**     | Character   |
| **Access**   | Read/Write  |
| **Sphere X** | Yes         |

## Notes
- The `GOLD` property now has an upper limit of 25,000,000 to prevent server hangs or crashes due to excessively high values.
- When `FEATURE_TOL_VIRTUALGOLD` is enabled, `GOLD` and `<GOLD>` will function as `VirtualGold` and `<VirtualGold>`.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)