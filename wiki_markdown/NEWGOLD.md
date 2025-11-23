## Description

This function generates a specified amount of gold in a character's backpack.

## Ficha

|              |               |
|--------------|---------------|
| **Function** | **NEWGOLD**   |
| **Type**     | Character     |
| **Access**   | Write         |
| **Sphere X** | Yes           |

## Syntax

`[char].NEWGOLD <amount>[, <pile>]`

## Parameters

- `amount`: The amount of gold to generate.
- `pile`: (Optional) If `1`, the new gold is stacked on the existing pile in the pack. Otherwise, it's stacked in a new pile (default behavior).

## Notes
- The `NEWGOLD` function now has an upper limit of 25,000,000 for the amount of gold generated to prevent server hangs or crashes due to excessively high values.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)