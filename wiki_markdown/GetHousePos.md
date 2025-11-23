# GetHousePos

This function returns the position of a given house UID in the player's house list.

## Ficha

|              |                 |
|--------------|-----------------|
| **Function** | **GetHousePos** |
| **Type**     | Character       |
| **Access**   | Read-Only       |
| **Sphere X** | Yes             |

## Syntax

`[char].GetHousePos <house_uid>`

## Parameters
- `house_uid`: The UID of the house to search for in the list.

## Return Value
- Returns the position of the house in the list (0-based index).
- Returns `-1` if the house UID is not found in the list.

[Category: Functions](CategoryFunctions.md)
