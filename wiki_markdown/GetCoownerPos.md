## Description

This function returns the position of a given character UID in the co-owner list of a multi (house).

## Ficha

|              |                 |
|--------------|-----------------|
| **Function** | **GetCoownerPos** |
| **Type**     | Multi (House)   |
| **Access**   | Read-Only       |
| **Sphere X** | Yes             |

## Syntax

`<[multi].GetCoownerPos <char_uid>>`

## Parameters

-   `<char_uid>`: The UID of the character to find in the co-owner list.

## Return Values

-   Returns the 0-based position of the character in the list.
-   Returns -1 if the character is not found.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)