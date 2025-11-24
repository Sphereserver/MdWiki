## Description

This method allows control over payment values using a dedicated trigger.

## Ficha

|              |               |
|--------------|---------------|
| **Method**   | **PayGold()** |
| **Type**     | Character     |
| **Access**   | Write         |
| **Sphere X** | Yes           |

## Syntax

`[char].PayGold()`

## Trigger

The `ON=@PayGold` trigger fires when this method is called.

### Arguments for `@PayGold`

- `Argn1`: Gold to pay.
- `Argn2`: Payment type (0 = Train, 1 = Buy, 2 = Hire).
- `src`: The NPC receiving the money.
- `argo` (if any): The stack of gold used to pay (e.g., for training).

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)