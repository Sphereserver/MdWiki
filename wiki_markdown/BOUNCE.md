## Description

This function moves a specified item into the character's backpack, triggering a message indicating the item has been placed in the pack.

## Ficha

|              |             |
|--------------|-------------|
| **Function** | **BOUNCE**  |
| **Type**     | Item        |
| **Access**   | Write       |
| **Sphere X** | Yes         |

## Syntax

`[item].BOUNCE`

## Notes
- `BOUNCE` now calls triggers `@DropOn_Self` and `@ItemDropOn_Self` on the character's backpack. If a `RETURN 1` is performed in these triggers and a new `CONT` has not been set via scripts, the item is dropped on the ground; otherwise, it is left in the new `CONT`.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)