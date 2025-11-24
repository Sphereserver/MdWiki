## Description

This document defines properties and functions related to secured containers within a multi (house).

## Ficha

|              |               |
|--------------|---------------|
| **Property** | **SecuredContainers** |
| **Type**     | Multi (House) |
| **Access**   | Read-Only     |
| **Sphere X** | Yes           |

## Syntax

`<[multi].SecuredContainers>`

## Notes
- The `@Destroy` trigger is no longer strictly needed for deleting items from the house list; pointers are now added back on `CItem` and `CItemStone` to handle this.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)