## Description

This property was previously a single flag for items that prevented both dropping and trading. It has since been split into separate flags for more granular control over these behaviors.

## Ficha

|              |             |
|--------------|-------------|
| **Property** | **NoDropTrade** |
| **Type**     | Item        |
| **Access**   | Read/Write (via separate flags) |
| **Sphere X** | Yes         |

## Notes
- This property has been split into separate flags, allowing for individual control over "no drop" and "no trade" functionalities. Each now has its own `CliLoc` (Client Localization) entries.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)