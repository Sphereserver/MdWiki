## Description

This property returns the total count of locked down items for a multi (house).

## Ficha

|              |               |
|--------------|---------------|
| **Property** | **Lockdowns** |
| **Type**     | Multi (House) |
| **Access**   | Read-Only     |
| **Sphere X** | Yes           |

## Syntax

`<[multi].Lockdowns>`

## Notes
- The `@Destroy` trigger is no longer strictly needed for deleting items from the house list; pointers are now added back on `CItem` and `CItemStone` to handle this.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)