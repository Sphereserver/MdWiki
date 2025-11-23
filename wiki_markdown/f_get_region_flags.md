## Description

This function returns the region flags from a specified point in the world.

## Ficha

|              |             |
|--------------|-------------|
| **Function** | **f_get_region_flags** |
| **Type**     | Global      |
| **Access**   | Read        |
| **Sphere X** | Yes         |

## Syntax

`f_get_region_flags(x, y, z)`

## Parameters

- `x`: The X coordinate of the point.
- `y`: The Y coordinate of the point.
- `z`: The Z coordinate of the point.

## Example

`VAR.RegionFlags = f_get_region_flags(100, 100, 0)` - Returns the region flags at coordinates (100, 100, 0).

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)