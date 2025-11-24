## Description

This function works like a random `{ }` range, but for strings.

## Ficha

|              |                    |
|--------------|--------------------|
| **Function** | **STRRANDRANGE**   |
| **Type**     | String             |
| **Access**   | Read-Only          |
| **Sphere X** | Yes                |

## Syntax

`<STRRANDRANGE "string1" weight1 "string2" weight2 ...>`

## Parameters

-   `"string"`: The string value to choose.
-   `weight`: The weight (chance) of choosing this string.

## Examples

-   `<STRRANDRANGE "boots" 1 "shoes" 1 "watermelons" 1>` returns one of the three strings randomly.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)