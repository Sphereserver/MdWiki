## Description

The `DEF` keyword is used to retrieve values specifically from `[DEFNAME]` sections within scripts. It no longer finds the numeric identifier of Resource `DEFNAME`s (like `ITEMDEF`, `CHARDEF`, `SPELL`); for that, `RESDEF` should be used.

## Ficha

|              |             |
|--------------|-------------|
| **Keyword**  | **DEF**     |
| **Type**     | Definition  |
| **Access**   | Read-Only   |
| **Sphere X** | Yes         |

## Syntax

`<DEF.defname>`

## Parameters

-   `defname`: The `defname` defined within a `[DEFNAME]` section.

## Examples

-   `<DEF.mt_walk>` returns the value associated with `mt_walk` in a `[DEFNAME]` section.

## Notes
- When Sphere encounters a keyword without a prefix, it searches in the following order: functions, `VAR`s, `RESDEF`s, `DEF`s. Using the `DEF` prefix will skip unnecessary lookups.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Keywords](./CategoryKeywords.md)