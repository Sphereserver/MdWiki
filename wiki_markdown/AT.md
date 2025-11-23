## Description

The `AT*` keyword (e.g., `AT.0`) is used to access an object at a specific position within a list or collection and perform read, write, or execute operations on it. It works with a numerical index to retrieve the object.

## Ficha

|              |             |
|--------------|-------------|
| **Keyword**  | **AT***     |
| **Access**   | Read/Write/Execute |
| **Sphere X** | Yes         |

## Syntax

`[collection].AT.n.<property/function>`
`[collection].AT.X`
`[collection].AT.Y`
`[collection].AT.Z`

## Parameters

- `n`: The zero-based index of the object within the collection.

## Example

- `SPAWN.AT.0.REMOVE` - Removes the first spawned object.
- `SYSMESSAGE <SPAWN.AT.0.STR>` - Displays the strength of the first spawned object.
- `SYSMESSAGE <SPAWN.AT.X>` - Displays the X coordinate of the referenced object.
- `SPAWN.AT.Y = 123` - Sets the Y coordinate of the referenced object to 123.

## Notes
- This keyword has been changed to `r_GetRef` internally, allowing it to find objects by position within collections.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Keywords](./CategoryKeywords.md)