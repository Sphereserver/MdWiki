## Description

This function returns the position of a given character UID in the ban list of a multi (house).

## Ficha

|              |                 |
|--------------|-----------------|
| **Function** | **GetBanPos** |
| **Type**     | Multi (House)   |
| **Access**   | Read-Only       |
| **Sphere X** | Yes             |

## Syntax

`<[multi].GetBanPos <char_uid>>`

## Parameters

-   `<char_uid>`: The UID of the character to find in the ban list.

## Return Values

-   Returns the 0-based position of the character in the list.
-   Returns -1 if the character is not found.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)