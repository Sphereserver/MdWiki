## Description

This function revokes any `House_Priv` to a specified character on a multi (house or ship), with the exception of `HP_GUILD`.

## Ficha

|              |               |
|--------------|---------------|
| **Function** | **RevokePrivs** |
| **Type**     | Multi (House/Ship) |
| **Access**   | Write-Only    |
| **Sphere X** | Yes           |

## Syntax

`[multi].RevokePrivs <char_uid>`

## Parameters

-   `<char_uid>`: The UID of the character whose privileges will be revoked.

## Notes
- `HP_GUILD` privileges are not revoked by this function.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)