## Description

This function adds a house to a player's list of owned houses.

## Ficha

|              |               |
|--------------|---------------|
| **Function** | **AddHouse**  |
| **Type**     | Character     |
| **Access**   | Write-Only    |
| **Sphere X** | Yes           |

## Syntax

`[char].AddHouse <uid>`
`[char].AddHouse <house_uid>, <house_priv>`

## Parameters

-   `<uid>`: The UID of the house to add.
-   `<house_priv>`: (Optional) The privilege level for the house (e.g., `HP_OWNER`, `HP_COOWNER`). Defaults to `HP_OWNER`.

## Notes
- If the player's current count of houses exceeds their `MaxHouses` limit, the house will be redeeded.
- Calling `AddHouse <house_uid>, HP_COOWNER` will replace the current privilege with the new one.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)