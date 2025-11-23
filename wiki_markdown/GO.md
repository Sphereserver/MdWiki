## Description

This command teleports the character to the specified location. It now accepts an optional map index as a second argument, allowing teleportation to places with the same name on different maps.

## Ficha

|              |               |
|--------------|---------------|
| **Command**  | **GO**        |
| **Type**     | Character     |
| **Access**   | Write-Only    |
| **Sphere X** | Yes           |

## Syntax

`[char].GO <location>[, <map_index>]`

## Parameters

-   `<location>`: The name or coordinates of the destination.
-   `<map_index>`: (Optional) The index of the map where the location is defined (e.g., `0` for map0, `1` for map1).

## Examples
- `GO britain, 0` teleports to Britain in map0.
- `GO britain, 1` teleports to Britain in map1 (if that region is defined in the map script file).

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Commands](./CategoryCommands.md)