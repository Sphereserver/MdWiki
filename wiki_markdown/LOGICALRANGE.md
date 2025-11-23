## Description

This function returns a random number within a specified range, supporting reverse ranges (where the minimum value is greater than the maximum).

## Ficha

|              |                 |
|--------------|-----------------|
| **Function** | **SERV.LOGICALRANGE** |
| **Type**     | Server          |
| **Access**   | Read            |
| **Sphere X** | Yes             |

## Syntax

`SERV.LOGICALRANGE(min, max)`

## Parameters

- `min`: The minimum value of the range.
- `max`: The maximum value of the range.

## Example

`VAR.RandomValue = SERV.LOGICALRANGE(10, 50)` - Returns a random number between 10 and 50.
`VAR.RandomValue = SERV.LOGICALRANGE(50, 10)` - Returns a random number between 10 and 50 (reverse range).

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)