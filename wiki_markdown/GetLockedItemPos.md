## Description

This function returns the position of a given item UID in the locked down items list of a multi (house).

## Ficha

|              |                   |
|--------------|-------------------|
| **Function** | **GetLockedItemPos** |
| **Type**     | Multi (House)     |
| **Access**   | Read-Only         |
| **Sphere X** | Yes               |

## Syntax

`<[multi].GetLockedItemPos <item_uid>>`

## Parameters

-   `<item_uid>`: The UID of the item to find in the locked down items list.

## Return Values

-   Returns the 0-based position of the item in the list.
-   Returns -1 if the item is not found.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)