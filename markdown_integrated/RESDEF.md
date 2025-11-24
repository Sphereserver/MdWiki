## Description

`RESDEF` is a keyword similar to `DEF`, but it specifically retrieves only the numeric identifier of Resource `DEFNAME`s (e.g., `ITEMDEF`, `CHARDEF`, `SPELL`). This is useful for obtaining the numerical ID of a resource directly.

## Ficha

|              |             |
|--------------|-------------|
| **Keyword**  | **RESDEF**  |
| **Type**     | Resource    |
| **Access**   | Read-Only   |
| **Sphere X** | Yes         |

## Syntax

`<RESDEF.defname>`

## Parameters

-   `defname`: The `DEFNAME` of the resource (e.g., `i_dagger`, `s_clumsy`).

## Examples

-   `<RESDEF.i_dagger>` returns the numeric ID of the `i_dagger` item.
-   `<RESDEF.s_clumsy>` returns the numeric ID of the `s_clumsy` spell.

## Notes
- This keyword was introduced because the `DEF` keyword no longer finds the numeric identifier of Resource `DEFNAME`s.
- When Sphere encounters a keyword without a prefix, it searches in the keyword lists in this order: functions, `VAR`s, `RESDEF`s, `DEF`s. Using the `RESDEF` prefix will skip unnecessary lookups.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Keywords](./CategoryKeywords.md)