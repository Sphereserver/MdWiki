## Description

This function validates a string against a bcrypt hash.

## Ficha

|              |                   |
|--------------|-------------------|
| **Function** | **BCRYPTVALIDATE** |
| **Type**     | String            |
| **Access**   | Read-Only         |
| **Sphere X** | Yes               |

## Syntax

`<BCRYPTVALIDATE string, hash>`

## Parameters

-   `string`: The plain text string to validate.
-   `hash`: The bcrypt hash to compare against.

## Return Values

-   Returns `1` if the hash matches the string, otherwise `0`.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)