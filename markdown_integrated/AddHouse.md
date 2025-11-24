# AddHouse

This function adds a house UID to the player's house list. If the player's current house count exceeds their limit, the house will be redeeded.

## Ficha

|              |               |
|--------------|---------------|
| **Function** | **AddHouse**  |
| **Type**     | Character     |
| **Access**   | Write         |
| **Sphere X** | Yes           |

## Syntax

`[char].AddHouse <house_uid>[, <house_priv>]`

## Parameters
- `house_uid`: The UID of the house to add.
- `house_priv`: (Optional) The privilege level for the house (e.g., `HP_OWNER`, `HP_COOWNER`). Defaults to `HP_OWNER`.

## Notes
- This function will remove the house from any previous owner and delete their keys for this house if the `house_uid` is already owned.
- If the house count exceeds `MaxHouses`, the house will be redeeded.

[Category: Functions](CategoryFunctions.md)
