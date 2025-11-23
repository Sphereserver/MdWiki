## Description

This function retrieves the resource index from a `defname`, ignoring the resource type (Chardef, Spell, Itemdef, Template...) bits.

## Ficha

|              |                    |
|--------------|--------------------|
| **Function** | **RESOURCEINDEX**  |
| **Type**     | Defname            |
| **Access**   | Read-Only          |
| **Sphere X** | Yes                |

## Syntax

`<RESOURCEINDEX <defname>>`

## Parameters

-   `<defname>`: The `defname` of the resource.

## Examples

-   `<RESOURCEINDEX s_clumsy>` returns `1`, which is the spell number (ID).

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)