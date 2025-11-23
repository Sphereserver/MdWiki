## Description

This function adds a ship to a player's list of owned ships.

## Ficha

|              |               |
|--------------|---------------|
| **Function** | **AddShip**   |
| **Type**     | Character     |
| **Access**   | Write-Only    |
| **Sphere X** | Yes           |

## Syntax

`[char].AddShip <uid>`
`[char].AddShip <ship_uid>, <house_priv>`

## Parameters

-   `<uid>`: The UID of the ship to add.
-   `<ship_priv>`: (Optional) The privilege level for the ship (e.g., `HP_OWNER`, `HP_COOWNER`). Defaults to `HP_OWNER`.

## Notes
- If the player's current count of ships exceeds their `MaxShips` limit, the ship will be redeeded.
- Calling `AddShip <ship_uid>, HP_COOWNER` will replace the current privilege with the new one.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)