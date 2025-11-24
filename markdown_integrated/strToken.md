## Description

The `strToken` function tokenizes strings, unlike `explode`, it does not override commas, allowing strings with commas to be tokenized correctly.

## Ficha

|              |             |
|--------------|-------------|
| **Function** | **strToken** |
| **Type**     | String      |
| **Access**   | Read-Only   |
| **Sphere X** | Yes         |

## Syntax

`<strToken "string", "value", "separator">`

## Parameters

-   `"string"`: The input string to tokenize.
-   `"value"`: Specifies what to return:
    -   `0`: Returns the length of the tokenized string.
    -   `Number`: Returns a specific element of the string (0-based index).
    -   `startNumber-endNumber`: Returns a range of specific elements.
-   `"separator"`: The character to use as a separator for tokenizing (e.g., `" "` for space, `","` for comma, or any single character).

## Examples
- `<strToken "A.B.C", 0, .>` RETURNS 3
- `<strToken "A.B.C", 2, .>` RETURNS B
- `<strToken "A.B.C", 1-2, .>` RETURNS A.B
- `<strToken "A,B.C", 1, .>` RETURNS A,B

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)